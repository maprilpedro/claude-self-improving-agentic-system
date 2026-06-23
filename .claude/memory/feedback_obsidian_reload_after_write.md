---
name: feedback-obsidian-reload-after-write
description: "Do NOT auto-run `obsidian reload` after vault writes — Pedro finds it too much. Let the app pick up changes on its own."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 75def9b2-7431-4617-a2f8-4050b1882aed
---

**Do NOT run `obsidian reload` after filesystem writes to vault files.** Reverses the prior standing instruction. Pedro 2026-06-23: *"reloading Obsidian each time is too much. Don't do it anymore please."*

**Why the reversal:** the manual reload was firing on essentially every vault edit (trio syncs, Status updates), which is too noisy / disruptive on his side. The cost of running it outweighs the indexing benefit for him. The underlying indexing lag is real (filesystem writes bypass the watcher under Google Drive stream mode — confirmed 2026-06-22), but Pedro would rather the app catch up on its own / refresh manually than have Claude reload it.

**How to apply:**
- After filesystem `Write`/`Edit` on vault files: just say what changed and where. **Do not** call `obsidian reload`.
- If index freshness genuinely matters for a follow-up step (search/backlinks right after a write), prefer the **obsidian-cli** skill for that operation (routes through the app, indexes directly) rather than a filesystem write + reload — see [[reference_obsidian_paths]].
- Only reload if Pedro explicitly asks for it.
