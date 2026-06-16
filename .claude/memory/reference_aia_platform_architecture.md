---
name: aia-platform-architecture-doc
description: "Vineet Barshikar's AIA Platform Architecture doc — the federated-renderer model = the mechanism AEM's rendering standard plugs into; the A2UI-ownership reference."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 5adcc150-22d0-4b0d-80bb-a2af17da6db0
---

Confluence **3878837092** (space `~vbarshikar`), "AIA Platform Architecture — aia-ui-experience, AO 2.0 and aia-extensions", author **Vineet Barshikar** (Slack **@vbarshikar**, confirmed working 2026-06-16). URL: https://wiki.corp.adobe.com/pages/viewpage.action?pageId=3878837092 (read via Atlassian MCP `confluence_get_page`; the `confluence_search_user` endpoint 403'd, page-get worked).

**The A2UI-ownership answer (what Bertrand asked 2026-06-16):** A2UI = the **AIA platform** = aia-ui-experience (customer-facing chat SPA, TS/Vite/React 18/React Spectrum S2) + AO 2.0 (Python/FastAPI backend, A2A protocol) + aia-extensions (plugins). The renderer SDK (`@adobe-dxue/a2ui-renderer-sdk`) + core renderers (`@adobe-dxue/renderers-core`) are **owned by the aia-ui-experience platform team** — the AIA-platform side, **NOT the coworker team**. The doc's OWN open question: whether the a2ui-renderer-sdk lives long-term with aia-ui-experience or the AO platform team (unsettled).

**🔑 Why it matters for Pedro — the rendering-standard mechanism:** the doc lays out a **federated-renderer model**. Domain teams (data, journeys, audiences) publish their **own renderer packages** (`@adobe-aep/renderers-*`) and declare them in **`plugin.json` → `renderers.packages`**; aia-app loads them at runtime via Vite Module Federation; `registerRenderer()` adds the type to the registry. All implement one contract: `FederatedRendererProps { props, children, onAction }`. **This is EXACTLY the hook for an AEM rendering standard**: AEM publishes its own renderer package (asset grids, content/recommendation lists) into the same contract + declares it per plugin, rather than reinventing per agent. A2UI node-tree primitives today = Text / Column / Row / Card / Icon / TextField / ChoicePicker / Button. Governance/contribution gates are in the doc's ownership table (core = aia-ui-experience platform team PR; domain renderer packages = each team's own repo + platform review).

**Other receipts in the doc:** aia-extensions plugin layout = `.claude-plugin/plugin.json` + `skills/<name>/SKILL.md` + `references/` (same open Agent Skills format AEM's marketplace uses — corroborates [[project_aem_agents_intelligence]] skills-mechanism read). A2A frame sequence (AUTH→SESSION_READY→USER_INPUT→text_delta→artifact_created→tool_call→episode_done). `ao/web` (internal UI) explicitly out of scope.

Ties: the rendering lane (AEMAGT-2140, Josh Hailpern's Coworker-UI consolidation, Eugene's A2UI experimenting, Silvia's AO2-UI-repo contribution path) — **AEM's reusable rendering standard = a federated renderer package on this A2UI contract.**
