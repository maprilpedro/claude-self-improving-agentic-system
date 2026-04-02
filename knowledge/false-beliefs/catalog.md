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

## FB-009: "Being liked is more important than being respected in org politics"

- **Source**: Greene, *The 33 Strategies of War*, Strategy 1: The Polarity Strategy
- **Date**: 2026-04-02
- **Common belief**: To advance in a corporate org, you need to be liked. Avoid antagonizing people. Seek consensus. Don't make enemies.
- **Why it's wrong**: Greene's Thatcher analysis is definitive on this. Thatcher's personal popularity numbers were consistently lower than Callaghan's. She was disliked by large portions of the electorate. She won three elections anyway, and dominated British politics for a decade. Pundits tracked popularity; she tracked a different metric — the clarity and intensity of her support base. Dominating presence has more pull than likability. "Let some of the public hate you; you cannot please everyone."
- **What to do instead**: Build a base of people who are genuinely committed to your direction — not a broad pool of people who mildly approve. A Senior Director with 5 strongly aligned advocates is more powerful than one with 20 lukewarm ones. Take positions. Be clear about what you're for and against.
- **Caveat**: The "don't seek to be liked" principle has limits in corporate environments where you depend on the same people repeatedly. The goal is respect and trust, not antagonism for its own sake. Thatcher eventually fell because she polarized too broadly and too rigidly — the reversal at the end of Strategy 1 makes this explicit.

## FB-010: "Consensus means alignment — get everyone to agree before moving"

- **Source**: Greene, *The 33 Strategies of War*, Strategy 5: Avoid the Snares of Groupthink (The Command-and-Control Strategy)
- **Date**: 2026-04-02
- **Common belief**: Good product leaders build consensus before moving. If everyone agrees, the path is clear. Decisions made with full buy-in are more durable.
- **Why it's wrong**: Greene shows that groupthink — the irrationality of collective decision-making — produces the worst outcomes. Groups default to the safe, familiar, uncontroversial option. Genuine creative or strategic insight almost never emerges from consensus. It emerges from individuals with clear vision who can then bring others along. The leader who waits for full consensus before moving has already been outmaneuvered by the leader who moved and let others catch up.
- **What to do instead**: Separate two things: (1) the decision itself, and (2) the process of communicating and executing it. Decisions should be made by the person with the clearest view and most accountability. Communication and execution benefit from involvement. "Create a sense of participation, but do not fall into groupthink."
- **Caveat**: For decisions that genuinely require others' knowledge to make well — technical feasibility, cross-team dependencies — collaborative input improves the decision. The trap is treating input-gathering as consensus-building, or using "alignment" to defer a decision that one person should make.

## FB-011: "Moving first gives you the advantage — get there before competitors"

- **Source**: Greene, *The 33 Strategies of War*, Strategy 9: Turn the Tables (The Counterattack Strategy)
- **Date**: 2026-04-02
- **Common belief**: First-mover advantage is decisive. In competitive situations — org politics, product bets, market positioning — moving first is almost always better.
- **Why it's wrong**: Greene's counterattack strategy argues the opposite: moving first exposes your strategy and limits your options. The person who holds back, lets the opponent move, and then responds from a position of full information often has the structural advantage. "Moving first — initiating the attack — will often put you at a disadvantage: You are exposing your strategy and limiting your options." The defensive player knows what the attacker wants; the attacker does not know what the defender has held back.
- **What to do instead**: In adversarial or competitive situations, learn to hold and observe before committing. Let others play their hand. Reserve your move for when you have enough information to respond decisively. "Discover the power of holding back and letting the other side move first."
- **Caveat**: In non-adversarial situations (product launches, feature development, greenfield opportunity), speed genuinely matters and first-mover advantages are real. This principle applies specifically to competitive dynamics and adversarial negotiations, not to product execution.

## FB-012: "Retreat signals weakness — always hold your ground"

