---
type: Module
title: UsageError
description: "Graphify community 36: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:47:44Z" }
stale_after: "2026-10-05T02:47:44Z"
source_commit: 2285898e55a2ed6720d292c1eb4bd34a1f6f1690
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T12:47:39+10:00", digest: 67114822a3e7b1d9 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member() (skills/iig3d/scripts/iig3d.py:L105)
- _check_variant() (skills/iig3d/scripts/iig3d.py:L1060)
- .resolve_ref() (skills/iig3d/scripts/iig3d.py:L118)
- A catalogue ref named by the user: `<member>/<id|file|stem>`, a… (skills/iig3d/scripts/iig3d.py:L119)
- cmd_refs() (skills/iig3d/scripts/iig3d.py:L1367)
- The refs a render would pass, plus every catalogue ref of the member with its… (skills/iig3d/scripts/iig3d.py:L1368)
- Route (skills/iig3d/scripts/iig3d.py:L226)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L233)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L251)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L374)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L381)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L382)
- UsageError (skills/iig3d/scripts/iig3d.py:L41)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L42)
- select_refs() (skills/iig3d/scripts/iig3d.py:L470)
- Style refs as paths (see pick_style_refs), user refs appended, capped by… (skills/iig3d/scripts/iig3d.py:L478)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [prepare](/modules/prepare.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
