---
name: html-dashboard-preference
description: When Pedro asks for a dashboard/roadmap/visual, build a self-contained HTML file in the deck palette, not a markdown note.
metadata:
  type: feedback
---

For dashboards / roadmaps / visuals, Pedro wants a **self-contained HTML file** he opens in the browser — NOT a markdown note. 2026-05-27 he rejected a Mermaid-in-markdown roadmap: *"No - i want a nice HTML dashboard, not yet another md file."*

**Why:** markdown dashboards (even with Mermaid) read like notes; he wants something that looks like a real, styled dashboard/roadmap.

**How to apply:** single-file HTML, inline CSS, no external deps/CDN (works offline, no plugins). Deck palette ONLY — white, light grey, dark grey, Adobe red (#FA0F00), black; no green/blue/pink (status = red critical, dark-grey active, light/outline todo, dashed on-hold — never green). `open` it for him after saving. Offer a dynamic/data-bound version as a follow-up. Example shell: `2026/Roadmap Dashboard.html`. Related: [[feedback_pptx_palette]], [[reference_roadmap_dashboard]].
