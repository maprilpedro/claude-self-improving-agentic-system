---
name: PPTX template — H2'26 AEM & Agentic Web Planning
description: Always use this Pedro-curated deck as the template reference when building AEM PM pptx output. Contains current Adobe corporate styling, AEM-specific layouts, and recent slide masters that match what leadership reviews.
type: reference
originSessionId: c3970bb1-0fc5-47cd-80ee-cd157b1b93c6
---
**Path:** `/Users/pedrofer/Downloads/[Internal] - H2'26 AEM & Agentic Web Planning.pptx`

**Why use this:** Pedro confirmed 2026-05-05 — "always use this as a template reference." Replaces the older `Adobe Experience Manager _TEMPLATE.pptx` from OneDrive Templates folder. This deck (110 slides, 22.1 MB, 12 masters) is the current AEM corporate template Pedro and leadership work from.

**Default layouts to use when generating slides:**
- `[6] Content Slide` — primary content layout (TITLE + OBJECT placeholders). Use this for tables, wireframes, body content.
- `[7] Content Slide [Dark]` — dark variant.
- `[2] Section Divider [White-A]` or `[3] 1_Section Divider [White-B]` — for section openers.
- `[18] White - Bottom Graphic` — alternate content layout matching mid-deck reference slides.

**Slide dimensions:** 13.33" × 7.50" (16:9 widescreen, EMU 12188825 × 6858000).

**Build pattern (python-pptx):**
```python
from pptx import Presentation
from pptx.oxml.ns import qn
prs = Presentation("/Users/pedrofer/Downloads/[Internal] - H2'26 AEM & Agentic Web Planning.pptx")
# Strip sample slides
sldIdLst = prs.slides._sldIdLst
for sldId in list(sldIdLst):
    rId = sldId.get(qn("r:id"))
    prs.part.drop_rel(rId)
    sldIdLst.remove(sldId)
content_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(content_layout)
```

**Reference build script:** `/tmp/build_aov2_deck.py` — last run 2026-05-05 for AOv2 May 11 deck section. Uses Adobe Clean font, Adobe red (`#EB1000`), DARK (`#1A1A1A`), GRAY (`#6E6E6E`).

**Output destination convention:** vault deck folders, e.g. `2026/AEM Agents Intelligence/AAI - Project Folder/Loni JM May 11 deck/`.
