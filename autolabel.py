"""
Auto-label script for GitHub issues
Labels:
- bug if issue contains "error"
- feature if issue contains "add"
"""

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage
if __name__ == "__main__":
    print(get_labels("error test"))
    print(get_labels("feature adding requirements"))
    print(get_labels("email feature adding error"))
