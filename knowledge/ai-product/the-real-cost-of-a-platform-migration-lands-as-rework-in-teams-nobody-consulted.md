# The Real Cost of a Platform Migration Lands as Rework in Teams Nobody Consulted

**Date identified:** 2026-07-13
**Folder:** ai-product/
**Status:** Promoted — 2 independent observations, different people, different domains, different channels.

## The pattern

When an AI platform changes its **execution substrate** (the harness, the surface, the orchestration layer), the migration is scoped and estimated as a **port** — move the code, move the skills, done. That estimate is produced by the platform team and by the teams doing the porting.

The real cost lands somewhere else. Every downstream team that built against the *old* substrate's assumptions inherits work that was never in anyone's plan, and it surfaces the way all unplanned work surfaces: **dropped in passing, in a Slack thread, by an engineer who assumed everyone already knew.**

The tell is always the same shape. A senior engineer states a large consequence in a subordinate clause, nobody reacts, and it is on no roadmap, no estimate and no status page.

## The observations

**1. Threat models. 2026-07-09.** Setting up the AEM security review for Coworker, Catalin Luta (Sr Manager, security, in the VP's own org) says in passing that **all the teams have to redo their Threat Models**. Nobody in the thread reacts. It is a per-team, per-agent deliverable, triggered purely by the execution surface changing. It appeared on none of the migration's artifacts: not the GA readiness canvas, not the day-after map, not the public "Production Readiness" definition, not the end-of-August port estimate.

**2. Workflow-bearing renderers. 2026-07-10.** An engineer asks the Coworker EM how to migrate existing custom renderers. Joshua Hailpern answers that renderers *"as they existed before, **with deep/complex workflows embedded in them**"* were removed when the harness was redesigned, along with *"direct connections to agents."* ⚠️ **Read the qualifier.** Rendering still exists and is extensible (ADR 001). What is gone is the renderer that **carried a workflow** and had a direct line to the agent. For those there is **nothing to port into** — the replacement is a different mechanism (a real page driven by the harness · a conversation of tools and skills · generative UI), which makes it a **redesign, not a port**, and therefore a **design decision rather than an engineering one.** Absent from every estimate.

*(Correction, 2026-07-13: an earlier draft of this entry said "there are no renderers any more." That over-stated Josh's words and Pedro caught it. The rework is real; the framing was sloppy. The instance stands — the cost is unplanned, and the ADR shows how large it is: two repos, two PRs, and the `ao` one has to land first.)*

Two independent people, two domains (security, UI), two channels, three days apart, same structure.

## Why it matters for a PM

**The port date and the readiness date are different numbers, and the gap between them is made of this.** If you only carry the port estimate upward, you will be held to a date that excludes the work that actually determines whether a customer can use the thing. (This is the mechanism underneath the *Production Readiness* distinction: skills ported **and** provisioning, legal, security, onboarding done.)

**Nobody else will find these, because nobody else is looking across the teams.** The platform team knows what it removed. The security manager knows what his review implies. Neither is scoping the *portfolio's* rework, because neither owns the portfolio. The PM who tracks the migration across agents is the only person positioned to notice, and noticing is a cheap, high-credibility move in front of an engineering VP — it is unplanned engineering cost in *their* org, which is the currency they actually trade in.

## How to use it

- **Hunt the subordinate clause.** When a substrate changes, read the threads for consequences stated in passing by engineers who think they are stating the obvious. That is where the rework is announced.
- **Keep a rework register, separate from the port table.** One line per consequence, per team. It is the delta between "skills ported" and "customer can use it".
- **Bring it up, don't sit on it.** It reframes you from a status reporter into the person who found the cost, and it lands better with engineering leadership than any program update.
- **Assume there is more.** Two in one week, in the same migration, means the scan is not finished. Expect a third.
- **🔑 Price the keys in the same conversation — the rework often arrives disguised as autonomy** (added 2026-08-03, folded in from a parked candidate). A central platform will devolve a decision to the consuming team **and frame it as a grant**. On 2026-07-15 Horia Galatanu told AEM the rail was no longer mandated — *"it becomes a bit more of a product by product thing… You shouldn't feel like you're waiting for the core team to build something… you're holding the keys to your destiny"* — and Manas Garg closed it: *"from this point onwards, these are application concerns."* **The grant is real** (the rail-vs-full-screen fork genuinely became AEM's). **It is simultaneously an unscoped transfer of UI work onto the consuming team's date, and a pre-built answer to "why isn't it ready" — because it is your job now.** In that room nobody priced it, including Pedro, while EH sat at roughly one effective engineer plus two June hires. **The move is not to refuse the keys. It is to accept the ownership and price it out loud in the same conversation** — what it adds to the estimate, and whose headcount pays — *before* the autonomy gets quoted back at you as a commitment. A grant you accepted silently becomes a deadline you agreed to.

## Related

- [[An Undefined Gate Is a Date Nobody Can Give]] (promoted to `leadership/` 2026-08-03) — the sibling failure: a date requested against a checklist nobody wrote. This entry is the *content* that should be on that checklist.
- ai-product/ [[Everything Is a Skill — The Agent Dissolves as a Build Unit]] — the same substrate shift, seen from the build-unit side.
- leadership/ [[Definition Ownership Is the Moat on Shared Data Infrastructure]] — whoever writes the readiness definition owns the date.
- `.claude/memory/reference_coworker_enablement.md` — the AEM instances, with sources.
