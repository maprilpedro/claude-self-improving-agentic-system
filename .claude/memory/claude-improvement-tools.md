---
name: Claude Code improvement tools and extensions
description: Recommended MCP servers, skills, editor extensions, and architecture improvements for the PM knowledge system
type: reference
---

## MCP Servers to Add

| MCP Server | Why |
|---|---|
| Obsidian MCP | 30-60-90 plan and Experience Hub notes live in Obsidian. Closes the loop between knowledge/ and working notes. |
| Linear / Jira MCP | If Adobe uses either for tracking. Pull ticket context directly. |
| Notion MCP | Only if the team uses it. |
| GitHub MCP | Richer PR/issue context for agents reviewing or creating PRs. |

## Already Connected MCP Servers

Slack, Telegram, Gmail, Google Calendar, Google Drive, Drafts

## High-Value Existing Skills

- `recap_as_dpm` for ingesting articles into knowledge/
- `pptx` for building decks (pairs with Rule of Three, Aristotle's Five-Point Plan patterns)
- `learn-feynman` and `learn-quiz` for stress-testing understanding of new domains

## Skills to Build

- **Knowledge ingestion skill** that takes any input (URL, PDF, pasted text) and runs the full learning protocol: read, extract, update knowledge/, git commit
- **Stakeholder brief generator** that pulls from projects/adbe-experience-hub/context/ and knowledge/domain/ to draft comms for specific audiences

## Editor Extensions (VS Code)

- Markdown All in One for better knowledge file editing
- Foam or Dendron for wiki-style linking between knowledge files
- GitLens for tracking when knowledge entries were added

## Architecture Improvement

Build a custom MCP server wrapping knowledge/ with tools like:
- `search_knowledge(query)` for semantic search across all knowledge files
- `get_patterns_for(situation)` to return relevant patterns for a PM scenario
- `check_hypotheses()` to return active hypotheses and status
- `ingest_learning(source, content)` to auto-route learnings to the right files

This turns knowledge/ from "files Claude reads" into "a service Claude queries."

## What Not to Add

- No package managers. Markdown + git is the right stack.
- No database. Git is the database.
- No CI/CD. Auto-commit rule in CLAUDE.md is enough.
- No static site generator. That's scope creep.
