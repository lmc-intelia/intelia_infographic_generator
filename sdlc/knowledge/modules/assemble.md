---
type: Module
title: assemble
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:06:16Z" }
stale_after: "2026-10-05T05:06:16Z"
source_commit: 6ac4d77c7d0e6ad62e60d2fa01cebbade71dc4ca
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T15:06:12+10:00", digest: 755d0eccdd75a015 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- text_labels() (skills/iig3d/scripts/iig3d.py:L1019)
- word_count() (skills/iig3d/scripts/iig3d.py:L1031)
- reference_composition() (skills/iig3d/scripts/iig3d.py:L1035)
- The Reference Composition section: reproduce reference image 1, swap in the… (skills/iig3d/scripts/iig3d.py:L1036)
- assemble() (skills/iig3d/scripts/iig3d.py:L1054)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L1068)
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1891)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1892)
- Item (skills/iig3d/scripts/iig3d.py:L286)
- Spec (skills/iig3d/scripts/iig3d.py:L294)
- _str() (skills/iig3d/scripts/iig3d.py:L317)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L321)
- load_spec() (skills/iig3d/scripts/iig3d.py:L325)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L326)
- orientation() (skills/iig3d/scripts/iig3d.py:L405)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L451)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L452)
- icon_guidance() (skills/iig3d/scripts/iig3d.py:L921)
- The Icon Set section: copy each numbered glyph from the sheet onto its item. (skills/iig3d/scripts/iig3d.py:L922)
- redact() (skills/iig3d/scripts/iig3d.py:L949)
- content_block() (skills/iig3d/scripts/iig3d.py:L992)
- The content section; `icon_slots` maps item index to a sheet glyph note… (skills/iig3d/scripts/iig3d.py:L993)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [iig3d.py](/modules/iig3d-py.md)
- [.items](/modules/items.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
