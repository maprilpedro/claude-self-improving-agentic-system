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

## What to do

1. Decide the packaging axis on customer legibility. That is the PM call, and it is the one the platform owner will (correctly) refuse to make for you.
2. Then name the record that carries the other axis, explicitly, and make it enforceable. A path-based reviewer file beats a free-text metadata field, because the platform validates it and a broken entry surfaces on its own.
3. Do not let a packaging change quietly delete an ownership signal. When several source repos consolidate into one, "which repo is it in" stops discriminating — and if that was the de-facto ownership proxy, ownership becomes unknowable the day the merge lands.

## Related

[[Selection and Cross-Surface Consistency Are a PM Mandate]] · [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] · [[A Single-Harness Marketplace Is Not a Cross-Harness Standard — Publish vs Find]] · [[Three-Layer AI Skill Governance Architecture (Customer-Side)]] · [[Govern a Consistency Layer Over Primitives You Don't Own]]
