#!/usr/bin/env bash
# vault-hygiene.sh — list unchecked Obsidian tasks with 📅 due dates earlier than today.
# Usage: ./scripts/vault-hygiene.sh [vault-path]
# Default vault: $VAULT_PATH env var or hardcoded Pedro path.

set -euo pipefail

TODAY=$(date +%Y-%m-%d)
export TODAY
VAULT="${1:-${VAULT_PATH:-/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault}}"

if [[ ! -d "$VAULT" ]]; then
  echo "vault not found: $VAULT" >&2
  exit 1
fi

# /usr/bin/grep + perl to bypass RTK path-mangling on quoted vault path.
# BSD awk lacks 3-arg match — use perl for date extraction + comparison.
/usr/bin/grep -rn --include="*.md" -E '^- \[ \].*📅 [0-9]{4}-[0-9]{2}-[0-9]{2}' "$VAULT" 2>/dev/null \
  | /usr/bin/perl -ne '
      if (/📅 (\d{4}-\d{2}-\d{2})/ && $1 lt $ENV{TODAY}) {
        print;
      }
    '
