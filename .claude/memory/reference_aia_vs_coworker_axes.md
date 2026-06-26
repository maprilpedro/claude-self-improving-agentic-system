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
