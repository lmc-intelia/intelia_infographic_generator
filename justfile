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
