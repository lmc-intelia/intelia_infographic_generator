---
type: Module
title: Catalogue
description: "Graphify community 45: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:12:49Z" }
stale_after: "2026-10-05T05:12:49Z"
source_commit: 0dac1771abb0a241b787b37f99663e8da1c9a6f4
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:06:12+10:00", digest: 755d0eccdd75a015 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member_yaml() (skills/iig3d/scripts/iig3d.py:L105)
- .ref_path() (skills/iig3d/scripts/iig3d.py:L114)
- .is_layout() (skills/iig3d/scripts/iig3d.py:L117)
- A general routing layout or a member's own device name. (skills/iig3d/scripts/iig3d.py:L118)
- _load_meta() (skills/iig3d/scripts/iig3d.py:L1386)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L1423)
- add_ref() (skills/iig3d/scripts/iig3d.py:L1444)
- Normalise an image into refs/<member>/, register it in the member YAML (or… (skills/iig3d/scripts/iig3d.py:L1445)
- .negative_tail() (skills/iig3d/scripts/iig3d.py:L146)
- Last sentence of the family negative list; a fragment that ends with it already… (skills/iig3d/scripts/iig3d.py:L147)
- .flag_values() (skills/iig3d/scripts/iig3d.py:L151)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L155)
- expected_docs() (skills/iig3d/scripts/iig3d.py:L1570)
- render_docs() (skills/iig3d/scripts/iig3d.py:L1577)
- stale_docs() (skills/iig3d/scripts/iig3d.py:L1586)
- `docs stale: <path>` for every generated file that is missing or differs from… (skills/iig3d/scripts/iig3d.py:L1587)
- cmd_list() (skills/iig3d/scripts/iig3d.py:L1658)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L169)
- cmd_check() (skills/iig3d/scripts/iig3d.py:L1779)
- check() (skills/iig3d/scripts/iig3d.py:L1840)
- Every catalogue rule in one pass; empty list means clean. (skills/iig3d/scripts/iig3d.py:L1841)
- _check_type() (skills/iig3d/scripts/iig3d.py:L185)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L186)
- validate_member() (skills/iig3d/scripts/iig3d.py:L211)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L212)
- .items() (skills/iig3d/scripts/iig3d.py:L63)
- Catalogue (skills/iig3d/scripts/iig3d.py:L91)
- .routing() (skills/iig3d/scripts/iig3d.py:L98)
- has_negative_list() (skills/iig3d/scripts/iig3d.py:L988)

# Depends on
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
