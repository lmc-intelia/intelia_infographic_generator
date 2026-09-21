---
type: Module
title: resolve_icons
description: "Graphify community 49: skills/iig3d/scripts/iig3d.py"
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
- cmd_icons() (skills/iig3d/scripts/iig3d.py:L1850)
- Name search and text-based suggestion in one call, so Claude can pick or verify… (skills/iig3d/scripts/iig3d.py:L1851)
- parse_icon() (skills/iig3d/scripts/iig3d.py:L628)
- (pack, name) for `pack:name`, or for `name` when a default pack is set;… (skills/iig3d/scripts/iig3d.py:L629)
- icon_svg() (skills/iig3d/scripts/iig3d.py:L643)
- The cached SVG under icons/<pack>/<name>.svg, fetched from Iconify on a miss… (skills/iig3d/scripts/iig3d.py:L644)
- render_icon() (skills/iig3d/scripts/iig3d.py:L664)
- Rasterise one SVG to an RGBA PIL image of `size` px; currentColor renders black. (skills/iig3d/scripts/iig3d.py:L665)
- spec_icons() (skills/iig3d/scripts/iig3d.py:L673)
- [{index, label, pack, name, via: spec}] for every item whose icon names a pack… (skills/iig3d/scripts/iig3d.py:L674)
- search_icons() (skills/iig3d/scripts/iig3d.py:L817)
- Glyph names in `pack` whose Iconify name matches `query`; empty when fetching… (skills/iig3d/scripts/iig3d.py:L818)
- _words() (skills/iig3d/scripts/iig3d.py:L832)
- suggest_icon() (skills/iig3d/scripts/iig3d.py:L841)
- (name, via) for an item from its text: the synonym table on the label, then the… (skills/iig3d/scripts/iig3d.py:L842)
- resolve_icons() (skills/iig3d/scripts/iig3d.py:L860)
- Every item's glyph: the spec's own name when it exists (a missing name falls… (skills/iig3d/scripts/iig3d.py:L861)
- build_icon_sheet() (skills/iig3d/scripts/iig3d.py:L892)
- One white PNG contact sheet: each item's glyph in black with its number and… (skills/iig3d/scripts/iig3d.py:L893)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
