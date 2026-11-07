---
description: Start each new feature on its own branch. Never work directly on main. When the work is done, commit and push, then ask before opening a pull request.
alwaysApply: true
---

# Ongoing Development

## Start on a branch

- Before the first edit for a new feature, create a branch for it. Do not commit or edit on `main` (or the repository's default branch).
- Branch from an up-to-date default branch unless the user names another base. Follow the repository's branch naming convention; otherwise use `feature/<short-kebab-name>`.
- If the current branch already belongs to this feature, keep working there. If it belongs to other work, ask before mixing the two.
- Read-only work (questions, investigation, reviews) needs no branch.

## Finish the branch

- When the feature is complete and its checks pass, commit with a message that describes the change, then push the branch and set its upstream.
- This rule is the user's standing request to commit and push feature branches on completion. It does not cover `main`, force pushes, or merges.
- After pushing, ask the user whether to open a pull request for the branch. Do not open one until they say yes.
