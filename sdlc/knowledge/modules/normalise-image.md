---
type: Module
title: normalise_image
description: "Graphify community 50: skills/iig3d/scripts/iig3d.py"
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
- to_rgb() (skills/iig3d/scripts/iig3d.py:L1234)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L1235)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L1310)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L1311)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L1461)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L1462)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
