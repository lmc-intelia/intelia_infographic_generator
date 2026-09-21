---
type: Module
title: resolve_icons
description: "Graphify community 49: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:03:47Z" }
stale_after: "2026-10-05T05:03:47Z"
source_commit: b59f3451dc0b77b589cbafd9812f581df6f10352
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:03:44+10:00", digest: 1eab83aa7c95cc71 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- parse_icon() (skills/iig3d/scripts/iig3d.py:L626)
- (pack, name) for `pack:name`, or for `name` when a default pack is set;… (skills/iig3d/scripts/iig3d.py:L627)
- icon_svg() (skills/iig3d/scripts/iig3d.py:L641)
- The cached SVG under icons/<pack>/<name>.svg, fetched from Iconify on a miss… (skills/iig3d/scripts/iig3d.py:L642)
- render_icon() (skills/iig3d/scripts/iig3d.py:L662)
- Rasterise one SVG to an RGBA PIL image of `size` px; currentColor renders black. (skills/iig3d/scripts/iig3d.py:L663)
- spec_icons() (skills/iig3d/scripts/iig3d.py:L671)
- [{index, label, pack, name, via: spec}] for every item whose icon names a pack… (skills/iig3d/scripts/iig3d.py:L672)
- search_icons() (skills/iig3d/scripts/iig3d.py:L815)
- Glyph names in `pack` whose Iconify name matches `query`; empty when fetching… (skills/iig3d/scripts/iig3d.py:L816)
- _words() (skills/iig3d/scripts/iig3d.py:L830)
- suggest_icon() (skills/iig3d/scripts/iig3d.py:L839)
- (name, via) for an item from its text: the synonym table on the label, then the… (skills/iig3d/scripts/iig3d.py:L840)
- resolve_icons() (skills/iig3d/scripts/iig3d.py:L858)
- Every item's glyph: the spec's own name when it exists (a missing name falls… (skills/iig3d/scripts/iig3d.py:L859)
- build_icon_sheet() (skills/iig3d/scripts/iig3d.py:L890)
- One white PNG contact sheet: each item's glyph in black with its number and… (skills/iig3d/scripts/iig3d.py:L891)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
