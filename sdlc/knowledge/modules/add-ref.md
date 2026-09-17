---
type: Module
title: add_ref
description: "Graphify community 43: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T02:19:39Z" }
stale_after: "2026-10-01T02:19:39Z"
source_commit: 1c44ce7af8f81c51eaf6b7d3b08e5cffeb7b73da
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T12:19:34+10:00", digest: 6abb96a301e9dd69 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member_yaml() (skills/iig3d/scripts/iig3d.py:L102)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L128)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L133)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L139)
- _check_type() (skills/iig3d/scripts/iig3d.py:L155)
- Walk one schema node: a bare type name or {type, keys|items|values}. (skills/iig3d/scripts/iig3d.py:L156)
- validate_member() (skills/iig3d/scripts/iig3d.py:L181)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L182)
- slugify() (skills/iig3d/scripts/iig3d.py:L548)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L949)
- add_ref() (skills/iig3d/scripts/iig3d.py:L970)
- Normalise an image into refs/<member>/, register it in the member YAML (or… (skills/iig3d/scripts/iig3d.py:L971)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
