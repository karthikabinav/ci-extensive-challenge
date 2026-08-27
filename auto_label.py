import re

def get_labels(title: str):
    """Automatically label issues by keyword using whole-word matching."""
    labels = []
    # Use word boundaries to avoid substring false positives (e.g. adding != add)
    if re.search(r"\berror\b", title, re.IGNORECASE):
        labels.append("bug")
    if re.search(r"\badd\b", title, re.IGNORECASE):
        labels.append("feature")
    return labels

# Example usage:
# labels = get_labels(issue_title)
# then apply via GitHub API update_issue
