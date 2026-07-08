---
name: reference_aia_vs_coworker_axes
description: Terminology lock — two separate axes in the AOv2 migration. AIA = the front-end (AI Assistant UI); Coworker/AOv2 = the backend. Don't collapse a backend migration into a UI swap.
metadata:
  node_type: memory
  type: reference
---

**🔒 WORD LOCK (Pedro, 2026-06-26 — "souvent tu en oublies toujours", recurring error):**
- **"Coworker UI" / "Coworker Rail" = UI (front).** The rail / app surface the user sees.
- **"Coworker" (alone) / "Coworker harness" = backend (the AOv2 runtime).** The skills/agentic harness behind the surface.
- So "Coworker" by itself = **backend**, never the UI. Only say UI when you write "Coworker UI" or "Coworker Rail". Re-check this token every time before writing.

**Two separate axes in the EPA / AEM "Migration to AOv2." Do not conflate them** (Pedro corrected Claude **twice on 2026-06-25** — once on the Felix plan, again on Corey's provisioning thread; **again 2026-06-26** on the UI/backend word-lock above; the conflation keeps recurring, so re-check the axis every time before drafting).

- **Backend axis:** AOv1 → AOv2. This is the actual "migration to AOv2" — the agent/skills harness behind the surface.
- **Front axis:** the **AI Assistant UI (AIA)** vs the **Coworker UI / Coworker Rail**. AIA = AEM's current front-end (the rail in experience.adobe.com), today powered by AOv1. The **Coworker harness** = the backend (productized AOv2 runtime); the **Coworker UI / Rail** = the front it ships with. Keep the harness (backend) and the UI/Rail (front) as distinct words.

**A backend migration to AOv2 ≠ a UI swap to Coworker.** They can move independently:
- **Direct cutover (EPA Plan A):** AOv2 backend **+** Coworker UI. AIA front retired.
- **Bridge (EPA Plan B):** AOv2 backend (skills) consumed **behind AIA** via A2A. Front stays the AI Assistant the customers already use.

**Why it matters for Pedro's read:** Corey's load-bearing line *"all usage week over week is in the current AI assistant, no customers in Coworker yet"* is a **front statement** — customers live on the AIA front. So Plan B (keeps AIA front, swaps backend) delivers value now; Plan A (moves to the Coworker front) moves them to a front with no users yet. That is exactly why the bridge is NOT throwaway. Calling Plan A "replace the AI Assistant UI with the Coworker UI" without isolating the backend migration = the conflation to avoid.

**Provisioning TBYB onto Coworker is NOT an AEP-held date** (Pedro, 2026-06-25, correcting Claude on Corey's thread). Corey asked "when will AEP auto-provision TBYB customers to Coworker." Pedro's answer: *"dès que tu veux des clients dessus"* — provisioning is **on-demand**, available whenever AEM wants customers on the Coworker backend, not a fixed external milestone we wait on. → the real gate is **feature parity on AEM's side**, then provision. Don't frame provisioning as an AEP dependency with an unknown date. ⚠️ The GA Readiness canvas line "TBYB customers are NOT auto-provisioned on Coworker; manual FI whitelisting" is **unsourced** (predates this session, origin unclear) — flagged as `[unverified]`; do not assert the "manual FI whitelisting" mechanism until confirmed.

**Bertrand's cutover model (2026-06-25, thread) — the manifest-vs-rail fork now leans RAIL-REPLACEMENT.** Bertrand: end-July the **Unified Shell stops loading AIA 1.0 and shows Coworker Chat instead** (rail mode) = *"kind of AIA 2.0 — a custom UI using Coworker as a harness in headless mode — same as Coworker Enterprise (standalone full-screen) is doing."* The agents-as-they-are-today retire **with** AIA 1.0. His open question: *"can we expose our AEM agents as skills in this new model."* → This is the **rail-replacement** reading (the AIA 1.0 rail is removed from the Shell and replaced by a Coworker-headless rail), NOT a manifest-repoint of the old AIA UI. Now corroborated by **Josh (06-22) + Bertrand (06-25)** → the manifest-repoint reading looks unlikely. ⚠️ Still Bertrand's "my understanding," not a platform decree (Anjul/Manas own it) — don't bank as decided. The bridge (Plan B) stays consistent: it produces the skills the new model needs while customers are still on the AIA-1.0 front during the gap.

Ties [[reference_coworker]] (Coworker = productized AOv2), [[reference_coworker_faq]], [[feedback_dont_conflate_pattern_with_object]] (selection is manifest-scoped — sourced detail in vault `AEM — Coworker Skills Mechanism`, 06-26 section). AOv1/AIA both going away ~end-July (Bertrand 06-24).

**🆕 2026-07-08 — DOC READ corrects the "cliff" (Satya Deep Maheshwari's "AI Assistant UI vs Coworker UI — front-ends & backends" deep-dive, wiki 3941700446; a repo source-read, "preliminary, inferences flagged").** The two fronts and their backends per the doc:
- **AI Assistant UI** → backend = **Gandalf** orchestration layer (`aep-gandalf-api`) → which delegates agentic work to **AOv2**. The doc states *"AI Assistant is already on AO V2."*
- **Coworker UI** → **AOv2 directly** (via `ao-client`, WebSocket A2A), no Gandalf.
- So **both UIs reach AOv2** — the real distinction is Gandalf-mediated (AIA, the incumbent path the whole base uses today) vs direct-`ao-client` (Coworker, needs the org provisioned for direct Coworker access). "Coworker UI → AOv1" is a non-question; AOv1 isn't in either UI's path per this doc.
- ⚠️ **This partially CONTRADICTS Pedro's own 06-26 `ao`-repo read** (AIA → AOv1 orchestrator → A2A bridge → Coworker). Either AIA finished AOv1→AOv2 since, or "AOv1 orchestrator" = Gandalf re-pointed to AOv2. Wiring unconfirmed; the customer-facing conclusion holds either way.
- **The Day-After-Map "non-provisioned org = no assistant on Aug 1" was OVER-ASSERTED** (an inference stated as fact; Pedro caught it 07-08). Corrected: an un-migrated org likely **keeps the AIA rail** (already on AOv2 via Gandalf) — it doesn't get a broken Coworker rail. The swap is **flag-gated** (`shell-coworker-enabled` per the ExC Unified Shell Feature Flags doc 3956336717), so it's per-org/cohort, not a hard global cliff. Manas (06-18): "AOv1 stays as long as someone is on it, no central switch." → **the single unresolved hinge (= the Josh question): does the shell remove the AIA rail GLOBALLY end of July, or only for provisioned/flagged orgs while the rest keep AIA?** If the latter, no cliff.
- **The Coworker rail runs on AOv2** (test flags `ao2-aia-enabled` + `shell-coworker-enabled`, #cxue-coworker-rail-hybrid-collaborators). **WebMCP = the mechanism for the rail to ACT on a surface** (a page registers tools the agent reads/drives; Mikaela's `shell_navigate` merged) — this is the answer to Eugene's "can the rail act on the EH dashboard vs only redirect": yes, IF EH registers WebMCP tools.

**🔒 AOv1 had NO skills (Pedro corrected Claude twice, 2026-06-26).** AOv1 = an orchestrator agent routing to *other agents*, guessing blindly. The v1 "50/50" failure = blind **agent-routing** with nothing to distinguish — NOT skill-overlap (skills didn't exist in v1). Don't say "v1 skills overlapped." The v2 difference: (1) the **manifest** is resolved deterministically by scope/identity (in front of the LLM), so the "which context" choice is no longer a guess; (2) inside the manifest you pick a **skill** (not a black-box agent), made distinguishable by its **description** (`domain` + `when-to-use`) and measured by the overlap audit. So "won't we have the v1 problem routing to the right manifest?" → no: manifest routing = deterministic config, not a prompt-intent guess; the only residual guess is skill-within-manifest, which the descriptions + audit address. (A manifest is a scoped *set of skills* for a user/surface, NOT a runtime routing target — clarify if a stakeholder conflates the two.)
