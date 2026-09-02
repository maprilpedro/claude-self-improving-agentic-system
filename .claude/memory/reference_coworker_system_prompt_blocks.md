---
name: reference_coworker_system_prompt_blocks
description: "How Coworker carries persistent instructions — the .ao/prompts/system block system, block_dir, the three layers (blocks vs skills.preload vs hooks), and the finding that AEM has no prompt surface on the GA manifest. Read before any 'can we make Coworker behave like X' question."
metadata:
  node_type: memory
  type: reference
---

# Coworker's instruction layer — system-prompt blocks (verified in repo 2026-09-01)

**The question this answers:** "what plays the role of a CLAUDE.md in Coworker." Asked by Pedro 2026-09-01. The answer is **`.ao/prompts/system/` in `Adobe-Experience-Platform/aep-ai`**, not Business Context and not `skills.preload`.

Spec: `docs/initiatives/tracks/platform/design/system-prompt-blocks.md`. Author **Shubham Lohiya** (`slohiya_adobe`), PR #907, 2026-04-07. He also owns `services/aep-ai-runtime/src/aep_ai_runtime/prompts/` today. ⚠️ **Not in the public developer reference** — thirty pages exist under `docs/public/site/developer-reference/` including `hooks.md`, `skills.md`, `skill-monitoring.md`, and **there is no system-prompts page**. Same shape as the missing manifest-PR process doc already noted in [[reference_aov2_marketplace_manifest]].

## The mechanism

**A block is one markdown file:** YAML frontmatter (`name`, `description`, optional `conditions`) + a Jinja-capable body. `conditions` gates the whole block (`tools:` = ALL required, `any_tool:` = at least one, `runtime:` implemented but unused). Jinja handles paragraph-level variation inside a block.

