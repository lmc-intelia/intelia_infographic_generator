---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
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
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L1068)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1238)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1402)
- main() (skills/iig3d/scripts/iig3d.py:L1408)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L152)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L166)
- _check_type() (skills/iig3d/scripts/iig3d.py:L182)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L183)
- validate_member() (skills/iig3d/scripts/iig3d.py:L208)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L209)
- _str() (skills/iig3d/scripts/iig3d.py:L312)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L316)
- load_spec() (skills/iig3d/scripts/iig3d.py:L320)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L321)
- _nums() (skills/iig3d/scripts/iig3d.py:L517)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L521)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L522)
- exit_code() (skills/iig3d/scripts/iig3d.py:L857)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L908)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [select_refs](/modules/select-refs.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
