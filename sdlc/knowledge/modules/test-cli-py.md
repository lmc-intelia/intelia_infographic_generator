---
type: Module
title: test_cli.py
description: "Graphify community 7: tests/test_cli.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:24:25Z" }
stale_after: "2026-10-01T01:24:25Z"
source_commit: 98b000f59040f64ed079923f41989f9b05d6b26b
sources:
  - { id: test_cli, resource: tests/test_cli.py, last_modified: "2026-09-17T11:24:21+10:00", digest: 93b8aa057c422b47 }
---

# Files
- `tests/test_cli.py`

# Symbols
- test_cli.py (tests/test_cli.py:L1)
- R1, R11, R16: the script imports as a module and exposes the subcommand table. (tests/test_cli.py:L1)
- test_remaining_commands_print_one_json() (tests/test_cli.py:L104)
- test_module_imports_and_has_main() (tests/test_cli.py:L12)
- run() (tests/test_cli.py:L17)
- test_list_counts() (tests/test_cli.py:L25)
- test_route_shape() (tests/test_cli.py:L34)
- test_refs_shape() (tests/test_cli.py:L40)
- test_palette_shape() (tests/test_cli.py:L45)
- test_prompt_writes_file() (tests/test_cli.py:L50)
- test_render_dry_run() (tests/test_cli.py:L58)
- test_render_without_key_exits_1() (tests/test_cli.py:L71)
- test_render_with_fake_client() (tests/test_cli.py:L80)
- test_usage_error_is_json_exit_1() (tests/test_cli.py:L92)
- test_render_requires_out_dir() (tests/test_cli.py:L97)

# Depends on
- no EXTRACTED edges to other modules

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
