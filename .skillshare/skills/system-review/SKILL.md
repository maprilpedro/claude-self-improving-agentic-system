---
name: system-review
description: The full monthly System Review for the PM knowledge system — the heavyweight sibling of /consolidate. Runs the five-dimension review the global CLAUDE.md mandates: drift audit, hypothesis lifecycle, decision scoring, quality-criteria pruning, then logs the review and resets the cadence. Use this whenever Pedro says "run a system review", "full system review", "do the review", or when /consolidate or session-start surfaces that a review is due (monthly, 1st of month, co-located with the Promotion Strategy review). This is the deliberate, periodic deep clean — not the per-session /consolidate, and not the read-only staleness-auditor drift report. Pedro triggers it; never run it automatically.
disable-model-invocation: true
---

# System Review

The periodic deep clean of the knowledge system. `/consolidate` runs every session and is light — it captures what just happened and flags drift. The System Review runs monthly and is heavy — it *acts* on the accumulated drift: promotes and kills hypotheses, scores decisions whose outcomes are now known, prunes quality criteria that stopped signaling, and demotes rules that reality contradicted. The point is that compounding only works if the base is periodically cleaned; without this, stale rules and untested hypotheses accumulate and the system slowly lies to itself.

This is **not** `/consolidate` (per-session, capture + flag) and **not** the `staleness-auditor` subagent (read-only, reports drift but changes nothing). The System Review *consumes* the auditor's report and makes the edits Pedro approves.

Cadence and history live in `.claude/state.md`, never in CLAUDE.md (per the global CLAUDE.md "System Review" rule). Read that file first.

## Step 0 — Confirm the review is actually due, and load the open decisions

Read `.claude/state.md`. Check:

- **Last full System Review** date and **Next review due**. If the next-due date is still in the future and Pedro did not explicitly ask for an off-cycle review, say so and confirm he wants to run it now anyway. A review run too early on a thin base is productivity theater (`feedback_consolidation_without_substance`) — the same honesty bar as `/consolidate` Step 0.
- The **Open hypothesis-lifecycle decisions** table — these are candidates a prior auditor already surfaced and parked for Pedro's call. They are the review's starting worklist.
- The **Parked hypothesis candidates** table — patterns holding for a 2nd/3rd observation. Each gets a verdict this review: promote (threshold met), keep parked (still waiting), or drop (stale by this review).

Then check today's date against the parked/pending dates so nothing silently rolls over.

## Step 1 — Drift audit (spawn `staleness-auditor`)

Spawn the `staleness-auditor` subagent (read-only). It scans both canonical Status & Todo files, project memory, `hypotheses/active.md`, `INDEX.md`, and `decisions/` against today's date, and returns a structured drift report: stale Status sections, hypotheses at the promote/kill threshold, rules to demote, decisions to score, quality-criteria drift, and the cadence check.

Do not re-derive this by hand — the auditor exists so the review starts from a clean, dated inventory instead of an ad-hoc scan. Fold its report in as the worklist for Steps 2-4. If the Obsidian app is not running, the auditor falls back to filesystem reads at the vault path; that is fine.

When the auditor flags a stale Status section, **flag it, do not silently rewrite** (`feedback_refresh_stale_status_sections`) — add a dated staleness note near the top of that section, or surface it in the debrief for Pedro to refresh. The review's job is the knowledge base; the Status files are Pedro's to correct.

## Step 2 — Hypothesis lifecycle (the part that actually moves)

Walk `hypotheses/active.md` plus the auditor's threshold list and the state.md pending/parked tables. Apply the repo's hard gates:

- **Promote** a hypothesis to a knowledge rule at **3+ independent confirmations** (global CLAUDE.md). Move it to `hypotheses/resolved.md` with the evidence and date, *and* write the rule into the right `knowledge/` folder (leadership, ai-product, patterns, etc.). Promotion is not just archiving — the durable rule has to land somewhere it will be read.
- **Kill** a hypothesis that is contradicted, or untested and superseded/deprioritized with no decision riding on it. Move to `hypotheses/resolved.md` with the kill reason and date. Never delete (Knowledge Quality Rules).
- **Demote** any `knowledge/` rule the auditor flagged as contradicted back to a hypothesis in `active.md`, with the contradiction cited. A rule that reality broke is a hypothesis again, not a deletion.
- **Parked candidates** — for each, record the verdict in state.md: promoted (with where it landed), still parked (waiting for the Nth observation), or dropped as stale. "Independent" is the bar — two reps of the same event are one observation (the 2026-05-27 review caught this).

