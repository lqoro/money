#!/bin/bash
# One-time setup to run Trencher nonstop on a Mac (paper trading only).
#   cd ~/money && bash deploy/mac/setup.sh
# Safe to run again: it updates the launchd job in place.
set -euo pipefail
cd "$(dirname "$0")/../.."
REPO="$(pwd)"
LABEL="com.trencher.agent"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
LIVE_BRANCH="trencher-live"
LIVE_DIR="$REPO/../trencher-live"

say() { printf '\n==> %s\n' "$*"; }

say "Python environment"
command -v python3 >/dev/null || { echo "Install Python 3 first (brew install python)."; exit 1; }
[ -d .venv ] || python3 -m venv .venv
.venv/bin/pip install -q -r requirements.txt

say "Claude Code (the brain runs on your Claude plan through it)"
if ! command -v claude >/dev/null; then
  echo "Claude Code isn't installed. Install it, log in once with 'claude', then run this again:"
  echo "  npm install -g @anthropic-ai/claude-code"
  exit 1
fi
echo "found $(command -v claude)"

say ".env"
if [ ! -f .env ]; then
  cp .env.example .env
  echo "created .env from .env.example"
fi
# set_env KEY VALUE [REPLACEABLE]: set KEY in .env when it's missing, blank, or equal to
# REPLACEABLE (the .env.example default). Any other value you chose is kept.
set_env() {
  local key="$1" value="$2" replaceable="${3:-}" current
  if ! grep -q "^$key=" .env; then
    printf '%s=%s\n' "$key" "$value" >> .env
  else
    current="$(grep "^$key=" .env | tail -1 | cut -d= -f2-)"
    if [ -z "$current" ] || [ "$current" = "$replaceable" ]; then
      awk -v k="$key" -v v="$value" 'index($0, k "=") == 1 { print k "=" v; next } { print }' .env > .env.tmp
      mv .env.tmp .env
    fi
  fi
  echo "$key=$(grep "^$key=" .env | tail -1 | cut -d= -f2-)"
}
set_env DUET_SYNC_DIR "$(cd "$REPO/.." && pwd)/trencher-live"
# Restarts on code merged to main. To opt out, set AUTO_UPDATE=no in .env.
set_env AUTO_UPDATE true false

say "Shared branch with Claude Duet ($LIVE_BRANCH at $LIVE_DIR)"
if [ ! -d "$LIVE_DIR/.git" ] && [ ! -f "$LIVE_DIR/.git" ]; then
  git fetch -q origin
  if git ls-remote --exit-code --heads origin "$LIVE_BRANCH" >/dev/null; then
    git worktree add -q -B "$LIVE_BRANCH" "$LIVE_DIR" "origin/$LIVE_BRANCH"
  else
    git worktree add -q --detach "$LIVE_DIR"
    git -C "$LIVE_DIR" checkout -q --orphan "$LIVE_BRANCH"
    git -C "$LIVE_DIR" rm -rfq .
    echo '{"pause_new_trades": false, "settings": {}, "owner_note": ""}' > "$LIVE_DIR/steer.json"
    git -C "$LIVE_DIR" add steer.json
    git -C "$LIVE_DIR" commit -q -m "Start the Trencher live branch"
    git -C "$LIVE_DIR" push -q -u origin "$LIVE_BRANCH"
  fi
fi
git -C "$LIVE_DIR" push -q --dry-run origin "HEAD:$LIVE_BRANCH" \
  || { echo "This Mac can't push to GitHub yet. Log in with 'gh auth login' (or set up git credentials) and run again."; exit 1; }

say "Brain check"
set -a; . ./.env; set +a
.venv/bin/python -m agent brain || echo "The brain didn't answer. Run 'claude' once and log in, or run 'claude setup-token' and put the token in .env as CLAUDE_CODE_OAUTH_TOKEN."

say "launchd job ($LABEL)"
mkdir -p "$HOME/Library/LaunchAgents" "$REPO/memory"
chmod +x "$REPO/deploy/mac/run.sh"
cat > "$PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key><array><string>$REPO/deploy/mac/run.sh</string></array>
  <key>WorkingDirectory</key><string>$REPO</string>
  <key>EnvironmentVariables</key>
  <dict><key>PATH</key><string>$PATH</string></dict>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>ThrottleInterval</key><integer>30</integer>
  <key>StandardOutPath</key><string>$REPO/memory/launchd.log</string>
  <key>StandardErrorPath</key><string>$REPO/memory/launchd.log</string>
</dict>
</plist>
PLIST
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"

say "Done. Trencher is running and restarts on its own."
echo "  log:     tail -f $REPO/memory/agent.log"
echo "  status:  cd $REPO && .venv/bin/python -m agent status"
echo "  stop:    launchctl bootout gui/\$(id -u)/$LABEL"
echo
echo "Keep the Mac awake: System Settings > Energy > 'Prevent automatic sleeping when the display is off'."
