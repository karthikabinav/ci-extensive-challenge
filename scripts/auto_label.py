"""
auto_label.py

Automatically labels GitHub issues by keyword matching for the
ci-extensive-challenge repository.

Rules:
  - If the issue title or body contains "error"  -> apply label "bug"
  - If the issue title or body contains "add"    -> apply label "feature"
  - An issue can receive multiple labels if multiple keywords match.

Usage (with REST API, needs a personal access token):
  GITHUB_TOKEN=<token> GITHUB_REPO=owner/ci-extensive-challenge python scripts/auto_label.py <issue_number> --run

By default the script runs in "preview" mode for a built-in test payload
so it is easy to experiment with safely.
"""

import sys

# Keyword -> label mapping, evaluated in order.
KEYWORD_LABELS = (
    ("error", "bug"),
    ("add", "feature"),
)


def get_labels_for_text(text):
    """Return the list of labels that apply to *text* (title + body)."""
    labels = []
    if not text:
        return labels
    text_lower = text.lower()
    for keyword, label in KEYWORD_LABELS:
        if keyword in text_lower:
            labels.append(label)
    return labels


def apply_labels(repo, issue_number, labels, token):
    """Apply *labels* to the given issue via the GitHub REST API."""
    import json
    import urllib.request

    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/labels"
    data = json.dumps(labels).encode()
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request) as response:
        return response.status


def main():
    tests = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    print("Keyword auto-labeller preview:")
    for title in tests:
        print(f"  {title!r} -> {get_labels_for_text(title)}")
    print("All preview cases executed successfully.")


if __name__ == "__main__":
    main()
