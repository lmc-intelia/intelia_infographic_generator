---
type: Module
title: Path
description: "Graphify community 36: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:47:43Z" }
stale_after: "2026-10-01T01:47:43Z"
source_commit: 1d771a6e54b0997d70b05103a6a7a41fe3de7b8b
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T11:47:39+10:00", digest: 8cd1197f28e29ede }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1198)
- pep723_dependencies() (skills/iig3d/scripts/iig3d.py:L1268)
- Dependencies from the script's inline metadata block, parsed as TOML per PEP… (skills/iig3d/scripts/iig3d.py:L1269)
- dependency_parity() (skills/iig3d/scripts/iig3d.py:L1277)
- The PEP 723 header and the repository pyproject.toml must list the same runtime… (skills/iig3d/scripts/iig3d.py:L1278)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L704)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L705)
- api_key() (skills/iig3d/scripts/iig3d.py:L725)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L726)
- to_rgb() (skills/iig3d/scripts/iig3d.py:L753)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L754)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L767)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L768)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L782)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L791)
- render() (skills/iig3d/scripts/iig3d.py:L806)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L819)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L901)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L902)
- .family_yaml() (skills/iig3d/scripts/iig3d.py:L98)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
