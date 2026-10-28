---
name: feedback-diagram-layout
description: Trees and maps in the vault are drawn left to right like his own sketches, ordered, with short labels. A radial mindmap with long labels confused him (2026-10-28).
metadata:
  type: feedback
---

When Pedro's tree or map goes into the vault, draw it **left to right, root on the left, branches in his order top to bottom, leaves of 3 to 6 words**, and colour only what carries meaning (yellow = Doing on the Coworker tree). Detail stays in the source (Kanban card, Status), not in the box.

**Why:** 2026-10-28, his Coworker priorities tree first went in as a Mermaid `mindmap`: radial, branch 1 on the right and branch 3 on the left, leaves of 15 words. Pedro: "un autre affichage que ça ? C'est confus". The same content as a Mermaid `flowchart LR` with short labels matched his iPad sketch and read at a glance. His sketches are left-to-right trees, and order is part of the content (Adoption first).

**How to apply:**
- Mermaid in Obsidian: `flowchart LR`, not `mindmap`. Avoid parentheses inside node text.
- Put the diagram where he lands: at the top of the note, not under banners. Then check the render yourself (`obsidian dev:screenshot` in reading view, move the image out of the vault) before telling him it works.
- Two homes for the same items (tree + Kanban) drift: note which one is the source and update the other in the same step. See [[project_aem_agents_intelligence]] 2026-10-28 priorities block.
