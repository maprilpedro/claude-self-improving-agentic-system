---
name: AEP TryBuy Project Artifacts — source of truth (AEP-side)
description: SharePoint location holding AEP's canonical TryBuy / TBYB project artifacts. Pedro flagged 2026-05-07 as the AEP-side source of truth for customer entitlement / TBYB status.
type: reference
originSessionId: c3970bb1-0fc5-47cd-80ee-cd157b1b93c6
---
**URL:** `https://adobe.sharepoint.com/sites/DExProductManagement/Data%20Governance%20and%20Legal%20Programs%20Library/Forms/AllItems.aspx?id=%2Fsites%2FDExProductManagement%2FData%20Governance%20and%20Legal%20Programs%20Library%2FTryBuy%20Project%20Artifacts`

**Path:** SharePoint → DExProductManagement → Data Governance and Legal Programs Library → **TryBuy Project Artifacts**

**Status (2026-05-07):** Pedro confirmed this as **the AEP-side source of truth** for the TryBuy program. Lives under the Data Governance and Legal Programs Library — matters because TBYB has compliance dimensions (HIPAA exclusion criteria, customer eligibility decisions).

**Why this matters for the AEM master-list lane:**
- Confirms AEP has a more formal artifact process than AEM's current state (manual SQL mapping in Grafana, Jabin + Raul).
- This is the **upstream artifact set** that should feed the consolidated Customer Master List. Any AEM-side consolidation must reconcile against these artifacts, not invent a parallel source.
- Likely contains: TBYB customer eligibility criteria, list versions over time, governance approvals, exclusion rules (HIPAA etc.) — exactly what Bertrand named in the NYL thread May 7 ("once calculated based on (?, e.g. no HIPAA), needs to be periodically updated").
- Yanira's DaaS Workspace coord with Andre likely needs to consume / reference this.

**Use cases:**
- Reference in master-list 1-pager as the AEP-side source the consolidated lane builds on.
- Reference in NYL recovery framing for Bertrand May 8 — *"AEP has TBYB artifacts in DEx PM SharePoint; AEM-side mapping is manual. Master-list lane reconciles the two."*
- Reference in the May 12+ scoping call with Yanira + Andre (DaaS) + Raul — point of contact for AEP-side input.

**Don't assume:**
- Access — Pedro should verify he can open the link from his AEP context. Some Data Governance folders are restricted.
- Freshness — SharePoint folders can go stale. Check last-modified dates before treating as canonical.
- Completeness — TryBuy ≠ TBYB universally; confirm if these artifacts cover the full agent-enablement scope or only TryBuy specifically.

**Owner TBD:** likely DEx Product Management custodian. Confirm during master-list scoping call.
