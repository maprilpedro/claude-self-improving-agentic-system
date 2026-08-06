# Announce a Forced Surface Migration With an Opt-Out — the Refusals Come Back as Replies Instead of Escalations

**Date identified:** 2026-08-05
**Folder:** ai-product/
**Status:** Promoted — 2 independent observations, three weeks apart, two people, and the second one carries the outcome.

## The pattern

When a platform replaces one AI surface with another for customers who did not ask for it, the instinct is to flip quietly. The migration is planned as an engineering event with a cutover date, and the communication is written afterwards, as a release note.

The mechanism that works instead is small and counterintuitive. **Roughly one week before each cohort flips, announce it in the product and by email to the administrators, say plainly what is coming, and give them a way to say no.** Some will say no. That is the point.

The refusal is going to happen either way. What the pre-announcement controls is **where it lands**. Without it, the customer discovers the change on the day, on a live surface, and the refusal arrives as a support ticket or an escalation through an account team — expensive, late, and attached to a name. With it, the refusal arrives as a reply to an email, a week early, from an admin who is still calm, and it becomes a row in the rollout list rather than an incident.

The window is doing two jobs at once. It is a courtesy, and it is a **cheap opt-out valve that converts your worst-case cohort into a filtered one.**

## The observations

**1. The drawn sequence. 2026-07-15.** Rachel Hanessian (Coworker customer rollout) walked a Miro board of the customer-facing transition: today = the old assistant in place · next = a **banner** reading *"CX Enterprise Coworker is coming soon. It's an evolution of AI assistant"* **plus a Gainsight popup** · then the same banner with a **"Try now"** · eventually the new surface as the default. She asked which AEM surfaces could carry it: *"do you have this type of banner in AEM, or where are all the placements in AEM that we can take over?"* The sequence was described as the plan. **No outcome data was attached to it yet.**

**2. The same mechanism, with the result. 2026-08-05.** Namita Krishnan, on the weekly rollout sync, described it as settled practice and gave the reason: *"before we actually flip them, we are giving them like around a one week heads up notice… just put in some gain site banners or emails to the admins, just giving them a heads up that, hey, this is going to come… coworker's coming, it's a bigger, better AI assistant."* Then the outcome: ***"we've seen some admins actually responding back to that e-mail saying, oh no, I don't want it. So just giving them a chance to be prepared for this transition and opt out if needed."*** She attributed the practice explicitly: *"this is based on a learning we had from the previous trial."*

Two people, three weeks apart, same mechanism, and the second states both that it is a learned correction and that the opt-outs actually arrive.

## Why it matters for a PM

**The opt-out is a measurement instrument, not just a courtesy.** Every admin who replies "no" is telling you, before you have spent anything, that this cohort was going to churn or complain. A migration that produces zero opt-outs on a good-sized cohort is not proof the change is welcome; it usually means the announcement never reached an administrator.

**It changes what "forced migration" costs politically.** The reason teams flip quietly is fear that offering an exit will empty the cohort. In practice the exits are a small, self-selecting minority, and the alternative is not zero refusals — it is the same refusals arriving later, louder, and in front of an account executive.

**It puts a deadline on a surface-ownership question that otherwise drifts.** The announcement has to appear *somewhere*, and that somewhere is a front door someone owns. When the platform team asks "which of your placements can we use", the honest reading is that a decision about your surface is going to be made on the rollout's schedule, with or without you. The pre-announcement window is what turns that from an open question into a dated one.

## How to use it

- **Size the window to the audience, not the engineering.** One week is enough for an admin to react and not so long that the message goes stale. It is set by how fast an administrator reads mail, which is the only variable that matters.
- **Send it to administrators specifically, not to end users.** They are the ones with standing to refuse and the ones who will be blamed internally if the surface changes without warning.
- **Use two channels — one central, one in-surface.** Email reaches the licence holder; the in-product banner reaches the person actually working. Neither alone gets the right reader.
- **Name the replacement in the customer's terms.** *"It's an evolution of AI Assistant"* / *"a bigger, better AI assistant"* — continuity framing, not a new product launch, because a rename reads as something they now have to learn.
- **Log the opt-outs as a cohort attribute, not a failure.** They are the cheapest customer research the migration will produce.
- **If you own the surface being borrowed, answer the placement question in writing before the first cohort.** Which placements, whose copy, who owns the trigger. Silence here is answered by someone else's banner on your front door.

## Related

- ai-product/ [[The Real Cost of a Platform Migration Lands as Rework in Teams Nobody Consulted]] — the engineering half of the same migration; this entry is the customer-facing half.
- ai-product/ [[Selection and Cross-Surface Consistency Are a PM Mandate]] — the placement question is the entry-routing question, and the announcement is what dates it.
- ai-product/ [[PLG Checkbox Antipattern — Announcement Without Ownership]] — the failure mode on the receiving surface: real estate granted, then abandoned.
- leadership/ [[An Undefined Gate Is a Date Nobody Can Give]] — the sibling: the flip date exists only once the announcement content does.
- `.claude/memory/project_experience_hub.md` — the AEM-side instances (Rachel 07-15, Namita + Huong Vu 08-05), with sources.
