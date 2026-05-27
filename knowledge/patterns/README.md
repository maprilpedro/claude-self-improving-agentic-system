# PM Patterns & Frameworks

> Recurring patterns in product management. Each pattern needs at least 2 supporting observations.

## User Research Patterns

### First Principles Customer Research — Skip the Admin, Find the Owner
- **Date identified**: 2026-04-10
- **Source**: Loni Stark, H2 Prelim Part 3 (April 2026). Rights management discovery example.
- **Pattern**: When customers say they want something (rights management, archiving, federated search), the stated desire is rarely the real need. The person who talks to you about it is usually an admin or a PM proxy — not the person whose problem it actually is. Loni's instruction: find the 1-2 people whose professional life depends on this problem. Not the guardian. The person who would get sued.
- **The interview protocol Loni described**:
  1. What does [topic] mean to you?
  2. What are you most fearful of when you think about [topic]?
  3. Where did [topic] show up in your work last month? What triggered it?
  4. Are there moments you get excited about [topic]? Tell me about those.
- **Why it works**: You're excavating a mental model, not evaluating a feature. The output tells you: what the user fears, what they love, what triggers the need, and what a good outcome looks like. Then you map your product knowledge onto that model — not the other way around.
- **What breaks**: Asking "do you want this feature?" before doing this. You'll get happy ears. Everyone says yes to features that solve problems they think they have.
- **Application**: Before designing or scoping any AI capability that "customers have asked for," find the actual business owner of the problem and do this interview. Five minutes of this beats a 30-person co-innovation call.

## AI Agent Reporting Patterns

### Three-Tier Tag Taxonomy for Agent Interaction Reports
- **Source**: AEM agent reporting system (Felix Delval + Pedro), tag review April 7, 2026
- **Date**: 2026-04-07
- **Pattern**: Agent interaction reports become actionable when tags are structured in three distinct tiers:
  1. **request_type** — what the user was trying to accomplish (4-6 per agent). These are the intents. They define the surface area of the agent's use cases.
  2. **custom** — behavioral patterns, edge cases, and context flags (5-7 per agent). These explain how interactions played out, not what was asked.
  3. **value-realization** — confirmed successful outcomes (2-3 per agent). These are the wins — what the agent actually delivered.
- **Anti-patterns to avoid**: (1) Tags that track failures at the orchestrator level (e.g. wrong-agent-routed) belong to the routing layer, not individual agent reports. (2) Value-realization tags that are just past-tense versions of request_type tags add no signal. (3) Input format tags (user provided an ID, user referenced by position) are operational noise for PM purposes. (4) Capability tags ("CF model retrieved") are not value outcomes — something has to land for a tag to be value-realization.
- **When it applies**: Any AI agent or LLM-powered product where you want to understand usage patterns, measure outcomes, and communicate performance to product leadership.

## Stakeholder Communication Patterns

### Gap Recovery Framing — When You Don't Have What You Said You Had
- **Date identified**: 2026-04-09
- **Source**: Pedro/Bertrand org numbers situation, April 9, 2026.
- **Pattern**: When you've overpromised information you don't have, the recovery move is to reframe the gap as diligence, not confession. Don't say "I don't have it." Say "I want to give you accurate numbers, not fast ones — give me until [specific time]."
- **Why it works**: It reframes the gap from "he didn't have it" to "he has standards." The person waiting gets a timeline and a signal that you're being rigorous, not sloppy.
- **What to avoid**: Over-explaining why you don't have it, apologizing more than once, or adding "I thought I had it but..." — all of these draw more attention to the miss than the reframe does.
- **Variation**: If you have partial data, lead with that. "I have X and Y confirmed, still validating Z" is stronger than asking for time with nothing in hand.

### Self-Gate, Don't Gate Their Work
- **Date identified**: 2026-04-15
- **Source**: Drafting Rubin reply to Silvia/Angela. Initial phrasing "Before we lock the AEM user tagging..." read as gatekeeping a brake on their work. Pedro flagged it.
- **Pattern**: When you need alignment before an adjacent team codes something that affects your product, the framing has to put the gate on you, not on them. "Before we lock X" = you are blocking their work. "Before I send suggestions, I'd find it useful to understand Y" = you are self-gating your own contribution to serve them better. Same outcome, opposite tone.
- **Why it matters**: Cross-org asks are relationship-sensitive. If your first response reads as a brake, the next request goes to someone else or gets coded without you. Self-gating signals humility and diligence while still securing the alignment moment.
- **How to apply**: Audit any cross-org reply for phrases like "before we lock," "before we proceed," "we need to align first." Replace with "before I send suggestions," "so my input fits what you're building," "happy to dig in, one thing I'd find useful first." The tone flips from controlling to contributing.
- **Related**: Soft sell (Art of Seduction), Distribution vs Validation for Tool Rollout (leadership/).

### Save Scoping Questions for the Live Call, Not the Written Reply
- **Date identified**: 2026-04-15
- **Source**: Rubin reply drafting. First version included four scoping questions in the email (scope, audience, source, roadmap). Pedro pulled back.
- **Pattern**: Written scoping questions let the other side answer in writing and skip the meeting. You lose the live conversation where real information flows. In writing, stake claims and flag risks — but hold the deep questions for the call. Strip the reply to the minimum needed to justify the walkthrough.
- **Why it works**: In writing, they craft polished answers that close the loop. On a call, questions breathe — answers branch, context emerges, you see the tool, you read body language. The scoping questions stay in your head as the call agenda, not as email content.
- **How to apply**: Draft the reply with full scoping questions first to clarify your own thinking. Then delete everything that can be asked on the call. Keep only: the answer to their direct question, one or two flags that justify a sync, the call ask. Bring the deleted questions into the meeting as your agenda.

### Peer Review Is Audit, Not Validation — Plan Accordingly
- **Date identified**: 2026-04-16
- **Source**: Apoorva Gupta agent report review (April 16, 2026). Pedro expected validation; got a punch list instead (50-60% data gap vs Grafana, TSR counting "no result found" as success, tag classification bleeding across agents, missing First Useful Result Rate, no content-type breakdown).
- **Pattern**: When you bring an artifact to a peer PM with a data team (Ankur, Varun), the meeting will almost always be an audit, not a rubber stamp. Their delegates will stress-test numbers, question metric definitions, and find gaps. That's the norm, not the exception. Calling it "validation" before the review sets you up to misreport the outcome to your manager.
- **Anti-pattern**: Walking out of a peer review telling your manager "I got it validated" when in reality you got it audited and now have a punch list. That framing sets a false expectation and damages credibility when the gaps surface.
- **How to apply**: Before any peer review with a data-capable team, plan for audit outcomes:
  1. Name internally (and to yourself) that this is an audit, not a rubber stamp. You are inviting stress-testing.
  2. Calibrate what a successful outcome looks like — specific gap findings, concrete metric improvements, clear next steps. Not a yes/no.
  3. Report the outcome to your manager in audit language: "X's team stress-tested, found gaps, we're closing them." Not "X validated."
  4. The peer who did not push back and said "looks good" either did not engage seriously or has a lower quality bar than your eventual audience. Prefer engaged audit over polite rubber stamp.
- **Senior Director framing**: Director says "I got feedback." Senior Director says "Their team stress-tested the report end to end, found specific gaps, and handed us the exact metric our target audience actually wants." Same meeting, two different framings. Use the second when reporting upward.

### The Program Manager Drafting Inversion
- **Date identified**: 2026-04-16
- **Source**: Yanira Castaneda (PgM) offered to draft an exec summary deck for Loni + Jean-Michel with Pedro as the sender. Would have put her framing under Pedro's name.
- **Pattern**: Program Managers often offer to draft content that ends up being sent under the PM's name. The offer is genuinely helpful program management, but it inverts authorship — the drafter owns the framing, and the PM becomes a messenger. McIntyre's "visible results" rule: whoever produces the artifact owns it, regardless of whose name signs it.
- **Why it matters for visibility**: Exec-facing artifacts are a primary visibility mechanism. Letting the PgM draft them means your name carries framing that isn't yours, and your voice never reaches the executive audience that matters. At promotion time, you have few artifacts with authorial ownership.
- **How to apply**: Flip the flow when you see it:
  1. PgM provides raw content and coordination (agent statuses, cross-team updates, data aggregation). This is their strength and scope.
  2. PM drafts the narrative. Voice, framing, strategic connective tissue stay with you.
  3. PgM reviews the draft for factual accuracy before send.
- **Reframe language that works**: "Happy for you to pull the content and coordination — that's your strength. I'd rather draft the narrative myself so it lands in my voice. Can you send me the raw material instead of a deck?" This respects their scope, redistributes the labor correctly, and preserves authorship.
- **Related**: McIntyre "visible results"; Law 7 (get others to do the work ethically — they provide content, you provide synthesis; credit both).

### Threat Framing Detection in Collaboration Emails
- **Date identified**: 2026-04-16
- **Source**: Pedro caught this in an email draft to Sergey about AEM-AO SLAs. The line "I would rather bring one aligned view to our leadership than two separate reads" read as leverage, not collaboration.
- **Pattern**: Any phrase that implies "otherwise this goes wrong for both of us" is leverage framing, even when dressed as collaboration. Examples: "one aligned view vs two separate reads," "before this lands on leadership's desk," "to avoid surprising our VPs." These create implicit pressure and read as mild threats to peer recipients.
- **Anti-pattern**: Using collaboration-flavored language to apply pressure. The recipient feels the pressure even if they don't articulate why, and the working relationship takes a small hit on every such email.
- **How to apply**: Before sending any peer collaboration email, scan for phrases that imply mutual consequences for non-alignment. Replace with direct questions or factual observations. "What exists today on your side?" is stronger than "I'd rather we align before this surfaces to leadership." Questions invite engagement; implied consequences invite defense.
- **Quick test**: If the sentence could be read as "help me avoid an outcome" rather than "help me understand," it's leverage framing. Rewrite as a question or observation.
- **Connected to**: Managing up, validate-then-scale response pattern.

