---
type: Module
title: Path
description: "Graphify community 35: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:03:47Z" }
stale_after: "2026-10-05T05:03:47Z"
source_commit: b59f3451dc0b77b589cbafd9812f581df6f10352
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:03:44+10:00", digest: 1eab83aa7c95cc71 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- .family_yaml() (skills/iig3d/scripts/iig3d.py:L102)
- .member_yaml() (skills/iig3d/scripts/iig3d.py:L105)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L1156)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L1157)
- api_key() (skills/iig3d/scripts/iig3d.py:L1177)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L1178)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L1245)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L1254)
- render() (skills/iig3d/scripts/iig3d.py:L1269)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L1282)
- _load_meta() (skills/iig3d/scripts/iig3d.py:L1389)
- _check_variant() (skills/iig3d/scripts/iig3d.py:L1418)
- _new_member_record() (skills/iig3d/scripts/iig3d.py:L1426)
- add_ref() (skills/iig3d/scripts/iig3d.py:L1447)
- Normalise an image into refs/<member>/, register it in the member YAML (or… (skills/iig3d/scripts/iig3d.py:L1448)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L155)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L163)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L169)
- validate_member() (skills/iig3d/scripts/iig3d.py:L211)
- Problems with a member record against schema.yaml `member`; empty when valid. (skills/iig3d/scripts/iig3d.py:L212)
- UsageError (skills/iig3d/scripts/iig3d.py:L44)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L45)
- slugify() (skills/iig3d/scripts/iig3d.py:L953)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [.items](/modules/items.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
