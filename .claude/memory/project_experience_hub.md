---
name: AEM Experience Hub project context
description: EH-only after Phase 2 vault split (2026-05-03). Surface, contribution model, Sorin team, O2 personalization KRs. AAI work in sister file.
type: project
originSessionId: 298c09b0-7372-4e27-9660-87019bb7d26c
---

> **Phase 2 vault split landed 2026-05-03.** AAI content (agent reporting, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, Felix/Rubin/Varun threads, Apoorva punch-list, KR3/4/5/6) lives in `project_aem_agents_intelligence.md`. This file is EH surface, contribution model, Sorin team, O2 personalization KRs only.

> ## ▶️ 🟡 2026-09-22 — SLACK AUDIT 09-16 → 09-22, EH SIDE (full read: [[project_aem_agents_intelligence]] 2026-09-22 block)
> - **🟢 The nav asks are moving without a go from Pedro.** Adrian Ciulea 09-22: "I will be taking care of adding the LLM Apps menu item"; Sorin opened `HOME-926`, Laurentiu wrote the spec, asked Pedro for feedback (DM 09-22: "Looks very good!… Sorin has more experience"). Eugene 09-16: the Product Announcements widget already supports targeted, flagged announcements, use it for LLM Apps; wants a call with Pedro + Sorin + Laurentiu (Laurentiu "will set something up", 09-21). Pedro to Laurentiu 09-22: "one EDS page per announcement… image + text… click more for info", modelled on Brand Concierge.
> - **🟢 Announcements.** Pedro 09-22 11:11 `#experience-hub`: wants a Coworker Panel announcement, asked for the BC page with "the great design". Mihai Copae had already posted 09-18 in `#aem-bc-trial`: BC trial activate page updated to Peter Klassen's design, preview on stage (AEM FCCS2 Stage org, "Show me" button). Pedro 09-16 `#aem-cloud-foundation-pm`: kudos to Peter, "we'll pivot to request a similar design for next announcements".
> - **🔴 Guliz 09-16 DM: "I need you to add Silvia or me to every Coworker panel meeting… I really need to be there for anything CW related. I'll tell you why later."** Pedro agreed. Pritom Baruah dropped into the Coworker rollout sync proposing "alignment post GA on Coworker UI collaboration"; Pedro read it as wanting to drive; Guliz: "strange things are happening". Guliz also shared the Projects MVP roadmap; Pedro to sync with Horia. The "why later" is not on record.
> - **🟢 Pipeline troubleshooting button.** Temp channel `#tmp-cw-pipeline-activation-ui` 09-16 (Pedro): skills pulled for GA, button still live. Sorin 09-16: keep it, best effort. Sergiu: no, avoid disappointment. **Brian 09-17: remove the button until the AOv1-style implementation returns, Coworker version "a few weeks".** Pedro's plan 09-22 (to Tina/Yanira, then Brian): re-wire AOv1 into Coworker skills, keep the new-gen work with Manas/Trent, full switch "some weeks still".
> - **🟢 Ramon.** Support view shipped in Unified Shell 09-17 at `experience.adobe.com/#/aem/heimdall-security` (read-only for `AEMSecAlpha` and `Skyline SRE`, fetches what EH shows: Security Health, pen tests, CMK). Developers Live recording done with Ron. **He still needs the EH-priorities meeting with Pedro.**
> - **📦** Rotary calendar updated by Nicu 09-16 (Vlad's ask done); Assets code freeze 09-29, URR authoritative. Fred-as-a-Service: Pedro told Amit Gupta 09-22 "progressively de-commission… target of 6 months". `#experience-workspace-cm` (09-21): Felix Meschberger's brand-bucket model vs Bertrand's CM-program control plane; Ian: fix the EDS FQDN first, automate via CM APIs. Prodesp channel silent since 09-04.
> - ⚠️ **Tenth consecutive flag on the EH Status & Todo `Current Status`**, seventeen weeks. Pedro's to refresh.
>
> ## ▶️ 🔴 2026-09-16 — THE PANEL ACTIVATION NEEDS EH IN RODSON'S CHANNEL, AND THREE TEAMS WANT EH REAL ESTATE
> - **🔴 Panel activation is EH's front-door work now.** The AEM panel is announce 09-24 / TBYB activation the week after / SKU 10-05 (AAI 2026-09-16 block). Pedro asked 09-16 where to connect Rodson Clavel with the EH team → `#cxue-coworker-panel-hybrid-collaborators` `C0BCKG35NFP` (Rodson's; pinned activation recipe; Tim Lynn, Mark Doten, Mikaela Symanovich and Josh answer there; Bertrand is in, the EH team is not). Sorin, Eugene, Mihai and Adrian to be added; Pedro's own 09-01 activation thread there is dead after Philippe's 09-03 question. CORS and custom-domain rendering live in `#aem-wildcard-cors-enablement` `C0BTZS3APGF` — Mikaela's shell-domain render is becoming the real solution, not a temp fix; customer author domains land "in January" (Mark Doten 09-11).
> - **🔵 The instance-switcher question got an answer without AEM.** Peter Klassen, 09-07, in Bertrand's 08-31 `#p42-architecture` thread: "the plan is to consolidate with One AEM MCP - with NLS i believe choosing content sources would become obsolete." Pedro was not in the thread; whether that is EH's answer is his to say. Cole's instance-picker outline still owed.
> - **🔴 Three asks for EH real estate in one week.** Laurentiu Odoleanu 09-09 `#experience-hub`: Adobe LLM Apps in the left nav between UE and CM, GA November, feature flag for internal tenants first (Sorin) — asks Pedro's go. Peter Klassen DM 09-10: "ok to position Content AI there in the Navigation Pane?" Prodesp (Alexandre Boldrin, 09-04 then a nudge 09-11, `#tmp-prodesp-no-eh`): restrict EH per profile for politically isolated municipalities; EH deep links reach author features that were disabled, Cloud Manager visible without a product profile (`CMGR-72725`); Sorin apologised 09-14, "we will review and figure out an answer". Instances of [[Selection and Cross-Surface Consistency Are a PM Mandate]].
> - **🟢 Announcements and the release lane.** Mihai Copae 09-11 design proposals (Pedro: "I think i like it ! Specially the first one"), 09-14 improvements on stage (bigger title and image, centred, scrollable long content) awaiting feedback; wiki "How to create an announcement" 3696785260. Sorin 09-09: the LLM Optimizer announcement tenant list is being updated with Andrei Chiriac, flag re-enabled later that week. Ramon 09-16: Developers Live recording done with Ron (Security Scanning → Experience Hub → Claude + AEM MCP), support-view changes on Unified Shell 09-17, and he needs an EH-priorities meeting with Pedro. Vlad Bailescu 09-16: update the `uber-release-registry` dashboard with the new Rotary schedule.
> - ⚠️ **Ninth consecutive flag on the EH Status & Todo `Current Status`**, sixteen weeks. Pedro's to refresh.
>
> ## ▶️ 🔴 2026-09-02/03 — THE PLACEMENT QUESTION GOT ANSWERED BY A DATE, AND BERTRAND ASKED THE INSTANCE-SWITCHER QUESTION IN PUBLIC
> - **🔴 Lianne Ramos, 09-02 01:02, `#cx-coworker-trial-rollout-core`:** the AEM tab of Paul Midura's *Cohort 3* file is the list of AEM customers gaining Coworker on **09-08**; she asked for the AEM Gainsight *"You will soon have access to Coworker!"* alert to be deployed ~a week ahead (i.e. 09-02) and a reply in her thread once done. **This is the 07-15 Rachel / 08-05 Huong placement ask, now with a customer date on it.** No written EH placement decision exists; the alert is going out through the central channel regardless. Watch → [[watches]].
> - **🔵 Bertrand, 08-31 `#p42-architecture`:** saw a Coworker demo showing the *"active"* Workfront instance under the prompt; asks whether AEM wants the same, an active CS or AMS instance with a switch between AEM contexts *"as we do in the Experience Hub from the left hand side rail"*, Eugene tagged. **Unanswered. It is the front-door selection problem stated by Bertrand himself, and it is the instance-picker outline Cole Connelly owes.** Instance of [[Selection and Cross-Surface Consistency Are a PM Mandate]].
> - ⚠️ **Eighth consecutive flag on the EH Status & Todo `Current Status`**, now ~14½ weeks behind. Not banner-stacked; Pedro's to refresh.
>
> ## ▶️ 🟢 2026-08-10/11 — THE EH→COWORKER HANDOFF IS BEING BUILT, EUGENE IS BACK, AND DECISION #3 IS RESOLVING ITSELF UNDER TIME PRESSURE
> Source: group DM `C0BPMFYLTJL` (Mihai Copae, Sorin Slavic, Eugene Bannykh, Mircea Salan, Adrian Ciulea, Pedro), opened 08-07.
> - **🟢 Two working paths exist where there were none.** Mihai created `HOME-896`, then found a Coworker-API route (create `session` → get `episodeId` → create a `turn` with the prompt → redirect to the full page), tested with curl, and shipped **a testable first iteration on stage 08-10** — Coworker-gated, falling back to today's behaviour when Coworker is off. His own reservation: *"I do not like the fact that is taking too long for the both API calls to complete, before opening the window."* **Eugene, back from leave 08-11, surfaced a simpler one already in the repo** — `aem-home-ui#546`: write the prompt to the shared `next-gen-aia` cache (`initialPrompt`, `{ message, shouldSubmit: true, newConversation: true }`) and redirect the shell to `/coworker/`. He is careful about it — *"I dont know if the right way, just something that worked before."*
> - **🔴🔑 DECISION #3 OF THE 07-03 CHAT-ENTRY NOTE IS BEING ANSWERED BY THE CALENDAR, NOT BY THE ARGUMENT.** Eugene: *"We will probably need to hide the suggested prompts for some time: 24th may be too close to test all of them against Coworker. I think safest way is to just hide them until we are sure that they are either all working or updated to work with Coworker."* **Pedro's 07-03 call was pause/remove; Josh's side said keep-and-feed-AO2 on 07-08; it was never reconciled. Now engineering is proposing the pause for a different reason.** ⚠️ **Decide it deliberately rather than letting the GA date decide it** — it is EH's front door losing a visible feature on announcement day. Route stays Fu Chi (pipeline) + Zeus Courtois (AO2 recommendations). 🔑 Eugene also notes the populate-don't-submit behaviour matches Coworker's own prompt suggestions, so the pattern is consistent either way.
> - **⏳ A dependency on a team EH does not own.** The `ChatInput` component comes from **exc-app**; if reverting the open-in-side-rail change does not produce the full page, Mihai wants **Pedro to push exc-app for a fix before GA** (*"we need you to put some pressure"*). Same API (`ai.openChat()`) gates the **Troubleshoot with AI** buttons in the failed-pipelines widget and Cloud Manager — no fix means those go behind a feature flag and get hidden. **That is a customer-visible EH regression with an owner outside AEM.**
> - **✅ CLOSED 2026-08-15, PEDRO — "la demande de Brian a été faite avec lui online."** Brian Chaikelson had asked the same EH question three times (08-05, 08-11, DM 08-12 06:05 with a clock on it, *"I need to know for a GTM update I'm doing tomorrow (Wed)"*) — what is still in H2 for Experience Hub (extensions, personalization revamp. **It was handled live with him rather than in writing, so there is no artifact and no thread to cite.** ⏳ **One thing that does not follow from "done live" — whether the roadmap deck itself was edited.** Verify the slide before the 08-17 deadline passes, or it closes as a conversation and stays open as a document.
>   - **📍 The artifact is `FY26 Q4 AEM Roadmap.pptx`** → https://adobe.sharepoint.com/:p:/s/DExProductManagement/IQBrMybA6uWKQ4pbGoNUATXSAUHN_Sj3anuTijVr9s3Kk2g?e=ij6WsH — Brian copied it from the Q3 deck into the in-progress folder. Q3 (where the two EH items are written today) → https://adobe.sharepoint.com/:p:/r/sites/DExProductManagement/_layouts/15/Doc.aspx?sourcedoc=%7B9F3C21EC-8739-4E9E-8F97-F600C3FBC68C%7D&file=FY26%20Q3%20AEM%20Roadmap.pptx&action=edit — **Brian pointed Pedro at "around slide 57" on 08-07 08:06; Pedro replied "thanks, reviewing" and has not come back.**
>   - **🔴 DEADLINE 2026-08-17 for all roadmap slide updates** (per Gina's email, relayed by Brian). **Brian is on PTO from 08-13**, so for him it is 08-12. Thread → https://adobe.enterprise.slack.com/archives/GTYKF4UAC/p1785824018519439. Philippe has already updated Governance, Context and Security; Peter Klassen added Backup Retention.
>   - 🔑 **Same thread, Brian asked whether the Coworker docs strategy belongs in the roadmap deck. Pedro deliberately held it** (*"working on giving a heads-up to Loni before it appears on any doc, in sync with Bertrand"*). **The Loni note went out 08-12, so that hold is now released and both answers are owed together.**
> - ⚠️ **Fourth consecutive staleness flag on the EH Status & Todo `Current Status` (2026-08-11), ~11½ weeks behind.** Deliberately NOT banner-stacked in the note — it already carries prior banners and the 08-06 cleanup named stacked banners as the failure mode. Flagged in `watches.md` instead. **It is Pedro's to refresh.**
>
> ## ▶️ 🔴🔑 2026-08-05 — THE ASK FOR EH'S FRONT DOOR CAME BACK, FROM A SECOND PERSON, WITH A ROLLOUT CLOCK ON IT. AND A COWORKER-SIDE PM ASKED WHAT EH's SUGGESTED PROMPTS BECOME.
> Source: the weekly AEM→Coworker rollout sync, 08-05 (full read AAI-side, `project_aem_agents_intelligence.md` **2026-08-05 ROLLOUT SYNC block**). Room: Pedro, Yanira, Namita Krishnan, Cole Connelly, Yelena Doliner, Huong Vu. Rachel absent.
> - **🔴🔑 THE PLACEMENT ASK, SECOND TIME IN THREE WEEKS, NOW ATTACHED TO A DATE.** The Coworker rollout runs a **one-week pre-flip announcement** — Gainsight banners plus admin emails — and its purpose is the exit: **Namita**, *"we've seen some admins actually responding back to that e-mail saying, oh no, I don't want it. So just giving them a chance to be prepared for this transition and **opt out if needed**"*, framed as *"based on a learning we had from the previous trial"*. **Her ask, verbatim:** *"for AEM customers, what are some surfaces we can use, right? Like admin emails, for sure we should do it, but then **in the surface, in AEM**, like **Shankari used to help us with gainsite**, so how can we do that? How can we do some kind of **banners** as well?"*
> - **Huong Vu — and ⚠️ she is not new, which is the useful part.** **Senior PMM, San Jose, reporting to Akin Ajayi** (Coworker PMM). She was already in [[project_adobe_org]] and in the AAI Stakeholder Map under Akin, and already a watch target on 07-15. 🔑 **Akin's team is the distribution channel Bertrand routed Pedro's AIA cutover comms through on 07-07** — Pedro drafts, they hold the machine. **So the EH placement ask is coming through a relationship that was mapped a month ago and never used.** She split the mechanism: **admin emails go from one central channel** to any customer licensing a CXL application; **the in-surface banner needs coordinated AEM work**, because *"[Gainsight], it seems like we have different mechanism for surfacing in AEP, like CDP, AJO, and then AEM… we'd love the team's help on also surfacing the same copy in AEM as well, just to maximize the chance of the right user seeing it."*
> - **→ THIS IS THE 07-15 RACHEL ASK, RE-ASKED BY SOMEONE ELSE, WITH A FLIP DATE BEHIND IT.** Rachel's *"where are all the placements in AEM that we can take over?"* is still unanswered by AEM three weeks on, and she was absent again today. **The difference is that GA is now 08-24 and the announcement fires ~one week before each cohort flip, so the placement decision has a deadline it did not have on 07-15.** ⚠️ **A banner and a Gainsight popup placed by another team, on the EH front door, is precisely the silent-replacement case decision #2 exists to prevent** ([[Selection and Cross-Surface Consistency Are a PM Mandate]]). **Answer it deliberately and in writing — which EH placements, whose copy, who owns the trigger.**
> - **🔴 SUGGESTED PROMPTS — Cole Connelly asked what they become in Coworker.** *"the prompts that you want to surface when users first come in as suggestions. I think we should talk about what those prompts might look like in the coworker world."* → **This is decision #3 of the 07-03 chat-entry note (pause vs keep the Fu Chi feed), still unreconciled since Josh's side said keep-and-feed-AO2 on 07-08.** The platform is now asking AEM for the answer. **Fu Chi is the pipeline owner; Zeus Courtois owns the AO2 recommendation side.**
> - **⏳ Cole's third item, the AEM instance picker, is banked AAI-side but is EH-shaped** — AI Assistant had an API listing a customer's AEM instances, and Cole wants AEM's outline before go-live because *"we want to make that selection process ergonomic because it was really painful in AI assistant"*. **It is the front-door selection problem in a Coworker-UI shirt.**
>
> ## ▶️ 🟢 2026-07-30 — SECURITY HEALTH SHIPS IN EH: THE FIRST "SECURITY AND COMPLIANCE" SURFACE, AND A RELEASE-NOTES PARAGRAPH DELIVERED.
> - **Security Health is live in Experience Hub** (doc read 07-30: AEM CS "Security Health" page, last update 2026-07-15). Daily scans of **production environments only**, results surface in EH under the **Admin & IT profile**, in a new left-nav section **"Security and Compliance"** that also lists **Penetration Tests**. Three finding types, aligned OWASP Top 10: 3rd-party **Java** library CVEs (A03:2025 Software Supply Chain Failures — CVE ID/score, grouped bundle/group/library, CSV export), **redundant permissions** and **overly broad/insecure permissions** (both A02:2025 Security Misconfiguration). KPIs with 30-day comparison. **Limitations: prod-only, Java-only (no JS/UI deps).**
> - **📤 Release-notes paragraph (EN) delivered in-chat** for Pedro's "super release notes". Everything sourced from the doc **except** the closing "additional types of security findings will be added over time" — Pedro's own addition, phrased as roadmap intent, flagged to him ([[feedback_separate_facts_from_proposals]], [[feedback_audit_outward_artifacts]]). His call left open: name the two limitations or not (field will find them).
> - **🔑 The contribution-model receipt:** a non-EH team's capability shipping *through* EH's surface, with its own nav section and profile targeting. The line for any broader comm: **EH is becoming the surface where AEM exposes its operational posture — security today, more tomorrow.** Feeds G3's narrative with a shipped case, not a plan.
> - **✅ UPDATE 2026-08-14 — THE PUBLIC DOC IS LIVE AND IT NAMES BOTH LIMITATIONS.** https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/security-health — the open call from 07-30 (say the limitations or not) resolved to **say them**, in a dedicated `Limitations` section: prod-only, Java-only. Whoever wrote it, the decision is made and Pedro should not re-litigate it.
> - **📊 THE SUCCESS NUMBERS ARE RAMON'S, IN HIS 2026-07-30 16:14 DM DRAFT, NOT IN THE DOC.** Go-Live announcement draft targeting `#one-aem-team-announcements` plus manager emails; Pedro approved it in chat at 17:02 (*"Looks goooood !"*). Verbatim: **"during Limited Availability (20 customers): 74% of LA customers remediated vulnerabilities, vs. just 28% across all AEM customers — visibility drives action"** and **"914 production programs currently carry 51,101 open third-party library vulnerabilities."** ⚠️ **n=20, self-selected, against a whole-base comparator — the two denominators are not comparable. If it goes into any artifact that travels, the n goes in the same sentence** ([[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]]).
> - **🔑 The "why we built it" that beats the doc's, also Ramon's and also unpublished:** *"AI-accelerated development is pushing more code (and more vulnerabilities) into customer apps. Those risks aren't just the customer's — they can hit platform stability and Adobe's reputation if a breach goes public."* The doc stops at *"without waiting for a scheduled security audit"*. **The Adobe-side argument exists only in a DM.**
> - **🔑 The real unlock is Adobe's response capability, and it is a future claim.** Ramon's `What's next`: notifications on new vulnerabilities, proactive monitoring and outreach, and *"for the next Log4j-style event, we can instantly identify impacted customers and reach out to them."* ⚠️ **On 2026-06-22, on a live foundation-release regression, the same person wrote *"I don't think we can see the number of potentially impacted customers via logs etc"* — so this is a capability GA makes possible, not one already demonstrated.** Do not state it in the past tense.
> - **⏳ STILL OWED BY PEDRO: the go-to-market half + monthly release notes.** Ramon asked twice on 07-24 (*"still waiting for my documentation draft"* / *"is the go to marketing / monthly release notes prepared for Security Health GA?"*), Pedro answered *"That is on my todo P1"*. ✅ **Confirmed by Pedro 2026-08-14: the Go-Live announcement DID go out.** So Ramon's 74%-vs-28% and the 914 / 51,101 figures are **already public inside Adobe**, not draft — treat them as quotable but keep the n=20 caveat, because a published number gets requoted.
> - **✍️ 2026-08-14 — Pedro is writing the `User Value / Why we built it` and `AEM Value Unlock & Priority` fields.** ⚠️ **His first stub said the feature exposes the security posture of "customer code and platform" — "platform" is wrong** and the doc's own Limitations section contradicts it. What is scanned is the **customer's** application layer: third-party Java libraries in custom code, and access-control entries in their permission configuration. **Adobe's platform is the scanner, not the subject.**
>
> ## ▶️ 🔴🔑 2026-07-22 — **NO EH USAGE NUMBER IS PEDRO'S OWN, AND THE MEASUREMENT CHAIN WAS NEVER CONNECTED.** (Found preparing the check-in — [[project_checkin_2026]].)
> - **The latest EH figure: 14,000 weekly users, 79% return rate. Dated 2026-06-05.** Source = **Guliz Sicotte**, stated at the EH / Experience Workspace / Skills design alignment meeting (*"not just a springboard… what people consider home to kick off their workflows"*), banked as a "new banked metric" in the State of the Project. **It is Design's number about Pedro's product, not an EH-instrumented measurement.** He re-used it 07-15 with Rachel + Namita. **Attribute it to Guliz when citing — attribution strengthens, being asked for the method does not.**
> - **The prior figure: 2026-04-02 EH Demo — growth "stuck at 85%", returning users ~62% stable, new-user count dropping.** Source = **Sorin**, spoken. ⚠️ **Do NOT juxtapose with the June figure** — different metrics, different people, and side by side they imply a 62→79 improvement that probably does not exist.
> - **🔴 Nothing since 2026-06-05. Seven weeks, and no number Pedro produced himself.**
> - **🔴🔑 THE ROOT CAUSE: the Grafana cross-check was never done.** Memory has carried "Grafana access obtained April 8" since spring, but the Bertrand 1-1 questions file (mtime 2026-06-30) still reads *"Grafana cross-check — need to join the IDP group… Is access still possible via that path?"* → **the access is neither confirmed nor used, three months on, and the cross-check against Felix's reports never happened.**
> - **→ This is why Bertrand's 2026-04-13 claim (EH = key driver of AEM MAU growth, >60% of the customer base) is still backed by no dated figure.** It is not a writing omission, it is a measurement chain that was never plugged in. **On a goal whose title is "measurable driver of adoption growth", Pedro has produced no measurement.** ⏳ watches.
>
> ## ▶️ 🔴🔑 2026-07-15 — AEP ASKED FOR EH'S REAL ESTATE, BY NAME. *"Where are all the placements in AEM that we can take over?"*
> Source: the Rachel + Namita rollout sync, 07-15 (full read AAI-side). ✅ Attribution clean — Pedro alone in the room.
> - **Rachel Hanessian showed a Miro board of the customer-facing transition** — *"the experience changes that we are expecting. **This is what Cole is driving with the UI team**"* — and it lands **on EH's surface**. The states: **today** = left-nav item + homepage entry + full screen + rail · **next** = a **banner** (*"CX Enterprise Coworker is coming soon. It's an evolution of AI assistant"*) **+ a Gainsight popup** (she asked *"do you guys use gainsite in AEM?"*; Pedro: *"we do, yeah"*) · **then** = the same banner with **"Try now"** → opens **full screen**, *"you won't open the rail because **we don't have the rail yet**"* · **eventually** = the Coworker rail.
> - **🔴🔑 THE ASK, VERBATIM:** *"we should work with you on like where, because I don't know, **do you have this type of banner in AEM, or where are all the placements in AEM that we can take over?**"* → **AEP is asking AEM which of its surfaces they may occupy, and EH is the surface with 14K weekly users and a 79% return rate.** **This is the most direct ask on Pedro's own product anyone has made in this migration, and it arrives as an open question rather than a fait accompli.** → **Answer it deliberately: EH's entry routing is the thing Pedro has spent two months arguing EH must own** ([[Selection and Cross-Surface Consistency Are a PM Mandate]]). **A banner + Gainsight popup placed by another team, on the EH front door, is exactly the silent replacement decision #2 exists to prevent.**
> - **⏳ Rachel owes the Miro/mural.** **Get it — it is the customer-facing message, already drawn, for a surface Pedro owns.** ⚠️ Naming wobble she caught herself: *"that should not say coworker chat… that should just say **coworker**."*
> - **🔴 Rachel is out ~07-16 → ~07-29; Pedro is out from 07-20.** If the placements conversation does not happen this week, **it happens without either of them.**

> ## ▶️ 🔑 2026-07-15 — THE RAIL IS NO LONGER MANDATED. THE EH ENTRY FORK IS AEM'S OWN CALL, AND AEP SAID SO.
> Source: the Coworker demo to the AEM agent team (07-15, Horia Galatanu + Manas Garg + Rachel Hanessian; full read AAI-side, `project_aem_agents_intelligence.md` 07-15 block). ⚠️ Room-mic transcript, three people on one label — see [[reference_transcript_glossary]] before quoting.
> - **🟢 Horia Galatanu (AEP, Sr Dir PM), verbatim:** *"there's been a slight change in philosophy where… **We don't want to necessarily mandate that, hey, it has to be a right [rail]**… We're asking the applications to kind of take the lead and figure out how it works for them. For [some] application, it makes more sense to have some sort of a **floating bar**… for others, the **right rail** still makes total sense… it becomes **a bit more of a product by product thing**… the goal is more around **interacting with the page and being able to take actions on that page** versus performing exactly what you would be doing in the full screen."* **Manas Garg confirmed:** *"from this point onwards, these are application concerns."*
> - **→ THE SORIN-vs-EUGENE FORK WAS NEVER AEP'S TO DECIDE.** Sorin leaned rail, Eugene leaned full-screen, both waiting on Josh. **The platform owner has now said the pattern is the application's choice, per surface.** Pedro's **destination-agnostic handoff-contract** position and the **EH-owns-the-entry-routing** thesis are backed by AEP, in front of Bertrand. Decisions #1 and #2 (keep the centre bar, repoint the handoff) are **AEM's to make and defend, not to wait for.** Clean corroboration of [[Selection and Cross-Surface Consistency Are a PM Mandate]] and of [[There Waiting Has Two Forms — Consistent Chat or (Often) Invisible]] — Horia independently reached the entry's exact claim (form follows the surface; floating bar here, rail there).
> - **🔴 THE COST, AND NOBODY IN THE ROOM NAMED IT.** *"You're holding the keys to your destiny"* also means **the EH chat surface is now AEM's build, on AEM's estimate.** If the entry pattern is an application concern, **EH inherits UI work that is in no plan and no headcount** — with Sorin at ~1 effective engineer plus two June hires. **Do not celebrate the autonomy without pricing it.**
> - **🔴 THE RAIL DATE SLIPPED, FROM THE ROLLOUT OWNER. Rachel Hanessian:** *"the **context awareness piece is there**. The rail is **still being kind of retrofitted**… a version to be tested… **in like 2 weeks**… **code complete would be end of month. I expect it to be a few more weeks after that till we get it polished and out.**"* → **07-31 is code-complete, not availability.** Testable ≈ 07-29, out ≈ **mid-to-late August**. **Everything EH-side planned against "the rail ships 07-31" needs re-dating.** Context awareness already exists — that half is not the blocker.
> - **📤 This sharpens the Silvia message already owed** (watches, due before 07-20): Eugene's condition is met (the harness sees and acts on the page), full-screen survives, **and now the rail-vs-full-screen choice is explicitly AEM's** → **unblock Eugene's sketch and let him and Silvia make the call.** That is their lane ([[user_ui_cx_gap]]), and it is now formally open.

## About Experience Hub

AEM Experience Hub is the unified home screen / landing page for AEM Cloud Service at experience.adobe.com. Launched August 2024. Previously named AEM Home and AEM Launchpad. Not a replacement for existing AEM UIs. An action-oriented entry point that surfaces the right tools per persona.

**Current PM:** User (took over from Shankari March 2026.)

**Org:** User → Bertrand (Senior Director PM) → Loni (VP PM for AEM)

**Obsidian vault root:** `/Users/pedrofer/ObsidianAdobeVault/020 Professional/Adobe/Projects/2026/Experience Hub/`

---

## 2026 Yearly Review Goals (drafted with Bertrand, April 2026)

**G1 — Agent Intelligence & Reporting (now AAI scope):** see `project_aem_agents_intelligence.md`. Listed here for completeness — built and owned via the AAI surface.

**G2 — EH Platform Integration:** Own Experience Hub's integration with AEP and Adobe DX, including AO 2.0 migration and the new agent prompting surface. Ensure EH remains a reliable and current entry point as the underlying platform evolves.

**G3 — Experience Hub Adoption & Growth:** Establish Experience Hub as the measurable driver of AEM practitioner adoption growth, with data and narrative that leadership can point to at any level. Document and attribute EH's contribution to AEM monthly active user growth. Deliver the contribution model and user profiling that make EH contextual and extensible, and enable other teams to surface their work through EH as a shared platform.

File: `AEM EH - Key Files/Experience Hub - 2026 Yearly Review Goals.md`

---

## Team and Capacity (confirmed April 1, 2026 Sorin 1:1)

Pedro is PM of record. Team: Sorin Slavic (lead engineer), Eugene Bannykh (UX, US timezone), Mircea Salan (engineer, internship project lead), Anna Maria (intern).

Effectively 1 engineer. Sorin split across multiple projects. Anna Maria cannot contribute meaningfully near-term. Mikhail and Anastasia departed around the same time she arrived. Hiring pipeline open: best case May 1 first hire, June 1 second. Worst case: summer or positions closed. Roadmap declares 3 (1 + 2 in progress) for planning. Headcount minimum for roadmap: 5. EH bundled under Growth and Adoption.

Sorin's framing: "We are not a big house, but we are a proud house."

**Eugene Bannykh's manager:** Silvia Mulet Ferre (Sr Product Design Manager, Adobe Design, Austin) → Guliz Sicotte → Archana Thiagarajan → Eric Snowden (SVP Adobe Design) → David Wadhwani. Adobe Design is a separate VP chain, NOT AEP — relevant for cross-org coordination on EH UX.

---

## 3 Product Priorities for 2H2026

**Priority 1 — Skills + MCP surface**
Replace generic prompt grid with skills-aware, MCP-connection-aware chat surface. AO 2.0 lands May–July — right moment to redesign. Bertrand brief drafted (`EH as the Skills and MCP Surface - Bertrand brief.md`). Hold until Eugene's design view reviewed and MCP current state confirmed with Sorin.

**Priority 2 — Contribution Model / UX AI Framework**
Full alignment Pedro + Eugene + Sorin (April 1). Sorin independently drafting — main focus for 2 open reqs (UX + AI). Pilot mechanism: +Add Extension (App Builder, React SPA, IMS identity). Mircea Salan demoed March 27 — not production-ready. Known gaps: feature flag not activated, App Registry instability, stage-to-prod manual command, iframe context injection limited to user profile only, wizard needs simplification.

**Priority 3 — Customer Profiling**
5 profiles (General, Content Author, Asset Librarian, Developer, Admin). Bertrand deprioritized. Pedro's reframe: profiling is the mechanism that makes Priority 1 contextual, not a standalone ask. Don't raise until Skills+MCP is validated.

---

## 2H Roadmap

HOME-832 in JIRA (created April 1, 2026) — four H2 initiative descriptions: AI Assistant Integration Improvements, Collaboration Model Implementation, User Profiling Research, Supporting Teams and Promotional Surface. Working draft: `Home 2H2026 Roadmap - Experience Hub EH.md`. Canva roadmap planning doc still to be located and shared with Sorin.

---

## EH as MAU Driver — Claim to Own

Bertrand quote in April 13 Loni meeting: *"I would like to think that what we did with Experience Hub has been a key driver in expanding the number of monthly active users for AEM."* >60% customer base. Pedro's product. Surface this claim explicitly — own it, back it with data, make it a narrative Pedro controls. Stable metrics deck (KR5) is one vehicle. Grafana access obtained April 8 — cross-check vs Felix reports outstanding.

---

## EH Surface Integrations

### Brand Concierge Light-up — Summit Deadline (April 19-22, 2026)

Three options discussed in April 1 refinement sync. Sorin confirmed full production implementation is too late. Eugene designed wizard ~1 month ago. Bertrand contributed to shaping. Content AI indexing takes hours — can't be faked on customer side. Cloud Manager micro frontend PR (Peter's team) still open. Decision sent to Bertrand + Peter. Effective answer deadline April 2.

### Experimentation Page Integration (Jim Stoklosa's team)

Experimentation page is a full-screen landing page + sub-pages, not a widget. True to Eugene's mockups. Not all customers get it — contextual experimentation is an extension, not a default entitlement. Available across all AEM flavors.

EH responsibility: feature flag + navigation button visibility logic. Business logic (which tenants see it) defined by experiments team via API condition — EH maintains it but cannot define it alone. Micro frontend implementation: experiments team's responsibility (same model as security team). Sub-pages: experiments team must declare them so EH can manage pathing. Recent widget: experiments team should onboard their noun to unified shell recent service.

Jim's team: Dereje Dilnesaw (required), Julien Ramboz (required), Sanjeev Verma (optional). Slack sent April 1; Dereje responded April 8.

### Prompt Search (April 2 EH Demo)

Unified search for assets via AI assistant prompt (click +) is almost done. Returns results from first production repository user has access to — same as semantic search in AEM Assets. Bug confirmed: pulls from first prod repo only (context bug). Working with CJ analytics team on tracking gap between displayed and recorded prompts. Search still only covers assets — pages, content fragments, experiments, launches not included. Context bug (multi-environment users default to first prod env) still open.

### Adoption Data (April 2 EH Demo)

- Growth stable but stuck — Sorin: "stuck at 85%"
- Return users stable at ~62%
- New user count is dropping
- Prompt suggestions: steady views. "Content or knowledge" prompts most used.
- Analytics tracking bug: gap between what's shown and what's recorded — working with CJ analytics team

---

## Fu Chi (AEP Personalization) — EH-side personalization owner

Fu Chi (AEP team) built the personalized prompt recommendation pipeline. Weekly 1:1 with Pedro. Shankari was invited to first sessions.

**Architecture she owns:**
- Pipeline: user prompts → clean → embeddings → K-means clustering → topic reports
- Signal blending: user history (primary) → org signals (fallback) → global signals
- Output: CSV/table of user IDs + ranked prompt recommendations
- EH owns prompt bar + buttons. AEP owns right rail.
- Prompt library is centralized — agent owners can enrich it

**Already exists in her data:** behavioral cluster analysis (content authoring, asset focus, cloud manager usage) — raw material for Priority 3 (Customer Profiling). Real, not hypothetical.

**Workflow-aware recommendations** (suggest next action based on prior steps) on her roadmap, not yet prioritized.

**Open actions with Fu Chi:**
- Fu Chi to share prompt recommendation file
- Fu Chi to share Analytics DB wiki page for widget recommendation analysis
- Fu Chi to send draft email + spreadsheet for agent owner prompt review (March 25 ask — status unclear)
- Fu Chi to share Workfront persona use case (March 25 ask)
- Pedro to review prompt file with Sorin + schedule follow-up

---

## Cross-VP — Prompt Library Platform (O2 KR `EH consumes prompt library not wiki`)

Added April 28, 2026:

- PM: Cole Connelly (Principal PM, NY)
- EM: Joshua Hailpern. Lead engineers: Somya Biswari, Zeus Courtois.
- Org chain: Cole → Stephen Gould (GPM, SF) → Tim Lott (Director, Lehi) → Daniel Sheinberg (Sr Director) → **Sunil Menon (VP, Experience Cloud Portfolio, SJ)** → Amit Ahuja → Anil Chakravarthy.
- **Sunil Menon = peer of Loni Stark at VP level** under Amit Ahuja. Prompt Library Platform sits in his tree, NOT in AEM/Loni's.
- Right ladder: tactical Pedro→Cole, strategic Pedro→Stephen Gould (also Pedro's existing DX/Unified Shell contact), portfolio decisions Loni→Sunil at VP layer.
- Org-chart screenshots: `screenshots/20260428-org-*.png`.
- **2026-05-19 bridge:** Joshua Hailpern (EM here) also leads AIA UI / Mithril / Fruitbar; Somya Biswari + Zeus Courtois are lead engineers on both. Prompt Library Platform and Mithril/Fruitbar = same engineering galaxy under Sunil Menon's tree. Full note in `project_aem_agents_intelligence.md` "May 19 — Engineering bridge".

---

## Interpersonal Watch (cross-cutting, kept EH-side)

| Person | Dynamic | Notes |
|---|---|---|
| Philippe Kapfer | Senior PM under Bertrand. Scope: Governance Agent + Security. Arrived 2 years after Pedro. Took security perimeter from Pedro. Potential promotion competitor — actively building Loni visibility. | Tactic: agree 1:1, create dissent in front of the boss (April 2). Pattern to break: hold position under public pressure, don't retract. Recovery path: reintroduce concerns as technical requirements, not debates. Use Corey Dulimba as first testeur for unpolished work, NOT Philippe. Treat as competitor, not ally. He doesn't attack — he makes you applaud him. |

---

## Sorin Workstream — Active Threads

### Data Compliance — Risk accepted (Bertrand, April 1, 2026)

Ian Boston (April 1) confirmed two legal risks with the agent reporting pipeline (data residency cross-region pull, governance/deposition risk). **Bertrand's decision (April 1):** "Ian's comments are important but not critical. We continue with Felix." Decision logged in `/decisions/2026-04-01-data-compliance-continue-felix.md`. Pipeline ownership lives AAI-side now; EH carries the surface implication only — the EH integration does not introduce additional compliance scope.

### Open Outreach (April 2, 2026 baseline)

| Person | Topic | Status |
|---|---|---|
| Ilya Grafutko | QI program synergy | Met April 14 |
| Ian Boston | Regional data aggregation | Confirmed two legal risks April 1 |
| Bertrand | Data compliance | Risk accepted April 1 — closed |
| Peter Klassen | Brand Concierge light-up option | Responded April 2 (full proposal) |
| Jim Stoklosa + team | Experimentation page onboarding call | Dereje responded April 8 |

---

## EH Status & Todo (Obsidian) + Key Files

All paths relative to: `/Users/pedrofer/ObsidianAdobeVault/020 Professional/Adobe/Projects/2026/Experience Hub/AEM Experience Hub - Project Folder/`

- Status & Todo: `AEM EH Status and Roadmap/Experience Hub - Status and Todo.md` (renamed from `EH - Status and Todo.md` 2026-05-03)
- Bertrand 1-1 questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Bertrand.md` (cross-cutting, kept EH-side)
- Sorin 1-1 questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Sorin.md`
- State of Project: `AEM EH - Key Files/Experience Hub - State of the Project.md`
- Stakeholder Map: `AEM EH - Key Files/Experience Hub - Stakeholder Map.md`
- 2H Roadmap draft: `Roadmap/Home 2H2026 Roadmap - Experience Hub EH.md`
- EH Evolutions proposal: `202603 - EH Evolutions proposal.md`
- Bertrand brief: `EH as the Skills and MCP Surface - Bertrand brief.md`
- MOC: `🎯 AEM Experience Hub MOC.md`
- Meeting notes folder: **moved out of EH folder 2026-05-13** → `/2026/Meeting Notes/` (neutral, shared with AAI and other projects). Previously `Adobe Projects 2026 Meeting Notes/` under EH project folder. Rename + move applied because folder content (Bertrand, Felix, Namita, Ian, Yanira 1-1s) was cross-cutting, not EH-specific.

---

## Slack Channels (EH-relevant)

`#experience-hub`, `#experience-hub-ai-assistant`, `#aem-home-platform-team`, `#aem-home-core-team`, `#temp-experiencehub-dxue`, AEM experience hub extension builder.

---

## Reporting chain

Pedro → Shankari Panchapakesan (Group PM, SJ) → Bertrand (Sr Director PM, Basel) → Loni Stark (VP AEM & Commerce, SJ) → Amit Ahuja → Anil Chakravarthy → Shantanu Narayen. Arrangement temporary — Shankari moving to report directly under Loni on a 6-month trial. Pedro's check-ins go directly to Bertrand. Loni's actual title: **VP, AEM & Commerce** (PM + Product Marketing).

---

## May 5 Bertrand 1-1 — EH-side drop-ins

Source: `Meeting Notes/Bertrand 1 1/20260505 - Bertrand Pedro 1 1_otter_ai_transcript.txt`. AAI signals in sister memory file.

**Mithril / Coworker (Joshua Hailpern team).** AI Assistant V2 with "mode rail" (observer + suggestion). Launching ~late May (T-25 days). **AEM Sites NOT included** — repeat exclusion pattern (also Modernization Agent + Experience Workspace). Bertrand asked Sorin + Eugene to do Mithril review. Pedro saw UI via night Slack May 4. Bertrand: *"Ça va être un point important pour la migration AOv2 si on y va."* Bertrand actioned: chase Guliz on XD/Adobe-Design loop visibility.

**Marcus Räck (Experience Workspace creator).** Declined Pedro's unified-chat ask: *"je pense qu'il faut chaque solution ait son propre tchat."* 4 chats now (Experience Workspace, Modernization, Slick, Rosetta=Manager Services). ⚠️ **"Slick" + "Rosetta" = low-confidence names** — from a garbled May 5 Otter auto-transcript (*"sleek… le chat dans Rosetta qui est la version manette services"*, Unknown Speaker; "manette services" = mis-heard "Manager Services"). Pedro didn't recall the names 2026-05-28, will verify later. Don't assert as canonical until confirmed. Pedro pushing common substrate (history, context). Bertrand views chat unification as AOv2-migration-relevant.

**Cédric Huesler — repair contact.** Pedro got him annoyed via Slack push on AOv2 + contribution model May 5 morning. Tactical contact for Experience Workspace + AOv2-on-Sites discussions.

**Sylvia Mulet Ferre auto-fix-prompt initiative for EH.** Sylvia (Eugene's manager, Adobe Design / Guliz tree) launching: hypothesis = users come once and stop because request too complicated from start. Bertrand skeptical: *"je sais pas trop où elles vont venir avec ça."* Track scope + intersection w/ Eugene.

**Customer migration pattern.** 1-year migration deadline approach. Decouple "platform update" vs "platform move." Nico's content-repo migration initiative waking customers up — many need re-migration with hard deadlines.

**EH headcount note.** *"On va avoir 2 personnes qui sont remplacées pour Experience Hub. On va être de trop"* (Bertrand).

---

## May 12 — Bertrand 1-1 EH-side drop-ins

Source: `Meeting Notes/Bertrand 1 1/20260512 - Bertrand Pedro 1 1.md`. AAI-side content in sister memory.

**1. 🆕 Quiet Hours Update via Agents — beta launching.** Activated on ID. Customers run **Quiet Hours-Update via the chatbot/agent** (free). Beta cohort: (customers who previously used Quiet Hours Update) ∩ (customers w/ AI) = **81 customers** to activate. Expect dozens of feedback. **Ties O4 (Ship Quiet Hours).** Concrete proof point for May 11 deck "customer trust increase" slide. Companion to Bertrand customer-trust slide (Pedro to add quote-worth slots).

**2. 🆕 Breaking changes manager — name rename needed.** Raspberry team finds "breaking changes" too negative. Concept stays: central repo declaring breaking changes w/ dates, impacted customers, procedures, docs. For ~120 customers internal use + customer-facing awareness. Pedro action: source new name.

**3. 🆕 Two new EH hires start beginning of June.** ✅ CONFIRMED started 2026-06-01 (Pedro, 2026-07-03) — the System Review "did they start?" flag is closed; onboarding plan still open. Resolves Bertrand May 5 *"2 personnes remplacées pour EH"* note. Profiles:
- One ex-AEP.
- One full-stack AI engineer (*"qui fait pas mal d'AI"*).
- Bertrand: *"ça peut vous aider à coder plein de trucs."* Capacity inflection for EH eng (Sorin = 1 effective today).

**4. Customer update push state — O6 lever.** ~120 customers behind on Content Fragments / content freshness. ~100 still behind. **Aldi (7-8 programs) + Volkswagen + Americans** = key targets. Plan: propose manual update first → automatic update later. **1-year window option:** customer commits to test impl + monthly platform updates while staying off auto-update. CSM one-by-one outreach. Mostly positive responses to progressive migration. Ties to O6 Aging Customers (slipped end-March KR).

**5. AOv2 + skills + context framing.** EH-relevant fragments: cross-surface AI-Assistant continuity Bertrand wants (chat history retrievable across surfaces); Michael compliance pushback (data residency primary-region constraint). Open product question for EH surface = where does the AI Assistant icon route post-Mithril (per-surface context vs global Assistant). Full AOv2 framing in AAI memory.

**6. Sylvia auto-fix-prompt initiative status.** Bertrand May 5 flagged. May 12 update: Sylvia "very actively" in contact with Tim Lynn (Mithril). Pedro coached her to synchronize w/ Guliz but hedge on AOv2. Bertrand: Gilles + Michael had AOv2-counterpart meeting with Manas + Ken — relayed *"v1 was very complicated."*

**Pedro action items from EH side:**
- Slot Quiet-Hours-via-Agents 81-customer beta into May 11 deck customer-trust slide.
- Find rename for "Breaking changes manager."
- Verify Grafana JSON-size issue post-Raul-list-fix before next exec demo (cross-cutting, also AAI).
- Confirm AI Assistant SKU/pricing model w/ Bertrand (cross-link Mithril Silvia pricing question).
- Onboard plan for 2 June hires.

---

## May 12 — Mithril Silvia Eugene Pedro sync (EH-side anchor)

Source: `Meeting Notes/Eugene/20260512 - Mythril Silvia Eugene Pedro Sync.md`. Full notes in AAI memory. EH-side anchor:

- Silvia use case = **context-reading, not UI-interaction.** *"We don't want AI to interact with UI. We want AI to read UI."* Mithril MVP misses this.
- Eugene framing: post-Mithril, AI Assistant icon becomes contextual per surface (pipeline, etc.). Pre-Mithril = dummy shortcut everywhere.
- 🆕 **Matthew** = Mithril co-owner alongside Tim Lynn. Surname TBD. Tomorrow May 13 Silvia + Eugene + Tim + Matthew sync. Pedro not invited — Silvia reports back.
- 🆕 Migration window UX problem: multi-month window with mixed v1/v2/migrating agents. User confusion on which has skills/Mithril. Mitigation = in-app notifications (Silvia). Eugene: low risk currently.
- 🆕 Pricing question: AI Assistant free or paid? Affects failure tolerance. Pedro action: confirm w/ Bertrand.
- Pedro→Silvia: relayed Loni reframe (*"maybe v2 not the correct question, list requirements"*) — same Loni reframe Bertrand reported at P42 hours later. Converging signal.

**EH action:** send Silvia engineering-manager-per-AEM-agent list (Guliz-assigned design POV on AOv2).

---

## May 12 — Cross-cutting Loni reframe (full content AAI-side)

Loni reframe verbatim — *"No, that's not the question. Question is context, and how do we equip our agents with proper context."* Strategic anchor at VP level. Connects EH (Mithril context-reading primitive ask) ↔ AAI (Ian's North Star architecture for AEM agents AOv2). Same axis, two surfaces. Full context in AAI memory; EH-side relevance = context-reading on Mithril is the **visible UI expression** of the strategic context-architecture pivot.

---

## May 22 — EH's role in the distributed-harness model (Ian NorthStar exchange)

Ian Boston's Agentic NorthStar + the May 19-22 thread reshape how EH should be positioned. Full AAI-side record in `project_aem_agents_intelligence.md` "May 22 — Ian NorthStar thread".

In the distributed-harness model **the UI decides which harness/agent to call** (Ian: explicit/prompted selection, not auto intent-detection), and **cross-surface consistency is vital + PM-led** (Ian: *"an Adobe user feels like it is the same surface regardless of implementation details or UI engineering ownership"*).

**This makes EH (and the agent surfaces) the selection + consistency layer for AEM agents — not just a launchpad.** EH's job grows into: (a) the surface where practitioners select / are prompted toward the right agent (the selection UX Pedro now PM-leads, Ian on record), and (b) the consistency layer that makes distributed, independently-owned agent UIs feel like one Adobe surface (the answer to the 4-chats fragmentation: Experience Workspace / Modernization / Slick / Mithril).

Ties to: EH Priority 1 (Skills+MCP surface), the contribution model, Eugene's per-surface contextual AI Assistant icon, Mithril context-reading (Silvia — context-reading powers good prompted selection), and Pedro's convergence push (now architect-backed). Strategic upgrade to EH's narrative: **EH = the practitioner-facing selection + consistency layer in Adobe's distributed agent architecture.**

---

## Sister project

`project_aem_agents_intelligence.md` — agent reporting platform, AO 2.0 liaison, three-tier reporting, Loni+JM May 11 deck, H-005 resolved, Felix/Rubin/Varun threads, Apoorva punch-list, KR3/4/5/6, AEMEO-9508 Data Advisory Agent overlap watch, Vaishnav PMM signal, broadcast-rep muscle. **+ May 12 Loni reframe + Ian = North Star architect + Ian one-pager deliverable + May 13 Felix/Lara 3-way (External Agent naming, $2K/mo cost data, Mark Pfaff).**
