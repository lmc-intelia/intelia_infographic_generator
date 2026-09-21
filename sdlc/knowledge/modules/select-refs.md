---
type: Module
title: select_refs
description: "Graphify community 45: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:21:34Z" }
stale_after: "2026-10-05T02:21:34Z"
source_commit: d126a0296a37604c78c4c0df4830556ff521c974
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T12:21:30+10:00", digest: 5a17624de6e73002 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1476)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1477)
- Item (skills/iig3d/scripts/iig3d.py:L270)
- _pairing() (skills/iig3d/scripts/iig3d.py:L390)
- Ref ids paired with the layout; the member's first pairing when the layout has… (skills/iig3d/scripts/iig3d.py:L391)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L395)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L396)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L429)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L430)
- pick_pinned_refs() (skills/iig3d/scripts/iig3d.py:L439)
- The pinned ref first, then the layout's style refs as company up to per_render… (skills/iig3d/scripts/iig3d.py:L440)
- select_refs() (skills/iig3d/scripts/iig3d.py:L457)
- Style refs as paths (see pick_style_refs), user refs appended, capped by… (skills/iig3d/scripts/iig3d.py:L465)

# Depends on
- [add_ref](/modules/add-ref.md)
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
