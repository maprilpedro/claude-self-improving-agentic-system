# Three-Tier Intelligence Reporting Architecture

_Section: Artifact Architecture — part of `patterns/`; router = README.md._

- **Date**: 2026-05-01
- **Source**: AEM Agent reporting evolution (per-agent weekly → Portfolio Monthly Briefing → AEM Agents QBR)
- **Pattern**: For cross-product or cross-agent intelligence work, three reporting tiers serve three distinct audiences from one data source. Senior leadership tier (quarterly, commercial framing, PMM-led) sits above a senior management tier (monthly, narrative, cross-portfolio) which sits above the operational tier (weekly, deep, routing surface). Each tier has a different cadence, register, and ownership — but they reconcile arithmetically because they share a single data layer.
- **When it applies**: A PM owns a portfolio of products / agents / surfaces with two or more layers of leadership consumption. A single weekly per-product report can't satisfy both the agent PMs (who need depth + routing) and the VPs (who need cross-portfolio narrative + commercial signal). Adding a monthly bridging tier with the right register resolves the "WoW data is too transactional" complaint at the metric layer.
- **Architecture statement worth saying out loud**: *"The QBR is the senior-leadership commercial view. The Portfolio Monthly Briefing is the management narrative. The per-agent reports are the working surface. Three artifacts, three audiences, one data source."* Naming the tiers explicitly is itself a Senior Director move — most PMs ship one report and let the audience self-select.
- **Authorship gradient**: PMM tends to own the senior-leadership tier (commercial). Portfolio PM owns the management tier (narrative + cross-portfolio rollup). Agent / product PMs own the operational tier (weekly routing). Mismatch happens when a PM tries to author at a tier above their accountability — common failure mode is shipping a "QBR" that's actually a per-product weekly report with a quarterly title.
- **Cuts matter as much as keeps**: The management-tier artifact must explicitly cut WoW data, per-customer named diagnoses, and capability gap rows. Those belong in the operational tier. Without disciplined cuts, the management tier collapses back into a glorified weekly.
- **Time and budget**: Tier 1 (operational) is the highest investment — it's where the data layer lives. Tier 2 (management) is mostly aggregation + framing. Tier 3 (senior leadership) is mostly editorial + commercial framing. The investment ratio is roughly 70/20/10.
- **Counter-pattern to avoid**: Three artifacts with three parallel data pipelines = three numbers that don't reconcile = trust collapse. The single-data-source rule is non-negotiable.

---
