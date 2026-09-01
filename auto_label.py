# Auto-label script for GitHub issues
# Labels new issues by keyword: "bug" if title contains "error", "feature" if title contains "add"

def get_labels(title: str):
    """Return list of labels based on keywords in title."""
    labels = []
    title_lower = title.lower()
    if "error" in title_lower:
        labels.append("bug")
    if "add" in title_lower:
        labels.append("feature")
    return labels

# Example usage with GitHub API (via MCP tools):
# For each new issue, call get_labels(issue_title) and apply labels via update_issue
# Example:
#   title = "error test" -> ["bug"]
#   title = "feature adding requirements" -> ["feature"]
#   title = "email feature adding error" -> ["bug", "feature"]

if __name__ == "__main__":
    test_titles = ["error test", "feature adding requirements", "email feature adding error"]
    for t in test_titles:
        print(f"{t!r} -> {get_labels(t)}")
