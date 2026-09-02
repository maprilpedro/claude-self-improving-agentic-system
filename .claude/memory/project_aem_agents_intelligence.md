---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (currently **the 2026-09-01 session**; 07-15 → 07-27 archived to W29/W30 on 08-03, the 08-03 sweep + Agent Owners Alignment to **W32a** on 08-04, the two 08-04 blocks to **W32b** on 08-06, the **08-04 CLINT + 08-05 ROLLOUT SYNC blocks to W32 on 08-07**, the **08-05 AUDIT REPO + 08-06/07 AUDITS-WENT-PUBLIC blocks to W32 on 08-10**, and the **08-25/26 COHORT block to W35 on 09-02**) + the compact durable reference below. ⚠️ **The archiver moves dated blocks but does NOT move RESUME pointers — check the pointer still resolves after every run.** **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**
>
> ⚠️ **"moving 0 block(s)" HAS TWO CAUSES — DIAGNOSE BEFORE ACTING (2026-08-07).** (1) **The layout invariant below is broken** → the archiver cannot see the blocks. That is a bug, fix it. (2) **Every dated block is newer than `RETENTION_DAYS = 7`** → there is genuinely nothing it may move yet, which is correct behaviour on a dense week. **Check which one you are in before "fixing" anything.** On 2026-08-07 the file sat at **23.5K against a 24K read cap with every block under 7 days old**, so the only lever was **writing the blocks shorter** — the largest was a single 3.4K-token event block, trimmed to 2.2K. 🔑 **On a dense week the cap is a writing constraint, not an archiving one.** ✅ A **SessionStart hook now warns** when any session-start file approaches the cap (`scripts/archive_memory.py --check-startup`, wired in `.claude/settings.json`) — added because both prior truncation incidents were discovered by accident, never by a warning.
>
> 🔴 **LAYOUT INVARIANT, learned the hard way 2026-08-04 — DATED EVENT BLOCKS MUST SIT ABOVE THE LIVING-REFERENCE SECTIONS.** `split_active()` in the archiver treats the first non-blockquoted `## ` heading as the start of the living reference and everything after it as unmovable. This file had drifted so that four dated `> ###` blocks sat *below* `## 2026 Yearly Goal — G1`, so the archiver saw **one** block (the protected RESUME) and reported *"moving 0 block(s)"* while the file sat at **29K tokens, 5K past the read cap** — i.e. **the cap guard reported success while the file was silently truncating at session start, which is the exact 2026-06 awareness-loss failure it was built to prevent.** Fixed by reordering (content-preserving, verified line-multiset-identical), after which the same script moved 29K → 19K on the first try. **When appending a new dated block, put it directly after the RESUME, never at the end of the file.**