- **Source**: Greene, *The 33 Strategies of War*, Strategy 11: Trade Space for Time (The Nonengagement Strategy)
- **Date**: 2026-04-02
- **Common belief**: Giving ground — whether in a negotiation, a prioritization debate, or an organizational conflict — signals weakness and invites further pressure.
- **Why it's wrong**: Greene demonstrates through examples including Fabius Maximus (the Roman general who refused to engage Hannibal directly) that strategic retreat is often the highest form of strength. By refusing to fight on the opponent's terms, Fabius denied Hannibal the decisive battle he needed and let time and supply lines do the work. "Retreat in the face of a strong enemy is a sign not of weakness but of strength." Sometimes you can accomplish the most by doing nothing.
- **What to do instead**: When an adversary is strong and the timing is wrong, disengage deliberately. Don't fight the battle today if the terrain will be better in three months. Buy time. Let the opponent's momentum exhaust itself. Return when conditions have shifted.
- **Caveat**: Perpetual non-engagement is just avoidance — it only works as a deliberate strategy with a specific purpose and return condition. And in organizational contexts, being seen as someone who never takes a stand has its own costs. The principle applies to specific battles, not to a general posture of retreat.

## FB-013: "Being direct and transparent is always more persuasive than being indirect"

- **Rating**: Nuanced
- **Date cataloged**: 2026-04-02
- **Source**: Greene, *The Art of Seduction*, Appendix B (Soft Seduction); The Charmer chapter; The Charismatic chapter
- **Why people believe it**: "Radical candor" and "transparency" have become corporate values. Direct communication feels honest. Indirect communication feels manipulative.
- **Evidence against**:
  - Edward Bernays's Easter parade stunt (1929) sold cigarettes to millions of women by disguising a sales pitch as a news event. Explicit ads for the same product had minimal effect.
  - Reagan's 1984 campaign: CBS reporter Lesley Stahl aired a 4.5-minute critical piece over flattering visuals. A Reagan aide called to thank her — the images completely overpowered the critical words.
  - Zhou Enlai negotiated better terms for China from a position of weakness by appearing to concede supremacy to Stalin. Direct assertion would have failed.
  - Greene: "The less you seem to be selling something — including yourself — the better."
- **What's actually true**: Directness works when the other party already trusts you and is ready to receive the message. In most influence situations involving new stakeholders or senior audiences, indirect approaches (stories, demonstrations, emotion before logic, letting people arrive at the conclusion themselves) work better. The medium often carries more weight than the content.
- **Caveat**: Pure indirectness without substance fails eventually. The soft sell only works if there is something genuine behind it. Transparency with people who have already opted in is powerful.
- **Implication**: Before any important influence attempt, ask: is this a situation where directness will land or trigger resistance? If resistance is likely, story first. Emotion first. Evidence second. Explicit argument last.

## FB-014: "Charisma is a personality trait you either have or don't"

- **Rating**: Misleading
- **Date cataloged**: 2026-04-02
- **Source**: Greene, *The Art of Seduction*, The Charismatic chapter (Joan of Arc, Lenin, de Gaulle, Roosevelt, Krishnamurti)
- **Why people believe it**: Charismatic people seem to radiate something innate. It feels genetic, unchosen.
- **Evidence against**:
  - Napoleon spent hours practicing his gaze in a mirror, modeling it on the actor Talma.
  - De Gaulle deliberately cultivated Olympian composure as a strategic tool — it was not his natural state.
  - Lenin had zero charisma one-on-one; his charisma emerged only when he had a clear message, a cause, and a crisis to dramatize.
  - Greene identifies specific learnable components: Purpose (have a clear direction), Mystery (reveal contradictions slowly), Calm under pressure, Eloquence, Theatricality, Fervency.
- **What's actually true**: Charisma is the impression created by a cluster of behaviors, most of which can be practiced. The components that can't be faked (genuine belief in something) require actually caring — but that's a choice, not a trait.
- **Caveat**: Some people start with more natural ease. The gap between natural and practiced is real but much smaller than the gap between practiced and unpracticed.
- **Implication**: Run the checklist: Do you have a clear, repeatable point of view? Do you stay calm when challenged? Do you believe in what you're building? If not, fix those first. The rest (presence, language, mystery) follow.

## FB-015: "Transparency builds trust — share your thinking openly"

