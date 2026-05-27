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
| H-003 — Senior Director visibility = communication not performance | RESOLVED | ✅ **Promoted 2026-05-27** → leadership/ "The Director→Senior Director Gap Is a Communication/Visibility Gap". Confirmed (4 evidence-for + self-diagnosis + Ian-thread, 0 against). In resolved.md. |
| H-001 — 10-minute attention drop | RESOLVED | ✅ **Killed 2026-05-27** (untested/deprioritized) → resolved.md. No field test in 2+ months, no decision riding on it. |
| H-002 — pictures 6.5x recall | RESOLVED | ✅ **Killed 2026-05-27** (untested/deprioritized) → resolved.md. Same pattern as H-001. |
| H-007 — reactive vs proactive ownership | Proposed 2026-05-08; single instance (NYL) | Reassess **2026-06-05** (4-week window). Tracking mechanism currently inactive — log interim reps in Status files |

## Notes

- `decisions/` entries carry no scoreable predicted-outcome dates; NYL reactive-ownership decision is scored with H-007 on 2026-06-05.
- 2026-05-27 consolidation (not a full review): `ai-product/` +4 entries (Distributed-Harness Architecture — everything-is-a-skill, moat=data-not-mechanism, selection+consistency PM mandate, token-cost hierarchy); leadership Forum-entry outcome-confirmed (Ian shipped NorthStar + Saar escalation); H-003 evidence added. **Full System Review still due — co-schedule with Promotion Strategy review 2026-06-01.**
- When a full System Review runs, add a Review log row and reset "Last full System Review" + "Next review due".