> ## ▶️ RESUME HERE — left off **2026-09-01** (consolidated 2026-09-02). 🔴 **AEM HAS NO PROMPT SURFACE ON THE MANIFEST THAT CARRIES ITS GA SKILLS.** 🔑 **Coworker's persistent-instruction layer is `.ao/prompts/system/` block directories, scoped per MANIFEST — and AEM's 18 GA plugins live in `cx-coworker.yaml`, which AEM does not own. So every AEM skill runs under `app/aep`, told it is an Adobe Experience Platform coworker.** The ask is written and the target is named (Shubham Lohiya). Full mechanism → [[reference_coworker_system_prompt_blocks]]. See the 2026-09-01 block directly under this; the 08-27 inventory work is the block after it.
>
> ### 🔴🔑 2026-09-01 — THE INSTRUCTION LAYER: AEM IS A TENANT WITH NO PROMPT SURFACE
>
> **📍 WHERE THIS CAME FROM.** Pedro's own use case, stated plainly: he wants Coworker to *"always display an image instead of the name and path"*, to *"behave like a CMS admin or content owner"*, and if possible **to vary by the surface the user is on**. Question behind it — what plays the role of a CLAUDE.md in Coworker. Whole session was source-reading in `Adobe-Experience-Platform/aep-ai` @ `main`.
>
> **🔑 THE ANSWER IS `system_prompt.block_dir`, NOT `preload` AND NOT BUSINESS CONTEXT.** Numbered markdown blocks under `.ao/prompts/system/`, composed **once at manifest resolve time** into a frozen string. Full mechanism, the three layers, the design decisions and the ask → **[[reference_coworker_system_prompt_blocks]]**. Do not re-derive it; it cost a session.
>
> **🔴 THE FINDING. Zero AEM manifests declare `preload`; zero declare a `skills:` block at all.** 9 of 104 prod manifests preload something and none is AEM's. **But the real problem is one level up: the composition unit is the manifest, and AEM does not own the manifest its GA skills ship in.** ✅ **Pedro's correction, and it matters** — the prod manifest for AEM on Coworker is **`prod/manifests/cx-coworker.yaml`**, the shared GA one. **Not `aem-aia`**, which is the AI Assistant lane being deprecated (still routed, `aem-orgs-to-aem-aia`, `enabled: true`). ⚠️ This repo's memory had called `aem-aia` "AEM's own central manifest" — **that line predates GA and is now superseded in [[reference_aov2_marketplace_manifest]]**.
>
> **🎯 THE ASK IS WRITTEN AND THE ARGUMENT IS THEIRS.** Design decision #4 chose directories over file lists *"because this matches how skills directories work."* **Skills arrive from plugins. Prompt blocks cannot.** `plugins.md` has zero mentions of prompt or instruction. Two shapes — (1) let a plugin/marketplace contribute a `block_dir`, (2) a PreTurn hook scoped to a plugin, which decision #7 and Future Work already commit to for output style. **Target: Shubham Lohiya** — wrote the design doc, owns `aep_ai_runtime/prompts/`, **and is already on this repo's list of observed approvers on the prod `cx-coworker.yaml` path.** 🔴 **Pedro writes it** ([[feedback_pedro_writes_claude_critiques]]); the authority sits in their own doc, which is where his asks land hardest ([[feedback_first_reply_ownership_sentence]]).
>
> **🟢 THE PROVEN AEM PRECEDENT IS ONE MANIFEST OVER, AND IT RESOLVES AN OWNERSHIP UNKNOWN.** `app/aem-guides` — 4 blocks. `00-identity.md` by **Manav Mittal** (`manavm@adobe.com`, MTS, India), PR #5113, 2026-06-22. Then `15-scope.md`, `20-content-trust.md` and a rewritten `45-interaction.md` by **Gunjan Kumar** (`gukumar@adobe.com`, **Principal Scientist**, India), PR #7486, 2026-07-22, titled *"add prompt-layer guardrails for tagging assistant"*. 🔑 **The pattern is the split: one person ships the assistant with an identity, a specialist comes back a month later and adds the guardrail layer.** Gunjan also posted the `dalp-workflow` roundup 08-29 including a `skill-compactor` skill for SKILL.md and CLAUDE.md — he builds on this layer. ✅ **This closes the `aem-guides-extensions` ownership row that [[reference_aov2_marketplace_manifest]] carried as `unknown`.**
>
> **📦 THE TWO PROD MANIFESTS, and the delta is one skill.** `cx-coworker.yaml` (GA, shared) = **18** `aem-aia-extensions` plugins. `aem-cx-coworker.yaml` = **"AEM Bug Bash Coworker"**, 19 plugins, **a temporary copy sitting in prod** by its own header comment, routed to segments `aem-bug-bash` and `ohio-hands-on-labs-orgs`. **The only difference is `aem-pipeline-troubleshooter`** — excluded from GA, live in the bug bash, and one of the three `IMS + PAT` skills that write to a customer's git repo. Carsten's onboarding commit is **PR #11524, 08-27**; he pinned versions 08-31 (#12439) and **un-pinned them 09-01 (#12431)**, two days later, eight days after GA. Nobody has said why.
>
> **🔎 AND IT PROBABLY CLOSES THE 08-27 SCOPE QUESTION.** The prod `aem-aia-extensions` marketplace policy carries `exclude: ["aem-edge-dispatcher", "aem-workflow-ops", "aem-workflow-api", "experience-replication", "aem-replication", "aem-platform-codeveloper", "aem-pipeline-troubleshooter", "*-dev", "*-stage", "*-beta"]`. **Three of the five "missing families" from the Showcase-file comparison are named there** — Dispatcher, Workflow, Replication. And the bug bash manifest installs **19** plugins against the Showcase file's **19** skills. 🔑 **Hypothesis, not conclusion: the Showcase CSV is an extract of what the bug-bash manifest actually installs, not a rival inventory.** Content Supply Chain and Asset Sourcing are not in the exclude list — they are simply not in `aem-aia-extensions`. **Checkable in one name comparison.**
>
> **⚠️ MY OWN OVER-CLAIM, CORRECTED IN-SESSION AND WORTH THE HABIT.** `cx-surface-m365-dsg.yaml`'s header says it is routed on `request.surface == m365`. **That predicate is in no routing rule** — prod routes `segment_id` → `manifest_id` only, and the named segment does not exist. A comment describing intent was read as a mechanism. [[feedback_separate_facts_from_proposals]], [[feedback_audit_outward_artifacts]].
>
> **🔧 THE PANEL FLAG, asked for and found.** `?shell_aiChatEnabled=true`, appended **after `/ui`, not in the hash** → `adobeaemcloud.com/ui?shell_aiChatEnabled=true`. Apoorva asked Corey + Pedro in `#aem-agentic-owners-alignement` 08-24 18:13; **Corey gave the pointer, Mark Doten gave the parameter** and corrected her when she put it in the hash. Banked in [[reference_coworker_rail_access]]. Mark Doten's frame, same thread: *"if an org has Coworker, the rail is not accessible because the Coworker rail is not available yet… there are select applications that have the button enabled, but those show a popover."*
>
> **🛡️ BUSINESS CONTEXT + GUARDRAILS — a live design debate nobody from AEM is in.** **Danny Miller** loaded **50+ Adobe guardrails** into Business Context under `Policies and Rules` (08-27) and Coworker enforced one at generation time, verbatim: *"⚠️ Guardrail violation (N-1020): This sandbox already has 1,870 streaming audiences, well over the org limit of 500… Per your guardrail policy, I need your go-ahead."* **A guardrail = an Adobe-published operational limit with an ID, a threshold and a stated technical consequence**, sourced from the Health Check service list. **Zan Chu asked for the raw Excel on 08-27 and never got it.** **Yunyao Li** asked whether guardrails apply to all customers by default or pick-and-choose; Danny: available to all, editable, **a copy per customer** — and *"I don't like forcing spend on a customer w/o ability for them to control it"*, because pre-checking costs tokens. Routed to Patricia Yu + Eden Wen for the admin UI. Tickets: `CXCW-75` (open, business context named as the answer), `PLAT-278380` (**unassigned**), `AEPAPPS-1493`. 🔴 **All of it is AEP. No AEM guardrail list exists that I could find** — so AEM skills can act but cannot prevent, which is the 08-27 "nothing is measured" finding seen from the other end.
>
> **🔎 KNOWLEDGE (P6):** applied — [[Govern a Consistency Layer Over Primitives You Don't Own]] (the cleanest instance yet: AEM must govern behaviour of skills running inside a manifest it does not own) · [[Selection and Cross-Surface Consistency Are a PM Mandate]] · [[An Undefined Gate Is a Date Nobody Can Give]] (the bug-bash copy in prod with no removal date) · [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]] · [[feedback_separate_facts_from_proposals]]. **No new entry and no new park — see the consolidation note.**
>
> ### 🔴🔑 2026-08-27 — THE SECOND INVENTORY FILE, THE FIVE MISSING FAMILIES, AND FOUR CORRECTED COUNTS
>
> **📍 THE TWO SOURCES.** (a) `~/Downloads/table (3).csv` — and ⚠️ **`table (4).csv` is byte-identical to it, `cmp` reports no difference. A re-download, not a new extract.** 93 data rows. (b) `~/Downloads/20260827 - AEM-related skills, APIs, and MCP servers available AEM Showcase.csv`, **27 data rows**, same 11-column template with two headers renamed (`Use Case` → `Supported Use Case`, `Mon. Source` → `Monitoring Source`).
>
> **🔴 THE SCOPE IS THE WHOLE QUESTION AND IT IS UNCONFIRMED.** The 08-27 file's own title says **`available AEM Showcase`**; `table (3)` carries no scope label at all. **The most likely reading is catalogue versus what is actually provisioned in the Showcase org, and that is an inference from a filename, not a confirmation.** ⏳ **Ask whoever produced it.** Until then no skill count is safe to quote, because Pedro now has four numbers in circulation for one question — **85, 62, 60, 19**.
>
> **✅ FOUR CORRECTIONS TO THE 08-27 MORNING READ, all applied in place in the block below.** 92 rows → **93**. 84 skills → **85** (the type breakdown always summed to 85; the total was the error). ~59 user-reachable → **60** (85 minus 25 rows at Access Point `Internal`). Seven `Skill (API Ref)` → **8**, the eighth being `aem-cloudmanager-releases-access`, never named. ⚠️ **All four had already reached `watches.md` and one of them was on its way to Bertrand.** 🔑 **The lesson is narrow and mechanical: a count read off a source in one pass is a claim, not a fact — count it before it enters the registry or an outward artifact** ([[feedback_audit_outward_artifacts]]).
>
> **🔴 FIVE WHOLE FAMILIES ARE IN THE CATALOGUE AND ABSENT FROM THE SHOWCASE FILE** (zero string matches, checked both directions). **AEM Dispatcher — 8 skills**, the second-largest owner team, an orchestrator plus seven subs · **Content Supply Chain** — 2 skills plus the `csca__*` MCP · **AEM Workflow** — `aem-content-workflow-access`, `aem-content-workflow-inspect` · **Asset Sourcing** — `asset-sourcing-admin` plus its **76-tool** MCP · **AEM Replication** — `experience-replication`. ⚠️ **The first pass at this comparison named four and missed Dispatcher.**
>
> **🟢 AND TWO SKILLS EXIST ONLY IN THE SHOWCASE FILE** — `aem-sites-figma-read` and `aem-sites-visualcontentfragments-create`, both AEM Sites, both Figma-to-VCF. 🔑 **A 27-row file containing two items absent from a 93-row file is the proof that these are not two photographs of one inventory.** Plus a third, `update-profile-api`, which is `aem-cloudmanager-releases-access` under another name.
>
> **⚠️ THE TWO FILES CONTRADICT EACH OTHER ON WHETHER MCP USAGE IS MEASURED.** `table (3)`: the 8 servers carry `Usage Metrics: yes`, `Alerting: partial`, source **`Platform telemetry`**. The Showcase file: the 5 servers carry `Usage Metrics: No`, `Alerting: No`, source **`MCP connection health check`** — which is liveness, not usage. **On all 27 Showcase rows `Usage Metrics` and `Alerting` are `No`.** 🔑 **The only usage-shaped object in either file is `Progress log (aem-onboarding-progress)` on `aem-onboarding-workflow`, built by one team for itself. That is the pattern to generalise and it is directly Pedro's lane.**
>
> **🛠️ FIVE RATIONALISATION PATHS, ranked cheapest first, all read off the Showcase file.**
> 1. **Demote the API-reference layer — the only one Pedro can decide alone.** Its 7 `Skill (API ref)` rows describe **4 backends** (`aem`, `aem_discovery`, Cloud Manager, `bps-il-admin-console`) and **only 3 are declared as `API Service`** — `bps-il-admin-console` has a service but no row, and `update-profile-api` calls `api_request` without naming a service at all. **Doing it takes the Showcase skill count 19 → 12 with no capability removed.** Manas's 07-16 tiered-documentation point arriving as data.
> 2. **Merge `AEM MCP` and `OneAEM MCP`.** 14 tools each in this file (17 each in the catalogue), near-identical use-case text, the only stated difference being `code-mode org` — a deployment parameter, not a product. ⚠️ **Post-GA: Carsten's 08-19 freeze explicitly held off moving other MCPs under One AEM MCP.**
> 3. **Fold `aem-sites-figma-read` into `aem-sites-visualcontentfragments-create`** — it is a step of it and nothing else consumes it. 12 → 11.
> 4. **Decide the skill-versus-MCP duplication.** ⚠️ **The list is not the same in the two files.** Catalogue: **five families** (Brand Governance · Permissions Governance · Content Supply Chain · Document Authoring · Asset Sourcing). Showcase: **three pairs** (`experience-governance` 11 subs vs Governance MCP 22 tools · `experience-generation` 15 subs vs Experience Generation Content MCP 18 tools · the DA half vs DA MCP 13 tools), because two families are absent and Brand plus Permissions Governance are merged into one `Governance MCP`. **This is the pricing and portability decision, not a cleanup — Bertrand holds the question, Pedro holds the evidence, and he must say which file he is quoting.**
> 5. **Generalise the onboarding progress log** as the observability pattern, starting with the three catalogue skills carrying `IMS + PAT`, the only three that write to a customer's git repo.
>
> **📐 CUMULATIVE EFFECT of 1, 2 and 3 on the Showcase inventory: 19 skills → 11, 5 MCP → 4, 3 API Services → 4 declared, 27 rows → 19.** Nothing removed.
>
> **⚠️ NAMING — one alignment conversation, not five renames.** `adaptive-forms-authoring`, `experience-generation`, `experience-governance`, `update-profile-api` and `bps-il-admin-console` break `aem-<application>-<feature>-<action>`, and `aem-cloud-manager-ops` spells `cloud-manager` where `aem-cloudmanager-api` spells `cloudmanager`.
>
> **⚠️ WHAT COULD NOT BE COMPARED.** The Showcase file collapses 7 families into `(N sub-skills)` without naming the subs, and its counts run **below** the matching catalogue items — governance 11 against 15, generation 15 against 17, onboarding 8 against 9. **So roughly 6 more items are probably missing inside those families and the file does not name them.** The three likely Assets orphans are `metadata-advisory`, `search-indexing` and `environment-provisioning`, but that is inference from use-case text, not a name match.
>
> **🔎 KNOWLEDGE (P6):** applied — [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]] (a second, cleaner instance: the API-reference layer is not a build unit at all, and the file cannot decide whether a backend is a skill, a service or both) · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (four live numbers for one question, and the honest answer names the scope before the figure) · [[feedback_dont_conflate_pattern_with_object]] (two files describing the same estate are not versions of each other until you prove it) · [[feedback_audit_outward_artifacts]]. **No new entry and no new park — see the consolidation note.**
>
>
> ### 📊🔑 2026-08-26/27 — THE SKILL + MCP INVENTORY, AND THE OBSERVABILITY COLUMN IS EMPTY
>
> **📍 THE SOURCE.** `~/Downloads/table (3).csv`, 93 data rows (⚠️ **corrected 2026-08-31 — the first read said 92**), columns `Item Name · Type · Owner Team · Access Point · Use Case · Env · Auth Method · Monitoring · Mon. Source · Usage Metrics · Alerting`. ⚠️ **A point-in-time extract, not a live artifact — the estate moves weekly, so re-pull before quoting any of these counts.** Read 2026-08-27.
>
> **THE SHAPE: 85 skills + 8 MCP servers across 14+ owner teams.** (⚠️ **corrected 2026-08-31 from 84** — the type breakdown below always summed to 85; the total was the error.) Type split: **50 `Skill` · 23 `Skill (Sub)` · 8 `Skill (API Ref)` · 2 `Skill (Orchestrator)` · 1 `Skill (Router)` · 1 `Skill (Internal)`.** 🔑 **Only 60 are reachable by a user** (⚠️ **corrected 2026-08-31 from ~59** — 85 minus the 25 rows at Access Point `Internal`, which are the 23 subs plus `aem-sites-contentfragments-detect-duplicates` and `aem-sites-brand-guidelines-check-text`) — the 23 subs carry Access Point `Internal` and are invoked by orchestrators, never selected directly. **That is the honest denominator when someone asks what a customer can reach**, against the `62 AEM skills` in the GA announcement and the 11 visible in prod. Owner concentration: AEM Sites 13 · Cloud Manager 11 · AEM Assets 11 · AEM Dispatcher 8 · Sites/CF 6.
>
> **🔴 FINDING 1 — NOTHING IS MEASURED. All 85 skills carry `Monitoring: no`, `Mon. Source: -`, `Usage Metrics: no`, `Alerting: no`.** Not most. All. The 8 MCP servers carry `partial`, sourced from `Platform telemetry` — and ⚠️ **read the full row, added 2026-08-31: they also carry `Usage Metrics: yes` and `Alerting: partial`.** So the honest line is not "nothing is measured", it is **the skills are not measured and the MCP servers are**. **No skill is observable, therefore no skill is reportable** — which is the structural reason skill-level reporting keeps failing, now visible as one uniform column rather than an argument. Directly Pedro's lane.
>
> **🔑 FINDING 2 — FIVE CAPABILITIES SHIP TWICE, AND THIS IS BERTRAND'S OPEN QUESTION.** Brand Governance (5 skills + `governance__bga_*`) · Permissions Governance (2 skills + `governance__pga_*`) · Content Supply Chain (2 skills + `csca__*`) · Document Authoring (2 skills + 11 CRUD tools) · Asset Sourcing (1 skill + 76 tools). **Bertrand, `#aem-agent-owners-alignement` 2026-08-25 12:48, verbatim:** *"if we keep the oneAEM MCP server to barebone tools, without duplicating the skills, then we make the coworker MCP much more interesting and 'valuable' - generating value to customers and to Adobe (revenue)… the question is whether, by artificially augmenting the role of tools, we are not shooting ourselves in the foot (business wise, not technically)."* And 08-24 19:32: *"if our coworker skills are pointing at MCP tools, then they should work 'as is'… But if they are pointing at APIs, then they will only work in Coworker (eg. the assets-discovery skill)."* → **The duplication is a pricing and portability decision, not a hygiene bug. Pedro holds the five named families; Bertrand holds the question. That is the move.**
>
> **⚠️ FINDING 3 — `AEM MCP` AND `OneAEM MCP` OVERLAP HEAD-ON.** 17 tools each, both covering environments and read/write/delete, under **different owner teams** (AEM Platform vs AEM Sites/CF). Post-GA, not GA — Carsten's 08-19 freeze decision explicitly held off moving other MCPs under One AEM MCP.
>
> **🟢 FINDING 4 — EIGHT "SKILLS" ARE DOCUMENTATION.** (⚠️ **corrected 2026-08-31 from seven** — `aem-cloudmanager-releases-access` was never named.) `aem-cloudmanager-api` (112 endpoints) · `aem-open-api` · `aem-r-api` · `aem-sling-api` · `aem-repository-discovery-api` · `aem-content-workflow-access` · `bps-il-admin-console` · `aem-cloudmanager-releases-access`. All typed `Skill (API Ref)`. **This is Manas's 07-16 point arriving as data** — *"everything doesn't have to be modeled as a skill; a lot of it can be tiered documentation"* — and reclassifying them is the cheapest cleanup available while also fixing the denominator.
>
> **🟢 FINDING 5 — TWO TEAMS BUILT THE SAME PATTERN SEPARATELY.** Dispatcher = 1 orchestrator + 7 subs; Cloud Manager pipeline troubleshooting = 1 orchestrator + 6 subs. Identical shape, an orchestrator routing to a per-step failure investigator. One shared pattern would serve both.
>
> **Smaller, all actionable.** (a) **Six skills read a brief out of a document** (`docx-parse`, `docx-read-text`, `docx-export`, `docx-extract-annotations`, `brief-docx-highlight`, `pdf-parse`) — and the estate already has the right answer next door in `aem-sites-content-update`, a Router that classifies and dispatches. (b) **18 names break `aem-<application>-<feature>-<action>` and they cluster by team, not at random** — Brand Governance, Enterprise Context and Content Supply Chain all use verb-first (`discover-brands`, `evaluate-page-against-brand`, `view-brand-checks`, `manage-enterprise-context-rules`). **One alignment conversation, not eighteen renames.** Two names also mix `_` and `-` inside (`aem-assets-metadata_form-onboarding`, `aem-assets-search_filter-onboarding`). (c) 🔴 **Three skills carry `IMS + PAT` and they are the only three that write to a customer's git repo** — `aem-cloudmanager-pipeline-troubleshooting`, `aem-cloudmanager-pipeline-fix-applier`, `aem-edge-dispatcher-fixing`; two mention "revoke PAT" in their own use case. **They are also unmonitored. That is the audit line.**
>
> **🕳️ THE GAP VISIBLE BY ABSENCE.** No skill covers **delete, cleanup or rollback**, and workflow support is read-only (`aem-content-workflow-inspect`, no execute path). **Matches `AEMAGT-2581`**, the only cross-agent finding of the bug bash, still filed `Normal` and unassigned.
>
> **📤 An English rationalisation report was produced in-chat** (inventory shape, the five findings ranked, the smaller items, and a six-step suggested order). Not sent anywhere.
>
> **🔧 ADMIN CONSOLE, small but it cost time.** `AEM Agents on Coworker - GA Bug Bash - Authors` is an **Admin Console User Group**, not a product profile and not an AEM-side group — which is why it is invisible if you look under Product Profiles. **Path: adminconsole.adobe.com → check the org switcher is on AEM Showcase → Users → User groups.** Direct: `https://adminconsole.adobe.com/38931D6666E3ECDA0A495E80@AdobeOrg/users/groups`. **Created by Yanira 2026-08-15**, and her own caveat still stands unless someone changed it: *"I did not add any author roles b/c I don't know what program we will be using, what environment, what AEM Role"* — **she added only the CM Developer role.** Latest add: Yanira to Gerald Prendi, 2026-08-26 14:31, group DM `C0BSY04G1LL`.
>
> **🔎 KNOWLEDGE (P6):** applied — [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]] (the API-ref demotion and the skill-vs-MCP duplication are both the build-unit question resurfacing) · [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] (18 naming exceptions clustering by owner team, not at random) · [[Selection and Cross-Surface Consistency Are a PM Mandate]] · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (~59 user-reachable is the honest denominator against 62 and 84). **No new entry — see the consolidation note.**
>
## 2026 Yearly Goal — G1

