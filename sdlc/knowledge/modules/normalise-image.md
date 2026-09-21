---
type: Module
title: normalise_image
description: "Graphify community 43: skills/iig3d/scripts/iig3d.py"
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
- normalise_image() (skills/iig3d/scripts/iig3d.py:L1016)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L1017)
- to_rgb() (skills/iig3d/scripts/iig3d.py:L861)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L862)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L875)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L876)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
