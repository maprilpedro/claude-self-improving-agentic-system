# A Multi-Team Agent Test Measures Whatever Is Least Controlled — Usually Access, Not the Agent

_Section: AI Product Risks — part of `ai-product/`; router = README.md._

- **Date identified**: 2026-08-15
- **Source**: Pedro's own reproduction run on the AEM Showcase org the weekend before the Coworker GA bug bash, plus two earlier instances in the same migration.

- **Insight**: An agent only answers after a long chain has held — identity, org membership, product entitlement, environment provisioning, manifest, skill load, API config, token. **A multi-team test exercises the whole chain but attributes every failure to the last link, which is the agent.** So the test does not measure agent quality. It measures whichever link is least controlled across the participants, and in an enterprise product that link is almost always **access**, because access is the only part of the chain that is per-person and per-environment rather than per-build.

- **Why access specifically**: everything else in the chain is uniform for everyone in the room — the same manifest, the same skills, the same API. Entitlement is the one layer that varies per participant, is invisible until exercised, and produces errors that look like product failures (`Failed to authenticate`, `no results`, `not provisioned`) rather than like setup failures.

- **Observations**:
  1. **2026-08-15, five walls in five attempts, none of them the agent.** Testing the bug-bash target three days out produced `Failed to authenticate with Adobe ID` on an AEM author *while being org admin*, `401 invalid OAuth token` cross-org, `no environments provisioned`, `403 "Profile is not valid" (403025)` on Cloud Manager, and `User is not provisioned` on Assets. **Admin rights are not access — an AEM environment is reachable only through one of its product profiles.** Meanwhile the agent chain itself worked on the first try where entitlement was in place: one skill made a live API call and returned 13 real records.
  2. **2026-07-20, the Tokyo test.** Wouter's cross-app run confirmed AEP, CJA and AJO. **The AEM half was blocked by environment startup failures, not by the capability under test**, so the actual question — do AEM skills work through Coworker end to end — came back unanswered rather than answered negatively.
  3. **2026-08-14, the merge itself.** The engineer's local environment broke, so **nothing was validated before merging**; verification happened afterwards on stage, and fifteen of sixteen ported plugins stayed unexercised because nobody could say how to reach them.

- **Application**: Before any multi-team agent test, **run the chain yourself, as one participant, on the exact target** — not to check the agent, but to find which link is uncontrolled. Then pre-clear that link for everyone (attach the group to the product profile, name the environment, confirm the role) *before* the session. Publish what the test covers and what it could not reach. If a confidence declaration is due afterwards, say which link each failure sat on.

- **Anti-pattern**: Scheduling the test, inviting the teams, and discovering the access layer on the morning of. The failures arrive as agent defects, the room believes them, and the go/no-go decision inherits the error. **A test that cannot separate "the agent was wrong" from "the tester could not get in" produces a number nobody should sign.**

- **Related**: ["No Results Found" Is a Product Gap in Agentic UX](no-results-found-is-a-product-gap-in-agentic-ux-not-a-legitimate-answe.md) (the failure taxonomy this depends on — a diagnostic empty answer is what let the entitlement cause be identified in minutes); [Success Definitions Must Be Agreed Before Metrics Are Scaled](success-definitions-must-be-agreed-before-metrics-are-scaled.md); [Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number](../leadership/lead-the-slide-with-the-honest-read-of-your-own-metric-not-the-flatt.md).
