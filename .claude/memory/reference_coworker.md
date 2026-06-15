---
name: reference_coworker
description: Coworker = the productized AOv2 / Coworker Harness, the Adobe-native AI assistant at ao.adobe.io/chat. Field guide (Betsy Daly) on Coworker-vs-Claude + the semantic layer + MCP setup.
metadata:
  type: reference
---

**Coworker** = Adobe's native AI assistant running on the Experience Platform Agent Orchestrator = the **productized AOv2 / "Coworker Harness"** (the rebrand tracked in [[project_aem_agents_intelligence]] 2026-06-05 #4). A field "when-to-use-what" guide circulated 2026-06-12 by **Betsy Daly** (Betsy.Daly@Adobe.com — offers live demos) concretizes it.

**Access:** https://ao.adobe.io/chat · plugins https://ao.adobe.io/plugins · MCP config https://ao.adobe.io/mcp

**What it is:** a domain-expert analyst that both answers conversationally AND runs multi-step investigations against live data (CJA/AA). Chatbot analysis, root-cause analysis (finds breakpoint → decomposes funnel → cross-tabs → surfaces Jira), memory across sessions, **27 built-in skills** (audience building, schema exploration, journey creation, exec summaries, experiment analysis).

**The semantic layer = the differentiator (the bankable PM point).** With the *same* MCPs connected, Claude sees raw tools (`runReport`, `findDimensions`, `findSegments`) but zero environment context. Coworker adds: entity resolution (name→exact ID), Knowledge Graph (schema/dataset/audience/destination relationships), cross-session memory, error recovery (auto-substitutes authorized IDs), automated Jira cross-ref, org context (fiscal calendar, naming conventions, known data-quality issues). Guide's line: *"Without the semantic layer, Claude is a universal tool-caller — powerful but uninformed. YOU become the semantic layer."* → This is the **context-is-the-product** thesis in the field (ties Loni's "the question is context" axis + ai-product [[Moat = the Data, Not the Mechanism]]). Parked as a knowledge observation, not yet promoted (1 vendor-doc instance).

**Coworker vs Claude / Claude Code — the split:**
- **Coworker (default for Adobe data):** any CJA/AA/AEP question, RCA, exec summaries, audience/schema/journey work, Jira×data cross-ref, anything wanting carried-forward memory. Runs in a sandbox.
- **Claude / Claude Code:** local files, arbitrary code, non-Adobe APIs (Salesforce/GA), native .pptx/PDF, long-form writing, fast scripting, when you already know exact IDs.

**3 MCPs, plug into both Coworker and Claude:** **CJAMCP** (built-in plugin, 28 tools), **AAMCP** (manual HTTP, https://aa-mcp.adobe.io/mcp, 24 tools), **Fluffyjaws** (33 tools — Jira/Dynamics/docs/env investigation). Claude Code FJ setup now uses a CLI (`fj login`, browser Okta) not the old cookie-paste; AA/CJA via Settings → Connectors.
