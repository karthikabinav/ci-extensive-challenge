#!/usr/bin/env python3
"""
Issue auto-labeling script.

Automatically labels issues based on keyword matching:
  - label "bug" if the issue contains "error"
  - label "feature" if the issue contains "add"

Matching is case-insensitive and inspects both the title and the body.
"""

KEYWORD_LABELS = {
    "error": "bug",
    "add": "feature",
}


def labels_for_issue(title: str, body: str = "") -> list:
    text = f"{title or } {body or }".lower()
    return sorted({label for keyword, label in KEYWORD_LABELS.items() if keyword in text})


def main():
    sample_issues = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for title in sample_issues:
        print(f"Issue: {title!r} -> labels: {labels_for_issue(title)}")


if __name__ == "__main__":
    main()
