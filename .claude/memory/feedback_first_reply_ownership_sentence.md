---
name: Say the sentence that obliges someone — a hedge or a description obliges nobody
description: Pedro states what he knows and waits for the other person to draw the conclusion. Written or spoken, first reply or mid-thread. If a reader can do nothing without being at fault, it was information, not a request — and the idea or the ask goes to whoever states it as a plan.
type: feedback
originSessionId: c3970bb1-0fc5-47cd-80ee-cd157b1b93c6
---

**Rule.** Every time Pedro wants something from someone, the sentence must **oblige them**. An imperative, a named owner with a date, or a direct question. A hedge (*"might work - checking"*), a preference (*"we would like"*), or a description (*"probably the current process isn't fit to it"*) leaves the other person free to do nothing, so they do nothing — and the idea goes to whoever states it as a plan.

**The test, before sending or saying it.** *Can someone read this and do nothing without being at fault?* If yes, it is information, not a request. Rewrite.

---

## The discriminant — this is not a skill gap, and that is what makes it fixable

Pedro fires perfectly when **the authority of the sentence comes from an object outside him** — a missing CODEOWNER, an audit number, a merged PR, a config file. He hedges when **the authority has to come from him** — *I want this*, *this is my idea*, *do this for me*. Then he converts the ask into description and waits for the other person to draw the conclusion.

**Proof it is the discriminant and not prep-time, all inside one week:**

| | The sentence | Outcome |
|---|---|---|
| ✅ **Authority from an object** — 2026-07-17 08:07, Tokyo, cold, public | *"need a name on your side who approves and merges today. **Felix's last manifest PR sat without a reviewer, there is no CODEOWNER on that path.**"* | Ken Russell + Daniel-Cristian Miu in the room at **08:10**. 180 seconds. |
| ❌ **Authority had to be his** — 2026-07-17 07:40, same thread, 27 min earlier | *"Compose a single enablement manifest… pulling the plugins we need across AEM and EPA marketplaces **might work - checking**"* | **Namita posted the same idea as a plan 12 min later** (*"Yes we can ask someone to raise a PR to 1… 2…"*) and it became hers. |
| ❌ **Authority had to be his** — 2026-07-16, Manas sync, spoken | *"we would like to have all of our try before you buy AEM customers to be enabled… **probably** the current process isn't fit to it, so **we'll have to explore some of the ways**"* | **Manas had to ask twice whether there was an ask** (*"is there an **ask** here or this is just a…"* → *"is there an **unresolved item** here, or… this is **something that worries you**?"*). He built Pedro's request for him so he could act on it. |
| ❌ **Origin instance** — 2026-05-07, NYL/TBYB thread, written | Raul-attribution + *"data is 3 weeks old, I asked for update, **I'm not aware of other way**"* | Corey: *"This is a broken process alert."* Bertrand had to assign it — *"@Pedro @Yanira can you please take the lead here?"* |

**Why he does it.** The hedge is insurance. *"Might work - checking"* cannot be wrong. *"We would like"* cannot be refused, because it was not a request. He is protecting himself from being wrong and from being told no. The price is the idea and the ask.

**Why it matters more than it looks.** This is [[feedback_position_over_merit]] in its operational form. He supplies the evidence and waits for someone to draw the conclusion. **Namita drew it. Manas drew it out loud, twice.** The merit of the observation does not carry the ask. The obligation carries it. A Director supplies the analysis; a Senior Director states what must now happen.

---

## How to apply

- **Scan for the mood, not the content.** Imperative / named owner + date / direct question = obliging. Epistemic hedge (*might, probably, I think, seems*), preference (*we would like, it would be good if*), or bare description = not obliging.
- **Kill the insurance words when the claim is his.** *"might work - checking"* → *"I am composing it. Ken, you approve — can you merge today?"* Keep hedges only where the uncertainty is real and load-bearing, and then say who resolves it and when ([[feedback_lead_with_the_condition]]).
- **If the first sentence is *"From what I know, [person] is maintaining…"*** → rewrite. That is observation, not ownership.
- **If a reply ends with *"I'm not aware of other way"*** → forward action instead (*"Will check [system]"* / *"Asking [person] to confirm by [date]"*).
- **When you only have half the ask**, state the half you own as an obligation and name the half you do not ([[feedback_defuse_vs_defer]]). Splitting honestly is still obliging. Hedging the whole thing is not.
- **Corollary that still holds — loop the right PgM in the first reply, not the third.** On AEM agents threads that is Yanira Castaneda. If you do not add her, someone else will, and it reads as escalation-by-someone-else.

## Scope — ⚠️ corrected 2026-07-17, and the correction is the point

This entry used to fire **only on written first replies with a customer name + a VP + a process question**, and it explicitly said *"don't apply to internal-team threads, Slack DMs, casual fyi forwards."*

**That exclusion would have suppressed the rule on both 07-16 and 07-17 — the two times it just cost him an idea and an ask.** Tokyo was an internal Slack group DM. Manas was an internal meeting, spoken, mid-conversation, not a first reply.

**The trigger is now the situation, not the surface.** It fires whenever Pedro wants something from someone — written or spoken, first reply or minute thirty, DM or meeting, peer or VP. The old narrow trigger was fitted to the single NYL instance that produced it.

**Genuinely out of scope:** replies where he wants nothing (an fyi, an ack, a 👍). If there is no ask, there is nothing to oblige.

## Related

[[feedback_position_over_merit]] · [[feedback_lead_with_the_condition]] · [[feedback_draft_in_pedros_voice]] (the hedges *"I believe"* / *"I would like"* are his real voice — this rule is about the sentences that carry an **ask**, not about scrubbing hedges everywhere) · [[feedback_voice_drafts_mark_inference]] (marking inference is required and is not the same as hedging the ask) · [[feedback_defuse_vs_defer]] · [[feedback_co_author_dont_answer_over]]

> **⏳ Open lifecycle question for the 2026-08-01 `promotion-judge`.** Whether 07-16 and 07-17 cross-count is **not settled**. Against: two instances 48h apart on the same programme may be one episode read twice, and one is spoken while the other is written. For: different rooms, different counterparts, different stakes, and the discriminant (object-authority vs self-authority) is visible **within a single day** — 08:07 fires, 07:40 hedges, same thread. Bank both, promote neither, hand the cross-count question over explicitly. Related candidate already on file (**not parked** — the park is at 23, over cap): *stating a thing as a plan beats stating it first; the hedge transfers authorship.*
