# Global Agent Instructions

Source of truth for shared agent instructions. Provider entry points only point here. Do not follow them recursively or copy rule text into them.

## Rules

Before planning or starting a task, read and apply every `*.md` file in `~/.agents/rules/`, subject to higher-priority instructions and runtime capabilities. The current files are `parallel-delegation.md`, `no-em-dashes.md`, `token-efficiency.md`, `domain-language.md`, `clean-code.md`, and `ongoing-development.md`. Read any other `*.md` file in that directory too. A `.mdc` file with the same stem is the Cursor name for that rule; apply the rule once.

Before code, documentation, configuration, or test changes, also read applicable local guidance, in order:

1. Repository `AGENTS.md` for the working directory, then `.cursor/rules/**`, `.cursor/**/*.mdc`, and `.cursor/**/*.md`.
2. Home-level Cursor rules for this project under `~/.cursor/projects/**/rules/**`.

Use `description`, `globs`, and `alwaysApply`. Read only files that apply. Skip directories that do not exist. Do not scan `~/.cursor/extensions` unless the task is about Cursor extensions or editor configuration.

## Skills

Read a `SKILL.md` before using a skill whose name, description, or invocation policy matches the task. Prefer the provider catalog. If the catalog may be missing a skill, check:

- `~/.agents/skills/*/SKILL.md`
- `~/.codex/skills/*/SKILL.md`
- `~/.cursor/skills-cursor/*/SKILL.md` and `~/.cursor/skills/*/SKILL.md`
- Repository `.agents/skills/*/SKILL.md` and `.cursor/skills/*/SKILL.md`

Do not list every skill file when the catalog already has the match. Resolve a skill's scripts, templates, assets, and docs relative to that skill directory unless it says otherwise. Use resources the active provider can run.

## Precedence

System, developer, and direct user instructions win, then the most specific applicable rule or skill. Project guidance overrides broader personal defaults. Mention a conflict when it changes the result.

Re-read applicable rules and skills when starting a task, entering a repository, or touching a new technology. Do not assume they are already loaded.
