---
name: reference_aia_vs_coworker_axes
description: Terminology lock — two separate axes in the AOv2 migration. AIA = the front-end (AI Assistant UI); Coworker/AOv2 = the backend. Don't collapse a backend migration into a UI swap.
metadata:
  node_type: memory
  type: reference
---

**Two separate axes in the EPA / AEM "Migration to AOv2." Do not conflate them** (Pedro corrected Claude **twice on 2026-06-25** — once on the Felix plan, again on Corey's provisioning thread; the conflation keeps recurring, so re-check the axis every time before drafting).

- **Backend axis:** AOv1 → AOv2. This is the actual "migration to AOv2" — the agent/skills harness behind the surface.
- **Front axis:** the **AI Assistant UI (AIA)** vs the **Coworker UI**. AIA = AEM's current front-end (the rail in experience.adobe.com), today powered by AOv1. Coworker = productized AOv2 (its own UI/app + AOv2 backend).

**A backend migration to AOv2 ≠ a UI swap to Coworker.** They can move independently:
- **Direct cutover (EPA Plan A):** AOv2 backend **+** Coworker UI. AIA front retired.
- **Bridge (EPA Plan B):** AOv2 backend (skills) consumed **behind AIA** via A2A. Front stays the AI Assistant the customers already use.

**Why it matters for Pedro's read:** Corey's load-bearing line *"all usage week over week is in the current AI assistant, no customers in Coworker yet"* is a **front statement** — customers live on the AIA front. So Plan B (keeps AIA front, swaps backend) delivers value now; Plan A (moves to the Coworker front) moves them to a front with no users yet. That is exactly why the bridge is NOT throwaway. Calling Plan A "replace the AI Assistant UI with the Coworker UI" without isolating the backend migration = the conflation to avoid.

**Provisioning TBYB onto Coworker is NOT an AEP-held date** (Pedro, 2026-06-25, correcting Claude on Corey's thread). Corey asked "when will AEP auto-provision TBYB customers to Coworker." Pedro's answer: *"dès que tu veux des clients dessus"* — provisioning is **on-demand**, available whenever AEM wants customers on the Coworker backend, not a fixed external milestone we wait on. → the real gate is **feature parity on AEM's side**, then provision. Don't frame provisioning as an AEP dependency with an unknown date. ⚠️ The GA Readiness canvas line "TBYB customers are NOT auto-provisioned on Coworker; manual FI whitelisting" is **unsourced** (predates this session, origin unclear) — flagged as `[unverified]`; do not assert the "manual FI whitelisting" mechanism until confirmed.

Ties [[reference_coworker]] (Coworker = productized AOv2), [[reference_coworker_faq]], [[feedback_dont_conflate_pattern_with_object]]. AOv1/AIA both going away ~end-July (Bertrand 06-24).
