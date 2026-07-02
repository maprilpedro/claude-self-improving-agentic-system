# Anonymization Does Not Fix Data Residency — Ian Boston's "Stolen Data" Framing

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-01
- **Source**: Ian Boston's Slack response to Pedro, April 1, 2026.
- **Insight**: Anonymization is often suggested as a fix for data compliance in AI measurement pipelines. It is not. As long as a prompt is readable, it remains customer data — and data residency obligations follow the data, not its identifiability. To anonymize to the point where it is no longer customer data, you must transform it to the point it loses all evaluation value. Ian's framing: if you can no longer identify the customer from the data, you have effectively stolen it — it becomes Adobe data, and you can no longer delete it when the customer terminates (breaking data lifecycle requirements).
- **The one loophole**: Classify prompts as operational data. This permits centralization, but restricts use to maintaining service uptime only. You cannot use operational data to evaluate or improve the service — which makes it useless for agent measurement and reporting.
- **Ian's meta-point**: The PLAs from end of 2025 may not have been fully signed off. His preference is to fix the problem quietly before it surfaces to legal. If legal gets involved and the problem is confirmed: stop immediately, fix, and potentially do more remediation.
- **Application**: When someone proposes anonymization as a compliance fix for cross-region AI data, ask two questions: (1) Is the data still readable as a prompt? If yes, it's still customer data. (2) Does the residency obligation apply to where data is processed, not just stored? If yes, anonymization changes nothing about geography.
