#!/usr/bin/env bash
# Quick check that docs.whatsable.app is free of Cloudflare RUM beacon injection.
set -euo pipefail

DOCS_HOST="${DOCS_HOST:-docs.whatsable.app}"
PATH_TO_CHECK="${PATH_TO_CHECK:-/guides/notifyer-system/monday-overview}"
URL="https://${DOCS_HOST}${PATH_TO_CHECK}"

echo "Checking ${URL} ..."

html="$(curl -fsSL "$URL")"

if echo "$html" | grep -qE 'cloudflareinsights|data-cf-beacon|beacon\.min\.js'; then
  echo "FAIL: Cloudflare Web Analytics beacon detected."
  echo "Run: ./security/cloudflare/apply-hardening.sh"
  exit 1
fi

echo "PASS: No Cloudflare beacon in HTML."

if curl -fsSI "$URL" | grep -qi 'content-security-policy'; then
  echo "PASS: CSP header present."
else
  echo "INFO: No CSP header (Mintlify default may still apply)."
fi
