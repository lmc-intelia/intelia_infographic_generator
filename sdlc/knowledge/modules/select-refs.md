---
type: Module
title: select_refs
description: "Graphify community 41: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:48:39Z" }
stale_after: "2026-10-05T04:48:39Z"
source_commit: fc98b7651e28bcb666f0776fc2f24f2441f4e765
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T14:48:35+10:00", digest: 9768d0e87bdeefb9 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1875)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1876)
- Item (skills/iig3d/scripts/iig3d.py:L286)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L413)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L414)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L447)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L448)
- pick_pinned_refs() (skills/iig3d/scripts/iig3d.py:L457)
- The pinned ref first, then the layout's style refs as company up to per_render… (skills/iig3d/scripts/iig3d.py:L458)
- select_refs() (skills/iig3d/scripts/iig3d.py:L475)
- Style refs as paths (see pick_style_refs), then the icon sheet, then user refs,… (skills/iig3d/scripts/iig3d.py:L484)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
