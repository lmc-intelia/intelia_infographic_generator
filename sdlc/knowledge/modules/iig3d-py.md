---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
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
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1350)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1351)
- Item (skills/iig3d/scripts/iig3d.py:L240)
- Spec (skills/iig3d/scripts/iig3d.py:L248)
- _str() (skills/iig3d/scripts/iig3d.py:L268)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L272)
- load_spec() (skills/iig3d/scripts/iig3d.py:L276)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L277)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L397)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L398)
- _nums() (skills/iig3d/scripts/iig3d.py:L446)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L450)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L451)
- redact() (skills/iig3d/scripts/iig3d.py:L547)
- content_block() (skills/iig3d/scripts/iig3d.py:L590)
- text_labels() (skills/iig3d/scripts/iig3d.py:L614)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L804)

# Depends on
- [assemble](/modules/assemble.md)
- [Catalogue](/modules/catalogue.md)
- [load_catalogue](/modules/load-catalogue.md)
- [Member](/modules/member.md)
- [_new_member_record](/modules/new-member-record.md)
- [normalise_image](/modules/normalise-image.md)
- [Path](/modules/path.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- [assemble](/modules/assemble.md)
- [load_catalogue](/modules/load-catalogue.md)
- [Path](/modules/path.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
