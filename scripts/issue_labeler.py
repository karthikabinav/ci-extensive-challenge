import re

def get_labels(title, body=""):
    text = (title + " " + body).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Test cases
print(get_labels("error test"))  # ["bug"]
print(get_labels("feature adding requirements"))  # ["feature"]
print(get_labels("email feature adding error"))  # ["bug", "feature"]