- **Rating**: Nuanced
- **Date cataloged**: 2026-04-02
- **Source**: Greene, *The 48 Laws of Power*, Law 3 (Conceal Your Intentions)
- **Why people believe it**: "Radical transparency" and "default to openness" are corporate values at many tech companies. Sharing your reasoning openly feels honest and trustworthy. Concealment feels manipulative.
- **Evidence against**:
  - Otto von Bismarck deliberately concealed his intentions from both allies and opponents throughout the unification of Germany — revealed only what served him at the moment of strategic necessity.
  - Greene: people who telegraph their next move give opponents time to prepare counter-moves. Announcing your strategy invites resistance before you've built the momentum to overcome it.
  - In org politics, sharing that you're building toward X before X is built gives the opposition time to organize. Many initiatives die before they exist because they were announced before they were real.
  - Sharing uncertainty or incomplete thinking with senior stakeholders signals lack of readiness, not transparency.
- **What's actually true**: Transparency about values and principles builds trust. Transparency about tactics and in-progress strategy can kill initiatives. There is a difference between being honest (not lying) and being fully open (sharing everything). The first is non-negotiable; the second is a strategic choice.
- **Nuance**: With your direct manager, high transparency about uncertainty is generally right — they need to make decisions and need your actual picture. With senior stakeholders, present finished thinking, not in-progress thinking. With peers in competitive situations, be thoughtful about what you share and when.
- **Implication**: Before sharing a plan or initiative, ask: is this baked enough to share? If not, work it until it is. The right time to tell Bertrand about a new idea is after you've thought through the core objections, not when the idea first occurs to you.

## FB-016: "Always say more — detail and explanation build credibility"

- **Rating**: Dangerous
- **Date cataloged**: 2026-04-02
- **Source**: Greene, *The 48 Laws of Power*, Law 4 (Always Say Less Than Necessary)
- **Why people believe it**: Detailed explanations feel thorough. In many professional contexts, over-explaining feels like diligence. Being laconic feels arrogant or evasive.
- **Evidence against**:
  - Coriolanus — Shakespeare's example and Greene's — lost the consulship by saying too much. His words gave opponents ammunition they would not otherwise have had.
  - Henry Kissinger's negotiating power came largely from deliberate ambiguity: "We'll see" and "interesting" were more powerful than clear positions because they left the other party guessing and gave him room to maneuver.
  - Louis XIV answered questions of great consequence with "I'll think about it" — the most powerful reply available. It gave away nothing and preserved all options.
  - Greene: "The more you say, the more common you appear, and the less in control." Power appears self-contained.
- **What's actually true**: Saying less creates more impact when each word is weighted. In high-authority-differential situations, long explanations often signal defensiveness — the powerful say less because they don't need to justify themselves. Strategic silence is not evasion; it is economy.
- **Nuance**: In trusted peer conversations and in direct report relationships, fuller explanation is often the right move for collaborative thinking. The principle applies most powerfully in high-stakes upward or lateral communication.
- **Implication**: In any important meeting, before speaking, ask: is this necessary? If the answer isn't clearly yes, hold it. After a win, resist the urge to explain how it happened.

## FB-017: "Busy, responsive people are valued — maximize availability"

- **Rating**: Misleading
- **Date cataloged**: 2026-04-02
- **Source**: Greene, *The 48 Laws of Power*, Law 16 (Use Absence to Increase Respect and Honor)
- **Why people believe it**: Responsiveness is a visible signal of engagement and work ethic. Being available to everyone feels like good stakeholder management. Fast replies feel professional.
- **Evidence against**:
  - Deporetes (the jester) was highly visible at the court of Philip II of Spain — until he became so ubiquitous that the king finally said "I never want to see this man again." Total availability led to contempt.
  - Greene: "Once you cannot be had for love or money, people will begin to push toward you." Value is created partly by scarcity. The scarce person is sought; the always-available person is taken for granted.
  - The Art of Seduction's Coquette chapter confirms: controlled unavailability creates desire and pursuit. Total availability kills it.
