---
name: AEM Agent Ownership Matrix (canonical)
description: The 10 AEM agents — PgM/PM/Eng owners, JIRA, AEM team. From slide 44 of `[Internal] - H2'26 AEM & Agentic Web Planning.pptx` (April 2026 internal H2'26 AEM DX Planning Deck).
type: reference
originSessionId: cb38e83a-13e1-40d4-9cc3-d78d0272c5df
---
Canonical agent ownership matrix as of 2026-04-28. Source: slide 44 "H2 2026 AGENT ORCHESTRATOR DEPENDENCIES" of the H2'26 AEM & Agentic Web Planning deck.

| Agent | AEM team | PgM | PM | Eng | JIRA |
|---|---|---|---|---|---|
| AEM Onboarding Agent — Assets Skills | Assets | Pritie Sharda | Pritie (handed off from Nick Whittenburg) | Pritie Sharda | ASSETS-65719 |
| Assets + Content Optimization Agent | Assets | Amit Arora | Greg Klebus | Piyush | AEMAGT-1236 |
| Assets + Discovery Agent Skills | Assets | Prashant | Apoorva Gupta | Piyush | AEMAGT-1120 |
| Experience Governance Agent | Foundation | Robert Guthrie | Philippe Kapfer | Daniel Mrose | AEMAGT-856 |
| Experience Modernization Agent | AO-tracked / Foundation | Yanira Castaneda | Gabriel Walt | Paolo | AEMAGT-538 |
| Experience Production Agent (EPA) | AO-tracked / Sites | Yanira Castaneda | Corey Dulimba | Gilles | AEMAGT-15 |
| Site Advisory Agent | Foundation (Content AI) | Georgeta Vladescu-Viezure | Laurentiu Odoleanu | Remus Stratulat | AEMAGT-2 |
| Development Agent (EDA) | Foundation | Marius Duta | Brian Chaikelson | Remus Stratulat | AEMAGT-1 (also AEMAGT-1282) |
| Sites Optimization Agent | Sites | Juliana Campbell | Hyman Chung | Mihai Corlan | (no JIRA in slide) |
| Market Intelligence Agent | Sites | Juliana Campbell | David | Mihai Corlan | AEMAGT-286 |

## Patterns

- **Yanira Castaneda** = PgM for the two AO-tracked cross-cutting agents (EPA + Modernization). Owns the AO-side reporting plumbing.
- **Pritie Sharda** = PM + PgM + Eng for Onboarding Agent. One-person team. Capacity flag.
- **Piyush** = Eng for both Assets Discovery + Assets Content Optimization. **Same team runs both** (Greg Klebus, COA PM, 2026-06-26): they finalize **Discovery first, then move into Content Optimization** → on the Coworker migration, COA being "not started" is deliberate sequencing behind Discovery, not a stalled agent.
- **Remus Stratulat** = Eng for Site Advisory + Development Agent (EDA). Two Foundation agents.
- **Mihai Corlan** = Eng for both Sites agents.
- Sites has 2 dedicated agents NOT in Pedro's 6-agent reporting taxonomy: Sites Optimization + Market Intelligence.

## Agent classification

- **Sites:** EPA (cross-tracked), Sites Optimization, Market Intelligence
- **Assets:** Discovery, Content Optimization, Onboarding
- **Foundation:** Governance, Development (EDA), Site Advisory
- **AO-tracked / cross-team:** EPA, Modernization (PgM Yanira)
- **Forms:** none in reporting taxonomy

## Discovery Agent classification correction

Pedro initially thought Discovery was Sites. Slide 44 confirms it's **Assets** (label "Assets + Discovery Agent Skills", PgM Prashant who is Assets PgM). Apoorva is in Assets PM track via DAM/DM scope, not Sites.

## ABAC renderer — registered under Governance, functionally assets governance (open, 2026-06-26)

The **ABAC renderer** (conversational authoring of Attribute-Based Access Control policies) is a **Content Hub feature consumed through the Experience Governance Agent via A2A** — authoritative answer from Philippe Kapfer (Governance PM), 2026-06-25 DM: *"ABAC c'est pour Content hub et ça passe par le governance Agent en A2A, mais ils n'ont pas de MCP, donc je ne sais pas ce qu'ils vont implémenter et comment."* So it surfaces + reports under Governance because it routes through the Governance Agent (A2A), but it is functionally a Content Hub / assets-governance capability. JIRA **NXUI-368**. The ABAC / Content Hub team has **no MCP yet** — implementation TBD. Daniel Mrose (@dmrose, also the Governance Agent Eng owner above) is connected; Sorin pinged him + others 2026-06-26.

Two open threads: (1) what the ABAC / Content Hub team will actually implement (no MCP yet) → gates the renderer-audit ABAC board; (2) **reporting-attribution = Pedro's lane** — it shows in Governance usage reports while being a Content Hub capability, so the bucket may need a label. The mechanical "under Governance" is correct (A2A routing); the *functional* owner is Content Hub.

## Source PPTX

`[Internal] - H2'26 AEM & Agentic Web Planning.pptx`. Adobe SharePoint canonical link in [H2 26 Content Planning](https://wiki.corp.adobe.com/spaces/WEM/pages/3788744851/H2+26+Content+Planning) wiki. Local copy in Pedro's Downloads folder as of April 28, 2026.

## How to apply

- When Pedro mentions an agent and needs to know who owns it: look up here first.
- When sharing context about agents to anyone outside the immediate team, this is the canonical ownership.
- If an agent's PM/PgM/Eng changes, update this memory immediately.
- Cross-reference with `customfield_18200` (Assigned PM) and `customfield_18201` (Assigned ENG) in JIRA when verifying.
