---
name: CLI binaries playbook (yq/comby/sd/scc/difft/shellcheck/ast-grep)
description: When to reach for each binary in this repo. yq+comby+sd+scc+difft are workhorses for memory/knowledge ops; shellcheck+ast-grep reserved for future code surface.
type: reference
---

# CLI Binaries — When to Use Which

All 7 installed via Homebrew. Repo is 67 markdown + 1 JSON (no code today), so tool fit skews to text/markdown ops.

## High-fit (use by default)

### yq — memory frontmatter
Memory files = YAML frontmatter (`name` / `description` / `type`) + markdown body. Use yq to read, validate, batch-update metadata.

```bash
# List all memories by type
for f in .claude/memory/*.md; do
  yq -f extract --front-matter=extract '.type + " | " + .name' "$f" 2>/dev/null
done

# Find memories missing description
for f in .claude/memory/*.md; do
  yq -f extract --front-matter=extract 'select(.description == null) | .name' "$f"
done

# Update type field in place
yq -i --front-matter=process '.type = "feedback"' file.md
```

Reach for yq when: validating memory metadata, finding orphans, batch-updating frontmatter, generating MEMORY.md index from disk truth.

### comby — multi-line structural rewrites in markdown
Better than sed/sd for templated patterns spanning multiple lines.

```bash
# Rewrite "Why:" / "How to apply:" blocks to new template
comby ':[old]Why: :[reason]\n:[old]How to apply: :[how]' \
      'Reason: :[reason]\nApply: :[how]' \
      .claude/memory -matcher .md

# Renumber hypotheses across files
comby 'H-:[n]' 'HYP-:[n]' knowledge/hypotheses -matcher .md
```

Reach for comby when: knowledge entry template evolves, mass-rename across markdown, restructure INDEX.md tables.

### sd — surgical find/replace
Drop-in for sed; simpler regex syntax.

```bash
sd 'tomorrow' '2026-05-04' file.md
sd 'Bertrand(?! Hardy)' 'Bertrand Hardy' .claude/memory/*.md
```

Reach for sd when: single-string mass swap, quicker than Edit tool for simple regex replace.

### scc — inventory metric
Fast LOC counter. Good for system-review cadence.

```bash
scc knowledge/                    # total
scc knowledge/leadership/         # per-folder
scc --by-file knowledge/ | head   # biggest files
```

Reach for scc when: system review (every ~2 weeks per global rule), tracking knowledge folder growth, finding bloated entries.

### difft — semantic diff
Markdown noise drops vs `git diff`.

```bash
GIT_EXTERNAL_DIFF=difft git diff knowledge/
GIT_EXTERNAL_DIFF=difft git show <sha>
```

Reach for difft when: reviewing knowledge/memory edits, scanning recent commits, pre-commit during consolidation passes.

## Low-fit today (defensive, kept for future)

### shellcheck
No shell scripts in repo today. Use when hooks land in settings.json with shell scripts.

### ast-grep
No code surface today. Use if skills/agents grow TypeScript/Python.

## Default tool order by task

| Task | Order |
|---|---|
| Find/list memory by metadata | yq → grep |
| Validate MEMORY.md matches disk | yq + sd |
| Mass restructure knowledge entry format | comby |
| Single-string rename across .md | sd > sed |
| Reviewing diff before commit | difft |
| System review inventory | scc |
| Routine grep | rtk grep (existing) |
