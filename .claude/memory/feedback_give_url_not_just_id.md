---
name: feedback-give-url-not-just-id
description: Always give the clickable URL alongside any ID (Confluence page, Slack canvas/thread, JIRA, GitHub PR) — Pedro needs to open the source, not reconstruct the link.
metadata:
  type: feedback
---

When referencing any object by ID — Confluence `pageId`, Slack canvas (`F0B…`) or thread ts, JIRA key, GitHub PR — **give the full URL too**. The ID alone is fine to keep for precision, but it must be accompanied by something Pedro can click.

Stated by Pedro 2026-08-12: *"en règle générale, c'est ok de me donner l'id mais donne moi aussi l'URL que je puisse ouvrir les docs et liens que tu me référence."*

**Why:** he verifies sources himself before reusing them outward. An ID he has to reconstruct into a URL is friction at exactly the moment the point of the reference is to go and read it. Pairs with [[feedback_slack_permalink_with_drafts]] (same rule, Slack side, already established) and [[feedback_confirm_ask_before_producing]] (don't characterize an unread source — he can only check if he can open it).

🔴 **SECOND FAILURE 2026-08-15, and it was the one form the recipe below did not cover.** A whole Slack read-back was reported using bare **channel and group-DM IDs** (`C0BQ4L7BVL2`, `DQ6H0AV7H`) and a bare **file ID** (`F0BPBFCST5F`). Pedro: *"je t'ai demandé de chaque fois me donner l'url pour slack - je ne peux rien faire juste avec l'id."* **The rule is every Slack object, not only canvases and threads.** A report he cannot open is a report he has to take on trust, which is the opposite of why he asks for sources.

**How to apply:**
- Slack **channel or DM**: `https://adobe.enterprise.slack.com/archives/<CHANNEL_ID>` — works for `C…` channels, `C…`/`G…` group DMs and `D…` DMs alike
- Slack **message/thread**: `https://adobe.enterprise.slack.com/archives/<CHANNEL_ID>/p<ts with the dot removed>` — ts `1786660097.959949` → `p1786660097959949`. Build it yourself; do not wait for a permalink field
- Slack **file or doc**: `https://adobe.enterprise.slack.com/docs/T02CAQ0B2/<file_id>` (Slack docs/canvases) or `https://adobe.enterprise.slack.com/files/<uploader_user_id>/<file_id>` (uploads)
- Slack **canvas**: `https://adobe.enterprise.slack.com/docs/T02CAQ0B2/<canvas_id>`
- Confluence: `https://wiki.corp.adobe.com/pages/viewpage.action?pageId=<id>`
- JIRA: `https://jira.corp.adobe.com/browse/<KEY>`
- GitHub: full `https://github.com/<org>/<repo>/…` path

Format: keep the ID inline for precision and hang the URL off it, e.g. canvas `F0BMUV76DHU` → link. **Check before sending: if a chat reply contains a bare `C…` / `D…` / `F…` / `T…` token with no link on it, it is not finished.**
