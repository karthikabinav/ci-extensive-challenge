# Auto-label issues by keyword with word-boundary matching
import re

def get_labels(title: str, body: str = ""):
    text = f"{title} {body}".lower()
    labels = []
    if re.search(r"\berror\b", text):
        labels.append("bug")
    if re.search(r"\badd\b", text):
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for t in tests:
        print(t, "->", get_labels(t))
