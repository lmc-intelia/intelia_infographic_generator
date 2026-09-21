---
type: Module
title: Path
description: "Graphify community 52: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:30:03Z" }
stale_after: "2026-10-05T05:30:03Z"
source_commit: fae00c698effe61c7083ae8264ab6a14d68f8f09
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:29:58+10:00", digest: 4b4238bdfa8f4e38 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .family_yaml() (skills/iig3d/scripts/iig3d.py:L102)
- .member_yaml() (skills/iig3d/scripts/iig3d.py:L105)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L1177)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L1178)
- api_key() (skills/iig3d/scripts/iig3d.py:L1198)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L1199)
- resolve_logo() (skills/iig3d/scripts/iig3d.py:L1254)
- The logo to stamp: `--logo PATH`, else IIG3D_LOGO, else the bundled Intelia… (skills/iig3d/scripts/iig3d.py:L1255)
- drop_shadow() (skills/iig3d/scripts/iig3d.py:L1265)
- A blurred black copy of the logo's alpha, shifted by `offset`; the layer is… (skills/iig3d/scripts/iig3d.py:L1266)
- stamp_logo() (skills/iig3d/scripts/iig3d.py:L1283)
- Composite `logo_path` (RGBA) into the bottom-left corner of `image`, `pad` px… (skills/iig3d/scripts/iig3d.py:L1284)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L1325)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L1334)
- render() (skills/iig3d/scripts/iig3d.py:L1349)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG, the… (skills/iig3d/scripts/iig3d.py:L1363)
- _check_variant() (skills/iig3d/scripts/iig3d.py:L1505)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L163)
- cmd_render() (skills/iig3d/scripts/iig3d.py:L1807)
- pep723_dependencies() (skills/iig3d/scripts/iig3d.py:L1913)
- Dependencies from the script's inline metadata block, parsed as TOML per PEP… (skills/iig3d/scripts/iig3d.py:L1914)
- dependency_parity() (skills/iig3d/scripts/iig3d.py:L1922)
- The PEP 723 header and the repository pyproject.toml must list the same runtime… (skills/iig3d/scripts/iig3d.py:L1923)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [normalise_image](/modules/normalise-image.md)
- [prepare](/modules/prepare.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
