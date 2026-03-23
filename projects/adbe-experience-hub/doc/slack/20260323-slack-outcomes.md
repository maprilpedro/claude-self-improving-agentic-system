---
title: "#aem-home-core-team Slack — Key Outcomes & Analysis"
date: 2026-03-23
sources: AEM-HOME-CORE-TEAM.md + AEM-HOME-CORE-TEAM-nov2025-march-23.md
coverage: September 2024 — March 2026
---

# #aem-home-core-team Slack — Key Outcomes

## Coverage

September 2024 to March 2026. Spans MVP design, alpha program, GA launch, post-GA experimentation, and current state.

---

## Loni Signals (VP PM for AEM)

- **May 28, 2025**: Asked for a specific August GA date. Not "summer." A specific date.
- **May 29, 2025**: "What is our plan to redirect users (not if they use deep-linked bookmarks) to Experience Hub?" No clear answer on file.
- **Aug 16, 2025**: "Great to see Sites Optimizer connected into Experience Hub — I was just thinking and wondering about this last evening. Good we are trying to look at in-product nudge for PLG."
- **Oct 13, 2025**: Flagged preset defaults in A/B testing discussion: "I see the default was Asset Librarian. It should still be CA, no?" She is watching closely.

---

## Bertrand Decisions You Inherited

- **Nov 28, 2024**: Gave detailed 4-point critique of the alpha build: UI broken, environment links broken, no functional area shortcuts, compact display issues.
- **Dec 17, 2024**: Pushed Roles → Intentions shift. Navigation labels moved from role names (Content Author, Developer, Security Admin) to intentions (Authoring content, Building experiences, Writing code, Security). Shankari confirmed. Reference wiki: Launchpad Intent vs Role Matrix.
- **Feb 2025**: Pressed again on the same direction ("I've tried to bring this up a few times pre-summit"). Eventually resolved.
- **Apr 30, 2025**: Suggested ContentHub as a new top-level intention beyond the 3 core personas.
- **No date (Sites Trials context)**: "For users that only have a single program/env available to them: does it make sense to display the switcher at all?" Open design question, no answer on file.

---

## Your Prior Fingerprints

- **Aug 2025 (post-GA)**: Mihai confirmed that Security widget at top for Security & Dev persona was previously agreed with you (@pedrofer) and @adulvac.
- Shankari disagreed: "Security Admin is not our largest and most important persona. Which is incorrect on both counts."
- Mihai proposed a compromise layout for that persona specifically.
- Status: **Unresolved.**

---

## Burning Problems

### 1. Value proposition not clear to users
**Sep 25, 2025** — Shankari's own diagnosis: "The value of Experience Hub is not presented upfront to users." She proposed an onboarding video inside the product. No implementation on file.

### 2. Navigation confusion / multiple entry points
**May 29, 2025** — Loni asked for a redirect plan. No answer.
**May 2025** — Customer Mark Schulz: "I keep getting to Experience Hub via Experience Home and wonder why I need both?"
**Nov 2025** — Sorin flagged left nav structure as post-Summit open question: "There are concerns about lack of structure and categories seeming random."
Status: **Unresolved.**

### 3. Environments widget invisible to new users
**Sep 17, 2025** — Sorin identified the root cause: environments only appear after a user logs in at least once (local user must be created first). Bertrand flagged as critical: "We're going to miss big time on the whole point of the widget."
Status: **Unresolved.**

### 4. Recents widget inaccurate
**May 2025** — Customer Mark Schulz: "Recents widget needs some love. It's not accurate."
Status: **Unresolved.**

### 5. Security & Compliance not discoverable — now a live customer bug
**Sep 10-15, 2025** — Bertrand and Andrei Dulvac flagged as UX issue: role switcher confusing, no nav path to security even for asset librarians.
**Feb 11, 2026** — Customer @geco cannot see "Security and Compliance" section in Experience Manager. Missing: Penetration Tests. Andrei flagged alongside it. This is no longer just a UX concern — it is a live customer-impacting production issue.
Status: **Unresolved. Escalated to customer-impacting.**

### 6. Left nav structure open
**Nov 2025** — Sorin explicitly flagged as post-Summit open question. No agreed direction for how to accommodate new services wanting to add features.
Status: **Unresolved.**

### 7. Role switcher — single environment users
**No date (Sites Trials context)** — Bertrand raised whether showing the switcher at all makes sense for users with a single program/env. No answer on file.
Status: **Open question.**

### 8. Bounce rate analytics accuracy
**Sep 5, 2025** — Bounce rate with click filter "looks fishy." Under investigation. No resolution on file.
Status: **Unresolved.**

### 9. Trial environment conflict
**Jan 24, 2025** — Bruce Lefebvre: enabling Experience Hub for specific orgs broke the Headless Trial experience. Status unclear — may have been resolved quietly. Worth confirming with Sorin.
Status: **Unknown.**

---

## What's Working

- **Nov 2025** — SIMPLE onboarding variant won A/B test decisively: 17.9% CTR vs 0.36% for "with selection" variant. Anastasia proposed rolling to 100% with code cleanup on the losing variant. Authoring environments simple variant already at 100%.
- **Aug 26, 2025** — GA launched on time per Loni's request.
- **Dec 2024** — Alpha program reached 35 users across 17 external customer tenants including Real Madrid, Volkswagen, Accenture, Best Buy, Brightline Trains, Capgemini, Cox Communications, ESRI, Henkel, IPG Health, Merkle, Netcentric, T. Rowe Price, Valtech and others.
- **Dec 17, 2024** — Roles → Intentions strategic direction confirmed and aligned.

---

## Key People Active in This Channel

| Person | Role | Notable Contributions |
|---|---|---|
| Shankari Panchapakesan | PM (outgoing) | MVP scope, GA, analytics, A/B testing |
| Sorin Slavic | Lead Engineer | Deployments, feature flags, auth routing, alpha feedback |
| Mihai Bradoschi | Engineer | Widget layout, UX feedback, GA prep |
| Anastasia Pintilie | Engineer | Recents, widget layout proposals, A/B testing execution |
| Eugene Bannykh | UX Designer | Dark theme bugs, button styling, announcement widget |
| Bertrand de Coatpont | Sr Director PM (Pedro's boss) | Strategic direction, Roles→Intentions, alpha critique |
| Andrei Dulvac (@adulvac) | Stakeholder | Role switcher UX feedback, security discoverability, agreed Security widget placement with Pedro |
| Loni | VP PM AEM | GA date, redirect plan, PLG signal, preset defaults |
| Mark Schulz | Customer (partner) | Most detailed external feedback on record |
| Bruce Lefebvre | Internal | Headless Trial conflict |

---

## Post-Summit Agenda (based on open items, priority order)

1. **Value proposition** — articulate and surface it upfront (Shankari diagnosed Sep 2025)
2. **Navigation simplification** — left nav structure and multiple entry point confusion (Sorin + Loni)
3. **Redirect plan for legacy entry points** — Loni asked May 2025, still no answer
4. **Environments widget for first-time users** — Bertrand flagged as critical (Sep 2025)
5. **Security & Compliance discoverability** — now customer-impacting, @geco Feb 2026
6. **Role switcher for single-env users** — Bertrand open question (Sites Trials context)
7. **Recents widget accuracy** — customer feedback May 2025
8. **Analytics cleanup** — bounce rate accuracy Sep 2025
9. **Confirm trial environment conflict status** with Sorin
