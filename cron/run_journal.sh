#!/bin/bash
# Scheduled /journal runner — claude headless engine. Invoked by launchd.
# Usage: run_journal.sh <today|weekly>
PERIOD="${1:-today}"
PROJECT="/Users/pedrofer/GitHub/claude-self-improving-agentic-system"
LOGDIR="$HOME/Library/Logs/journal-cron"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/journal-$PERIOD.log"

# launchd runs with a minimal PATH — restore what claude + tools need
export PATH="/Users/pedrofer/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

{
  echo "===== $(date '+%F %T') /journal $PERIOD ====="
  cd "$PROJECT" || { echo "cd failed"; exit 1; }
  # claude engine (default, no --qwen): reads fresh vault + project memory, writes the entry.
  # Scoped allowlist — NOT a permission bypass. Only the tools the journal needs:
  #   Bash(python3:*) = the --list-only file selection; Bash(obsidian:*) = vault writes;
  #   Read = read the period notes; Write = write the journal file; Glob/Grep = locate notes.
  claude -p "/journal $PERIOD" \
    --permission-mode default \
    --allowed-tools 'Bash(python3:*)' 'Bash(obsidian:*)' 'Read' 'Write' 'Glob' 'Grep'
  echo "----- claude exit $? -----"
} >> "$LOG" 2>&1
