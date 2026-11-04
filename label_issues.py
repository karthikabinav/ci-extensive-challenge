#!/usr/bin/env python3
"""
Automatically labels new issues by keyword.
- label "bug" if the issue contains "error"
- label "feature" if the issue contains "add"
"""
import os, json, urllib.request

def labels_for(text):
    t = (text or "").lower()
    labels = []
    if "error" in t:
        labels.append("bug")
    if "add" in t:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path:
        with open(event_path) as f:
            event = json.load(f)
        issue = event.get("issue", {})
        text = (issue.get("title") or "") + " " + (issue.get("body") or "")
        print(labels_for(text))
    else:
        tests = ["error test", "feature adding requirements", "email feature adding error"]
        for t in tests:
            print(t, "->", labels_for(t))
