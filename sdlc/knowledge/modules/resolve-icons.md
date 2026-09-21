---
type: Module
title: resolve_icons
description: "Graphify community 49: skills/iig3d/scripts/iig3d.py"
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
- cmd_icons() (skills/iig3d/scripts/iig3d.py:L1741)
- Name search and text-based suggestion in one call, so Claude can pick or verify… (skills/iig3d/scripts/iig3d.py:L1742)
- parse_icon() (skills/iig3d/scripts/iig3d.py:L622)
- (pack, name) for `pack:name`, or for `name` when a default pack is set;… (skills/iig3d/scripts/iig3d.py:L623)
- icon_svg() (skills/iig3d/scripts/iig3d.py:L637)
- The cached SVG under icons/<pack>/<name>.svg, fetched from Iconify on a miss… (skills/iig3d/scripts/iig3d.py:L638)
- render_icon() (skills/iig3d/scripts/iig3d.py:L658)
- Rasterise one SVG to an RGBA PIL image of `size` px; currentColor renders black. (skills/iig3d/scripts/iig3d.py:L659)
- spec_icons() (skills/iig3d/scripts/iig3d.py:L667)
- [{index, label, pack, name, via: spec}] for every item whose icon names a pack… (skills/iig3d/scripts/iig3d.py:L668)
- search_icons() (skills/iig3d/scripts/iig3d.py:L811)
- Glyph names in `pack` whose Iconify name matches `query`; empty when fetching… (skills/iig3d/scripts/iig3d.py:L812)
- _words() (skills/iig3d/scripts/iig3d.py:L826)
- suggest_icon() (skills/iig3d/scripts/iig3d.py:L835)
- (name, via) for an item from its text: the synonym table on the label, then the… (skills/iig3d/scripts/iig3d.py:L836)
- resolve_icons() (skills/iig3d/scripts/iig3d.py:L854)
- Every item's glyph: the spec's own name when it exists (a missing name falls… (skills/iig3d/scripts/iig3d.py:L855)
- build_icon_sheet() (skills/iig3d/scripts/iig3d.py:L886)
- One white PNG contact sheet: each item's glyph in black with its number and… (skills/iig3d/scripts/iig3d.py:L887)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
