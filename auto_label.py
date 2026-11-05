#!/usr/bin/env python3
"""Automatically label GitHub issues by keyword.\nRules: bug if error, feature if add (case-insensitive)."""
def determine_labels(text):
    t=text.lower(); labels=[]
    
    if "error" in t: labels.append("bug")
    if "add" in t: labels.append("feature")
    return labels
