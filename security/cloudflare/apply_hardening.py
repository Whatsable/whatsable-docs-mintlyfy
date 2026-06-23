#!/usr/bin/env python3
"""Permanently disable Cloudflare Web Analytics (RUM) for docs.whatsable.app.

Applies two durable controls:
  1. Configuration rule (disable_rum) — blocks beacon injection even if Web Analytics is re-enabled
  2. RUM site API update — sets auto_install=false for the docs hostname

Requires: CLOUDFLARE_API_TOKEN with Zone Config Rules Edit (+ Account Analytics Read)
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

API_BASE = "https://api.cloudflare.com/client/v4"
ZONE_NAME = os.environ.get("ZONE_NAME", "whatsable.app")
DOCS_HOST = os.environ.get("DOCS_HOST", "docs.whatsable.app")
RULE_REF = "disable_rum_docs_whatsable"


def api(method: str, path: str, body: dict | None = None) -> dict:
    token = os.environ.get("CLOUDFLARE_API_TOKEN")
    if not token:
        print(
            "ERROR: Set CLOUDFLARE_API_TOKEN (Zone > Config Rules > Edit).\n"
            "Create token: https://dash.cloudflare.com/profile/api-tokens",
            file=sys.stderr,
        )
        sys.exit(1)

    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode()
        print(f"API error {exc.code} {method} {path}:\n{payload}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    print("==> Verifying API token...")
    api("GET", "/user/tokens/verify")

    accounts = api("GET", "/accounts?per_page=50").get("result") or []
    if not accounts:
        print("ERROR: No Cloudflare accounts found for this token.", file=sys.stderr)
        sys.exit(1)
    account_id = accounts[0]["id"]
    print(f"    Account: {account_id}")

    print(f"==> Resolving zone {ZONE_NAME}...")
    zones = api("GET", f"/zones?name={ZONE_NAME}").get("result") or []
    if not zones:
        print(f"ERROR: Zone '{ZONE_NAME}' not found.", file=sys.stderr)
        sys.exit(1)
    zone_id = zones[0]["id"]
    print(f"    Zone ID: {zone_id}")

    print(f"==> Disabling RUM auto-install for {DOCS_HOST}...")
    try:
        sites = api("GET", f"/accounts/{account_id}/rum/site_info/list").get("result") or []
    except SystemExit:
        sites = []
    matched = [s for s in sites if s.get("host") == DOCS_HOST]
    if not matched:
        print(f"    No RUM site entry for {DOCS_HOST} (OK — may already be removed)")
    for site in matched:
        site_id = site.get("site_tag") or site.get("site_id")
        if not site_id:
            continue
        api(
            "PUT",
            f"/accounts/{account_id}/rum/site_info/{site_id}",
            {
                "auto_install": False,
                "enabled": False,
                "host": site.get("host", DOCS_HOST),
                "zone_tag": site.get("zone_tag") or zone_id,
            },
        )
        print(f"    Disabled RUM site {site_id}")

    print(f"==> Adding configuration rule disable_rum for {DOCS_HOST}...")
    new_rule = {
        "ref": RULE_REF,
        "expression": f'(http.host eq "{DOCS_HOST}")',
        "description": "Disable Cloudflare Web Analytics (RUM) — prevents beacon.min.js injection on docs",
        "action": "set_config",
        "action_parameters": {"disable_rum": True},
        "enabled": True,
    }

    rulesets = api("GET", f"/zones/{zone_id}/rulesets").get("result") or []
    config_ruleset = next((r for r in rulesets if r.get("phase") == "http_config_settings"), None)

    if config_ruleset is None:
        result = api(
            "POST",
            f"/zones/{zone_id}/rulesets",
            {
                "name": "default",
                "kind": "zone",
                "phase": "http_config_settings",
                "rules": [new_rule],
            },
        )
    else:
        ruleset_id = config_ruleset["id"]
        existing = api("GET", f"/zones/{zone_id}/rulesets/{ruleset_id}")["result"]
        rules = [r for r in (existing.get("rules") or []) if r.get("ref") != RULE_REF]
        rules.insert(0, new_rule)
        result = api("PUT", f"/zones/{zone_id}/rulesets/{ruleset_id}", {"rules": rules})

    if not result.get("success"):
        print(f"ERROR: Failed to apply configuration rule: {result}", file=sys.stderr)
        sys.exit(1)
    print("    Configuration rule applied.")

    print("\n==> Verifying live HTML...")
    verify_url = f"https://{DOCS_HOST}/guides/notifyer-system/monday-overview"
    with urllib.request.urlopen(verify_url) as resp:
        html = resp.read().decode(errors="replace")
    markers = ("cloudflareinsights", "data-cf-beacon", "beacon.min.js")
    if any(m in html for m in markers):
        print(
            "WARN: Beacon still in HTML — wait 1–2 min for propagation, or disable manually:\n"
            "  Dashboard → Analytics & logs → Web Analytics → Disable",
            file=sys.stderr,
        )
        sys.exit(1)

    print("OK: Permanent hardening applied. Re-scan with Burp to confirm 2.1 / 2.2 are gone.")


if __name__ == "__main__":
    main()
