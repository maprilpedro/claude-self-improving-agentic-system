---
name: feedback-obsidian-reload-after-write
description: "Run `obsidian reload` after every filesystem create/update of a vault file so the app indexes it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 75def9b2-7431-4617-a2f8-4050b1882aed
---

After creating or updating any **Obsidian vault** file via filesystem `Write`/`Edit`, run `/Applications/Obsidian.app/Contents/MacOS/obsidian reload` so the running app picks it up. Standing instruction from Pedro 2026-06-22.

**Why:** Filesystem writes bypass Obsidian's file watcher/indexer (Google Drive stream mode + the app not re-scanning), so a new note exists on disk but does not appear in Pedro's file explorer or search until the vault reloads. Confirmed live 2026-06-22: a freshly written talking-points note was on disk + readable by path but invisible in the app until `obsidian reload`.

**How to apply:**
- Trigger only for **vault** files (under `…/My Drive/ObsidianVault/`). Repo edits (`knowledge/`, `.claude/memory/`) don't need it — they're not vault notes.
- Run once after a batch of vault writes is done, not per-edit, to avoid spamming reloads.
- Better long-term = a PostToolUse hook scoped to vault paths (offered; not yet wired). Until then, do it manually.
- Prefer obsidian-cli `create` for brand-new notes when practical (routes through the app, indexes directly) — see [[reference_obsidian_paths]] and the obsidian-cli skill.
