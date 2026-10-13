#!/usr/bin/env python3
"""Automatically labels issues by keyword."""

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels


if __name__ == "__main__":
    examples = ["error test", "feature adding requirements", "email feature adding error"]
    for example in examples:
        print(example, "->", get_labels(example))
