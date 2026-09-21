---
type: Module
title: prepare
description: "Graphify community 39: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:12:49Z" }
stale_after: "2026-10-05T05:12:49Z"
source_commit: 0dac1771abb0a241b787b37f99663e8da1c9a6f4
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:06:12+10:00", digest: 755d0eccdd75a015 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member() (skills/iig3d/scripts/iig3d.py:L108)
- .resolve_ref() (skills/iig3d/scripts/iig3d.py:L121)
- A catalogue ref named by the user: `<member>/<id|file|stem>`, a… (skills/iig3d/scripts/iig3d.py:L122)
- .pin_token() (skills/iig3d/scripts/iig3d.py:L142)
- _split_vars() (skills/iig3d/scripts/iig3d.py:L1654)
- prepare() (skills/iig3d/scripts/iig3d.py:L1674)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L1675)
- cmd_route() (skills/iig3d/scripts/iig3d.py:L1735)
- cmd_refs() (skills/iig3d/scripts/iig3d.py:L1742)
- The refs a render would pass, plus every catalogue ref of the member with its… (skills/iig3d/scripts/iig3d.py:L1743)
- cmd_palette() (skills/iig3d/scripts/iig3d.py:L1774)
- split_style() (skills/iig3d/scripts/iig3d.py:L240)
- (style, pin) after reading a ref name out of `style`: with `layout` naming a… (skills/iig3d/scripts/iig3d.py:L241)
- select_refs() (skills/iig3d/scripts/iig3d.py:L479)
- Style refs as paths (see pick_style_refs), then the icon sheet, then user refs,… (skills/iig3d/scripts/iig3d.py:L488)
- Colour (skills/iig3d/scripts/iig3d.py:L521)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L525)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L569)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L570)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L612)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [resolve_icons](/modules/resolve-icons.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