- **What's actually true**: Strategic unavailability — not always available, not always the first to respond, selectively present — creates gravity. It signals that your time is a finite resource worth competing for.
- **Nuance**: Availability matters during trust-building phases and in crisis situations. This principle applies most powerfully after you have established your value.
- **Implication**: Do not respond to every Slack within minutes. Decline low-value meetings. Be visibly present at the things that matter and visibly absent at the things that don't. The gap creates value.

## FB-018: "Timidity is safer than boldness in corporate environments"

- **Rating**: Dangerous
- **Date cataloged**: 2026-04-02
- **Source**: Greene, *The 48 Laws of Power*, Law 28 (Enter Action with Boldness)
- **Why people believe it**: Being cautious and measured feels safe. Bold moves feel risky. In a large org with lots of stakeholders, a small mistake made boldly seems worse than a large mistake made cautiously.
- **Evidence against**:
  - Greene's consistent historical evidence: bold entry into any endeavor creates an impression of power and self-assurance that timid moves never create. Bold actions seem right because confidence is contagious.
  - Timidity in leadership positions signals that you're not sure you belong there — and stakeholders read that signal immediately.
  - Cats stalk prey only after a moment of stillness — not timidity, but controlled boldness. "The boldness of the cat creates its own fear in the prey."
  - The opposite of bold is not careful — it's hesitant. Hesitation in leadership is visible and toxic: it makes others hesitate too.
- **What's actually true**: In execution, boldness creates momentum and inhibits opposition before it organizes. In communication, confident, direct language lands harder than hedged language. In stakeholder dynamics, taking a position earns more respect than seeking consensus.
- **Nuance**: Boldness must be grounded. Boldness without competence behind it is bluster and it fails fast. The preparation must be there before the boldness.
- **Implication**: When entering a new role, making a new proposal, or presenting to senior leadership — commit fully. Do not hedge, do not qualify excessively, do not retreat from a position the first time it's challenged. Enter with conviction.

## FB-019: "Good work eventually gets noticed — you don't need to promote yourself"

- **Rating**: Dangerous
- **Date cataloged**: 2026-04-02
- **Source**: McIntyre, *Organizational Politics* (Ch 6, Ch 8 — Political Suicide / Visible Results)
- **Common belief**: Doing excellent work is sufficient for career advancement. Self-promotion feels uncomfortable and unnecessary. The right people will notice eventually.
- **Why it's wrong**: Organizations do not automatically surface good work to the people who make promotion decisions. Decision-makers have hundreds of inputs competing for their attention. The PM who does excellent work in a closed room has effectively opted out of the promotion conversation. McIntyre calls this one of the most reliable political suicide patterns — not dramatic failure but quiet invisibility. "Invisible contributions have no political value."
- **What to do instead**: Ensure contributions are legible to the right people. Name your work in artifacts. Follow up in writing after verbal contributions are adopted. Connect your results to the metrics your sponsors care about. The goal is not bragging — it is making your contribution attributable.
- **Caveat**: Self-promotion without underlying substance is immediately detected and damages credibility. The sequence must be: do excellent work, then make it visible. Not visible first.

## FB-020: "To change someone's behavior, you have to address them directly"

- **Rating**: Nuanced
- **Date cataloged**: 2026-04-02
- **Source**: McIntyre, *Organizational Politics* (Ch 9 — The Paradox of Influence)
- **Common belief**: If someone is doing something you need to change, the most effective path is to address them directly — point out the behavior and request the change.
- **Why it's wrong**: McIntyre's paradox of influence establishes that the most reliable way to change someone else's behavior is to change your own first. Your behavior creates a significant portion of the other person's behavioral context. When you change your approach, their behavior changes in response — often without any direct request. Direct addressing triggers defensiveness in proportion to the magnitude of the request.
- **What to do instead**: Before any direct conversation about someone's behavior, run the self-observation step first. What are you doing that is contributing to the pattern? Change that and observe the response. If direct conversation becomes necessary after that, come from a position of having already changed your side of the dynamic.
- **Caveat**: True adversarial behavior — deliberate undermining, systematic credit-stealing — cannot be resolved through self-modification alone. The paradox applies to friction in collaborative relationships, not to hostile acts.

