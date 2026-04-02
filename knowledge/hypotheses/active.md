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

## H-005: Owning Cross-Agent Measurement Standardization Creates Structural Cross-Org Influence for the Experience Hub PM

- **Status**: Proposed
- **Date proposed**: 2026-03-26
- **Category**: Leadership / Strategy
- **Source signal**: No cross-agent measurement standard exists as of March 2026. Each agent team measures success differently. Bertrand, Conrad, and Loni have all expressed frustration with this. Felix Delval's platform can solve it technically.
- **Hypothesis**: "We believe that the Experience Hub PM owning the cross-agent measurement standard — by driving adoption of a shared TSR/VRR baseline across all agent teams — will create durable cross-org influence, because measurement standards become infrastructure that every team depends on. The owner of the standard gets visibility into every agent's performance and a seat at every agent roadmap conversation."
- **Test design**: Propose the standard (1-page). Validate with Bertrand. Get Conrad/Gilles alignment. Onboard EGA (Philippe) as first new agent on Felix's platform. Track: (1) how many agent teams adopt the standard; (2) whether Pedro is consulted on agent roadmap conversations he wasn't previously in.
- **Evidence for**:
  - Conrad told all agent owners to build equivalent reports to EPA (March 24 Slack). No one has done it yet — the position is open.
  - Bertrand specifically asked for standardized agent dashboards in 1:1 (March 24). Pedro has the tool (Felix's platform) to deliver it.
  - Infrastructure owners have cross-org influence by definition — every team that depends on the infrastructure needs a relationship with the owner.
- **Evidence against**:
  - Felix built the platform — it's his infrastructure. Pedro's role is PM adoption driver, not technical owner. Credit-sharing and positioning matters here.
  - **VRR complexity (2026-03-31)**: Bertrand raised that VRR has 5 tiers and is being collapsed to one number. This means the "shared measurement standard" is more complex than initially framed — TSR and VRR are not flat metrics. The standard needs to specify tier definitions, not just metric names. This is a complication but not a hypothesis killer.
- **Next step**: Get the 5-tier VRR definition from Yanira's wiki. Update Felix's platform to show VRR distribution, not just average. Then the standard is credible. Until then, presenting VRR numbers to Bertrand risks the same correction again.
