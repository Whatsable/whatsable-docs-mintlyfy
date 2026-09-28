# Support WhatsApp Number Swap — Audit Report

**Date:** 2026-09-28
**Requested change:** Replace the old French support number with the new US number across all MDX/MD/JSON/config/theme/footer/navbar/`sameAs`/`contactPoint` occurrences in this repo (`whatsable-docs-mintlyfy`, live at `docs.whatsable.app`).

## Target numbers

| | Old (French) | New (US) |
|---|---|---|
| Display | `+33 7 66 86 40 02` | `+1 555-966-5903` |
| E.164 | `+33766864002` | `+15559665903` |
| wa.me | `wa.me/+33766864002`, `wa.me/33766864002` | `https://wa.me/15559665903` |
| tel: | `tel:+33766864002` | `tel:+15559665903` |

Also checked for a leftover blocked US number: `+13476861478` / `+1 347-686-1478`.

## Result: zero occurrences found

An exhaustive search of the working tree (all tracked and untracked files, `.git` excluded) and of the **entire git history across every local and remote branch** found **no occurrences** of any of the following, in any format:

- `+33 7 66 86 40 02`, `+33766864002`, `33766864002`, `33 7 66 86 40 02` (and variants with `-`/`.` separators)
- `wa.me/+33766864002`, `wa.me/33766864002`
- `tel:+33766864002`
- `+13476861478` / `+1 347-686-1478`

Commands used (from repo root, `main` @ `fc8e2e0a`):

```bash
rg -n --hidden -g '!.git' '\+?33\s*7\s*66\s*86\s*40\s*02' -i
rg -n --hidden -g '!.git' '33[\s\-\.]?7[\s\-\.]?66[\s\-\.]?86[\s\-\.]?40[\s\-\.]?02'
rg -n --hidden -g '!.git' 'wa\.me/\+?33766864002'
rg -n --hidden -g '!.git' 'tel:\+?33766864002'
rg -n --hidden -g '!.git' '1[\s\-\.]?347[\s\-\.]?686[\s\-\.]?1478'
git log --all -p -S'766864002'
git log --all -p -S'7 66 86 40 02'
git log --all -p -S'3476861478'
```

All returned zero matches.

## Residual search (as requested, per "if zero hits, still search wa.me / support phone / contactPoint / telephone")

| Pattern | Files with matches | Notes |
|---|---|---|
| `wa\.me` (case-insensitive) | `guides/notifyer-system/api/incoming-message.mdx` | One hit: a sample webhook payload with an unrelated example WhatsApp link (`https://wa.me/50660039931`, Costa Rica) inside sample JSON body text — not a support/contact number, left unchanged. |
| `tel:` | none | — |
| `contactPoint` / `telephone` / `sameAs` (JSON-LD-style keys) | none | No structured-data contact block exists in `docs.json` or anywhere else. |
| `\bphone\b` | 39 files | All are generic references to "phone number" as an API field/concept (e.g. `phone_number` request params, "verify the phone number format"), not the support contact number. |
| `\+33` | only inside `images/*.svg` | False positives from SVG path/coordinate data, not phone numbers. |
| `\+1[ -.]?[0-9]` | 25 files | All are generic **placeholder** example numbers used in API docs (`+1234567890`, `+14155550123`) to illustrate the E.164 format — not the support number, and not the blocked `+13476861478` number either. Left unchanged per "do not invent numbers elsewhere." |
| `docs.json` navbar/footer/socials | — | No phone/WhatsApp contact field present (`footer.socials` only has `x`, `github`, `linkedin`; `navbar.primary` links to a pricing page, no `tel:`/`wa.me`). |

## Conclusion

No French support number (`+33 7 66 86 40 02` in any format) or leftover blocked US number (`+13476861478`) exists anywhere in this repository's current content or history. **No files required editing.** The generic placeholder numbers found in API examples (`+1234567890`, `+14155550123`) are illustrative format examples unrelated to the support contact number and were intentionally left untouched.

If the actual support WhatsApp number is meant to be added to these docs for the first time (rather than swapped), please confirm where it should appear (e.g. `docs.json` footer/navbar, a dedicated "Contact support" section, or JSON-LD `contactPoint`/`sameAs` metadata), and it will be added using the new US number:

- Display: `+1 555-966-5903`
- E.164: `+15559665903`
- wa.me: `https://wa.me/15559665903`
- tel: `tel:+15559665903`
