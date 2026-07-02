# Failure Taxonomy Needs an Explicit Quality vs Gap Split

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-30
- **Source**: Bertrand de Coatpont's response to W13 agent reports, March 30.
- **Insight**: When presenting agent failure data to senior stakeholders, mixing quality failures (agent tried, something broke) with capability gaps (agent structurally cannot do this) in a single table forces the reader to do the classification work themselves. Bertrand's first refinement request was to split these explicitly. The distinction matters because the response is different: quality failures go to engineering, capability gaps go to the roadmap.
- **Two failure types to surface explicitly:**
  - Quality = `failed-update`, `routing-issue`, `not-enabled`, `not-configured` tags. Agent tried. Fixable.
  - Gap = `unsupported` tag + explicit refusals. Agent cannot. Requires product decision.
- **Application**: Any top failed requests table should have a Type column. One word — Quality or Gap — that removes the inference burden from the reader.
