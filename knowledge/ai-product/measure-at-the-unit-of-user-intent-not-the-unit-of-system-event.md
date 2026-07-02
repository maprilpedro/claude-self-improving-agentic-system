# Measure at the Unit of User Intent, Not the Unit of System Event

_Section: Measuring AI Features — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-22
- **Source**: Varun Kalra (Discovery Agent technical validator, Apoorva's team) in sync with Pedro, April 22, 2026. Discussing how Apoorva's three value-realization metrics (Query Unsuccessful Rate, First Useful Result Rate, Remaining Prompts Rate) should be computed.
- **Insight**: Value-realization metrics for an agent have to sum to something meaningful (typically 100%) to be interpretable as a distribution. They only sum cleanly when the denominator matches the unit of user goal — the intent — not the unit of system event — the interaction. Pedro's initial implementation measured at chat or interaction level. Varun's correction: one intent can span multiple interactions. If the user fires four queries refining the same intent and two return results, splitting the four into different buckets at the interaction level produces three categories that will never add to 100%. Measure at the intent level: the intent is the carrier of "did the user get what they wanted."
- **Concrete rule**:
  - **Intent 1, returned nothing** → Query Unsuccessful bucket.
  - **Intent 2, returned results, no follow-up query for the same intent within 2 minutes** → First Useful Result bucket.
  - **Intent 3, required follow-up refinements before success** → Remaining Prompts bucket.
- **Why this matters beyond metrics**: Intent-level measurement forces the product team to define "what is an intent" — which in turn forces clarity on what the agent is supposed to resolve vs. what's a refinement vs. what's a new task. This is a product-definition exercise disguised as a measurement exercise.
- **Application**: For any agent-UX metric that involves success / failure classification across a conversation, audit the unit. If it's at the interaction or chat level, you probably need intent-level aggregation. The 2-minute window is a reasonable default for intent continuity; the exact threshold needs validation with the product owner.
- **Anti-pattern**: Reporting three mutually-exclusive categories that don't sum to 100%. The gap IS the signal that your unit of measurement is wrong.
- **Related**: Technical Success Rate vs Value Realization Rate (different metrics, same intent-unit principle); VRR Is a Tiered Metric.
