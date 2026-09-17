---
type: Module
title: iig3d.py
description: "Graphify community 9: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:24:25Z" }
stale_after: "2026-10-01T01:24:25Z"
source_commit: 98b000f59040f64ed079923f41989f9b05d6b26b
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T11:24:21+10:00", digest: 9492b4ff52b292e6 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- iig3d.py (skills/iig3d/scripts/iig3d.py:L1)
- main() (skills/iig3d/scripts/iig3d.py:L1015)
- read_yaml() (skills/iig3d/scripts/iig3d.py:L102)
- render_docs() (skills/iig3d/scripts/iig3d.py:L1031)
- check() (skills/iig3d/scripts/iig3d.py:L1035)
- add_ref() (skills/iig3d/scripts/iig3d.py:L1039)
- write_yaml() (skills/iig3d/scripts/iig3d.py:L107)
- load_catalogue() (skills/iig3d/scripts/iig3d.py:L113)
- Route (skills/iig3d/scripts/iig3d.py:L173)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L180)
- Resolve (layout, style) to a family member. Explicit 3d-* style wins; a 3d-*… (skills/iig3d/scripts/iig3d.py:L191)
- Item (skills/iig3d/scripts/iig3d.py:L233)
- Spec (skills/iig3d/scripts/iig3d.py:L241)
- _str() (skills/iig3d/scripts/iig3d.py:L257)
- load_spec() (skills/iig3d/scripts/iig3d.py:L261)
- Parse the YAML content spec; unknown keys and missing title/items/label fail by… (skills/iig3d/scripts/iig3d.py:L262)
- _ratio_value() (skills/iig3d/scripts/iig3d.py:L314)
- snap_aspect() (skills/iig3d/scripts/iig3d.py:L321)
- Return (supported ratio, original when snapped). Presets and None use the… (skills/iig3d/scripts/iig3d.py:L322)
- orientation() (skills/iig3d/scripts/iig3d.py:L336)
- UsageError (skills/iig3d/scripts/iig3d.py:L35)
- select_refs() (skills/iig3d/scripts/iig3d.py:L352)
- Pairing refs for the layout (2 to 3), padded from the member pool when short,… (skills/iig3d/scripts/iig3d.py:L359)
- Bad input: exit code 1, message on stdout as JSON. (skills/iig3d/scripts/iig3d.py:L36)
- Colour (skills/iig3d/scripts/iig3d.py:L416)
- .as_dict() (skills/iig3d/scripts/iig3d.py:L420)
- _nums() (skills/iig3d/scripts/iig3d.py:L424)
- normalise_colour() (skills/iig3d/scripts/iig3d.py:L428)
- Any CSS colour literal to #RRGGBB (alpha dropped); None when it is not a colour. (skills/iig3d/scripts/iig3d.py:L429)
- is_neutral() (skills/iig3d/scripts/iig3d.py:L457)
- Greys, near-white and near-black by the HSL rule: S < 15 %, L > 92 % or L < 10… (skills/iig3d/scripts/iig3d.py:L458)
- extract_palette() (skills/iig3d/scripts/iig3d.py:L464)
- Colours from a CSS file: custom properties in declaration order, then bare… (skills/iig3d/scripts/iig3d.py:L465)
- palette_paragraph() (skills/iig3d/scripts/iig3d.py:L511)
- Prompt (skills/iig3d/scripts/iig3d.py:L523)
- redact() (skills/iig3d/scripts/iig3d.py:L529)
- slugify() (skills/iig3d/scripts/iig3d.py:L533)
- _bullets() (skills/iig3d/scripts/iig3d.py:L537)
- render_layout_block() (skills/iig3d/scripts/iig3d.py:L541)
- The member's device layout as the markdown block the Layout Guidelines slot… (skills/iig3d/scripts/iig3d.py:L542)
- content_block() (skills/iig3d/scripts/iig3d.py:L558)
- text_labels() (skills/iig3d/scripts/iig3d.py:L582)
- word_count() (skills/iig3d/scripts/iig3d.py:L594)
- assemble() (skills/iig3d/scripts/iig3d.py:L598)
- Fill templates/base-prompt.md; warnings for text budget and item range; strict… (skills/iig3d/scripts/iig3d.py:L609)
- write_prompt() (skills/iig3d/scripts/iig3d.py:L660)
- prompts/NN-infographic-<slug>.md with NN the next free number; never overwrites. (skills/iig3d/scripts/iig3d.py:L661)
- parse_env_file() (skills/iig3d/scripts/iig3d.py:L677)
- Minimal .env parser: KEY=VALUE, optional `export `, quotes stripped, # comments… (skills/iig3d/scripts/iig3d.py:L678)
- api_key() (skills/iig3d/scripts/iig3d.py:L698)
- (key, source). Order: --api-key, ./.env in the calling directory, process… (skills/iig3d/scripts/iig3d.py:L699)
- exit_code() (skills/iig3d/scripts/iig3d.py:L722)
- load_prompt_text() (skills/iig3d/scripts/iig3d.py:L726)
- backup_existing() (skills/iig3d/scripts/iig3d.py:L735)
- _genai_client() (skills/iig3d/scripts/iig3d.py:L744)
- render() (skills/iig3d/scripts/iig3d.py:L750)
- Call Nano Banana Pro with the persisted prompt file and save an RGB PNG.… (skills/iig3d/scripts/iig3d.py:L763)
- Catalogue (skills/iig3d/scripts/iig3d.py:L78)
- .routing() (skills/iig3d/scripts/iig3d.py:L85)
- _add_common() (skills/iig3d/scripts/iig3d.py:L862)
- _add_prepare_args() (skills/iig3d/scripts/iig3d.py:L866)
- build_parser() (skills/iig3d/scripts/iig3d.py:L879)
- .layouts() (skills/iig3d/scripts/iig3d.py:L89)
- .member() (skills/iig3d/scripts/iig3d.py:L92)
- _split_vars() (skills/iig3d/scripts/iig3d.py:L920)
- prepare() (skills/iig3d/scripts/iig3d.py:L940)
- Shared front half of prompt and render: spec, route, aspect, refs, palette,… (skills/iig3d/scripts/iig3d.py:L941)
- cmd_render() (skills/iig3d/scripts/iig3d.py:L969)
- .ref_path() (skills/iig3d/scripts/iig3d.py:L98)
- dispatch() (skills/iig3d/scripts/iig3d.py:L989)

# Depends on
- [Member](/modules/member.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
