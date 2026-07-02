# Cross-Region Data Aggregation Is a Compliance Risk in AI Measurement

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-31
- **Source**: Ian Boston (via Bertrand 1:1, March 31, 2026).
- **Insight**: AI agent interaction data is collected per region (in AEM: VA, NLD2, AUS5, CAN2, GBRS, IND1). Re-aggregating that data across regions for a unified report may violate data residency laws or contractual data governance agreements — especially in EU regions (GDPR) and regulated industries. The data pipeline may be technically capable of cross-region aggregation while being legally prohibited from doing so.
- **Important distinction**: The AEP Co-Pilot Report itself provides per-region data — the source is clean. The compliance breach happens in the aggregation step performed by the consuming pipeline (Felix, Lara), not at the source. This matters for framing the fix: it's a pipeline behavior problem, not a platform problem. The source doesn't need to change — the aggregation logic does.
- **Why PMs need to own this**: PMs who commission reporting infrastructure are often unaware of data governance constraints. Engineering builds what is technically possible. Legal and data governance teams are not automatically in the loop. The PM asking "do we have the right to aggregate this?" is the right check.
- **Application**: Before scaling any cross-region AI measurement pipeline, explicitly ask: what data residency rules apply to each region? Does the pipeline aggregate after extraction? If yes, that aggregation step may be the compliance breach — even if the source provides clean per-region data.
