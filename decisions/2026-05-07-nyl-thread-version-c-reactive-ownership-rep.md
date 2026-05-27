## Decision: Sent minimum-ack reply (Version C) on NYL TBYB escalation thread

## Context

May 6 evening: Brian Thopsey (account team) emailed `aemagentsteam@adobe.com` asking for $0 Beta SKU for New York Life. Corey replied pointing to Summit Labs workbook + flagged "account work is sorted for TBYB program." Bertrand DM'd Corey curious about TBYB enablement. Corey escalated next morning (May 7) to Bertrand + Tina + Pedro asking *"how does one know if a customer is enabled on TBYB?"*

**Pedro's first reply (May 7 7:32 AM):** pointed at Raul's git README + Grafana dashboard. Said *"Data is 3 weeks old, I asked for an update and an easier way to get the data. I'm not aware of other way but might exist."* Did NOT loop Yanira.

**Corey's response (May 7 14:37):** *"This is a broken process alert. + @Yanira Castaneda and already added Tina. An account team is pinging the agent group distro about getting a $0 SKU so who is responding?"* — escalation triggered by Pedro's data-only reply.

**Bertrand (May 7 8:39 AM):** named four things needing documentation (no $0 SKU, all explorer→TBYB migration, list update process, easy customer check) and assigned: *"@Pedro @Yanira can you please take the lead here?"*

**Yanira (May 7 8:05 AM):** scheduled sync next week with Pedro + Raul, coordinating with IT for auto-reply, discussing DaaS Workspace view with Andre, asked Brian for source DL.

**Corey (May 7 9:16 AM):** *"Pedro / Yanira can you get back to the account team at NYL with how to get NYL what they need?"*

**Pedro's recovery decision** — chose Version C (minimum-ack) over Version A (forward-framed lane carve-out) and Version B (time-boxed commitment):

> *"+1 to Yanira's plan. I'll cover data freshness with Raul; aligned with the split. Will sync before publishing externally."*

## Alternatives considered

1. **Version A — forward-framed lane carve-out.** "+1 to Yanira's plan. Quick clarification — Raul owns the org-categorization data and refresh + easier-lookup is in flight. Splitting cleanly: Yanira leads process / auto-reply / DaaS view; Pedro covers data freshness with Raul + lookup ergonomics. Will sync before anything ships externally." Reads as coordinator. ~5 sentences.
2. **Version B — time-boxed commitment.** Same as A + adds *"Aiming to have the dashboard freshness fixed and a one-page lookup for the field by end of next week."* Reads as ownership. Carries delivery risk.
3. **Version C (chosen) — minimum-ack.** 3 sentences. Cooperative, not leading. Defensible during deck-week capacity stretch. Leaves Yanira to fully lead.
4. **Solo NYL email + FAQ skeleton + thread recovery (full play).** 1-2 hours of work. Senior-Director-grade rep but cost-prohibitive during May 11 deck week.

## Reasoning

May 11 Loni + JM deck week. Apoorva punch-list close due May 8. JM warm-up Claude project not shipped. KR4 Priority Consolidation in draft. Real capacity = none for FAQ + solo NYL ownership work.

Yanira's reply was well-shaped (auto-reply, DaaS view, source DL, sync next week). She's leading correctly. Bertrand assigned both Pedro AND Yanira — letting Yanira fully lead is defensible. Version C ack-only signals coordination without taking on work outside scope.

NYL = one customer. Not strategic priority compared to deck.

## Trade-offs accepted

**What Version C buys:** ~5 minutes of writing. Capacity preserved for deck. Defensible coordination posture.

**What Version C costs:** Does not convert the moment into a leadership-perception rep. Bertrand's "@Pedro @Yanira can you please take the lead here?" reads as assignment, not voluntary lead. Version A or B would have been the rep that closes the gap Pedro named May 1 (*"bias for delivery and poor strategic communication skills"*). Version C protects capacity but doesn't move the muscle.

## What Pedro felt afterward

*"Je me sens mal d'avoir loupé le framing initial. Je me sens mal de ça >> 'This is a broken process alert. + @Yanira Castaneda and already added Tina.'"*

Two distinct sources:
1. **Initial framing miss** — first reply was data-only (URLs, "Raul is maintaining," "I'm not aware of other way"). Should have included one literal ownership sentence. Pattern matches the May 1 self-named gap.
2. **Corey's "broken process alert" message** — read as evidence Pedro's reply triggered the escalation. Tina was added (broader visibility). Yanira added by Corey instead of Pedro.

## What's true vs what's not (anti-spiral)

- **True:** Could have shaped the first reply with one literal ownership sentence. Learning rep on reactive-ownership muscle.
- **False:** Corey's "broken process alert" was about Pedro's email. Re-reading: Corey was naming an org-level system gap (no $0 SKU clarity, no field FAQ, no easy TBYB lookup, no clear routing). Diagnosis would have held even if Pedro had looped Yanira. The system gaps existed before Pedro's reply.
- **Cost of escalation:** lower than the felt cost. Bertrand assigned, didn't single Pedro out. Tina seeing the thread = visibility (PMM context, could be net-positive).

## Decision owner

Pedro. Reactive thread, recovery move was Pedro's call to size. Consciously chose protection-of-capacity over rep-on-the-muscle.

## Lesson kept

This is the **third reactive moment in 1 week** where data-instinct fired before ownership-instinct (Felix May 5, Bertrand May 5, NYL May 7). **Pattern is now visible to Pedro in real time** — that itself is the muscle improving (faster feedback loop than 6 months ago). Save the rep, don't replay it.

Two new feedback memories saved this session to lock the lesson:
- `feedback_first_reply_ownership_sentence.md` — first reply on customer-escalation threads needs one literal ownership sentence
- `feedback_dont_litigate_prior_replies.md` — recovery is forward-framed, not backward-framed defense

## Closing move

May 8 9 AM: Send Bertrand 2-line Slack: *"Quick update on NYL — Raul + me will have a refreshed data view and a field-facing lookup by next Friday. Will ping when shipped."* Forward-framed. Time-boxed. Unprompted. Converts feeling into rep #4 on broadcast muscle.

## Supersedes

Nothing prior. First Decision Journal entry on reactive-ownership pattern.

## Outcome (scored 2026-05-27 — first System Review)
The decision's value is as evidence for **H-007** (reactive vs proactive ownership), which reassesses **2026-06-05** — full score lands there. Review caveat: H-007's tracking instrument has been **inactive since May 8** (no interim reactive-ownership reps logged in Status), so the 6/5 reassessment will have thin data and this NYL instance may stay the primary evidence. **Score: immediate recovery move was sound (capacity-protection during deck week, defensible); the missed first-reply framing is the logged learning. Deferred to H-007 on 2026-06-05 — if no further reps land, reassess whether one instance can resolve H-007 or it should be re-scoped/extended.**