**Naming is `{NN}-{block_id}.md` and the two halves do different jobs.** `NN` is sort order only. **`block_id` is the override key** — the same `block_id` in a later directory *replaces* the earlier one (and takes the child's prefix, so a child can reposition an inherited block); a new `block_id` is an *addition*, sorted by its number. Platform uses round numbers, app blocks use the gaps (`25-domain_guidance` sits between `20` and `30`).

**A manifest opts in with one key:**
```yaml
system_prompt:
  block_dir: app/aem
  disabled_blocks: []     # optional; suppresses by block_id, GLOBALLY, whatever layer contributed it
```
`block_dir` **accumulates root-first down the inheritance chain** into `block_dirs` — it does not replace. `disabled_blocks` unions. Same accumulation as `tools` (`_accumulate_system_prompt_config`).

**🔑 Composition happens at MANIFEST RESOLVE TIME, not per turn.** Result is frozen on `BaseConfig.resolved_system_prompt`; `SessionConfig.get_system_prompt()` just returns it. **Nothing is "called" at runtime.** Order: load root-first → overlay by `block_id` → sort by prefix → drop `disabled_blocks` → filter `conditions` against the *manifest's* declared tools → render Jinja → join with a blank line. Fail-fast: a missing `block_dir` raises `FileNotFoundError` before the session starts.

## The three layers — do not confuse them

| Layer | When | Carries | Cost |
|---|---|---|---|
| **`system_prompt.block_dir`** | composed once at manifest resolve | persona, boundaries, output rules | paid once, in the system message |
| **`skills.preload`** | full SKILL.md body injected as a **system reminder before every turn** | a workflow driver, so the agent advances without a trigger phrase | per turn, heavier |
| **PreTurn hooks** | per turn | genuinely dynamic facts (effective tools, user output style) | per turn |

Design decision #7 is explicit: **output style comes via hooks, not config** — the platform `tone_and_style` block already says *"Custom preferences may appear as system reminders. When present, follow those preferences."* Future Work lists a PreTurn hook for user output-style preferences. ⚠️ `context: fork` on a SKILL.md **disables preload** for it (runtime logs a warning and skips).

## Who has what (prod, read 2026-09-01)

`.ao/prompts/system/platform/` = **12 blocks**, `00-identity` → `90-output_efficiency`, inherited by everyone. ⚠️ The design doc says nine blocks on multiples of ten; the tree has twelve including `45-filesystem_layout` and `55-memory`. **Read the directory, not the doc, before picking a number.**

| block_dir | Declared by | Files |
|---|---|---|
| `app/aep` | `cx-coworker-base` (root) **and re-declared by `aem-aia`** | `00-identity`, `25-domain_guidance`, `85-output_guidance` |
| `app/aem-guides` | `aem-guides` | `00-identity`, `15-scope`, `20-content-trust`, `45-interaction` |
| `app/cx-surface-m365` | `cx-surface-m365` | `00-identity`, `25-capabilities`, `26-bot-commands`, `35-out_of_scope` |
| `app/livedemos` | `livedemos-coworker` | `00-identity`, `50-support-request-routing` |

Also present: `app/catalyze`, `app/audience-analysis`, `app/workfront`, `app/aep-esa`, `app/cx-slack-common`, `app/cx-surface-slack`, `app/cx-coworker-technical-assistant-slack`.

**`app/aep/85-output_guidance.md` in full** — it is the closest thing to the rule Pedro wants for assets:
> **Entity naming.** In responses, avoid referring to platform entities (audiences, journeys, offers, etc.) by raw ID — use the human-readable name instead. If the name isn't in your context, check if you can use your tools to look it up.

**`app/aep/00-identity.md`:** *"You are CX Enterprise Coworker, Adobe's AI coworker for customer experience teams working on **Adobe Experience Platform and related Applications**…"*

## 🔴 The AEM finding, and it is the load-bearing one

**Zero AEM manifests declare `preload`. Zero declare a `skills:` block at all.** 9 of 104 prod manifests preload something (`cx-coworker-business-adobe-com`, `-lloyds`, `-prada`, `-projects-demo`, `-newsletter`, `-wegmans`, `-dsg`, `cx-surface-m365-dsg`, `livedemos-coworker`) and none is AEM's.

**But preload was never the right lever.** The right one is `block_dir`, and **AEM has no manifest it owns that carries its GA skills.** Confirmed by Pedro 2026-09-01: the prod manifest for AEM on Coworker is **`prod/manifests/cx-coworker.yaml`**, the shared GA one — *not* `aem-aia` (that is the AI Assistant lane being deprecated, still routed via `aem-orgs-to-aem-aia`, `enabled: true`). ⚠️ **An earlier read of this repo's memory called `aem-aia` "AEM's own central manifest"; that line predates GA and is superseded.**

→ **Every AEM skill reached through the GA manifest runs under `app/aep`** — told it is a coworker for Adobe Experience Platform, with entity-naming rules written for audiences, journeys and offers. AEM has a working block directory one manifest over (`app/aem-guides`) and it cannot reach GA.

**⚠️ `aem-aia.yaml` line 126-127 re-declares `block_dir: app/aep`, which it already inherits from `cx-coworker-base`. It is a no-op line.** Kept here because it is the thing that made `aem-aia` look like the lever when it is not.

## The ask, and the sentence that carries it

**The blocker is a documented decision, #4 in the design doc, verbatim:**
> **Chosen:** Manifests declare `block_dir: app/aep` (a directory path), not a list of individual block files.
> **Why:** Directories are self-contained… The manifest just points to the directory. **This matches how skills directories work.**

🔑 **That last sentence is the whole argument. Skills arrive from plugins. Prompt blocks cannot.** `plugins.md` in the developer reference has zero mentions of prompt or instruction — a plugin ships skills, tools, MCP servers and API configs, and not one line of system prompt.

Two shapes, ranked:
1. **Let a plugin or marketplace contribute a block directory.** `block_dirs` is already a list and already accumulates; this adds one more contributor.
2. **A PreTurn hook scoped to a plugin.** Likelier to land — decision #7 and Future Work already commit to hooks for output style.

**Target: Shubham Lohiya.** He wrote the design doc, owns the `prompts/` package (commits 08-20, 08-25), **and is already listed in [[reference_aov2_marketplace_manifest]] among the observed approvers on the prod `cx-coworker.yaml` path.** Same person owns the prompt layer and approves the manifest AEM ships into.

⚠️ **Raise the collision risk yourself before they do:** `disabled_blocks` suppresses **globally by `block_id`** (decision #5), so plugin-contributed blocks on a shared manifest can be suppressed by any tenant via id collision. Namespacing them `aem_*` is the obvious mitigation and saying it first makes the ask read as engineering.

## ⚠️ One correction to carry — surface routing is NOT a thing yet

`cx-surface-m365-dsg.yaml`'s own header comment says it is *"Routed only for `request.surface == m365` AND DSG org (segment `dsg-m365-surface-orgs`)"*. **That predicate is in no routing rule.** Prod `config.yaml` routes only `segment_id` → `manifest_id`, and neither the rule nor the segment `dsg-m365-surface-orgs` exists in prod. **The comment describes intent, not a mechanism — do not cite it as an existing capability.** What *does* exist is one manifest per surface, each with its own `block_dir`, which is how m365 gets a different identity and out-of-scope block.
