# Success Definitions Must Be Agreed Before Metrics Are Scaled

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-30
- **Source**: Yanira 1:1; Yanira's success definition wiki.
- **Insight**: Scaling a measurement dashboard before success definitions are aligned across teams creates a false picture. Each agent team may define "technical success" and "value realization" differently. When those definitions are different but the report shows them side by side, every comparison is misleading.
- **The right asset**: A per-agent success definition document, built jointly by PM and engineering, validated before the dashboard goes broad. In AEM, Yanira holds this as a wiki. Pedro must align Felix's dashboard column definitions to that wiki before presenting to leadership.
- **Application**: Before any cross-agent measurement goes to a senior audience, ask: "Do we have a shared definition of success for each agent in this report?" If no, the numbers are not ready to compare.

## The second axis — definitions drift across askers and across time, not only across teams

*Added 2026-08-06. Sources: the 07-24 KR-status session; the 08-06/07 audit republish; Karthik Penikalapati (Rubin) at the 08-06 AEM Rubin sync.*

The original insight is about definitions varying **between teams**. Three observations say the same corruption happens with a single team and a single definition, along two other axes.

**Across askers.** When the query is generated on demand — an LLM writing SQL against a warehouse — the same question asked twice returns two numbers, because the query is re-derived each time. Karthik Penikalapati, building Rubin's Report Builder against exactly this, verbatim:

> *"If you go and ask like an investigate, it might assume your SQL in a different way when different people ask the same question. This way your report is **grounded to the same SQL query**."*

That is worth noting for where it comes from: a data platform team shipped a product whose entire purpose is pinning the query, which is external corroboration that ad-hoc querying is not a reporting method.

**Across time.** A number published with a link goes stale against its own source. On 2026-08-06 an audit run was republished the same day it was cited in three messages; the catalogue moved 88 → 98 skills and the naming failures 28 → 37. Anyone opening the link read different figures than the message stated. Worse, a rules change can masquerade as progress: an earlier 37 → 28 improvement was entirely a grading change (an underscore downgraded from fail to warn), with **zero teams renaming anything**.

**The general form.** A metric is only stable if three things are pinned, and teams are only one of them:

| Axis | Drifts when | Fix |
|---|---|---|
| Across teams | each team defines success its own way | a ratified per-agent definition |
| Across askers | the query is re-derived per request | a stored, grounded query — one report, one SQL |
| Across time | the corpus or the grading rules move under the number | name the denominator and the run date every time; re-derive a delta by running today's rules over both dates, never by diffing two stored outputs |

**Application:** before publishing any delta, ask which of the three moved. If the rules moved, it is not progress, and reporting it as progress is the most expensive version of this mistake, because it is the one that gets believed.

**A fourth axis, found 2026-08-10: the destination sets the denominator, not your own estate.** Pedro's skill audit measures nine AEM marketplaces and grades disambiguation across them — a real number, produced honestly, on the wrong population. The manifest AEM is moving into, `cx-coworker`, registers thirteen marketplaces from a dozen teams; only one is in the audit. **Every collision figure was AEM-against-AEM, while the routing competition a customer will actually experience is AEM-against-everyone.** The instrument was scoped to what the team owns, which is the natural scope and the one nobody questions, because it is the scope you can fix.

Two mechanisms in the destination file made the gap concrete rather than theoretical: a `plugin_deduplication_strategy: overwrite` where the earliest-listed marketplace wins a name collision and AEM sits tenth of thirteen, and a `required_entitlements` declaration that is mandatory in the shared manifest and that exactly one AEM plugin had ever done. **Neither is discoverable from inside the team's own estate.**

**The general form.** When work is scoped to a shared destination, the measurement has to be re-scoped to that destination before the numbers mean anything, and it has to happen *before* the move rather than after. **Ask what the denominator becomes on the other side, and expect it to grow.** Two consequences worth stating out loud when you re-scope: the new figures will not be comparable to the old ones, and some of the apparent deterioration is not deterioration but the first honest look. Say both before publishing, or the correction reads as a regression you caused.
