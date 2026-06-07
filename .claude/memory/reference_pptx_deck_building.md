---
name: reference_pptx_deck_building
description: How decks get built in this setup — pptx skill pipeline, Adobe Clean template source, HTML→PNG for diagrams/tables, local QR, and the PowerPoint-overwrite gotcha.
metadata:
  type: reference
---

Reusable toolchain for building Adobe-branded PPTX decks (established building the Bucharest keynote, 2026-06-06/07).

**Template source (Adobe Clean branding).** `~/Downloads/20250130 - Improvements for Release Management.pptx` = a real Pedro deck on the Adobe master. Theme: fonts **Adobe Clean Black** (titles) + **Adobe Clean** (body); palette **Adobe red `EB1000`**, black, white, greys `2C2C2C`/`5F5F5F`/`919191`, `F5F5F5`. Layout grammar: left red vertical bar + Adobe logo bottom-left on every slide; title slide, red-panel agenda, big-title section dividers (slideLayout5). The skill's `pack.py --original <template>` preserves master/theme/logo.

**Pipeline (pptx skill).** unpack → edit slide XML / reorder `<p:sldIdLst>` → `clean.py` → `pack.py`. Add slides by duplicating a divider with `add_slide.py` (it writes the file + rel but does NOT insert into `sldIdLst` — do that by hand). Content slides built by overwriting the dup's spTree (header text box + body/pic). QA = `soffice → pdf → pdftoppm → jpg`, inspect, fix, re-render.

**Tools installed this session (macOS):** **LibreOffice** (`brew install --cask libreoffice`) for pptx→pdf render/QA; **segno** (`pip install segno`) for QR codes generated **locally** (don't send internal wiki URLs to an external QR service); **Chrome headless** (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless --screenshot`) to render HTML diagrams/tables → PNG.

**Diagrams & dense tables → build in HTML, render to PNG, embed.** Native pptx tables are painful; an HTML table/diagram (deck palette, monospace for the harness diagrams) rendered via Chrome at `--force-device-scale-factor=2` gives a clean image. Size the Chrome `--window-size` height to the content or you get whitespace padding. Convert `.webp` source images to PNG (`sips -s format png`) — PowerPoint handles webp poorly.

**🔴 Gotcha — close the deck before writing.** If the .pptx is open in PowerPoint while you overwrite it on disk, PowerPoint autosaves its cached copy back over your edits (and can leave a 294KB stub / "not a valid Office file"). Always `lsof` the file before `cp`; if a handle is held, ask Pedro to quit PowerPoint, then write. Also: when Pedro edits in PowerPoint, **re-unpack from disk** before the next change — PowerPoint renumbers `slideN.xml` files and media (`imageNN.png`) on save, so cached working dirs go stale.

See [[reference_pptx_template]] (the H2'26 planning-deck template, separate use) and [[feedback_html_dashboard_preference]] (HTML for dashboards).
