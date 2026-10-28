#!/bin/bash
# Started by launchd (see setup.sh). Pulls merged changes, then runs Trencher.
# When Trencher sees a newer main it exits, and launchd starts this script again.
set -u
cd "$(dirname "$0")/../.."
if [ -f .env ]; then set -a; . ./.env; set +a; fi

if [ "${AUTO_UPDATE:-false}" = "true" ]; then
  branch="${AUTO_UPDATE_BRANCH:-main}"
  if git fetch -q origin "$branch" && git merge --ff-only -q "origin/$branch"; then
    .venv/bin/pip install -q -r requirements.txt || true
  else
    echo "auto-update: couldn't fast-forward to origin/$branch, running the current code" >&2
    export TRENCHER_UPDATE_FAILED=1  # so Trencher doesn't restart-loop on the same update
  fi
fi

exec .venv/bin/python -m agent run
