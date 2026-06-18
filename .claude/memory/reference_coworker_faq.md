---
name: cx-coworker FAQ (canonical CXO enablement runbook)
description: The canonical Coworker FAQ for PMs/account teams. Customer-surface direction, terminology lock, AIA migration owner (Raj Patel), and the reporting white-space. How to fetch it via gh.
metadata:
  node_type: memory
  type: reference
---

**Doc:** `OneAdobe/cxo-enterprise-coworker` → `docs/runbooks/coworker-faq.md`. Owner **Babu Ramaraj**, last updated 2026-06-02. Audience = PMs + account/customer-success teams (enablement, customer-facing), not an AEM eng doc.

**Access:** internal GitHub org `OneAdobe` is only visible to Pedro's Adobe gh identity. Two gh accounts on this machine: `maprilpedro` (personal, active by default — gets 404 on OneAdobe) and `pedrofer_adobe` (Adobe). Fetch pattern:
```
gh auth switch -u pedrofer_adobe
gh api repos/OneAdobe/cxo-enterprise-coworker/contents/docs/runbooks/coworker-faq.md --jq '.content' | base64 -d
gh auth switch -u maprilpedro   # restore
```

**What matters for Pedro (AAI reporting lane):**
- *"Teams building new skills → build on the Coworker Harness, not the AI Assistant skill framework"* = harness-default guidance. Mild tension with Pedro's "harness = two-way" door framing, but not a contradiction (Bertrand 06-17 endorsed other-harness-if-Coworker-not-fit; FAQ predates the 06-17 P42 reopening). His "skills portable → harness swappable" holds.
- **Raj Patel** owns the AIA → Coworker migration (Phase 2, Jul 2026, Workstream 1). Intersects Pedro's Rubin-port / reporting-continuity work → stakeholder to map.
- **Surface is not Pedro's concern** — he is surface-agnostic by design. ao.adobe.io deprecated as customer destination, Coworker Chat is the surface; AIA stays "for read/discovery". This neither validates nor threatens his thesis.
- **Reporting white-space:** the canonical FAQ has ~zero on reporting / observability / metrics / usage-credit; pricing TBD; Phase 2 = governance + Org Memory + Business Context, no agent-measurement story. Pedro's reporting/credit lane is unrepresented in the canonical narrative = visibility risk + opening to own.

**Terminology lock (customer-facing):** use "CX Enterprise Coworker", "Coworker Harness", "Coworker Chat"; avoid "Agent Orchestrator", "AO1.0/2.0". Consistent with [[reference_mcp_terminology]]. Companion to [[reference_coworker]] and [[reference_ai_observation_architecture]].
