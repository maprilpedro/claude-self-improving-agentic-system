# Two-Track Reporting Infrastructure — Fast Iteration vs Stable Foundation

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-30
- **Source**: Yanira 1:1, AEM agent reporting setup.
- **Insight**: When building measurement infrastructure for an AI product, two tracks often need to run in parallel: (1) a fast-iteration track (manual, PM-driven, quick to change) that produces learning quickly; (2) a stable-foundation track (engineering-backed, data-platform integrated, scalable) that takes months. Confusing the two stalls both. The fast track should not wait for the foundation track to be ready. The foundation track should use the fast track's output as a spec.
- **Pattern**: Get the fast track to ~80% stable first. Use it to learn what the report needs to contain. Then hand that spec to the infrastructure team. This way the infrastructure team builds the right thing, not a guess.
- **Risk**: If the foundation team (DAS in this case) has a different motivation (cost tracking vs product quality), their natural output will not match what PMs need. Explicit alignment on requirements before they build is critical.
