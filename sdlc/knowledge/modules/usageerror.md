---
type: Module
title: UsageError
description: "Graphify community 36: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:05:37Z" }
stale_after: "2026-10-05T04:05:37Z"
source_commit: 7ba9fba7a655769a839ae420f00e5a62beab9810
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T13:02:34+10:00", digest: 48021e1d3120f54d }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _check_variant() (skills/iig3d/scripts/iig3d.py:L1060)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L1068)
- _check_type() (skills/iig3d/scripts/iig3d.py:L182)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L183)
- validate_member() (skills/iig3d/scripts/iig3d.py:L208)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L209)
- Route (skills/iig3d/scripts/iig3d.py:L226)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L233)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L251)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L374)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L381)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L382)
- UsageError (skills/iig3d/scripts/iig3d.py:L41)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L42)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [prepare](/modules/prepare.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
