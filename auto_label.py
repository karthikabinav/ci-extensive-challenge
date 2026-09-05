import re

def get_labels(title: str, body: str = ""):
    text = f"{title} {body}"
    labels = []
    if re.search(r"\berror\b", text, re.IGNORECASE):
        labels.append("bug")
    if re.search(r"\badd\b", text, re.IGNORECASE):
        labels.append("feature")
    return labels

if __name__ == "__main__":
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for t in tests:
        print(t, "->", get_labels(t))
