---
type: Module
title: normalise_image
description: "Graphify community 45: skills/iig3d/scripts/iig3d.py"
resource: skills/iig3d/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T02:19:39Z" }
stale_after: "2026-10-01T02:19:39Z"
source_commit: 1c44ce7af8f81c51eaf6b7d3b08e5cffeb7b73da
sources:
  - { id: iig3d, resource: skills/iig3d/scripts/iig3d.py, last_modified: "2026-09-17T12:19:34+10:00", digest: 6abb96a301e9dd69 }
---

# Files
- `skills/iig3d/scripts/iig3d.py`

# Symbols
- to_rgb() (skills/iig3d/scripts/iig3d.py:L754)
- Flatten any PIL mode to RGB; alpha composites onto `background`. (skills/iig3d/scripts/iig3d.py:L755)
- _image_from_response() (skills/iig3d/scripts/iig3d.py:L768)
- First inline image part of a Gemini response as an RGB PIL image; None when… (skills/iig3d/scripts/iig3d.py:L769)
- normalise_image() (skills/iig3d/scripts/iig3d.py:L909)
- Copy `src` to `dest` as an RGB JPEG no larger than `max_edge` on its long side. (skills/iig3d/scripts/iig3d.py:L910)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
