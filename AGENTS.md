# Global Agent Instructions

This file is the source of truth for the user's shared agent instructions across projects and providers. Maintain shared guidance and resource references here; keep provider entry-point files as references to this file.

## Rules and Guidance

Before planning or starting any task, read and apply these global rules, subject to higher-priority instructions and runtime capabilities:

- `~/.agents/rules/parallel-delegation.mdc`: Delegate independent work when it will not interfere with ongoing tasks. Choose the best model or provider for each subtask, and keep expensive models off trivial work.
- `~/.agents/rules/no-em-dashes.mdc`: Prohibit em dashes in agent writing and en dashes used as substitutes; allow hyphens in compound words.
- `~/.agents/rules/token-efficiency.mdc`: Keep work and responses efficient while preserving safeguards, complete scope, and meaningful verification.
- `~/.agents/rules/domain-language.mdc`: Prefer and enforce the codebase's domain language; challenge mismatched terms and avoid duplicate concepts under synonyms.
- `~/.agents/rules/clean-code.mdc`: Enforce Clean Code craftsmanship: simplicity, clear names, small focused units, honest structure, and readable tests. Before writing, changing, or reviewing code, apply the `clean-code` skill at `~/.agents/skills/clean-code/SKILL.md`.

Before making code, documentation, configuration, or test changes, discover applicable guidance in this order:

1. Repository instructions and repository-local Cursor rules, if present:
   - `AGENTS.md` files applicable to the working directory.
   - `.cursor/rules/**`
   - `.cursor/**/*.mdc`
   - `.cursor/**/*.md`
2. Shared personal rules in `~/.agents/rules/`, if present.
3. Home-level Cursor project rules in `~/.cursor/projects/**/rules/**`.

Use rule metadata such as `description`, `globs`, and `alwaysApply` to determine applicability. Read only relevant files. Provider entry-point files that reference this file are pointers, not additional rule sources; do not follow them recursively.

## Skills and Supporting Resources

Discover relevant skills from the active provider's skill catalog and these locations, when present:

- Shared personal skills: `~/.agents/skills/*/SKILL.md`
- Codex skills: `~/.codex/skills/*/SKILL.md`
- Cursor skills: `~/.cursor/skills-cursor/*/SKILL.md` and `~/.cursor/skills/*/SKILL.md`
- Repository-local skills supported by the active provider, including `.agents/skills/*/SKILL.md` and `.cursor/skills/*/SKILL.md`.

Use each skill's name, description, and invocation policy to decide when it applies. Read the relevant `SKILL.md` before using a skill. Resolve referenced scripts, templates, assets, and documentation relative to that skill's directory, unless the skill specifies another location. Use resources compatible with the active provider and available tools.

## Discovery

Prefer fast, targeted searches:

```sh
rg --files .cursor
rg --files ~/.agents/rules
find ~/.cursor/projects -type f -path '*/rules/*' -print
find ~/.agents/skills ~/.codex/skills ~/.cursor/skills-cursor ~/.cursor/skills -maxdepth 2 -name SKILL.md -print
```

Run commands only for directories that exist. Do not bulk-load `~/.cursor/extensions`; inspect it only when the task specifically concerns Cursor extensions or editor configuration.

## Precedence and Refresh

Follow system, developer, and direct user instructions first. Apply project-specific guidance over broader personal defaults where applicable. Among relevant rules and skills, use the most specific guidance first. Mention conflicts when they materially affect the result.

Do not assume guidance is already loaded. Re-check applicable rules and skills when starting a new task, touching a new technology area, or entering a repository with additional local guidance.
