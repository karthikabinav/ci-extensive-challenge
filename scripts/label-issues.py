import re

def get_labels(title: str, body: str = "") -> list[str]:
    """Automatically label issues by keyword using word boundaries.
    - label \"bug\" if text contains whole word \"error\"
    - label \"feature\" if text contains whole word \"add\"
    Uses case-insensitive matching with \\b to avoid false positives
    like \"adding\" matching \"add\" or \"terror\" matching \"error\".
    """
    text = f"{title} {body}".lower()
    labels = []
    if re.search(r"\berror\b", text):
        labels.append("bug")
    if re.search(r"\badd\b", text):
        labels.append("feature")
    return labels

# Examples:
# "error test" -> ["bug"]
# "feature adding requirements" -> [] ("adding" != "add")
# "email feature adding error" -> ["bug"]
