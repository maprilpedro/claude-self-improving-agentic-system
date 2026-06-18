---
name: cli-anything-harness-generator
description: CLI-Anything (HKUDS) — the harness GENERATOR. Reach for it to wrap an internal tool / API / codebase as a token-efficient agent-native CLI + SKILL.md. Saved for harness creation only.
metadata:
  type: reference
---

**CLI-Anything** (`github.com/HKUDS/CLI-Anything`, Apache-2.0). Saved 2026-06-18 for **one capability: harness generation.** Ignore its CLI-Hub registry (mostly creative-desktop tools — GIMP/Blender/CAD/video — not Pedro's world).

**The generator (the reason to keep it).** A Claude Code plugin that builds an agent-native CLI for any software, codebase, or internal tool in a 7-phase pipeline: analyze source / map GUI actions to APIs → design command groups + state + output → implement a **Click (Python) CLI** with REPL + JSON output + undo/redo → plan tests → write tests → document → publish (`setup.py`, installs to PATH). **Each generated CLI ships a `SKILL.md`** (AI-discoverable → fits the [[feedback_session_setup]]/skillshare workflow). `/cli-anything:refine <path> "<focus>"` does incremental, non-destructive gap-filling.

**Install:** `/plugin marketplace add HKUDS/CLI-Anything` → `/plugin install cli-anything`. Then `/cli-anything <software-path-or-repo>`.

**When to reach for it (Pedro):** when he wants to turn an internal tool / API / codebase into a token-efficient CLI + skill instead of hand-driving it (the reporting lane is the likeliest case — wrap a data source as a CLI). Same family as the RTK token-efficiency ethos [[reference_cli_binaries]].

**Caveats:** Python/Click toolchain (eng-exec, [[user_ui_cx_gap]] — Sorin/Eng territory for build+maintain). **For any Adobe-internal tool: the auth/security line applies** — clearance before pointing the generator at an internal surface or storing its tokens. The community registry has a track record of security patches (token/path-traversal/injection) → don't install random community harnesses on a machine with Adobe creds; the generator on a tool Pedro controls is the clean use.
