---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T03:13:15Z" }
stale_after: "2026-10-01T03:13:15Z"
source_commit: e5e99535de68b5513b2d805225a669510f6415dd
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T12:38:26+10:00", digest: 4be94854c4daa288 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1115)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1256)
- main() (skills/iig3d/scripts/iig3d.py:L1262)
- Spec (skills/iig3d/scripts/iig3d.py:L248)
- _str() (skills/iig3d/scripts/iig3d.py:L268)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L272)
- load_spec() (skills/iig3d/scripts/iig3d.py:L276)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L277)
- _nums() (skills/iig3d/scripts/iig3d.py:L446)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L450)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L451)
- redact() (skills/iig3d/scripts/iig3d.py:L547)
- content_block() (skills/iig3d/scripts/iig3d.py:L590)
- text_labels() (skills/iig3d/scripts/iig3d.py:L614)
- exit_code() (skills/iig3d/scripts/iig3d.py:L753)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L804)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [_dry_assembly](/modules/dry-assembly.md)
- [Member](/modules/member.md)
- [_new_member_record](/modules/new-member-record.md)
- [Path](/modules/path.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
