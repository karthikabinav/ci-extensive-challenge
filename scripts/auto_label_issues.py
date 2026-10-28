#!/usr/bin/env python3
"""Auto-label GitHub issues by keyword.
- label "bug" if issue title/body contains "error"
- label "feature" if issue title/body contains "add"
This script is intended to run in GitHub Actions on issue creation.
"""
import os, sys, json, urllib.request

def main():
    title = os.environ.get("ISSUE_TITLE", "").lower()
    body = os.environ.get("ISSUE_BODY", "").lower()
    text = f"{title} {body}"
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    print(json.dumps({"labels": labels}))
    # In GitHub Actions, use github.rest.issues.addLabels with these labels
    return labels

if __name__ == "__main__":
    main()
