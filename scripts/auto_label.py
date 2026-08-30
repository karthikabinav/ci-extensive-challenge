# Auto-label script for issues
# bug if contains whole word error, feature if contains whole word add
import re

def get_labels(title, body=""):
    text = ((title or "") + " " + (body or "")).lower()
    labels = []
    if re.search(r"\berror\b", text):
        labels.append("bug")
    if re.search(r"\badd\b", text):
        labels.append("feature")
    return labels

if __name__ == "__main__":
    for t in ["error test", "feature adding requirements", "email feature adding error"]:
        print(t, get_labels(t))
