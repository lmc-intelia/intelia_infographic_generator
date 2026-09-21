---
type: Module
title: prepare
description: "Graphify community 41: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:36:43Z" }
stale_after: "2026-10-05T02:36:43Z"
source_commit: 6de363a7f637fc903d43af9cfa93954eafdc5fc9
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T12:34:05+10:00", digest: 3579c45b24e4283a }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member() (skills/iig3d/scripts/iig3d.py:L105)
- .resolve_ref() (skills/iig3d/scripts/iig3d.py:L118)
- A catalogue ref named by the user: `<member>/<id|file|stem>`, a… (skills/iig3d/scripts/iig3d.py:L119)
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1285)
- prepare() (skills/iig3d/scripts/iig3d.py:L1305)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1306)
- cmd_route() (skills/iig3d/scripts/iig3d.py:L1358)
- cmd_refs() (skills/iig3d/scripts/iig3d.py:L1365)
- The refs a render would pass, plus every catalogue ref of the member with its… (skills/iig3d/scripts/iig3d.py:L1366)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1380)
- cmd_check() (skills/iig3d/scripts/iig3d.py:L1385)
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
- slugify() (skills/iig3d/scripts/iig3d.py:L622)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [select_refs](/modules/select-refs.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
