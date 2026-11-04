# Cove AI Skills

Claude skills built by The Cove for car rental content work. Each folder is one skill, with its instructions in `SKILL.md`.

| Skill | What it does |
|---|---|
| `content-machine` | Writes, fixes and adapts FAQs and help copy to house style for each audience: consumer (including motorhomes and leasing), travel agent, My Account, chatbot and support replies. Checks new FAQs against the live set for duplicates. |
| `cove-translation-sheets` | Translates, audits and fixes car rental content across 14 locales (en-GB, de-DE, es-ES, es-MX, fr-FR, pt-PT, pt-BR, it-IT, da-DK, nl-NL, nb-NO, pl-PL, fi-FI, sv-SE). Includes the glossary, native-speaker corrections and an automated check script. |
| `cove-skills-updater` | Checks this repo for new or updated skills and offers each one for you to install with one click. |

## Get the skills (Claude app, desktop and Cowork)

**First time**

1. Download [cove-skills-updater.zip](https://github.com/thecove-ai/cove-ai-skills/releases/latest/download/cove-skills-updater.zip).
2. In Claude, go to Customize > Skills and choose Upload skill.
3. In a new chat, ask Claude to **"check for new Cove skills"**. It lists every published skill and shows a Save card for each one. Click Save on the ones you want.

**Staying up to date**

- Ask Claude to "check for new Cove skills" whenever you like, or ask it to set up a weekly scheduled task that does the check for you. New and updated skills wait for your click; nothing installs on its own.
- To get an email when something new is published, click **Watch > Custom > Releases** at the top of this repo.
- You can also download any skill directly. These links always point at the newest version:
  - [content-machine.zip](https://github.com/thecove-ai/cove-ai-skills/releases/latest/download/content-machine.zip)
  - [cove-translation-sheets.zip](https://github.com/thecove-ai/cove-ai-skills/releases/latest/download/cove-translation-sheets.zip)

To update by hand: delete the old version in Customize > Skills, then upload the new zip.

**For organization admins:** on a Team or Enterprise plan, an owner can add a skill once for everyone in the organization from the organization's skill settings, instead of each person uploading it.

## Claude Code

```
npx skills add thecove-ai/cove-ai-skills -g -a claude-code -s '*' -y
```

Run the same command again (or on a schedule) to pick up new skills and updates. It needs Node 22.20 or later. Set `DISABLE_TELEMETRY=1` if you don't want the CLI to send anonymous usage data.

## How publishing works

1. The maintainer pushes a change to a skill folder on `main`. The commit message becomes the release note, so describe the change.
2. The **Publish skills** workflow (`.github/workflows/publish-skills.yml`) runs on every push to `main`. It:
   - adds a version to the end of each skill's description, e.g. `(v2026-11-04-ab12c34)`, taken from the last commit that touched the skill
   - zips each skill
   - publishes the versioned copies and `catalog.json` to the `dist` branch, which `cove-skills-updater` reads
   - creates a GitHub Release with every zip attached, if any skill is new or changed
3. Folders listed in `.skillsignore` are never published.

Skills change Claude's instructions for everyone who installs them. Changes to `main` are made by the maintainer only; if you want a change, open an issue or a pull request.
