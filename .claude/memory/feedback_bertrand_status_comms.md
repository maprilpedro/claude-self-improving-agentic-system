---
name: feedback_bertrand_status_comms
description: How Bertrand wants a leadership/team status update shaped — lead with a concrete win, trim table detail, explain provisioning-type mechanisms in plain terms, show what's moving (bug-bash status) over abstract ETAs.
metadata:
  type: feedback
---

On the 2026-07-21 "AEM Agents on Coworker — Status" running note (goes to agent teams + leadership incl. Saar), Bertrand's review asked for three cuts:

- **Trim detail from the migration/cohort table.** The "185 → 177 → 174; Ulta coming-soon; Superloop opted out" trail was too much for a leadership table. Keep the headline number, drop the trail.
- **Rewrite provisioning concretely — say what it actually means.** Not the jargon ("segment in git, flip the flag") but the plain mechanism: two things must be true (agents are already on by default; Coworker access is a manual per-org git allow-list + a feature-flag flip that does not scale to ~2,600).
- **Per-agent table: show what is moving, not a column of "TBD".** Drop the Manifest column and the abstract "Production Readiness / ETA" column; replace with bug-bash status (EPA done, EDA + Governance targeted).

**Why:** for a status leadership reads, Bertrand wants concrete movement and plain meaning, not exhaustive provenance. The receipts/audit trail belong in Pedro's private scaffolding, not the sent body. Same instinct as [[feedback_bertrand_concrete_first]].

**How to apply:** when shaping a status Bertrand will see, lead with a concrete win, keep tables to what changed this period, explain mechanisms in plain words, and keep the source/audit trail in a separate for-Pedro section. Links: [[feedback_bertrand_concrete_first]], [[feedback_separate_facts_from_proposals]], [[feedback_status_rollup_not_tracker]].