### "We" vs Named Person in Stakeholder Communications
- **Date identified**: 2026-04-09
- **Source**: AEM Agent Reports Slack message revision, April 9, 2026.
- **Pattern**: When communicating an initiative to a group that includes people outside your manager's direct line, attribute it to "we" rather than naming the manager as the originator. "We want to track product gaps" instead of "Bertrand asked us to track product gaps."
- **Why it works**: (1) Naming your manager as the driver positions you as executing someone else's ask — not as a leader with a point of view. (2) "We" signals joint ownership with leadership, which is better for your visibility. (3) It avoids making people who aren't in Bertrand's org feel like they're receiving a directive.
- **When to use**: In any Slack message, email, or public communication where you're announcing work that originated from a manager ask but you are the one executing and owning it.
- **Exception**: In a direct 1:1 with Bertrand, attributing something back to him is fine and appropriate. The rule applies to outward communications.

### Compliance Risk Stays Out of Adoption Messages
- **Date identified**: 2026-04-09
- **Source**: AEM Agent Reports Slack drafting, April 9, 2026. Ian Boston's data residency risk.
- **Pattern**: When a compliance risk exists but the decision-maker has accepted it and work continues, do not include the risk in broad adoption communications. It belongs in 1:1s and decision logs, not status Slack messages.
- **Why**: The adoption message is designed to drive engagement and confidence. A compliance caveat in that message creates alarm in people who have no decision power over it, and undermines the adoption you're trying to drive.
- **The test**: Ask "does including this change anyone's behavior who is reading this message?" If no — because the decision is already made — leave it out. If yes — because action is needed — include it with precision.
- **Connected to**: Bertrand's April 1 risk acceptance decision (data compliance). Ian's "fix it quietly" framing.

### Two-Audience Artifact Split — Operator Reports vs Exec Reports
- **Date identified**: 2026-04-13
- **Source**: AEM agent report review (adbe-agent-dashboard-validation). All-agents report and per-agent reports used the same template. Neither audience was served well.
- **Pattern**: When a report or document serves two audiences with fundamentally different needs, one template will fail both. The fix is not to add more sections — it is to build separate artifacts.
  - **Operator artifact**: customer-level, named entities, action-oriented, detailed funnels. Designed to be acted on by the person who owns the agent or feature.
  - **Executive artifact**: pattern-level, verdict-first, strategic synthesis, portfolio view. Designed to inform judgment at the VP or Senior Director level.
- **Diagnostic signs**: Execs find the report too detailed. Operators find it too abstract. The same section reads differently depending on who's reading it. The "insights" section names customers or orgs the exec doesn't recognize.
- **Application**: Before building any shared report, ask: who are the two audiences, and are their needs compatible? If not, separate the artifacts from the start. Retrofitting is harder and usually produces a frankenstein. The split also creates a natural accountability structure — operator report owned by agent owner, exec report owned by the PM who coordinates across agents.
- **Observed at AEM**: All-agents report was built like a bigger version of per-agent reports. Same nav, same sections, same level of detail. Loni needed fleet-level patterns and a one-sentence verdict. Corey needed LG Electronics' failure breakdown. The same template delivered neither cleanly.

### Differentiation as Diagnostic Requirement
- **Date identified**: 2026-04-22
- **Source**: Varun Kalra (Discovery Agent validator) on why Discovery Agent's uniform "no results found" response breaks product-gap triage. Compared with Governance Agent's explicit "I cannot help with this" response.
- **Pattern**: You cannot fix what you cannot distinguish. When two fundamentally different failure modes produce the same observable output, triage is impossible and improvement work becomes random. Before a product can improve, its failure surface has to be at least as granular as the distinct causes you'd want to address. In Discovery Agent: "unsupported query" and "content doesn't exist" and "search quality failed" all return the same user-facing "no results found." A PM looking at the data can't tell which of the three is happening, so can't route the fix to the right team (scope owner vs content owner vs search-quality owner).
- **The diagnostic bar**: Your observable signals need to distinguish between things you would take different action on. If the action is identical regardless of cause, fine to collapse. If actions differ, the signal must differ. This is the minimum taxonomy requirement.
- **How to apply**: In any reporting or measurement work, when you see a single category that swallows multiple root causes, mark it. Ask "would I want to do different things for different instances of this?" If yes, split it. The single bucket is hiding a diagnostic problem even if your numbers look clean.
- **How to spot this in practice**: Watch for categories named by observed symptom ("error," "no result," "abandoned") rather than root cause. Symptom-named buckets are the canary. Root-cause-named buckets force the taxonomy to stay sharp.
- **Anti-pattern**: Accepting an uninformative category because the data "looks clean." Clean data with hidden causal mixing is worse than messy data with clear distinctions — the clean version gives false confidence.
- **Related**: Failure Taxonomy Quality vs Gap Split (patterns/); "No Results Found" Is a Product Gap in Agentic UX (ai-product/).

### Light Warm-Up Before a Big-Ticket Meeting
- **Date identified**: 2026-04-21
- **Source**: Jaclyn Eckersley in P42 Status meeting, April 21. With the Loni + Jean-Michel meeting 2 weeks out (week of May 4), Jaclyn told Pedro to send a "light status summary" to Jean-Michel the week before (week of April 28). Her framing: "doesn't need to have all the details… just some sort of status update. Hey, even if it is 'this is the feedback from someone' — it's just something." The big meeting gets the full deck. The week-before note keeps the exec warm.
- **Pattern**: When you have a high-stakes exec meeting scheduled, there's a tendency to save all your material for the moment and go silent in the lead-up. That silence is a risk: the exec walks in cold, you walk in blind to their latest thinking, and any shift in their priorities surprises you live. A light warm-up artifact — one screen, a few bullets, a recent data point — solves all three. It primes the exec on the topic, gives them a chance to react ("actually I want you to also cover X"), and surfaces any new constraint before the main event.
- **Why it works**: (1) Exec mental context is the bottleneck in high-stakes meetings; warming them up lowers the activation energy of the full presentation. (2) It creates a feedback loop — if the warm-up lands flat, you know to adjust the main artifact. If they respond with a question, that question becomes a planned slide. (3) It compounds the visibility of the work — instead of one touchpoint, you get two, and the second one builds on the first.
- **How to apply**: For any VP-level meeting scheduled 1-2 weeks out, commit to a light status artifact the week before. Scope: max one screen. Content: a verdict-first sentence, one chart or data point, one thing you're tracking, one question for the exec (optional). Delivery: Slack, email, or a shared note — not a deck. Avoid perfection theater. The goal is touchpoint, not artifact. A scrappy 10-minute note beats a polished 2-hour deck for this purpose.
- **Anti-pattern**: Treating the warm-up as a mini-version of the main artifact. You spend 2 hours, the exec reads for 30 seconds, and you've burned prep time that should have gone to the main deck. Keep it genuinely light. A link to a work-in-progress beats a finished mini-deck.
- **Related**: Claude Projects as Queryable Exec Artifacts (the warm-up can be "I loaded the draft analysis into this Claude project, take a look when you have a moment"); H2 Planning Visibility.

### Exec Report Design Principles — What Makes a VP-Level Report Work
- **Date identified**: 2026-04-13
- **Source**: AEM agent report review, April 13, 2026. Synthesized from Loni and Bertrand's known preferences and what was missing from the existing reports.
- **Pattern**: Seven principles that consistently distinguish exec-grade reports from operator-grade reports:
  1. **Verdict first** — open with one sentence of judgment, not data narration. "Users are growing but outcomes are not following" beats "W14 saw strong top-of-funnel growth with customers up 9.3%." The exec reads the first sentence and decides if the report is worth their time.
  2. **Define all metrics at first use** — executives cannot be expected to know your internal acronyms. TSR, VRR, EPA — add one line near the KPI strip. The five seconds it takes to add eliminates a credibility risk in every meeting.
  3. **Baseline beside every number** — a number without a reference point is not actionable. "23.2% TSR" with no target or historical average means nothing. Show the all-time average, the target, or the benchmark. Bertrand explicitly asked for "ratios vs baseline," not absolute numbers.
  4. **Name an owner on every recommendation** — a recommendation without an owner is an observation. Executives will always ask "who owns this?" If the answer isn't in the report, the report is incomplete.
  5. **Patterns not named entities** — VP-level stakeholders don't process individual customer names as signal. "LG Electronics has 2.6% SR" is noise. "High-volume new customers are failing at 3x the fleet average" is signal. The PM's job is to do this synthesis before the exec has to.
  6. **Emphasize the metric leadership declared primary** — if Loni said repeating users are the primary value signal, that metric needs to visually dominate the KPI strip, not sit equal to seven others. What the exec said matters most should appear as if it matters most.
  7. **Surface decisions, not just data** — include a "What Needs a Decision" section. Two to three items max. Each with: the situation, the recommendation, the owner. This positions the PM as a decision-surfacer rather than a reporter. Senior Director behavior, not Director behavior.
- **Application**: When preparing any artifact for VP or Senior Director review, run through these seven. Missing any one of them is a gap that the exec will notice, even if they don't name it.

## Product Analytics Patterns

### High Conversion + Low Penetration = Awareness Problem, Not Product Problem
- **Source**: AEM Experience Hub analytics, April 2, 2026 — 36.3% AEM penetration, 96% EH→profile conversion
- **Date**: 2026-04-02
- **Insight**: When users who reach a product convert at a very high rate (96%) but overall penetration of the addressable base is low (36%), the growth lever is not improving the product — it's getting more people to the product. The product is working. The problem is awareness, navigation, and entry points from other surfaces.
- **Anti-pattern**: Optimizing the product experience when the real problem is that most users never arrive. Misdiagnosing a discovery problem as a quality problem wastes cycles and misframes the roadmap.
- **PM Application**: Before any "improve retention/engagement" roadmap item, check whether the conversion rate once users arrive is already high. If yes, the priority is acquisition/awareness, not experience improvement. For EH: 96% engage once they land — the 13 weeks roadmap focus should be on why 64% of AEM users never reach EH, not on what happens after they do.

## Strategy Patterns

