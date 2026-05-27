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

- **Status**: Resolved — Killed (2026-05-27, untested / superseded). Moved to `resolved.md`.
- **Summary**: 9 weeks untested (the Bertrand-alignment + PLG-consolidation test never ran); no evidence beyond the original three signals. The EH thesis has since evolved (2026-05-22) to "EH = the selection + consistency layer in the distributed-harness model," which absorbs and supersedes the hero-surface bet — preserved in `ai-product/` "Selection and Cross-Surface Consistency Are a PM Mandate." Killed as untested-and-superseded, not contradicted.

## H-006: Agent Adoption Failure Is Primarily a Trigger Problem, Not a Friction Problem

- **Status**: Resolved — Killed (2026-05-27, untested). Moved to `resolved.md`.
- **Summary**: Genuinely testable, but the designated first test (Greg Klebus 1:1 user interviews) never ran in 7 weeks, and the "3 evidence-for" were one session (Apoorva / Loni, H2-Prelim April 10) = a single independent observation, not three. Killed as untested rather than carried indefinitely; the trigger-vs-friction distinction is sound craft and can be revived as a fresh hypothesis if a real adoption test is scheduled.

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
