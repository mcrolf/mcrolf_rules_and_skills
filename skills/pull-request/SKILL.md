---
name: pull-request
description: Write pull request titles and descriptions that name the subject, explain the problems fixed and how, describe each new feature's purpose and behavior, and record the testing done, evidence of success, and merge danger (one-way or two-way door, blast radius). Use when opening, drafting, or updating a pull request, or when the user asks for a PR title, PR description, or PR summary.
---

# Pull Request

Write the title and description from what the branch actually changes. All PR text follows [references/writing.md](references/writing.md), [references/domain-language.md](references/domain-language.md), and the Writing section below. Opening a PR follows [references/ongoing-development.md](references/ongoing-development.md): ask the user first.

If the repository has a PR template (`.github/pull_request_template.md` or similar), fill its sections with the content below instead of replacing it.

## Gather the facts

1. Read the commits and diff against the base branch (`git log <base>..HEAD`, `git diff <base>...HEAD`). Read enough of the changed code to describe behavior, not just which files moved.
2. Read the issue, ticket, or conversation that prompted the work to learn the problem or the feature's purpose.
3. Collect the testing actually done: commands run and their results, and manual checks. Use this session's results and anything recorded on the branch. Do not invent results.
4. When updating an existing PR, re-read the full diff. Rewrite sections the new commits made inaccurate.

## Title

- Name the main subject matter: the feature, component, or problem the PR is about, in the project's terms.
- With several subjects, list them when there are two or three short ones (`Add export retries and fix CSV header order`). Otherwise generalize to what they share (`Harden billing sync error handling`).
- Follow the repository's title convention (Conventional Commits prefix, ticket key) if recent merged PRs use one. Otherwise start with an imperative verb.
- Keep it under about 72 characters, with no trailing period.

## Description

Include only the sections that apply. A PR can have both.

### Problems fixed

For each problem, state:

- **The problem**: the observed behavior, who or what it affected, and the cause when known.
- **The fix**: what changed to correct it, and how that addresses the cause.

Link the issue or ticket when one exists.

### New features

For each feature, state:

- **Purpose**: the need it serves and who uses it.
- **Behavior**: what it does, how it is triggered or used, and its inputs, outputs, defaults, limits, and any configuration or flag.

Changes that are neither (refactors, docs, dependency bumps) get one line each under **Other changes**.

### Testing

- List each check: the command or manual steps, and the result.
- Name anything not tested and why.
- Never say a check passed unless it ran and passed. If nothing was tested, write `Not tested` and the reason.

### Evidence

Show that the change worked, not just that checks ran.

- For a fix, show the original failure and that it no longer happens: the failing test or error before, and the passing result after.
- For a feature, show it doing what the Behavior section says: command output, a log excerpt, a screenshot, or a link to a run.
- Keep excerpts short and quote them exactly. Use output from this session or the branch's CI. Never reconstruct or invent it.
- If there is no evidence beyond the checks in Testing, say so.

### Merge danger

- **Door**: say whether the change is a two-way door or a one-way door, and why.
  - Two-way: cheap to reverse. Reverting the merge or a small follow-up restores the old behavior with no lasting effect (code-only changes, additive changes, behavior behind a flag).
  - One-way: hard or impossible to reverse once merged or deployed (a destructive or data-rewriting migration, removing a public API, field, or route, deleting data, publishing a release, or a decision others will build on). Name what makes it one-way and the rollback plan or mitigation.
- **Blast radius**: name what can break if the change is wrong: which users, services, data, callers, or environments, and how the failure would show up. Base it on the diff and its callers, not a guess.

## Writing

Apply [references/writing.md](references/writing.md), including its punctuation rules. Its product-copy guidance carries over to PRs as follows:

- State facts the diff, issue, or conversation establishes. If a detail is unknown, say so or ask. Do not guess at causes, impact, or results.
- Use plain sentences that name the change and its effect. No pitch language, slogans, or claims like "significantly improves" without evidence.
- Do not add a summary or closing sentence that repeats the sections above it.

## Template

```markdown
## Problems fixed

- **<problem>**: <what went wrong, and why>. Fixed by <what changed and how it addresses the cause>. (<issue link>)

## New features

### <feature name>

<Purpose: the need it serves and who uses it.> <Behavior: what it does, how it is used, defaults and limits.>

## Other changes

- <one line each>

## Testing

- `<command>`: <result>
- Manual: <steps>. Result: <what was observed>.
- Not tested: <gap>, because <reason>.

## Evidence

- Before: <failure, quoted exactly>
- After: <result, quoted exactly, or a screenshot or run link>

## Merge danger

- **Door**: <Two-way or One-way>. <Why, and for a one-way door the rollback plan or mitigation.>
- **Blast radius**: <what can break if this is wrong, and how it would show up.>
```

## Check before submitting

- The title names the main subject, or lists or generalizes several.
- Every problem has its fix. Every feature has its purpose and behavior.
- Every statement is supported by the diff, the issue, or the conversation.
- The testing section matches what actually ran.
- The evidence is real output or a real artifact that shows the change working, or the PR says there is none.
- Merge danger names the door type with a reason, and the blast radius names what can break.
- The text passes the Writing section and the punctuation rules in [references/writing.md](references/writing.md).
