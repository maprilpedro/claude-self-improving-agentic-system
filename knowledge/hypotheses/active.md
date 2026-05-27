# Active Hypotheses

> PM hypotheses currently being tested. Move to `resolved.md` once confirmed or killed.

## Lifecycle

```
Observe signal --> Propose hypothesis --> Design test --> Collect evidence --> Resolve
```

## Status Key
- **Proposed**: Hypothesis stated, not yet tested
- **Testing**: Actively gathering evidence
- **Ready to resolve**: Enough evidence to decide

## H-001: Audiences Disengage at Exactly 10 Minutes

- **Status**: Resolved — Killed (2026-05-27, untested / deprioritized). Moved to `resolved.md`.
- **Summary**: Literature-only (Medina / Gallo); the field test (shift at the 10-minute mark across 5 presentations) was never run in 2+ months, and no decision rode on it. The actionable craft (build in a shift / demo / question periodically) is already absorbed into presentation practice (`tools/`). Retired to keep the active set meaningful, not contradicted.

## H-002: Pictures Produce 6.5x Better Recall Than Text Alone

- **Status**: Resolved — Killed (2026-05-27, untested / deprioritized). Moved to `resolved.md`.
- **Summary**: Literature-only (Mayer / Gallo); the A/B recall test was never run, and no decision gated on it. Image-rich-over-text is already standard practice (PPTX template + palette conventions). Retired, not contradicted.

## H-003: The Senior Director Visibility Gap Is a Communication Problem, Not a Performance Problem

- **Status**: Resolved — Confirmed + Promoted (2026-05-27). Moved to `resolved.md`; promoted to a `leadership/` rule.
- **Summary**: 4 evidence-for + behavioral self-diagnosis (2026-04-02) + 2026-05 Ian-thread evidence (a well-placed *question* moved Ian to ship the NorthStar next day + escalate memory ownership to Saar VP — influence via communication, not delivery), 0 against over ~2 months. Cross-confirmed by resolved [[H-005]]. Promoted to leadership/ "The Director→Senior Director Gap Is a Communication/Visibility Gap, Not a Capability Gap." Companion open hypothesis: H-007 (reactive vs proactive ownership, reassess 2026-06-05).

## H-004: Naming a Hero Surface and Backing It with PLG Investment Will Measurably Improve Feature Discovery

- **Status**: Proposed
- **Date proposed**: 2026-03-26
- **Category**: AI Product / Platform Strategy
- **Source signal**: Loni's hero surfaces concept (Session IV, March 26). Current state: AEM users reach the product through 4+ entry points with no PLG investment focused on any one of them. Adoption reviews show slow feature discovery and high bounce rates.
- **Hypothesis**: "We believe that naming Experience Hub as the canonical hero surface and concentrating PLG investment (nudges, announcements, onboarding flows, agent prompt discovery) on that single surface will measurably improve feature discovery rates and adoption cohort retention, because compounding PLG investment in one place produces more signal and more habit than diluted investment across many surfaces."
- **Test design**: Define Experience Hub as hero surface (get Bertrand + Loni alignment). Consolidate next three PLG experiments to run through Experience Hub only. Compare adoption cohort metrics (CTR, return visits, feature activation) to prior period when experiments were distributed.
- **Evidence for**:
  - Steve Jobs / Apple concentrated all marketing on a small number of hero products and hero stores — retail became a Times Square for Apple's brand
  - Loni's explicit framing: identify hero surfaces to monitor, promote, and run PLG on
  - Experience Hub A/B test (SIMPLE variant, Nov 2025): 17.9% vs 0.36% CTR — focused PLG experiment on one surface produced clear signal
- **Evidence against**:
  - (none yet)
- **Next step**: Get Bertrand validation on hero surfaces one-pager. Then bring to Loni's next session.

## H-006: Agent Adoption Failure Is Primarily a Trigger Problem, Not a Friction Problem

- **Status**: Proposed
- **Date proposed**: 2026-04-10
- **Category**: AI Product / Adoption
- **Source signal**: Apoorva Gupta (H2 Prelim Part 3, April 2026) — Content Optimization Agent and DM Templates both have near-zero adoption despite reduced friction. Loni Stark's "sensor + hero" framing in the same session.
- **Hypothesis**: "We believe that low adoption of AI agent features is more often caused by users not knowing they have a problem worth solving (trigger failure) than by the feature being too hard to use (friction failure). Fixing the UX before fixing the trigger is wasted investment."
- **Test design**: For any AEM agent with <5% adoption despite UX simplification, interview 5 users. Ask: did you know this feature existed? Did you have a moment in the last month where you needed this but didn't use it? What triggered you to try it (if ever)? Classify responses as trigger failure (never knew or never felt the need) vs friction failure (knew, tried, gave up). If >60% of non-adopters are trigger failures, hypothesis is confirmed.
- **Evidence for**:
  - Content Optimization Agent: simplified rendition creation, still negligible adoption (Apoorva, April 2026)
  - DM Templates: 14 months near-zero adoption despite refreshed editor (Apoorva, April 2026)
  - Loni: "How does a human get the aha moment without even having to invoke any agent?" — framing the problem as trigger-first
