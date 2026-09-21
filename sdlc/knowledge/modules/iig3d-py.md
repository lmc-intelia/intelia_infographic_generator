---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
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
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- _dry_assembly() (skills/iig3d/scripts/iig3d.py:L1498)
- Assemble a prompt for every member x pairing layout; report ref-rule violations. (skills/iig3d/scripts/iig3d.py:L1499)
- Item (skills/iig3d/scripts/iig3d.py:L283)
- Spec (skills/iig3d/scripts/iig3d.py:L291)
- _str() (skills/iig3d/scripts/iig3d.py:L312)
- _opt_str() (skills/iig3d/scripts/iig3d.py:L316)
- load_spec() (skills/iig3d/scripts/iig3d.py:L320)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L321)
- orientation() (skills/iig3d/scripts/iig3d.py:L396)
- ref_rule_violations() (skills/iig3d/scripts/iig3d.py:L442)
- The two selection invariants, stated once for the selector and the checker. (skills/iig3d/scripts/iig3d.py:L443)
- _nums() (skills/iig3d/scripts/iig3d.py:L517)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L521)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L522)
- Prompt (skills/iig3d/scripts/iig3d.py:L612)
- redact() (skills/iig3d/scripts/iig3d.py:L618)
- content_block() (skills/iig3d/scripts/iig3d.py:L661)
- text_labels() (skills/iig3d/scripts/iig3d.py:L685)
- word_count() (skills/iig3d/scripts/iig3d.py:L697)
- reference_composition() (skills/iig3d/scripts/iig3d.py:L701)
- The Reference Composition section: reproduce reference image 1, swap in the… (skills/iig3d/scripts/iig3d.py:L702)
- assemble() (skills/iig3d/scripts/iig3d.py:L720)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L732)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L795)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L796)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L908)

# Depends on
- [Catalogue](/modules/catalogue.md)
- [load_catalogue](/modules/load-catalogue.md)
- [Member](/modules/member.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [UsageError](/modules/usageerror.md)

# Inferred
- [Catalogue](/modules/catalogue.md)
- [Path](/modules/path.md)
- [prepare](/modules/prepare.md)
- [UsageError](/modules/usageerror.md)

# Features
- [iig3d skill](/features/iig3d-skill.md)
