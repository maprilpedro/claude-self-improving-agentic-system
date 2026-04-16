## Decision: Exclude experimentation_agent from Pedro's agent intelligence reporting scope

The canonical list of AEM-owned agents in AO chats DB includes 7 identifiers (experience_governance_agent, governance_agent, aem_experience_development_agent, aem_experience_production_agent, discovery_agent, content_optimization_agent, experimentation_agent). For Pedro's reporting work — the agent intelligence dashboard, JIRA pipeline, and validation meetings with agent PMs — the scope is reduced to 6, excluding experimentation_agent.

## Context

The Rubin outreach on April 15 required sharing a canonical AEM-owned agent list with Karthik Penikalapati. Pedro shared all 7 identifiers. Karthik confirmed Rubin has those agents on April 16.

Separately, Pedro is building agent reporting infrastructure with Felix Delval to answer Loni's question about "% of top requests making it into agents." The report is being validated with agent PMs (Jim done, Apoorva reviewed April 16 with audit findings, Corey pending). The question of which agents belong in that reporting surfaced on April 16 when discussing the Experimentation Agent PM.

## Alternatives considered

1. **Keep experimentation_agent in all scopes.** Would require adding Jim Stoklosa to the validation cycle and building experimentation-specific metrics. Expands Pedro's scope at the moment Law 45 says don't over-expand.
2. **Drop experimentation_agent from the Rubin tagging list too.** Would require a correction to Karthik. But experimentation_agent is technically an AEM-owned agent running on AO, so from Rubin's AEM-footprint perspective it belongs.
3. **Keep two scopes separate (chosen).** Rubin counts all 7 for AEM footprint. Pedro's agent intelligence reports on 6. No correction needed with Karthik.

## Reasoning

Platform footprint and PM reporting scope are different questions. Rubin is answering "how much AEM use is in the AI Assistant" — that's a footprint question, experimentation_agent counts. Pedro's reporting is answering "are AEM's agents giving customers the right things" for a specific set of agents Pedro is tracking with named PM owners, named engineering leads, and a validation path to Loni. Experimentation has a different PM chain (Jim Stoklosa), different surface (left-nav panel in EH), and different audience. Including it in Pedro's reporting would expand scope without strategic fit.

Also: the April 16 Apoorva review surfaced a punch list for Discovery Agent alone. Adding Experimentation Agent to the validation cycle before Discovery is validated would dilute focus on the critical path to Loni.

## Trade-offs accepted

- Pedro's reports will not show experimentation_agent usage. If a future ask from Bertrand/Loni requires an "all AEM agents" cut, Pedro will need to add experimentation_agent at that point or explain the scope.
- Jim Stoklosa remains in the Stakeholder Map as the Experimentation team PM, but is not in Pedro's agent intelligence validation loop.
- Risk of a future audit catching the scope gap ("why isn't experimentation in the AEM agent report?"). Mitigated by being explicit in any artifact about which agents are in scope.

## Supersedes

None. This is the first decision on agent reporting scope boundaries.
