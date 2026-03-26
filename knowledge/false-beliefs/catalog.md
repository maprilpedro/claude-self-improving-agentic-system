# False Beliefs Catalog

> PM conventional wisdom that's wrong or misleading. Each entry needs evidence.

## Why This Matters

Product management is full of axioms that sound right but don't hold up under scrutiny.
Cataloging these prevents repeating industry-wide mistakes.

## Rating Scale
- **Dangerous**: Actively harmful if believed
- **Misleading**: Points in the wrong direction
- **Nuanced**: True in some contexts, false in others
- **Outdated**: Was true, no longer is

## FB-001: "More slides with more detail = better presentation"

- **Rating**: Dangerous
- **Date cataloged**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 8; Dr. Richard Mayer's multimedia learning research; John Medina's *Brain Rules*
- **Why people believe it**: Feels thorough. Feels like you're giving the audience everything they need. PowerPoint's default template encourages it.
- **Evidence against**:
  - Mayer's research: adding redundant or irrelevant information impedes learning (coherence principle)
  - Average PowerPoint slide has 40 words. Jobs's first four slides at Macworld 2008 had 7 words total
  - Picture superiority effect: 10% recall for text after 72 hours vs 65% for text + pictures
  - Medina: "The brain is fundamentally a lazy piece of meat" that doesn't want to waste energy processing cluttered slides
- **What's actually true**: Simpler slides with fewer words and more images produce dramatically better recall, engagement, and persuasion. One theme per slide. Pictures > words.
- **Nuance**: Detailed slides work fine as leave-behind documents. But presentation slides and document slides should never be the same thing.
- **Implication**: Strip your slides bare. If it has bullet points, it's a document, not a presentation.

## FB-002: "Great presenters are naturals"

- **Rating**: Misleading
- **Date cataloged**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 15; Gladwell's *Outliers*; Ericsson's deliberate practice research
- **Why people believe it**: Jobs looked effortless onstage. It seems like charisma is innate.
- **Evidence against**:
  - Jobs rehearsed for days before keynotes, sometimes spending 4+ hours onstage in rehearsal
  - Apple teams spent hundreds of hours preparing 5-minute demo segments
  - Jobs personally designed slides, obsessed over lighting, and ran multiple full dress rehearsals
  - Jobs's early presentations (1984) were good but noticeably less polished than his 2007 peak
  - Gladwell/Ericsson: 10,000 hours of deliberate practice is required for world-class expertise in anything
  - Churchill practiced so thoroughly he seemed extemporaneous. His granddaughter: "Practice is essential, particularly if you want to sound spontaneous."
- **What's actually true**: Presentation skill is built through thousands of hours of deliberate practice. "Spontaneity" is the result of planned practice. Every great presenter rehearses far more than average ones.
- **Nuance**: Some people have more natural comfort on stage, but the gap between natural and practiced is vastly smaller than the gap between practiced and unpracticed.
- **Implication**: Stop admiring great presenters and start practicing like them. Record yourself. Get feedback. Repeat.

## FB-003: "Data speaks for itself"

- **Rating**: Dangerous
- **Date cataloged**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 9
- **Why people believe it**: Numbers feel objective and authoritative. Presenting raw data seems rigorous.
- **Evidence against**:
  - "5GB" meant nothing to consumers. "1,000 songs in your pocket" changed an industry.
  - "730 million transistors" was meaningless until Intel compared it to fitting all of Europe into Ithaca, NY
  - IBM's petaflop computer got media coverage only after comparing it to "100,000 laptops stacked 1.5 miles high"
  - Apple's 5% market share sounded bad until Jobs compared it to BMW and Mercedes
- **What's actually true**: Numbers need to be specific, relevant, and contextual. Without analogy or comparison, big numbers are just noise. The audience doesn't do the math for you.
- **Nuance**: For deeply technical audiences, raw data has more utility. But even engineers respond better to contextualized numbers.
- **Implication**: Every number in a presentation should be dressed up with context: an analogy, a comparison, or a "what this means to you" translation.

## FB-004: "Complex language signals expertise"

- **Rating**: Dangerous
- **Date cataloged**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 10; Jack Welch's management philosophy; Suze Orman interview
- **Why people believe it**: Sophisticated vocabulary and technical jargon make you sound like an authority.
- **Evidence against**:
  - Jobs vs Gates language analysis: Jobs scored far better on readability. Jobs used 10.5 words per sentence; Gates used 21.6
  - Jack Welch fired a leader who couldn't explain his business simply. "Insecure managers create complexity."
  - Suze Orman: "It's our fear of not being important that leads us to communicate things in a more complex way than we need to."
  - Most press releases fail because they're "self-indulgent, buzzword-filled wastes of time"
  - Plain English Campaign: simpler rewrites consistently improve understanding and action
- **What's actually true**: Simplicity signals mastery. The ability to explain complex ideas simply demonstrates deeper understanding. Einstein: "If you can't explain it simply, you don't understand it well enough."
- **Nuance**: Technical depth is appropriate in technical peer reviews. But for any cross-functional or leadership audience, plain language wins.
- **Implication**: Run your writing through readability tools. Aim for a fog index under 8. If you wouldn't say it to a friend, don't put it in a presentation.

