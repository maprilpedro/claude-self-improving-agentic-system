# Capability-Level Monthly Usage Is the Value Narrative Metric (BVR)

_Section: Measuring AI Features — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-23
- **Source**: Pedro + Philippe Kapfer Governance Agent report review, April 22–23, 2026. Context: identifying what metrics to expose for Governance Agent value realization ahead of Loni + Jean-Michel meeting (week of May 4). Wiki reference: [AEM Agentic Success Definition Compliance Framework](https://wiki.corp.adobe.com/spaces/WEM/pages/3774169978/AEM+Agentic+Success+Definition+Compliance+Framework).
- **Insight**: TSR, VR (intent-level), and VRR (tier-based) all answer the same question at different resolutions: *was this interaction valuable?* They operate at the interaction or intent level. Leadership doesn't consume interaction-level data — they consume **rate of value-producing events per month**. That requires a different metric unit: **capability-level monthly count**. "Brand checks performed per month" and "permission audit requests via agent per month" are not derivatives of VR or TSR — they are the count of times the agent did its job. This is the metric that maps to the adoption narrative ("the agent delivered value X times this month") and to the Senior Director level story Pedro is building for Loni.
- **Two Governance Agent candidates (April 22)**:
  - Number of brand checks performed per month
  - Number of permission audit requests performed via agent per month
- **Why this unit matters**: Rate metrics (TSR, VR) normalize for volume — a 60% VR at 100 interactions and at 100,000 interactions read the same. The capability-level count restores the volume signal that VPs need: "this agent is being used 50× more than last quarter." Without it, a successful adoption arc is invisible in your dashboard.
- **When to use each unit**:
  - TSR → *does the system work?* (engineering / platform health)
  - VR intent-level → *does the user get what they came for?* (product experience quality)
  - VRR tiered → *what shape of value distribution are we seeing?* (strategic framing)
  - **BVR capability-count → *how much value did this agent produce this month?*** (adoption narrative, VP-facing)
- **Application**: For every AEM agent, identify 1–2 capability-level monthly counts that map to its reason for existing. These become the headline numbers in the adoption story. Validate definitions with the agent's PM owner; implement with the parallel reporting track owner.
- **Anti-pattern**: Reporting only rate metrics to leadership. The absence of a volume number makes every success story unfalsifiable — nobody can tell if the agent is growing or shrinking.
- **Related**: Metric Definition Ownership — PM Validates, Reporting Track Owner Implements; Two-Validator Pattern for Report Rollout; VRR Is a Tiered Metric; Raw Call Volume Is Mostly the Agent Talking to Itself.
