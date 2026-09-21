---
type: Module
title: build_icon_sheet
description: "Graphify community 49: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:30:53Z" }
stale_after: "2026-10-05T04:30:53Z"
source_commit: 71c08107aa2dfcc1db57f7b3771bfd7713d219d0
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T14:30:49+10:00", digest: fe9bead68c7c4cae }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- parse_icon() (skills/iig3d/scripts/iig3d.py:L621)
- (pack, name) for `pack:name`, or for `name` when a default pack is set;… (skills/iig3d/scripts/iig3d.py:L622)
- icon_svg() (skills/iig3d/scripts/iig3d.py:L636)
- The cached SVG under icons/<pack>/<name>.svg, fetched from Iconify on a miss… (skills/iig3d/scripts/iig3d.py:L637)
- render_icon() (skills/iig3d/scripts/iig3d.py:L656)
- Rasterise one SVG to an RGBA PIL image of `size` px; currentColor renders black. (skills/iig3d/scripts/iig3d.py:L657)
- spec_icons() (skills/iig3d/scripts/iig3d.py:L665)
- [{index, label, pack, name}] for every item whose icon resolves to a pack. (skills/iig3d/scripts/iig3d.py:L666)
- build_icon_sheet() (skills/iig3d/scripts/iig3d.py:L675)
- One white PNG contact sheet: each item's glyph in black with its number and… (skills/iig3d/scripts/iig3d.py:L676)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
