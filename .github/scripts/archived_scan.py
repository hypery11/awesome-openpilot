#!/usr/bin/env python3
"""Find archived, moved or missing GitHub repositories linked from README.md.

Opens one issue (or updates the existing open one) listing them. Never edits the
README: a maintainer decides whether to remove or annotate each entry.
"""
import json, os, re, subprocess, sys

TITLE = "Link health: archived or missing GitHub repositories"
SKIP_OWNERS = {"orgs", "sponsors", "settings", "marketplace", "topics", "features",
               "apps", "users", "about", "pricing", "login", "search", "collections"}
REPO = os.environ.get("GITHUB_REPOSITORY", "")

def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True)

text = open("README.md", encoding="utf-8").read()
seen, repos = set(), []
for owner, name in re.findall(r"https?://github\.com/([A-Za-z0-9-]+)/([A-Za-z0-9._-]+)", text):
    name = re.sub(r"\.git$", "", name)
    if owner.lower() in SKIP_OWNERS or not name:
        continue
    key = f"{owner}/{name}".lower()
    if key in seen:
        continue
    seen.add(key)
    repos.append(f"{owner}/{name}")

archived, missing, moved, errors = [], [], [], []
for full in repos:
    r = gh("api", f"repos/{full}")
    if r.returncode != 0:
        msg = (r.stderr or r.stdout).strip()
        if "Not Found" in msg or "HTTP 404" in msg or "HTTP 451" in msg:
            missing.append(full)
        else:
            errors.append(f"{full}: {msg.splitlines()[0] if msg else 'unknown error'}")
        continue
    data = json.loads(r.stdout)
    if data.get("archived"):
        archived.append((full, (data.get("pushed_at") or "")[:10]))
    if data.get("full_name", "").lower() != full.lower():
        moved.append((full, data.get("full_name")))

print(f"Checked {len(repos)} repositories: {len(archived)} archived, {len(missing)} missing, "
      f"{len(moved)} moved, {len(errors)} errors")

lines = [f"Weekly scan of the {len(repos)} `github.com/owner/repo` links in `README.md`.",
         "Nothing was removed automatically. For each item, remove the entry from **both** README files, "
         "update the link, or keep it with a note.", ""]
if archived:
    lines += ["### Archived", ""] + [f"- [ ] [{f}](https://github.com/{f}) (last push {p})" for f, p in archived] + [""]
if missing:
    lines += ["### Not found (deleted, private or renamed without redirect)", ""] + [f"- [ ] https://github.com/{f}" for f in missing] + [""]
if moved:
    lines += ["### Moved (link still redirects; update it)", ""] + [f"- [ ] `{a}` → [{b}](https://github.com/{b})" for a, b in moved] + [""]
if errors:
    lines += ["### Could not check (API error, will retry next week)", ""] + [f"- {e}" for e in errors] + [""]
run_url = f"{os.environ.get('GITHUB_SERVER_URL','https://github.com')}/{REPO}/actions/runs/{os.environ.get('GITHUB_RUN_ID','')}"
lines += [f"_Updated by the [Archived repo scan]({run_url}) workflow._"]
body = "\n".join(lines)

summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a", encoding="utf-8") as fh:
        fh.write(body + "\n")

found = gh("issue", "list", "--state", "open", "--search", f'in:title "{TITLE}"',
           "--json", "number,title", "--limit", "20")
if found.returncode != 0:
    print(found.stderr, file=sys.stderr)
    sys.exit(1)
existing = [i for i in json.loads(found.stdout) if i["title"] == TITLE]
problems = archived or missing or moved

if problems:
    if existing:
        num = str(existing[0]["number"])
        r = gh("issue", "edit", num, "--body", body)
        print(f"Updated issue #{num}")
    else:
        r = gh("issue", "create", "--title", TITLE, "--body", body)
        print(r.stdout.strip())
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
        sys.exit(1)
elif existing:
    num = str(existing[0]["number"])
    gh("issue", "close", num, "--comment", f"All {len(repos)} linked repositories are active again. Closing.")
    print(f"Closed issue #{num}: nothing left to fix")
else:
    print("No archived, moved or missing repositories.")
