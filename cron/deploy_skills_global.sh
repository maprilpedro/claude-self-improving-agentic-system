#!/bin/bash
# Redeploy this repo's skills to the GLOBAL skillshare (claude + warp targets),
# so they're available in every project. Run after editing any of these skills —
# global holds COPIES (skillshare ignores symlinked sources), so edits here do NOT
# auto-propagate. This script is the propagation step.
set -e
REPO_SKILLS="/Users/pedrofer/GitHub/claude-self-improving-agentic-system/.skillshare/skills"
G="$HOME/.config/skillshare/skills"
for s in podcast-script digest journal; do
  rsync -a --delete --exclude='__pycache__' --exclude='*.pyc' "$REPO_SKILLS/$s/" "$G/$s/"
  echo "deployed $s -> global"
done
skillshare sync --global
echo "Global skills updated (claude + warp)."
