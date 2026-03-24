# Risks

## Immediate (Act This Week)

**Analytics dashboard loss**
TJ built and owned the Adobe Analytics dashboard. TJ has left the company. If his account is deactivated before ownership is transferred, we lose our primary measurement tool and its custom segments. Transfer ownership, export data, document access. This cannot wait.

## Active Risks

**Vision-reality gap**
The employee meeting demo showed a vision mock, not the actual product. Stakeholders across 15+ teams have formed expectations that do not match reality. This is a trust problem. Every month it goes unaddressed, credibility erodes. The fix is honest communication: write down what Experience Hub is and is not, get leadership sign-off, and communicate it broadly.

**Capacity vs demand**
Two engineers. 15+ stakeholder teams with competing asks. More initiatives than the team can absorb. Without strong PM prioritization and explicit tradeoffs, the team ends up doing many things poorly instead of a few things well.

**No contribution model**
Experience Hub is being treated as a service team. Teams ask for features but do not build them. With two engineers, this is unsustainable. A contribution model where other teams build and own their own widgets is the only way to scale.

**Agent quality**
40 to 50 percent of agent responses are bad or unsupported today. Customers are hitting a wall. There is no standardized way to measure or improve this across Adobe. Driving adoption of agents through Experience Hub before this is resolved would backfire. Additional risks confirmed in Agent Owner Alignment meetings (March 2026): current value/functionality scoring is subjective with no objective measurement, the Onboarding agent has no usage metrics yet (not in production), and the EPA + Discovery interoperability demo may be dropped from Summit due to unresolved blockers.

Root cause confirmed in Loni's working session (March 23, 2026): the current architecture does not support agent reasoning. Agents route to solutions — they don't reason through them. The fix is AO 2.0's agent loop, expected in production May at earliest, June-July realistically. Until then, quality has a structural ceiling that prompt improvements cannot raise. The risk for Experience Hub: surfacing agents prominently before the architecture improves accelerates the trust erosion instead of building it.

**AO 2.0 migration risk**
AO 2.0 is a new architecture, not an upgrade. Teams must port existing agent code into the skills-based model — this is significant engineering work. Ian Boston flagged this in the CXO Skills Catalog context: writing a SKILL.md file is not the same as porting a working agent. Timeline pressure (Summit + May production target) increases the risk that agents are declared ready before the migration is complete or tested.

**Security discoverability — live customer bug**
Customer @geco cannot see the Security and Compliance section in Experience Manager (Feb 11, 2026). The role switcher does not provide a nav path to security features even for asset librarians. Flagged by Bertrand and Andrei Dulvac in September 2025 as a UX concern, now a production issue. Needs a fix, not a roadmap entry.

**Environments widget invisible to new users**
The "My Authoring Environments" widget only appears after a user logs in at least once. First-time users see nothing. Bertrand called this critical in September 2025: "We're going to miss big time on the whole point of the widget." Root cause identified by Sorin. No fix deployed as of March 2026.

**Unified Shell alignment**
The boundary between Experience Hub and Unified Shell is unclear. Both teams are building overlapping things around navigation, widgets, and personalization. Promises were made to align that were never delivered. This creates confusion for stakeholders and potential rework.

**Summit deliverables**
Summit is roughly one month away from March 2026. Deliverables are in progress. Any disruption puts the Summit presence at risk. Shankari should continue driving these while Pedro ramps up.

**Concierge POC**
The Concierge light-up POC with Patrice has no clear product decision. It is unclear whether it should ship, iterate, or stop. The Concierge team has not fully aligned on their requirements.
