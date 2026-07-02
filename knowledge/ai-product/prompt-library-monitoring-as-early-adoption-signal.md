# Prompt Library Monitoring as Early Adoption Signal

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-16 + 2026-04-10
- **Source**: March 16 Agent Owner Alignment (Shankari + Bertrand prompt library discussion). State of Project (Apoorva's prompt management). H2 Prelim Part 3 April 10 (Loni's closing praise for Apoorva).
- **Insight**: Daily monitoring of which prompts are actually being triggered is one of the earliest adoption signals available. It tells you what users are trying to do, not what you told them they could do. For a PM who owns an agent, the two things to track daily are: (1) which of my prompts are being used and (2) which new prompts are users writing that I didn't anticipate.
- **Apoorva's approach**: She monitors the Discovery agent's prompt usage daily and tracks repeating users. She is one of the only agent PMs doing this as of April 2026. Loni explicitly praised this behavior.
- **Prompt library ownership model**: Prompt library is cross-product (AP team owns the platform). AEM-specific prompts are each agent team's responsibility — test, preview, add, remove. This is not optional. Prompts that go unmanaged drift out of alignment with what the agent can actually do, which directly fuels the trigger failure problem.
- **Application**: Any agent PM should have a daily 5-minute prompt review routine. What got used? What got ignored? What did users ask for that isn't in the library? This is faster signal than any weekly report.
