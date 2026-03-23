---
name: AEM Experience Hub project context
description: Full context on the Experience Hub project - what it is, who owns it, team, org, state, risks, and SD angle
type: project
---

AEM Experience Hub is the unified home screen / landing page for AEM Cloud Service at experience.adobe.com. Launched August 2024. Previously named AEM Home and AEM Launchpad. Not a replacement for existing AEM UIs. An action-oriented entry point that surfaces the right tools per persona.

**Current PM:** User (took over from Shankari in March 2026)

**Why:** Shankari is on the user's team (peer PM, not a direct report) and is moving off the project. User is taking over a high-visibility project directly watched by Bertrand (Senior Director PM, user's boss) and Loni (VP Product Management for AEM).

**Team:**
- Shankari: peer PM on the team, currently still driving Summit deliverables before handing off fully
- Sorin: lead engineer (key person, strong technical judgment)
- Open headcount: backfill for Mihai who left (hiring in progress)
- Eugene: UX Designer, US timezone, reports to Silvia Mulet
- Silvia Mulet: UX Manager, leads UX team on Experience Hub. Booking time with Pedro and Eugene to review current UX projects and next steps.
- Was 3 engineers, now 2

**Org:**
- User → Bertrand (Senior Director PM) → Loni (VP PM for AEM)

**Top priority for 2026:** Integrating AEM agents into Experience Hub. Agent prompts surfaced inside Experience Hub via the Prompt Library Platform. Five agents: Production (page editing), Discovery (asset search), Optimization (renditions), Governance (brand/DRM compliance), Developer Agent (EDA — Experience Developer Agent, owned by Brian Chaikelson who reports to Bertrand). Pipeline troubleshooting is a skillset within Developer Agent, not a standalone agent.

**Prompt Library Platform:** Backend infrastructure for curating and serving AI prompts. Admin UI + end-user UI embedded in AI Assistant. Supports role filtering, similarity detection, B2B/B2C detection. PM: Cole Connelly. EM: Joshua Hailpern.

**Key risks as of March 2026:**
1. TJ's Adobe Analytics dashboard at risk of deletion (TJ left the company, account deactivation pending). Urgent.
2. Vision-reality gap: employee meeting demo showed vision mock, not actual product. Multiple stakeholders have false expectations.
3. Capacity: 2 engineers vs 15+ stakeholder teams with competing asks.
4. No contribution model: teams ask for features but don't build them.
5. Agent quality: ~40-50% bad responses, no standardized quality measurement across Adobe. Confirmed in Agent Owner Alignment meeting 2026-03-17. Root causes: no defined success criteria per agent, LangFuse piloted by some teams only (not centralized), Grafana covers usage not quality, Prompt Library has no review/approval process before prompts reach customers, conversations derail and users don't return. User flagged this to Horia (CXO Skills Catalog owner) with a quality caveat for AEM Content skills 27-35 and a wiki note. This is a known risk that could undermine Summit credibility if "A = Available" is interpreted as production-ready.
6. Unified Shell alignment: boundary between Experience Hub and Unified Shell still unclear.

**Immediate context (March 2026):**
- Summit is ~1 month away. Shankari driving Summit deliverables. User staying in the backseat.
- Post-Summit: user sets direction, builds roadmap with Sorin, resets stakeholder expectations.
- 30-60-90 day plan exists in Obsidian vault.

**Obsidian vault folder:** /Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Experience Hub

**Slack channels:** #experience-hub, #experience-hub-ai-assistant, #aem-home-platform-team, #aem-home-core-team, #temp-experiencehub-dxue, #dx-product-measurement, #tmp_aem_missing_prompt_library

**Historical context (August 2025, around GA launch):**
- User previously agreed with @adulvac to place Security widget at top of dashboard for Security & Dev persona. Shankari disagreed — she believes Security Admin is not the most important persona. Unresolved. Needs data to settle post-Summit.
- Duplicate Detection feature was shown in Summit demo but not released. @jmallory confirmed it was "not beyond a Summit demo." This is a concrete example of the vision-reality gap.
- Loni gave positive signal on Sites Optimizer being connected to Experience Hub. Her framing: PLG (Product-Led Growth) in-product nudge. She sees Experience Hub as a growth driver, not just navigation.
- Product Announcement widget was blank on a Volkswagen customer screen. Bug in production at GA.

**CXO Agentic Skills Catalog (March 2026):**
- User flagged to Horia that AEM Content skills 27-35 are marked "A" but agent quality is ~40-50% failure rate with no standardized measurement. Risk of overstating readiness to Amit.
- Ian Boston (principal architect) raised a bigger concern: AO 2.0 is a completely new architecture. Teams would need to port existing agent code to ship real skills — significant engineering work, not just writing SKILL.md. 4 weeks to Summit is tight.
- Developer Agent (EDA) has no row in the catalog. User flagged to Brian Chaikelson and Bertrand.
- User asked Shankari for clarity on what specifically she needs reviewed/updated.

**How to apply:** When working on any Experience Hub task, start with this context. The user is new to the project, ramping up, and trying to establish credibility with Bertrand and Loni. Every artifact should help close the vision-reality gap or advance the agent integration priority.
