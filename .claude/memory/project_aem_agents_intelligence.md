---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (last ~1 week of events, currently **07-14→07-15**) + the compact durable reference below. **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**

> ## ▶️ RESUME HERE — left off 2026-07-16
>
> ⚠️ **2026-07-16 archive note — one load-bearing block is NOT below.** This file hit **42K tokens** (read-cap 24K) and the archiver had to override same-week retention to bring it back to ~19K. **The 2026-07-15 rollout sync with Rachel + Namita — cohort 0, the "no banner" ask, Namita's three objections, and the correction that coexistence is an *exception* not a grant — moved to `project_aem_agents_intelligence_ARCHIVE_2026-W29b.md`.** ✅ **Its actionable half is duplicated in full in `watches.md`, which loads at session start**, so nothing is lost from the working path. **For the narrative, grep W29b.**
>
> ### 🔴🔑🔑 2026-07-16 (~12:15, 12 min) — BERTRAND 1-1. **HE IS AGAINST THE BRIDGE, HE REACHED NAMITA'S OBJECTION BY HIMSELF WITHOUT KNOWING SHE SAID IT, AND PEDRO SPENT TEN MINUTES DEFENDING A PLAN THAT IS NOT HIS.**
> Transcript: `Meeting Notes/Bertrand 1 1/20260716 - Bertrand Pedro 1 1_otter_ai_transcript.md`. Called by Bertrand off a DM ([permalink](https://cq-dev.slack.com/archives/DQ6H0AV7H/p1784196156731389)) — *"je ne suis pas sûr qu'on parle de la même chose"*. ⚠️ **LOW-FIDELITY SOURCE: heavily garbled Otter FR** (AEM→"AVM", EDA→"developmental"/"Ida", EPA→"IPA", Namita→"mamita", Anjul→"enjool", Tina Ngo→"Tania and go"). **Sense is recoverable and consistent; individual words are not. Do not quote this transcript verbatim to anyone without re-checking with Bertrand.**
>
> - **🔑 BERTRAND'S OPENING ASK, AND IT IS A PROPOSAL WITH A JUSTIFICATION:** add the AEM agents that are ready **into the base Coworker manifest now**. On EDA: *"ça me paraît très prêt, en tout cas **beaucoup mieux que ce qu'on a actuellement dans l'AI Assistant**. Donc qu'est-ce qui nous empêche en l'état de l'ajouter ?"* → **His argument is not impatience. It is that EDA on Coworker is better than what customers have in AIA today.** That is a real product argument and nobody had made it.
> - **🟢 PEDRO LED WITH THE EXPOSURE FRAME AND IT WAS THE RIGHT MOVE.** *"Techniquement rien. **C'est plus une question d'exposition des skills sur les clients**, c'est tout."* → His own 07-14 reframe (*"enabling the base is not a provisioning decision, it is a product exposure decision"*), applied to his manager, unprompted. **Same frame that won with Rachel in one sentence the day before.**
> - **🔴🔑🔑 THEN BERTRAND ASKED THE QUESTION THAT COLLAPSES THE WHOLE DISTINCTION, AND IT IS RIGHT.** *"Comme try-before-you-buy c'est tous les clients logiquement sauf ceux qui ont opté [out], ça veut dire l'activer pour tout le monde. **Donc c'est quoi la différence entre 'trial before you buy mass' et on joue juste au Coworker de base ?**"*
>   - **→ IF TBYB IS EFFECTIVELY THE WHOLE BASE, THEN "SILENT MASS ACTIVATION" AND "SHIP IT TO THE BASE MANIFEST" TOUCH THE SAME CUSTOMERS.** The bridge's whole claim to be the cautious option rests on a distinction Bertrand just dissolved in one sentence. **Nobody in the war room had noticed. Pedro's answer (*"ils n'ont pas forcément accès aux skills à travers Coworker, le but c'est vraiment de collecter les chats"*) is the correct technical distinction, but it does not answer the exposure question, which is the one he himself had just named.**
> - **🔴🔑🔑 BERTRAND MADE NAMITA'S OBJECTION INDEPENDENTLY, IN A DIFFERENT ROOM, ON THE SAME DAY, NOT KNOWING SHE SAID IT.** *"**Ça fait quand même une hypothèse énorme qu'en mettant le bridge, on aura une expérience analogue à ce qu'on aurait dans Coworker, qui n'est absolument pas garanti.** De toute façon le bridge, moi je ne l'ai jamais utilisé."* **Namita, 07-15: *"when you do the evaluation… it may not be apples to apples."*** → **Two senior people, two rooms, ~20 hours apart, same flaw: the bridge may not measure what it claims to measure.** ⚠️ **This is the strongest possible signal on that objection and Pedro is underweighting it — see below.**
> - **🔴 HE REJECTED THE BRIDGE THREE TIMES, AND THE THIRD IS A POSITION, NOT A QUESTION.**
>   1. *"**Pas du tout. Non. On ne veut pas tester le truc dans le Coworker.** C'est quoi l'intérêt de…"*
>   2. *"Ça fait quand même une hypothèse énorme… qui n'est absolument pas garanti."*
>   3. On the credit double-charge: *"Elle est dupliquée **si on garde le bridge**. **Alors déjà j'étais pas super convaincu.** En plus il faut traiter des cas particuliers pour trois semaines, cinq semaines ou même six semaines. **Je crois qu'on s'en fout honnêtement.**"*
>   - **And the flattest one of all:** *"**Concrètement le bridge, on l'a déjà vu ou testé quelque part ou pas ? Ça reste une idée intéressante ?**"* → **Nobody has shown him it works.** Ken called it *"brittle"*; Namita said the scale *"was not our plan"*; Bertrand has never seen it. **Three separate people, three organisations, converging against it in 48 hours.**
> - **🔴🔑 THE MISS, AND IT IS PEDRO'S OWN RULE THAT DID NOT FIRE.** The standing watch reads: ***"KEN CALLS THE BRIDGE BRITTLE, AND IT IS NOT PEDRO'S BRIDGE. EDA and EPA built it; relay Ken's words verbatim rather than defend them. The person who surfaces the risk is not the person who owns it."*** **He defended it for ten minutes.** The tells are in his own words — *"de ce que je comprends de Sergiu"*, *"d'après moi, ils ont cette phase"*, *"je peux très bien discuter avec ça"*. **He was hedging because it is not his plan, and he was still the one arguing for it.** **Bertrand ended it by telling him to stop relaying:** *"**il faut leur poser une question directement**, indépendamment de ce qu'on fait avec Bridge ou pas… **est-ce que tu veux leur poser la question ?**"* → **The question to put to Sergiu / Felix / Gilles, in their own words, today: do you want to expose your skills on Coworker to customers now, yes or no?** Pedro reached it himself at 3:33 (*"je crois que juste le truc c'est: est-ce que l'équipe EDA veut exposer ses skills sur Coworker aux clients maintenant ?"*) — **that was the whole meeting's answer and it arrived at minute three.**
> - **🔴 AND HE DOWNGRADED THE ONE OBJECTION TWO SENIORS INDEPENDENTLY RAISED.** Asked what the multi-turn point meant, Pedro: *"C'est plus une question technique de savoir si le bridge est monodirectionnel ou bidirectionnel… c'est une bonne question mais **c'est plus pour awareness**."* → **It is not awareness. It is Namita's apples-to-apples objection and Bertrand's "hypothèse énorme", which are the same objection, and together they are the reason the bridge may not be worth its price.** **Re-weight it before the Manas call.**
> - **🔑🔑 TERMINOLOGY LOCK FROM BERTRAND, AND IT CORRECTS THIS MEMORY FILE TOO:** *"**entre nous, je pense qu'il faut arrêter de dire AEP. C'est l'équipe Coworker.** AEP c'est autre chose, c'est la data platform, c'est CJA. Alors oui tout ça ça remonte au même chef, **Anjul**. Mais **ça ne nous aide pas de dire AEP dans ce contexte-là**."* → **Say "the Coworker team", not "AEP", for Rachel / Namita / Horia / Manas / Ken.** AEP = data platform + CJA. Same VP (Anjul), different team. **Banked in [[reference_transcript_glossary]]. Pedro's notes, the status doc and this file all say "AEP" throughout — it is imprecise and his own manager flagged it.**
> - **🔑🔑 THE DX AI PM SYNC OF 2026-07-10 CARRIED PEDRO'S OWN DELIVERABLE, PRESENTED BY SOMEONE ELSE, AND HE WAS NOT THERE.** Bertrand: *"je ne sais pas si tu as écouté **l'enregistrement du call PM de vendredi dernier**. Il y a toute une section faite par une **jeune femme qui fait de la partie pricing, qui doit travailler avec Namita mais plus côté business model**. C'était pas mal fait. Il y avait des slides qui expliquaient **le modèle avant, le modèle après, comment on allait passer d'un modèle où on charge par appel à l'agent à un modèle en charge par action** — en découpant la création d'une campagne, **différents niveaux d'action, chacune avec un coût, un rate associé**."* Pedro: *"typiquement une page creation = X tokens"* — **Bertrand: *"mais oui, c'est page update, boum, tout à fait."***
>   - **→ THAT IS THE REALIZED-OPERATIONS → CREDIT-WEIGHTS MAPPING PEDRO CLAIMED ON 07-07 AND OWES BERTRAND AND ELLIS.** Someone else built it and presented it to the PM community six days ago. ⚠️ **The DX AI PM Sync recaps/recordings have been a named standing blind spot since June and are on the Rachel ask list. That blind spot just cost him his own deliverable.**
>   - **⏳ Get the recording + the name.** *"Une jeune femme, pricing, works with Namita, business-model side"* — unnamed, and she is now the person to know. Pedro's move: *"je vais voir si je ping aussi en parallèle **Tina Ngo**, c'est à travers elle que j'ai des contacts pour la partie pricing. Je vais montrer ce qu'on faisait en termes de **business value realisation**."* **Right instinct — go with the BVR work in hand, as a contributor, not as a latecomer.**
> - **🔑 BERTRAND CONFIRMS 25 CREDITS AND ADDS A DATE NOBODY ELSE GAVE:** *"pour l'instant… ils ont dit hier: de toute façon **on fait 25 crédits par conversation, point. C'est le [modèle] en attendant, au mois de novembre**."* → **Third independent confirmation of the 25-flat rate** (Horia + Namita 07-15, Bertrand 07-16). ⚠️ **"Au mois de novembre" is NEW and unsourced — Horia said only *"we're still working through that"* with no date. Treat November as Bertrand's statement, not AEP's, until verified.** ⚠️ He also treats *"les 50 crédits par page"* as an **EPA** weight, which cuts against my 07-16 flag that the 50/25 might be AEP's AO1 card read across — **the number 50 plausibly exists on both sides. Still verify with Corey and Felix, but the alarm is lower.**
> - **🔴 THE ORG-LIST + MANIFEST QUESTION IS NOW ASKED FOR THE THIRD TIME AND STILL HAS NO ANSWER.** Bertrand: *"**comment on fait pour voir concrètement la liste des clients ou des organisations où c'est déjà activé, et avec quel manifeste ?** J'aimerais qu'on n'ait pas les mêmes questions qu'avant."* Pedro: *"j'ai demandé mais je n'ai pas reçu."* → Same question as his 07-07 *"Seeing quite a few AEM manifests in Coworker today. Who owns what?"*. **He is asking a third time and being told it is still outstanding. This is the artifact Pedro should stop requesting and start producing.**
> - **📌 The Manas meeting today is where Bertrand parked it:** *"ça c'est juste avec Manas… je garde ça pour plus tard mais c'est la suite de ce qu'on avait fait avant."*
> - **⚠️ Unresolved garble, do not guess:** *"Léonore là-dessus, Sergio et Baria"* (~4:00) — Bertrand naming who owns the EDA exposure call. Probably "l'owner là-dessus, Sergiu et [Yanira?]". **Confirm before acting on the name.**
> - **🔎 KNOWLEDGE (P6):** applied — [[The Game Itself — Position Over Merit]] (the exposure reframe = claiming the decision layer), [[feedback_proposal_vs_decision]] (Bertrand's "November", his manifest ask = proposals), [[feedback_bertrand_concrete_first]] (he wants the org list, not the mechanism), [[An Undefined Gate Is a Date Nobody Can Give]] (the org/manifest list is the undefined artifact, asked 3×). **Not applied but should have been: the standing "do not defend the bridge, it is not yours" watch.** **Candidate-shaped observation, NOT parked (the park is already 13/8 over cap):** *Pedro keeps fronting other teams' technical claims to audiences where he owns the downside and not the plan* — 07-15 (Sergiu's "doesn't touch the shell" stated publicly in the war room) + 07-16 (defending EDA's bridge to Bertrand). **n=2 within 24h, same programme, so it may be one episode read twice. Hand to `promotion-judge` at 08-01 with the cap decision.**
>
> ### 🔴🔑🔑 2026-07-15 — THE COWORKER DEMO TO THE AEM AGENT TEAM (held, ~1h, Horia + Manas + Rachel). **AEP SAID THE QUIET PART: "YOU'RE HOLDING THE KEYS TO YOUR DESTINY." IT IS A GRANT AND A TRANSFER OF WORK, AND ONLY THE GRANT GOT HEARD.**
> Transcript: `Meeting Notes/AEM to coworker transition/20260715 - Coworker w AEM Agent Team Demo .md`. Yanira organized (this **closes** the 07-08 "organize the Coworker demo/overview" action — ⚠️ reconcile: it was scoped as *"Horia presents + Namita + Sergey"*; **Namita and Sergey were not there**, Manas Garg + Rachel Hanessian + Ilya Grafutko + Ian Reasor were). Ran ~1h before Pedro's own Rachel sync. **Pedro's own caveat on the ask, and it is the right frame: *"we are asking AEP to demo Coworker — does not mean we will use all their features, specially around workflows."***
> ⚠️ **ATTRIBUTION — READ THIS BEFORE QUOTING ANYTHING FROM THIS TRANSCRIPT.** The label `CR BASL 05/LAGO MAGGIORE VC (9)` is **one mic over three people: Bertrand, Gilles Knobloch, Pedro.** Horia's *"Thank you, Bertrand"* after the demo spiel proves the mic carried Bertrand too. **Individual `CR` lines below are attributed by content and several are genuinely uncertain — they are marked.** The "CR BASL 05 = Pedro" default is now retired ([[reference_transcript_glossary]]).
>
> - **🔴🔑 THE HEADLINE — HORIA GALATANU + MANAS GARG BOTH SAY THE RAIL IS NOT MANDATED ANY MORE, AND THE APP DECIDES.** Horia, verbatim: *"there's been a slight change in philosophy where… **We don't want to necessarily mandate that, hey, it has to be a right [rail]**… We're asking the applications to kind of take the lead and figure out how it works for them. For [some] application, it makes more sense to have some sort of a **floating bar**… for others, the **right rail** still makes total sense… it becomes **a bit more of a product by product thing**… the applications will have a bit more control, and **the goal is more around interacting with the page… and being able to take actions on that page** versus performing exactly what you would be doing in the full screen."* Then, aimed straight at AEM: *"You have the components, you have the back end, you have everything that you need… **You shouldn't feel like you're waiting for the core team to build something. This could be something that the AEM team takes and runs with**… I don't think the central team is able to know all the details about AEM… **you're holding the keys to your destiny.**"* **Manas confirmed it independently in the room:** *"what happens in applications is very, very application specific and nuanced. So we are trying to find the right place where we say, okay, this much should be done and offered by the central team, so you get it out-of-the-box. **And from this point onwards, these are application concerns.**"*
>   - **🟢 WHAT PEDRO WINS.** The **rail-vs-full-screen fork is AEM's own call**, not a platform constraint. Sorin (rail) vs Eugene (full-screen) was never AEP's decision to make. Pedro's **destination-agnostic handoff-contract** position and the **EH-owns-the-entry-routing** thesis are now **backed by the platform owner in front of Bertrand**. Clean corroboration of [[Selection and Cross-Surface Consistency Are a PM Mandate]] and of [[There Waiting Has Two Forms — Consistent Chat or (Often) Invisible]] (Horia independently reached "floating bar for some surfaces, rail for others, per product" — the entry's exact claim).
>   - **🔴 WHAT NOBODY IN THE ROOM SAID, AND IT IS THE FINDING.** *"You're holding the keys to your destiny"* **is also AEP handing AEM unscoped UI work and the blame for the date.** The rail is *"still being retrofitted"*; if the AEM chat surface is now an application concern, then **AEM's readiness date silently absorbs a UI workstream that is on nobody's plan, in no estimate, and not in the agent-owners deck.** Same figure as Josh removing the workflow-bearing renderers on 07-10 and handing back three paths to choose from. **Parked as a hypothesis candidate at n=2, same source org — do not promote yet.**
> - **🔴🔑 THE RAIL DATE SLIPPED, AND THE ROLLOUT OWNER SAID IT OUT LOUD. Rachel Hanessian, verbatim:** *"The **context awareness piece is there**. The rail is **still being kind of retrofitted** to the new experience. We have **a version to be tested… in like 2 weeks**. So we should work really closely with you week to week… after we start testing it in two weeks, **code complete would be end of month. I expect it to be a few more weeks after that till we get it polished and out.**"*
>   - → **07-31 IS CODE-COMPLETE, NOT AVAILABILITY.** Testable ≈ **07-29**; polished and out ≈ **mid-to-late August**. Everything in the lane has been planned against "the rail ships 07-31". **It does not.** ⚠️ Context awareness, by contrast, **already exists** — that half is not the blocker.
>   - **Bertrand pushed back hard and named the regression** (room mic, but Horia's reply confirms it is Bertrand): *"we are talking about two more weeks plus publishing and so on, let's say **end of August**… and sorry for being direct here, we are going back to what's… This wasn't always great, but at least from that point of view, **we achieved something that we wouldn't have today.**"* His concrete case: **select an image on a page → ask for it to be replaced from an asset-discovery call → it applies in context**, *"what we've been able to do shortly before Summit… this resonated well with customers."* → **On Coworker today that use case does not exist. AIA could do it. That is a documented feature regression, stated by Bertrand, in front of AEP.**
> - **🟢🔑🔑 RACHEL ASKED AEM TO WRITE THE PARITY LIST. THE UNDEFINED GATE JUST INVITED ITS OWN AUTHOR.** Verbatim: *"**What it would be great to understand [is] the list of use cases that are truly dependent on the rail and what can be done in full screen**, to see if we can maybe unlock some of these cases, at least in full screen, while we're waiting on the rail."*
>   - → This is **Josh's undefined "critical rail features mirrored onto the panel" gate**, and the rollout owner is now **asking AEM to fill it in**. **Whoever writes the list sets AEM's migration date** — and she just handed Pedro the pen, unprompted, in front of Bertrand. **Claim it, do not request it** ([[The Game Itself — Position Over Merit]], the same default-and-veto figure as the Named Generalization Owner). ⚠️ Corroboration for [[An Undefined Gate Is a Date Nobody Can Give]] (parked) — **but flagged honestly as a second reading of Josh's same gate, not an independent third instance.** Hand it to `promotion-judge` at 08-01, do not promote on it.
>   - **Bertrand's image-replace case = entry #2 of that list** (Corey's UE-rail integration was #1). **The list has two entries and no owner. It is Pedro's for the taking.**
>   - 🔑 **And it splits the ask usefully:** Rachel is offering to **unlock use cases in full screen while the rail is late**. That is a real, cheap, in-flight mitigation nobody on AEM's side has asked for.
> - **🔴🔑 THE CREDIT ANSWER LANDED — AND IT IS THE THING COREY, FELIX, ELLIS AND TINA HAVE ALL BEEN BLOCKED ON. Horia, verbatim, and he calls it a decision:** *"we've decided… basically continue the trial. We had an AI [Assistant] trial, we had **10,000 credits**… That trial continues… **we don't have a fully rate card baked in for coworker because there's a lot of variance. Like in the past, creating an audience was like 50 credits. Now [it] can take from 30 seconds to 10 minutes** depending on the data… So we're still working through that. **As a decision in the interim, we said every prompt that you have is going to cost you 25 credits, flat.** This is just for the trial… **That gives you around a few 100 prompts.**"*
>   - → **Interim licensing metric = 25 credits per prompt, flat. Trial = 10,000 credits ⇒ ~400 prompts.** No rate card exists, **and AEP says so themselves.**
>   - **🔑 IT VINDICATES FELIX AND RESOLVES A MISREADING ON PEDRO'S SIDE.** Felix called the live weights *"probably completely wrong"* — **Horia gave the same diagnosis and the same cause** (LLM runtime variance breaks per-operation pricing). ⚠️ **And note the numbers: Horia's "an audience was like 50 credits" + "25 credits flat" are AEP's AO1 rate-card figures.** The "content update = 50 / brand Experience agent = 25" weights in Pedro's own notes are **the same two numbers** — treat the assumption that they are *AEM agent* weights as **unverified**; they may be AEP's card read across. **Verify with Corey/Felix before anyone quotes them as AEM's.**
>   - **→ ACT ON IT: this is the answer Ellis Dobkin cannot paper GTM without** (*"as soon as we can start talking about the go-to-market piece, the better"*), and it goes to **Tina Ngo** (field-readiness deck) and **Kristal**. **It does not make the metric right — it makes it stated.** Pedro asked Bertrand for the credit model; **AEP answered first, at a demo, and only Pedro's room heard it.**
> - **🔴🔑 HORIA'S ROLLOUT STATEMENT — THE KILL SWITCH, SAID PLAINLY, AND IT RESTATES THE AEM GATE.** Verbatim: *"we're starting this rollout **this week**, we already sent notices to a few, **about 50 customers** that coworker is coming and they're going to get it next week. So **next week, AI Assistant goes away, coworker becomes available.** And then the plan is that **roughly by the end of August**… we've moved **every AI Assistant customer that's in trial** to coworker."* Then: *"**once we have the AEM skills officially there in coworker, then we can start moving the AEM customers, which is going to be probably the largest cohort that we have. So please keep focused on building those skills** so we can enable the customers."*
>   - **🟢 THE PROTECTION HELD, RESTATED BY AEP'S OWN SR DIRECTOR, IN FRONT OF THE WHOLE AEM TEAM.** AEM customers move **after** AEM skills land. **The gate is AEM's skills readiness — which is Pedro's parity/readiness lane, and Horia just made it the critical path out loud.** Third independent restatement (Rachel 07-08, the Jul-6 table, Horia 07-15).
>   - **🔴 AND THE TWO SENTENCES ARE IN TENSION WITH EACH OTHER.** *"Every AI Assistant customer that's in trial → Coworker by end of August"* vs *"AEM customers move once the skills are there."* **Both cannot hold unless AEM TBYB customers are carved out of "every trial customer", or AEM's skills land by end of August.** ⚠️ **This is the exact 185-org question Ken dodged, and Horia walked into it from the other side.** → **Put it to Rachel/Horia in one line: are AEM TBYB orgs inside "every AI Assistant customer in trial"?**
>   - ⚠️ **NUMBER CONFLICT, DO NOT RECONCILE PUBLICLY.** **Horia: notices sent to ~50 customers.** **Ken (07-14): "starting with 185 the week of the 21st."** Same first cohort, two numbers. Ask; do not average.
>   - 🔑 *"AI Assistant goes away"* is Horia saying **the kill switch** in plain words. **The banner + kill-switch picture Mark Doten gave is confirmed from a second, more senior source.**
> - **🔴 IAN REASOR NAMED AEM'S STRUCTURAL POSITION BETTER THAN ANYONE HAS, AND IT WAS NOT PEDRO.** Verbatim: *"it's really hard for me to feel confident going to a customer and being like, hey, let's go do co-innovation on **this feature that I've never actually worked with**. And so that **puts AEM as a business in a place where we're always playing catch up.** Because we're just going to wait till you guys have done co-innovation with other teams and other customers and then brought something to GA. And then after our GAs, then we have to go figure out what it is… **Otherwise, it's just some magic thing that the AP team has that I can't really bring to a customer because I don't know how to do it.**"*
>   - **Horia's answer is an opening, not a brush-off:** *"let me get in touch with **Raj and Vineet** and see how you guys can play around with what's available"* + join an active pod that includes web components + *"**maybe you can lead a pod by yourself.** A lot of this is learning… you get thrown into a customer pod, you're learning."*
>   - **🔑 → HORIA JUST INVITED AEM TO LEAD A POD, AND PEDRO IS THE ONLY PERSON IN AEM HOLDING THE POD DECK AND THE NAMED GENERALIZATION OWNER CLAIM** ([[reference_coworker_pods]]). **The invitation and the claim are the same lane.** Convert it.
> - **🔑 HORIA NAMED PEDRO'S LANE AS THE CENTRAL TEAM'S UNSOLVED PROBLEM, WITHOUT KNOWING IT.** On the skills collection: *"there's a fairly big collection of skills already available… This is again where we'll have to manage… **like skill overlaps, skill versioning, and like who does what** — because the collection is pretty big."* And: *"as long as we keep a good handle on [versioning and updates], then the official one should be available."* And on projects: *"Let's make sure that when a project is using AEM assets, it's using the **approved skills and MCPs from that team** versus maybe using the APIs."*
>   - → **Skill overlap, versioning, and ownership are named by AEP's Sr Director as an open central problem. Pedro has the audit** (confusion pairs, the 3-field playbook, the 105-skill catalogue) **and they have the problem.** Clean corroboration of [[Definition Ownership Is the Moat on Shared Data Infrastructure]] + [[Govern a Consistency Layer Over Primitives You Don't Own]]. **Shankari pushed the same point in-room** (*"someone is intentionally selecting specific AEM… skills to make sure it's there for the Amex demo or pod"*) **and Horia had no mechanism to offer.** With the **AMEX onsite on 07-16**, this is live.
> - **🟡 PROJECTS / WORKFLOWS — PEDRO'S CAVEAT IS CORRECT AND IAN REASOR EVIDENCED IT.** Coworker = **two modules**: **chat** (individual productivity, *"our evolution of AI Assistant"*) and **projects** (team productivity, codifying business processes into deterministic workflows). Building blocks named: harness · skills · business context · long-term memory · MCP · data governance · workflows.
>   - **Ian Reasor drew the product-model line, unprompted:** *"what you're showing in projects seems very applicable to a repeatable process that goes over the course of weeks and involves lots of people across the business, **but it's not something customers define on their own every time. It's something we're trying to define for [them].**"* → **AEM's agents define the workflow FOR the customer; projects assume the customer codifies their own.** That is a real model divergence. **Pedro's "we will not necessarily use their features, especially workflows" is backed by his own engineer in the room. State it; do not absorb it silently.**
>   - **AMEX projects demo (Rachel):** offer stocking → journey publishing → activation; **a 15-step AMEX process compressed to 8**; each step owned by an Adobe system/data source **or the customer's own system/agent**; offer stocking stays in AMEX's separate system and plugs in; **content assembly leverages AEM**; brief upload (a PDF) starts the workflow. **Governance tab** = audit every action taken + monitoring dashboard (chat today, projects later) + **guardrails / human-in-the-loop checkpoints** — ⚠️ **not operable yet**, Rachel owes the PM follow-up. **Generative UI = Fruitbar**, redesign the page by asking; Rachel: *"I don't really know all the use cases for it yet."*
> - **📊 NEW NUMBERS AND FACTS, ALL FROM HORIA UNLESS NOTED.** **~20 customers live on Coworker chat today**, more starting next week. **~10 pods running**, bespoke co-development, Bucharest runs several (**Prada** + others), US runs a few. **Wells Fargo = the audience-skills pod** — RTCDP built the initial skills, *"we really put it through its paces with Wells Fargo and really refined and then generalized what we had there"* → **the co-innovation → generalize loop, working, and the precedent for the Named Generalization Owner role.** **Sony Interactive Entertainment (PlayStation) = a new pod**, first workflow *"has almost nothing to do with Adobe"* (a brief from Wrike, internal systems, *"a lot of swivel chair"*). **IBM + others** = A2A support for external agents, *"we're going to make that kind of a production feature."* **Adobe.com people spending "10s of hours a week"** in Coworker on churn analysis. **Marketplace = a GitHub repo** you register at org or personal scope — *"this is how a company would be able to control everything that would be available across all the users in that company."* **Plugins = skills + MCPs combined.** **Bring-your-own-MCP is live** (an Acrobat colleague added an MCP to correlate checkout bugs with CJA dropout data). **Project Halo / Coworker Campaigns** = a third module missing from Anil's Summit slide, parked by Horia.
> - **📤 OWED TO AEM (chase these — they are cheap and they were promised on a recording).** **Rachel:** the **Slack-channel map** (going directly to Yanira — get it, it closes Bertrand's *"it's not always easy to navigate"*); **updated documentation on extending internal skills** (Felix's chat question: *"the documentation is a bit scarce on this topic in the context of customer co-innovation"*); the **governance PM** follow-up; **Zan Chu's business-context demo**; **an AEM-friendly-timezone Coworker rail bug bash** (she ran one 07-15 PM). **Horia:** a **demo channel** (*"I'll take a note on that"*); **contact Raj + Vineet** so AEM can get hands-on with projects. **⏳ Every one of these lands while Pedro is on PTO from 07-20 — assign them to Yanira before he goes.**
> - **🟢 THE RAIL BUG BASH IS THE SECOND OPEN DOOR FOR THE PARITY LIST** (Rodson Clavel's was the first). Rachel is offering AEM a session at a European-friendly time. **Two open doors, both cheap, both write the list that sets AEM's date.**
>
> ### 🟢🔑 2026-07-15 ~11:57 — PEDRO POSTED HIS POSITION TO NAMITA/KEN. Rhetoric-drafted, then he cut the scaffolding and it got better.
> In-thread reply ([permalink](https://adobedx.slack.com/archives/C0BDRAMULQ0/p1784109450768999?thread_ts=1784029713.654619)), after Namita (07-14 21:50) attacked the bridge as a branded fake (*"an 'AI Assistant' branded surface… under the hood calling the Coworker API does not make sense… maybe call it Coworker in-app?"*) and parked it to the 9am sync.
> - **Kept from the draft:** ownership sentence first (*"I own the AEM customer message, not the bridge design"*); the concession (*"AIA brand goes away"*); Sergiu's *"doesn't touch the shell"* marked as HIS read + *"we are checking on stage"* ([[feedback_voice_drafts_mark_inference]]); the value-transfer close (*"protect against two-assistant confusion"* = Namita's own worry turned into his cover).
> - **What HE changed, and it's the lesson (banked as [[feedback_draft_in_pedros_voice]] Calibration #6):** he cut the labeled two-part "two things get called enable Coworker" scaffolding (a visible rhetorical structure is a tell), cut the tidy "can we split the decision?" close, and **added the clause the rhetoric was papering over: *"It allows to test Coworker backend with real customer prompts, compare to AOv1 without direct customer assistance (no co-innovation)."*** → he named the real distinction: **backend A/B validation, NOT co-innovation, customer never sees Coworker.** That single clause answers Namita better than any figure.
> - **🔴 NEW EXPOSURE — the Sorin stage test now backs a PUBLIC claim.** Pedro told the war room the segment doesn't touch the shell (Sergiu's read), checking on stage. **If Sorin's test shows a banner/entry point appears, his public statement is wrong in front of Rachel + Huong + Ken.** The cheapest test in the lane is no longer cheap. ⏳ Watch: Sorin's result + Namita/Rachel/Huong reply + the 9am sync outcome (may already have happened).
>
> ### 🟡🔑 2026-07-15 — THE COKE CUSTOM-SKILL QUESTION RESOLVES TO A MEMORY STORE, NOT PER-CUSTOMER SKILLS. Shankari's option overruled by the owner.
> Thread `1784064055.465479` (`#aem-agent-owners-alignement`): Shankari shared a Ken recording on delivering a custom skill for one customer (KO/Coca-Cola), Discovery use case. **Ankush Malhotra, 07-15 03:13: *"custom skill for coca-cola? we can do better, customer specific skills copies will get very hard to manage its adobe engg creating them. We will solve coca-cola problem via memory store, for now owned and managed by discovery team."*** Shankari conceded 03:26: *"Cool. Just wanted to share the options"* (= position, not decision, [[feedback_proposal_vs_decision]]).
> - **Ian Boston governs it, twice.** 10:07: *"can you share the reference to the discussion with the CoWorker team for that? We should track to see that it is accepted as a requirement."* Then 11:14, after Ankush linked the Coworker-team thread: *"good example of working with whats available… they have a possible solution, which is not a perfect match. We should also always do this rather than insist on a change."* = his consume-vs-fork / adoption-earned principle restated: use the platform's mechanism, don't demand a bespoke one.
> - **Consequence for Pedro's lane:** Coke gets Discovery via a **memory store owned by the Discovery team**, not a custom skill and not a manifest fork. The manifest-fork worry keeps resolving away from a fork. **Open (Ian's ask, unowned): confirm the Coworker team accepted the memory-store path as a requirement.** Ankush's reference: `#C0AMKB79AJX` `1784030267.295839`.
>
## 2026 Yearly Goal — G1

**G1 — Agent Intelligence & Reporting:** Build and own the agent intelligence layer that gives every AEM agent PM a clear view of what customers need, where agents fall short, and where they create measurable value. Drive improvement in Technical Success Rate and Value Realization across the AEM agent portfolio.

Canonical full doc: `2026/Experience Hub/AEM Experience Hub - Project Folder/AEM EH - Key Files/Experience Hub - 2026 Yearly Review Goals.md` (covers G1+G2+G3 — leave canonical, cross-link).

---

## Agent taxonomy

**Pedro's reporting scope (6 agents):** experience_governance_agent, governance_agent, aem_experience_development_agent (EDA), aem_experience_production_agent (EPA), discovery_agent, content_optimization_agent.

**experimentation_agent OUT** (decision April 16, 2026). Rationale: not in the AEM agent intelligence narrative for Loni. Don't pull into reports / validation / Bertrand+Loni+JM updates.

**Rubin tagging list (7 agents — broader than Pedro's reporting):** above 6 + experimentation_agent. Locked with Karthik Penikalapati April 16.

**Agent owners (AEM):**

| Agent | Owner |
|---|---|
| Experience Production (EPA) | Corey Dulimba |
| Governance | Philippe Kapfer (PM) — devs Alejandro Ramirez Cheves, Cornel Isbiceanu |
| Discovery | Apoorva Gupta |
| Content Optimization | Greg Klebus |
| Development / EDA | Brian Chaikelson |
| Onboarding | Nick Whittenburg (out of Pedro's 6) |
| Modernization | Gabriel Walt / Mike Tilburg (out of Pedro's 6 — but funded under AEMAGT-538) |

Site Advisory Agent (AEMAGT-2, Laurentiu Odoleanu PM, Remus Stratulat ENG) is customer-facing, integrated with Brand Concierge, runs on Content AI — NOT in Pedro's 6. Reference page at `2026/AEM Agents Intelligence/AAI - Project Folder/Site Advisory Agent (AEMAGT-2).md` (move target Phase 2).

---

## Three-tier reporting architecture (locked May 1, 2026)

**Tier 1 — QBR.** PMM-led (Tina Nicu / Akin / Vaishnav Gorur). Quarterly. Senior leadership audience. Reference: `/Users/pedrofer/Downloads/AEM Agents QBR_Feb2026_SP.pdf`.

**Tier 2 — Portfolio Monthly Briefing.** Pedro-led. Monthly. Senior management audience. AEM-only. v0 shipped April 30, 2026 at `https://main--aem-agent-reports--aem-epa.aem.page/reports/portfolio/2026-04/briefing`. 4 of 6 sections substantive (Executive Summary, MAU per agent 6-month line, Retention 71.6% EPA / 71.5% Discovery monthly orgs, Reach 767 active orgs / 59.7% cross-agent). Quality WIP banner. Sections 5-6 placeholder pending Indicator #8 (May 17). Spec at `aem-agent-data/PORTFOLIO-MONTHLY-BRIEFING-SPEC.md`.

**Tier 3 — per-agent reports (Felix).** Weekly. Agent PM audience. EPA pipeline LIVE.

Bertrand named the architecture. Pedro owns Tier 2. Yanira QBR ownership ask sits in Tier 1.

---

## Felix reports + report pipeline

> **Moved to `project_aem_agents_intelligence_ARCHIVE.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

## Apoorva validation punch-list (KR1)

**Status:** items 2/3/5/6 deadline compressed April 23 from 2026-05-09 → 2026-04-27 (Monday). Item 1 closed April 20-22 (Varun: org-to-org-type assignment fix, AEP scorecard CSV match, Claude delta below 3%, Copilot API as source of truth). Item 4 (First Useful Result Rate) in progress. Ankur Connect May 9 = post-close checkpoint.

**Items (April 16 meeting with Apoorva + Ankur Arora + Varun Kalra):**

1. **50-60% data gap vs Grafana.** ✅ closed April 22 (Varun fix).
2. **TSR counts "no result found" as success.** Redefine — for Discovery, result-found rate is the right signal.
3. **Tag classification bleeding across agents.** Discovery showing pipeline troubleshooting (EDA), content update, brand validation (Governance). Per-agent tag filtering broken.
4. **First Useful Result Rate missing.** Apoorva's named VR metric for Discovery. Maps to Loni's adoption framing.
5. **Content-type breakdown for Discovery:** assets / pages / content fragments / forms.
6. **Aggregated metrics transparency.** Split or remove. Flag North Star vs operational.
7. (Medium) Promo SKU + Try-Before-You-Buy credit utilization view.
8. (Medium) Calculation logic documentation per metric.

**Walk-in line for Bertrand/Loni:** "Apoorva's team stress-tested, found gaps, we're closing them. First Useful Result Rate incorporated. Report credible for Loni path after fixes." NOT "Apoorva validated."

---

## Rubin — CXO-wide AI Assistant Usage Dashboard

**Owner:** Angela Han (Sr Data Scientist Manager, Customer Engineering, San Jose). NOT in AEP PM chain — Data Science / Engineering. URL: https://rubin.adobe.io/dashboard/login

**Source confirmed April 16 (Karthik):** AEP AO chats DB. Different pipeline from Felix but same AEP infrastructure neighborhood. *"We are ingesting all the AI prompt / response events, so regardless of their origin, if they touch AEP AO -> we should have it in Rubin."* Contradicts Silvia's earlier "EH entry only" framing — Rubin is platform-wide, not EH-scoped.

**The inversion — Rubin needs something AEM has:** AEP provisioning API doesn't return org status (COMMERCIAL, NFR) for AEM-only orgs. Rubin can't cleanly count commercial AEM users. Felix has a local Prod orgs list. Karthik wants this scaled into AEP provisioning. **Felix's artifact = cross-org leverage.** Pedro's move: own the contribution, position AEM as the team that closes an AEP gap. Senior Director-level cross-org contribution.

**Contacts:**
- **Angela Han** — Rubin owner. Reports Richard Maraschi → Shivakumar Vaithyanathan (VP Platform Eng).
- **Karthik Penikalapati** — Rubin tech lead. Reports to Angela.
- **Silvia Mulet Ferre** — Sr Product Design Manager, Adobe Design (Austin). Eugene Bannykh's manager. Chain: Guliz Sicotte → Archana Thiagarajan → Eric Snowden → David Wadhwani.
- **Uma Subbu** — Sr Product Designer, Adobe Design (Chicago). Reports to Silvia. Co-investigating AEM AI Assistant + Agent usage with Felix's report + Rubin. UX hypotheses + UX Suggestions.

---

## AO 2.0 strategy + AEM-AO liaison

> **Moved to `project_aem_agents_intelligence_ARCHIVE.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

## Priority Consolidation View (KR4)

Draft saved April 24 at `AAI - Project Folder/Agent Reports/20260424 - Priority Consolidation View.md` (Phase 2 move target). Answers Loni's April 13 unanswered question (*"what % of top requests are making it into the agent"*).

Structure:
1. Answer to the Question
2. Top 10 Gap Categories table (classified measurement / product gap / value realization, with status + owner + ETA)
3. Closure Mechanism (Governance Agent AEMAGT-1240 as proof point)
4. What's New Since March (intent-level measurement, "no results found" as product gap, capability-level monthly usage as adoption narrative, voluntary platform consolidation)
5. What We'd Want Next (3 asks)
6. What This Is Not

Volumes + unowned routing pending Apoorva validation close. KR4 ship date moved May 1 → May 8.

---

## Stakeholder shortlist (AAI lane)

**AEM Agent PMs:** Apoorva Gupta (Discovery), Corey Dulimba (EPA), Philippe Kapfer (Governance), Greg Klebus (Content Optimization), Brian Chaikelson (EDA), Nick Whittenburg (Onboarding), Gabriel Walt / Mike Tilburg (Modernization).

**Agent PgMs:** Yanira Castaneda (AAI counterpart), Pritie Sharda, Robert Guthrie, Marius Duta, Amit Arora, Prashant, Georgeta Vladescu-Viezure, Juliana Campbell.

**AO / AEP:** Conrad Woltge (Sr Principal Architect), Trent Davies (eng, AO), Ken Russell (eng, AO), Sergey Generalov (PM, AO), Ian Boston (compliance), Manas Garg (AOv2 dev experience).

**Data / Reporting:** Felix Delval (data eng, EPA pipeline), Lara (taxonomy + Governance), Varun Kalra (Discovery validator, Apoorva's team), Karthik Penikalapati (Rubin tech lead), Angela Han (Rubin owner).

**Design (Adobe Design lane):** Silvia Mulet Ferre (Eugene's manager), Uma Subbu.

**Leadership:** Loni Stark (VP AEM & Commerce), Jean-Michel Pittet (VP Eng AEM), Jaclyn Eckersley (FinOps, AEM Eng VP-side), Bertrand de Coatpont (Sr Director PM, manager), Shankari Panchapakesan (Group PM, transitional).

**PMM:** Tina Nicu, **Tina Ngo** (Principal PMM, AEM agents GTM + customer-trial pitches — added NYL + State Street to a TBYB cohort 05-27 w/ Namita Krishnan; pricing/packaging angle. **DM'd Pedro 07-07 22:12 + 07-08 pre-attributing the coworker-migration lane** — "i hear you're leading the efforts for coworker migration across all aem agents… is there a standard weekly meeting you own"; Pedro pointed her to GA canvas F0BD4RALNHF. = comms-lane PMM counterpart to Akin, natural fold-in for the weekly / comms-plan. ⚠️ **NOT Tina Nicu** — two Tinas in PMM. `tinan@adobe.com`, U0284AYUX99), Akin (PMM for AEM survey + TBYB comms owner), Vaishnav Gorur (new PMM AEM agents — pending confirm Wed May 6), Haresh Kumar (chain to Vaishnav).

**Cross-VP peer (Sunil Menon tree):** Cole Connelly (Principal PM, Prompt Library Platform). Tim Lott → Daniel Sheinberg → Sunil Menon (peer to Loni at VP level under Amit Ahuja). Strategic backstop = Stephen Gould.

**Special:** Jim Stoklosa (dual — EH for Experimentation surface, AAI as report contributor for EPA).

---

## Interpersonal — Philippe Kapfer (competitor frame)

Senior PM under Bertrand. Scope: Governance Agent + Security. Arrived 2 years after Pedro. Took security perimeter from Pedro. **Potential promotion competitor — actively building Loni visibility** (Governance Agent / Enterprise Context getting named in Loni meetings, backed by Michael Marth).

**Pattern (April 2):** agreed privately on report-to-JIRA filtering, then pushed back on the same point once Bertrand was on the email thread. Pedro retracted publicly — bad move. **Tactic:** agree 1:1, create dissent in front of the boss.

**Pattern to break:** hold position under public pressure, don't retract. Recovery: reintroduce tracking concern at implementation as technical requirement, not debate. Stop using Philippe as first go-to for new trials (report-to-JIRA, new report sections) — use **Corey Dulimba** as first testeur instead. Giving Philippe early access to unpolished work hands him weak points.

**Second pattern (April 2):** uses Pedro as real-time mirror — gets Pedro to validate his positioning in side-chat during a Loni meeting. Pedro said *"very much on dirait hein cool!"* on governance/enterprise context, Philippe closed with *"C'est gentil mon loulou."* Pedro became active supporter without realising. He doesn't attack — he makes you applaud him.

Per Pedro's own framing: *"friends obsessed with girls will drop you for whatever is good for them in the moment."* Treat as colleague, not ally. Treat as competitor.

---

## Pedro's session-named development gap (May 1 self-diagnosis)

*"i have a bias for delivery and poor communication skills strategically."*

**Reframe:** broadcast frequency, not skill issue. May 1 night Slack to Bertrand was first rep on the muscle. Stack 3 reps a day for a month and the diagnosis stops being true.

---

## Status & Todo files (Obsidian)

**AAI canonical (post Phase 1 — 2026-05-03):** `2026/AEM Agents Intelligence/AAI - Project Folder/Status and Roadmap/AEM Agents Intelligence - Status and Todo.md`

**EH:** `2026/Experience Hub/AEM Experience Hub - Project Folder/AEM EH Status and Roadmap/EH - Status and Todo.md`

**Old `AI-Assistant - Status and Todo.md`** — DEPRECATED 2026-05-03, banner points to AAI canonical, frozen pending Phase 2 retirement.

**Mirror rule retired 2026-05-03.** Tasks live in their owning project's Status & Todo. Cross-link in dependent project's Focus if blocking.

**CLAUDE.md rule:** ask for conversation links when updating these files. Accept "no link, date/time" for internal-only meetings.

---

## Slack channels

`#dx-product-measurement`, `#tmp_aem_missing_prompt_library`, leadership-tight channel (Pedro+Yanira+Jaclyn+Conrad+Ian+Bertrand, created April 21).

---

## Open vault gaps (still tracked)

- Stakeholder Map Vaishnav entry (held until Wed May 6 confirmation)
- Pre-meeting strategic brief for May 11 Loni + JM (draft week of May 5)
- Briefing v0 sections 5-6 (pending Indicator #8 on May 17)

---

