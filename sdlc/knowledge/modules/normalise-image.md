---
type: Module
title: normalise_image
description: "Graphify community 50: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:30:53Z" }
stale_after: "2026-10-05T04:30:53Z"
source_commit: 71c08107aa2dfcc1db57f7b3771bfd7713d219d0
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-21T14:30:49+10:00", digest: fe9bead68c7c4cae }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L1004)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L1005)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L1145)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L1146)
- to_rgb() (skills/iig3d/scripts/iig3d.py:L990)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L991)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
