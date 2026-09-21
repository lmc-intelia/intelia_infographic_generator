---
type: Module
title: test_catalogue.py
description: "Graphify community 3: tests/test_catalogue.py, tests/test_routing.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-21T05:30:03Z" }
stale_after: "2026-10-05T05:30:03Z"
source_commit: fae00c698effe61c7083ae8264ab6a14d68f8f09
sources:
  - { id: test_catalogue, resource: tests/test_catalogue.py, last_modified: "2026-09-21T12:47:39+10:00", digest: 47594ced5e7dd9e2 }
  - { id: test_routing, resource: tests/test_routing.py, last_modified: "2026-09-21T12:34:05+10:00", digest: 68018c1e94cbf3f7 }
---

# Files
- `tests/test_catalogue.py`
- `tests/test_routing.py`

# Symbols
- test_catalogue.py (tests/test_catalogue.py:L1)
- R3, R15: the YAML catalogue is complete, internally consistent and schema-valid. (tests/test_catalogue.py:L1)
- test_schema_rejects_missing_fragment() (tests/test_catalogue.py:L106)
- test_ref_files_on_disk() (tests/test_catalogue.py:L118)
- test_no_vendored_watermark() (tests/test_catalogue.py:L130)
- test_check_clean() (tests/test_catalogue.py:L136)
- Shipped catalogue is clean once user-added watermarks are accepted; every… (tests/test_catalogue.py:L137)
- test_check_reports_seeded_violations() (tests/test_catalogue.py:L143)
- test_check_dependency_parity() (tests/test_catalogue.py:L169)
- cat() (tests/test_catalogue.py:L43)
- test_fifteen_members() (tests/test_catalogue.py:L47)
- test_member_keys() (tests/test_catalogue.py:L52)
- test_fragment_ends_with_negative_list() (tests/test_catalogue.py:L60)
- test_routing_rows() (tests/test_catalogue.py:L65)
- test_pairings_resolve() (tests/test_catalogue.py:L74)
- test_ref_flags() (tests/test_catalogue.py:L85)
- test_alternates_exist() (tests/test_catalogue.py:L93)
- test_family_constants() (tests/test_catalogue.py:L98)
- test_routing.py (tests/test_routing.py:L1)
- R4: industrial-3d routes by layout; a named member skips the table; unknown… (tests/test_routing.py:L1)
- test_split_style() (tests/test_routing.py:L115)
- test_split_style_ref_without_member_layout_fails() (tests/test_routing.py:L119)
- cat() (tests/test_routing.py:L35)
- test_general_layout_routes_to_primary() (tests/test_routing.py:L41)
- test_device_layout_returns_member() (tests/test_routing.py:L51)
- test_explicit_member_style_skips_table() (tests/test_routing.py:L59)
- test_layout_defaults_to_member_device() (tests/test_routing.py:L66)
- test_no_layout_no_style_defaults_to_bento_grid() (tests/test_routing.py:L72)
- test_unknown_layout_lists_valid_names() (tests/test_routing.py:L78)
- test_unknown_style_lists_valid_names() (tests/test_routing.py:L84)
- test_pinned_member_sets_style_and_default_layout() (tests/test_routing.py:L90)
- test_pinned_member_conflicts_with_explicit_style() (tests/test_routing.py:L97)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
