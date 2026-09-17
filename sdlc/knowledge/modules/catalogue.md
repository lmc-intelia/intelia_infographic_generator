---
type: Module
title: Catalogue
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:47:43Z" }
stale_after: "2026-10-01T01:47:43Z"
source_commit: 1d771a6e54b0997d70b05103a6a7a41fe3de7b8b
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T11:47:39+10:00", digest: 8cd1197f28e29ede }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member_yaml() (skills/iig3d/scripts/iig3d.py:L101)
- catalogue_markdown() (skills/iig3d/scripts/iig3d.py:L1056)
- expected_docs() (skills/iig3d/scripts/iig3d.py:L1075)
- render_docs() (skills/iig3d/scripts/iig3d.py:L1082)
- stale_docs() (skills/iig3d/scripts/iig3d.py:L1091)
- `docs stale: <path>` for every generated file that is missing or differs from… (skills/iig3d/scripts/iig3d.py:L1092)
- .is_layout() (skills/iig3d/scripts/iig3d.py:L113)
- A general routing layout or a member's own device name. (skills/iig3d/scripts/iig3d.py:L114)
- cmd_list() (skills/iig3d/scripts/iig3d.py:L1153)
- .negative_tail() (skills/iig3d/scripts/iig3d.py:L118)
- Last sentence of the family negative list; a fragment that ends with it already… (skills/iig3d/scripts/iig3d.py:L119)
- .flag_values() (skills/iig3d/scripts/iig3d.py:L123)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L127)
- check() (skills/iig3d/scripts/iig3d.py:L1288)
- Every catalogue rule in one pass; empty list means clean. (skills/iig3d/scripts/iig3d.py:L1289)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L132)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L138)
- _check_type() (skills/iig3d/scripts/iig3d.py:L154)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L155)
- validate_member() (skills/iig3d/scripts/iig3d.py:L180)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L181)
- has_negative_list() (skills/iig3d/scripts/iig3d.py:L582)
- .items() (skills/iig3d/scripts/iig3d.py:L59)
- Catalogue (skills/iig3d/scripts/iig3d.py:L87)
- _load_meta() (skills/iig3d/scripts/iig3d.py:L916)
- .routing() (skills/iig3d/scripts/iig3d.py:L94)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L941)
- add_ref() (skills/iig3d/scripts/iig3d.py:L962)
- Normalise an image into refs/<member>/, register it in the member YAML (or… (skills/iig3d/scripts/iig3d.py:L963)

# Depends on
- [_dry_assembly](/modules/dry-assembly.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
