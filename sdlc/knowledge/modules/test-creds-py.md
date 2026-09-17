---
type: Module
title: test_creds.py
description: "Graphify community 21: tests/test_creds.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.3.5, at: "2026-09-17T01:21:39Z" }
stale_after: "2026-10-01T01:21:39Z"
source_commit: 646c305c3cf5097475ddbd17e3f8940ff9f1afdb
sources:
  - { id: test_creds, resource: tests/test_creds.py, last_modified: "2026-09-17T11:21:36+10:00", digest: 4c40dd0d7e15dc03 }
---

# Files
- `tests/test_creds.py`

# Symbols
- test_creds.py (tests/test_creds.py:L1)
- R10: GEMINI_API_KEY from ./.env in the calling directory, then the environment;… (tests/test_creds.py:L1)
- test_dotenv_in_cwd_wins_over_environment() (tests/test_creds.py:L14)
- test_google_key_accepted() (tests/test_creds.py:L23)
- test_environment_when_no_dotenv() (tests/test_creds.py:L29)
- test_explicit_key_wins() (tests/test_creds.py:L35)
- test_parent_dotenv_ignored() (tests/test_creds.py:L42)
- test_key_value_never_in_source() (tests/test_creds.py:L52)
- test_parse_env_file() (tests/test_creds.py:L59)

# Depends on
- [test_prompt.py](/modules/test-prompt-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [iig3d skill](/features/iig3d-skill.md)
