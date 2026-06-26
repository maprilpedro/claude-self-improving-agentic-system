---
name: reference_coworker_rail_access
description: How to see the Coworker rail (the "AIA 2.0" front) on stage + the two-assistants-on-EH-home observation. Stage feature flags + prod build link. The transition-window UX that sits on Pedro's EH selection/consistency lane.
metadata:
  type: reference
---

# Coworker rail — how to see it + the two-assistants observation (2026-06-26)

Source: Eugene Bannykh relayed Rodson Clavel's instructions in cq-dev Slack (channel `C07MVKU1APJ`, msg `1782407495.189399`, screenshot file `F0BE1L86M96` — kept in Slack, NOT copied to this repo per [[feedback_no_internal_to_personal_repos]]).

## Access (how to see the Coworker rail)
- **Stage:** enable two feature flags → `ao2-aia-enabled` + `shell-coworker-enabled`.
- **Prod:** not GA yet — use the prod build link `experience.adobe.com/?unified-shell_version=PR-12141-…`.
- The rail's backend = **AO stage endpoint** `agent-orchestrator-stage-va7.adobe.io` (shown in the panel footer) = the **Coworker harness**. Flag names confirm Bertrand's cutover model: `ao2-aia-enabled` = AOv2 behind an AIA-style rail ("AIA 2.0"), `shell-coworker-enabled` = Unified Shell loads Coworker.

## The observation (Pedro's lane)
The staging screenshot (EH home, "Welcome Eugene", Overrides on) shows **TWO chat entry points at once**:
1. Center bar = the existing **AI Assistant** (*"Ask AI Assistant anything"* + prompt library + Experience Manager) = today's AIA.
2. Right rail = the new **Coworker** rail (*"Ask Coworker anything"*, AO stage endpoint in footer).

Two reads, both true:
- **The Coworker rail looks like AIA by design** — same assistant-panel visual language, Coworker harness underneath = the "AIA 2.0 = same look, new engine" continuity. (Word-lock: Coworker UI/rail = front that imitates AIA; harness = backend. [[reference_aia_vs_coworker_axes]].)
- **Two assistants coexist on the EH home** = a staging artifact (Overrides on + both flags). End-state per Bertrand = the Unified Shell **stops loading AIA 1.0** and the rail replaces the center bar. So "two at once" is the transition window, not the target.

**Why it's Pedro's:** this is the EH front door with two chat entry points — the "which one does the user land in / how is it one coherent surface" question made literal on screen. = the EH **selection + consistency layer** lane ([[project_experience_hub]]), and the migration-window UX confusion (mixed surfaces) flagged before. The lever: own how EH routes/consolidates the entry during the transition, not let two bars sit side by side.
