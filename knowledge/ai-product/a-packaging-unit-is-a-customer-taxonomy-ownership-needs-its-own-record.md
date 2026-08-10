# A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record

**Source:** `#p42-architecture` thread `1784580015.006749` (Ian Reasor → Carsten Ziegeler → Ankush Malhotra → Satya Deep Maheshwari → Ian Boston, 2026-07-20 → 07-28), plus a live audit of `Adobe-AEM-Foundation/aem-aia-extensions`, `epa-experience-generation-extensions`, `aemforms-aia-extensions` and `ao-plugin-extensions-aem-onboarding` (2026-08-03).
**Date:** 2026-08-04

## The claim

In an extensible AI platform, the **packaging unit** (AOv2 calls it a plugin; elsewhere a bundle, an app, a pack) is what the customer installs, sees and pays against. Its granularity is therefore a **customer-taxonomy decision**, not an org-chart decision — even though the same unit is also, mechanically, the unit of versioning, of CODEOWNERS and of dependency declaration.

Carsten Ziegeler, verbatim, 2026-07-21:

> *"Plugins are a mechanism for distribution — with that these are customer facing. We have to find the right granularity that makes sense for our customers, and not reflect our org/team structures. Right now, I would rather go with coarse grained plugins that make usage easier and enable use cases we even do not think about today."*

Ian Reasor reached the same place from the other side, asking *"Since this is customer-facing, perhaps this shouldn't be an engineering decision. Do we need to bring this decision to PM?"* Carsten: *"yes, right — this should not be an engineering decision."*

## Why it bites — the axes are many-to-many, and you can only package on one

Measured on AEM's real catalogue (2026-08-03, 107 skills across four marketplaces):

- **One agent spans several product areas.** EPA alone splits across `content` (7 skills), `edge` (4), `sites` (3).
- **One product area spans several agents.** `aem-assets` carries both `aem-assets-discovery` (Discovery agent) and `aem-assets-content-optimisation` (Content Optimization agent) — two agents, two PMs.

So a name, a folder or a plugin boundary can encode the customer's taxonomy **or** the builder's, never both. Whichever axis you package on, **the other axis stops being derivable and needs an explicit record.**

## The corollary that gets missed

Teams reach for the packaging unit as an ownership record because it is the only structured thing available. It is a bad one, and the failure is silent:

| Record | What it actually answers | State when observed |
|---|---|---|
| `author` in the marketplace entry | who wrote this | 11 of 12 plugins said "AEM Team" — a field everyone fills identically says nothing |
| CODEOWNERS | who must review changes to this path | the only machine-enforced one; GitHub validates it and flagged an unresolvable team on line 1 |
| `domain` in the skill file | what this capability is about | 2 of 107 skills carried it, and the one team that did wrote `aem-forms / form authoring (structure)` — an **application**, not an owner |

Note the last row: even the team that did the work put a *product* value in the field others hoped would carry *ownership*. The classification field will not become an ownership field by wishing.

## Measured again, wider — 2026-08-05

A repeatable audit over **88 skills across nine marketplaces** (`OneAdobe/aem-coworker-audits`, published run) put numbers on point 3 below, and they are worse than the first read suggested.

| Signal | State |
|---|---|
| `domain` declared | **18 of 88** — and in **three incompatible formats**: `Assets`, `aem-forms / form authoring (field rules)`, empty |
| Application derivable from the skill *name* | 67 of 88 |
| Application derivable from **anything at all** | **67 of 88. Twenty-one skills say nothing.** |

Two things this settles.

**A field that exists is not a field that answers.** Coverage of `domain` went from 2/107 to 18/88 as more teams filled it in, and it still cannot be grouped on, because nobody agreed a format. The same audit found the parallel case on a different field: of the 24 skills carrying a `when-to-use`, **13 restate their own description** — full coverage, zero disambiguation. Asking for coverage a second time moves neither.

**So the record has to be ranked, not single.** The working design is a four-tier ladder — hand-maintained map → declared field → inferred from the name → unassigned — where **every row reports which rung classified it**. That is the honest version of an ownership record when no single source covers the corpus: not one field pretending to be authoritative, but an explicit precedence with the guess labelled as a guess. The hand map goes *first*, not last, because it is the only rung anyone ratified and it must be able to correct a wrong inference rather than only fill a blank behind one.

## The corollary that costs the most — the telemetry has to carry the axis you chose

