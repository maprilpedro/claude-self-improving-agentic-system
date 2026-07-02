# Regional Failure Concentration Is a Diagnostic Signal

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-01
- **Source**: AI-Assistant-Findings.md — NLD2 46% failure rate across agent interactions.
- **Insight**: When failure rate data is available by region, look for concentration before averaging. NLD2 showing a 46% failure rate while overall rates are lower means the aggregate number understates the problem in that region and overstates it in others. A regionally concentrated failure pattern suggests an infrastructure, latency, or configuration issue specific to that region — not a prompt quality or agent logic problem.
- **Application**: Any cross-region AI product should segment failure data by region before drawing conclusions. If one region is significantly worse, investigate root cause (data residency, latency, regional model deployment) before averaging it away.
