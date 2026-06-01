# System State

Operational state for the PM knowledge system. Cadence + lifecycle tracking lives here, not in CLAUDE.md (per global CLAUDE.md "System Review" rule). `staleness-auditor` and `/consolidate` read this file for the review-cadence check.

## System Review

Full System Review = stale rules, ready-to-promote/discard hypotheses, decision outcomes, quality-criteria pruning. Pedro decides timing (~every 2 weeks or after a milestone); not automatic.

| Field | Value |
|---|---|
| System initialized | 2026-03-19 |
| Last full System Review | **2026-05-27** (first ever) |
| Next review due | **2026-07-01** |
| Cadence | **Monthly**, 1st of month, co-located with the Promotion Strategy review. **Run locally with Claude (full vault + repo); Claude surfaces it at session start when due** — no automation. |

### Review log

| Date | Scope | Outcome |
|---|---|---|
| 2026-05-27 | First full review (10wk accumulation, ~5 cycles overdue). All 5 dimensions via `staleness-auditor`. | **Hypotheses:** killed H-004 (untested/superseded — EH thesis moved to selection+consistency layer) + H-006 (untested — Greg test never ran, 1 obs not 3); H-003 confirmed+promoted earlier same day. Active now = H-007 only. **Drift:** flagged ~3wk-stale Current Status blocks + ~50 past-due tasks + 🔴 inflation → refreshed both Current Status + reconciled tasks + re-triaged 🔴 (see session). **Decisions:** scored data-compliance-Felix (bet held, new ISO-42001 vector) + NYL reactive-rep (with H-007 on 6/5). **Quality:** patterns AI-Assistant→AAI fixed; parked-candidates centralized (below); ai-product "invocations" caveated. Base otherwise healthy — source/date hygiene strong, no dup emergency, FB-001→030 contiguous. |

## Open hypothesis-lifecycle decisions

Surfaced by `staleness-auditor` 2026-05-19. Pending Pedro's call — do not auto-resolve.

| Hypothesis | State | Decision owed |
|---|---|---|
| H-003 — Senior Director visibility = communication not performance | RESOLVED | ✅ **Promoted 2026-05-27** → leadership/ "The Director→Senior Director Gap Is a Communication/Visibility Gap". Confirmed (4 evidence-for + self-diagnosis + Ian-thread, 0 against). In resolved.md. |
| H-001 — 10-minute attention drop | RESOLVED | ✅ **Killed 2026-05-27** (untested/deprioritized) → resolved.md. No field test in 2+ months, no decision riding on it. |
| H-002 — pictures 6.5x recall | RESOLVED | ✅ **Killed 2026-05-27** (untested/deprioritized) → resolved.md. Same pattern as H-001. |
| H-007 — reactive vs proactive ownership | Proposed 2026-05-08; single instance (NYL) | Reassess **2026-06-05** (4-week window). Tracking mechanism currently inactive — log interim reps in Status files |

## Parked hypothesis candidates (holding for 2nd evidence)

Central tracker (was scattered across INDEX Access Log — quality gap fixed at the 2026-05-27 review). Promote at a clean 2nd *independent* instance; drop if stale by the next review.

