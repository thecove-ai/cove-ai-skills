# Cove AI Skills

Claude skills built by The Cove for car rental content work. Each folder is one skill, with its instructions in `SKILL.md`.

| Skill | What it does |
|---|---|
| `content-machine` | Writes, fixes and adapts FAQs and help copy to house style for each audience: consumer (including motorhomes and leasing), travel agent, My Account, chatbot and support replies. Checks new FAQs against the live set for duplicates. |
| `cove-translation-sheets` | Translates, audits and fixes car rental content across 14 locales (en-GB, de-DE, es-ES, es-MX, fr-FR, pt-PT, pt-BR, it-IT, da-DK, nl-NL, nb-NO, pl-PL, fi-FI, sv-SE). Includes the glossary, native-speaker corrections and an automated check script. |

## Install a skill

**Claude app (web, desktop, Cowork)**

1. Download the skill's folder (e.g. `cove-translation-sheets`) and zip it, so the zip contains the folder with `SKILL.md` inside.
2. In Claude, go to Customize > Skills and choose Upload skill.
3. To update later, delete the old version and upload the new zip.

**Claude Code**

Copy the skill folder into `~/.claude/skills/`, so you end up with `~/.claude/skills/cove-translation-sheets/SKILL.md`.

## Changes

Skills change Claude's instructions for everyone who installs them, so changes come from one place: the maintainer's synced copy of this repo. A background sync pushes updates to `main` shortly after they are made, refuses anything that looks like an internal file ID or company email address, and builds a fresh zip for each skill that changed. If you want a change, open an issue or a pull request rather than editing `main` directly.
