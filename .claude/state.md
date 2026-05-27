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

## Notes

- `decisions/` entries carry no scoreable predicted-outcome dates; NYL reactive-ownership decision is scored with H-007 on 2026-06-05.
- 2026-05-27 consolidation (not a full review): `ai-product/` +4 entries (Distributed-Harness Architecture — everything-is-a-skill, moat=data-not-mechanism, selection+consistency PM mandate, token-cost hierarchy); leadership Forum-entry outcome-confirmed (Ian shipped NorthStar + Saar escalation); H-003 evidence added. **Full System Review still due — co-schedule with Promotion Strategy review 2026-06-01.**
- When a full System Review runs, add a Review log row and reset "Last full System Review" + "Next review due".