Confirmation bar reminder: a *pattern* moving from project memory into `knowledge/` needs **2+ supporting observations**; a *hypothesis* promoting to a *rule* needs **3+ confirmations**. Don't conflate the two.

## Step 3 — Score decisions with knowable outcomes

For each entry the auditor flags in `decisions/` (repo root) whose outcome window has passed:

- Read the decision and its predicted outcome.
- Score it honestly: did the bet hold, partially hold, or miss? What actually happened, and what does that say about the reasoning?
- Append a dated **Outcome** section to the decision file. Don't rewrite the original call — the value is in the before/after.
- If the outcome confirms or breaks a hypothesis, route that back into Step 2.

Decisions without a scoreable predicted-outcome date are noted, not forced. (State.md already tracks which decision is tied to which hypothesis window — e.g. the NYL reactive-ownership decision scored with H-007.)

## Step 4 — Quality-criteria pruning

This is the dimension `/consolidate` skips. Look for signal that stopped signaling:

- **Priority-symbol inflation** — too many 🔴 means triage broke, not that everything is urgent (`feedback_overwhelm_calibration`). Flag for re-triage.
- **Roll-up divergence** — KR notes drifting from Status roll-ups; Status files acting as task trackers instead of roll-ups (`feedback_status_rollup_not_tracker`).
- **Terminology drift** — locked terms slipping (e.g. "Tool Calls" not "invocations" / "interactions", per `reference_mcp_terminology`).
- **Stale or duplicate knowledge** — outdated entries, naming inconsistencies, parked candidates scattered instead of centralized. Mark outdated entries as outdated *with reasoning* — never delete (Knowledge Quality Rules).
- **Index hygiene** — `INDEX.md` folder counts matching reality, Access Log contiguous, no orphaned hypothesis IDs.

Fix what is mechanical and safe (counts, naming, centralizing). Flag what needs Pedro's judgment (re-triage, roll-up reconciliation). Don't silently rewrite his Status priorities.

## Step 5 — Regenerate the dashboard

Run `python3 scripts/consolidation_dashboard.py`. It rebuilds `consolidation-dashboard.html` from repo data only (git log over `knowledge/` + `.claude/memory/`, INDEX inventory, hypotheses, memory files). Generated, never hand-maintained; the html is gitignored, the generator is committed. After a review that moved hypotheses, the active/resolved counts and the commit-prefix mix should visibly shift — that shift is the review's receipt.

## Step 6 — Log the review and reset the cadence

In `.claude/state.md`:

1. Add a **Review log** row: date, scope (what accumulated since the last review), and a tight outcome summary (hypotheses promoted/killed, decisions scored, drift fixed, quality fixes).
2. Reset **Last full System Review** to today and **Next review due** to the next 1st-of-month (co-located with the Promotion Strategy review).
3. Update the **Open hypothesis-lifecycle decisions** and **Parked hypothesis candidates** tables to reflect this review's verdicts — clear what resolved, carry forward what is still pending.

This is what makes the next review (and the next session-start cadence check) start from truth instead of a guess.

## Step 7 — Debrief, summarize, commit

1. **Debrief asks** — the specific things only Pedro can answer that a dimension surfaced (e.g. "this decision's outcome isn't knowable yet — when will it be?", "this 🔴 cluster needs your re-triage"). Short, pointed.
2. **Change summary** (`feedback_document_updates`) — what promoted, what got killed, what decisions scored and how they landed, what quality criteria you pruned, what you flagged for Pedro. Skimmable, with 🔴/🟢 carry-forward called out. Lead with the verdicts, not the process.
3. **Commit** (`Commit Rule`) — stage `knowledge/`, `.claude/memory/`, `.claude/state.md`, and `decisions/`. Use `rtk git`. Prefix: `hypothesis:` if the review was dominated by lifecycle moves, else `learn:`; `note:` only if it was pure hygiene. End with the Co-Authored-By trailer. **Never push** (auth-blocked).

## What success looks like

The drift the auditor found got *acted on*, not just re-reported. Every hypothesis at threshold earned a verdict with evidence. Decisions whose outcomes are knowable got scored honestly, win or miss. Quality criteria that stopped signaling got pruned or flagged. The dashboard counts moved. `.claude/state.md` shows today as the last review and the next date set. Nothing was deleted — superseded, demoted, or killed-with-reasoning instead. The next `recall` and the next `/consolidate` start from a base that tells the truth.
