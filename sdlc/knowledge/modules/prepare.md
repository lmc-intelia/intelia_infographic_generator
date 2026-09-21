---
type: Module
title: prepare
description: "Graphify community 39: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:49:58Z" }
stale_after: "2026-10-05T04:49:58Z"
source_commit: 6197c1b39e2b704463349bd9e1b4033182bc40ce
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T14:48:56+10:00", digest: 05b5aa06590e0558 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .pin_token() (skills/iig3d/scripts/iig3d.py:L142)
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1639)
- prepare() (skills/iig3d/scripts/iig3d.py:L1659)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1660)
- cmd_route() (skills/iig3d/scripts/iig3d.py:L1719)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1758)
- cmd_check() (skills/iig3d/scripts/iig3d.py:L1763)
- split_style() (skills/iig3d/scripts/iig3d.py:L240)
- (style, pin) after reading a ref name out of `style`: with `layout` naming a… (skills/iig3d/scripts/iig3d.py:L241)
- Colour (skills/iig3d/scripts/iig3d.py:L517)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L521)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L558)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L559)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L565)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L566)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L608)
- slugify() (skills/iig3d/scripts/iig3d.py:L949)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [resolve_icons](/modules/resolve-icons.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
