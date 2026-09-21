---
type: Module
title: Path
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
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
- .family_yaml() (skills/iig3d/scripts/iig3d.py:L102)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L1156)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L1157)
- api_key() (skills/iig3d/scripts/iig3d.py:L1177)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L1178)
- to_rgb() (skills/iig3d/scripts/iig3d.py:L1213)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L1214)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L1227)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L1228)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L1242)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L1251)
- render() (skills/iig3d/scripts/iig3d.py:L1266)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L1279)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L1371)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L1372)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L163)
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1715)
- pep723_dependencies() (skills/iig3d/scripts/iig3d.py:L1820)
- Dependencies from the script's inline metadata block, parsed as TOML per PEP… (skills/iig3d/scripts/iig3d.py:L1821)
- dependency_parity() (skills/iig3d/scripts/iig3d.py:L1829)
- The PEP 723 header and the repository pyproject.toml must list the same runtime… (skills/iig3d/scripts/iig3d.py:L1830)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [prepare](/modules/prepare.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
