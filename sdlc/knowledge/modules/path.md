---
type: Module
title: Path
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:52:20Z" }
stale_after: "2026-10-05T04:52:20Z"
source_commit: 8ed9020fab339416db7371697fc62e238ae2042e
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T14:48:56+10:00", digest: 05b5aa06590e0558 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .member_yaml() (skills/iig3d/scripts/iig3d.py:L105)
- .ref_path() (skills/iig3d/scripts/iig3d.py:L114)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L1152)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L1153)
- api_key() (skills/iig3d/scripts/iig3d.py:L1173)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L1174)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L1230)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L1239)
- render() (skills/iig3d/scripts/iig3d.py:L1254)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L1267)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L1356)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L1357)
- _load_meta() (skills/iig3d/scripts/iig3d.py:L1371)
- _check_variant() (skills/iig3d/scripts/iig3d.py:L1400)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L1408)
- add_ref() (skills/iig3d/scripts/iig3d.py:L1429)
- Normalise an image into refs/<member>/, register it in the member YAML (or… (skills/iig3d/scripts/iig3d.py:L1430)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L155)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L163)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L169)
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1699)
- UsageError (skills/iig3d/scripts/iig3d.py:L44)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L45)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [prepare](/modules/prepare.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
