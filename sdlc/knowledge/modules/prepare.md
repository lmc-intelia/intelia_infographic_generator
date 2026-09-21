---
type: Module
title: prepare
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:30:03Z" }
stale_after: "2026-10-05T05:30:03Z"
source_commit: fae00c698effe61c7083ae8264ab6a14d68f8f09
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:29:58+10:00", digest: 4b4238bdfa8f4e38 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .pin_token() (skills/iig3d/scripts/iig3d.py:L142)
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1746)
- prepare() (skills/iig3d/scripts/iig3d.py:L1766)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1767)
- cmd_route() (skills/iig3d/scripts/iig3d.py:L1828)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1867)
- cmd_check() (skills/iig3d/scripts/iig3d.py:L1872)
- split_style() (skills/iig3d/scripts/iig3d.py:L240)
- (style, pin) after reading a ref name out of `style`: with `layout` naming a… (skills/iig3d/scripts/iig3d.py:L241)
- Colour (skills/iig3d/scripts/iig3d.py:L523)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L527)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L564)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L565)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L571)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L572)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L614)
- slugify() (skills/iig3d/scripts/iig3d.py:L974)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [resolve_icons](/modules/resolve-icons.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
