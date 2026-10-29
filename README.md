# Rules and skills

Shared agent rules and skills. [`AGENTS.md`](AGENTS.md) is the source of truth. Each provider gets a short entry-point file that points at it. Do not copy the rule text into provider files.

This repository contains:

| Path | Role |
| --- | --- |
| `AGENTS.md` | Discovery, precedence, and where to read rules and skills |
| `rules/*.mdc` | Always-on rules: parallel delegation, no em dashes, token efficiency, domain language, clean code |
| `skills/*/SKILL.md` | `knowledge-bank`, `react-best-practices`, `tough-critic` |

Skills and `AGENTS.md` look for `~/.agents/rules` and `~/.agents/skills`. A clone by itself is not enough. Open this repository in a provider you already use, paste the shared prompt, then paste the prompt for each provider you want.

## Prompt your agents to handle this for you
Follow the instructions below to get your agents to handle setup and configuration for you.

## Shared install

Paste this once:

```text
Install the rules and skills in this repository as my personal agent setup.

Link this repo into ~/.agents. Do not copy file contents.

- Link AGENTS.md to ~/.agents/AGENTS.md.
- Link each file in rules/ into ~/.agents/rules/.
- Link each directory in skills/ into ~/.agents/skills/, keeping the directory name.

If a destination is already a real directory, leave it in place and tell me so I can move it aside. Leave any other skills already in ~/.agents/skills alone.

When you finish, show me the links you created.
```

The provider prompts below assume this install is done.

## Codex

Codex loads global instructions from `~/.codex/AGENTS.md` and user skills from `~/.agents/skills`. Paste this in Codex:

```text
Point Codex at my shared agent instructions.

Write ~/.codex/AGENTS.md as a short pointer. It should tell Codex to read and follow ~/.agents/AGENTS.md before starting any task, treat that file as the source of truth for rules and skills, and report it if the file cannot be read. Do not paste the rule text into ~/.codex/AGENTS.md.

Do not install these skills under ~/.codex/skills. Codex already reads ~/.agents/skills, and a second copy would list each skill twice.

Do not replace a repository AGENTS.md. That file is for the project, and Codex loads it in addition to ~/.codex/AGENTS.md.

When you finish, tell me how to confirm the skills knowledge-bank, react-best-practices, and tough-critic are available. If a new skill does not appear, tell me to restart Codex.
```

## Claude

Claude Code reads `CLAUDE.md`, not `AGENTS.md`. It loads skills from `~/.claude/skills`, not from `~/.agents/skills`. Paste this in Claude Code:

```text
Load my shared agent instructions and the skills in this repository for every Claude Code project.

Write ~/.claude/CLAUDE.md so it imports ~/.agents/AGENTS.md with @~/.agents/AGENTS.md and nothing else. Do not copy the rule text. Do not put the .mdc files in ~/.claude/rules. Claude user rules use different frontmatter, and the import is what tells Claude to read ~/.agents/rules.

Link each skill directory from this repo into ~/.claude/skills/, keeping the directory name. Claude names a skill after its directory. If a destination is already a real directory, leave it and tell me. If this Claude instance uses CLAUDE_CONFIG_DIR, use that directory instead of ~/.claude.

When you finish, tell me to start a new session and run /context, and to expect CLAUDE.md under Memory files. Remind me that an explicit skill mention expands one skill per message: /knowledge-bank, /react-best-practices, or /tough-critic.
```

## Cursor

Cursor loads user skills from `~/.agents/skills` on this machine. It does not load `~/.agents/AGENTS.md` outside the project that contains it. Paste this in Cursor:

```text
Make Cursor follow my shared agent instructions in every project, and confirm the skills from this repository are visible.

Check that knowledge-bank, react-best-practices, and tough-critic resolve from ~/.agents/skills. Do not copy them unless one is missing.

Cursor does not load ~/.agents/AGENTS.md globally. Add this User Rule in Customize, under Rules:

Before starting any task, read and follow ~/.agents/AGENTS.md. It is the source of truth for shared global instructions, rule and skill discovery, precedence, and supporting resources. If it cannot be read, report the missing source of truth instead of silently proceeding without it.

If you cannot edit User Rules yourself, show me that text and tell me to paste it under Customize → Rules → User Rules. Do not inline the rule files into that text. The rule tells Agent to read the file.

Do not link these rules into a project's .cursor/rules unless I ask for that project. Those .mdc files are valid Cursor project rules with alwaysApply set, but the User Rule is what covers every project.

When you finish, tell me to confirm the three skills under Customize → Skills.
```

`~/.agents/skills` stays on this machine. Cursor does not copy it to Cloud Agents, Agents Window remote SSH, or self-hosted workers. To use the same skills there, paste this as well:

```text
Link the skills from this repository into ~/.cursor/skills so I can sync them for Cloud Agents. Skip any destination that is already a real directory, and tell me which ones you skipped. Then tell me to turn on Settings → Agents → Sync Skills for Cloud Agents. Only ~/.cursor/skills syncs, and the synced skills stay private to me.
```

## T3 Code

T3 Code does not keep its own rules or skills. It runs Codex, Claude Code, or Cursor, and it lists whatever that provider already loads. In a T3 session, paste the shared prompt if you have not yet, then paste the prompt for the provider that session is using. If that Claude instance has a custom `CLAUDE_CONFIG_DIR`, say so in the Claude prompt.

After the agent finishes, tell T3 to pick up the new files:

```text
The provider files for this session are in place. Tell me the T3 steps to load them: Restart agent session from the command palette, then check the skill list with $. If a skill is still missing, say to refresh that provider under Settings → Providers.
```

Home-directory files still apply in T3 worktrees under `~/.t3/worktrees/<project>/`. A project `AGENTS.md` or `CLAUDE.md` applies when it is in the checkout T3 is using.
