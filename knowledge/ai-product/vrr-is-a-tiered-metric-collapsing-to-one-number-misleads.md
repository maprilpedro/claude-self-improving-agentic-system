# VRR Is a Tiered Metric — Collapsing to One Number Misleads

_Section: Measuring AI Features — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-31
- **Source**: Bertrand de Coatpont, 1:1 March 31, 2026.
- **Insight**: Value Realization Rate is not a binary. In AEM's measurement context, VRR is structured as a 5-tier classification (tiers not yet fully defined as of March 31 — Yanira's wiki holds the definition). Collapsing a tiered distribution into a single aggregated percentage hides the shape of the data. If 80% of interactions are tier-1 (minimal value) and 5% are tier-5 (high value), the average number could read as "good" while the distribution is actually poor.
- **Consequence**: Every VRR number reported as a single figure before the tier definitions are applied is potentially misleading. Cross-agent VRR comparison with a single number is especially dangerous — the tiers may be defined differently per agent.
- **Fix**: Get the 5-tier definition (from Yanira's success definition wiki). Report VRR as a distribution, not a single percentage. Aggregate only within a tier or across comparable tiers.
- **Application**: Any AI product measuring "user value" should ask: is this a scalar or a distribution? Before presenting a single VRR number to leadership, verify you know what it's averaging over.
