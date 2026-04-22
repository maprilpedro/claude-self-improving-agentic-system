---
name: Conversation link optional when none exists
description: When asking for Teams/Slack/email links for Status & Todo updates, accept that some meetings don't have one. Date + time + meeting name is sufficient for internal-only sessions.
type: feedback
originSessionId: f2f7afb5-77f7-464b-bde1-71b40503f09e
---
Rule. Always ask for a conversation link when updating Status & Todo files (per existing CLAUDE.md rule). But accept "I don't have a link, the date/time/meeting name is enough" as a complete answer for internal-only meetings where no external artifact exists.

**Why.** On 2026-04-21, after I processed the P42 Status meeting transcript and updated the Status & Todo file, I asked Pedro for a Teams meeting link or similar. He answered: "I dont have a link - mentioning in P42 status, the time and date is enough for this one." Some internal meetings simply don't generate a shareable artifact. Demanding one when there isn't one adds friction. The date/time + meeting name in the session log IS the pointer.

**How to apply.** Ask the question per the rule. If the user says no link exists, don't re-ask, don't apologize excessively, don't force a placeholder. Accept the date/time/meeting name reference in the session log as sufficient and move on. If a link exists later, the user can add it themselves.

**What still needs a link.** External meetings (customer calls, cross-org syncs), Slack threads referenced in asks, Confluence proposals, email threads that contain decisions. Those have artifacts and deserve the pointer.
