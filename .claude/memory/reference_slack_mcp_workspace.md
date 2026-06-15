---
name: reference_slack_mcp_workspace
description: "claude.ai Slack connector must be OAuth'd to cq-dev (Adobe) — found pointing at Pedro's personal workspace 2026-06-10, breaking all Adobe Slack reads."
metadata: 
  node_type: memory
  type: reference
  originSessionId: beda40f7-b409-4f4c-89f0-77971617cb07
---

The claude.ai Slack connector (MCP `claude_ai_Slack`) was discovered on 2026-06-10 to be authorized against Pedro's **personal** Slack workspace (only `#general` from 2016 + `#claude_general` visible), not the Adobe enterprise workspace (**adobedx** / cq-dev).

**🔴 Root cause clarified 2026-06-15: Pedro is on his PRIVATE Claude account** (out of enterprise credits) — so the Slack connector is tied to his personal workspace and the **adobedx enterprise workspace is not reachable from the private account at all.** This is not (only) a wrong-OAuth-target you can re-pick; on the private account the enterprise Slack simply isn't connected.

**Symptom:** `channel_not_found` on every Adobe channel — including known-good ones like `#aem-agents` (C09KKLW1N86). Local `/mcp` reconnect and VPN do NOT fix it.

**Options (2026-06-15):** (1) attach adobedx to this private account's Slack connector IF Adobe's Slack admin allows third-party app installs (often blocked); (2) go back to the **enterprise Claude** account when credits return; (3) **Pedro pastes the Slack content into chat** — Claude ingests it directly (used 2026-06-15 for the p42-architecture Rubin/Coworker thread). Option 3 is the reliable fallback while on private Claude.

**Old fix (only valid on the enterprise account):** claude.ai → Settings → Connectors → Slack → reconnect, picking the adobedx/cq-dev workspace on the Slack OAuth screen. Does NOT apply while on the private account.

**Check before relying on Slack reads:** if an Adobe channel read fails, search channels for "aem" — zero results = wrong workspace, don't keep retrying IDs.

Related: [[feedback_never_send_slack]] (read-only use anyway).
