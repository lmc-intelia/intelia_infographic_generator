---
type: Module
title: Path
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:21:21Z" }
stale_after: "2026-10-05T05:21:21Z"
source_commit: 2efd6dab1b448f314234109aa7de72730da1239c
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:21:18+10:00", digest: 92e1dac7df45de37 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member_yaml() (skills/iig3d/scripts/iig3d.py:L105)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L1156)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L1157)
- api_key() (skills/iig3d/scripts/iig3d.py:L1177)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L1178)
- stamp_logo() (skills/iig3d/scripts/iig3d.py:L1262)
- Composite `logo_path` (RGBA) into the bottom-left corner of `image`, `pad` px… (skills/iig3d/scripts/iig3d.py:L1263)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L1304)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L1313)
- render() (skills/iig3d/scripts/iig3d.py:L1328)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG, the… (skills/iig3d/scripts/iig3d.py:L1342)
- _load_meta() (skills/iig3d/scripts/iig3d.py:L1455)
- _check_variant() (skills/iig3d/scripts/iig3d.py:L1484)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L1492)
- add_ref() (skills/iig3d/scripts/iig3d.py:L1513)
- Normalise an image into refs/<member>/, register it in the member YAML (or… (skills/iig3d/scripts/iig3d.py:L1514)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L155)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L163)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L169)
- validate_member() (skills/iig3d/scripts/iig3d.py:L211)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L212)
- _str() (skills/iig3d/scripts/iig3d.py:L317)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L321)
- load_spec() (skills/iig3d/scripts/iig3d.py:L325)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L326)
- UsageError (skills/iig3d/scripts/iig3d.py:L44)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L45)
- slugify() (skills/iig3d/scripts/iig3d.py:L953)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [_dry_assembly](/modules/dry-assembly.md)
- [iig3d.py](/modules/iig3d-py.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)
- [prepare](/modules/prepare.md)
- [resolve_icons](/modules/resolve-icons.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
