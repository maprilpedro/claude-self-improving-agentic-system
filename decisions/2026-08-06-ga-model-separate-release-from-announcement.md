## Decision: GA is two milestones, not one — the release is per-plugin and belongs to the teams, the announcement is portfolio-wide and belongs to Pedro

> 🔴🔴 **SUPERSEDED IN PART — 2026-08-10, by Pedro, on reading it back.**
>
> **What survives, and it is now the operative definition of GA:** *"GA = Adobe dit publiquement que les agents AEM sont disponibles, avec legal, security, docs, PMM derrière."* The "announcement" half of this file **is** the GA. It is Pedro's. ➕ **New on 08-10: customer announcements are owed BEFORE the GA** — which is the same machinery Namita Krishnan and Huong Vu asked AEM for on 08-05 (one-week pre-flip Gainsight banners + admin emails) and that AEM has still not answered. That open EH item is now on this file's critical path.
>
> **What is wrong:** the "**release belongs to the teams, per-plugin**" half. Pedro, verbatim, on the sentence built from it — *"complètement faux."* All three phrasings it has worn are dead: a plugin move between `experimental` / `ga` marketplace json files (as written 08-06), the skill's `lifecycle` field (as "corrected" 08-07), and "each team sets its own GA". **The `lifecycle` field was banked as the release mechanism twice and corrected twice. It is not the mechanism.**
>
> **And "two milestones" does not mean what this file says.** The operative split, as Pedro stated it to Bertrand on 2026-08-10, is **GA without the Coworker panel (08-24) vs GA with the panel (~09-21)** — matching the canvas column "Coworker UI with Panel GA" and the Post-GA Fast Follow.
>
> **Predictions below are void** except the 08-24 one. The 08-10 test ("does the room argue about the split itself") cannot be scored, because the split it names was never the live one.
>
> **Root cause, worth keeping.** Pedro said one true thing on 08-06 — *"sépare les deux choses qu'on confond"* — and the elaboration written around it invented a mechanism he never named. **Quote the decision; do not extend it.** See [[feedback_proposal_vs_decision]] and [[feedback_confirm_ask_before_producing]].

**Date:** 2026-08-06. **Decision owner: Pedro Ferreira.** Not escalated, not delegated — he was asked for a call and made it.

## Context

At the Agent Owners Alignment on 2026-08-03, Corey Dulimba rejected the *shape* of the composite GA gate Pedro had been working to — *"I don't know what customer provisioning means. So that's not checked for my agent… That's not something that we even are in control of, so why is that a gate?"* — and proposed the counter-model: *"isn't it just whoever gets added to the manifest would be considered GA?"*, per agent, now. **Brian Chaikelson, Guliz Sicotte and Ankur Arora aligned inside two minutes**, and Ian Reasor removed the risk objection (*"enabling that for customers doesn't turn off AI assistant… no harm, no foul"*). Pedro acknowledged and did not decide, committing to bring a per-agent checklist to the 2026-08-10 call.

Two things then happened that made the choice urgent rather than academic.

1. **The room's model got built.** On 2026-08-04 in `#p42-architecture`, Carsten Ziegeler opened *"Supporting different lifecycles of plugins/skills"* and by 14:33 he and Satya Deep Maheshwari had converged on **one branch, two marketplace json files (`experimental` and `ga`), a plugin being in one or the other**, plus Carsten's Coworker PR `aep-ai#8457` for pattern-based plugin inclusion. **Moving a plugin between the two files is now literally the act of going GA.** The mechanism exists in code whether or not anyone writes a checklist.
2. **Pedro stated the composite plan externally and it held.** On 2026-08-05, on the weekly Coworker rollout sync, he walked Namita Krishnan, Cole Connelly, Yelena Doliner and Huong Vu through GA 08-24, bug bash 08-17→08-21 and a formal AEM commitment on 08-10. **Nobody challenged a date.** Cole: *"wow, that's sooner than I expected, so that's awesome."*

So both models had support, and the checklist due Monday would look completely different under each.

## Alternatives considered

