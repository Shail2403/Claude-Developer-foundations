---
name: state_name_format
description: State name formatting rule - first char capital, rest lowercase
metadata:
  type: feedback
---

## State Name Formatting

**Rule**: State names must follow "Capitalized" format - first character uppercase, rest lowercase.

**Examples**:
- `Maharashtra` (correct)
- `Delhi` (correct)
- `Tamil Nadu` (correct - each word capitalized)
- `maharashtra` (becomes `Maharashtra`)
- `DELHI` (becomes `Delhi`)
- `tamilnadu` (becomes `Tamilnadu`)

**Why**: User explicitly requested: "State name first char should be always capital and rest non capital"

**How to apply**: 
- Use `str.capitalize()` in the API to normalize incoming state names
- Always store and return state names in this format
- API endpoints accept any casing and auto-normalize before lookup/storage
- This ensures consistent state name representation across the API
