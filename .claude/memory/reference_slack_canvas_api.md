---
name: reference_slack_canvas_api
description: Slack canvas update gotchas — section-targeted replace is destructive/erratic; full-content replace (no section_id, no H1) is the safe mode; mentions read as <@ID> but must be WRITTEN as ![](@ID).
metadata:
  type: reference
---

# Slack canvas API — editing gotchas (learned the hard way, 2026-07-03, GA Readiness canvas F0BD4RALNHF)

1. **Never trust section-targeted `replace`.** Observed behavior is erratic: replacing a paragraph consumed the *following* sibling blocks (Key/Cutover sections wiped); replacing a table emptied the table's cells and inserted the new content *after* it; replacing with empty content deleted the *next* section (lost a good table). Three incidents in one session.
2. **The safe mode = full-canvas `replace` (no `section_id`) with the complete intended content.** Read the canvas first, rebuild the full markdown with the edits, replace once, read back to verify. Deterministic.
3. **Do NOT include a leading `# H1`** in full-replace content — the canvas has an intrinsic title that always survives; an H1 in the content duplicates it.
4. **Mentions: read ≠ write syntax.** `slack_read_canvas` serializes real mentions as `<@W...>`; writing `<@W...>` back produces broken literal text. To create real mentions, write **`![](@W...)`**. Verification: after writing, read back — real mentions re-serialize as `<@ID>`.
5. Before any canvas edit, capture the full current markdown (it is the restore point).
