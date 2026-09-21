"""Automatically label new issues by keyword.

The companion GitHub Actions workflow (.github/workflows/issue-labeler.yml)
runs on newly opened issues and applies:
- \"bug\" when the issue title/body contains \"error\"
- \"feature\" when the issue title/body contains \"add\"
"""

def labels_for_issue(text: str) -> list[str]:
    lowered = text.lower()
    labels = []
    if "error" in lowered:
        labels.append("bug")
    if "add" in lowered:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    import sys
    print(labels_for_issue(" ".join(sys.argv[1:])))
