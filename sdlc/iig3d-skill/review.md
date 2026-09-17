# Review: iig3d skill
From: spec.md (2026-09-17). Status: draft. Risk: low.

Reviewer: `sdlc:reviewer` agent against REVIEW.md, spec.md (R1 to R21), plan.md and `git diff 1fc0d20...HEAD`.
Verifier: `sdlc:verifier` agent ran every plan.md Proof command; all matched except the `grep -rl watermark`
line, which matched the words "no watermarks" in every prompt fragment (plan corrected to grep for the flag).
Every Important finding below was fixed in one red→green cycle (`build red|green review-fixes`, 9 failing tests
then 291 passing) and re-checked.

## Bugs
- Important: skills/iig3d/scripts/iig3d.py:849 `render()` opened reference images and built the client outside the retry `try`, so an unreadable `--ref` or a client error escaped as a traceback with exit 1 instead of the `{"status":"error"}` record and exit 2 (R11). Fixed: setup is inside the error envelope; `tests/test_render.py::test_bad_ref_image_is_error_not_traceback` and `::test_client_factory_failure_is_error`.
- Important: skills/iig3d/scripts/iig3d.py:691 `write_prompt` matched `^(\d{2})-`, so after 99 prompt files every later prompt overwrote `100-...` (R8 never overwrites). Fixed: `^(\d+)-`; `tests/test_prompt.py::test_write_prompt_past_ninety_nine`.
- Nit: skills/iig3d/scripts/iig3d.py:1331 `check()` ran `_dry_assembly` only when nothing else failed, hiding ref-rule violations behind a stale doc. Fixed: always runs.
- Nit: skills/iig3d/scripts/iig3d.py:610 the R9 word budget ignored item `detail` and stat captions. Fixed: counted.
- Nit: skills/iig3d/scripts/iig3d.py:495 `--palette-vars` skipped the duplicate drop and the 8-colour cap. Fixed: applied (neutrals stay when named explicitly).

## Security
- Important: skills/iig3d/scripts/iig3d.py:945 `new_member.name` was only checked for the `3d-` prefix, so `name: "3d-../../../pwned"` wrote a JPEG and a YAML outside the catalogue. Fixed: name must match `^3d-[a-z0-9]+(?:-[a-z0-9]+)*$`; `tests/test_add.py::test_new_member_name_must_be_slug` (four bad names, no file escapes).
- Nit: justfile:1 `set dotenv-load := true` exports `GEMINI_API_KEY` from `./.env` into every recipe's environment, including the two agent shells. Left as is: the recipe file predates the skill and the owner chose it; `render` reads `./.env` itself so the setting is not needed by the skill.

Checked clean: the key value never reaches stdout, the prompt file, YAML or logs (stderr prints only `<cwd>/.env:GEMINI_API_KEY`); `./.env` only, no parent walk; YAML loaded with SafeLoader/CSafeLoader; `.env` git-ignored; ref file names pass through `slugify`.

## Compliance
- Important: skills/iig3d/scripts/iig3d.py:1306 R21's guard was off for anything `add` wrote: `check()` waived the watermark rule for every `user_added` ref and `add_ref` called `check(allow_watermark=True)`, so a watermarked stock image added later reported clean. Fixed: a watermark flag is a violation unless `--allow-watermark` is passed and the ref is user-added; `add` returns `status: violations` and names the file; `tests/test_add.py::test_user_added_watermark_is_reported`, `tests/test_catalogue.py::test_check_reports_seeded_violations` (vendored watermark fails even with `--allow-watermark`).
- Important: tests/test_refs.py:18 R5's "never two watermark refs" was not pinned: the shipped catalogue has no watermark flags since the R21 regeneration, so the assertions ran over an empty set. Fixed: a `flagged` fixture restores the source flags in memory; `test_never_two_watermarks_even_when_pairing_names_two` and `test_low_res_alone_gets_company` pin both rules through `pick_style_refs` and `ref_rule_violations`.
- Nit: .gitignore:5 ignores `infographic/` while spec R19 said output directories are not ignored. Fixed in the spec text (the ignore is deliberate; step 15 of the plan).

Nits not addressed (8, per the cap): `redact()` also masks any 40-character token; `item.icon` and the file slug bypass `redact`; regenerated refs record scratchpad paths in `source.path`; `list` has no explicit `--json` flag (output is always JSON); `aspect_snapped_from` surfaces as a warning only; `pick_style_refs` can return four refs when the low-res rescue fires; `tests/test_cli.py` runs `docs` against the real skill root; the plan's watermark grep wording (fixed in plan.md).
