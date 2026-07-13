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

**2. Custom renderers. 2026-07-10.** An engineer asks the Coworker EM how to migrate existing custom renderers. Joshua Hailpern answers that there are **no renderers any more** — *"these were removed by the coworker team when they reinvisioned how the harness would work."* Every agent that built one now has rework, and the three replacement paths (hybrid page + harness, tools and skills, generative UI) are **different in kind, not a port.** Also absent from every estimate.

Two independent people, two domains (security, UI), two channels, three days apart, same structure.

## Why it matters for a PM

**The port date and the readiness date are different numbers, and the gap between them is made of this.** If you only carry the port estimate upward, you will be held to a date that excludes the work that actually determines whether a customer can use the thing. (This is the mechanism underneath the *Production Readiness* distinction: skills ported **and** provisioning, legal, security, onboarding done.)

**Nobody else will find these, because nobody else is looking across the teams.** The platform team knows what it removed. The security manager knows what his review implies. Neither is scoping the *portfolio's* rework, because neither owns the portfolio. The PM who tracks the migration across agents is the only person positioned to notice, and noticing is a cheap, high-credibility move in front of an engineering VP — it is unplanned engineering cost in *their* org, which is the currency they actually trade in.

## How to use it

- **Hunt the subordinate clause.** When a substrate changes, read the threads for consequences stated in passing by engineers who think they are stating the obvious. That is where the rework is announced.
- **Keep a rework register, separate from the port table.** One line per consequence, per team. It is the delta between "skills ported" and "customer can use it".
- **Bring it up, don't sit on it.** It reframes you from a status reporter into the person who found the cost, and it lands better with engineering leadership than any program update.
- **Assume there is more.** Two in one week, in the same migration, means the scan is not finished. Expect a third.

## Related

- [[An Undefined Gate Is a Date Nobody Can Give]] (parked) — the sibling failure: a date requested against a checklist nobody wrote. This entry is the *content* that should be on that checklist.
- ai-product/ [[Everything Is a Skill — The Agent Dissolves as a Build Unit]] — the same substrate shift, seen from the build-unit side.
- leadership/ [[Definition Ownership Is the Moat on Shared Data Infrastructure]] — whoever writes the readiness definition owns the date.
- `.claude/memory/reference_coworker_enablement.md` — the AEM instances, with sources.
