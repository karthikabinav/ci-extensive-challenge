"""
Automatic issue labeling script.

Labels new issues by keyword:
  - label "bug" if the issue contains "error"
  - label "feature" if the issue contains "add"

Usage:
  export GITHUB_TOKEN=<personal_access_token>
  export GITHUB_REPOSITORY=owner/repo
  python scripts/label_issues.py
"""

import json
import os
import sys
import urllib.request

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("GITHUB_REPOSITORY")
API_BASE = "https://api.github.com"

# Keyword -> label mapping
KEYWORD_LABELS = {
    "error": "bug",
    "add": "feature",
}


def compute_labels(issue):
    """Return the list of labels that should be applied based on keywords."""
    text = ((issue.get("title") or "") + " " + (issue.get("body") or "")).lower()
    return sorted({label for keyword, label in KEYWORD_LABELS.items() if keyword in text})


def api_request(path, method="GET", payload=None):
    req = urllib.request.Request(API_BASE + path, method=method)
    req.add_header("Authorization", f"token {GITHUB_TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    data = json.dumps(payload).encode() if payload is not None else None
    with urllib.request.urlopen(req, data=data) as resp:
        return json.loads(resp.read().decode())


def main():
    if not GITHUB_TOKEN or not REPO:
        sys.exit("GITHUB_TOKEN and GITHUB_REPOSITORY environment variables are required")
    issues = api_request(f"/repos/{REPO}/issues?state=open")
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = compute_labels(issue)
        existing = {lbl["name"] for lbl in issue.get("labels", [])}
        to_add = [lbl for lbl in labels if lbl not in existing]
        if to_add:
            api_request(f"/repos/{REPO}/issues/{issue[number]}/labels", method="POST", payload={"labels": to_add})
            print(f"Issue #{issue[number]}: added labels {to_add}")
        else:
            print(f"Issue #{issue[number]}: no new labels needed (computed: {labels})")


if __name__ == "__main__":
    main()
