---
name: knowledge-bank
description: Compiles a project knowledge bank from the codebase and user attachments, covering architecture, user flows, features, a domain glossary, data models, and other essentials. Use when the user asks for knowledge-bank, a project documentation pack, architecture docs, a domain glossary, user flow diagrams, a feature inventory, or to document essential project knowledge.
---

# Knowledge Bank

Build a durable, evidence-based document set a new contributor or later agent can use without rediscovering the system. Use the project's domain language. Read `~/.agents/rules/domain-language.mdc` before the glossary or any new name.

## Goal

Write markdown and diagrams covering at least: architecture, user flows, features, a domain glossary, data models, and other evidenced essentials (auth, environments, integrations, runbook pointers, decision records).

Do not invent product facts. Mark unknowns. Cite a repo path or attachment for any non-obvious claim.

## Attachments first

On the first response after this skill is invoked, ask for source material, even if the repo already has docs. Wait for a reply, or an explicit "proceed with repo only", before writing. Skip the wait only when materials are already attached or the user said to continue.

Ask for briefs, PRDs, roadmaps, acceptance criteria, architecture diagrams, ADRs, runbooks, onboarding docs, glossaries, style guides, schema dumps, ERDs, OpenAPI, GraphQL, or proto specs, design exports, permission matrices, compliance notes, analytics catalogs, feature-flag lists, and anything else they treat as source of truth. Chat files, absolute paths, or URLs are fine.

Inventory attachments in the index (title, type, origin) and fold them into the relevant docs. Prefer attachment language over speculation. When an attachment and the code disagree, use the codebase term and note the conflict in the glossary.

## Output

Default: `./docs/knowledge-bank/` in the active workspace. Use another path if the user names one. Keep filenames stable and link them from `INDEX.md`. Start the index from [templates/INDEX.md](templates/INDEX.md).

```text
docs/knowledge-bank/
  INDEX.md
  architecture.md
  user-flows.md
  features.md
  domain-glossary.md
  data-models.md
  integrations.md
  environments-ops.md
  sources.md
  assets/
```

`integrations.md`, `environments-ops.md`, and `assets/` are optional. Do not create empty files. A topic with no evidence goes under Gaps in `INDEX.md`.

## Workflow

1. Run the attachment step and incorporate what they provide.
2. Orient: entrypoints, package layout, frameworks, deploy targets, major folders, and existing README, docs, and AGENTS.md.
3. Architecture: runtimes, modules, request and data flow, key libraries, auth boundaries, background jobs, external services. One overview diagram plus short prose.
4. User flows: primary roles and happy paths (sign-up, core loop, settings, admin when present). Mermaid `flowchart` or `sequenceDiagram` in `user-flows.md`, labeled with glossary terms.
5. Features: shipped capabilities by area. For each, record purpose, entry points, actors, dependencies, and flags. Skip wishlist items unless they are documented as planned.
6. Glossary: canonical term, definition, aliases to avoid, where it is defined, and a bounded-context note when one word differs by area. Do not flatten a collision.
7. Data models: entities, relationships, ownership, identity, lifecycle. Mermaid `erDiagram` or tables from schema or types. Note migrations or multi-store splits.
8. Other essentials, only when evidenced: integrations, env and config, observability, permissions, test pointers, important scripts.
9. Sources and gaps: every major repo path or attachment, plus open questions.
10. Index: purpose, how to use the bank, links, gap severity, and last-updated date. If a bank already exists, update it in place, keep filenames, and note what changed.

## Writing and done

Be concise. Use domain language. Diagrams are Mermaid in markdown unless the user asks for another format. Summarize long copyrighted specs; do not paste them. Follow the no-em-dash and token-efficiency rules.

Done when the user was asked for attachments or waived that step, `INDEX.md` and the evidenced core docs exist, and glossary, features, and architecture share terms. In chat, give the absolute bank path, what was included, what is missing, and any attachment-versus-code conflict.

Export, a single-doc expansion, or glossary fixes in code happen only if the user asks.
