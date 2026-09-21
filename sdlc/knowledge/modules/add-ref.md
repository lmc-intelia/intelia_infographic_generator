---
type: Module
title: add_ref
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
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
- _load_meta() (skills/iig3d/scripts/iig3d.py:L1018)
- .member_yaml() (skills/iig3d/scripts/iig3d.py:L102)
- _check_variant() (skills/iig3d/scripts/iig3d.py:L1047)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L1055)
- add_ref() (skills/iig3d/scripts/iig3d.py:L1076)
- Normalise an image into refs/<member>/, register it in the member YAML (or… (skills/iig3d/scripts/iig3d.py:L1077)
- .is_layout() (skills/iig3d/scripts/iig3d.py:L114)
- A general routing layout or a member's own device name. (skills/iig3d/scripts/iig3d.py:L115)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L152)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L160)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L166)
- _check_type() (skills/iig3d/scripts/iig3d.py:L182)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L183)
- validate_member() (skills/iig3d/scripts/iig3d.py:L208)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L209)
- UsageError (skills/iig3d/scripts/iig3d.py:L41)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L42)
- slugify() (skills/iig3d/scripts/iig3d.py:L609)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
