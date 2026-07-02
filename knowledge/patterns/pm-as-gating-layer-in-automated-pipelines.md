# PM as Gating Layer in Automated Pipelines

_Section: Anti-Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-04-02
- **Source**: Philippe Kapfer's feedback on the report-to-JIRA trial, April 2, 2026.
- **Observations**: (1) Auto-created JIRA stories from the EGA report trial created overhead — some were duplicates, some partially relevant. Philippe's first ask was a manual trigger, not better filters. (2) The "fluffyjaw" reference signals a prior experience with noisy auto-created tickets that eroded trust in an automated system. (3) His framing: "Once the quality improves, we can decide to automate." The gate is a trust-building step, not a permanent constraint.
- **Pattern**: When automation creates work items that land directly in a PM's or engineer's backlog, the PM needs a review gate before creation — not after. Automating past that gate produces noise, creates cleanup work, and erodes trust in the pipeline. The right model: pipeline generates *candidates*, PM reviews and approves, then artifacts are created. The gate is the product.
- **Why this matters**: A backlog is a prioritized, trusted list. Every low-quality item added to it degrades the signal of the whole list. PMs protect their backlogs the way engineers protect their codebase — and for the same reason.
- **The trust ladder**: Manual trigger (PM approves every story) → curated auto (PM sets rules, reviews exceptions) → full auto (proven quality, PM spot-checks). Don't skip steps.
- **Lightweight gating mechanism**: Slack notification with candidate list before JIRA creation. PM responds with approval or filters. Only confirmed items become stories. No additional tooling required.
- **Application**: Before automating any workflow that creates work items for another team, ask: does this person's backlog have a trust contract? If yes, get their approval on the gating model before running the first batch. Start with manual trigger regardless of what's technically easier.
