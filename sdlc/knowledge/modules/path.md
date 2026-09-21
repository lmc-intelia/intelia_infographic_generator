---
type: Module
title: Path
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:34:09Z" }
stale_after: "2026-10-05T02:34:09Z"
source_commit: da9997f4fe89158d984ba9c261c11eb28668ab76
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T12:34:05+10:00", digest: 3579c45b24e4283a }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _load_meta() (skills/iig3d/scripts/iig3d.py:L1031)
- _check_variant() (skills/iig3d/scripts/iig3d.py:L1060)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L1068)
- add_ref() (skills/iig3d/scripts/iig3d.py:L1089)
- Normalise an image into refs/<member>/, register it in the member YAML (or… (skills/iig3d/scripts/iig3d.py:L1090)
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1338)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L152)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L160)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L166)
- validate_member() (skills/iig3d/scripts/iig3d.py:L208)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L209)
- UsageError (skills/iig3d/scripts/iig3d.py:L41)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L42)
- slugify() (skills/iig3d/scripts/iig3d.py:L622)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L812)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L813)
- api_key() (skills/iig3d/scripts/iig3d.py:L833)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L834)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L890)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L899)
- render() (skills/iig3d/scripts/iig3d.py:L914)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L927)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)
- [prepare](/modules/prepare.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
