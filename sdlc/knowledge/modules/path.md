---
type: Module
title: Path
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:47:44Z" }
stale_after: "2026-10-05T02:47:44Z"
source_commit: 2285898e55a2ed6720d292c1eb4bd34a1f6f1690
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T12:47:39+10:00", digest: 67114822a3e7b1d9 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- normalise_image() (skills/iig3d/scripts/iig3d.py:L1016)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L1017)
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1340)
- pep723_dependencies() (skills/iig3d/scripts/iig3d.py:L1427)
- Dependencies from the script's inline metadata block, parsed as TOML per PEP… (skills/iig3d/scripts/iig3d.py:L1428)
- dependency_parity() (skills/iig3d/scripts/iig3d.py:L1436)
- The PEP 723 header and the repository pyproject.toml must list the same runtime… (skills/iig3d/scripts/iig3d.py:L1437)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L812)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L813)
- api_key() (skills/iig3d/scripts/iig3d.py:L833)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L834)
- to_rgb() (skills/iig3d/scripts/iig3d.py:L861)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L862)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L875)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L876)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L890)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L899)
- render() (skills/iig3d/scripts/iig3d.py:L914)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L927)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [prepare](/modules/prepare.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
