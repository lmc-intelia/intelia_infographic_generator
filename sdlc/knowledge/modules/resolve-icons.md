---
type: Module
title: resolve_icons
description: "Graphify community 49: skills/iig3d/scripts/iig3d.py"
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
- cmd_icons() (skills/iig3d/scripts/iig3d.py:L1757)
- Name search and text-based suggestion in one call, so Claude can pick or verify… (skills/iig3d/scripts/iig3d.py:L1758)
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
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
