---
name: reference-coworker-enablement
description: How a customer actually gets Coworker — the two Unified Shell flags (activation ≠ deprecation), the git-segment path, and the manifest→skill map that decides which skills they get.
metadata:
  type: reference
---

# Coworker enablement — the flags, the segment, the manifest

The three mechanics that decide what an AEM customer sees. Confused constantly, including at Sr Director level. Read this before answering any "can we put customer X on Coworker" question.

## 1. Two flags, and they are different objects

**Mark Doten, verbatim, `#aia_coworker_convergence` 2026-07-08 19:33 (ts `1783532019.450579`):**

> "Unified Shell has 2 feature flags:
> 1. Enable Coworker (they would need to be removed from this)
> 2. AI Kill Switch to remove AIA (they would need to be removed from this)"

| State | Enable Coworker | AI Kill Switch | Customer sees |
|---|---|---|---|
| Today, most | off | off | AI Assistant only |
| **Coexistence** | on | off | AIA **and** Coworker |
| Deprecated | on | on | Coworker only |

**→ ACTIVATION IS NOT MIGRATION.** Enabling Coworker does not remove AI Assistant. Deprecation is the second flag, and it is what cohort 3 does.

⚠️ **OPEN (asked Mark 2026-07-13, unanswered):** he named two flags; he never said they are **independently settable**. The coexistence row is an inference until he confirms. Pedro has already stated it to Bertrand, Yanira and Jaclyn in writing.

**What this settles.** Ankur Arora's *"can support be added in a staged manner?"* → **staged activation yes, staged deprecation no.** Cohort 3 is where the fallback disappears, and EH exposes every agent on one bar, so there is nowhere left to fall back to. Pedro's original "ALL agents must port before ANY AEM customer migrates" was **over-broad**; the precise version is more defensible, not less.

## 2. Entitlement ≠ Coworker access

Two objects. Both true. Bertrand has conflated them twice (2026-07-09, 2026-07-13).

**AEM agents entitlement.** Every AEM cloud (CS/AMS) licence gets the agents by default, with an opt-out. No provisioning step tied to the Agents SKU. *(Bertrand, in-thread 2026-07-09 17:08.)*

**Coworker access.** A separate gate: the org must be in a **segment in git** (`Adobe-Experience-Platform/ao`, template at `/issues`, docs `config/README.md`), then **Mark Doten flips the Unified Shell flag**. Ken Russell wrote the runbook (2026-07-08). Backups if Mark is out: Stephen Gould, Mikaela Symanovich.

**The receipt that proves they are different:** Felix Delval, 2026-07-09, on adobe.com — *"I see that they are currently not mentioned in any segment on ao."* An Adobe org, with AEM, with the agents entitled, **and invisible in Coworker**.

**The trial SKU** would retire the git step. Ken wants it; Namita asked who is building it; **nobody answered**. Ken 2026-07-09: it *"should be available in AEP Provisioning service by end of July"* and he is *"setting up time to meet with the team next week"* (2026-07-10). At ~2,600 customers, today it is one git file and one human.

⚠️ Ken's own caveat, unremarked in-thread: the runbook *"will not address enabling any additional CJA data views, or hydration of data stores etc. We are assuming these customers have that already in place with AIA."* → silent for AEM-only / net-new orgs with no AEP sandbox.

## 3. The manifest decides which skills they get

**One manifest is active per customer**, selected before the prompt, not per turn (Reasor + Satya, code-confirmed — [[reference_aov2_marketplace_manifest]]).

Skill inventory, verified 2026-07-13 from `~/GitHub/adbe-skill-audit/data/skills.json` (102 skills, 4 marketplaces):

| Marketplace | Skills | What is in it |
|---|---|---|
| `aia-extensions` (**the central AEM manifest**, `aem-aia.yaml`) | **22** | `discovery`, `quiet-hours`, `update-free-periods`, `experience-replication`, coding/fix/transpiler, program/pipeline/environment management, troubleshooters, `cloud-manager-api`. **Zero content-fragment skills.** |
| `epa` (**its own manifest**) | **18** | `multi-cf-edits`, `aem-content-update`, `content-create`, `aem-page-update`, `da-page-edit`, `publish-da`, `brand-governance`, docx/pdf brief parsers. **No `discovery`.** |
| `forms` (own marketplace `aemforms-aia-extensions`) | 2 | `forms-author`, `forms-rule-author` |
| `excat` (own nested marketplace.json) | 60 | EDS migration/import/design tooling |

**→ THE FORK.** Felix's **EPA co-innovation org list** (`ao#6444`, 2026-07-10) is *"currently mapped to the EPA Manifest."* So a customer put on that list gets the EPA skills **and not Discovery**. Apoorva wanted Coca-Cola on Coworker *for Discovery* — she would have raised the request and found out weeks later. AMEX's ask is content-fragment, so EPA is right for them and wrong for Coke.

**Nothing in the 102 skills previews content at runtime.** `preview-import` (excat) is a local EDS dev-server preview, a different object. Publish exists. Rendering what is actually delivered on a customer's own channels does not.

## 4. What no longer exists

**Custom renderers are gone.** Joshua Hailpern, `#aem-aep-coworker-rendering` 2026-07-10 (ts `1783693457.727019`): *"nor do we have 'renderers' as they existed before, with deep/complex wrokflows embeded in them… these were removed by the coworker team when they reinvisinoed how the harness would work."*

The three replacement paths, his words: **hybrid** (*"the coworker harness has visibility onto the page and can interact with the page that is open"* — Mithril/Hybrid-2.0), **tools and skills** (*"a conversational experience, not a point and click"*), **generative UI** (early state, "prioritized by leadership"). His preference between them is explicitly flagged as opinion.

→ Every AEM agent that built a renderer has **rework**, and it is not in the end-of-August port estimate. Same shape as the **threat-model rework** Catalin Luta raised: the migration's real cost lands as unplanned engineering in teams nobody consulted.

## 5. AEP's own contingency rule (useful, do not publish)

Lianne Ramos's cohort-1 contingency table (2026-07-08, image `F0BG059MNMC`) has a row: **"Customer has AEM → Do we revert the customer to AIA? → Yes."** So when someone asks to put an AEM customer into cohort 1, **AEP's own plan says to take them back out.** Use it in-thread, not in a status doc.

Related: [[reference_coworker_rail_access]], [[reference_aov2_marketplace_manifest]], [[reference_coworker]], [[project_aem_agents_intelligence]].
