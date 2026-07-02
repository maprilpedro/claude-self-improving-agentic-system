# Pilot a New Model Through an Existing Feature, Not a New Build

_Section: Anti-Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-03-31
- **Observations**: (1) Eugene Bannykh proposed using +Add Extension (an existing EH feature) as the pilot mechanism for the contribution model — instead of building a new contribution infrastructure from scratch. (2) The feature already exists; the model being tested is the governance and collaboration process around it.
- **Pattern**: When proposing a new operating model (contribution model, collaboration process, review workflow), find the feature that already exists and run the pilot through it. This reduces engineering risk, shortens the feedback loop, and produces evidence with real constraints rather than hypothetical ones.
- **Why it works**: A pilot through an existing feature fails fast on the real friction (permission model, quality gate, team adoption) without waiting for new infrastructure to be built. If the model doesn't work with the existing feature, building a new surface for it won't fix the underlying problem.
- **Application**: Before committing to build new tooling for a process change, ask: is there an existing feature that could carry a pilot version of this? Use it. Build new only once the process is proven.
