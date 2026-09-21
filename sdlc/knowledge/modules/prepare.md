---
type: Module
title: prepare
description: "Graphify community 41: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:47:44Z" }
stale_after: "2026-10-05T02:47:44Z"
source_commit: 2285898e55a2ed6720d292c1eb4bd34a1f6f1690
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T12:47:39+10:00", digest: 67114822a3e7b1d9 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1287)
- prepare() (skills/iig3d/scripts/iig3d.py:L1307)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1308)
- cmd_route() (skills/iig3d/scripts/iig3d.py:L1360)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1382)
- .pin_token() (skills/iig3d/scripts/iig3d.py:L139)
- split_style() (skills/iig3d/scripts/iig3d.py:L237)
- (style, pin) after reading a ref name out of `style`: with `layout` naming a… (skills/iig3d/scripts/iig3d.py:L238)
- Colour (skills/iig3d/scripts/iig3d.py:L509)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L513)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L550)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L551)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L557)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L558)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L600)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
