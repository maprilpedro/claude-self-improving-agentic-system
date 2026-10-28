---
name: release-management-project-context
description: "Release Management, one of Pedro's four projects since 2026-10-28 — release activation and reviews, customer update pauses (Quiet Hours, Update-Free, RO), Rotary, Visual Regressions / Fred, the H1'27 release item. Sisters project_aem_agents_intelligence.md (Coworker Lead), project_experience_hub.md, project_security_health.md."
metadata:
  type: project
---

> **🗂️ Created 2026-10-28** when Pedro set his four projects ("J'ai 4 projects principaux : Coworker lead, Experience Hub, Release Management et Security Health"). Release work used to sit EH-side (and a few asks in the AAI Status). Vault: `2026/Release Management/` with `Release Management - Status and Todo.md` and `🎯 Release Management MOC.md`. Sisters: [[project_aem_agents_intelligence]] (Coworker Lead), [[project_experience_hub]], [[project_security_health]].
>
> **Layout invariant (same as the other project files):** dated event blocks go directly under the RESUME, above the first `## ` reference section, or `scripts/archive_memory.py` cannot see them.

> ## ▶️ RESUME HERE — **2026-10-28:** RBI escalation answered (block below), customer call **Tue 11-03**. Four customers hit the same pause limits in two weeks, a policy question still open. Release activation handed to Victor Mirica 10-27. SKYOPS-163976 (H1'27, "HC: TBD") to explain to Bertrand and 5 HC to ask Nicu. Overdue from the Coworker Status: Razvan's UnderArmour / Best Buy ask (10-14), Tatyana's January review date (10-16), UPS RO-pause ticket (10-27). Tasks in the vault Status; watches in [[watches]] (Release Management section).
>
> ## ▶️ 🔴 2026-10-28 — RBI ESCALATION: THREE WEEKS OF PM SILENCE ON A RENEWAL-AT-RISK THREAD, PEDRO ANSWERED WITH THE UPDATE-FREE EXTENSION (moved here verbatim from [[project_experience_hub]] the same day)
> - **Source.** Email thread "RBI <> Adobe - Follow up meeting", pasted by Pedro 10-28. RBI = Raiffeisen Bank International (customer contact Pablo Cejas Romanelli). Account team: Patrick Hauzel (Account Manager FSI), Martin Floess, Markus Rogger (Sr Manager Enterprise Sales FSI). Giovanni Sarbia (Senior Cloud SME), Vlad Bailescu (EM Sites), Bertrand, Razvan (added by Bertrand 10-23).
> - **The ask.** RBI wants AEM updates at their own pace, monthly (discussed with Pedro 09-08), for regulatory reasons. Flagged ~6 months ago, escalated early September. Sales chased PM six times 10-07 → 10-20. Patrick 10-20: renewal and the AEM Cloud extension next year at risk. Giovanni 10-22: a possible slower-cadence SKU ("only Product Management can comment on or commit"); another RBI entity weighs on-prem → AEMaaCS next year; RBI is off RO again for a separate issue; his data says manual updates do not reduce regression risk. Vlad: Core Components version cannot be pinned. Next customer call **Tue 11-03**.
> - **Pedro's reply, sent 10-28 ~10:10 CET** (built from his 09:58 draft; which suggested edits he kept is not known): platform health and vulnerability fixes first; Update-Free extension for selected customers, 3 × 1 week → 10+ × 1 week per year; guardrail max 2-3 releases behind; interim monthly manual updates. Current limits (Experience League, checked 10-28): 3 Update-Free periods of 7 days per rolling 12 months, Quiet Hours max 8 h.
> - **Same limit, four customers in two weeks.** Norfolk asked 10 h Quiet Hours (Dharani 10-23; Pedro to Nicu 10-22: "Increase Quiet hours to 10h for one customer"). Microsoft (Doug Hicken 10-27 `#internal-aem-microsoft`: "Quiet hours and update free periods simple do not do what we need them to do"). UPS RO pause 11-01 → 01-11. RBI. A policy question, not a per-account reply.
> - **Read.** Release management is the lane Ramon proposed a Bucharest PM take over ([[watches]] CAREER section). A three-week PM silence on a Sales escalation with Bertrand cc'd is evidence for that proposal. Knowledge: [[Say the Sentence That Obliges — the Hedge Transfers the Ask]]. Watch → [[watches]].
> - **Also 10-27.** Pedro told Merit Vossmann (TAM; B. Braun account, inferred from "Congrats for BBraun takeover") that Visual Regressions will be decommissioned "over next months", announcement on the way, "date in around 6 months", and that she may say so to the customer. Her follow-up "what do we recommend using instead ? one of our agents?" was unanswered at 10-28 09:45. Not known whether this is the same tool as Fred-as-a-Service (09-22, "target of 6 months" to Amit Gupta). https://adobe.enterprise.slack.com/archives/D0CBFJ858TD/p1793110852430919

