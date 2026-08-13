# Auto-Label Automation

This repository includes an automation script that automatically labels new issues by keyword:

- label "bug" if the issue contains "error"
- label "feature" if the issue contains "add"

Implementation:
- Python script: `scripts/auto_label.py`
- GitHub Actions workflow: `.github/workflows/auto-label.yml`

Test cases:
1. "error test" -> bug
2. "feature adding requirements" -> feature
3. "email feature adding error" -> bug, feature
