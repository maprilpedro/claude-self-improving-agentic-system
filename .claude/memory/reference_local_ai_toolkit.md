---
name: reference_local_ai_toolkit
description: The local AI content toolkit (podcast-script / digest / journal skills), the claude⇄qwen engine switch, and the launchd journal schedule — what exists, where, and how to maintain it.
metadata:
  type: reference
---

Built 2026-06-21 by porting the content-generation pieces of **Open Notebook** (github.com/lfnovo/open-notebook, a self-hosted NotebookLM alternative) natively into Claude Code. NOT the full app — no Docker/SurrealDB/TTS/audio. Three user-invocable skills, each with a transparent **engine switch**:

- **`/podcast-script`** — generates the *read* podcast script (outline → per-segment dialogue chain, ported from the `podcast-creator` package). 4 PM profiles. FR default.
- **`/digest`** — applies a reusable PM extraction template to a source (Open Notebook "Transformations"). 5 templates: exec / decisions / risks / actions / sowhat. EN default.
- **`/journal`** — `today|yesterday|weekly|lastweek` rollup of vault notes touched in the window. Scans the whole `2026/` tree, ranks by Obsidian frontmatter date (`date modified`→`date created`→fs-mtime, sync-independent), map-reduce on large sets (no silent truncation), thin-week (<2 notes) → propose candidates from memory. EN default.

**Engine switch (the key idea):** `claude` (default) = Claude runs it in-context (fresh vault read + project memory + session synthesis; content → Anthropic). `qwen` (via `--qwen` or "local/privé/sensible") = a self-contained `*_local.py` runs against **local Ollama (Qwen3-30B-a3b-instruct, 64K ctx)** and returns ONLY metadata — sensitive Adobe-internal content never enters Claude's context. Output header tags the engine. Templates encode Pedro's rules (decision≠proposal, forward-looking actions, position-over-merit).

**Scope = GLOBAL** (all projects). Git source of record = this repo's `.skillshare/skills/`; global holds **copies** (skillshare ignores symlinked sources) in `~/.config/skillshare/skills/` → linked into `~/.claude/skills` (claude) + `~/.agents/skills` (warp). Project copies removed via `.skillshare/skills/.skillignore` to avoid an in-repo duplicate. **After editing any of these skills, run `cron/deploy_skills_global.sh`** to propagate repo→global (global does NOT auto-track the repo — silent-drift risk otherwise).

**Journal schedule (launchd, on the mac — jobs live in `~/Library/LaunchAgents/`, NOT in the repo):** `com.pedro.journal.daily` = weekdays 18:00 → `/journal today`; `com.pedro.journal.weekly` = Fri 13:00 → `/journal weekly`. Both run `cron/run_journal.sh` → **claude headless** (`claude -p`, scoped `--allowed-tools`, NOT permission-bypass). Needs the mac awake + Claude auth in the cron env; each run = real Claude usage. Logs in `~/Library/Logs/journal-cron/`. Remove with `launchctl bootout gui/$(id -u)/com.pedro.journal.{daily,weekly}`. Concrete instance of [[feedback_simple_local_reminders]]. Commits: `557e752`, `7306616`, `0850830`.
