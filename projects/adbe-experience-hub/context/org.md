# Org and Stakeholders

## Reporting Chain

```
Pedro (Director PM)
  └── Bertrand (Senior Director PM)
        └── Loni (VP Product Management, AEM)
```

This project has direct visibility with Bertrand and Loni. Shankari also reported to Bertrand.

Pedro has been included in two of Loni's small senior working sessions (Session I Agents March 23, Session IV Surfaces March 26). These are first-principles strategy sessions, not status meetings. Being in the room is a credibility signal.

## Key Internal Stakeholders

### AEM Product Teams
- Assets
- Sites
- Forms
- Guides
- Security
- BPO (Business Process Optimization)

### Platform and Infrastructure
- Next Gen team (AI assistant, US-based) — owns the agent orchestration layer
- Unified Shell team — overlapping concerns around navigation and widgets
- DX UE team
- Platform team
- Cloud Manager UI (shares daily standup with Experience Hub)

### Emerging Integrations
- Concierge team (Patrice) — active POC, unclear requirements alignment
- Site Optimizer
- Content Hub
- Prompt Library Platform (PM: Cole Connelly, EM: Joshua Hailpern, Lead Engineers: Somya Biswari and Zeus Courtois)

### Strategy and Architecture (cross-org)
- Conrad Woltge — Principal architect. Documenting agentic design patterns. Confirmed MCP + Skills as integration direction. Flagged security patterns as too sensitive to advance without separating LLM access from certain data.
- Corey Dulimba — Experience Production PM. Holds 1200 real customer questions (unanalyzed). Surfaced the "talk to the CMS" user need: bulk administrative actions via conversation rather than Groovy scripts. Open chat box discovery mechanism but hallucinations are a problem.
- Haresh Kumar — Field/customer-facing PM. Brings real-world customer pushback on pricing and feature readiness. Raised that modernization agent has no enterprise-scale evidence yet.
- Arun Taneja — Working on surfaces/LLM apps as a CAB/CAPS customer discussion topic. Needs slides and a POV first. Opportunity for Pedro to contribute.
- Felix Delval — Built the full agent measurement platform (aem-agent-reports). Daily working session with Pedro as of March 26. Primary technical collaborator on agent reporting standardization.
- Yanira Castaneda — Project Manager running the Agent Owner Alignment Monday meeting (~55 people).

## Stakeholder Pattern

Most teams approach Experience Hub with hypothetical requests. They often have not aligned internally on what they actually want. This creates back-and-forth without clear outcomes.

Classify each relationship as one of three types:
- **Partner** — they build with us (widget contributors, integration owners)
- **Customer** — they consume what we build
- **Observer** — interested but not active

## Slack Channels

- `#experience-hub`
- `#experience-hub-ai-assistant`
- `#aem-home-platform-team`
- `#aem-home-core-team`
- `#temp-experiencehub-dxue`
- `#dx-product-measurement`
- `#tmp_aem_missing_prompt_library`
