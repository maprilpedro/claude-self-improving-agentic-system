---
name: aia-platform-architecture-doc
description: "Vineet Barshikar's AIA Platform Architecture doc — the federated-renderer model = the mechanism AEM's rendering standard plugs into; the A2UI-ownership reference."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 5adcc150-22d0-4b0d-80bb-a2af17da6db0
---

> ## 🔴 SUPERSEDED IN PART — READ THIS FIRST (reconciled into the entry at the 2026-08-03 System Review; the warning had sat in MEMORY.md unreconciled since 07-10).
>
> **The federated-renderer model below is no longer the live mechanism.** **Joshua Hailpern, 2026-07-10: the workflow-bearing renderers *"were removed by the coworker team when they reinvisioned how the harness would work"*** — and he handed AEM three replacement paths to choose among (hybrid / tools+skills / generative UI). **So: do NOT pitch "AEM publishes a federated renderer package into `plugin.json → renderers.packages`" as the current hook.** That was the mechanism as documented by Vineet in June; the Coworker harness re-architecture removed it.
>
> **What is still accurate here:** the ownership answer (A2UI = the AIA platform; renderer SDK owned by the aia-ui-experience platform team, not the Coworker team), the plugin layout, the A2A frame sequence, and the general *shape* of the argument — that a rendering contract carries structure and a domain team can supply its own renderer. **What is stale:** the specific registration mechanism and the assumption that the renderers exist to plug into.
>
> **Live successors:** the three rendering capabilities are distinct and must not be collapsed — Manish Bansal's A2UI card + backend call (rendering OUT, actionable), Pankaj Sangra's inline-URL render (rendering OUT, passive), and issue #2300 PageUrl-context-INTO-agent (Eugene's question). See [[project_aem_agents_intelligence]] 07-20 block and the knowledge entry [[A Rendering Contract Carries Structure, Not Skin — the Brand Travels Only Where You Own the Renderer]]. The 07-10 removal is also observation #2 in [[The Real Cost of a Platform Migration Lands as Rework in Teams Nobody Consulted]].

Confluence **3878837092** (space `~vbarshikar`), "AIA Platform Architecture — aia-ui-experience, AO 2.0 and aia-extensions", author **Vineet Barshikar** (Slack **@vbarshikar**, confirmed working 2026-06-16). URL: https://wiki.corp.adobe.com/pages/viewpage.action?pageId=3878837092 (read via Atlassian MCP `confluence_get_page`; the `confluence_search_user` endpoint 403'd, page-get worked).

**The A2UI-ownership answer (what Bertrand asked 2026-06-16):** A2UI = the **AIA platform** = aia-ui-experience (customer-facing chat SPA, TS/Vite/React 18/React Spectrum S2) + AO 2.0 (Python/FastAPI backend, A2A protocol) + aia-extensions (plugins). The renderer SDK (`@adobe-dxue/a2ui-renderer-sdk`) + core renderers (`@adobe-dxue/renderers-core`) are **owned by the aia-ui-experience platform team** — the AIA-platform side, **NOT the coworker team**. The doc's OWN open question: whether the a2ui-renderer-sdk lives long-term with aia-ui-experience or the AO platform team (unsettled).

**🔑 Why it matters for Pedro — the rendering-standard mechanism:** the doc lays out a **federated-renderer model**. Domain teams (data, journeys, audiences) publish their **own renderer packages** (`@adobe-aep/renderers-*`) and declare them in **`plugin.json` → `renderers.packages`**; aia-app loads them at runtime via Vite Module Federation; `registerRenderer()` adds the type to the registry. All implement one contract: `FederatedRendererProps { props, children, onAction }`. **This is EXACTLY the hook for an AEM rendering standard**: AEM publishes its own renderer package (asset grids, content/recommendation lists) into the same contract + declares it per plugin, rather than reinventing per agent. A2UI node-tree primitives today = Text / Column / Row / Card / Icon / TextField / ChoicePicker / Button. Governance/contribution gates are in the doc's ownership table (core = aia-ui-experience platform team PR; domain renderer packages = each team's own repo + platform review).

**Other receipts in the doc:** aia-extensions plugin layout = `.claude-plugin/plugin.json` + `skills/<name>/SKILL.md` + `references/` (same open Agent Skills format AEM's marketplace uses — corroborates [[project_aem_agents_intelligence]] skills-mechanism read). A2A frame sequence (AUTH→SESSION_READY→USER_INPUT→text_delta→artifact_created→tool_call→episode_done). `ao/web` (internal UI) explicitly out of scope.

Ties: the rendering lane (AEMAGT-2140, Josh Hailpern's Coworker-UI consolidation, Eugene's A2UI experimenting, Silvia's AO2-UI-repo contribution path) — **AEM's reusable rendering standard = a federated renderer package on this A2UI contract.**
