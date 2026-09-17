---
type: Module
title: Path
description: "Graphify community 36: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T03:14:52Z" }
stale_after: "2026-10-01T03:14:52Z"
source_commit: 08802b907cd4f8f7021c481a3d443d13812b6656
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T12:38:26+10:00", digest: 4be94854c4daa288 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1209)
- pep723_dependencies() (skills/iig3d/scripts/iig3d.py:L1279)
- Dependencies from the script's inline metadata block, parsed as TOML per PEP… (skills/iig3d/scripts/iig3d.py:L1280)
- dependency_parity() (skills/iig3d/scripts/iig3d.py:L1288)
- The PEP 723 header and the repository pyproject.toml must list the same runtime… (skills/iig3d/scripts/iig3d.py:L1289)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L708)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L709)
- api_key() (skills/iig3d/scripts/iig3d.py:L729)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L730)
- to_rgb() (skills/iig3d/scripts/iig3d.py:L757)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L758)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L771)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L772)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L786)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L795)
- render() (skills/iig3d/scripts/iig3d.py:L810)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L823)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L912)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L913)
- .family_yaml() (skills/iig3d/scripts/iig3d.py:L99)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
