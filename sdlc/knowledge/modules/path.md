---
type: Module
title: Path
description: "Graphify community 36: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T02:38:32Z" }
stale_after: "2026-10-01T02:38:32Z"
source_commit: d8412565305a2fce317384d37b5816a2bf81c8ac
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
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L786)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L795)
- render() (skills/iig3d/scripts/iig3d.py:L810)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L823)
- .family_yaml() (skills/iig3d/scripts/iig3d.py:L99)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [normalise_image](/modules/normalise-image.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