*Added 2026-08-06 (AEM Rubin sync). Source: transcript `20260806 - AEM Rubin Sync`, Karthik Penikalapati + Venkatesh Kunda (Rubin), with Angela Han present.*

Picking the axis is the visible half of the decision. The invisible half is whether the **measurement substrate logs it** — and the two can be settled on the same day, by different people, in opposite directions.

The AEM case, in hours:

- **Morning.** The agent axis is rooted on the **plugin**, on measured evidence: the plugin is declared on 88 of 88 skills and no plugin has ever belonged to two agents, whereas the name's application token is *inferred*, covers 67 of 88, and **disagrees with the declared `domain:` on 14 of the 18 skills carrying both**.
- **Afternoon.** The reporting platform is asked to group by plugin. It does not log plugins. *"We still did not get that logging data, but I think we can start with the skill grouping."* The only grouping available is **the skill name — the axis just disqualified.**

The failure mode is that nothing announces it. Nobody re-opens the decision; the report simply gets built on whatever the substrate can group by, and every number published afterwards silently rides the rejected axis while the decision record still says otherwise. The disagreement lives on in a footnote nobody writes.

**So the axis decision has a second question attached, and it should be asked in the same breath as the first: is this axis in the telemetry, or only in the artefact?** A packaging axis that exists only in the repository layout is a documentation fact. A packaging axis that arrives in the event stream is a reportable one. If they differ, there are exactly two honest exits — get the field logged, or publish on the axis you have and state its known error rate — and choosing neither means the substrate has quietly overruled the PM.

Note the asymmetry with the ownership record above: an ownership record can be hand-maintained and ranked, because it is read at human speed. **A reporting axis cannot** — it is read per event, so it must be emitted at write time or it does not exist. That is why this one has to be fixed upstream rather than patched with a map.

## What to do

1. Decide the packaging axis on customer legibility. That is the PM call, and it is the one the platform owner will (correctly) refuse to make for you.
2. **Then check the telemetry carries it, before anything is promised on top of it.** Ask the reporting team what the event stream actually groups by. If the chosen axis is absent, that is a logging request with a lead time, not a reporting preference.
3. Then name the record that carries the other axis, explicitly, and make it enforceable. A path-based reviewer file beats a free-text metadata field, because the platform validates it and a broken entry surfaces on its own.
4. Do not let a packaging change quietly delete an ownership signal. When several source repos consolidate into one, "which repo is it in" stops discriminating — and if that was the de-facto ownership proxy, ownership becomes unknowable the day the merge lands.

## Refinement 2026-08-10 — the third exit does not exist, and taking one of the two has a shape

The telemetry corollary above named two honest exits. **Worked live on 2026-08-07 and the second one is viable, but only with a specific discipline attached.** Pedro had rooted the agent axis on the plugin (declared on 88 of 88, never forks) and Rubin then said it does not log plugins, offering the skill name — the axis the same decision had disqualified. He published on the name.

**What makes that defensible rather than a quiet capitulation is three things done together.**

1. **The rejected axis stays the record of record.** The plugin map is still the source of truth for who owns what. The name is what ships to the reporting surface. Two artefacts, one of them explicitly downstream — not a reversal of the decision.
2. **The error rate is measured and published with the number, not held in reserve.** On the 2026-08-07 catalogue the name resolved the grouping key from a clean segment on **51 of 98 rows**; 18 were inferred from loose tokens, 14 came from a *declared* field that the name contradicted, 4 from the plugin, and 11 did not resolve at all. **One skill carried the whole argument** — a governance-plugin skill whose name filed it under a different application than its three siblings. A single named misfile does more work in a room than the percentage.
3. **The logging request stays open.** Publishing on the fallback is what you do while the field lands, not instead of asking for it. The footnote is the standing reminder that the workaround has a cost.

🔑 **The general form: when the substrate cannot carry the axis you chose, publish on the axis it can carry with the disagreement rate attached, and keep the chosen axis as the record of record.** The failure mode is not choosing the fallback — it is choosing it silently, because then the substrate has made the taxonomy decision and no one can see that it did.

⚠️ **The cost is real and should be said out loud.** A footnote depends on someone reading it, and a number travels further than its caveat. This exit buys time; it does not close the gap.

## Related

[[Selection and Cross-Surface Consistency Are a PM Mandate]] · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] · [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] · [[A Single-Harness Marketplace Is Not a Cross-Harness Standard — Publish vs Find]] · [[Three-Layer AI Skill Governance Architecture (Customer-Side)]] · [[Govern a Consistency Layer Over Primitives You Don't Own]]
