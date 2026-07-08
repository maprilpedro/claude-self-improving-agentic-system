---
name: feedback_slack_permalink_with_drafts
description: With every Slack reply draft, give the permalink to the thread's last message so Pedro can locate where to paste.
metadata:
  type: feedback
---

Pedro 2026-07-08: when I draft a reply to a Slack thread, always end with the **permalink to the latest message in that thread**, so he can jump straight to where he pastes.

**Why:** he runs many threads in parallel; without the link he wastes time hunting for the right thread across 16 audit channels + DMs.

**How to apply:** after any Slack reply draft (and when reporting on a thread I read), append the permalink. Format:
`https://adobedx.slack.com/archives/<CHANNEL_ID>/p<TS_no_dot>?thread_ts=<PARENT_TS>&cid=<CHANNEL_ID>`
- `<TS_no_dot>` = the last message's ts with the dot removed (e.g. `1783440244.478709` → `p1783440244478709`).
- `thread_ts` = the parent message ts (keeps the dot). Drop `?thread_ts=...&cid=...` for a non-threaded channel message.
- Workspace host: use the one Pedro shares from (seen so far: `adobedx.slack.com`, `adobe.enterprise.slack.com`). Match the channel's workspace when known.

Fold into [[reply]] and [[capture-slack]] outputs. Reading Slack = interactive session only ([[reference_slack_mcp_workspace]]). Never send ([[feedback_never_send_slack]]).
