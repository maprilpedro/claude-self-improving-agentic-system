---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (last ~1 week of events, currently **06-24→06-30**) + the compact durable reference below. **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**

> ## ▶️ RESUME HERE — left off 2026-07-03
>
> ### 🟢🛠️ 2026-07-03 (après-midi) — Playbook canvas REBUILT + 3-field standard LOCKED; integration-tracker canvas deduped; Ian ping drafted (unsent)
> - **Skill Selection Playbook canvas (F0BE83GE63S) rebuilt for readability** off Pedro's "très difficile à lire" call: the wall-of-H2 problem (half the body sentences were headings), asks buried 2/3 down, five-docs-in-one. Repaired: 5 real H2s, the two asks + you-own/I-coordinate split moved to the top, jargon defined inline (manifest, golden set, "0.763 = one pick in four wrong"). All substance kept. Read = the zero-in-channel-engagement of 06-26 partly explained by packaging: uptake came only from people Pedro TALKED to — a broadcast doc only its author can transmit doesn't scale ([[feedback_position_over_merit]]-adjacent; instance, not a new entry).
> - **🔑 The proposed field standard is now THREE fields: `domain` / `when-to-use` / `when-NOT-to-use`** (Pedro's call, same day): `when-to-use` = trigger + user's words; `when-NOT-to-use` = boundary + sibling redirect. `keywords` deliberately NOT in the public ask (triggers already carry search text). Canvas v2 live + vault twin [[Skill Selection Playbook — canvas repaired content (2026-07-03)]]. ⚠️ Align the audit-header spec (Tanju piggyback lane listed 4 fields incl. keywords) on these 3 so the audit doesn't count false non-conformes.
> - **Integration-tracker canvas (F0BEH27BLCS, #aem-agent-owners-alignement) deduped:** the ASCII box-drawing duplicate table removed, real markdown table kept (10 rows incl. Forms, real mentions); channel refs re-written as markdown archive-URL links. Two new canvas-API gotchas banked in [[reference_slack_canvas_api]] (channel refs = read≠write + API-unverifiable).
> - **Date-fix pass:** the morning session had mislabeled itself 07-04 (real date Fri 07-03) — memory blocks, watches, 2 vault note titles (Obsidian CLI rename, backlinks auto-updated), 9 vault files corrected; Monday watches re-dated 07-07→07-06. GA canvas F0BD4RALNHF still carries 6 "07-04" stamps — Pedro's call pending (6 manual UI micro-edits vs a full replace).
> - **Ian Boston ping SENT 07-03 (drafted same day, option B scope line):** the two-doors question (AIQ Events Dataset path vs DaaS Next + DPaaS) + the VA7 region check, scope = record-level tags read in place / aggregates-only out (Pedro corrected the "never raw records" ambiguity — reads happen on records, nothing raw LEAVES). Session rules used live: [[feedback_edit_the_span_not_the_artifact]] (3 options for one line), [[feedback_co_author_dont_answer_over]] (hand Ian the question), [[feedback_dont_conflate_pattern_with_object]] (two doors ≠ one object). PKD register recalibrated: **sentence shapes, not vocabulary** ([[feedback_pkd_chat_tone]] calibration #2).
> - Also: 3 loose repo files routed (pm-research agent + 2 commands tracked w/ stale-ref fixes; vault-split plan filed to `decisions/`). No new knowledge entry (honest) — instances cited above.
>
> ### 🟢🔑 2026-07-03 (midi) — VICTOR ANSWERED (email "AEM Coworker Working Session - Topics 06/18", red inline, 12:36) — the load-bearing questions from the 07-02 session get their AEP-side answers
> Victor Vlasceanu answered Pedro's blue inline comments (sent 07-02 16:37) within a day. What landed (screenshots 2026-07-03 12:47):
> - **🔑 The A/B/C reporting decider, answered with a process:** to Pedro's "can AEM sign the T&C, join the IMS Org, run its own jobs on the DataLake in-region, aggregates out?" → Victor: "**This** [link] is the main process for teams to access to AEP events dataset. **(available for all regions)**." = a standard team-access path to the AEP events dataset EXISTS, all regions → **Plan A (build in-place) looks viable**; the link (in the email, unread) is the pre-read for the **Angela Mon 07-06** meeting. Not yet a signed yes — read the process doc before locking direction.
> - **🔑 Provisioning phase answers:** Phase 1 (pilot = org IDs in a segment + runbook) → "**Yes**" confirmed. Phase 2 (mass migration) → "**You can do bulk operations for IMS org Ids**" = **a bulk path EXISTS** (working-level claim — verify scope at the Manas meeting: does "bulk" cover segment membership + SKU entitlement, the two separate rules?) **+ "AOv1 and AOv2 are not mutually exclusive today, so you need to remove from AOv1 if you want customers to have single experience"** = NEW fact: dual-running is possible → no forced hard cutover per org, BUT an explicit AOv1-removal step someone must own → strengthens the per-org cutover-owner gap + the ≥3-states denominator problem. Phase 3 (SKU steady-state) = no answer (Ken/Manas lane, as Pedro framed).
> - **Gating:** "**Sync sent**" — Victor booked the gating sync off Pedro's 3 points (advisories→error for AEM tools; feed the one-AEM-MCP conflict-probability into Gate 2; golden set seeded from confusion-pairs) + the Form-2a/2b selection-ceiling question. Check calendar.
> - **The stuck PR:** Pedro's "PR to get a new marketplace accepted, blocks our migration to skills, stuck since yesterday (shutdown week)… support beyond the channel for production?" → Victor: "**Will try to unblock today. Please tag me if this things will be blocked in the future.**" = Victor self-designates as the AEP-side unblock contact (⚠️ which PR — the marketplace-acceptance one; possibly distinct from ao#5773 governance-plugin prod — verify which one clears). Verify unblock landed by Mon 07-06; if Governance clears, update the GA canvas row.
> **Read:** the mid-July trigger's condition (a) ("no bulk provisioning path exists") is being answered BEFORE the trigger — partially defused at the mechanics level; what remains open is *ownership* of running the mass migration + comms, not the tooling. Victor = the fast working-level AEP channel (answers in <24h, twice now). Stakeholder enriched.
> **📖 Victor's "This" link RESOLVED + READ same day** (`aep-ao.pages.adobeitc.com/reference/aep-events-benchmark-datasets-access/`; source = `Adobe-Experience-Platform/ao` `docs/public/site/reference/aep-events-benchmark-datasets-access.md`, mirror of Confluence 3785437776, space aepai): **the AIQ provisioning guide — AI Quality Platform team (`@platform-quality`)**. Mechanics: JIRA clone **PLAT-277924** (or the `aiq-dataset-access` Claude skill in the ao repo) + team-members CSV → AEP Role `AIQ-Team-<TEAM>`, **read + AEP Query Service on the Events Dataset** (all AO telemetry: interactions, agent executions, tool invocations, guardrails) — 2-3 business days. **Prod = gated by Adobe Legal**: analytics/exploratory use = a lightweight email to `Grp-AEP-AI-Requests-Legal@adobe.com` (use case + 4 standards acknowledged). Handling: no copy to local/other storage, **no cross-region moves**, no raw prompts/responses/traces exfil — read-in-place only. **🔑 The money table (customer categories): usage tracking for CREDITS and for ANALYTICS/adoption = ✅ allowed for ALL THREE categories, including `no_data_access` customers.** → Pedro's business reporting (MAU/orgs/retention/per-agent value) sits entirely in the universally-allowed column, AND the credit/licensing reporting orphan (Bertrand's COA question) has its data-rights answer. **⚠️ The region catch: the dataset is homed in the AEP AI Quality VA7 org** (Prod+Stage) — Victor says "available for all regions", Ian's constraint says in-region hard; whether a VA7-homed central events dataset satisfies in-region for EU AEMCS customers = THE open question for Ian/Angela. Also: this path (AIQ Events Dataset + Query Service) ≠ obviously the same object as Ian's "DaaS Next + DPaaS single source" — two doors to reconcile before locking Plan A. ABAC labels (`AIQ_SHARED`) due end-May 2026 = should be live. **Plan A verdict: mechanism EXISTS and fits (query in place, aggregates as analytics output); open checks = region homing + the DaaS/DPaaS reconcile.**
>
> ### 🟢📐 2026-07-03 — Day-after map DELIVERED (Pedro's "what works Aug 1?" ask) + banked
> Answer built + banked in vault [[AIA Decommission — Day-After Map (2026-07-03)]] (GA canvas re-read live, unchanged since 06-26). **Synthesis: on Aug 1 what works for a standard AEM customer is MCP; the in-product assistant works only for hand-provisioned orgs (aem-orgs = 5 internal, base = 2k/300-400 active), markdown-only, on a fraction of agents (EPA furthest, Discovery internal-only, COA not started).** **CORRECTED 07-03 (Pedro):** Forms is NOT out — skills exist in a custom repo, not in any marketplace (invisible to Coworker; outside the EPA bridge); Governance = first skills LANDED, blocked this week on prod PR ao#5773 (ownerless). GA canvas F0BD4RALNHF updated live same day (Governance blocker + Forms row; one clumsy section-replace on the way — full content restored, verified clean) + vault twin + Day-After Map synced.
> **📤 BERTRAND READINESS NOTE SENT 07-03** (email, EN): **"I am treating AEM's cutover readiness as one program"** = the program claim ON RECORD to his manager, with the plan (canvas [0]-linked / Manas provisioning+ORR / Angela Rubin / Josh rail) + follow-his-line on the date (hold, staged option in the pocket, Anjul = last resort) + **the mid-July trigger proposed in writing** (no bulk provisioning path + global date stands by ~07-15 → stop waiting) + ONE ask (comms owner, suggested next to Akin's TBYB transition plan). Voice diffs banked as calibration #3 ([[feedback_draft_in_pedros_voice]]): metaphor-words cut ("tripwire"), want-not-veto ("before anyone flips" removed), no priority labels, footnote receipts, "In a nutshell" chunking, Business-Reporting terminology self-lock. Watches: Bertrand reply ~07-07; **mid-July trigger 07-15**. Governing uncertainty = Anjul's date + the unanswered manifest-vs-rail fork. **6 ownerless gaps = the Bertrand escalation list** (mass provisioning, fork, per-org cutover owner, customer comms — incl. the 81-org Quiet-Hours beta check, credit/licensing reporting orphan, quality gate). Status task closed → new escalation task 📅 07-08 (after Josh answers the fork). Confusion-pairs (item 1) PAUSED mid-plan by Pedro — plan stands in the 07-03 watch. Next in-session ask: what the decommission means technically for the **EH prompt-bar → AIA embed** (EH-side).
>
> ### 🟢🔎 2026-07-03 (night) — 10-channel Slack audit (3-wk window 06-12→07-03, 5 parallel readers; all channels covered to the boundary)
> Channels: #aem-agents, #aep-agent-orchestrator-collaboration, #aem-agent-experience-production, #aem-agent-owners-alignement, #p42-architecture, #aem-mcp, #ai-assistant-egc-ama, #p42-orr-circle (noise), #aem-aep-coworker-rendering, #aem-p42-leadership. New intel only below (already-banked threads skipped).
> **🔴 Dangling pings TO Pedro (answer owed):** (1) Corey 06-17, PR #58 `OneAdobe/aem-agent-reports` adds **Figma agent** to the EPA report — *"@Pedro Ferreira something you also need to do on your side?"* unanswered 2 wks (new agent entering the report taxonomy); (2) **Greg Klebus 07-01 uparrow** on Ankur's announce: **AEM Discovery Skill LIVE in Coworker** (5 internal orgs, Assets-only, wiki 3942897766) = the first AEM skill live — someone expects Pedro to act; (3) Siddhartha Srivastava cc'd Pedro+Yanira on AMA testing-instructions wiki (06-19); (4) Pedro's 07-02 escalation of Gerald's PR `ao#5773` (governance plugin OOTB in cx-coworker prod) still ownerless AEP-side.
> **🔴🔑 The decommission battlefield (p42 thread `1781690973.168739`, Ian Boston 06-17 — the thread BEHIND the Rubin port):** P42 decommission list (API-First A2A/MCP routing; AI Observation for Agents; DaaS Next for Agents) → *"All reporting for Agents will now be provided by AO Rubin"*, prompts via AEP LangFuse. Pedro's reply = the public claim of the Rubin port + named the orphan (**credit/licensing usage reporting** — Bertrand's COA question). **Michael Marth: "the items above need my approval and the way I read them I will not approve"** = decision contested at Sites-eng leadership. **Bertrand: only real decision = Anil's stop-AIA-on-AO1.0 (via Anjul), does NOT forbid other harnesses where Coworker doesn't fit** (EMA-on-Claude-SDK outperforms AOv1; Mysticat LLMO jobs Coworker can't do). DACI demanded, doesn't exist → **Felix Meschberger now owns a formal AEM Coworker DACI** (born from Pedro's 06-16 founding post, Marius Duta's suggestion).
> **🔑 Ian Boston 07-02 (reply to Pedro, #aem-mcp thread `1782825794.226979`):** accepted Pedro's frame ("makes sense") but planted two constraints on the Rubin port — **single source for management reporting = DaaS Next + DPaaS** ("standardised access, consistency in the numbers") and **in-region as a hard requirement**; "what we do with Coworker/Rubin is TBD, but that will have to be in region. DPaaS does not support reporting on customer data." → bring INTO the Angela meeting Mon 07-06.
> **🔑 Dates hardened:** Bertrand public 2×: **AIA 1.0 + AO 1.0 retire END of July** (not 07-15), Unified Shell switches to **CoWorker Chat rail = "AIA 2.0", custom UI on Coworker headless**; Pedro's "July 15 too short" objection superseded by the end-of-July clarification (his objection itself never got a direct reply). Tim Lynn: UI cutover "in july, no exact date." Dan Balescu reality-check: **Coworker GA = press-release GA, 16 early-access customers**, AEM AIA stays on AOv1 "undetermined time."
> **🔑 Rendering path DECIDED (Pedro's own channel `#aem-aep-coworker-rendering`, 06-24):** chat-artifact components get contributed to `Adobe-dxue/coworker-ui-experience` packages/chat-ui **A2UIRenderer** (Tim Lynn guidance, relayed by Eugene); **Harsh Chiki: "markdown nailed, next = data grid"** + shared the A2UI storybook + offered collaboration; **Bertrand entered the thread** asking where data-grid renderer code lives. Pedro's Coworker-Rendering wiki review ask (3941701228, 06-23) = **zero replies**. → feeds the Josh 07-08 meeting + the Rebecca+Sorin+Eugene+Harsh meeting.
> **🔴 Two new competitive fronts on the MCP lane:** (1) **CX Enterprise MCP GA'd WITHOUT AEM** — Tanju: "engaged too late to be included in their GA scope… we supported CXE in gathering AEM usage data"; (2) **Adobe Marketing Agent exposes the 5 AEM agents in Beta on ChatGPT/Claude/Gemini via its OWN MCP** (`aep-ai-ama.adobe.io/mcp`, MCP→A2A over AOv1; AOv2 move "planned for July" under the agentic gateway) — Harsh Chiki's *"how does it align with One AEM MCP?"* + Alex Trifan's *"what is your PM decision?"* = **Pedro's decision, dangling in public** (#aem-agents thread `1781265348.778349`).
> **🔴 Third harness axis + naming correction:** **AIP/AUP builds `adobe-chat-harness`** (Adobe Intelligence Platform — Photoshop/Firefly; #adobe-intelligence-platform); Meschberger: "don't be distracted, continue with Coworker." + AEP **rejects the word "Harness" for Coworker** — official names "CoWorker" / "CoWorker Headless" (Ian, replying to Pedro's own recap). → both = v5 candidates for One-AEM-Many-Harnesses (v4 just shipped).
> **🔑 MCP reporting materialized + number-hygiene receipts:** **Jabran BUILT the joined dashboard** (06-26, AWS logs manual for now, per-tool + One-AEM-MCP); Christian's 06-25 30d report: **348K external requests (-5% vs May), 149 external orgs (+9), 94% from MCP apps**, top = KOMATSU 45K / CrowdStrike 25K / Canon Medical 18K / Abercrombie 17K. Hygiene: **Cursor over-counted** (many clients piggyback `aem-oauth-cursor` — Copilot/Augment/Cline/Windsurf/Codex), **internal-agent usage shows 0** (Tanju flag, Christian confirmed), Cedric: "we discuss these in leadership meetings — worried we conclude the wrong insights." **Cedric independently asked for an actions-by-client dashboard (AEMAGT-2052)** = external demand for Pedro's volume-vs-value cut → outcome support for [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]] (flag for next System Review, not a new entry).
> **Also banked:** Playbook 06-26 — zero replies IN-CHANNEL but **uptake happened out-of-band (Pedro, 07-03): Corey opened a JIRA off Pedro's ping (ID to capture — not findable via JQL playbook/skill-selection searches 07-03), Sergiu said OK.** Action = FORMALIZE the uptake (link the JIRA, scope Sergiu's commitment, per-team adoption rows), not a relance; Rubin Chat Analysis promo to leadership 06-12 = zero engagement; **AEM Context Service** (Ashok Kumar) = API-first Discovery-Service replacement, Ian ties it to CM-anchored credits/reporting ("not onboarded in CM breaks reporting, leaves Adobe exposed"); Ian HIPAA ruling on the GA canvas (Coworker can never be in AEM's HIPAA BAA scope; ePHI must not enter); **Rodson Clavel writing the WebMCP docs** (tool-count/description guidance hole = Playbook insertion point; Jonny Moon: 9,140 words of registered tools "works well"); Marketing Agent Testing wiki (Pedro/Yanira, owed "EOW" ~06-26 per Yanira's leadership agenda) — **verify delivered**; Sergey Generalov: Rubin "mostly business use, field", Langfuse per-region joinable; Ilya Grafutko: "tell me what instrumentation is missing"; AOv2 self-service org+user rollout segments "near future"; Trace API endpoints exist (`GET /copilot/chats/{id}/interactions`); leadership channel (Yanira 06-22 agenda) names Pedro the **Coworker-guidance owner**. **No new knowledge entry (honest)** — intel + instances; the Cedric ask logged as outcome support.
>
> ### 🟢📤 2026-07-03 (eve) — MCP reporting-framework wiki PUBLISHED + One-AEM-Many-Harnesses v4 LIVE + Christian/Jabran relance SENT
> **The owed wiki shipped:** `wiki.corp.adobe.com/pages/viewpage.action?pageId=3958942271` (space ~pedrofer, DRAFT banner). Vault twin `AAI - Project Folder/MCP Business Reporting Framework (wiki draft) 2026-07-03.md` carries the URL. Content = the 5-metric framework (active orgs ✅ / MAU ⚠️ identity-definition open Q for Christian / retention ✅ / Tool Calls by class ✅ / value realization 🔴 blocked on the CloudWatch join), the Level-0/Level-1 data model (never cross-divide), the generic-vs-specific tool cut (Christian's correction baked in) + add-time classification rule (hook = Tanju's catalog loop), reporting rules incl. the HOLD. Definitions marked *proposed*, facts sourced — no numbers upward. = the own-the-definition / write-the-framework move made a citable artifact ([[feedback_position_over_merit]]; operationalizes [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]] + [[Metric Definition Ownership — PM Validates, Reporting Track Owner Implements]]: Pedro defines, Christian/Jabran implement).
> **Relance SENT** (group DM `C0BE2P6J00M`, EN): wiki link + the CloudWatch join re-ask + **one-off joined 30d export** as a lower-bar first pass + explicit "hold stands until your traffic review is clean". DM verified silent since Pedro's 06-30 accept before sending. Watch: awaiting reply ~07-08, then raise in #am-mcp instead of a 3rd DM ping.
> **v4 republished** (Confluence `3908567486`, version 4 — open op since 06-07 closed): brand-travel table split (visual skin vs structure/voice/behavior, per Brian) + "Claude → an LLM" in check/definition. **Root cause of the recurring Confluence 401s = VPN not connected, NOT PAT expiry** — three weeks suspecting the wrong culprit; check VPN first on any future 401.
> **No new knowledge entry (honest)** — execution of banked plans; instances cited above. H-007 untouched (wiki + relance = proactive/prepped, not a cold reactive rep).

> ### 🔧 2026-07-03 — System-overhaul session (P1-P7 + capture-1-6, ~15 commits, git log = the record) + Christian DM worked
> **PM-relevant residue only:** (1) group DM `C0BE2P6J00M` captured via the new `/capture-slack` → venue correction + the open **CloudWatch↔jwt_client_id join ask** (see the 06-30 block addendum ↓ + watches). (2) ~~/reply draft to Christian+Jabran~~ → **SENT 07-03 eve** (see block above). (3) ~~draft the wiki~~ → **PUBLISHED 07-03 eve** (see block above). (4) New session mechanics live: watches.md (single dated registry), /reply + /capture-slack auto-trigger, glossary, ENTITY_INDEX, _inbox. Caveman hook removed for this repo (PKD×director-PM register full again). No new knowledge entry (system session — honest); H-007 unchanged (the Christian draft = prepped, not cold).

> ## ▶️ (older) — left off 2026-07-02

> ### 🟢🔑📐 2026-07-02 — Reporting-substrate decision framed + provisioning mechanism VERIFIED in the `ao` config. Two email/Slack threads worked live (Victor inline reply on the Manas agenda; the cq-dev EPA-manifest thread). Big session on where AEM reporting lands + how customers actually get onto Coworker.
> **🔑 Two reporting tracks — DO NOT conflate ([[feedback_dont_conflate_pattern_with_object]]):** (1) **business reporting = Pedro's** (MAU/orgs/retention/per-agent value for Loni+JM); source today = **Copilot Review Tool → Pedro's business backend, NO Langfuse** (corrected + committed `169a985`; the old "Copilot→Langfuse→backend" line was wrong). (2) **engineering track = Langfuse/traces** (Ian/Sergiu/Felix), a separate parallel path, never Pedro's business source. Victor's inline "traces→Langfuse / events→AEP DataLake / quality-flow for the 12-day limit" = **entirely the engineering track**, not Pedro's alimentation.
> **🔑 Business-source continuity problem (the real one):** the Copilot Review Tool is an **AOv1 artifact** → as agents move to Coworker, that source **dries up.** So the **Rubin port = re-sourcing** business reporting off the AEP DataLake (Coworker data), NOT because Langfuse was ever in his chain. **Timing sharpened by the cq-dev thread:** the bridge swaps the **backend** (AOv1→AOv2) behind the unchanged AIA v1 UI → the source dries at the **backend swap**, earlier than a UI change.
> **🔑 Reporting decision A/B/C — full reasoning in vault [[Decision — Business Reporting Port — Rubin vs AEP-AEM Bridge (2026-07-02)]] + [[Angela — Rubin Business-Report Port — next]] (Mon 07-06).** Short: A = build in-place on the AEP side (T&C/IMS-Org, aggregates out); B = AEP→AEM Databricks bridge; C = AEP builds it. Ian's 06-23 verbatim: point 5 = customer-FACING (→ **C off**, not Pedro's internal reporting); point 4 = use-in-place ALLOWED / exfiltrate-to-AEM NOT (→ **B constrained**, A clean). **Decider = a capability Q for AEP (Victor/Falca), NOT Ian (he only relayed Falca):** can AEM run jobs on the DataLake in-region, aggregates out? Yes → in-place, no bridge, Pedro's call.
> **🔴🔑 PROVISIONING MECHANISM — VERIFIED first-hand in `Adobe-Experience-Platform/ao` config (not inferred):** Triggered by the cq-dev thread (Bertrand→Vitaly→Felix Delval→Satya on PR `ao#5811`). Vitaly: the AOv1→AOv2 **bridge forwards at the sub-agent level + the forwarding path enforces the manifest** → each sub-agent needs its own manifest (Conway's Law); EPA replaces **Content Update/Create technical agent only** first; Bertrand's bar = *"as long as it's not visible to end users, all good"* (backend swap, Plan B). Felix Delval: *"how do we know who has access to Coworker UI?"* + *"currently no one is using this manifest."* **Verified in `config/aep-aia/environments/prod/`:**
> - **Access = explicit per-org segment membership + SKU entitlement, two SEPARATE rules.** `config.yaml` rule `aem-orgs-to-aem-aia` (enabled) binds segment `aem-orgs` → manifest `aem-aia`. **But `aem-orgs` has NO app-access rule of its own** (unlike `aem-onboarding-orgs`/`aem-drm-orgs` which have both) → app access = a separate entitlement segment (SKU, e.g. `entitled-acp-coworker`). Manifest ≠ app access; need BOTH.
> - **`aem-orgs.yaml` = 5 orgs, ALL internal/demo/trial** (Skyline Prod Test017, Adobe Demo 002, AEM Sites Trial, AEM Showcase, Sites Internal). **Zero production customers** → that's why "no one is using this manifest." First member = "Skyline Prod Test" → [[reference_skyline_p42_orglist]] again.
> - **Access does NOT auto-inherit from AIA v1** — it's an explicit org-ID edit in a segment yaml. So **the bridge does NOT provision customers; provisioning is a separate, explicit, per-org track on top of it.** = answers Pedro's "il faut provisionner les clients sur Coworker en plus ?" → **YES.**
> - **42 customer/org segment files in prod** (coca-cola, amex, ibm, comcast, disney, gm, home-depot, intel, ey, air-india…) = enterprise-by-enterprise **hand-maintained** lists. For a **2k base / ~300 active**, 42 provisioned = the scale wall, real + current. The runbook Satya linked ([[reference_coworker_faq]] Babu Ramaraj) = the per-customer manual path.
> **🔑 Reporting consequence:** the **adoption denominator ("who's provisioned on AEM agents")** is READABLE from these segment yaml (aem-orgs + entitlement segments) but **manual** = same p42 fragility. Pedro's lane = own making this a single clean source (both cutover + adoption reporting hang on it, nobody owns it today). A customer can be in ≥3 states (AIA-v1-only / bridged-backend / Coworker-provisioned) → the denominator must distinguish them or it over-counts adoption. **Additive Slack reply drafted for the cq-dev thread** (build on Felix, claim the denominator ownership, concrete-Bertrand-first, don't answer-over — [[feedback_additive_not_corrective]]).
> **Provisioning = 3 phases (Pedro's frame — POSTED in the cq-dev thread 07-02, so it's on record as his structure):** (1) onboard **test customers** for AEM's Coworker-migration validation (manual segment+runbook OK for a pilot); (2) **mass migration of the entitled AOv1 base — 300-400 active today** (per-org segment + SKU, org by org = the wall — needs a bulk path); (3) **steady-state scale — 2k AEM customers, ~50 new orgs/week est.** (= Ken's SKU-based entitlement, not manual yaml). Phases 2-3 = Ken+Manas (SKU + migration track); phase-1 mechanics = Victor/AEP. **Pedro posted the guide + the 3 phases only — he did NOT yet plant the denominator-ownership grab** (who's-provisioned = the adoption denominator, nobody owns it). Held for the Manas meeting or a later add; the thread carries his *structure*, not yet his *ownership*.
> **New/enriched stakeholders:** **Victor Vlasceanu** (AEP, working-level; answered Manas's agenda inline — gating docs, provisioning guide, support channel `#aep-agent-orchestrator-collaboration`, per-team golden set; skills-marketplace = Manas's call). **Felix Delval** (@fdelval — EPA/AEM eng doing the config archaeology; **NOT** Felix Meschberger @fmeschbe). **Vitaly Tsaplin** (EPA manifest/bridge author, PR 5811). **Satya Deep Maheshwari** (found the provisioning runbook). **Alexander Falca** (AEP AI-Observation *access* owner — the real source Ian relayed; cc'd on the Manas email). **Gating (AEP `ao-collab` quality track):** the Coworker Agentic Gateway quality framework (Phase 1 catalog lint / Phase 2 selection eval / Phase 3 LLM judge; 3 admission gates; `mcp-tool-admission-gating.md`) = **AEP already built Pedro's Playbook at the gateway level.** Pedro's seam = the **upstream** discipline (description quality across AEM agents) + AEM's **own golden set** ("each team owns its own", Victor) seeded from the confusion-pairs for Ian → [[Govern a Consistency Layer Over Primitives You Don't Own]] (2nd outcome-instance, watch to harden).

> ### 🟢🔑🤝 2026-07-01 (b) — AEM Governance / One AEM MCP convening meeting (Pedro + Tanju + Governance-Agent Basel team + Gerald; ~30 min, full recording). [transcript: `Meeting Notes/One AEM MCP/20260701 - AEM Governance _ One AEM MCP.md` — this = the COMPLETE recording of the convening meeting whose opening only the Tanju 1-1 transcript caught (Mark/Andrew/"Speaker 3" = the Governance Basel team + Andrew).] Otter garbles: "1AM/AMCP"=One AEM MCP, "EGA/BGA/AGA/golden agent"=Governance Agent/MCP, "Entropic"=Anthropic, "who worker"=Coworker, "Lonnie"=Loni.
> **🎯 Pedro's frame (opening, ~00:01, = the user's stated goal for this whole lane):** *"I'd like very much to push all of the [cross]-agents to be consolidated behind One AEM MCP"* + *"a coherent interface for our customers in terms of MCPs"* — discussed with Bertrand. Coworker's own MCP-gateway layer = **not available today** (they'll push it "near future") → the window to consolidate behind One AEM MCP is now. Then Pedro mostly listens; Tanju + the Governance team work the integration mechanics.
> **🔑🔑 The external forcing function (promotion-grade — the WHY behind Pedro's lane, validates it by platform constraint not merit):** *"Anthropic says, hey guys, you cannot have gazillions of MCP servers in the store. Please talk internally and consolidate. That's how the idea came about of One AEM MCP server."* (Tanju, ~00:20:53). = the consolidation Pedro is convening is **forced by the store-admission limit**, not a nice-to-have → the strongest lever to move reluctant teams. **+ Exec pull:** *"Loni on Friday said 'I want to be in Slack'"* (Tanju, ~00:21:12); ChatGPT store = submitted, in review. The One AEM MCP is the single artifact that gets AEM INTO the Claude/ChatGPT/Slack stores → every agent team that stays out of it stays out of the stores.
> **🟢 The sell (why teams should come behind it — Tanju, sourced):** One AEM MCP already solves **discovery** (semantic search over ingested skills+APIs → best-10 hits → LLM writes code → executes in a **secure sandbox**) + **scaling** (~10,000 concurrent agents/users on the current architecture). *"This is what you would get for free if you take the One AEM MCP server, because the other guys are not there even."* Coworker/umbrella team built their OWN MCP = **200+ tools** (ingested AJO/Workfront/etc.) → **broke on MS Copilot Studio** = the cautionary precedent for un-curated tool-sprawl. Selection = *"a walking decision tree… max 3 hops; more than that = a regression signal to improve the catalog's semantic search."*
> **🟢 Governance integration path DECIDED (provisional, Tanju + Governance Basel owner):** (1) keep the **Governance Agent as an umbrella/standalone in parallel** (live customers already on it → not decommissioned near-term), add new functionality there, then **pass-through to One AEM MCP → AOv2** so the gov team *"controls what we deliver"*; re-decide direct-vs-proxied later (*"second moment, we sweep and we decide then"*). (2) **One entry point** into MCP functionality serving both One AEM MCP + AOv2 (*"one entry point for you and for the AOV2, and that's it"*). (3) **Skill delivery = a GitHub marketplace** — Governance publishes/updates a GitHub marketplace; adding a skill there **auto-updates Tanju's server** (no copy-around; the manifest YAML points to where the skills live = confirms [[reference_aov2_marketplace_manifest]]). **Why upstream-as-MCP is the only clean path:** the Governance function is an **LLM function, not a REST API** → can't be trivially wrapped.
> **Action items:** **Tanju** → send the repo link + public link to the One AEM MCP so the Governance team can connect + test (immediate). **Gerald** (Governance eng, building V2 skills) → provide the V2 skills that plug into One MCP + hand new skills forward as they land. **Governance Basel owner** → bring the direct-vs-route-through-governance question into the daily; the **"does the customer see a *governance-agent MCP* or a *One AEM MCP for governance*" = a Bertrand/product-side call, not technical.**
> **🔴 Risks / open:** proxy-on-proxy-on-proxy + MCP-to-MCP-to-MCP latency (feature toggles = escape hatch to shortcut a direct upstream); **EGA permission + DLP work is unfinished — wasted if going direct** to One AEM MCP (Governance team to decide their end); **CX Enterprise Edition MCP = another gateway in front** → gateway proliferation (driver = Anthropic store limits); **scaling cliff at ~10K** (beyond = micro-VM rearchitecture, not justified now); **A2A** — *"do we stop supporting A2A?"* raised, no customers on it, left open; **Coworker Uber-MCP convergence = aspirational, undated** — *"foolish to assume the 1AM MCP has a life after that… but I would not bet on that"* / Coworker team **declined to let Tanju clone/co-design ~2 months ago** ("waterfalling"). One AEM MCP persists as interim **by default, not by decision.**
> **Reconcile:** = the concrete first execution of the "Drive the cross-team MCP-integration push" task (Governance was "not yet" on 06-30 → now actively engaged, path defined). Confirms [[reference_aov2_marketplace_manifest]] (manifest YAML → marketplace; multiple marketplaces by design) + [[reference_aia_vs_coworker_axes]] (Coworker/AOv2 = backend end-state; gateway not shipped). **No new knowledge entry earned** — rich intel + an instance of the convening lane; but **WATCH (1 instance, not parked):** *"an external platform constraint (Anthropic: consolidate or you're out of the store) is a stronger forcing function for a cross-team convening than internal merit — lead the teams with the constraint, not the pitch"* — adjacent to [[feedback_position_over_merit]] + leadership/ Forum-to-Manufacture; hold for a 2nd instance ([[feedback_consolidation_without_substance]]). **New stakeholder:** **Gerald** (surname unknown — Governance-Agent eng building V2 skills, the source of the skills One AEM MCP will consume). Also referenced: Michal Mart (low-conf — Anthropic-side contact), Ilie (low-conf — regulatory-heavy customer co-innovating a maker/checker/auditor control framework). Governance Basel owner = CR-mic, attribution uncertain (likely the Governance plug-in owner, Andrei Stefan Tuicu-adjacent — do NOT assert).

> ### 🟢📊 2026-07-01 (c) — Tanju's status reply on the One AEM MCP integration list (Slack) → the cross-team tracker, corrected + expanded. [screenshots banked: `screenshots/20260701-tanju-*` (status reply, EPA clarif)]
> Pedro sent Tanju a status list ("who's on the One AEM MCP, confirm/correct") → Tanju's reply reshaped it. **The corrected cross-team state (broadcast to agent owners 07-01):**
> - **Assets** = Live in prod (search = @chiki, ex-@igurjar; CRUD adhoc = @amalhotr; + converged discover/search).
> - **Discovery** = In progress (@arora driving; the client LLM does the reasoning the Discovery Agent does today; sources already there = asset/fragment/sites&pages search; **Forms piece missing**; @meyer/Christian keeping tabs).
> - **Governance** = In progress (from the 07-01 (b) meeting: umbrella + pass-through via a GitHub marketplace).
> - **AEM Guides** = Ready — just waiting on the upstream MCP-server support to come online, then they switch.
> - **DA (da.live)** = Planned — @mhaack (Michael Haack) built the first DA MCP Server; on the roadmap to move it into One AEM MCP.
> - **LLMO** = Planned Q4 — wants an MCP Server (@duttchau, @petcu); good fit inside the AEM MCP Server.
> - **EPA** = **its own EPA-scoped MCP today** — the **Content Updater technical agent was renamed "EPA MCP Server" but only does EPA's own stuff**; GTM strategy not settled; **@cdulimba (likely Corey Dulimba, EPA owner — confirm) will clean up after the shutdown + set EPA prios.** (This resolves the "EPA listed twice with different status" confusion: own scoped MCP + upstream-to-One-AEM-MCP suggested as first iteration, prios TBD.)
> - **CDN Insights** = Exploring (@jjung, @aschhabr — Databricks-heavy agentic capabilities to expose via MCP into Coworker → toward One AEM MCP; "only a coffee chat so far").
> - **Content AI** = Exploring (@ashok, @mokatari — more fundamental question: what's left to serve when Asset/Page/Fragment Search already exist).
> - **Forms** = Open, no contact yet.
> **🔑 CORRECTION — "Encore" and "Jean-Claude" were Otter garbles of PERSON names, not teams.** Source = the 06-30 MCP Reporting Strategy transcript (Otter, no timestamps). Verbatim (line 152): *"Encore from assets, he's quite on board"* = **a person on the Assets team** (name mis-transcribed); *"what was his name, young Claude for Jean Claude"* = Tanju **searching for the name live** → uncertain even to him. Tanju "misspoke" on Encore, wants the transcript context. → drop both as teams; do not carry "Encore" / "Jean-Claude" as agents. (Corrects the 06-30 block below + the Status push task.)
> **New stakeholders (handles from Tanju, low-confidence spellings):** @cdulimba (likely Corey Dulimba, EPA owner/DRI — cleans up EPA post-shutdown), @arora (Discovery), @amalhotr + @chiki + @igurjar (Assets contributors), @mhaack (Michael Haack, DA MCP), @jjung + @aschhabr (CDN Insights), @ashok + @mokatari (Content AI), @duttchau + @petcu (LLMO). **No new knowledge entry** — cross-team status intel that expands the convening tracker. Tracker now lives in Status & Todo (`## One AEM MCP — integration tracker`).

> ### 🟢📋 2026-07-01 (d) — Ingested the EPA "Migration to AOv2" canvas (Slack canvas `F0BD48C5R9P`, EPA-team-maintained). = the canonical living doc for the EPA→AOv2 plan (formalizes the 06-25 Felix plan review already in memory + adds timeline, owners, decision).
> **🟢 DECISION formalized (06-25 EPA sync — Gilles, Corey, Satya, Pedro, Yanira, Tanju):** **Plan B (AOv1→AOv2 bridge) = primary execution path**; Plan A (direct migration) continues in parallel, NOT primary; **"treat Coworker as one optional surface, not the primary platform dependency."** = **outcome support for Pedro's switchability / two-way-door / keep-engine-optional thesis** (ai-product Distributed-Harness) — the EPA team adopted it as the canonical posture. Plan C (EPA custom harness) = **NOT VIABLE** (not core business / CCF; EW chose not-AOv2 so no base to reuse).
> **Desired state:** EPA substitutes all Technical Agents **except Forms** via the bridge; target 07-17. **Timeline:** EPA Manifest in AOv2 🟢 07-01 (PR `ao#5811`); Bridge in Staging 🟢 07-03 (synced EDA, "EDA no hurry"); Rollout plan 07-08; Skill Coverage Parity 07-10; Bridge in Prod 07-13; Skills+Bridge BugBash 07-15; **1st customer 07-20**. Bridge code = `Adobe-CloudManager/aem-ai-agent-orchestrator` @ `aov2` branch. Plan B flagged **risky** ("might only be used 2 weeks").
> **🟢 POSITION WIN — Pedro's callout is CITED in the canvas.** Plan A's dates carry: *"The dates below are not realistic, not all agents are ready"* linked to **Pedro's cq-dev thread**; "All AEM Skills validated **not before 07-31**." = his "we missed the starting line" / dates-not-realistic read is now IN the EPA canonical doc, attributed to him ([[feedback_position_over_merit]] — his analysis became the team's recorded truth).
> **Pedro's owned follow-ups (assigned to `WM9TYS877` = Pedro):** (1) **Skill Provisioning Process** — check with Manas how customers are provisioned on AOv2 + coworker (⚠️ canvas says "Manus" = Manas) → already partly on the tracker (Ken SKU + Manas follow-up); (2) **Integrate the engineering reporting solution with Langfuse in AOv2** ("fuse chain" = an Otter/AI-summary garble, clarified by Pedro 07-01) — how the engineering reporting hooks into **Langfuse** (traces) once EPA is on the bridge/AOv2; Pedro has no how yet → **plan = pull Ian Boston + Sergiu (EDA) into a working session** ([[reference_ai_observation_architecture]] OTel→LangFuse→DaaS/Rubin; ties Ian's reporting-continuity Q + the Rubin port); (3) **Skill Definition Audit + broadcast best-practices** (naming/description/triggers for LLM selection) = **DONE** (the overlap audit + the Playbook posted 06-26 + today's MCP broadcast). In the meeting Pedro also raised reporting/operationalization concerns + drove the LLM-skill-selection-metadata point; Tanju suggested codifying best-practices (CLAUDE.md-style) = aligns with the piggyback-on-Tanju's-loop play.
> **Reconcile:** confirms + formalizes the 06-25 Felix A/B/C review (already banked). Adds: the canonical canvas location, the concrete dates, PR `ao#5811` + the `aov2` branch, and Pedro's callout cited (position win). Ties [[reference_aov2_marketplace_manifest]] (EPA manifest without Forms; per-technical-agent manifests). **No new knowledge entry** — outcome support for the switchability thesis (flag for the next System Review, not a new rule). New owned item: run down "fuse chain" reporting in AOv2.

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

---

## Felix reports + report pipeline

> **Moved to `project_aem_agents_intelligence_ARCHIVE.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

## Apoorva validation punch-list (KR1)

**Status:** items 2/3/5/6 deadline compressed April 23 from 2026-05-09 → 2026-04-27 (Monday). Item 1 closed April 20-22 (Varun: org-to-org-type assignment fix, AEP scorecard CSV match, Claude delta below 3%, Copilot API as source of truth). Item 4 (First Useful Result Rate) in progress. Ankur Connect May 9 = post-close checkpoint.

**Items (April 16 meeting with Apoorva + Ankur Arora + Varun Kalra):**

1. **50-60% data gap vs Grafana.** ✅ closed April 22 (Varun fix).
2. **TSR counts "no result found" as success.** Redefine — for Discovery, result-found rate is the right signal.
3. **Tag classification bleeding across agents.** Discovery showing pipeline troubleshooting (EDA), content update, brand validation (Governance). Per-agent tag filtering broken.
4. **First Useful Result Rate missing.** Apoorva's named VR metric for Discovery. Maps to Loni's adoption framing.
5. **Content-type breakdown for Discovery:** assets / pages / content fragments / forms.
6. **Aggregated metrics transparency.** Split or remove. Flag North Star vs operational.
7. (Medium) Promo SKU + Try-Before-You-Buy credit utilization view.
8. (Medium) Calculation logic documentation per metric.

**Walk-in line for Bertrand/Loni:** "Apoorva's team stress-tested, found gaps, we're closing them. First Useful Result Rate incorporated. Report credible for Loni path after fixes." NOT "Apoorva validated."

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

> **Moved to `project_aem_agents_intelligence_ARCHIVE.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

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

**AO / AEP:** Conrad Woltge (Sr Principal Architect), Trent Davies (eng, AO), Ken Russell (eng, AO), Sergey Generalov (PM, AO), Ian Boston (compliance), Manas Garg (AOv2 dev experience).

**Data / Reporting:** Felix Delval (data eng, EPA pipeline), Lara (taxonomy + Governance), Varun Kalra (Discovery validator, Apoorva's team), Karthik Penikalapati (Rubin tech lead), Angela Han (Rubin owner).

**Design (Adobe Design lane):** Silvia Mulet Ferre (Eugene's manager), Uma Subbu.

**Leadership:** Loni Stark (VP AEM & Commerce), Jean-Michel Pittet (VP Eng AEM), Jaclyn Eckersley (FinOps, AEM Eng VP-side), Bertrand de Coatpont (Sr Director PM, manager), Shankari Panchapakesan (Group PM, transitional).

**PMM:** Tina Nicu, Akin (PMM for AEM survey), Vaishnav Gorur (new PMM AEM agents — pending confirm Wed May 6), Haresh Kumar (chain to Vaishnav).

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

---

