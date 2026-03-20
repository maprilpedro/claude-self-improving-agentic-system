# AEM Experience Hub

## Project Brief

Experience Hub is the new unified home screen for AEM Cloud Service users. It launched in August 2024 under the name "AEM Home" (previously "AEM Launchpad") and has been evolving since. It is not a replacement for existing AEM UIs. It is a faster, more action-oriented entry point that puts the right tools in front of the right personas when they land.

The product is now entering a new phase: integrating with AEM agents. Agent prompts will be surfaced directly inside Experience Hub. This is the current top priority.

Previous PM was Shankari. I am taking over as of March 2026.

## Goal

Make Experience Hub the default, trusted starting point for all AEM users, and the primary surface where AI agents and prompts are discovered and launched.

## Audience

| Persona | Primary Need |
|---|---|
| Content Authors | Quick access to pages, assets, forms. AI-assisted editing via Production agent. |
| Asset Librarians | Asset search and optimization. Discovery and Optimization agents. |
| Developers | Pipeline troubleshooting and dev tooling. Developer agent. |
| System Administrators | Provisioning, permissions, entitlements. Configuration tools. |
| Business Owners | License reporting, governance, brand compliance. Governance agent. |

## Scope

**Experience Hub (Home Screen)** — The landing page at experience.adobe.com. Features widgets, recents, quick actions, announcements, and role-based navigation. Detects licenses automatically and surfaces only what is relevant to the user. Fully customizable per persona.

**AI Assistant + Agents** — Six agents now in early access: Production (page editing), Discovery (asset search), Optimization (renditions), Governance (brand and DRM compliance, PM: Philippe Kapfer), EDA/Experience Developer Agent (pipeline troubleshooting, PM: Brian Chaikelson), sixth agent TBD. Accessed via the prompting window inside Experience Hub. Agent prompts are surfaced through the Prompt Library Platform.

**Prompting Window and Prompt Project** — The specific feature owned directly. This is the customer-facing surface where users interact with agents via prompts. Controls how prompts are displayed and how agent routing works. Weekly Agent Owner Alignment meeting (Mondays) syncs all six agent teams on the customer-facing experience. Notes in Obsidian: 020 Professional/Adobe/Projects/2026/Experience Hub/Agent Owner Alignement.

**Prompt Library Platform** — Backend infrastructure for curating and serving AI prompts across AEM and Adobe Experience Platform. Has an admin UI for prompt management and an embedded end-user experience inside the AI Assistant. Supports role filtering, similarity detection, and B2B/B2C customer detection.

## Team

| Person | Role |
|---|---|
| Me | PM (taking over from Shankari, March 2026) |
| Sorin | Lead engineer |
| Open headcount | Engineer (backfill for Mihai who left) |
| Eugene | UX (US timezone) |
| Shankari | Previous PM, supporting Summit transition |

Engineering team shares daily standup with Cloud Manager UI. Experience Hub gets the first 10 minutes. Monday planning is the main weekly rhythm.

## Org Chart

Shankari reported to Bertrand. I report to Bertrand. Bertrand (Senior Director PM) reports to Loni (VP Product Management for AEM). This project has direct visibility with both.

## Current Status (March 2026)

**What exists today:** A working landing page with widgets, recents, quick actions, and an AI assistant. Controlled adoption experiments are running. Analytics tracking is live in Adobe Analytics. Agent prompts are partially integrated.

**What is not ready:** Full personalization based on user role is not implemented. Most POCs started over the past year were never completed or formally killed. No external team has shipped a custom widget inside Experience Hub.

**Agent quality issue:** Roughly 40 to 50 percent of agent responses are poor or unsupported. Metrics for agent quality are not standardized across Adobe. Grafana covers usage but not quality. LangFuse is being evaluated.

**Immediate risk:** TJ, who built and owns the Adobe Analytics dashboard, has left the company. If his account is deactivated before ownership is transferred, we lose our primary measurement tool. This is the most urgent item right now.

**Summit:** Coming in approximately one month. Deliverables are in progress. Shankari is driving these while I ramp up.

## Key Risks

1. **Analytics dashboard** at risk of deletion when TJ's account deactivates. Transfer ownership this week.
2. **Vision-reality gap.** The employee meeting demo showed a vision mock, not the actual product. Multiple stakeholders believe features are live that are not. This erodes trust every month it goes unaddressed.
3. **Capacity.** Two engineers, 15+ stakeholder teams, and more asks than the team can absorb. Every new initiative without a clear tradeoff makes this worse.
4. **No contribution model.** Teams ask for features but do not build them. Experience Hub is being treated as a service team with the headcount of a two-person startup.
5. **Agent quality.** High failure rates and no standardized quality measurement mean we cannot confidently drive adoption of agents through Experience Hub until this is resolved.
6. **Unified shell alignment.** Promises were made about navigation alignment that were never prioritized. The boundary between Experience Hub and Unified Shell is still unclear.

## Immediate Priorities

1. Rescue the analytics dashboard before TJ's account is deactivated
2. Support Summit deliverables from the backseat while Shankari drives
3. Map stakeholder expectations vs reality (the gap is the main strategic risk)
4. Define what Experience Hub is and is not for 2026 and get leadership sign-off
5. Advance the agent prompt integration as the top product priority for the year

## SD Angle

This project sits at the intersection of three things leadership cares about right now: AI agents, cross-team platform strategy, and AEM Cloud adoption.

Taking over Experience Hub is not a maintenance assignment. It is a chance to own the front door of AEM and make it the surface where agents get adopted at scale.

Three reasons this is visible upward:

**Fixing the trust problem.** The current vision-reality gap is known inside Adobe. Being the PM who names it clearly, resets expectations honestly, and then delivers against a realistic scope is exactly the kind of judgment Bertrand and Lonie are looking for at Senior Director level. The ability to say no and hold the line is what separates directors from senior directors.

**Agent adoption at scale.** Experience Hub is where prompts from all six AEM agents will be discovered. Getting the prompt integration right, building a contribution model with agent teams, and driving adoption metrics are platform-level bets, not feature work.

**Cross-org leadership.** There are 15+ teams with dependencies on this project. Building a stakeholder intake process, drawing clear lines on what Experience Hub will and will not do, and holding that line while maintaining relationships is the core SD skill set. This project is a live test of it.

The story to tell upward: Experience Hub is the product that makes AEM agents real for customers. Without a good front door, the agents stay invisible. I own the front door.
