# Two-Audience Artifact Split — Operator Reports vs Exec Reports

_Section: Stakeholder Communication Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-04-13
- **Source**: AEM agent report review (adbe-agent-dashboard-validation). All-agents report and per-agent reports used the same template. Neither audience was served well.
- **Pattern**: When a report or document serves two audiences with fundamentally different needs, one template will fail both. The fix is not to add more sections — it is to build separate artifacts.
  - **Operator artifact**: customer-level, named entities, action-oriented, detailed funnels. Designed to be acted on by the person who owns the agent or feature.
  - **Executive artifact**: pattern-level, verdict-first, strategic synthesis, portfolio view. Designed to inform judgment at the VP or Senior Director level.
- **Diagnostic signs**: Execs find the report too detailed. Operators find it too abstract. The same section reads differently depending on who's reading it. The "insights" section names customers or orgs the exec doesn't recognize.
- **Application**: Before building any shared report, ask: who are the two audiences, and are their needs compatible? If not, separate the artifacts from the start. Retrofitting is harder and usually produces a frankenstein. The split also creates a natural accountability structure — operator report owned by agent owner, exec report owned by the PM who coordinates across agents.
- **Observed at AEM**: All-agents report was built like a bigger version of per-agent reports. Same nav, same sections, same level of detail. Loni needed fleet-level patterns and a one-sentence verdict. Corey needed LG Electronics' failure breakdown. The same template delivered neither cleanly.
