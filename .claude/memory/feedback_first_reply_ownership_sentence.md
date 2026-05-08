---
name: First reply on customer-escalation threads needs ONE explicit ownership sentence
description: Data-dump replies on threads with VPs / customer escalations read as "I don't know" even when implication is "fix in flight." First reply must have a literal ownership sentence.
type: feedback
originSessionId: c3970bb1-0fc5-47cd-80ee-cd157b1b93c6
---
**Rule.** When Pedro replies first on a thread that includes (a) a customer name, (b) a VP-level person (Bertrand, Loni, JM, Conrad), and (c) a process / ownership question — the reply must include **one literal ownership sentence** even if the rest is technical content.

**Why:** Pedro's natural style is to point at data (git URLs, dashboards, "Raul is maintaining"). At VP read-speed, that reads as *"I don't know, here's the data trail."* Implication ("Raul owns this so it's covered") doesn't survive phone-screen reading between meetings. Concrete trigger: 2026-05-07 NYL / TBYB thread — Pedro replied with Raul-attribution + "data is 3 weeks old, I asked for update, I'm not aware of other way." Corey Dulimba escalated next message with *"This is a broken process alert."* Bertrand had to assign *"@Pedro @Yanira can you please take the lead here?"* That assignment is the cost — Pedro got pulled into a deliverable that was avoidable with one ownership line up front.

**The missing line, expressed three ways:**
- *"Raul owns this; I'll close the loop with him by [time]."*
- *"NYL: I'll get the answer to the account team by EOD."*
- *"Routing to [PgM name] for process; I'll cover the data side."*

Any of those. Pick one. Pair with the technical content if needed. Don't omit.

**Also true (corollary): loop the right PgM in your first reply, not the third.** On AEM agents threads = Yanira Castaneda. If you don't add her, someone else will, and it'll read as escalation-by-someone-else.

**How to apply:**
- Before sending: scan first sentence for an active verb attributable to a named person ("Raul will," "I'll," "Yanira owns").
- If first sentence is *"From what I know, [person] is maintaining…"* → rewrite. That construction is observation, not ownership.
- If reply ends with *"I'm not aware of other way"* or similar → delete or rephrase as forward action ("Will check [system]" / "Asking [person] to confirm").

**Don't apply this rule to:** internal-team threads, Slack DMs, casual fyi forwards. Customer-escalation + VP-visibility = trigger.
