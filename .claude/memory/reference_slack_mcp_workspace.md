---
name: reference_slack_mcp_workspace
description: claude.ai Slack connector must be OAuth'd to cq-dev (Adobe) — found pointing at Pedro's personal workspace 2026-06-10, breaking all Adobe Slack reads.
metadata:
  type: reference
---

The claude.ai Slack connector (MCP `claude_ai_Slack`) was discovered on 2026-06-10 to be authorized against Pedro's **personal** Slack workspace (only `#general` from 2016 + `#claude_general` visible), not **cq-dev** (Adobe).

**Symptom:** `channel_not_found` on every Adobe channel — including known-good ones like `#aem-agents` (C09KKLW1N86). Local `/mcp` reconnect and VPN do NOT fix it; the OAuth grant itself is to the wrong workspace.

**Fix:** claude.ai → Settings → Connectors → Slack → reconnect, picking the **cq-dev** workspace on the Slack OAuth screen (top-right workspace selector). Then `/mcp` reconnect in the session.

**Check before relying on Slack reads:** if an Adobe channel read fails, search channels for "aem" — zero results = wrong workspace, don't keep retrying IDs.

Related: [[feedback_never_send_slack]] (read-only use anyway).