**G1 — Agent Intelligence & Reporting:** Build and own the agent intelligence layer that gives every AEM agent PM a clear view of what customers need, where agents fall short, and where they create measurable value. Drive improvement in Technical Success Rate and Value Realization across the AEM agent portfolio.

Canonical full doc: `2026/Experience Hub/AEM Experience Hub - Project Folder/AEM EH - Key Files/Experience Hub - 2026 Yearly Review Goals.md` (covers G1+G2+G3 — leave canonical, cross-link).

---

## Agent taxonomy

**Pedro's reporting scope (6 agents):** experience_governance_agent, governance_agent, aem_experience_development_agent (EDA), aem_experience_production_agent (EPA), discovery_agent, content_optimization_agent.

**experimentation_agent OUT** (decision April 16, 2026). Rationale: not in the AEM agent intelligence narrative for Loni. Don't pull into reports / validation / Bertrand+Loni+JM updates.

**Rubin tagging list (7 agents — broader than Pedro's reporting):** above 6 + experimentation_agent. Locked with Karthik Penikalapati April 16.

**Agent owners (AEM):**

| Agent | Owner |
|---|---|
| Experience Production (EPA) | Corey Dulimba |
| Governance | Philippe Kapfer (PM) — devs Alejandro Ramirez Cheves, Cornel Isbiceanu |
| Discovery | Apoorva Gupta |
| Content Optimization | Greg Klebus |
| Development / EDA | Brian Chaikelson |
| Onboarding | Nick Whittenburg (out of Pedro's 6) |
| Modernization | Gabriel Walt / Mike Tilburg (out of Pedro's 6 — but funded under AEMAGT-538) |

Site Advisory Agent (AEMAGT-2, Laurentiu Odoleanu PM, Remus Stratulat ENG) is customer-facing, integrated with Brand Concierge, runs on Content AI — NOT in Pedro's 6. Reference page at `2026/AEM Agents Intelligence/AAI - Project Folder/Site Advisory Agent (AEMAGT-2).md` (move target Phase 2).

---

## Three-tier reporting architecture (locked May 1, 2026)

**Tier 1 — QBR.** PMM-led (Tina Nicu / Akin / Vaishnav Gorur). Quarterly. Senior leadership audience. Reference: `/Users/pedrofer/Downloads/AEM Agents QBR_Feb2026_SP.pdf`.

**Tier 2 — Portfolio Monthly Briefing.** Pedro-led. Monthly. Senior management audience. AEM-only. v0 shipped April 30, 2026 at `https://main--aem-agent-reports--aem-epa.aem.page/reports/portfolio/2026-04/briefing`. 4 of 6 sections substantive (Executive Summary, MAU per agent 6-month line, Retention 71.6% EPA / 71.5% Discovery monthly orgs, Reach 767 active orgs / 59.7% cross-agent). Quality WIP banner. Sections 5-6 placeholder pending Indicator #8 (May 17). Spec at `aem-agent-data/PORTFOLIO-MONTHLY-BRIEFING-SPEC.md`.

**Tier 3 — per-agent reports (Felix).** Weekly. Agent PM audience. EPA pipeline LIVE.

Bertrand named the architecture. Pedro owns Tier 2. Yanira QBR ownership ask sits in Tier 1.

**✅ 2026-07-24 — THE WEEKLY KR STATUS SHIPPED (KR 1e "Aggregate Value Realized", OKR-review format).** Final content: Agents (665 orgs −2.3% / 1,668 users +2.1% / returning 90 / cross-agent 49.8% +3.5pp, trailing-4w basis; headline "The Summit spike is behind us", retention bullet chart-backed only), MCP (new-data-source flag + 1.6M requests / 96k tool calls 70% specific / 1,202 orgs / top customers incl. Eli Lilly value profile + the closing line "Requests show traffic. Specific tool calls show what customers really do - that is the number we will report from now on" = the cycle-1 plant of [[migrate-leadership-from-a-volume-metric-to-a-value-metric-without-a-cliff]]), Experience Modernization (1,522 +13% MoM / 658 +12% / 27,094 pages +31% / partners 81/10 stable — W30 window; ⚠️ the dashboard had silently stayed on Jun 15–21, caught before reporting). **Playground section dropped from this cycle's status** (single-org instrument view; full-view numbers not pulled). KR sheet context: Q2 VR 19.5% At Risk, Q3 28.5% On Watch. Session pattern: every headline number today (MCP ÷35, 847-vs-539, playground "failure", Modernization stale window, my own −19%) was a measurement artifact until scope/window/basis was pinned — including one I produced myself (the −19% cross-basis diff, corrected same evening).

**Agentic Playground = AEM Sites Trial (confirmed by Gilles, 06-24 DM, "Oui").** The aem.now playground runs on the single `aemsitestrial` tenant, so the playground usage dashboard showing **"External Orgs: 1"** is BY DESIGN, not a classification bug. That dashboard is **Pedro's own `aem-agent-reports` program report** (`.../reports/programs/aem-sites-trial/...`) — Felix Delval built it, Pedro added the Value Realization level (04-23 `#franklin-crosswalk-playground`). ⚠️ Its auto-generated "Executive Summary" (*"critical failure mode… no real customer validation"*) is a **miscadrage** — a playground is not a customer-adoption metric; do not paste it into a KR status. Report the playground from the **same instrument as the 6/24 status** (the full-playground view with the Customers/Partners/Adobe/Personal split), never the external-only single-org cut. **Meta-finding (2026-07-24 KR-update session):** three reporting instruments in one day (MCP clean-start, agents 847-vs-539, playground single-org) each produced a misleading headline until scope/window/classification were pinned — the measurement layer needs hardening before any number headlines. Ties [[H-009]]. Retention finding banked in [[project_checkin_2026]] (orgs return 41-65%, users only 12-27%, bigger agent worse *user*-retention).

---

## Felix reports + report pipeline

> **Moved to `project_aem_agents_intelligence_ARCHIVE_INDEX.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

## Apoorva validation punch-list (KR1) — 📕 CLOSED 2026-08-11, Pedro's call

> ✅ **"oublie" — Pedro, 2026-08-11.** Closed deliberately and **not** verified item by item. Opened at the April 16 meeting (Apoorva Gupta + Ankur Arora + Varun Kalra) against the Discovery Agent report; its lane has since been overtaken by the Coworker migration and the Rubin/definition port, and Bertrand's Q2 response already says G1's work *"needs to be… redone for a large part given the move to Coworker."* **Do not re-raise it at the next System Review.**
>
> **Tombstone, so the shape is not lost:** 8 items — (1) 50-60% data gap vs Grafana ✅ closed April 22 by Varun · (2) TSR counting "no result found" as success · (3) tag classification bleeding across agents · (4) First Useful Result Rate missing · (5) content-type breakdown for Discovery · (6) aggregated-metrics transparency · (7) promo SKU + TBYB credit utilization view · (8) calculation-logic documentation per metric. **Full text in git history** (`git log -S "Apoorva validation punch-list" -- .claude/memory/`).
>
> 🔑 **Two things worth carrying forward, because they outlived the list.** The **"no results found" reframe** (a product gap, not a legitimate answer) is banked in `knowledge/` and still true. And the attribution line — say *"Apoorva's team stress-tested and found gaps"*, **never "Apoorva validated"** — still applies to any report she has reviewed.

---

## Rubin — CXO-wide AI Assistant Usage Dashboard

**Owner:** Angela Han (Sr Data Scientist Manager, Customer Engineering, San Jose). NOT in AEP PM chain — Data Science / Engineering. URL: https://rubin.adobe.io/dashboard/login

**Source confirmed April 16 (Karthik):** AEP AO chats DB. Different pipeline from Felix but same AEP infrastructure neighborhood. *"We are ingesting all the AI prompt / response events, so regardless of their origin, if they touch AEP AO -> we should have it in Rubin."* Contradicts Silvia's earlier "EH entry only" framing — Rubin is platform-wide, not EH-scoped.

**The inversion — Rubin needs something AEM has:** AEP provisioning API doesn't return org status (COMMERCIAL, NFR) for AEM-only orgs. Rubin can't cleanly count commercial AEM users. Felix has a local Prod orgs list. Karthik wants this scaled into AEP provisioning. **Felix's artifact = cross-org leverage.** Pedro's move: own the contribution, position AEM as the team that closes an AEP gap. Senior Director-level cross-org contribution.

**Contacts:**
- **Angela Han** — Rubin owner. Reports Richard Maraschi → Shivakumar Vaithyanathan (VP Platform Eng).
- **Karthik Penikalapati** — Rubin tech lead. Reports to Angela.
- **Silvia Mulet Ferre** — Sr Product Design Manager, Adobe Design (Austin). Eugene Bannykh's manager. Chain: Guliz Sicotte → Archana Thiagarajan → Eric Snowden → David Wadhwani.
- **Uma Subbu** — Sr Product Designer, Adobe Design (Chicago). Reports to Silvia. Co-investigating AEM AI Assistant + Agent usage with Felix's report + Rubin. UX hypotheses + UX Suggestions.

---

## AO 2.0 strategy + AEM-AO liaison

> **Moved to `project_aem_agents_intelligence_ARCHIVE_INDEX.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

## Priority Consolidation View (KR4)

Draft saved April 24 at `AAI - Project Folder/Agent Reports/20260424 - Priority Consolidation View.md` (Phase 2 move target). Answers Loni's April 13 unanswered question (*"what % of top requests are making it into the agent"*).

Structure:
1. Answer to the Question
2. Top 10 Gap Categories table (classified measurement / product gap / value realization, with status + owner + ETA)
3. Closure Mechanism (Governance Agent AEMAGT-1240 as proof point)
4. What's New Since March (intent-level measurement, "no results found" as product gap, capability-level monthly usage as adoption narrative, voluntary platform consolidation)
5. What We'd Want Next (3 asks)
6. What This Is Not

Volumes + unowned routing pending Apoorva validation close. KR4 ship date moved May 1 → May 8.

---

## Stakeholder shortlist (AAI lane)

**AEM Agent PMs:** Apoorva Gupta (Discovery), Corey Dulimba (EPA), Philippe Kapfer (Governance), Greg Klebus (Content Optimization), Brian Chaikelson (EDA), Nick Whittenburg (Onboarding), Gabriel Walt / Mike Tilburg (Modernization).

**Agent PgMs:** Yanira Castaneda (AAI counterpart), Pritie Sharda, Robert Guthrie, Marius Duta, Amit Arora, Prashant, Georgeta Vladescu-Viezure, Juliana Campbell.

**AO / AEP:** Conrad Woltge (Sr Principal Architect), **Trent Davies** (`W4SGEQF46`, `tdavies@adobe.com`, Denver) — ⚠️ `correct:` 2026-08-20, **NOT "eng, AO"**. He is **Sr. Principal Architect, Experience Cloud**, and his role in the GA is specific: he owns the interpretation of *"all MCP servers must be behind the Coworker Gateway and pass the ARB review"* and therefore **grants the exception**. Christian Meyer routed it to him via Carsten on 08-18 13:41. **He is the authority Pedro's "agreement to go GA with reviews open" rests on** — Ken Russell (eng, AO), Sergey Generalov (PM, AO), Ian Boston (compliance), Manas Garg (AOv2 dev experience).

**Data / Reporting:** Felix Delval (data eng, EPA pipeline), Lara (taxonomy + Governance), Varun Kalra (Discovery validator, Apoorva's team), Karthik Penikalapati (Rubin tech lead), Angela Han (Rubin owner).

**🆕 Rollout data + comms (added 2026-08-21, both were missing and both own something Pedro's GA depends on):**
- **Paul Midura** — `pmidura@adobe.com`, `W4RPRDFFV`. **Owner of the cross-solution activation list (AEP + AEM + Workfront)** and therefore of column G `Non-Migration Reason` in the cohorts workbook. Pedro owns column F. DM `D0B2SLATWUX`; working group DM with Tina `C0BR07R1BJ8`. ⚠️ **Not to be confused with Paul Pop** (`pop@adobe.com`, eng, flagged the broken gateway tools on 08-10).
- **Huong Vu** — `huongv@adobe.com`, `U053CPN2XLH`, Senior PMM under Akin Ajayi. **Owns the Gainsight + admin-email machine for the Coworker rollout.** Operators: **Serah Metpalli**, **Young Ah Bang**; **Sonia Espejo Butler** for Workfront. Channel `#cx-coworker-trial-rollout-core` `C0ABFLYLZK7`.
- **Trent Davies** — see AO / AEP above. Sr. Principal Architect, Experience Cloud; grants the Gateway/ARB exception.

**Design (Adobe Design lane):** Silvia Mulet Ferre (Eugene's manager), Uma Subbu.

**Leadership:** Loni Stark (VP AEM & Commerce), Jean-Michel Pittet (VP Eng AEM), Jaclyn Eckersley (FinOps, AEM Eng VP-side), Bertrand de Coatpont (Sr Director PM, manager), Shankari Panchapakesan (Group PM, transitional).

**PMM:** Tina Nicu, **Tina Ngo** (Principal PMM, AEM agents GTM + customer-trial pitches — added NYL + State Street to a TBYB cohort 05-27 w/ Namita Krishnan; pricing/packaging angle. **DM'd Pedro 07-07 22:12 + 07-08 pre-attributing the coworker-migration lane** — "i hear you're leading the efforts for coworker migration across all aem agents… is there a standard weekly meeting you own"; Pedro pointed her to GA canvas F0BD4RALNHF. = comms-lane PMM counterpart to Akin, natural fold-in for the weekly / comms-plan. ⚠️ **NOT Tina Nicu** — two Tinas in PMM. `tinan@adobe.com`, U0284AYUX99), Akin (PMM for AEM survey + TBYB comms owner), Vaishnav Gorur (new PMM AEM agents — pending confirm Wed May 6), Haresh Kumar (chain to Vaishnav).

**Cross-VP peer (Sunil Menon tree):** Cole Connelly (Principal PM, Prompt Library Platform). Tim Lott → Daniel Sheinberg → Sunil Menon (peer to Loni at VP level under Amit Ahuja). Strategic backstop = Stephen Gould.

**Special:** Jim Stoklosa (dual — EH for Experimentation surface, AAI as report contributor for EPA).

---

## Interpersonal — Philippe Kapfer (competitor frame)

Senior PM under Bertrand. Scope: Governance Agent + Security. Arrived 2 years after Pedro. Took security perimeter from Pedro. **Potential promotion competitor — actively building Loni visibility** (Governance Agent / Enterprise Context getting named in Loni meetings, backed by Michael Marth).

**Pattern (April 2):** agreed privately on report-to-JIRA filtering, then pushed back on the same point once Bertrand was on the email thread. Pedro retracted publicly — bad move. **Tactic:** agree 1:1, create dissent in front of the boss.

**Pattern to break:** hold position under public pressure, don't retract. Recovery: reintroduce tracking concern at implementation as technical requirement, not debate. Stop using Philippe as first go-to for new trials (report-to-JIRA, new report sections) — use **Corey Dulimba** as first testeur instead. Giving Philippe early access to unpolished work hands him weak points.

**Second pattern (April 2):** uses Pedro as real-time mirror — gets Pedro to validate his positioning in side-chat during a Loni meeting. Pedro said *"very much on dirait hein cool!"* on governance/enterprise context, Philippe closed with *"C'est gentil mon loulou."* Pedro became active supporter without realising. He doesn't attack — he makes you applaud him.

Per Pedro's own framing: *"friends obsessed with girls will drop you for whatever is good for them in the moment."* Treat as colleague, not ally. Treat as competitor.

---

## Pedro's session-named development gap (May 1 self-diagnosis)

*"i have a bias for delivery and poor communication skills strategically."*

**Reframe:** broadcast frequency, not skill issue. May 1 night Slack to Bertrand was first rep on the muscle. Stack 3 reps a day for a month and the diagnosis stops being true.

---

## Status & Todo files (Obsidian)

**AAI canonical (post Phase 1 — 2026-05-03):** `2026/AEM Agents Intelligence/AAI - Project Folder/Status and Roadmap/AEM Agents Intelligence - Status and Todo.md`

**EH:** `2026/Experience Hub/AEM Experience Hub - Project Folder/AEM EH Status and Roadmap/EH - Status and Todo.md`

**Old `AI-Assistant - Status and Todo.md`** — DEPRECATED 2026-05-03, banner points to AAI canonical, frozen pending Phase 2 retirement.

**Mirror rule retired 2026-05-03.** Tasks live in their owning project's Status & Todo. Cross-link in dependent project's Focus if blocking.

**CLAUDE.md rule:** ask for conversation links when updating these files. Accept "no link, date/time" for internal-only meetings.

---

## Slack channels

`#dx-product-measurement`, `#tmp_aem_missing_prompt_library`, leadership-tight channel (Pedro+Yanira+Jaclyn+Conrad+Ian+Bertrand, created April 21).

---

## Open vault gaps (still tracked)

- Stakeholder Map Vaishnav entry (held until Wed May 6 confirmation)
- Pre-meeting strategic brief for May 11 Loni + JM (draft week of May 5)
- Briefing v0 sections 5-6 (pending Indicator #8 on May 17)
