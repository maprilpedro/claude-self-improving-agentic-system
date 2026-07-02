# Calibration Audit — When a Priority List Stops Signaling

_Section: Artifact Architecture — part of `patterns/`; router = README.md._
- **Source**: Pedro session, April 24, 2026
- **Date**: 2026-04-24
- **Observation**: Pedro's Status file had 12 items tagged 🔴 out of ~25 total. 🔴 had drifted from "highest-priority this week" to "still active" — which meant 🔴 no longer signaled anything. The symbol had lost its meaning. Same risk applies to any prioritization symbol (P0, high, starred, urgent) that is never pruned.
- **Pattern**: Priority symbols only work if they cost something to assign. When everything qualifies, nothing does. The calibration audit is periodic — count how many items carry the top label. If the count is more than ~5, the label has drifted and needs a rebalance. Demote or re-assign. The discipline is not to remove urgent items but to make "urgent" mean "top of mind, action this week" consistently.
- **Design rule**: Cap the top-priority label at a small number (4-5 for a Director roll-up). Anything beyond that cap is either miscoded or signals a capacity crisis. Either way, the audit surfaces it rather than letting the list silently grow.
- **When it applies**: Any tracking system where a priority label is meant to filter attention. Status files, JIRA boards, sprint planning, engineering dashboards.
- **When it fails**: If the cap is held mechanically rather than based on actual load-bearing-ness, important work gets artificially demoted. The cap is a calibration tool, not a quota — use judgment about what belongs above the line, then prune below.
