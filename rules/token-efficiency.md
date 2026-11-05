---
description: Spend fewer tokens on investigation, edits, and replies. Finish the task; do not drop safeguards or verification to save tokens.
alwaysApply: true
---

# Token Efficiency

Cut unused context, tool output, code, and narration. Token savings never justify an incomplete task or weaker correctness.

## Work

- Read the request and the relevant implementation before editing. Trace callers and dependencies far enough to see the consequences.
- Search narrowly and read excerpts. Bound tool output. Reuse verified context; do not re-read unchanged files or dump directories and logs.
- Batch independent reads. Delegate independent work with a focused brief and clear ownership. Do not delegate trivial work.
- Make the smallest clear change that satisfies the whole request. Reuse project patterns, helpers, platform features, and installed dependencies.
- Skip speculative features, premature abstraction, unrelated cleanup, new dependencies, and code compressed until it is harder to read.
- Keep progress notes to findings, decisions, and blockers.

## Do not drop these to save tokens

- Validation at trust boundaries, security, and encoding or escaping for the destination.
- Error handling that prevents data loss, including safeguards in code you move or refactor.
- Accessibility, and anything the user explicitly requested.
- Investigation, lint, and verification that the change needs.

## Verification

- A non-trivial logic change leaves a runnable check that fails if the behavior breaks. Reuse or extend an existing check, and make its command discoverable.
- Check observable behavior, including the edge cases and failure paths that matter. Lint does not verify logic. For a bug fix, show that the check catches the original failure when practical.
- Run the relevant checks and required lint. Repeat or widen only when a failure, a new change, or real uncertainty justifies it.
- Wording and formatting need a look, not a new test. If a required check cannot run, say why and what is unverified. Never imply an unrun check passed.

## Replies

State the changed behavior, the verification and its result, and any blocker. Include a material limitation. Omit repeated context, step-by-step tool narration, and offers to do work already requested. Keep what the user needs to understand or use the result.

Adapted from Ponytail for this verification bar.
