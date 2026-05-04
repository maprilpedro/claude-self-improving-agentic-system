#!/usr/bin/env bash
# check-memory-index.sh — diff .claude/memory/*.md frontmatter against MEMORY.md pointers.
# Surfaces:
#   ORPHAN          — memory file with no pointer in MEMORY.md
#   BROKEN          — MEMORY.md pointer references a file that doesn't exist
#   MISSING-TYPE    — memory file with no `type:` frontmatter
#   UNKNOWN-TYPE    — type is not in {user,feedback,project,reference}
#   SECTION-MISMATCH — pointer lives under wrong MEMORY.md heading for its type
# Exit 0 = clean, 1 = drift detected.

set -euo pipefail

MEM_DIR="${1:-/Users/pedrofer/GitHub/claude-self-improving-agentic-system/.claude/memory}"
INDEX="$MEM_DIR/MEMORY.md"

if [[ ! -f "$INDEX" ]]; then
  echo "MEMORY.md not found: $INDEX" >&2
  exit 2
fi

section_for() {
  case "$1" in
    user)      echo "User" ;;
    feedback)  echo "Feedback" ;;
    project)   echo "Projects" ;;
    reference) echo "References" ;;
    *)         echo "" ;;
  esac
}

EXIT=0

# 1. Broken links — every (foo.md) in MEMORY.md must resolve to a real file.
while IFS= read -r ref; do
  [[ -z "$ref" ]] && continue
  if [[ ! -f "$MEM_DIR/$ref" ]]; then
    echo "BROKEN: MEMORY.md links $ref but file missing"
    EXIT=1
  fi
done < <(grep -oE '\([^)]+\.md\)' "$INDEX" | tr -d '()' | sort -u)

# 2. Per-file checks.
for f in "$MEM_DIR"/*.md; do
  base=$(basename "$f")
  [[ "$base" == "MEMORY.md" ]] && continue

  type=$(yq --front-matter=extract '.type' "$f" 2>/dev/null || echo "")

  if [[ -z "$type" || "$type" == "null" ]]; then
    echo "MISSING-TYPE: $base has no frontmatter type"
    EXIT=1
    continue
  fi

  if ! grep -qF "($base)" "$INDEX"; then
    echo "ORPHAN: $base (type=$type) has no pointer in MEMORY.md"
    EXIT=1
    continue
  fi

  expected=$(section_for "$type")
  if [[ -z "$expected" ]]; then
    echo "UNKNOWN-TYPE: $base type=$type not in {user,feedback,project,reference}"
    EXIT=1
    continue
  fi

  actual=$(awk -v target="($base)" '
    /^## / { sec = substr($0, 4); next }
    index($0, target) { print sec; exit }
  ' "$INDEX")

  if [[ "$actual" != "$expected" ]]; then
    echo "SECTION-MISMATCH: $base type=$type under '$actual', expected '$expected'"
    EXIT=1
  fi
done

if [[ $EXIT -eq 0 ]]; then
  count=$(grep -cE '^- \[' "$INDEX" || true)
  echo "memory index clean ($count pointers, all sections match)"
fi

exit $EXIT
