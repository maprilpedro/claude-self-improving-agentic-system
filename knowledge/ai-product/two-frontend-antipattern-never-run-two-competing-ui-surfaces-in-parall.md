# Two-Frontend Antipattern — Never Run Two Competing UI Surfaces in Parallel

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-10
- **Source**: Loni Stark, H2 Prelim Part 3 (April 2026). Content Hub React vs EDS discussion with Apoorva.
- **Insight**: When a product team maintains two active front-end surfaces for the same capability, every downstream consequence is worse than making either choice. Loni's position: "neither one of those choices is worse than having two of them live."
- **What happens when you run two surfaces**: (1) Engineering is split — both frontends need maintenance, both fall behind. (2) Partners must build extensions for both or pick one and support half the users. (3) Demos become inconsistent — you show React, customer wants EDS behavior or vice versa. (4) Customer escalations multiply — "that feature is GA on one but not the other." (5) You've pushed an architectural decision onto the customer instead of making it yourself.
- **The right move**: Pick one. Commit. Migrate. The transition pain is finite. The two-surface pain compounds indefinitely.
- **Application**: When evaluating any surface consolidation decision, frame the question correctly: "What is the total cost of NOT deciding?" It is always higher than it looks. Loni's framing is decisive: one bad choice beats two permanent ones.
