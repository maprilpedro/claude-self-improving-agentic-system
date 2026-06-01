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
  - **2026-06-01 — first tracked reactive SUCCESS rep.** #aem-agents thread: Ian Boston tagged Pedro + Bertrand directly for PM guidance (*"you may have some guidance from a PM pov"*) on the Experience-Workspace-vs-alignment question, with Bertrand OOO (handed Pedro the pen) and Loni in town. Reactive trigger (someone else raised it, VP-visible). Pedro's posted first reply led with an ownership-framed PM synthesis (common-foundation position + "Happy to help pull that together with you and Ian"), NOT a data-dump or branching question. Per the test's classification = **reactive ownership rep SUCCESS.** Contrast with the May 7 NYL miss. Caveat: Pedro iterated the draft heavily before posting (not a cold real-time reply), so it tests the *output* muscle more than the *real-time recognition* muscle — partial evidence on the reactive thesis.
- **Evidence against**:
  - Single-instance evidence so far. May 7 NYL could be capacity-related (deck week, multiple May 8 deliverables) rather than reactive-vs-proactive structural difference. Further reps needed.
  - The 2026-06-01 success rep was draft-iterated, not cold — so the reactive *miss* (NYL) and reactive *success* (June 1) differ in prep time, not just direction. Weakens a clean proactive-vs-reactive read; the real variable may be prep/time-pressure, not direction.
- **Implications if confirmed**:
  - Senior Director coaching framework should explicitly separate proactive and reactive rep tracking. Telling someone to "ship more" doesn't address reactive misses.
  - The "MOC-First Ship" pattern (proactive) needs a companion **"First-Reply Ownership Sentence"** discipline (reactive). Both require building. Conflating them as one "broadcast frequency" muscle hides the gap.
  - Rep counting should weight reactive reps higher than proactive reps when calibrating progress toward Senior Director — they're rarer and harder.
- **Implications if disconfirmed**:
  - The single broadcast/strategic-comms muscle hypothesis (H-003) holds and reactive vs proactive is just task-flavor variance.
  - Coaching can stay simpler: ship more, broadcast more, stop the data-instinct in all situations.
- **Next step**: Track proactive vs reactive ownership reps explicitly for 4 weeks starting 2026-05-08. Use Status & Todo tracking. Reassess hypothesis 2026-06-05.
