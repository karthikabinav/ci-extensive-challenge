#!/usr/bin/env python3
"""
Automatically label GitHub issues based on keywords found in the issue text.

Labeling rules:
  - If the issue contains the keyword "error" -> apply the "bug" label
  - If the issue contains the keyword "add"   -> apply the "feature" label

Matching is case-insensitive and an issue can match multiple keywords, in
which case every corresponding label is applied.

Usage in CI (GitHub Actions):
  Ran whenever an issue is opened or edited. The workflow exports
  GITHUB_REPOSITORY, GITHUB_TOKEN, ISSUE_NUMBER, ISSUE_TITLE and ISSUE_BODY.

Local dry run (prints the labels that would be applied):
  python .github/scripts/auto_label.py "<issue title>" "<issue body>"
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

API_BASE = "https://api.github.com"

# Keyword -> label mapping.
KEYWORD_LABELS: dict[str, str] = {
    "error": "bug",
    "add": "feature",
}


def normalize(text: str | None) -> str:
    """Lower-case and collapse whitespace so keyword matching is stable."""
    return " ".join((text or "").lower().split())


def determine_labels(*texts: str) -> list[str]:
    """
    Return the list of labels that apply to the supplied issue texts.

    Example:
      determine_labels("error test") -> ["bug"]
      determine_labels("feature adding requirements") -> ["feature"]
      determine_labels("email feature adding error") -> ["bug", "feature"]
    """
    combined = normalize(" ".join(texts))
    return [label for keyword, label in KEYWORD_LABELS.items() if keyword in combined]


def api_request(method: str, url: str, token: str) -> list[dict]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "auto-label-issues-bot",
    }
    request = urllib.request.Request(url, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request) as response:
            payload = response.read().decode()
            return json.loads(payload) if payload else []
    except urllib.error.HTTPError as error:
        print(f"GitHub API {method} {url} failed: {error.code} {error.reason}",
              file=sys.stderr)
        raise


def apply_labels() -> int:
    """Compute and apply keyword-based labels to the issue from the CI env."""
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    token = os.environ.get("GITHUB_TOKEN", "")
    issue_number = os.environ.get("ISSUE_NUMBER", "")
    if not (repo and token and issue_number.isdigit()):
        print("Missing GITHUB_REPOSITORY / GITHUB_TOKEN / ISSUE_NUMBER; "
              "skipping API call.", file=sys.stderr)
        return 0

    labels = determine_labels(
        os.environ.get("ISSUE_TITLE", ""),
        os.environ.get("ISSUE_BODY", ""),
    )
    if not labels:
        print(f"Issue #{issue_number}: no keywords matched, no labels applied.")
        return 0

    api = f"{API_BASE}/repos/{repo}/issues/{issue_number}/labels"
    current = api_request("GET", api, token)
    current_names = {label["name"].lower() for label in current}
    new_labels = [label for label in labels if label.lower() not in current_names]
    if not new_labels:
        print(f"Issue #{issue_number}: labels already present, nothing to do.")
        return 0

    # POST appends labels without removing existing ones.
    api_request("POST", api, token)
    print(f"Issue #{issue_number}: applied labels {new_labels}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Dry run: python auto_label.py "<title>" ["<body>"]
        print(determine_labels(*sys.argv[1:]))
        sys.exit(0)
    sys.exit(apply_labels())
