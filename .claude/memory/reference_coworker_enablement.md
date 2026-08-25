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

🔴🔑 **CORRECTED 2026-08-25 BY PEDRO — DO NOT USE THE TWO-FLAG MECHANISM TO REASSURE A CUSTOMER.** The table above describes what the *flags* can do. It does **not** describe what happens to a customer who actually moves. **Pedro, 2026-08-24, verbatim: *"un client migre sur Coworker ne peut plus utiliser AIA."*** Claude argued the opposite twice that day, reasoning from cohort 3 (AEM Cloud Service is excluded from AIA deprecation, Ken Russell 07-14 *"cohort 3 probably doesn't have a date"*) and pushed Pedro away from a true statement he had already made.

**The two objects, and they are not the same question:**

| Question | Answer |
|---|---|
| When does AEP switch AIA off for everyone? | Cohort 3. **No date.** A two-team negotiation (Ken Russell, written, 07-14). |
| What does a customer lose the day they migrate to Coworker? | **AI Assistant.** Immediately. Regardless of cohort 3. |

**Why it matters, concretely.** A customer can migrate *before* cohort 3 forces them — that is exactly what the 08-27 internal and 08-31 TBYB batches are. For them, a capability that only exists on the AIA surface (**ABAC**) is not *"not yet available"*, it is **gone, with no replacement and no date**. Any limitation note, doc paragraph or comms line that says "AI Assistant remains available" is **false for the population being migrated**, which is the only population reading it. ⚠️ **Coexistence remains technically real** (Mark Doten confirmed flag 1 without flag 2 on 07-13) — but it is a state someone must choose, not the default a migrating customer lands in. Related: [[feedback_dont_conflate_pattern_with_object]].

✅ **CONFIRMED 2026-07-13 15:39.** Asked whether flag 1 can be set without flag 2, **Mark Doten: *"Technically, yes, but that is not my decision."*** The coexistence state is real.

🔴 **AND IT OPENED A BETTER QUESTION: nobody owns the policy.** The state exists, it is **already in use** (adobe.com, AMEX), and no one has decided whether an AEM customer may run both assistants during the transition. **Practice is ahead of policy.** That decision shapes the migration experience of AEM's own customers, so AEM should hold it — Pedro took the position with Mark at 16:59 (*"coexistence is the state we need… Happy to own that position if nobody else has"*) and is awaiting his answer on who does make the call. Same shape as the parity list: an unowned decision that sets AEM's outcome, claimed rather than requested.

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

## 4. Renderers — what is gone, and what is very much alive

⚠️ **Do not say "custom renderers no longer exist."** That over-states it, and Pedro caught it. Two things are true at once.

**What Josh removed.** Joshua Hailpern, `#aem-aep-coworker-rendering` 2026-07-10 (ts `1783693457.727019`), with the qualifier that matters: *"nor do we have 'renderers' as they existed before, **with deep/complex wrokflows embeded in them**… these were removed by the coworker team when they reinvisinoed how the harness would work."* Also: *"there are no more 'direct' connections to agents."* → the **workflow-bearing, agent-connected** renderer (the `ABACDraftRenderer` shape) is gone. For those there is **nothing to port into** — it becomes a redesign, not a port, and **choosing the replacement is a DESIGN decision, not an engineering one** (Silvia + Eugene, not Sorin).

**What exists.** **ADR 001 — A2UI Renderer Extensibility** (`Adobe-dxue/coworker-ui-experience/docs/adr/001_a2ui_renderer_extensibility.md`). ⚠️ **Owner = Tim Lynn (`tlynn_adobe`), status `proposed`, dated 2026-06-09** — a proposal, not a decision, and it **predates** the harness redesign Josh describes, so **verify with Tim that the tiers still hold** before relying on it.
- **Registry-based, open contribution.** *"Adding a new renderer is open to any team — the core chat UI team is not a gatekeeper."*
- **Four tiers, in order.** ① **SVG via markdown data-URI** (the default; renders in Claude.ai, ChatGPT, Slack, email, PDF) → ② **SSR React via A2UI** (base components, or server-rendered React) → ③ **compose from existing platform renderers** → ④ **custom client renderer, last resort**, and the PR must document why the other three failed.
- **The rationale is Pedro's own argument, written by AEP:** a custom client renderer *only works in the Coworker frontend*. SVG travels everywhere.
- **🔑 The prop-schema contract is a SKILL FILE.** *"There is no machine-readable schema shared between AO and the frontend. Instead, the `visual-artifacts` skill document in `ao` is the authoritative description of each component's expected props."* + *"Without the skill entry, the LLM will not know how to construct a valid `add_artifact` call even if the type passes validation."* → **a renderer starts as a PR into AEP's `ao` repo** (type in `KNOWN_TYPES`, a validator, `prompts/references/<type>.md`), and it must land **before** the `coworker-ui-experience` PR. ⚠️ **This is NOT the manifest** — the manifest decides which skills a customer gets; this decides what the LLM may render. Same mechanism, different object ([[feedback_dont_conflate_pattern_with_object]]).

⚠️ **Retrieval note.** This ADR was already in `knowledge/ai-product/` [[A Rendering Contract Carries Structure, Not Skin]] since 2026-06-19 and was **not retrieved** when Bertrand asked about it on 07-13. **Grep the knowledge folder before fetching an architecture source.**

The three replacement paths, his words: **hybrid** (*"the coworker harness has visibility onto the page and can interact with the page that is open"* — Mithril/Hybrid-2.0), **tools and skills** (*"a conversational experience, not a point and click"*), **generative UI** (early state, "prioritized by leadership"). His preference between them is explicitly flagged as opinion.

→ Every AEM agent that built a renderer has **rework**, and it is not in the end-of-August port estimate. Same shape as the **threat-model rework** Catalin Luta raised: the migration's real cost lands as unplanned engineering in teams nobody consulted.

## 5. AEP's own contingency rule (useful, do not publish)

Lianne Ramos's cohort-1 contingency table (2026-07-08, image `F0BG059MNMC`) has a row: **"Customer has AEM → Do we revert the customer to AIA? → Yes."** So when someone asks to put an AEM customer into cohort 1, **AEP's own plan says to take them back out.** Use it in-thread, not in a status doc.

Related: [[reference_coworker_rail_access]], [[reference_aov2_marketplace_manifest]], [[reference_coworker]], [[project_aem_agents_intelligence]].
