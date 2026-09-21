---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T02:34:09Z" }
stale_after: "2026-10-05T02:34:09Z"
source_commit: da9997f4fe89158d984ba9c261c11eb28668ab76
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T12:34:05+10:00", digest: 3579c45b24e4283a }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- build_parser() (skills/iig3d/scripts/iig3d.py:L1238)
- main() (skills/iig3d/scripts/iig3d.py:L1408)
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1496)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1497)
- Item (skills/iig3d/scripts/iig3d.py:L283)
- Spec (skills/iig3d/scripts/iig3d.py:L291)
- _str() (skills/iig3d/scripts/iig3d.py:L312)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L316)
- load_spec() (skills/iig3d/scripts/iig3d.py:L320)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L321)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L374)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L381)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L382)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L442)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L443)
- _nums() (skills/iig3d/scripts/iig3d.py:L517)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L521)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L522)
- redact() (skills/iig3d/scripts/iig3d.py:L618)
- content_block() (skills/iig3d/scripts/iig3d.py:L661)
- text_labels() (skills/iig3d/scripts/iig3d.py:L685)
- exit_code() (skills/iig3d/scripts/iig3d.py:L857)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L908)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [Member](/modules/member.md)
- [normalise_image](/modules/normalise-image.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)

# Inferred
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
