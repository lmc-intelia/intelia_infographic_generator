---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
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
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L1160)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L1161)
- exit_code() (skills/iig3d/scripts/iig3d.py:L1230)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L1343)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L155)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1689)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L169)
- dispatch() (skills/iig3d/scripts/iig3d.py:L1890)
- main() (skills/iig3d/scripts/iig3d.py:L1896)
- _str() (skills/iig3d/scripts/iig3d.py:L318)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L322)
- load_spec() (skills/iig3d/scripts/iig3d.py:L326)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L327)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L385)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L392)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L393)
- _nums() (skills/iig3d/scripts/iig3d.py:L531)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L535)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L536)
- Prompt (skills/iig3d/scripts/iig3d.py:L964)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [resolve_icons](/modules/resolve-icons.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [resolve_icons](/modules/resolve-icons.md)
- [UsageError](/modules/usageerror.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
