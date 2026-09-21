---
type: Module
title: resolve_icons
description: "Graphify community 49: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:21:21Z" }
stale_after: "2026-10-05T05:21:21Z"
source_commit: 2efd6dab1b448f314234109aa7de72730da1239c
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:21:18+10:00", digest: 92e1dac7df45de37 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- text_labels() (skills/iig3d/scripts/iig3d.py:L1019)
- Spec (skills/iig3d/scripts/iig3d.py:L294)
- parse_icon() (skills/iig3d/scripts/iig3d.py:L626)
- (pack, name) for `pack:name`, or for `name` when a default pack is set;… (skills/iig3d/scripts/iig3d.py:L627)
- icon_svg() (skills/iig3d/scripts/iig3d.py:L641)
- The cached SVG under icons/<pack>/<name>.svg, fetched from Iconify on a miss… (skills/iig3d/scripts/iig3d.py:L642)
- render_icon() (skills/iig3d/scripts/iig3d.py:L662)
- Rasterise one SVG to an RGBA PIL image of `size` px; currentColor renders black. (skills/iig3d/scripts/iig3d.py:L663)
- spec_icons() (skills/iig3d/scripts/iig3d.py:L671)
- [{index, label, pack, name, via: spec}] for every item whose icon names a pack… (skills/iig3d/scripts/iig3d.py:L672)
- resolve_icons() (skills/iig3d/scripts/iig3d.py:L858)
- Every item's glyph: the spec's own name when it exists (a missing name falls… (skills/iig3d/scripts/iig3d.py:L859)
- build_icon_sheet() (skills/iig3d/scripts/iig3d.py:L890)
- One white PNG contact sheet: each item's glyph in black with its number and… (skills/iig3d/scripts/iig3d.py:L891)
- redact() (skills/iig3d/scripts/iig3d.py:L949)
- content_block() (skills/iig3d/scripts/iig3d.py:L992)
- The content section; `icon_slots` maps item index to a sheet glyph note… (skills/iig3d/scripts/iig3d.py:L993)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)
- [suggest_icon](/modules/suggest-icon.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