1. **Hold the composite gate.** An agent is GA when skills, naming, manifest, UI, provisioning, security, ORR, legal, quality and reporting are all true. The checklist is a **gate**: rows are conditions, output is a date per agent.
2. **Adopt the room's model.** An agent is GA when its plugin is in the production manifest, per agent, decided by its own team. The checklist stops being a gate at all — each team can already decide — and becomes a **scope disclosure**: what a customer gets and does not get per agent, plus post-GA fast-follows.
3. **Separate the two milestones (chosen).** They are not competing definitions; they are two different events wearing one word.

## The decision

**Take the third path.**

- **Release is a per-plugin act and it belongs to the teams.** A team moves its plugin from the `experimental` marketplace file to the `ga` one when it is ready. This matches the mechanism Carsten and Satya built, unblocks the teams that already declared readiness, and takes Pedro out of a bottleneck he was never adding value in.
- **The announcement is a portfolio event on 2026-08-24 and it belongs to Pedro.** The composite list is not a gate on release — it is the bar for what Adobe says publicly, with legal, security, ORR, AI Ethics, documentation and PMM attached.

**So the artifact due Monday is not one document.** It is a per-agent release state (teams fill it, Pedro holds the format) plus an announcement bar (Pedro holds it, and it is portfolio-level, not per agent).

## Reasoning

The two camps were not disagreeing about *when*. They were attaching one word to two different milestones, which is why neither side could concede without appearing to give up something real.

What Corey actually asked for names the announcement, not the manifest write: *"for our skills to be considered GA in the standalone coworker application **so that as the rest of the field is talking to customers about coworker, AEM is included in those discussions**."* That is a request about the field conversation. His own definition at 17:31 the same day says the same thing — *"GA in this case means that customers will join the cohort roll out that AEP is doing"* — which is a rollout event, not a repository state.

And the composite gate was never wrong about *content*, only about *scope*. Provisioning, legal and AI Ethics genuinely do have to be true before Adobe tells customers AEM agents are generally available. They just have no business blocking a team from putting a working plugin in a manifest.

## Trade-offs accepted

- **Pedro gives up the per-agent gate.** He no longer decides when an individual agent is GA in the manifest sense. That was the leverage the composite model gave him and it is deliberately handed back.
- **Two words now need distinguishing in every conversation**, and the vocabulary is not agreed yet. If "GA" keeps being used for both, this decision quietly reverts. **The naming of the two states is now load-bearing** — and it is the same `lifecycle` field Clint Goudie-Nice asked about on 07-29 and nobody answered.
- **A team can ship into the `ga` manifest before the announcement bar is met.** That is intended, but it means a customer could reach a skill before the docs and the GTM exist. The announcement bar has to be visibly separate or this reads as shipping unannounced.
- **🔴 AI Ethics does not move.** EPA's item still reads *"team will evaluate end of Aug"*, which lands after both the 08-14 sign-off date and the 08-24 announcement, and it sits on Corey's own agent. **This decision does not solve that; it isolates it.** Under the old model it blocked everything. Now it blocks the announcement only.

## What this predicts, so it can be scored

- **2026-08-10, the owners call.** If the separation is right, Corey and Ankur accept the release half without argument (they already declared readiness verbally), and the discussion moves to the announcement bar's contents. **If the room argues about the split itself, the framing is wrong.**
- **2026-08-24.** Either the announcement happens with a bar that was met, or it slips — and if it slips, the test is whether it slips for a reason on the composite list (correct) or for something nobody listed (the list was incomplete).
- **The failure mode to watch for:** teams shipping into `ga` and then treating that as permission to tell customers. If that happens, the two milestones collapsed back into one word and the decision did not hold.

## Related

- `.claude/memory/project_aem_agents_intelligence.md` — the 08-03 Agent Owners Alignment (shard `..._ARCHIVE_2026-W32a.md`), the 08-04 architecture convergence (shard `..._ARCHIVE_2026-W32b.md`), the 08-05 rollout sync.
- [[An Undefined Gate Is a Date Nobody Can Give]] — the gate finally has contents; this decision says which gate.
- [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] — the same failure one layer down.
- `knowledge/hypotheses/parked.md` → *Two Milestones Wearing One Word* — the candidate pattern this decision is the third instance of. ⚠️ Parked, not promoted, and deliberately so.