## FB-021: "Emotional reactions signal authenticity and passion — they build trust"

- **Rating**: Dangerous
- **Date cataloged**: 2026-04-02
- **Source**: McIntyre, *Organizational Politics* (Ch 6 — Hazards of Uncontrolled Emotion)
- **Common belief**: Showing emotion in professional settings signals genuine investment and authenticity. Vulnerability and passion make you more relatable and trustworthy.
- **Why it's wrong**: McIntyre establishes a sharp asymmetry: one emotional outburst in a senior meeting can undo months of credibility building. There is no equivalent positive emotional event. Frustration signals loss of control; defensiveness signals insecurity; excitement that becomes pressure signals the ego is staked on the outcome. All of these make observers uncomfortable in high-stakes settings. The "authenticity" interpretation of emotional display is almost entirely a myth in hierarchical professional environments — what observers actually see is: can this person hold themselves together under pressure?
- **What to do instead**: Equanimity is the signal of senior-level readiness. Receive criticism calmly, absorb setbacks without visible distress, hold your ground on a challenged position without getting heated. The emotion can be real — the expression of it in public is a separate choice.
- **Caveat**: Genuine enthusiasm in appropriate contexts (team celebration, early-stage brainstorming, informal conversations) has real value. The rule applies specifically to high-stakes meetings with evaluating audiences.

## FB-022: "If you don't have the political leverage you need, work harder"

- **Rating**: Misleading
- **Date cataloged**: 2026-04-02
- **Source**: McIntyre, *Organizational Politics* (Ch 3 — Leverage Equation, Ch 11 — Political Game Plan)
- **Common belief**: If your career isn't advancing or your initiatives keep getting blocked, the answer is to perform better and deliver more. Results always win eventually.
- **Why it's wrong**: McIntyre's leverage equation shows that what matters is not raw output but valued output — output that is visible to decision-makers, attributable to you, and relevant to their priorities. Working harder on the wrong things, or doing excellent work that no one above you can see, does not change the leverage calculation. The director who doubles their output in a closed room remains invisible.
- **What to do instead**: Diagnose which leverage dimension is weakest before increasing effort. Is it Results (you need better outputs), Knowledge (you need a capability others don't have), Perception (you're not known by the right people), or Partnerships (you lack sponsors who advocate for you)? Target the weakest link. More output when Perception is the problem is wasted effort.
- **Caveat**: A minimum threshold of real performance is required — leverage built entirely on perception without substance collapses fast. The point is that performance alone is necessary but not sufficient.

## FB-023: "Playing not to lose is a safe strategy — minimize risk and protect position"

- **Source**: Lafley & Martin, *Playing to Win*, Chapters 1–2
- **Date**: 2026-04-02
- **Common belief**: In uncertain markets or under pressure, the prudent approach is to minimize exposure — don't overcommit, keep options open, stay in the game. "Participating" is safer than "winning."
- **Why it's wrong**: Lafley's Saturn case dismantles this completely. GM launched Saturn to participate in the small-car segment without investing adequately to win. Toyota and Honda, which aimed to win, made hard choices and significant investments. Saturn was eventually discontinued. Lafley: "Companies that aim merely to participate often fail to compete effectively." Playing not to lose is not a neutral posture — it is a guarantee of inadequate investment, which makes you uncompetitive against players who committed. The aspiration determines the investment level; low aspiration produces under-investment.
- **What to do instead**: Define what winning looks like in customer terms (not financial terms). Then make the investments that winning requires. If you can't make those investments, explicitly exit the arena rather than half-entering it. A conscious no-play is better than a low-ambition play.
- **Caveat**: "Playing not to lose" is appropriate in secondary arenas where you have no path to winning — the right answer there is exit, not defense. The trap is applying this posture in your primary arena where winning is possible with full commitment.

## FB-024: "Strategy is a plan — write it once, execute against it"

