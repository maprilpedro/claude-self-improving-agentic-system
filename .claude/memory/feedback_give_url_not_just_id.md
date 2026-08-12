---
name: feedback-give-url-not-just-id
description: Always give the clickable URL alongside any ID (Confluence page, Slack canvas/thread, JIRA, GitHub PR) — Pedro needs to open the source, not reconstruct the link.
metadata:
  type: feedback
---

When referencing any object by ID — Confluence `pageId`, Slack canvas (`F0B…`) or thread ts, JIRA key, GitHub PR — **give the full URL too**. The ID alone is fine to keep for precision, but it must be accompanied by something Pedro can click.

Stated by Pedro 2026-08-12: *"en règle générale, c'est ok de me donner l'id mais donne moi aussi l'URL que je puisse ouvrir les docs et liens que tu me référence."*

**Why:** he verifies sources himself before reusing them outward. An ID he has to reconstruct into a URL is friction at exactly the moment the point of the reference is to go and read it. Pairs with [[feedback_slack_permalink_with_drafts]] (same rule, Slack side, already established) and [[feedback_confirm_ask_before_producing]] (don't characterize an unread source — he can only check if he can open it).

**How to apply:**
- Confluence: `https://wiki.corp.adobe.com/pages/viewpage.action?pageId=<id>`
- Slack message/thread: the permalink from the MCP result, never just the ts
- Slack canvas: `https://adobe.enterprise.slack.com/docs/T02CAQ0B2/<canvas_id>`
- JIRA: `https://jira.corp.adobe.com/browse/<KEY>`
- GitHub: full `https://github.com/<org>/<repo>/…` path

Format: keep the ID inline for precision and hang the URL off it, e.g. canvas `F0BMUV76DHU` → link.
