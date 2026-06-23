---
name: feedback-vault-copy-of-published-pages
description: "Always keep a vault copy of any Confluence/wiki page published for Pedro — standing preference."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 17c67daf-e9c0-4126-adee-75e89cfcff7d
---

**Whenever a Confluence/wiki page is created or published for Pedro, also save a copy as a vault note.** Standing preference, Pedro 2026-06-23: *"toujours une copie vault stp."*

**Why:** the vault is his source of truth + offline/search surface; Confluence is the published artifact. Keeping both means he can edit/recall locally and the record survives independent of the wiki. Matches the existing pattern (the 06-18 working-session page had a vault twin).

**How to apply:**
- After publishing to Confluence, write a markdown twin under the owning project folder (e.g. `AAI - Project Folder/`).
- Put the wiki URL in the note frontmatter (`wiki:` field) and a one-line banner ("Vault copy of the published wiki page [id]").
- Mirror the content; carry over any honesty flags / open-to-confirm items (e.g. unresolved names).
- Do NOT run `obsidian reload` after writing (see [[feedback-obsidian-reload-after-write]]).
- Vault notes live outside the repo, so they are not committed — OneDrive/Obsidian sync carries them.
