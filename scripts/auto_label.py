def label_issue(title):
    t = title.lower()
    labels = []
    if "error" in t:
        labels.append("bug")
    if "add" in t:
        labels.append("feature")
    return labels

print(label_issue("error test"))
print(label_issue("feature adding requirements"))
print(label_issue("email feature adding error"))
