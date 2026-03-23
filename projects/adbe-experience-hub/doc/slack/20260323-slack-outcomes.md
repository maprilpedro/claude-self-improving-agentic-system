---
title: "#aem-home-core-team Slack — Key Outcomes & Analysis"
date: 2026-03-23
source: AEM-HOME-CORE-TEAM.md (Slack export)
coverage: September 2024 — November 2025
---

# #aem-home-core-team Slack — Key Outcomes

## Coverage

September 2024 to November 2025. 14 months spanning MVP design, alpha program, GA launch, and post-GA experimentation.

---

## Loni Signals (VP PM for AEM)

- **Aug 16, 2025**: "Great to see Sites Optimizer connected into Experience Hub — I was just thinking and wondering about this last evening. Good we are trying to look at in-product nudge for PLG."
- **May 28, 2025**: Asked for a specific August GA date. Not "summer." A specific date.
- **May 29, 2025**: "What is our plan to redirect users (not if they use deep-linked bookmarks) to Experience Hub?" No clear answer on file.
- **Oct 13, 2025**: Flagged preset defaults in A/B testing discussion: "I see the default was Asset Librarian. It should still be CA, no?" She is watching closely.

---

## Bertrand Decisions You Inherited

- **Dec 17, 2024**: Pushed the Roles → Intentions shift. Navigation labels moved from role names (Content Author, Developer, Security Admin) to intentions (Authoring content, Building experiences, Writing code, Security). Shankari confirmed. Reference wiki: Launchpad Intent vs Role Matrix.
- **Feb 2025**: Pressed again on the same direction ("I've tried to bring this up a few times pre-summit"). Eventually resolved.
- **Apr 30, 2025**: Suggested ContentHub as a new top-level intention beyond the 3 core personas.
- **Nov 28, 2024**: Gave detailed 4-point critique of the alpha build: UI broken, links broken, no functional area shortcuts, compact display issues.

---

## Your Prior Fingerprints

- **Aug 2025 (post-GA)**: Mihai confirmed that Security widget at top for Security & Dev persona was previously agreed with you (@pedrofer) and @adulvac.
- Shankari disagreed: "Security Admin is not our largest and most important persona. Which is incorrect on both counts."
- Mihai proposed a compromise layout for that persona specifically.
- Status: **Unresolved.**

---

## Burning Problems (all post-GA unless noted)

### 1. Value proposition not clear to users
**Sep 25, 2025** — Shankari's own diagnosis: "The value of Experience Hub is not presented upfront to users." She proposed an onboarding video inside the product. No implementation on file.

### 2. Navigation confusion / multiple entry points
**May 29, 2025** — Loni asked for a redirect plan. No answer.
**May 2025** — Customer Mark Schulz: "I keep getting to Experience Hub via Experience Home and wonder why I need both?"
**Nov 2025** — Sorin flagged left nav structure as a post-Summit open question: "There are concerns about lack of structure and categories seeming random."
Status: **Unresolved.**

### 3. Environments widget invisible to new users
**Sep 17, 2025** — Sorin identified the auth routing root cause: environments only appear after a user logs in at least once (local user must be created first). Bertrand flagged as critical: "We're going to miss big time on the whole point of the widget." A wayfinding widget that doesn't work for first-time users defeats its purpose.
Status: **Unresolved.**

### 4. Recents widget inaccurate
**May 2025** — Customer Mark Schulz: "Recents widget needs some love. It's not accurate."
Status: **Unresolved.**

### 5. Security & Compliance not discoverable
**Sep 10-15, 2025** — Bertrand: "People sometimes find the role switcher confusing. Not having a nav path to find security stuff even for asset librarians is weird." Proposed fix: add a "Services" section (like engineering did). No confirmed decision.
Status: **Unresolved.**

### 6. Left nav structure open
**Nov 2025** — Sorin explicitly flagged this as a post-Summit open question. No agreed direction for how to accommodate new services wanting to add features.
Status: **Unresolved.**

### 7. Bounce rate analytics accuracy
**Sep 5, 2025** — Bounce rate with click filter applied "looks fishy." Under investigation. No resolution on file.
Status: **Unresolved.**

### 8. Trial environment conflict
**Jan 24, 2025** — Bruce Lefebvre: enabling Experience Hub for specific orgs broke the Headless Trial experience. "This makes it difficult to debug trials issues." Status unclear — may have been resolved quietly. Worth checking with Sorin.
Status: **Unknown.**

---

## What's Working

- **Nov 2025** — SIMPLE onboarding variant won A/B test decisively: 17.9% CTR vs 0.36% for the "with selection" variant. Rolled to 100%. Code cleanup on losing variant.
- **Aug 26, 2025** — GA launched on time per Loni's request for a specific August date.
- **Dec 2024** — Alpha program reached 35 users across 17 external customer tenants: Real Madrid, Volkswagen, Accenture, Best Buy, Brightline Trains, Capgemini, Cox Communications, ESRI, Henkel, IPG Health, Merkle, Netcentric, Ping Identity, T. Rowe Price, Valtech and others.
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
| Bertrand de Coatpont | Sr Director PM | Strategic direction, Roles→Intentions, alpha critique |
| Loni | VP PM AEM | GA date, redirect plan, PLG signal, preset defaults |
| Mark Schulz | Customer (partner) | Most detailed external feedback on record |
| Bruce Lefebvre | Internal | Headless Trial conflict |

---

## Post-Summit Agenda (based on open items)

In priority order based on severity and leadership visibility:

1. Articulate and surface the value proposition (Shankari already diagnosed this)
2. Navigation simplification — resolve left nav structure and entry point confusion
3. Redirect plan for legacy entry points (Loni asked for this in May 2025)
4. Fix environments widget for first-time users (Bertrand flagged as critical)
5. Recents widget accuracy
6. Security & Compliance discoverability
7. Analytics cleanup (bounce rate)
8. Confirm trial environment conflict status with Sorin