- **Evidence against**:
  - (none yet)
- **Next step**: Use Greg Klebus 1:1 as first test. Ask: who is using Content Optimization Agent? What triggered their first use? What blocks non-adopters?

## H-005: Owning Cross-Agent Measurement Standardization Creates Structural Cross-Org Influence for the Experience Hub PM

- **Status**: Resolved — Confirmed (2026-05-03). Moved to `resolved.md`.
- **Summary of resolution**: Cross-org influence accrued to Pedro through ownership of the data substrate even before any literal "standard" shipped. Public naming as AEM-AO liaison (April 14), peer-team voluntary consolidation by Varun (April 22), three-tier reporting architecture locked with Pedro owning the middle tier (May 1), and Portfolio Monthly Briefing v0 shipped (April 30) collectively confirm the spirit-of-hypothesis prediction. See `resolved.md` for full evidence.

## H-007: Reactive Ownership Is a Harder Muscle Than Proactive Ownership

- **Status**: Proposed
- **Date proposed**: 2026-05-08
- **Category**: Senior Director Behaviors / Self-Diagnosis
- **Source signal**: Pedro NYL TBYB thread May 7, 2026. After 3 successful proactive-ownership reps in one week (Briefing v0 ✅, AOv2 5-phase plan ✅, MCP MOC ✅), Pedro reverted to data-instinct on a reactive thread (account team escalation). First reply was data-only (URLs + "I'm not aware of other way") instead of ownership-led. Corey's "broken process alert" was triggered by Pedro's reply. Bertrand had to assign explicitly: *"@Pedro @Yanira can you please take the lead here?"* Pedro's self-observation post-thread: *"je me sens mal d'avoir loupé le framing initial."*
- **Hypothesis**: "We believe that for execution-strong PMs building toward Senior Director, **reactive ownership** (responding when a thread / problem / customer escalation lands on them) is a structurally harder muscle to build than **proactive ownership** (shipping artifacts unprompted to senior leaders). The proactive muscle is in the writer's control — they choose timing, audience, and shape. The reactive muscle requires real-time recognition that a moment-of-truth has arrived AND override of the data-instinct AND production of an ownership sentence under time pressure. We can test this by tracking proactive vs reactive ownership reps separately over 4-6 weeks and comparing failure rates."
- **Test design**:
  - For 6 weeks, track every Slack/email reply Pedro sends on threads with (a) a customer name, (b) a VP-level person, (c) a process/ownership question.
  - Classify each reply as: **proactive ownership rep** (Pedro shipped/raised the topic), **reactive ownership rep success** (someone else raised it, Pedro included a literal ownership sentence in first reply), or **reactive ownership rep miss** (data-dump, deflection, branching question without ownership).
  - Compare with the same period's proactive reps (count of MOC-first ships acked by leaders).
  - Hypothesis confirms if reactive miss-rate is meaningfully higher than proactive miss-rate (proactive miss = no ack, reactive miss = no ownership sentence in first reply). Hypothesis disconfirmed if reactive and proactive miss-rates converge — meaning the muscle is the same in both directions.
- **Evidence for**:
  - **NYL May 7, 2026** — clearest single-instance evidence. After 3 successful proactive reps in 7 days, Pedro reverted to data-instinct on the first reactive thread. The ratio (3 proactive successes / 0 misses : 1 reactive miss / 0 successes) is small-N but suggestive.
  - Pedro's self-named gap from May 1 (*"bias for delivery and poor strategic communication skills"*) is consistent with the hypothesis — delivery is proactive (he chooses); strategic communication on incoming threads is reactive (he must read situation in real time).
  - Decision Journal entry `decisions/2026-05-07-nyl-thread-version-c-reactive-ownership-rep.md` — explicit acknowledgment that reactive moment was harder than the prior proactive moments.
- **Evidence against**:
  - Single-instance evidence so far. May 7 NYL could be capacity-related (deck week, multiple May 8 deliverables) rather than reactive-vs-proactive structural difference. Further reps needed.
- **Implications if confirmed**:
  - Senior Director coaching framework should explicitly separate proactive and reactive rep tracking. Telling someone to "ship more" doesn't address reactive misses.
  - The "MOC-First Ship" pattern (proactive) needs a companion **"First-Reply Ownership Sentence"** discipline (reactive). Both require building. Conflating them as one "broadcast frequency" muscle hides the gap.
  - Rep counting should weight reactive reps higher than proactive reps when calibrating progress toward Senior Director — they're rarer and harder.
- **Implications if disconfirmed**:
  - The single broadcast/strategic-comms muscle hypothesis (H-003) holds and reactive vs proactive is just task-flavor variance.
  - Coaching can stay simpler: ship more, broadcast more, stop the data-instinct in all situations.
- **Next step**: Track proactive vs reactive ownership reps explicitly for 4 weeks starting 2026-05-08. Use Status & Todo tracking. Reassess hypothesis 2026-06-05.
