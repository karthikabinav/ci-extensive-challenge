# CI Auto Label Script

This script automatically labels new issues by keyword.

- label `bug` if the issue contains `error`
- label `feature` if the issue contains `add`

Implemented via GitHub Actions: `.github/workflows/auto-label.yml`

Tested with three sample issues:
1. error test -> bug
2. feature adding requirements -> feature
3. email feature adding error -> bug, feature
