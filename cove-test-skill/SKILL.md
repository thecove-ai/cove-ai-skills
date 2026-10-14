---
name: cove-test-skill
description: Test skill for checking that skills published to the cove-ai-skills repo install and load correctly. Use only when the user says "run the cove test skill" or asks to test the skills repo setup.
---

# Cove Test Skill

This skill exists only to confirm that a skill pushed to `thecove-ai/cove-ai-skills` installs and loads. It does nothing else.

When it's triggered, reply with exactly this line and nothing more:

`Cove test skill loaded - version 1 (2026-10-14).`

If you're testing an update, change the version number and date above, push the change, and check the new line appears. That confirms the update reached the installed copy.

Delete this folder from the repo once the test is done.