- **Source**: Lafley & Martin, *Playing to Win*, Chapters 1 and 7
- **Date**: 2026-04-02
- **Common belief**: Strategy is a document or plan created in a planning cycle, handed down, and executed. Once the strategy is set, the work is execution. Revisiting the strategy signals indecision.
- **Why it's wrong**: Lafley explicitly frames strategy as iterative, not static. The five choices must be revisited as insights emerge — capabilities constrain where you can play, which may force a revision to the winning aspiration, which changes how to win, and so on. P&G's Olay transformation didn't happen in one planning cycle; it evolved as market insight accumulated. Chapter 7 (Think Through Strategy) emphasizes starting with the winning aspiration but being willing to refine it as other cascade elements are developed. Treating strategy as a fixed plan creates rigidity — you end up executing against choices that conditions have made wrong.
- **What to do instead**: Treat strategy as a living set of choices with explicit re-evaluation triggers. When market conditions change, when capabilities are discovered to be weaker than thought, or when competitive moves shift the landscape — revisit the relevant cascade choice and check what it implies for the others. Document the revision with reasoning.
- **Caveat**: Constant strategy revision is as bad as none. The right cadence for an annual planning org is quarterly strategy health checks (are the five choices still coherent?) and annual resets. Tactical pivots should not be confused with strategy changes.

## FB-025: "Capabilities are resources you need to acquire — budget and headcount solve the gap"

- **Source**: Lafley & Martin, *Playing to Win*, Chapter 5 (Play to Your Strengths)
- **Date**: 2026-04-02
- **Common belief**: When a capability gap is identified, the fix is resource: hire more people, buy a company, or fund a new team. Capabilities are assets you either have or acquire.
- **Why it's wrong**: Lafley shows through the Gillette acquisition that capabilities are systems of mutually reinforcing activities — not isolated assets. P&G's acquisition of Gillette succeeded because P&G applied its consumer understanding and brand-building system to Gillette's existing strengths. Acquisitions that fail (AOL Time Warner, DaimlerChrysler) treat capabilities as individual assets that can be combined. But sustainable competitive advantage comes from activity systems where each component strengthens the others. You can't acquire the system; you have to build the connections.
- **What to do instead**: Map capabilities as activity systems: what activities are required, how do they connect, which ones are already strong, and which gaps would break the reinforcing connections? Then invest in filling the gaps that serve the system — not just the gaps that look biggest in isolation. Also evaluate feasibility, distinctiveness, and defensibility before investing in building any capability.
- **Caveat**: Sometimes a genuine capability gap (missing technical expertise, missing data) does require hiring or acquisition. The point is that acquiring the resource without integrating it into the activity system produces a fragmented capability that doesn't compound.

## FB-026: "Good strategy comes from rigorous analysis — run the numbers, use the frameworks"

- **Source**: Lafley & Martin, *Playing to Win*, Chapter 7 (Think Through Strategy) and Chapter 8 (Shorten Your Odds)
- **Date**: 2026-04-02
- **Common belief**: Strategy is an analytic exercise. SWOT analysis, BCG matrix, Porter's Five Forces, VRIN model — the tools produce the answer if you populate them rigorously. The better the analysis, the better the strategy.
- **Why it's wrong**: Lafley acknowledges that analytical tools (SWOT, BCG matrix, VRIN) are useful for informing strategy discussions, but they don't produce strategy. The five cascade choices still require judgment under uncertainty — and that uncertainty is irreducible. The trap is mistaking analytical rigor for strategic clarity. Organizations that over-rely on analysis often produce strategies that are internally consistent but disconnected from real competitive dynamics or actual capabilities. Lafley: the goal is not to find a perfect strategy but to find approaches that align with your unique context.
- **What to do instead**: Use analytical tools to structure the thinking within each of the five cascade questions — not to generate the answers. The real work is building shared conviction among decision-makers about which choices to make and why. That requires conversation and judgment, not more analysis. Chapter 8's "shorten your odds" approach: run strategic experiments to reduce uncertainty in the most critical bets rather than trying to analyze your way to certainty.
- **Caveat**: Insufficient analysis is also a failure mode. The point is not to skip analytics — it is to not substitute analysis for decision-making. Frame the analysis as input to the strategic conversation, not output of the strategy process.

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
