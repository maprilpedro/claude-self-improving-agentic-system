---
name: reference_copilot_review_access
description: How to grant a person access to the AEP Co-Pilot Review Tool — clone JIRA NXUI-170; Pedro is now an approver.
metadata: 
  node_type: memory
  type: reference
  originSessionId: f794853c-a98f-49b5-8eeb-9c826487f5af
---

The **AEP Co-Pilot Review Tool** (browse/filter real AO interactions, rate responses, file JIRAs with full trace) at `experience.adobe.com/#/@target-data-platform/co-pilot/review/` is part of Felix Delval's EPA measurement stack, but **access is NOT granted by Felix/Okta directly — it goes through JIRA, project NXUI**.

To give one person rights:
- Clone ticket **`NXUI-170`** ("Product Review tool – Access Request"), fill the user's details, follow the approval flow. (Sourced: Shankari + the FluffyJaws bot inventory, Nov–Dec 2025.)
- Usage/access guide: wiki `display/aepai/Review Tool: Usage Guide`.
- Real examples: Marius Cândea `NXUI-1698` (2026-05-28), Yanira `NXUI-592/593`.

**Pedro is now in the approver loop** — 2026-05-28 Yanira asked *"@Pedro can you provide access to Marius Cândea please."* So he can grant directly, doesn't need to route to Shankari/Felix. Small `[P]`: controlling tool access = recognized owner.

Distinct from: LangFuse (trace/token, prod access via IAM group `GRP-EXPERIENCE-PRODUCTION-AGENT`) and the annotation tool (golden-dataset scoring). The report site itself (`main--aem-agent-reports--aem-epa.aem.page`) needs the **Sidekick** plugin for auth, a separate thing.