### The Strategy Cascade — Five Integrated Choices
- **Date identified**: 2026-04-02
- **Source**: Lafley & Martin, *Playing to Win*, all chapters
- **Observations**: (1) P&G's Olay transformation: masstige segment (WTP) + women 35+ (customer) + superior formulation + retail partnerships (HTW) + R&D and brand-building (capabilities) + innovation tracking (systems) — all five choices reinforced each other and the brand went from declining to $2.5B+. (2) GM's Saturn: aspired to "participate" in small-car segment → under-invested relative to Toyota/Honda → dismantled. (3) P&G's Gillette acquisition: screened for growth accretiveness, structural attractiveness, and strategic fit — worked because capabilities aligned. AOL Time Warner merger: no capability alignment → destroyed value.
- **Pattern**: A strategy that cannot answer all five cascade questions — or answers them inconsistently — is not a strategy. It is a wish list. The diagnostic power of the cascade is in the coherence test: change any one choice and verify the other four still hold. Where they don't, there is a gap that must be explicitly addressed. Choosing where NOT to play is as important as where to play. Low winning aspirations guarantee under-investment and competitive failure.
- **When it works**: Annual strategy reviews, roadmap prioritization, new product or initiative planning, when an org argument keeps cycling without resolution.
- **When it fails**: When used as a template to fill in rather than as a coherence diagnostic. When the aspiration is defined vaguely. When the management systems question is skipped (most common failure mode).
- **Related**: Strategy Choice Cascade in tools/decision-matrix.md, FB-023 (playing not to lose), FB-024 (strategy as plan)

### Low Aspiration Guarantees Under-Investment
- **Date identified**: 2026-04-02
- **Source**: Lafley & Martin, *Playing to Win*, Chapter 2; confirmed by Saturn/P&G contrast
- **Observations**: (1) Saturn aimed to participate, not win → did not invest to beat Toyota/Honda → discontinued. (2) P&G's outsourcing strategy under Passerini: aimed to win (best-of-breed, not conventional single-vendor) → lower costs + higher employee satisfaction + better service. Same external market, different aspiration, different investment level, different outcome.
- **Pattern**: The aspiration level determines the investment ceiling. Organizations that set modest aspirations explicitly or implicitly limit their investment below what winning requires. This is not a conscious choice — it's a consequence of the aspiration. "Good enough" as an unstated aspiration produces "good enough" resource allocation.
- **When it works**: Recognizing this pattern allows you to challenge under-investment by challenging the underlying aspiration: "Are we aiming to win here, or to participate? Because the investment we're putting in implies participation."
- **Related**: FB-023 (playing not to lose), Winning Aspiration in domain/ Strategy section

## Decision Patterns

### Plan in Analog Before Digital
- **Date identified**: 2026-03-19
- **Observations**: (1) Jobs storyboarded presentations on paper/whiteboards before opening Keynote. (2) Nancy Duarte recommends spending 2/3 of prep time on story, only 1/3 on slides. (3) Southwest Airlines was founded on a napkin sketch of three cities. (4) Cranium board game was sketched on a cocktail napkin.
- **Pattern**: The best ideas take shape on paper first. Jumping straight to digital tools (slides, Figma, code) constrains thinking.
- **When it works**: Early-stage ideation, product vision, presentation planning, strategy sessions.
- **When it fails**: When the problem is well-defined and execution speed matters more than creative exploration.
- **Related**: Headline Technique, Story-First frameworks

### The Antagonist-Hero Narrative
- **Date identified**: 2026-03-19
- **Observations**: (1) 1984 Mac launch: IBM as villain, Mac as hero. (2) iPhone launch: existing smartphones as villain, iPhone as hero. (3) Safari launch: slow browsers as villain, Safari as hero. (4) iPod launch: clunky MP3 players as villain, iPod as hero. (5) Al Gore's An Inconvenient Truth: fossil fuels as villain.
- **Pattern**: Every compelling product story follows problem-then-solution structure. Introduce the antagonist (pain point, competitor, limitation) before revealing the hero (your product/solution). The brain craves meaning before details.
- **When it works**: Product launches, sales pitches, investor presentations, stakeholder buy-in for new initiatives.
- **When it fails**: Internal technical reviews where the audience already knows the problem. Over-dramatizing minor improvements.
- **Related**: "Why Should I Care?" principle, Elevator Pitch framework

## Frameworks in Practice

### The Rule of Three
- **Date added**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 5
- **Theory**: Human short-term memory retains 3-4 items optimally. Structure any communication around three key points.
- **Reality**: Astonishingly consistent in practice. Jobs used it in virtually every presentation: three revolutionary products (iPhone launch), three parts to Apple (Mac, iPod/iTunes, iPhone), three stories (Stanford commencement). Kennedy's speeches, Obama's speeches, Marine Corps organizational structure, DuPont's crisis response all use groups of three.
- **Best for**: Any communication that needs to be remembered. Product messaging, feature prioritization for pitches, roadmap themes, meeting agendas.
- **Pitfalls**: Forcing unrelated items into three groups. Using it so mechanically it becomes predictable. Four is acceptable when natural.

### The Headline Technique
- **Date added**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 4
- **Theory**: Create a one-sentence description of your product/initiative that is concise (<140 characters), specific, and offers a personal benefit. Repeat it consistently across all channels.
- **Reality**: Jobs's headlines drove media coverage verbatim. "1,000 songs in your pocket" became the AP headline. "The world's thinnest notebook" appeared in 30,000+ articles. Google's pitch to Sequoia: "Google provides access to the world's information in one click" (10 words).
- **Best for**: Product launches, positioning statements, investor pitches, internal initiatives that need organizational buy-in.
- **Pitfalls**: Headline too generic ("innovative solution"). Headline that describes features instead of benefits. Inconsistent use across channels.

### Aristotle's Five-Point Persuasion Plan
- **Date added**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 1
- **Theory**: (1) Arouse interest with a story or statement. (2) Pose a problem. (3) Offer a solution. (4) Describe specific benefits. (5) State a call to action.
- **Reality**: Jobs followed this exact structure. Every keynote opened with an engaging hook, established a problem, introduced Apple's solution, described benefits in plain language, and ended with "Now go out and buy one!"
- **Best for**: Any persuasive communication: exec reviews, product pitches, change management.
- **Pitfalls**: Skipping step 2 (the problem). Going straight from problem to call-to-action without clearly articulating benefits.

### Nine Elements of Great Presentations
- **Date added**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 1
- **Theory**: Every powerful presentation incorporates: (1) Headline, (2) Passion statement, (3) Three key messages, (4) Metaphors/analogies, (5) Demonstrations, (6) Partners, (7) Customer evidence, (8) Video clips, (9) Props/show-and-tell.
- **Reality**: Jobs used all nine consistently. Most business presentations use zero to two of these.
- **Best for**: Checklist when preparing any high-stakes presentation.
- **Pitfalls**: Trying to cram all nine into a short presentation. Missing the most important ones (headline, three key messages, customer evidence).

### The Holy Shit Moment
- **Date added**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 13
- **Theory**: Script one emotionally charged, unexpected moment per presentation. It creates a dopamine release that acts as a "chemical Post-it note" in the brain, making the experience memorable.
- **Reality**: MacBook Air from a manila envelope. iPod from Jobs's pocket. Macintosh speaking for itself in 1984. These moments dominated news coverage and became the images people remembered for decades.
- **Best for**: Product launches, major announcements, keynotes. Even simple presentations benefit from one unexpected reveal.
- **Pitfalls**: Making the moment about spectacle rather than reinforcing the core message. Failing to rehearse the moment so it falls flat.

### Simplicity as Design Principle (Kanso)
- **Date added**: 2026-03-19
- **Source**: Gallo, *Presentation Secrets of Steve Jobs*, Scene 8
- **Theory**: Zen concept of kanso (simplicity). Remove everything that isn't essential. Applies to products, slides, and language.
- **Reality**: Average PowerPoint slide has 40 words. Jobs's first four slides at Macworld 2008 had 7 words total. His products stripped away buttons, features, complexity. Hans Hofmann: "The ability to simplify means to eliminate the unnecessary so that the necessary may speak."
- **Best for**: Slide design, product design, messaging, writing.
- **Pitfalls**: Oversimplifying to the point of being vague. Removing necessary context.

## Stakeholder Templates