## Scope and roadmap

- **Pedro's role.** The H2'26 canvas investment table names him PM of CFRO (Release Mgmt, Content AI, LLMO DRS, LLM Apps, Repo Service) under Razvan, with two other PMs, 58 HC ([[project_experience_hub]] 2026-10-22 block). On 10-27 he told Bertrand his top-level items besides Coworker are Release Management (Razvan) and EH.
- **H1'27.** SKYOPS-163976 Release Management Scalability + SKYOPS-163977 AI transformations of Rotary release tools, both "HC: TBD"; Bertrand 10-27: "sans que je sache trop ce que ça veut dire". H2'26 lines were SKYOPS-136515 (5 HC) and SKYOPS-136517 (8 HC). EDA breaking changes: AEMAGT-1282 (H2'26, RS 2) → AEMAGT-2920 (H1'27, "RS: ?"). Canvas https://adobe.enterprise.slack.com/docs/T025FJ55H/F0C5A1D4GAJ
- **OKRs.** O3 Release Management Agentification (Visual Comparison), O4 Ship Quiet Hours (incl. UPF paid extension), O6 Aging Customers Cleanup ([[reference_okr_structure]]).

## Operations

- **Release activation** (last Thursday of the month, 17:00 CET): Victor Mirica (`vmirica`, Rolling Stones) runs it since 2026-10-27, Pedro in the loop. Chain roughly Nicu Melcioiu (manager), Razvan. Pedro's choice to free operational time, not a scope transfer ([[project_aem_agents_intelligence]] 2026-10-27 Bertrand block).
- **Release reviews.** Tatyana asks for the dates; Nicu Melcioiu owns the calendar. Nov 2026.11 → 11/19 and Dec 2026.12 → 12/10 sent 10-12; January still owed.
- **Rotary calendar.** Nicu updated it 09-16 (Vlad Bailescu's `uber-release-registry` ask). Assets code freeze 09-29, URR authoritative.
- **Customer pause limits.** 3 Update-Free periods of 7 days per rolling 12 months, Quiet Hours max 8 h (Experience League, 10-28). RO pause on request (wiki "Pause Updates for a program in RO", https://wiki.corp.adobe.com/spaces/WEM/pages/1971265640).

## Decommissions Pedro has announced

- **Fred-as-a-Service:** to Amit Gupta 2026-09-22, "progressively de-commission… target of 6 months". First time on record.
- **Visual Regressions:** to Merit Vossmann 2026-10-27, "date in around 6 months". Same tool as Fred or not: not confirmed. Check the two dates stay consistent with anything said to Nicu or customers.

## Carried from EH memory (May 2026, status not re-checked)

- **Quiet Hours Update via Agents beta:** 81 customers (prior Quiet Hours Update users ∩ AI-enabled), free via the chatbot. O4 proof point (EH memory, May 12 Bertrand 1-1).
- **Breaking-changes manager rename:** the Raspberry team finds "breaking changes" too negative; the central-repo concept stays (~120 customers).
- **O6 aging customers:** ~120 behind (~100 still), Aldi (7-8 programs), Volkswagen, Americans; manual update first, then automatic; 1-year window option.

## Scope risk

- Ramon proposed in writing that a Bucharest PM take over the release track. It sits in a record Bertrand reads. Decide before the mid-year review whether to defend it or trade it ([[watches]] CAREER section).

## People

Razvan · Nicu Melcioiu · Victor Mirica · Vlad Bailescu (EM Sites) · Giovanni Sarbia (Senior Cloud SME) · Tatyana (release reviews) · Dustin Christensen (UPS RO pause) · Merit Vossmann (TAM, B. Braun).
