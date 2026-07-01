## Decision: Continue with Felix's reporting pipeline despite confirmed compliance risks

## Context
Ian Boston confirmed two legal risks with Felix's cross-region aggregation pipeline on April 1, 2026: (1) data residency contractual breach — aggregating across regions (VA, NLD2, AUS5, CAN2, GBRS, IND1) violates residency requirements for a subset of customers; (2) data governance deposition risk — datasets not registered in the Data Governance Catalog. Pedro escalated to Bertrand with Ian's full response and a proposed path (scope blast radius, accelerate DAS compliant infrastructure). Bertrand also suggested anonymization; Ian confirmed it does not resolve residency.

## Alternatives considered
1. Scope the blast radius and filter IMS Orgs with residency requirements
2. Accelerate DAS to build a compliant aggregation layer using Felix's pipeline as the spec
3. Run per-region reports only (loses aggregate view)
4. Stop the pipeline until compliant infrastructure is in place

## Reasoning
Bertrand's call: "Ian's comments are important but not critical. We continue with Felix." The aggregate view has operational value for the reporting program and Bertrand judged the risk acceptable at this stage.

## Trade-offs accepted
Known compliance risks remain open. If someone outside AEM BU flags this, the pipeline could be shut down and AEM could lose autonomy over prompt data handling (Ian's warning). The decision to continue is a calculated risk accepted by Bertrand.

## Decision owner
Bertrand de Coatpont (Senior Director PM). Pedro escalated with evidence and a proposed path on April 1. The decision belongs to Bertrand, not Pedro.

## Supersedes
Nothing prior on this topic.

## Outcome (scored 2026-05-27 — first System Review)
Risk accepted, **not yet triggered** (8 weeks on). Felix's pipeline is still LIVE and VP-sponsored (migrating SQLite→Postgres + LLM-as-Judge; engineers connected). No external-BU flag has shut it down — Bertrand's calculated risk has held to date. **New adjacent compliance vector emerged independently:** ISO 42001 / Tech GRC audit (Robert Guthrie, May 4), evidence due July 17, scope since narrowed to Discovery + Governance only. Not the residency risk Ian named, but the same compliance surface — the bet's downside is now partly materializing through a different door. **Score: correct to date; keep watching the residency vector + ISO-42001 audit. Re-score next review.**

## Outcome checkpoint (2026-07-01 — System Review, score-lite)

Bet still holds: Felix's pipeline is live, VP-sponsored, no external-BU flag has shut it down (~13 weeks). The residency vector never triggered. **But the decisive re-score data is not here yet — the ISO-42001 / Tech GRC audit evidence is due 2026-07-17** (audit narrowed to Discovery + Governance). Defer the definitive re-score to 07-17. **New frame this review:** the pipeline's relevance is now sunsetting for a *different* reason than the one this decision guarded against — not a compliance shutdown, but the **Rubin/Coworker substrate migration** (see new [[H-009]]). So the compliance bet held; the pipeline itself is depreciating via platform migration. Re-score at 07-17 on the audit outcome.
