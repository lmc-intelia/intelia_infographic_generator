---
type: Module
title: Catalogue
description: "Graphify community 45: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:49:58Z" }
stale_after: "2026-10-05T04:49:58Z"
source_commit: 6197c1b39e2b704463349bd9e1b4033182bc40ce
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T14:48:56+10:00", digest: 05b5aa06590e0558 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .family_yaml() (skills/iig3d/scripts/iig3d.py:L102)
- .is_layout() (skills/iig3d/scripts/iig3d.py:L117)
- A general routing layout or a member's own device name. (skills/iig3d/scripts/iig3d.py:L118)
- .flag_values() (skills/iig3d/scripts/iig3d.py:L151)
- member_markdown() (skills/iig3d/scripts/iig3d.py:L1513)
- catalogue_markdown() (skills/iig3d/scripts/iig3d.py:L1536)
- expected_docs() (skills/iig3d/scripts/iig3d.py:L1555)
- render_docs() (skills/iig3d/scripts/iig3d.py:L1562)
- stale_docs() (skills/iig3d/scripts/iig3d.py:L1571)
- `docs stale: <path>` for every generated file that is missing or differs from… (skills/iig3d/scripts/iig3d.py:L1572)
- cmd_list() (skills/iig3d/scripts/iig3d.py:L1643)
- check() (skills/iig3d/scripts/iig3d.py:L1824)
- Every catalogue rule in one pass; empty list means clean. (skills/iig3d/scripts/iig3d.py:L1825)
- _check_type() (skills/iig3d/scripts/iig3d.py:L185)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L186)
- validate_member() (skills/iig3d/scripts/iig3d.py:L211)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L212)
- .items() (skills/iig3d/scripts/iig3d.py:L63)
- Catalogue (skills/iig3d/scripts/iig3d.py:L91)
- _bullets() (skills/iig3d/scripts/iig3d.py:L953)
- _table() (skills/iig3d/scripts/iig3d.py:L957)
- layout_sections() (skills/iig3d/scripts/iig3d.py:L964)
- (heading, body) pairs of the member's device layout, shared by the prompt and… (skills/iig3d/scripts/iig3d.py:L965)
- .routing() (skills/iig3d/scripts/iig3d.py:L98)
- has_negative_list() (skills/iig3d/scripts/iig3d.py:L984)

# Depends on
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
