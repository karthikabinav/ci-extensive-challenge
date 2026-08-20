import os
import requests

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

def label_issue(owner, repo, issue_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels"
    labels = get_labels(issue_title)
    headers = {"Authorization": f"token {token}"}
    requests.post(url, json={"labels": labels}, headers=headers)

if __name__ == "__main__":
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for t in tests:
        print(f"{t} -> {get_labels(t)}")
