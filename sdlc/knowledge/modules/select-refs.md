---
type: Module
title: select_refs
description: "Graphify community 36: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:36:43Z" }
stale_after: "2026-10-05T02:36:43Z"
source_commit: 6de363a7f637fc903d43af9cfa93954eafdc5fc9
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T12:34:05+10:00", digest: 3579c45b24e4283a }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .ref_path() (skills/iig3d/scripts/iig3d.py:L111)
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1496)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1497)
- Item (skills/iig3d/scripts/iig3d.py:L283)
- pick_style_refs() (skills/iig3d/scripts/iig3d.py:L408)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L409)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L442)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L443)
- pick_pinned_refs() (skills/iig3d/scripts/iig3d.py:L452)
- The pinned ref first, then the layout's style refs as company up to per_render… (skills/iig3d/scripts/iig3d.py:L453)
- select_refs() (skills/iig3d/scripts/iig3d.py:L470)
- Style refs as paths (see pick_style_refs), user refs appended, capped by… (skills/iig3d/scripts/iig3d.py:L478)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [prepare](/modules/prepare.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
