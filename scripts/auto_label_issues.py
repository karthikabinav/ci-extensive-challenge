#!/usr/bin/env python3
"""
Automatically label GitHub issues by keyword.

Rules:
  - If the issue title/body contains "error" -> apply label "bug"
  - If the issue title/body contains "add"   -> apply label "feature"

Usage:
  python auto_label_issues.py --repo <owner>/<repo> --token $GITHUB_TOKEN

This is a standalone version of the logic in the
.github/workflows/auto-label-issues.yml GitHub Actions workflow, useful for
running locally or in cron jobs against existing issues.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

API = "https://api.github.com"

# Keyword -> label mapping (checked case-insensitively against title + body)
LABEL_RULES = [
    ("error", "bug"),
    ("add", "feature"),
]


def derive_labels(text):
    """Return the set of labels that apply to the given issue text."""
    lowered = (text or "").lower()
    return {label for keyword, label in LABEL_RULES if keyword in lowered}


def github_request(method, url, token, data=None, accept_preview=False):
    req = urllib.request.Request(url, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Authorization", f"Bearer {token}")
    if data is not None:
        req.add_header("Content-Type", "application/json")
        body = json.dumps(data).encode()
    else:
        body = None
    try:
        with urllib.request.urlopen(req, data=body) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        sys.stderr.write(f"HTTP {exc.code} {exc.reason} for {method} {url}\n")
        raise


def main():
    parser = argparse.ArgumentParser(description=LABEL_RULES.__doc__)
    parser.add_argument("--repo", required=True, help="Repository in owner/name form")
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"),
                        help="GitHub token (defaults to $GITHUB_TOKEN)")
    parser.add_argument("--limit", type=int, default=30,
                        help="Max number of open issues to scan")
    args = parser.parse_args()

    if not args.token:
        parser.error("A GitHub token is required (--token or $GITHUB_TOKEN)")

    issues = github_request(
        "GET", f"{API}/repos/{args.repo}/issues?state=open&per_page={args.limit}", args.token
    )

    for issue in issues:
        if "pull_request" in issue:  # skip pull requests
            continue
        text = issue.get("title", "") + "\n" + (issue.get("body") or "")
        labels = sorted(derive_labels(text))
        if labels:
            print(f"Issue #{issue[number]} \"{issue[title]}\" -> labels: {labels}")
            github_request(
                "PUT",
                f"{API}/repos/{args.repo}/issues/{issue[number]}/labels",
                args.token,
                data={"labels": labels},
            )
        else:
            print(f"Issue #{issue[number]} \"{issue[title]}\" -> no labels")


if __name__ == "__main__":
    main()