## FB-005: "The product demo should show everything"

- **Rating**: Misleading
- **Date cataloged**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 12; Guy Kawasaki, *The Macintosh Way*
- **Why people believe it**: If the product has many features, showing them all demonstrates value.
- **Evidence against**:
  - Jobs chose to demo 10 of 300 Leopard features. He told the media which features to highlight.
  - Kawasaki's five qualities of a great demo: short, simple, sweet, swift, substantial
  - Jobs's Safari demo lasted under 3 minutes and focused on one thing: speed vs IE
  - When Jobs introduced Safari for Windows, he demoed only speed, nothing else
- **What's actually true**: A demo should be like a movie trailer: show the best parts to tantalize, not the entire film. Focus on one or two differentiating features. Answer "So what?" for each feature shown.
- **Nuance**: Internal demos for engineering teams can be more comprehensive. But customer-facing demos should always be curated.
- **Implication**: Before any demo, ask: "What is the one thing I want them to remember?" Demo that. Cut everything else.

## FB-006: "Agent categories reflect what customers actually want"

- **Rating**: Misleading
- **Date cataloged**: 2026-03-23
- **Source**: Loni Stark, AEM PM Virtual Working Session I (Agents, March 23, 2026)
- **Why people believe it**: PMs spend months naming and structuring agent categories. They feel considered and intentional. Teams organize their work around them.
- **Evidence against**:
  - Loni said explicitly in a senior strategy session: "The seven agent categories are not grounded in customer reality. They reflect PM intuition."
  - Conrad Woltge confirmed from log analysis: most activity looks like systematic exploration by technical users testing capabilities, not productive use by target personas.
  - No documented personas or jobs-to-be-done for any agent existed as of March 2026, despite multiple agents being in market.
  - 1200 real customer questions (held by Corey Dulimba) had not yet been analyzed — the actual design input was sitting unused.
- **What's actually true**: Agent categories emerge from how product orgs are structured and what PMs intuit about their domain. Customer behavior may not map to those categories at all. The only way to know is to analyze real usage data.
- **Implication**: Before any roadmap or surface is built around agent categories, analyze actual usage logs. Let observed behavior reshape the categories.

## FB-007: "High agent failure rate means bad prompts"

- **Rating**: Dangerous
- **Date cataloged**: 2026-03-23
- **Source**: Cedric Huesler confirmation, Loni's Session I (Agents, March 23, 2026). EPA 40-50% failure rate analysis.
- **Why people believe it**: Prompts are visible and editable. Improving them feels like progress. It's accessible work.
- **Evidence against**:
  - Cedric Huesler (AO architect) confirmed that current agents route to a solution — they don't reason through one. This is a structural ceiling, not a prompt quality problem.
  - AO 2.0 adds agent loop reasoning. Until it ships (May-July 2026), prompt improvements cannot move failure rate below the architecture floor.
  - EPA failure rate is dominated by unsupported request types (bulk actions, form creation) and configuration gaps — not prompt phrasing.
- **What's actually true**: Agent failure rate has two components: (1) architecture ceiling (fixed only by AO 2.0), and (2) scope/configuration gaps (fixable by better scoping and onboarding). Prompt quality is a tertiary factor.
- **Implication**: Diagnose before optimizing. Map failures by root cause. Don't burn sprint capacity on prompt tuning if the ceiling is architectural.

## FB-008: "Building a new UI surface solves discovery problems"

- **Rating**: Misleading
- **Date cataloged**: 2026-03-26
- **Source**: Loni's AEM PM Virtual Working Session IV (Surfaces, March 26, 2026). Strong team consensus.
- **Why people believe it**: If users can't find a feature, adding a dedicated surface for it feels like a targeted fix.
- **Evidence against**:
  - Strong team consensus in Session IV: "we cannot keep creating new UIs — we already have too many."
  - AEM users already navigate Experience Hub, Experience Home, Cloud Manager, and direct product URLs. Adding a surface adds a navigation decision, it doesn't remove one.
  - PLG motions can't compound if discovery budget and feature nudges are spread across many surfaces.
  - Customer feedback: "I keep getting to Experience Hub via Experience Home and wonder why I need both?"
- **What's actually true**: A new surface fragments the audience further unless it clearly replaces an existing surface. The solution to discovery problems is better instrumentation and PLG investment on the existing hero surface — not a new surface.
- **Implication**: Default answer to "let's build a new surface" is "does this belong inside the existing hero surface?" New surface requires explicit justification.

## Seed Beliefs to Investigate

> These are commonly held PM beliefs worth examining. Move to entries above once evidence is gathered.

- "Users know what they want"
- "More features = more value"
- "First mover advantage is decisive"
- "Build it and they will come"
- "The customer is always right"
- "Data-driven means following the numbers"
- "MVP means minimum effort"
- "Product-market fit is a moment, not a process"
- "Roadmaps should be commitments"
- "Consensus means alignment"
