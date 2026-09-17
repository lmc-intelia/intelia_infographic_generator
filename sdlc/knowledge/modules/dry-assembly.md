---
type: Module
title: _dry_assembly
description: "Graphify community 45: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T03:14:52Z" }
stale_after: "2026-10-01T03:14:52Z"
source_commit: 08802b907cd4f8f7021c481a3d443d13812b6656
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T12:38:26+10:00", digest: 4be94854c4daa288 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1350)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1351)
- Item (skills/iig3d/scripts/iig3d.py:L240)
- _pairing() (skills/iig3d/scripts/iig3d.py:L358)
- Ref ids paired with the layout; the member's first pairing when the layout has… (skills/iig3d/scripts/iig3d.py:L359)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L363)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L364)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L397)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L398)
- select_refs() (skills/iig3d/scripts/iig3d.py:L407)
- Style refs as paths (see pick_style_refs), user refs appended, capped by… (skills/iig3d/scripts/iig3d.py:L414)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
