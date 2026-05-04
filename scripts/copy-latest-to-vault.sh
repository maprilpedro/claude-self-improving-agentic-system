#!/usr/bin/env bash
# copy-latest-to-vault.sh — copy newest .md from EH project (excluding doc/) to Obsidian vault.
# Wired into Claude Code Stop hook in .claude/settings.local.json.

set -euo pipefail

SRC="${1:-/Users/pedrofer/GitHub/claude-self-improving-agentic-system/projects/adbe-experience-hub}"
DEST="${2:-/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/}"
LOG="${COPY_LATEST_LOG:-/tmp/copy-latest-to-vault.log}"

log() { printf '[%s] %s\n' "$(date -u +%FT%TZ)" "$*" >>"$LOG"; }

if [[ ! -d "$SRC" ]]; then
  log "src missing: $SRC"
  exit 0
fi

if [[ ! -d "$DEST" ]]; then
  log "dest missing: $DEST"
  exit 0
fi

# Pick newest .md by mtime, space/newline-safe via stat + null sort.
LATEST=$(
  find "$SRC" -type f -name '*.md' -not -path '*/doc/*' -exec stat -f '%m %N' {} + \
    | sort -rn \
    | head -n 1 \
    | cut -d' ' -f2-
)

if [[ -z "$LATEST" ]]; then
  log "no .md found in $SRC"
  exit 0
fi

if cp "$LATEST" "$DEST"; then
  log "copied: $LATEST -> $DEST"
else
  log "copy failed: $LATEST -> $DEST"
  exit 1
fi
