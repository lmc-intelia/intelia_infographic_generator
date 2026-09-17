set dotenv-load := true

# A venv activated for a sibling project (the checkout this repo split from)
# leaks in through VIRTUAL_ENV and makes every `uv` call warn about the mismatch. uv
# already ignores it and uses ./.venv; blanking it here drops the warning, not the venv.
export VIRTUAL_ENV := ""

# interactive Gemini shell, approvals off
g_session:
    @gemini --approval-mode yolo

# interactive Claude shell on Opus, permissions off
opus:
    @claude --dangerously-skip-permissions --model opus "/caveman"

# interactive Claude shell on Fable, permissions off
fable:
    @claude --dangerously-skip-permissions --model fable "/caveman"

# install pre-commit hooks into .git/hooks (keeps the sdlc post-commit block)
hooks:
    @uv run pre-commit install --install-hooks

# run every pre-commit hook against the whole tree
lint:
    @uv run pre-commit run --all-files

# run the test suite
test:
    @uv run pytest -q

# symlink skills/iig3d into ~/.claude/skills and .claude/skills (refuses to replace a real directory)
install-local:
    #!/usr/bin/env bash
    set -euo pipefail
    src="$(pwd)/skills/iig3d"
    for target in "$HOME/.claude/skills/iig3d" ".claude/skills/iig3d"; do
        if [ -e "$target" ] && [ ! -L "$target" ]; then
            echo "refusing: $target is a real directory" >&2; exit 1
        fi
    done
    mkdir -p "$HOME/.claude/skills" .claude/skills
    ln -sfn "$src" "$HOME/.claude/skills/iig3d"
    ln -sfn "../../skills/iig3d" ".claude/skills/iig3d"
    echo "linked $HOME/.claude/skills/iig3d and .claude/skills/iig3d -> $src"

# remove only the symlinks install-local made
uninstall-local:
    #!/usr/bin/env bash
    set -euo pipefail
    for target in "$HOME/.claude/skills/iig3d" ".claude/skills/iig3d"; do
        if [ -L "$target" ]; then rm "$target"; echo "removed $target"; fi
    done

# validate the iig3d catalogue, refs and generated docs
iig3d-check:
    @uv run skills/iig3d/scripts/iig3d.py check

# sdlc deploy command: dev and staging install the skill locally; production is the merged PR
deploy env:
    #!/usr/bin/env bash
    set -euo pipefail
    case "{{env}}" in
        dev|staging) just install-local ;;
        production) echo "production release = merge the PR on GitHub; nothing to run locally" >&2; exit 1 ;;
        *) echo "unknown environment {{env}}" >&2; exit 2 ;;
    esac
