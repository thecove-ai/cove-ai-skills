#!/usr/bin/env python3
"""Build the published copy of every skill in this repo.

For each top-level folder that contains a SKILL.md (minus anything listed in .skillsignore):
  - work out a version from the last commit that touched the folder: v<YYYY-MM-DD>-<short sha>
  - copy the folder and append " (v...)" to the end of the SKILL.md description, so anyone can
    see which version they have installed from the description Claude shows
  - zip it (the zip holds the folder, ready for Customize > Skills > Upload skill)

Writes to OUT_DIR:
  catalog.json             what the cove-skills-updater skill reads
  skills/<name>/...        the stamped skill folders
  zips/<name>.zip          one zip per skill
  notes.md                 release notes (only the skills that changed)
  changed.txt              "true" or "false"

Usage: publish_skills.py OUT_DIR PREVIOUS_CATALOG_JSON
Needs: git history (fetch-depth: 0), PyYAML.
"""
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

import yaml

REPO = os.environ.get("GITHUB_REPOSITORY", "thecove-ai/cove-ai-skills")
DIST_BRANCH = "dist"
VERSION_SUFFIX = re.compile(r"\s*\(v\d{4}-\d{2}-\d{2}-[0-9a-f]+\)\s*$")


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout.strip()


def ignored():
    if not os.path.exists(".skillsignore"):
        return set()
    with open(".skillsignore") as f:
        return {l.strip().strip("/") for l in f if l.strip() and not l.startswith("#")}


def split_skill(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("SKILL.md has no frontmatter")
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def main(out_dir, previous_path):
    skip = ignored()
    names = sorted(
        d for d in os.listdir(".")
        if os.path.isdir(d) and not d.startswith(".") and d not in skip
        and os.path.isfile(os.path.join(d, "SKILL.md"))
    )
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(os.path.join(out_dir, "zips"))

    try:
        with open(previous_path) as f:
            previous = {s["name"]: s for s in json.load(f).get("skills", [])}
    except (OSError, ValueError):
        previous = {}

    skills, changed = [], []
    for name in names:
        date = git("log", "-1", "--format=%cs", "--", name)
        sha = git("log", "-1", "--format=%h", "--", name)
        note = git("log", "-1", "--format=%s", "--", name)
        version = f"v{date}-{sha}"

        meta, body = split_skill(open(os.path.join(name, "SKILL.md"), encoding="utf-8").read())
        if meta.get("name") != name:
            raise SystemExit(f"{name}/SKILL.md: frontmatter name '{meta.get('name')}' must match the folder name")
        description = VERSION_SUFFIX.sub("", str(meta.get("description", "")).strip())
        stamped = f"{description} ({version})"
        if len(stamped) > 1024:
            raise SystemExit(f"{name}: description is over 1024 characters once the version is added")
        meta["description"] = stamped

        dest = os.path.join(out_dir, "skills", name)
        shutil.copytree(name, dest, ignore=shutil.ignore_patterns(".DS_Store"))
        front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10000).strip()
        with open(os.path.join(dest, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(f"---\n{front}\n---\n{body}")

        zpath = os.path.join(out_dir, "zips", f"{name}.zip")
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            for root, _, files in os.walk(dest):
                for fn in sorted(files):
                    full = os.path.join(root, fn)
                    z.write(full, os.path.relpath(full, os.path.join(out_dir, "skills")))

        entry = {
            "name": name,
            "version": version,
            "updated": date,
            "change": note,
            "description": description,
            "skill_md_url": f"https://raw.githubusercontent.com/{REPO}/{DIST_BRANCH}/skills/{name}/SKILL.md",
            "zip_url": f"https://github.com/{REPO}/releases/latest/download/{name}.zip",
        }
        skills.append(entry)
        old = previous.get(name)
        if not old:
            changed.append(("New", entry))
        elif old.get("version") != version:
            changed.append(("Updated", entry))

    removed = sorted(set(previous) - set(names))
    catalog = {
        "repo": REPO,
        "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "skills": skills,
    }
    with open(os.path.join(out_dir, "catalog.json"), "w") as f:
        json.dump(catalog, f, indent=2)

    lines = ["Skills in this release:", ""]
    for kind, e in changed:
        lines.append(f"- **{e['name']}** ({kind.lower()}, {e['version']}): {e['change']}")
    for r in removed:
        lines.append(f"- **{r}** removed")
    lines += ["", "Get them: ask Claude to \"check for new Cove skills\" (cove-skills-updater), "
              "or download the zips below and upload them in Claude under Customize > Skills."]
    with open(os.path.join(out_dir, "notes.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(out_dir, "changed.txt"), "w") as f:
        f.write("true" if (changed or removed) else "false")

    print(f"{len(skills)} skill(s) built; changed: {[e['name'] for _, e in changed]}; removed: {removed}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
