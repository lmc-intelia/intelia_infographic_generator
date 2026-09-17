---
type: Module
title: Path
description: "Graphify community 36: skills/iig3d/scripts/iig3d.py"
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
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1206)
- pep723_dependencies() (skills/iig3d/scripts/iig3d.py:L1276)
- Dependencies from the script's inline metadata block, parsed as TOML per PEP… (skills/iig3d/scripts/iig3d.py:L1277)
- dependency_parity() (skills/iig3d/scripts/iig3d.py:L1285)
- The PEP 723 header and the repository pyproject.toml must list the same runtime… (skills/iig3d/scripts/iig3d.py:L1286)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L705)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L706)
- api_key() (skills/iig3d/scripts/iig3d.py:L726)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L727)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L783)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L792)
- render() (skills/iig3d/scripts/iig3d.py:L807)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L820)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [normalise_image](/modules/normalise-image.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
