---
type: Module
title: test_add.py
description: "Graphify community 34: tests/test_add.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T04:05:37Z" }
stale_after: "2026-10-05T04:05:37Z"
source_commit: 7ba9fba7a655769a839ae420f00e5a62beab9810
sources:
  - { id: test_add, resource: tests/test_add.py, last_modified: "2026-09-21T13:02:34+10:00", digest: 712ddea1b5e34cf8 }
---

# Files
- `tests/test_add.py`

# Symbols
- test_add.py (tests/test_add.py:L1)
- R13: add a user image as a first-class reference; new members need no Python… (tests/test_add.py:L1)
- write_meta() (tests/test_add.py:L10)
- test_ids_increment_past_highest() (tests/test_add.py:L105)
- test_normalise_image_small_stays_small() (tests/test_add.py:L111)
- test_new_member_name_must_be_slug() (tests/test_add.py:L120)
- Review finding: a member name is a path segment; only 3d-[a-z0-9-]+ is allowed. (tests/test_add.py:L121)
- test_user_added_watermark_is_reported() (tests/test_add.py:L133)
- Review finding (R21): a watermarked user image is registered but check must say… (tests/test_add.py:L134)
- test_add_with_variant_and_item_count_returns_pin() (tests/test_add.py:L144)
- test_add_unknown_variant_rejected() (tests/test_add.py:L158)
- test_add_to_existing_member() (tests/test_add.py:L16)
- test_add_bad_item_count_rejected() (tests/test_add.py:L166)
- test_add_new_member_with_variant() (tests/test_add.py:L173)
- test_regenerated_entry_keeps_key_order_and_origin() (tests/test_add.py:L185)
- test_new_member() (tests/test_add.py:L37)
- test_replace_missing_file_entry() (tests/test_add.py:L59)
- test_existing_entry_with_file_on_disk_rejected() (tests/test_add.py:L72)
- test_meta_missing_key_named() (tests/test_add.py:L80)
- test_bad_flag_and_unknown_pairing_rejected() (tests/test_add.py:L89)
- test_member_and_new_member_exclusive() (tests/test_add.py:L99)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