| Candidate | Parked | Status @ 2026-05-27 |
|---|---|---|
| Operate-as-the-Role, Don't Re-Ask-Permission | 2026-05-13 | 2nd instance likely (hosted forum May 18 + Ian "must be PM lead" May 22) — **verify distinct** from Public Naming / Pick Up the Open Action Item before promoting |
| AOv2 V1→V2 inversion / skill-level-evals gap / manifest customer-exposure | 2026-05-05 | **Largely promoted 2026-05-27** into ai-product/ Distributed-Harness section — confirm fully covered, else close remainder |
| Default-and-Veto for Non-Responsive Peers; Diff-Based Ask vs Doc-Request; Forward-Framed Recovery; Independent Confirmation Signals Org-Wide Lane | 2026-05-05/08 | No 2nd instance surfaced — **drop next review** if still none. "Forward-Framed Recovery" likely already absorbed by `feedback_dont_litigate_prior_replies`. |
| Reusing a Platform's Ready-Made Components Is a Soft Commitment to That Platform | 2026-05-29 | 1 instance, analysis-derived (not outcome-validated). Consistency-layer mapping: the cheapest path to UI consistency = reuse AO 2.0's ready bricks (NextGen AIA UI + Quarry + Mithril), which all sit in AO 2.0's orbit → convenience = soft lean toward AOv2; staying engine-independent costs more build. Generalizes: "just reuse their components" is never neutral on platform choice. Promote to ai-product or false-beliefs at a clean 2nd instance. |
| Own the Layer Above the Substrate When a Rival Tandem Ships It | 2026-05-29 | 1 clean instance (Enterprise Ground Truth — Philippe+Daniel build the context substrate Pedro named; play = own cross-agent consumption/consistency/contribution layer above it + route via shared-VP ally Ian, don't contest the substrate). Distinct wrinkle vs existing leadership/ "Definition Ownership as Moat" (Rubin = Pedro got into the definition; here a rival tandem owns substrate → claim layer above). **Verify distinct** before promoting. Promote at clean 2nd independent instance. |

## Notes

- `decisions/` entries carry no scoreable predicted-outcome dates; NYL reactive-ownership decision is scored with H-007 on 2026-06-05.
- 2026-05-27 consolidation (not a full review): `ai-product/` +4 entries (Distributed-Harness Architecture — everything-is-a-skill, moat=data-not-mechanism, selection+consistency PM mandate, token-cost hierarchy); leadership Forum-entry outcome-confirmed (Ian shipped NorthStar + Saar escalation); H-003 evidence added. **Full System Review still due — co-schedule with Promotion Strategy review 2026-06-01.**
- When a full System Review runs, add a Review log row and reset "Last full System Review" + "Next review due".
- 2026-05-29 (#3) consolidation: 1 new ai-product entry (rendering contract carries structure not skin — A2UI/MCP-Apps/WebMCP). **AOv2 decision landed** (Ian, May 12, Conrad-delegated) — closes the long "discussed not decided" caution across memory. "Own the Layer Above the Substrate" parked candidate **deepened** (Pedro claimed the surface-map/convergence lane publicly before Bertrand in the Apoorva thread) but still the **same EGT instance** — keep parked, not a 2nd independent instance. H-007 reassess **2026-06-05** (tracking still inactive — log reactive vs proactive reps). **Promotion Strategy review due 2026-06-01** (monthly) — feed it the day's visibility reps: Silvia public naming (Pedro+Ian = harness strategy owners), Ian citing the blog 3x as decision reference, the public lane-claim before Bertrand. System Review itself NOT due (done 05-27, next 07-01).
- 2026-06-01 consolidation: **No new knowledge entries** — strategic execution session (June 1 #aem-agents thread, Pedro posted VP-visible reply while Bertrand OOO). H-007 got its **first tracked reactive-ownership SUCCESS rep** (logged partial — draft-iterated not cold; added evidence-against that prep-time may be the real variable, not proactive-vs-reactive direction). Reassess **2026-06-05** as scheduled. Memory-grade research: AOv2 = harness-plural NOT discontinued (per Ian's North Star verbatim — Markus Haack misread); Experience Workspace = emerging winner (Cloudflare Worker not Slicc, end-user skills, own memory); Bertrand named the consistency problem publicly ("thousand flowers garden", framed on infra not UI); Ian semi-disengaging ("happy to accept architecture is irrelevant if I don't have to do that work") = risk to Pedro's sponsor; A2UI already the AIA standard + Vineet's component lib coupled to AO 2.0 → Pedro's lane = decoupling/design-ownership, place defensively. **🔴 Promotion Strategy review due TODAY 2026-06-01** (monthly) — feed it: Pedro posted the standing PM position on a VP-visible thread while Bertrand OOO + Loni in town (visibility rep); Ian's repeated blog citations. System Review NOT due (07-01). Parked candidate "architecture owner disengages → foundation becomes PM job by default" = 1 instance (June 1 Ian) — hold for 2nd.
- 2026-06-01 (#2) session: **No new knowledge entries** — strategic execution. Two big AAI memory blocks added: (1) **post-2 review DM fork** — Ian rejected the build-shared-components mechanism, proposed consistency-by-checking-against-a-written-definition (Claude enforces); Pedro's lane **evolved A→B** (from "PM curates each surface" → "PM owns the definition + skill-declaration standard + consistency check", surfaces/users curate within = own the system not the content); reply drafted in his voice; risk = sponsor(Ian)-disengage + Helix-disrupt culture → layer nobody funds. (2) **CX Coworker = AOv2 customer-facing** (AO 2.0 + AIA 2.0 in one box, Bertrand May 1), GA June 11, AOv2-timeline call being scheduled (Manas+Bertrand+Pedro+Ian+Yanira); dependency-map HTML built. `feedback_draft_in_pedros_voice` got a new instance ("rails"/metaphor rejection). **Knowledge-sweep candidate (NOT promoted, 1 instance):** "Own the definition/standard, not the per-surface content" — likely deepens leadership/ "Definition Ownership as Moat" rather than new; revisit at next consolidation. H-007 reassess **2026-06-05** as scheduled.
- 2026-05-29 (#4) consolidation: **No new knowledge entries** — execution session. Events: Aditi onboarding task closed (overdue 2026-05-23 → done 2026-05-29, P42 wiki links + Slack sent); Agent Owners Alignment Call page (3716634108) deep-read — Sliccy URL confirmed, Onboarding Agent = first AEM agent live on AOv2, Sergiu sandbox experiments, Gabriel Stardust/Snowflake, roadmap webinars **June 9-10**, CSO service-model still incomplete, unclaimed wiki action claimed (AO v1 vs v2 draft saved to vault `AO 2.0/AEM Agents on AO - v1 vs v2.md`); Martin Buergi = EW Alpha lead (not Marcus Räck), DM sent 2026-05-29 15:15 CEST, awaiting reply. All captured in project_aem_agents_intelligence.md NEW blocks. H-007 tracking still inactive — next reassess 2026-06-05.
