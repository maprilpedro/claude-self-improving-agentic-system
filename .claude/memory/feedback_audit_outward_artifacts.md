---
name: feedback-audit-outward-artifacts
description: "For outward/shared artifacts (wiki pages, capture docs), attribute every claim to its source and run a sourced/inference/invention audit before sharing."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 17c67daf-e9c0-4126-adee-75e89cfcff7d
---

**When building an artifact others will read (a Confluence capture page, a session record, a proposal), every claim must trace to its source, and run a full audit — classify each line sourced / his-prior-framing / inference / invention — BEFORE it is shared.** Standing expectation, enforced twice on 2026-06-23: Pedro's *"sois sur a 100% — pas d'invention, pas d'inference"* on both "Pre-load, Don't Limit" and the Josh rendering capture page.

**Why:** Pedro's wiki pages become the canonical record others rely on (Ian validated the 06-18 one as "a complete record"). A single invented or inferred line poisons that trust. The audit is the price of the stakeholder-gravity that makes the page valuable.

**How to apply:**
- **Session/meeting capture pages:** attribute every answer to **speaker + timestamp** from the transcript. Quote, don't paraphrase, where it matters; mark elisions in quotes honestly.
- **Run the audit before sharing:** go line by line, tag ✅ sourced / 📐 his prior framing / ⚠️ inference-or-my-framing / 🔴 error. Fix the 🔴, mark the ⚠️ as proposal, restore verbatim quotes. Report the verdict + residuals.
- **Keep synthesis separate from sourced.** A "what this means for us / my read" section is fine but must be labelled as synthesis, distinct from the sourced record — never blended in.
- **Cross-references count as sourced only if dated/attributed** (e.g. "AEP-dependency driver (06-18)"), and pulling a fact from prior memory into a transcript-page is an inference *relative to that transcript* — flag it.
- **Don't over-read endorsements.** "Consistent with my thesis" ≠ "validated"; log reserved judgment as reserved judgment ([[feedback_dont_overread_vp_quotes]]). Pedro caught Claude framing Ian's "I'm still checking" as "strong validation" on 06-23.
- Watch the residuals Pedro alone can resolve (garbled names, etc.) and surface them rather than guessing.
- **🔴 A COUNT READ OFF A SOURCE IN ONE PASS IS A CLAIM, NOT A FACT — COUNT IT (2026-08-27).** Reading a 93-row inventory CSV, four totals were stated from a single pass and all four were wrong: 92 rows for 93, 84 skills for 85, "~59 user-reachable" for 60, and seven `Skill (API Ref)` for eight. **The type breakdown quoted in the same sentence already summed to 85, so the error was visible on the page and went unchecked.** All four reached `watches.md` and one was on its way to Bertrand. A second pass over the same file also revealed a whole missing family (AEM Dispatcher, 8 skills) that the first comparison never named. **How to apply: before any total enters the registry or an outward artifact, produce it by an actual count, and check it against any breakdown stated beside it. `wc -l` undercounts a file with no trailing newline — that alone caused two of the four.**
