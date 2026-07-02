# Two-Validator Pattern for Report Rollout

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-09
- **Source**: Jim Stoklosa / Corey Dulimba dynamic, AEM Experience Production Agent reports.
- **Insight**: When an agent report is prepared by someone other than the PM owner (e.g. Jim prepares for Corey), two separate validation roles exist: (1) the preparer validates data accuracy and feature behavior — they know the data; (2) the PM owner validates as sign-off — they need to have seen it before it goes to leadership. These are different asks with different depths. Conflating them into one message to one person either over-asks the owner or under-validates the data.
- **Pattern**: Send detailed validation ask to preparer first. Once clean, send a lighter "does this look right to you?" to the PM owner. The owner's sign-off is what makes the visibility path credible — Bertrand won't show Loni a report the PM owner hasn't seen.
- **Application**: Map preparer vs owner for every agent report before sending any validation request.
