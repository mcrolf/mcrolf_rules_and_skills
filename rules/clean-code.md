---
description: Before writing, changing, or reviewing code, apply the clean-code skill. Prefer clear names, small focused units, and the project's conventions.
alwaysApply: true
---

# Clean Code

Before writing, changing, or reviewing code, read and apply `~/.agents/skills/clean-code/SKILL.md`. Read `heuristics.md` beside it only when that skill says to. If that path is missing and this rules repository is the workspace, read `skills/clean-code/SKILL.md`. If neither file can be read, say so and apply the fallback below.

Project conventions win, then `domain-language`. Name the conflict when it changes the result. These checks are an original working guide associated with Robert C. Martin's *Clean Code*, not a copy of the book.

## Fallback

- Add abstraction, configuration, or indirection only for a present need. Fix a local clarity problem in code you are already changing, and leave unrelated refactors out. Fix the root cause; use a special case only when a local fix is not available.
- Name things in the project's domain language. Keep functions and types small, focused, and at one level of abstraction, with few arguments and visible side effects.
- Comment only for intent, a consequence, or a warning the code cannot carry.
- Keep tests readable, fast, independent, and repeatable.
- Do not worsen rigidity, fragility, immobility, needless complexity, needless repetition, or opacity. If the clearer structure costs something, name the tradeoff.
