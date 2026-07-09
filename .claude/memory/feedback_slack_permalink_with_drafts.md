---
name: feedback_slack_permalink_with_drafts
description: With every Slack reply draft, give the permalink to the thread's last message so Pedro can locate where to paste.
metadata:
  type: feedback
---

Pedro 2026-07-08: when I draft a reply to a Slack thread, always end with the **permalink to the latest message in that thread**, so he can jump straight to where he pastes.

**🔴 RESTATED HARDER 2026-07-09 — "j'ai besoin TOUJOURS du lien."** A draft without its permalink is **not usable**, so it is not a draft. This applies to *every* Slack draft in *every* turn: first drafts, re-drafts, single-span rewrites, follow-up messages, and drafts produced in a turn that is mostly about something else. A thread ID or a channel name is not a substitute. The failure mode is mine drifting mid-session: I give the link on draft 1, then drop it on drafts 2 and 3 because "he already has it" — he does not, the thread has moved and so has the last-message ts.

**Also:** the workspace host matters. `#aem-agent-owners-alignement` (C0BARAMM89Z) resolves on **cq-dev**; `#p42-architecture` (C09KKLW1N86) on **adobedx**. If unsure which host, give both forms rather than one wrong one.

**Why:** he runs many threads in parallel; without the link he wastes time hunting for the right thread across 16 audit channels + DMs.

**How to apply:** after any Slack reply draft (and when reporting on a thread I read), append the permalink. Format:
`https://adobedx.slack.com/archives/<CHANNEL_ID>/p<TS_no_dot>?thread_ts=<PARENT_TS>&cid=<CHANNEL_ID>`
- `<TS_no_dot>` = the last message's ts with the dot removed (e.g. `1783440244.478709` → `p1783440244478709`).
- `thread_ts` = the parent message ts (keeps the dot). Drop `?thread_ts=...&cid=...` for a non-threaded channel message.
- Workspace host: use the one Pedro shares from (seen so far: `adobedx.slack.com`, `adobe.enterprise.slack.com`). Match the channel's workspace when known.

Fold into [[reply]] and [[capture-slack]] outputs. Reading Slack = interactive session only ([[reference_slack_mcp_workspace]]). Never send ([[feedback_never_send_slack]]).
