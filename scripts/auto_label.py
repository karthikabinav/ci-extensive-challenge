# Auto-label script - CORRECT implementation
# Uses word boundaries to avoid false positives (e.g., "adding" should NOT match "add")
import re

def get_labels(title: str, body: str = "") -> list:
    """
    Returns labels based on keywords:
    - "bug" if text contains whole word "error"
    - "feature" if text contains whole word "add"
    Uses case-insensitive word-boundary regex to avoid substring false positives.
    """
    text = f"{title} {body}".lower()
    labels = []
    if re.search(r"\berror\b", text):
        labels.append("bug")
    if re.search(r"\badd\b", text):
        labels.append("feature")
    return labels

# Example:
# "error test" -> ["bug"]
# "feature adding requirements" -> [] ("adding" != "add")
# "email feature adding error" -> ["bug"] (only "error" matches)
