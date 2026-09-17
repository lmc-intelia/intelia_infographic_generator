---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:17:57Z" }
stale_after: "2026-10-01T01:17:57Z"
source_commit: ed8da4b2d7f6ed195dd405ff4012371feb43b6f8
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T11:17:54+10:00", digest: cb2bf6321fdb6307 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L104)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L110)
- _check_type() (skills/iig3d/scripts/iig3d.py:L126)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L127)
- validate_member() (skills/iig3d/scripts/iig3d.py:L152)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L153)
- Route (skills/iig3d/scripts/iig3d.py:L170)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L176)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L181)
- Item (skills/iig3d/scripts/iig3d.py:L223)
- Spec (skills/iig3d/scripts/iig3d.py:L231)
- _str() (skills/iig3d/scripts/iig3d.py:L247)
- load_spec() (skills/iig3d/scripts/iig3d.py:L251)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L252)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L304)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L311)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L312)
- UsageError (skills/iig3d/scripts/iig3d.py:L32)
- orientation() (skills/iig3d/scripts/iig3d.py:L326)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L33)
- select_refs() (skills/iig3d/scripts/iig3d.py:L342)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L349)
- build_parser() (skills/iig3d/scripts/iig3d.py:L401)
- main() (skills/iig3d/scripts/iig3d.py:L409)
- .items() (skills/iig3d/scripts/iig3d.py:L50)
- Catalogue (skills/iig3d/scripts/iig3d.py:L75)
- .routing() (skills/iig3d/scripts/iig3d.py:L82)
- .layouts() (skills/iig3d/scripts/iig3d.py:L86)
- .member() (skills/iig3d/scripts/iig3d.py:L89)
- .ref_path() (skills/iig3d/scripts/iig3d.py:L95)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L99)

# Depends on
- [Member](/modules/member.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
