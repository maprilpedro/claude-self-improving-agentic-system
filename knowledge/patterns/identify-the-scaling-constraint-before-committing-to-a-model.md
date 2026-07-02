# Identify the Scaling Constraint Before Committing to a Model

_Section: Anti-Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-03-31
- **Observations**: (1) Pedro's immediate response to Eugene's contribution model proposal: "Can we build an automated quality check? If yes, model works. If not, we'd be the bottleneck." (2) Manual quality gates in platform teams always become the bottleneck at volume — the PM reviewing every contribution becomes the ceiling.
- **Pattern**: Before committing to any operational model that involves a review or gate, ask explicitly: what happens at 10x volume? Who or what does the checking? If the answer is "a human on the PM or design team," the model has a built-in ceiling. Identify the scaling constraint before the model is ratified, not after you've already committed to teams.
- **The automation question**: In 2026, many manual quality gates can be partly or fully automated. AI/Claude can check design standard compliance, accessibility basics, metadata completeness, conversion metric declaration. The question "can this be automated?" should be asked at model design time, not after the bottleneck appears.
- **Application**: When designing any review-gated contribution model, write out explicitly: (1) what does the gate check; (2) who/what does the checking; (3) what is the expected volume; (4) at what volume does the gate become a bottleneck; (5) what is the automation path?