### The Elevator Pitch (Four Questions)
- **Date added**: 2026-03-19
- **Context**: When you need to explain your product/initiative in 30 seconds.
- **Template**: Answer four questions in one sentence each: (1) What do you do? (2) What problem do you solve? (3) How are you different? (4) Why should I care?
- **Key phrases**: "What that means to you is..." (Jobs's signature bridge from feature to benefit)
- **Variations**: For investors, emphasize market size after the four questions. For customers, lead with the problem. For executives, lead with the business impact.

### The Bucket Method for Q&A
- **Date added**: 2026-03-19
- **Context**: Preparing for tough questions in any setting: exec reviews, board meetings, press, customer meetings.
- **Template**: (1) Identify the most common questions likely to be raised. (2) Categorize them into ~7 buckets. (3) Create the best answer for each category (answer must work regardless of how the question is phrased). (4) Listen for trigger words that map to a bucket. (5) Respond with confidence.
- **Key phrases**: "Our view on [trigger topic] is..." "What's important to understand about [trigger topic] is..."
- **Variations**: Works for product Q&A, analyst calls, media interviews, stakeholder pushback.

## Anti-Patterns

### Death by Bullet Points
- **Date identified**: 2026-03-19
- **Observations**: (1) Neuroscience research (Mayer, Medina) proves bullet points are the least effective way to deliver information. (2) Text recall after 72 hours: 10%. Text + picture: 65%. (3) Jobs never used bullet points. Not once. (4) Garr Reynolds calls bullet-heavy slides "slideuments" that kill effective communication.
- **Looks like**: Filling slides with text seems thorough and comprehensive.
- **Actually**: The brain sees words as tiny pictures, overloading cognitive processing. Bullet points demand note-taking, not attention. "The minute you put bullets on the screen you are announcing, 'Write this down, but don't really pay attention to it now.'" (Seth Godin)
- **Instead**: One theme per slide. Use photographs and images. Deliver information verbally. Let slides complement, not duplicate, your words.

### Solution Before Problem
- **Date identified**: 2026-03-19
- **Observations**: (1) Most entrepreneurs at TechCrunch 50 and DEMO failed because they jumped into their product without explaining the problem. (2) VC investor: "You need to create a new space in my brain to hold the information. It turns me off when entrepreneurs offer a solution without setting up the problem." (3) Most press releases fail because they announce products without establishing why anyone should care.
- **Looks like**: Getting excited about your solution and wanting to share it immediately.
- **Actually**: Without context (the problem), the brain has no bucket to place new information in. Primitive brain asks "Will it eat me?" not "How many teeth does it have?" Meaning before details.
- **Instead**: Establish the antagonist first. Even 30 seconds of problem framing transforms audience receptivity.

### The Capacity-Ask Mismatch
- **Date identified**: 2026-03-19
- **Observations**: (1) Experience Hub: 2 engineers, 15+ stakeholder teams with active requests. (2) Mihai (former lead engineer) left partly because PM-level work landed on engineering. (3) Security was the only team that actually contributed back — all others expected Experience Hub to build for them.
- **Pattern**: Small platform teams accumulate disproportionate ask volume because their product is high-leverage and visible. Without a formal contribution model and intake process, the team operates as a service desk. The PM spends all time managing requests, not setting direction. Engineers burn out. Good people leave.
- **When it works**: Naming the pattern explicitly to leadership ("we are a platform, not a service desk") creates the conditions to set boundaries and build a contribution model.
- **When it fails**: When the PM tries to say yes to everything to avoid conflict. The team loses, and the PM loses credibility for not protecting capacity.
- **Fix**: (1) Explicit contribution model — teams that want features must build them. (2) Formal intake process with written prioritization criteria. (3) Leadership backing to say no.

### The Vision-Reality Gap Pattern
- **Date identified**: 2026-03-23
- **Observations**: (1) AEM employee meeting showed a vision mock of Experience Hub, not the actual product. Multiple stakeholders formed expectations the team cannot meet. (2) Shankari's own diagnosis: "The value of Experience Hub is not presented upfront to users." (3) AI products especially prone to this because controlled demo environments don't expose architectural limitations.
- **Pattern**: A compelling vision demo is shown before the product exists. Stakeholders internalize the vision as the product. Every real interaction with the actual product disappoints relative to the memory of the demo. Trust erodes gradually and silently.
- **Why it happens**: It's tempting to show what's possible rather than what exists. Vision demos inspire; product demos disappoint. Leaders want to be inspired. Product teams want to impress.
- **Fix**: Name the gap explicitly and early. "What you saw was a vision mock. Here is what exists today. Here is the gap. Here is when it closes." The reset is uncomfortable once. The alternative is permanent credibility erosion.

### Earn the Right to Distribute — Stable Infrastructure Before Broad Sharing
- **Date identified**: 2026-03-30
- **Observations**: (1) Bertrand's first reaction to good agent report data was to ask for a stable URL before distributing it further. (2) Reports sent as zip files are perceived as one-offs regardless of their quality. (3) A permanent URL signals infrastructure; an attachment signals a draft.
- **Pattern**: Senior stakeholders implicitly evaluate whether a tool is ready to scale before investing attention in its content. Good data sent without a home looks like it will disappear. Good data at a stable URL looks like a system. The hosting question comes before the content question.
- **When it works**: Having a hosting answer ready when you share new data tools. Even a rough URL converts "interesting experiment" to "real infrastructure."
- **When it fails**: When teams focus entirely on content quality and ignore distribution mechanics. The best report no one can find again has no leverage.

### Parallel Artifact Streams Diverge — Always Check the Latest Version
- **Date identified**: 2026-03-31
- **Observations**: (1) Pedro's .md product reports and Felix's HTML reports are two separate streams for the same data. Felix's HTML was more advanced and already had Quality/Gap split + JIRA column structure — features incorrectly assumed to be missing because only the .md reports were checked. (2) In multi-track reporting work, the track you're not actively working on can advance without your knowledge.
- **Pattern**: When two parallel artifact streams exist (e.g. fast PM reports + engineering-built dashboards), they drift apart over time. Assuming they're in sync without verification causes duplicated work, missed capabilities, and wrong gap analysis.
- **Fix**: Before declaring something missing, check the latest version of every artifact stream. Read the HTML, not just the markdown. The stream you didn't write moves independently.
- **Application**: Whenever doing a gap analysis against someone else's artifact, read their artifact first. Not the version you remember from last week — the current file.

### Pilot a New Model Through an Existing Feature, Not a New Build
- **Date identified**: 2026-03-31
- **Observations**: (1) Eugene Bannykh proposed using +Add Extension (an existing EH feature) as the pilot mechanism for the contribution model — instead of building a new contribution infrastructure from scratch. (2) The feature already exists; the model being tested is the governance and collaboration process around it.
- **Pattern**: When proposing a new operating model (contribution model, collaboration process, review workflow), find the feature that already exists and run the pilot through it. This reduces engineering risk, shortens the feedback loop, and produces evidence with real constraints rather than hypothetical ones.
- **Why it works**: A pilot through an existing feature fails fast on the real friction (permission model, quality gate, team adoption) without waiting for new infrastructure to be built. If the model doesn't work with the existing feature, building a new surface for it won't fix the underlying problem.
- **Application**: Before committing to build new tooling for a process change, ask: is there an existing feature that could carry a pilot version of this? Use it. Build new only once the process is proven.

### Identify the Scaling Constraint Before Committing to a Model
- **Date identified**: 2026-03-31
- **Observations**: (1) Pedro's immediate response to Eugene's contribution model proposal: "Can we build an automated quality check? If yes, model works. If not, we'd be the bottleneck." (2) Manual quality gates in platform teams always become the bottleneck at volume — the PM reviewing every contribution becomes the ceiling.
- **Pattern**: Before committing to any operational model that involves a review or gate, ask explicitly: what happens at 10x volume? Who or what does the checking? If the answer is "a human on the PM or design team," the model has a built-in ceiling. Identify the scaling constraint before the model is ratified, not after you've already committed to teams.
- **The automation question**: In 2026, many manual quality gates can be partly or fully automated. AI/Claude can check design standard compliance, accessibility basics, metadata completeness, conversion metric declaration. The question "can this be automated?" should be asked at model design time, not after the bottleneck appears.
- **Application**: When designing any review-gated contribution model, write out explicitly: (1) what does the gate check; (2) who/what does the checking; (3) what is the expected volume; (4) at what volume does the gate become a bottleneck; (5) what is the automation path?

### Platform Contribution Model with Quality Gate
- **Date identified**: 2026-03-31
- **Observations**: (1) Experience Hub had 15+ teams requesting features from 2 engineers — unsustainable service desk dynamic. (2) Security was the only team that contributed back — proved self-service is possible. (3) EH Evolution proposal explicitly separates what EH gates (design, metric, lifecycle, testing) from what contributing teams own (build, data, monitoring).
- **Pattern**: Small platform teams cannot scale by building everything for consuming teams. The right model: define a contribution framework where consuming teams own their own features, and the platform team owns the quality bar. Platform team provides standards, component library, and approval gate. Consuming teams provide the build and the maintenance.
- **Three conditions for it to work**: (1) A published standard — teams need to know what "good" looks like before they build. (2) A gate with teeth — platform PM must be willing to reject contributions that don't meet the standard. (3) At least one proof point — one team that successfully contributed validates the model for others. Security in EH is that proof point.
- **What the gate covers**: Design standards, conversion metric, time-to-live (TTL) commitment, test evidence.
- **When it fails**: When the platform PM says yes to everything to avoid friction. The surface becomes noise, users stop trusting it, and the original problem (too many asks, too few engineers) is worse than before.

### Dashboard as Platform, Not Bulletin Board
- **Date identified**: 2026-04-15
- **Source**: Mike Tilburg (Modernization Agent PM) asked Pedro to merge his more complete report into the agent dashboard. Mike's report doesn't go through AO; uses different data pipeline. Motivation: personal visibility.
- **Pattern**: The moment your dashboard starts being seen as valuable, other PMs will ask to be included for visibility. If you say yes without conditions, you turn a platform into a bulletin board — a collection of whatever people want to post, with mismatched methodologies, inconsistent data sources, and no shared standard. Executives who look at the dashboard assume internal consistency; inconsistency confuses them and destroys trust in the artifact.
- **Three reasons to refuse an ad hoc merge**: (1) Architecture: different pipelines in the same surface without clear labeling mislead readers who assume comparability. (2) Identity: the dashboard is defined by what it is AND by what it isn't — letting any agent in dilutes the "what it is." (3) Governance hypocrisy: if you're asking other teams to meet shared standards (contribution model), you can't apply looser rules to your own platform.
- **Right response (the platform move)**: Do not refuse the person — refuse the ad hoc merge. Offer two paths: (1) indexed link from the dashboard, with a methodology note, for immediate visibility; (2) full integration later, conditional on meeting shared metrics and data source standards. This preserves architectural integrity, gives the requester visibility, sets precedent for future asks, and positions the PM as the platform's gatekeeper rather than its concierge.
- **Why it matters for Senior Director path**: Directors run service desks. Senior Directors run platforms with rules. The first time someone asks you to bend the rules for their visibility is the test — saying no (with a clean alternative) is the act that makes the platform a platform.

### TTL + Priority + Role-Linking — The Shared Surface Card System
- **Date identified**: 2026-03-31
- **Observations**: (1) EH announcement widget managed manually — teams asked EH engineers to create/update cards. (2) Experience Hub voice note (Pedro, March 30): proposed automated card creation with TTL, priority ranking, and role-linked display. (3) Shankari's 4-week rule enforced manually — TTL automates the enforcement.
- **Pattern**: In any shared surface where multiple teams want to publish content (announcements, cards, prompts, widgets), a four-mechanic system prevents the surface from becoming noise: (1) Self-service creation — teams submit, PM approves; (2) Priority ranking — set by platform PM, not contributing team; (3) Time To Live — every item expires automatically unless renewed with performance data; (4) Role-linking — items display only to the profiles they're relevant for.
- **Why this works**: It turns a human governance process (Shankari manually enforcing the 4-week rule) into an automated one. The PM's role shifts from "enforcer of expiry dates" to "setter of the system rules." Teams know the rules upfront and self-select accordingly.
- **Connection to contribution model**: This is the contribution model applied to content publishing. The same principles (teams own, platform gates) apply to both widgets and cards.

### Nominal Capacity vs Real Capacity — Plan to What's Actually Available
- **Date identified**: 2026-04-01
- **Source**: Sorin 1:1 April 1 — confirmed effectively 1 engineer despite 3 names on the team roster.
- **Observations**: (1) Experience Hub headcount: Sorin (split across multiple projects), Anna Maria (new intern, not yet ramped), Mircea Salan (internship project, limited scope). Nominal count is 3. Real capacity is ~1. (2) Hiring pipeline best-case adds capacity in May-June — worst case not until summer or positions closed. (3) Sorin's own framing: "We are not a big house, but we are a proud house."
- **Pattern**: Team headcount in org charts and project charters describes the nominal team — the people assigned. Real capacity is determined by: (1) effective bandwidth per person (how much of each person's time is actually allocated to this work); (2) ramp time for new hires and interns; (3) in-flight commitments that can't be dropped. The gap between nominal and real is usually 40-60% in large orgs.
- **Why this matters for roadmaps**: A roadmap built to nominal capacity will miss. A roadmap built to real capacity will ship. Planning to nominal looks ambitious. Planning to real looks like leadership.
- **Application**: Before finalizing any roadmap or quarterly plan, convert headcount to effective bandwidth. For each team member: what % of their time is actually available for new work in this cycle? That number is the planning constraint. Declare 3 engineers for planning purposes if 5 is the minimum needed — but build the roadmap to 3.

### Precise Question Gets Precise Compliance Answer
- **Date identified**: 2026-04-01
- **Source**: Pedro's outreach to Ian Boston April 1 — framed as specific data compliance questions, received detailed legal risk confirmation.
- **Observations**: (1) Vague PM questions ("do you have any concerns?") generate vague responses ("yeah, a few things to watch"). Precise technical questions ("does cross-region aggregation of AEP prompt data violate data residency requirements?") generate precise answers with legal framing and specific risks named. (2) Ian's response confirmed two distinct legal risks — Data Residency (contractual) and Data Governance (deposition) — because the question was scoped enough to draw out both.
- **Pattern**: When reaching out to technical or legal stakeholders on a risk question, do the pre-work first. Understand enough about the architecture and the regulatory context to ask a specific question. Specific questions are easier to answer — and harder to dismiss. They also signal that you've done homework, which earns a more thorough response.
- **Application**: Before sending a Slack or email to an SME on a risk topic, write down the specific mechanism you're asking about. "Is X happening? If yes, does it violate Y?" beats "any thoughts on the data stuff?"

### Preview Link Pattern — Ship Fast for a Fixed Event Without a Production Commitment
- **Date identified**: 2026-04-01
- **Source**: Sorin Slavic in April 1 EH refinement sync — Brand Concierge Summit options discussion.
- **Observations**: (1) Summit deadline (April 19-22) made full production implementation impossible in 2 weeks. Sorin proposed using a preview link — automatically generated for in-progress changes, gives full integration and real behavior, but is not merged to production. (2) Security team previously used a similar approach for early demos. (3) The pattern separates "does it work?" validation from "is it production-ready?" quality assurance.
- **Pattern**: When a fixed event (summit, exec demo, customer pilot) creates a hard deadline that production quality cannot meet, use the preview link approach: write the code, bypass production guardrails, generate a preview link for the specific demo context. After the event, decide whether to invest in making it production-ready or remove it.
- **Conditions**: (1) The audience is known and controlled — you know exactly who will click it and in what sequence. (2) The event is time-bounded — it's not a permanent commitment. (3) There's an explicit plan for what happens after — either productionize or remove.
- **Risk**: If the preview version leaks or gets treated as a commitment, you've created expectations you haven't shipped to. Be explicit upfront: "This is a Summit-only preview, not a product commitment."
- **Application**: Before saying "we can't do this in time for the event," ask whether a preview link version is viable. It often is, and it lets the event happen without blocking a production decision.

### Hard Deadlines Force Scope Clarity Faster Than Any Planning Process
- **Date identified**: 2026-04-01
- **Source**: Brand Concierge Summit discussion, April 1 EH refinement sync.
- **Observations**: (1) Brand Concierge light-up had been ambiguous for weeks — full implementation vs announcement card vs wizard, no decision. Summit on April 19-22 forced a clear three-option framework and a decision by tomorrow. (2) The same pattern appears in every release cycle: the week before a deadline, more decisions get made than in the prior month.
- **Pattern**: If a decision has been stuck for weeks, create or name a forcing event. The constraint of a real deadline — especially an external one like a summit or customer meeting — collapses the option space faster than any internal planning discussion.
- **Application**: When a decision is drifting, ask: is there an upcoming event that makes the cost of not deciding concrete? If yes, use it. Frame the decision in terms of what the event requires, not in abstract terms.

### Explicit Sequence as Protection Against Spread
- **Date identified**: 2026-04-02
- **Source**: Pedro's decision to sequence AI Assistant workstream items rather than run them in parallel, April 2, 2026.
- **Observations**: (1) Pedro had 10+ active items across the AI Assistant workstream — Felix integration, hosting, JIRA pipeline, MCP tracking, Ilya sync, VRR definition, etc. (2) Explicit decision: "I don't want to spread too thin." Defined four items in order: Felix changes → hosting → JIRA pipeline → MCP reporting. (3) MCP tracking explicitly parked: "not before items 1–3 are done."
- **Pattern**: Having priorities is not enough. Having a sequence is what prevents spread. A list of 10 orange items all looks equally urgent. A numbered sequence with an explicit "not before X" rule creates a forcing function — you know what to say no to right now, not just in general.
- **Why this matters for Senior Director visibility**: A PM who shows up to every conversation with a clear sequence and a clear "not this yet" signal operates differently than one who is responsive to every new request. Sequence is a form of strategic communication. "We're doing X, then Y, then Z — this new ask is after Z" is a leadership statement, not a deflection.
- **Application**: For any workstream with more than 5 active items, write the sequence explicitly. Not a priority ranking — an actual order. Then apply "not before [previous item]" to everything that isn't at the top.

### PM as Gating Layer in Automated Pipelines
- **Date identified**: 2026-04-02
- **Source**: Philippe Kapfer's feedback on the report-to-JIRA trial, April 2, 2026.
- **Observations**: (1) Auto-created JIRA stories from the EGA report trial created overhead — some were duplicates, some partially relevant. Philippe's first ask was a manual trigger, not better filters. (2) The "fluffyjaw" reference signals a prior experience with noisy auto-created tickets that eroded trust in an automated system. (3) His framing: "Once the quality improves, we can decide to automate." The gate is a trust-building step, not a permanent constraint.
- **Pattern**: When automation creates work items that land directly in a PM's or engineer's backlog, the PM needs a review gate before creation — not after. Automating past that gate produces noise, creates cleanup work, and erodes trust in the pipeline. The right model: pipeline generates *candidates*, PM reviews and approves, then artifacts are created. The gate is the product.
- **Why this matters**: A backlog is a prioritized, trusted list. Every low-quality item added to it degrades the signal of the whole list. PMs protect their backlogs the way engineers protect their codebase — and for the same reason.
- **The trust ladder**: Manual trigger (PM approves every story) → curated auto (PM sets rules, reviews exceptions) → full auto (proven quality, PM spot-checks). Don't skip steps.
- **Lightweight gating mechanism**: Slack notification with candidate list before JIRA creation. PM responds with approval or filters. Only confirmed items become stories. No additional tooling required.
- **Application**: Before automating any workflow that creates work items for another team, ask: does this person's backlog have a trust contract? If yes, get their approval on the gating model before running the first batch. Start with manual trigger regardless of what's technically easier.

### Jargon as a Sign of Insecurity
- **Date identified**: 2026-03-19
- **Observations**: (1) Jobs vs Gates language analysis: Jobs scored dramatically better on every readability metric. (2) Jack Welch despised jargon and fired a leader who couldn't explain his business simply. (3) Suze Orman: "It's our fear of not being important that leads us to communicate in a more complex way than we need to." (4) Mission statements are the worst culprits.
- **Looks like**: Using complex language sounds smart and authoritative.
- **Actually**: It signals insecurity and creates distance. Einstein: "If you can't explain it simply, you don't understand it well enough."
- **Instead**: Use simple, concrete, emotional words. Run text through readability tools. If a high schooler can't understand it, rewrite it.

---

## Strategic Patterns (from Greene, *The 33 Strategies of War*)

### Polarity Creates Momentum — Vagueness Kills It
- **Source**: Greene, *The 33 Strategies of War*, Strategy 1: The Polarity Strategy
- **Date**: 2026-04-02
- **Observations**: (1) Thatcher won elections by drawing sharp ideological lines that most politicians avoided. Her clarity repelled some voters but activated others far more strongly. Her poll numbers were lower than her opponents', yet she won. (2) Xenophon's Greeks found direction only when they defined who their enemy was — before that they were dissolving into argument and despair. Without polarity, there is no energy.
- **Pattern**: Clear positions — even controversial ones — generate more movement than careful hedging. In product work, a sharp "we will not do X" is more energizing than "we'll consider everything." Choosing what you're against creates definition. Definition creates momentum.
- **When it works**: When you have enough credibility and context to take the position. When the organization needs direction more than it needs consensus.
- **When it fails**: When the position is taken without relationships or evidence to back it. When you polarize before you've built the coalition you need.

### Adapt the Approach, Hold the Objective
- **Source**: Greene, *The 33 Strategies of War*, Strategy 2: Do Not Fight the Last War
- **Date**: 2026-04-02
- **Observations**: (1) Musashi changed his weapons, timing, and tactics with each duel — arriving late for some, early for others, using a wooden oar instead of a sword against Ganryu. He won every time by reading the specific opponent rather than applying a formula. (2) Napoleon's genius was precisely that he had no fixed principles — he adapted to circumstances completely.
- **Pattern**: The best strategists separate the unchanging objective (get home, win the duel, ship the feature) from the changeable method (how you get there). Past success at a method is a liability if you apply it mechanically to a new situation. The method should always be provisional; the goal should not be.
- **When it works**: In fast-changing environments (AI, new markets, new org structures). When the opponent/situation is novel.
- **When it fails**: When mistaking tactical flexibility for strategic drift — changing objectives as often as methods produces nothing.

### Thorough Preparation = Permission to Appear Unflappable
- **Source**: Greene, *The 33 Strategies of War*, Strategy 3: Do Not Lose Your Presence of Mind (The Counterbalance Strategy)
- **Date**: 2026-04-02
- **Observations**: (1) Hitchcock's famous on-set calm was not temperamental — it was earned. He had storyboarded every shot, designed every costume, blocked every scene before cameras rolled. His nonchalance was preparation made visible. (2) Nelson at Copenhagen could ignore the order to retreat because he had studied the sandbar maps, knew the winds, and had already war-gamed the scenario. He had earned his confidence.
- **Pattern**: The PM who appears calm under fire isn't naturally unflappable — they prepared more than everyone else. Presence of mind in high-stakes moments (exec reviews, escalations, unexpected challenges) is the output of pre-work: anticipating objections, knowing the data, understanding the stakeholder. The calm is a signal of preparation, not temperament.
- **When it works**: When you've done the work before the meeting, not during it.
- **When it fails**: When the preparation was shallow and the calm is fake — it breaks under real pressure and the credibility hit is worse than admitting uncertainty upfront.

### The Alliance Strategy — Build Coalitions That Do Your Work
- **Source**: Greene, *The 33 Strategies of War*, Strategy 27: Seem to Work for the Interests of Others While Furthering Your Own (The Alliance Strategy)
- **Date**: 2026-04-02
- **Observations**: (1) The most effective political players in any organization create networks of people who want the same outcome for their own reasons. (2) Greene's examples show that alliances built on apparent mutual benefit last longer than those built on pure loyalty. People stay in alliances when they see what they get from it.
- **Pattern**: Cross-org influence at scale doesn't work by convincing everyone of your vision. It works by identifying what each stakeholder already wants, finding the overlap with your goal, and framing your initiative as the thing that gives them what they want. You're not changing their minds — you're showing them a path to their own objectives.
- **When it works**: When you genuinely understand what the other party cares about. When your initiative really does help them, not just as rhetoric.
- **When it fails**: When the alignment is artificial. When the benefit to the ally evaporates once your goal is achieved — they'll remember.

### Take Small Bites — The Fait Accompli Pattern
- **Source**: Greene, *The 33 Strategies of War*, Strategy 29: Take Small Bites (The Fait Accompli Strategy)
- **Date**: 2026-04-02
- **Observations**: (1) Greene demonstrates through historical examples that overt power grabs trigger resistance and resentment, while gradual accumulation of territory goes largely unnoticed until it's too late to reverse. (2) John D. Rockefeller's consolidation of the oil industry happened through dozens of small acquisitions before anyone understood the scale of what he was building.
- **Pattern**: Large organizational changes that are proposed and announced as large changes get blocked or diluted. The same changes, introduced as a series of small, reasonable steps, each individually defensible, accumulate without triggering the immune response. This is not manipulation — it is sequencing strategy in a way that lets each step be absorbed before the next is proposed.
- **When it works**: When the end state is genuinely beneficial but would face political resistance if proposed all at once. When you have patience.
- **When it fails**: When the small steps don't actually build toward the goal (drift). When the incremental nature is used to obscure a genuinely bad end state from people who should evaluate it.

### Penetrate Minds Indirectly — Communication Strategies for Influence
- **Source**: Greene, *The 33 Strategies of War*, Strategy 30: Penetrate Their Minds (Communication Strategies)
- **Date**: 2026-04-02
- **Observations**: (1) Greene argues that direct argument activates defensiveness — the recipient starts looking for reasons to disagree. Indirect communication bypasses this reflex: stories, demonstrations, letting people arrive at the conclusion themselves. (2) The most effective influence is when the other person thinks they had the idea.
- **Pattern**: The PM who walks into a room and says "here is what we should do" will fight resistance. The PM who asks the right questions, presents the right data, tells the right story, and lets the senior person "discover" the conclusion gets the same outcome with a tenth the friction. This is not manipulation — it is reading how human persuasion actually works and working with it, not against it.
- **When it works**: In high-authority-differential situations (skip-levels, C-suite). When you need durable commitment, not just compliance.
- **When it fails**: When speed is paramount and indirect routes take too long. When the other party prefers directness and finds indirectness evasive.

### Study What's Missing — The Ideal Listener Pattern
- **Source**: Greene, *The Art of Seduction*, The Ideal Lover chapter (Casanova, Madame de Pompadour)
- **Date**: 2026-04-02
- **Observations**: (1) Casanova's method: study the gap between what each person has and what they secretly want, then provide it. Pompadour read Louis XV's boredom with formality and provided theater, games, and creative stimulation. (2) Talleyrand survived Napoleon's regime by making himself indispensable — he gave Napoleon the flattery of intellectual peer engagement that no one else offered. (3) Greene's pattern across all Ideal Lover examples: most people are not getting something important they need. Provide it and they become deeply loyal.
- **Pattern**: Before any important stakeholder interaction, map the gap — what do they have, and what are they not getting? The most effective form of influence is not better arguments; it is providing something the other person wants that they're not currently receiving. This requires actual observation, not projection.
- **When it works**: When you've done the homework and the gap you fill is real. When what you provide costs you little but matters a lot to them.
- **When it fails**: When you manufacture a gap or project your own needs. When it becomes transactional — they notice.

### Reflect Their Values Back — The Mirror Pattern
- **Source**: Greene, *The Art of Seduction*, The Charmer chapter (Charmer as mirror symbol)
- **Date**: 2026-04-02
- **Observations**: (1) The Charmer's symbol is the mirror: in your presence, others see themselves — their values, their tastes, their ideas — reflected back approvingly. They fall in love with their own reflection. (2) Disraeli's method with Victoria: treated her opinions as statecraft, her ideas as serious policy, called her "we authors" after reading her diary. (3) People who feel understood by you become dependent on you.
- **Pattern**: When you need to build trust quickly with a new stakeholder, find what they care about and demonstrate genuine understanding of it. Not flattery — actual comprehension. Ask questions that show you've thought about their world. Reference their specific challenges. The goal is not agreement; it is the feeling of being truly seen.
- **When it works**: In early relationship stages. When entering a new team or org. When managing upward with a new skip-level manager.
- **When it fails**: When it is pure performance without genuine interest — people eventually sense the hollow. When overused it becomes sycophancy.

### Yield to Win — Strategic Deference in High-Stakes Situations
- **Source**: Greene, *The Art of Seduction*, The Charmer chapter (Zhou Enlai / Catherine the Great examples)
- **Date**: 2026-04-02
- **Observations**: (1) Catherine the Great spent years deferring to Empress Elizabeth, her impossible husband Peter, and the entire Russian court — all while building the network and reputation that carried her into power. She got there without a battle. (2) Zhou Enlai told Stalin China had much to learn from the Soviets — got a better treaty than China's position deserved. (3) Greene's principle: "charm is a manipulative weapon that disguises its own manipulativeness, letting you gain a victory without stirring the desire for revenge."
- **Pattern**: When you are in a weaker structural position than the person you need to influence, direct assertion is usually the wrong tool. Strategic deference — appearing to accept their superiority, making them feel the initiative is theirs — removes their desire to fight you. You get the outcome without forcing the confrontation. This is not submission. It is patience in the service of the goal.
- **When it works**: Early in a new role when you're building credibility. When a senior stakeholder needs to feel in control of the narrative. When forcing a conclusion would create a resistant enemy who remembers the loss.
- **When it fails**: When mistaken for actual weakness and the other party starts to disregard you entirely. Must be paired with moments of clear, visible competence.

### Consistent Follow-Through as the Rare Differentiator
- **Source**: Greene, *The Art of Seduction*, The Charmer chapter ("Follow-through is key")
- **Date**: 2026-04-02
- **Observations**: (1) Greene: "Anyone can make a promise. What sets you apart is your ability to come through in the end, following up your promise with a definite action." (2) In a world of "bluff and smoke, real action and true helpfulness are perhaps the ultimate charm." (3) Pamela Churchill built a political empire not through brilliance but through making everyone she promised something to feel uniquely delivered to.
- **Pattern**: In corporate environments, most people over-promise and under-deliver, or make implicit commitments that evaporate. The PM who consistently does what they said — returns the email, writes the doc, follows up on the action item, remembers the conversation — stands out not by being dramatic but by being reliable. Over time, reliability becomes trust, and trust becomes influence.
- **When it works**: Always. This is a compounding behavior.
- **When it fails**: The only failure mode is promising things you don't do. The solution is to under-promise and over-deliver, or simply to say no upfront rather than yes with no follow-through.

---

## Power Patterns (from Greene, *The 48 Laws of Power*)

### Concentrate Force at One Point — Single Decisive Blow
- **Source**: Greene, *The 48 Laws of Power*, Law 23 (Concentrate Your Forces) and Law 29 (Plan All the Way to the End)
- **Date**: 2026-04-02
- **Observations**: (1) Rothschild's fortune was built on concentration, not diversification — single source, the British government debt, rather than spreading across markets. (2) Rommel's desert campaign succeeded through concentrated mobile force, not static defense. (3) Greene: "Intensity defeats extensity every time."
- **Pattern**: In resource-constrained environments (which all PM environments are), spreading attention creates average results everywhere. Concentrating all available force on one goal or one product surface creates breakthrough results that compound. The temptation is to cover everything. The discipline is to choose one thing and make it undeniable.
- **When it works**: When you can correctly identify the one thing that has the highest leverage. When the organization will let you focus.
- **When it fails**: When the "single point" is wrong. When dependencies on other workstreams are so tight that concentration ignores real constraints.

### Court Attention — Absence and Presence as Instruments
- **Source**: Greene, *The 48 Laws of Power*, Law 6 (Court Attention at All Cost) and Law 16 (Use Absence to Increase Respect and Honor)
- **Date**: 2026-04-02
- **Observations**: (1) P.T. Barnum manufactured controversy and spectacle because in his world indifference was the only real death. (2) Geronimo's value to the US cavalry rose dramatically after his surrender — his absence from the field made his presence at exhibitions mythic. (3) The Duke of Deuxponts example: refused to be seen in public during a period of unpopularity, returned to a court hungry for his presence.
- **Pattern**: Visibility must be managed, not maximized. Too much presence and you become background noise. Strategic absence — not attending every meeting, being selectively unavailable — increases demand for your presence. The goal is not constant visibility but memorable visibility. Every appearance should be deliberate.
- **When it works**: When you have established a baseline of presence and credibility. Strategic absence only works if people know what they're missing.
- **When it fails**: Before you've established value. Absence from people who don't yet know your worth is just absence.

### Isolate the Key Blocker — Separate Before Confronting
- **Source**: Greene, *The 48 Laws of Power*, Law 42 (Strike the Shepherd and the Sheep Will Scatter)
- **Date**: 2026-04-02
- **Observations**: (1) Pope Boniface VIII isolated Dante Alighieri from the White faction in Florence — removing Dante from Florence destroyed the Whites as a political force. (2) Athens used formal ostracism to neutralize its most powerful citizens precisely when they were most dangerous. (3) Greene: "One resolute person can turn a flock of sheep into a den of lions."
- **Pattern**: When a cross-org initiative faces organized resistance, the resistance is almost never uniform. It has one or two people driving it. Identify who is the "shepherd" — the person whose energy and will sustain the opposition. Neutralize that person first (through alignment, isolation, or reframing), and the rest of the opposition loses cohesion. Do not fight the broad coalition; address the driving force.
- **When it works**: When the blocking force is genuinely concentrated in one person or small group. When you can reach that person through legitimate channels.
- **When it fails**: When resistance is genuinely distributed and principled, not driven by one champion. When isolating the shepherd makes them a martyr.

### Win Hearts Before Winning Arguments — Emotional Conversion First
- **Source**: Greene, *The 48 Laws of Power*, Law 43 (Work on the Hearts and Minds of Others)
- **Date**: 2026-04-02
- **Observations**: (1) Chuko Liang captured and released the enemy general Menghuo seven times, winning genuine loyalty rather than forced submission. Each release was a demonstration of strength and generosity. (2) Marie-Antoinette ignored the hearts of the French people and paid with her head. Coercion always creates a larger resistance behind the surface compliance. (3) Greene: "The quickest way to secure people's minds is by demonstrating, in actions rather than words, how an action will benefit them."
- **Pattern**: Technical correctness and logical arguments do not move people. What moves people is the belief that you understand them, care about their interests, and are acting in their favor. The PM who wins alignment by making the other party feel seen and benefited gets durable buy-in. The PM who wins by being logically right gets grudging compliance that evaporates when convenient.
- **When it works**: In any alignment situation where the other party has sufficient autonomy to resist. Cross-org stakeholders, platform consumers, product teams.
- **When it fails**: When you don't have the time or enough access to understand what the other party actually cares about. In crisis situations where speed requires directive behavior.

### Mirror to Disarm — Reflect Back to Neutralize
- **Source**: Greene, *The 48 Laws of Power*, Law 44 (Disarm and Infuriate with the Mirror Effect)
- **Date**: 2026-04-02
- **Observations**: (1) Fouché dismantled Napoleon's spy network by building his own that mirrored it exactly — Napoleon could not attack what looked like his own work. (2) The Narcissus Effect: Marie Mancini reflected Louis XIV's idealized self back to him — he fell in love with the vision. (3) Ivan the Terrible placed Simeon on the throne as a mirror, demonstrating to the boyars what they claimed to want — it horrified them into compliance. (4) The Hallucinatory Effect: Yellow Kid Weil recreated a fake bank with such accuracy that the illusion was indistinguishable from reality.
- **Pattern**: People cannot easily attack what looks like their own behavior or values reflected back at them. When faced with resistance, adopt the other party's language, framework, and stated values — then show how your initiative is a logical extension of what they already believe. They are fighting their own reflection.
- **When it works**: In cross-org situations where the other party has publicly stated values or priorities you can align with.
- **When it fails**: When the mirroring is obvious or feels manipulative. When there is no genuine connection between your goal and their stated values.

### Reform Gradually — Borrow From the Past to Change the Present
- **Source**: Greene, *The 48 Laws of Power*, Law 45 (Preach the Need for Change, but Never Reform Too Much at Once)
- **Date**: 2026-04-02
- **Observations**: (1) Cromwell's radical Protestant revolution — destroying every vestige of the past — triggered such massive resistance that it collapsed into chaos and his execution. (2) Mao cloaked Communist revolution in Robin Hood imagery from Chinese history ("Water Margin"), making radical change feel like a return to Chinese tradition. (3) Greene: "People are creatures of habit. Too much innovation can disturb them and destroy the familiar patterns they rely on."
- **Pattern**: Change is easiest when it looks like continuity. Frame new directions as extensions or improvements on existing practice, not departures from it. Connect the new to something the audience already values. The most successful product pivots are framed as "the natural next step" rather than "something completely different." The radicalism is in the execution, not the framing.
- **When it works**: In large orgs with established norms and risk-averse cultures. When you need broad buy-in from people who are comfortable with the status quo.
- **When it fails**: When the change is genuinely incompatible with the past and the framing becomes dishonest. When speed is required and gradual introduction creates its own risks.

## Artifact Architecture

### Roll-up vs Task Tracker — One Authoritative Home Per Piece of Information
- **Source**: Pedro session, April 24, 2026 (vault alignment pass)
- **Date**: 2026-04-24
- **Observation**: Pedro maintains a multi-tier planning structure: an OKR folder with a KR Board kanban, individual KR notes containing Todoist-backed task lists with IDs, and two Status & Todo files (EH + AAI; the AI-Assistant file was retired in the 2026-05-03 Phase 2 split) that serve as project-level rollups. When the Status files' Focus sections started inlining full task descriptions, they duplicated what the KR notes owned better. Drift followed immediately — a task could update in one place and stale in the other. Realignment: Focus rows hold Item + KR backlink + Status + Due only. Detail lives in the KR note, referenced by `[[KR Note|KR#]]` backlink.
- **Pattern**: In a multi-tier planning system, each tier serves a distinct function and each piece of information should live in exactly one authoritative place. The Orientation tier (kanban board / OKR objective) tells you what matters. The Operational tier (KR notes / task management tool) owns individual tasks, deadlines, and IDs. The Roll-up tier (Status files) tells you what is load-bearing this week with links into the operational layer for detail.
- **Design rule**: A Focus or Roll-up row should never duplicate a task list inside a KR or project note. The column structure forces this: Item / Link-to-detail / Status / Due. When tempted to add a sub-task list, add it to the KR note instead and let the roll-up link to it.
- **Adjacent pattern**: This is structurally similar to how good software documentation works — canonical content lives in one place, every other mention links to it. Duplication invariably drifts. The information-architecture discipline is the same in a PM planning system as in a codebase.
- **When it applies**: Any planning system with 2+ tiers of visibility (PM with OKRs + sprint + status updates; engineering with roadmap + epics + stories; any org that has both strategy-level and operational-level artifacts).
- **When it fails**: If the operational layer doesn't exist yet (no KR notes), the roll-up tier will need to carry detail temporarily — but this is a sign the operational layer is missing, not that duplication is correct.

### Calibration Audit — When a Priority List Stops Signaling
- **Source**: Pedro session, April 24, 2026
- **Date**: 2026-04-24
- **Observation**: Pedro's Status file had 12 items tagged 🔴 out of ~25 total. 🔴 had drifted from "highest-priority this week" to "still active" — which meant 🔴 no longer signaled anything. The symbol had lost its meaning. Same risk applies to any prioritization symbol (P0, high, starred, urgent) that is never pruned.
- **Pattern**: Priority symbols only work if they cost something to assign. When everything qualifies, nothing does. The calibration audit is periodic — count how many items carry the top label. If the count is more than ~5, the label has drifted and needs a rebalance. Demote or re-assign. The discipline is not to remove urgent items but to make "urgent" mean "top of mind, action this week" consistently.
- **Design rule**: Cap the top-priority label at a small number (4-5 for a Director roll-up). Anything beyond that cap is either miscoded or signals a capacity crisis. Either way, the audit surfaces it rather than letting the list silently grow.
- **When it applies**: Any tracking system where a priority label is meant to filter attention. Status files, JIRA boards, sprint planning, engineering dashboards.
- **When it fails**: If the cap is held mechanically rather than based on actual load-bearing-ness, important work gets artificially demoted. The cap is a calibration tool, not a quota — use judgment about what belongs above the line, then prune below.

### Dual-Track Source Tracking — Slack Parent vs JIRA Parent
- **Source**: Pedro session, April 28, 2026 (H2 2026 HC Rollup analysis)
- **Date**: 2026-04-28
- **Observation**: When mapping H2 2026 roadmap items to their parent initiatives, two sources gave conflicting answers. The Slack canvas (curated source doc, manually grouped under section headers like "DX Initiative: Adobe LLMO (LLMO-4023)") said one thing. The JIRA "implements" relationships (formal record, fetched via MCP) said another. For most items the two agreed. For LLMO-4141 they diverged: Slack said LLMO-4023, JIRA said DX-1134 (Closed). Both are useful artifacts; neither is enough on its own.
- **Pattern**: When a planning surface is curated by humans (slides, Slack canvases, Confluence pages) AND backed by a structured system (JIRA, Linear, Asana), the two diverge over time because curation reflects current intent while the structured system reflects formal record. Track both side-by-side in coordination artifacts. Mismatches are signals — usually that the formal record needs updating to match new intent (or that intent is drifting from what's been formalized).
- **Design rule**: For any "what is this item part of?" column in a planning rollup, show both the human-curated source (Slack Parent / Slide Parent / Doc Parent) and the structured source (JIRA Parent / Linear Parent). When they match, the columns reinforce. When they disagree, you have a finding worth surfacing.
- **When it applies**: Cross-team planning where curated summaries exist alongside ticket trackers. PM rollups for executive review. Initiative-to-roadmap mappings.
- **When it fails**: If the human-curated source is the only authority (no formal system) or if the structured system is the only one used (no narrative summary), there's nothing to dual-track. One column is enough.

### Narrative Claim vs Canonical Truth — Status-Tagged Promotion
- **Source**: Pedro session, April 28, 2026 (H2 HC Rollup HOME-832 + AEMAGT-538 placements)
- **Date**: 2026-04-28
- **Observation**: Pedro's own work (HOME-832 Experience Hub, AEMAGT-538 Experience Modernization) sits formally under DX-1222 "Cloud: Product Adoption" in JIRA. But for the May 4 narrative — "EH and Modernization are AEM agent surfaces" — Pedro wanted them visible in the DX-1220 "Agentic Web" table. The temptation was to relabel parents to match placement. The cleaner pattern: keep parents truthful in their columns + use a Status / Source column to mark "Pedro-driven" or "Pedro-promoted." Truth and narrative coexist.
- **Pattern**: When a leader is making a deliberate cross-initiative narrative claim (an item belongs in a different conversation than its formal home suggests), don't rewrite the formal record — annotate the placement. The artifact becomes a transparent narrative layer over canonical truth. Anyone reading the table can see both: where the work formally sits AND why the leader is presenting it differently.
- **Design rule**: Use a status / placement-reason column. Values like "Pedro-driven" / "Pedro-promoted" / "Bertrand-claimed" make the narrative move explicit. Parent columns stay truthful. Subtotal commentary explains the cross-initiative inclusion.
- **When it applies**: Roadmap rollups for executive narrative. Cross-initiative coordination tables. Promotion-case artifacts where scope claims need to be both truthful and visibly assertive.
- **When it fails**: When the leader hides the move (rewrites parents to match placement) — that produces a doc that looks clean but breaks down under scrutiny from finance, planning, or the source-of-record team. Transparency in the placement-reason is what makes the move durable.

---

### Three-Tier Intelligence Reporting Architecture

- **Date**: 2026-05-01
- **Source**: AEM Agent reporting evolution (per-agent weekly → Portfolio Monthly Briefing → AEM Agents QBR)
- **Pattern**: For cross-product or cross-agent intelligence work, three reporting tiers serve three distinct audiences from one data source. Senior leadership tier (quarterly, commercial framing, PMM-led) sits above a senior management tier (monthly, narrative, cross-portfolio) which sits above the operational tier (weekly, deep, routing surface). Each tier has a different cadence, register, and ownership — but they reconcile arithmetically because they share a single data layer.
- **When it applies**: A PM owns a portfolio of products / agents / surfaces with two or more layers of leadership consumption. A single weekly per-product report can't satisfy both the agent PMs (who need depth + routing) and the VPs (who need cross-portfolio narrative + commercial signal). Adding a monthly bridging tier with the right register resolves the "WoW data is too transactional" complaint at the metric layer.
- **Architecture statement worth saying out loud**: *"The QBR is the senior-leadership commercial view. The Portfolio Monthly Briefing is the management narrative. The per-agent reports are the working surface. Three artifacts, three audiences, one data source."* Naming the tiers explicitly is itself a Senior Director move — most PMs ship one report and let the audience self-select.
- **Authorship gradient**: PMM tends to own the senior-leadership tier (commercial). Portfolio PM owns the management tier (narrative + cross-portfolio rollup). Agent / product PMs own the operational tier (weekly routing). Mismatch happens when a PM tries to author at a tier above their accountability — common failure mode is shipping a "QBR" that's actually a per-product weekly report with a quarterly title.
- **Cuts matter as much as keeps**: The management-tier artifact must explicitly cut WoW data, per-customer named diagnoses, and capability gap rows. Those belong in the operational tier. Without disciplined cuts, the management tier collapses back into a glorified weekly.
- **Time and budget**: Tier 1 (operational) is the highest investment — it's where the data layer lives. Tier 2 (management) is mostly aggregation + framing. Tier 3 (senior leadership) is mostly editorial + commercial framing. The investment ratio is roughly 70/20/10.
- **Counter-pattern to avoid**: Three artifacts with three parallel data pipelines = three numbers that don't reconcile = trust collapse. The single-data-source rule is non-negotiable.

---

### Reverse-Engineering Strategy — "What Would Have to Be True?"

- **Date**: 2026-05-04
- **Source**: Lafley & Martin, *Playing to Win*, Ch 8 ("Shorten Your Odds")
- **Pattern**: When a strategy team can't agree between competing options (or one person's option dominates the room), do not debate which is right. Reframe each option as a hypothesis and ask the seven-step question for each: *what would have to be true for this option to be the right one?* Then go test the conditions, not the conclusion. The team converges on the option whose conditions hold up, instead of the option held by the loudest voice.
- **The seven steps** (compressed):
  1. Frame the strategic choice — make options concrete and mutually exclusive.
  2. Generate strategic possibilities — at least three, including one that breaks current assumptions.
  3. Specify conditions for each — what would have to be true (industry, customer, position, competition, capability) for each to be the winning choice.
  4. Identify barriers to choice — which conditions look least likely or hardest to verify.
  5. Design tests for the barriers — proportional to the leader's confidence (lower confidence = bigger test).
  6. Conduct the tests — run them honestly, even if results are unwelcome.
  7. Make the choice — the option whose conditions hold becomes the strategy; document the discarded options + why.
- **Why it works**: It depersonalizes the choice. Every executive in the room owns the *test*, not the *option*. Disagreement gets routed to "we disagree about which condition matters" — which is testable — instead of "we disagree about who is right" — which is not.
- **PM application**: Use this in Director-level strategy debates where two roadmap directions compete and political weight is uneven. Frame both as hypotheses, ask the seven-step question, surface the conditions, propose the cheapest test for the most-disputed condition. The act of running the seven steps is itself a Senior Director move — it converts a position fight into a learning exercise.
- **When it applies**: Strategy debates with multiple credible options. Roadmap forks. Competing capability investments. Build vs buy vs partner. Cross-org arguments where positional power is uneven.
- **When it fails**: When time is too short to test (operational decisions). When the conditions are unfalsifiable in any practical timeframe (very long-term bets). When the choice is a values question rather than a strategy question.

### Six Strategy Traps — Audit Checklist Before Calling Something a Strategy

- **Date**: 2026-05-04
- **Source**: Lafley & Martin, *Playing to Win*, Ch 8
- **Pattern**: Most documents called "strategies" inside large orgs are not strategies — they are one of six recognizable failure modes. Before presenting any plan as a strategy (especially upward), audit it against these six traps. If two or more apply, it is not yet a strategy.
- **The six traps**:
  1. **Do-it-all** — every option chosen, no Where-to-Play discipline. Fails because resources scatter and no choice meaningfully outcompetes.
  2. **Don Quixote** — head-on attack against the strongest competitor where they are strongest. Fails because the entrenched leader has structural advantage; the attacker bleeds.
  3. **Waterloo** — fighting on too many fronts at once. Fails because management bandwidth + capability investment cannot scale across simultaneous fights.
  4. **Something-for-everyone** — trying to satisfy every customer segment with one offer. Fails because no segment finds the offer the best choice; competitors with focused offers win each segment.
  5. **Dreams that never come true** — aspirational mission statements with no Where-to-Play / How-to-Win cascade beneath. Fails because aspiration without choice is a wish.
  6. **Program-of-the-month** — chasing the latest framework or initiative. Fails because the org never builds compounding capability; every program restarts the learning curve.
- **PM application**: Run this audit on any roadmap deck or strategy doc before sending upward. Internal Director-level test: which trap is my own H2 plan most at risk of? Self-audit makes the upward presentation more credible — a leader who names their own trap pre-empts the critique. It also reframes the "promotion strategy" exercise — Senior Director candidates have to demonstrate *they don't fall into these traps*, not that they have grand plans.
- **When it applies**: Roadmap reviews. Strategy presentations. Promotion narratives. OKR cycles. Any moment when a leader is asked "what's your plan?"
- **When it fails**: When applied mechanically as a checklist rather than a diagnostic. The traps overlap — a do-it-all plan is often also something-for-everyone. The point is to surface real failure modes, not to score the doc.

### Six Telltale Signs of a Winning Strategy — Positive Diagnostics

- **Date**: 2026-05-04
- **Source**: Lafley & Martin, *Playing to Win*, Ch 8
- **Pattern**: Strategies that win share six observable signals. Use these as positive diagnostics — not predictions, but evidence the strategy is working. Useful for after-the-fact validation and for external benchmarks ("does competitor X have a winning strategy?").
- **The six signs**:
  1. **A distinct activity system** — the way the org gets work done is visibly different from competitors, and the differences reinforce each other (Porter's "fit" — feasible, distinctive, defensible).
  2. **Customers who are loyal as a result** — repeat buyers / users not because of switching cost or lock-in, but because the offer is genuinely the first choice for their need.
  3. **Competitors who are profitable** — the market structure allows multiple winners; the strategy doesn't depend on destroying competitors. Healthy competition is a signal of a real Where-to-Play, not a winner-take-all bloodbath.
  4. **More resources than competitors to invest in growth** — winning strategies generate the surplus to reinvest. If the strategy requires constant external funding to stay alive, it is not yet winning.
  5. **Competitors attacking each other, not you** — when the strategic position is well-chosen, rivals fight each other for second place. Direct attack on the leader is rare because the position is hard to assault.
  6. **First choice for new technology, employees, partnerships** — the org becomes a magnet. Talent, partners, innovators come to it first. This compounds.
- **PM application**: Use as a quarterly reality check — *which of the six signs does my product actually show today?* Honest answer is usually 1-2, sometimes 0. Improvement comes from designing toward the missing signs, not from declaring victory on the ones that are present. For promotion narrative — point to the signs that *did* emerge under the leader's tenure (e.g., AEM EH MAU growth = sign 4, partner pull = sign 6).
- **When it applies**: Strategy reviews. Quarterly business reviews. Promotion / impact narratives. Competitive analysis (does *their* strategy show these signs?).
- **When it fails**: When applied to too short a horizon — these signs take quarters to emerge. When confused with vanity metrics — "we have loyal customers" must mean repeat use because of fit, not because of contract lock-in.

### Outside Strategy Partner — The Sparring Partner Pattern

- **Date**: 2026-05-04
- **Source**: Lafley & Martin, *Playing to Win*, Ch 8 (Lafley + Martin's own working relationship as the canonical example)
- **Pattern**: Strategy work has a structural blind spot — the leader closest to the work is also closest to its assumptions. An outside partner with no operational stake provides three things internal teams cannot: (1) willingness to ask the dumb question, (2) immunity to the political weight of senior voices, (3) a structured framework that the leader doesn't have to defend authorship of. The pattern is *sparring partner*, not *consultant* — continuous, conversational, paired across cycles.
- **What makes it work**:
  - The partner has framework fluency (cascade, four dimensions, seven-step) but does not own the answer.
  - The relationship is cumulative — the partner knows the org's prior choices and can reference them.
  - The partner is willing to be wrong publicly so the leader can be wrong privately first.
  - The leader retains the choice; the partner only stress-tests it.
- **PM application**: Inside a corporate org, a Claude project (or equivalent persistent assistant) can serve this role at the Director level — framework fluency plus memory plus zero political weight. The role is not to give answers but to ask "what would have to be true?" before the leader presents to the next tier. For Pedro, this is exactly what the AAI / EH knowledge system is doing — a sparring partner that compounds across sessions and is willing to surface the trap the org would be too polite to name.
- **When it applies**: Director and above, where strategy choices have political weight and the leader's peer network may not be willing to push back honestly. Cross-functional moments where the leader is the senior person in the room.
- **When it fails**: When the partner becomes a yes-machine (too aligned), or a critic with no stake (too disengaged). When the leader treats the partner's output as the answer instead of as input to their own judgment.

