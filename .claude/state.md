# System State

Operational state for the PM knowledge system. Cadence + lifecycle tracking lives here, not in CLAUDE.md (per global CLAUDE.md "System Review" rule). `staleness-auditor` and `/consolidate` read this file for the review-cadence check.

## System Review

Full System Review = stale rules, ready-to-promote/discard hypotheses, decision outcomes, quality-criteria pruning. Pedro decides timing (~every 2 weeks or after a milestone); not automatic.

| Field | Value |
|---|---|
| System initialized | 2026-03-19 |
| Last full System Review | **never run** (2 months elapsed) |
| Next review due | **overdue** — propose at next natural break |
| Cadence anchor | Promotion Strategy monthly review (next 2026-06-01) — co-schedule the System Review with it |

### Review log

| Date | Scope | Outcome |
|---|---|---|
| — | — | No full review run yet. |

## Open hypothesis-lifecycle decisions

Surfaced by `staleness-auditor` 2026-05-19. Pending Pedro's call — do not auto-resolve.

| Hypothesis | State | Decision owed |
|---|---|---|
| H-003 — Senior Director visibility = communication not performance | Proposed 2026-03-19; 4 evidence-for + 1 dated obs, 0 against, 2 months untouched | **Promote** to a `knowledge/leadership/` entry, or set an explicit re-test |
| H-001 — 10-minute attention drop | Proposed 2026-03-19; literature-only, 0 field obs, test never run | **Kill-or-commit**: design the test or archive to resolved with "untested, deprioritized" |
| H-002 — pictures 6.5x recall | Proposed 2026-03-19; literature-only, 0 field obs, test never run | **Kill-or-commit** (same as H-001) |
| H-007 — reactive vs proactive ownership | Proposed 2026-05-08; single instance (NYL) | Reassess **2026-06-05** (4-week window). Tracking mechanism currently inactive — log interim reps in Status files |

## Notes

- `decisions/` entries carry no scoreable predicted-outcome dates; NYL reactive-ownership decision is scored with H-007 on 2026-06-05.
- When a full System Review runs, add a Review log row and reset "Last full System Review" + "Next review due".
