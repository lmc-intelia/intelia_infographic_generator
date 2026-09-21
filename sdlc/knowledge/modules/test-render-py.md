---
type: Module
title: test_render.py
description: "Graphify community 53: tests/conftest.py, tests/test_render.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:06:16Z" }
stale_after: "2026-10-05T05:06:16Z"
source_commit: 6ac4d77c7d0e6ad62e60d2fa01cebbade71dc4ca
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-17T11:22:55+10:00", digest: 889844ff3ec7d899 }
  - { id: test_render, resource: tests/test_render.py, last_modified: "2026-09-21T15:06:12+10:00", digest: cc0a045b263b7107 }
---

# Files
- `tests/conftest.py`
- `tests/test_render.py`

# Symbols
- png_bytes() (tests/conftest.py:L99)
- test_render.py (tests/test_render.py:L1)
- R11: dry-run shape, PNG save, backup rename, retries, exit codes; live smoke… (tests/test_render.py:L1)
- test_live_smoke() (tests/test_render.py:L105)
- test_bad_ref_image_is_error_not_traceback() (tests/test_render.py:L111)
- Review finding: failures before the API call must still yield the error record… (tests/test_render.py:L112)
- test_client_factory_failure_is_error() (tests/test_render.py:L120)
- test_quality_levels_are_one_model_and_its_image_sizes() (tests/test_render.py:L128)
- test_1k_uses_pro_model_with_image_size() (tests/test_render.py:L134)
- test_4k_uses_pro_model_with_image_size() (tests/test_render.py:L143)
- test_explicit_model_overrides_quality_model() (tests/test_render.py:L150)
- prompt_file() (tests/test_render.py:L16)
- test_dry_run_shape_and_no_file() (tests/test_render.py:L23)
- test_saves_png_and_flattens_rgba() (tests/test_render.py:L32)
- test_refs_passed_as_images_with_style_note() (tests/test_render.py:L48)
- test_backup_rename_on_rerun() (tests/test_render.py:L60)
- test_retry_then_error() (tests/test_render.py:L70)
- test_retry_then_success() (tests/test_render.py:L79)
- test_no_image_part_is_error() (tests/test_render.py:L86)
- test_exit_codes() (tests/test_render.py:L93)
- test_bad_resolution_rejected() (tests/test_render.py:L99)

# Depends on
- [conftest.py](/modules/conftest-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
