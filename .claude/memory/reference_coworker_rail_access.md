---
name: reference_coworker_rail_access
description: How to see the Coworker rail (the "AIA 2.0" front) on stage + the two-assistants-on-EH-home observation. Stage feature flags + prod build link. The transition-window UX that sits on Pedro's EH selection/consistency lane.
metadata:
  type: reference
---

# Coworker rail — how to see it + the two-assistants observation (2026-06-26)

Source: Eugene Bannykh relayed Rodson Clavel's instructions in cq-dev Slack (channel `C07MVKU1APJ`, msg `1782407495.189399`, screenshot file `F0BE1L86M96` — kept in Slack, NOT copied to this repo per [[feedback_no_internal_to_personal_repos]]).

## 🔑 POST-GA ACCESS (2026-08-24) — THE URL FLAG, and it goes after `/ui`, not in the hash

**`?shell_aiChatEnabled=true`** → `adobeaemcloud.com/ui?shell_aiChatEnabled=true`

Source: `#aem-agentic-owners-alignement` 2026-08-24 18:13, [thread](https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1787587984719469). **Apoorva Gupta** asked Corey + Pedro why rail mode had stopped working in AEM Showcase. **Corey Dulimba gave the pointer** (*"there is a flag you need to set in the URL now"* + a link into `#cxue-coworker-panel-hybrid-collaborators`); **Mark Doten gave the parameter**, then corrected her when she put it in the hash and still saw the popover: *"because you added it to the hash… you have to add it after `/ui`"*. She relayed it to Thirumalaivasan M + Ankur Arora 19 min later in `#aem-agent-discovery`.

⚠️ **Mark Doten's framing in the same thread, which is the caveat to carry:** *"if an org has Coworker, the rail is not accessible because the Coworker rail is not available yet… there are select applications that have the button enabled, but those show a popover that links to the Coworker application… as applications are ready for Coworker rail, they can be enabled to show it."* **So the flag opens the rail per application; it does not make the rail generally available.**

## Access (how to see the Coworker rail) — pre-GA stage recipe, kept for history
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

## 2026-07-10 — second, independent confirmation (Sorin Slavic, in Pedro's own thread `1783584402.501589`)

Sorin posted the recipe publicly, answering Corey's "is this available now for testing?": **`ctrl+i` → access overrides → enable → search `ao2-aia-enabled` → turn on.** On **prod it errors** (he showed it: "you will get 🙂 because it's prod; sorry"). On **stage it works**: `experience-stage.adobe.com/#/@aem-sites-engineering/cloud-manager/landing.html`. Screenshots `F0BGFHH2VFU` (Cloud Manager), `F0BGFHJC2AW` (AEM home), `F0BGDHG1QUW`.

**🔑 This is the direct answer to the "BECOMES vs LINKS TO" question (07-09 slide `F0BG4APMYHK`). THE RAIL BECOMES THE COWORKER PANEL, IN PLACE.** Both screenshots show the host page intact with a right-hand panel reading *"What are we making, Sorin?"* / *"Ask Coworker anything"* / Plan mode / "Suggested for you". **It is not a redirect.** → Pedro's public 07-09 12:22 statement to Apoorva ("the rail becomes the Coworker chat panel, same place, same behaviour") is **confirmed by his own engineer's screenshot**, and the AEP slide's "LINK TO COWORKER" label reads as the *interim* state (cohort 1 has no panel yet), not the end state.

**⚠️ Two honest limits.** (1) This is **stage with "Overrides on"** — it says nothing about prod behaviour at cutover. (2) It proves the panel **renders in place**. It does **not** prove the panel can **act on** the page. **Eugene's question (07-07) is unchanged and is now the only one left:** can the Coworker panel read and manipulate the EH dashboard, or is it a chat that merely sits next to it? **Cheapest possible test: ask Sorin to try one action from the rail on stage.** He is thirty seconds from the answer.

**Also visible in the 07-10 screenshots, and unremarked in-thread:**
- **The two entry points, again, live.** AEM home center bar = *"Ask AI Assistant anything"* (+ Prompt library). Right rail = *"Ask Coworker anything"*. Same page, two assistants, two engines. The 06-26 observation reproduced a fortnight later by a different person.
- **Suggested prompts survive in the Coworker rail** ("Suggested for you"), but they are **Coworker's**, not AEM's. = the Zeus / AO2-recommendation-system gap made visible. **This is the missing datum for the Fu Chi pause decision (07-03): do not pause, feed AEM content into the AO2 recommendation system.**
- **The rail is already context-aware per surface** — on Cloud Manager it suggests "Analyze my failed pipeline", "How do I grant a user access to environment?"; on the AEM home the suggestions differ. Coworker adapts its suggestions to the host page. Adapting ≠ acting; see the limit above.
- **Sorin's post contradicts Shankari's *"None of this is available yet"*** (07-09 15:22, 2 facepalm reactions). It is available on stage behind one flag. Pedro surfaced it with an ⬆️ to Gilles Knobloch + Shankari at 09:52, no commentary. Correct handling ([[feedback_additive_not_corrective]]).

**Why it's Pedro's:** this is the EH front door with two chat entry points — the "which one does the user land in / how is it one coherent surface" question made literal on screen. = the EH **selection + consistency layer** lane ([[project_experience_hub]]), and the migration-window UX confusion (mixed surfaces) flagged before. The lever: own how EH routes/consolidates the entry during the transition, not let two bars sit side by side.

---

## ✅ 2026-09-08 update — the flag is now TWO params (Rodson Clavel, pinned in `C0BCKG35NFP`)

`?shell_aiChatEnabled=true&shell_nextGenAIEnabled=true#` after `/ui`. Prerequisite: the org is already Coworker-enabled (ask in `#coworker-general-questions` `C070SDG809J`). ⚠️ QA/debug overrides silently force the legacy AIA panel; turn them off, or set `shell-coworker-enabled`, `ai-ui-kill-switch`, `ao2-aia-enabled` all to `true`. The older `devMode=true&shell_aiPanelEnv=dev…` method is retired ("Episode not found"). Coworker panel GA is still only Workfront + Target. Source: https://adobe.enterprise.slack.com/archives/C0BCKG35NFP/p1788905115110679 (Lénárd Palkó pointed Pedro at it 09-09).
