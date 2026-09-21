---
type: Module
title: normalise_image
description: "Graphify community 50: skills/iig3d/scripts/iig3d.py"
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
- to_rgb() (skills/iig3d/scripts/iig3d.py:L1216)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L1217)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L1230)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L1231)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L1374)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L1375)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
