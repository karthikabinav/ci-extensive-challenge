"""Auto-labeler: automatically labels GitHub issues by keyword.

Keyword rules:
    - issue text contains "error" -> label "bug"
    - issue text contains "add"   -> label "feature"

The text used for keyword matching is the issue title and body,
concatenated and matched case-insensitively, so an issue containing
both keywords receives both labels.

Usage as part of the CI workflow:
    python3 auto_labeler.py "<issue title + body>"

The script prints the space-separated list of labels to apply.
"""

import sys

BUG_LABEL = "bug"
FEATURE_LABEL = "feature"

# Keyword -> label mapping (checked in this order, each match adds its label).
KEYWORD_LABELS = (
    ("error", BUG_LABEL),
    ("add", FEATURE_LABEL),
)


def determine_labels(text):
    """Return the list of labels that match the given issue text."""
    text = (text or "").lower()
    labels = []
    for keyword, label in KEYWORD_LABELS:
        if keyword in text:
            labels.append(label)
    return labels


def main():
    if len(sys.argv) < 2:
        print("usage: python3 auto_labeler.py \"<issue text>\"")
        sys.exit(1)
    labels = determine_labels(sys.argv[1])
    print(" ".join(labels))


if __name__ == "__main__":
    main()
