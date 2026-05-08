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

- **Status**: Proposed
- **Date proposed**: 2026-03-19
- **Category**: User Behavior
- **Source signal**: John Medina's research cited in Gallo's *Presentation Secrets of Steve Jobs*. Peer-reviewed studies and Medina's own classroom observations both show the 10-minute mark as a consistent attention drop-off.
- **Hypothesis**: "We believe that audience engagement drops sharply at 10 minutes regardless of speaker quality, because the brain follows stubborn timing patterns. We can test this by tracking engagement signals (questions, eye contact, device usage) in our own presentations and meetings."
- **Test design**: In the next 5 presentations/meetings, introduce a deliberate shift (demo, story, question, new speaker) at the 10-minute mark. Compare audience engagement (questions asked, follow-up actions) with past presentations that didn't have this structure.
- **Evidence for**:
  - Medina's peer-reviewed research, cited in *Brain Rules* (2026-03-19, Gallo)
  - Jobs never exceeded 10 minutes without a shift: demo, video, guest speaker
  - Medina's classroom observation: students always say "10 minutes" when asked when they check out
- **Evidence against**:
  - (none yet)
- **Next step**: Apply the 10-minute rule in next presentation and observe results

## H-002: Pictures Produce 6.5x Better Recall Than Text Alone

- **Status**: Proposed
- **Date proposed**: 2026-03-19
- **Category**: User Behavior
- **Source signal**: Richard Mayer's multimedia learning research, cited in Gallo. 10% recall for oral-only after 72 hours. 65% if you add a picture.
- **Hypothesis**: "We believe that replacing text-heavy slides with image-rich slides in product reviews will produce measurably better stakeholder recall of key points, because visual and verbal information are processed in separate cognitive channels."
- **Test design**: Do an A/B comparison: present the same product update to two similar stakeholder groups. Group A gets traditional bullet-point slides. Group B gets image-rich slides with the same verbal content. Follow up 48 hours later to test recall of key points.
- **Evidence for**:
  - Mayer's experiments across multiple studies (2026-03-19, Gallo)
  - Jobs's image-heavy slides consistently produced more media coverage and audience recall than competitors' text-heavy approaches
- **Evidence against**:
  - (none yet)
- **Next step**: Design a controlled comparison for the next product review cycle

## H-003: The Senior Director Visibility Gap Is a Communication Problem, Not a Performance Problem

- **Status**: Proposed
- **Date proposed**: 2026-03-19
- **Category**: Strategy
- **Source signal**: User's self-identified gap is visibility and self-promotion. Gallo's book repeatedly demonstrates that equally capable people are perceived dramatically differently based on how they present ideas. The AT&T CEO (Sigman) had 42 years of success but was destroyed by one bad presentation next to Jobs.
- **Hypothesis**: "We believe that the difference between Director and Senior Director is primarily a communication/visibility gap, not a capability gap, because leadership perception is driven 63-90% by delivery (body language + vocal) rather than content (Mehrabian research). We can test this by systematically applying Jobs's techniques to stakeholder communications and tracking perception shifts."
- **Test design**: Apply three specific techniques from this book (Headline Technique, Rule of Three, Holy Shit Moment) to the next three high-visibility presentations. Track: (1) Whether the headline gets repeated by others, (2) Whether stakeholders recall the three key points, (3) Whether the presentation generates follow-up conversations.
- **Evidence for**:
  - Mehrabian's research: nonverbal cues (body language, tone) account for 63-90% of impression
  - Jobs's charisma was learned, not innate. He deliberately improved over 30+ years.
  - Sigman (42 years of AT&T leadership) was perceived as incompetent after one bad presentation
  - Buckingham: "Great leaders rally people to a better future." This is a communication skill.
- **Evidence against**:
  - (none yet, hypothesis is fresh)
- **Supporting observation (2026-04-02)**: Pedro self-diagnosed two linked behavioral patterns — execution bias and validation-seeking — both of which are expressions of the visibility gap hypothesis. The execution bias (defaulting to solving rather than framing) keeps him perceived as operational. The validation-seeking (measuring value by what he produces rather than what he influences) makes him dependent on external confirmation rather than positional authority. Both are communication/positioning problems, not capability problems. This confirms the hypothesis at the behavioral root level, not just the presentation level.
- **Next step**: Select the next high-visibility presentation and apply the three techniques. Document results.

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
