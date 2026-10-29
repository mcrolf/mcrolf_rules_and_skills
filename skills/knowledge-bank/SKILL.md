---
name: knowledge-bank
description: Compiles a project knowledge bank from codebase and user attachments covering architecture, user flows, features, domain glossary, data models, and other essentials. Use when the user asks for knowledge-bank, project documentation pack, architecture docs, domain glossary, user flow diagrams, feature inventory, or to document essential project knowledge.
---

# Knowledge Bank

Build a durable, evidence-based set of project documents that a new contributor (or future agent) can use without rediscovering the system from scratch. Prefer the project's own domain language. Read `~/.agents/rules/domain-language.mdc` before writing the glossary or naming anything in the bank.

## Goal

Produce a knowledge bank directory of markdown (and diagram) documents covering at least:

- Project architecture
- User flow diagrams
- Feature details
- Domain language glossary
- Data models
- Other essentials discovered in the project (auth model, environments, integrations, runbooks pointers, decision records)

Do not invent product facts. Mark unknowns explicitly. Cite source paths or attachment names for non-obvious claims.

## Step 0: Prompt for Attachments (required)

Before deep compilation, ask the user to attach or point to anything that should feed the bank. Do this in the first response after the skill is invoked, even if the repo already has docs.

Prompt for materials such as:

- Product briefs, PRDs, roadmaps, acceptance criteria
- Existing architecture diagrams, ADRs, runbooks, onboarding docs
- Domain glossaries, brand or content style guides
- Schema dumps, ERDs, API specs (OpenAPI/GraphQL), proto files
- Design files or exported flows (Figma links, screenshots, PDF wireflows)
- Role/permission matrices, compliance notes
- Analytics event catalogs, feature flags lists
- Anything else the user considers source-of-truth

Ask them to attach files in chat when possible, or give absolute paths / URLs. Wait for their reply (or an explicit "proceed with repo only") before writing the bank, unless they already attached materials or said to continue without waiting.

When attachments arrive, inventory them in the bank index (title, type, origin) and fold their content into the relevant docs. Prefer attachment language when it conflicts with speculative wording; prefer codebase terms when attachment and code disagree, and note the conflict in the glossary.

## Output Location

Default: `./docs/knowledge-bank/` in the active project workspace (create if missing).

If the user names another path, use that. Keep filenames stable and link everything from `INDEX.md`.

Suggested layout:

```text
docs/knowledge-bank/
  INDEX.md
  architecture.md
  user-flows.md
  features.md
  domain-glossary.md
  data-models.md
  integrations.md          # optional if needed
  environments-ops.md      # optional if needed
  sources.md               # repo paths + attachments used
  assets/                  # copied or exported diagrams/images if useful
```

Add or omit optional docs based on what exists. Do not create empty filler files; if a topic has no evidence, say so in `INDEX.md` under Gaps.

## Compilation Workflow

1. **Attachment gate**: Run Step 0. Incorporate any provided materials.
2. **Orient the repo**: Entrypoints, package/app layout, frameworks, deploy targets, major folders, existing `README`/`docs`/`AGENTS.md`.
3. **Architecture**: Runtimes, bounded areas/modules, request/data flow, key libraries, auth boundaries, background jobs, external services. Prefer one overview diagram plus short prose.
4. **User flows**: Primary personas/roles and happy-path journeys (sign-up, core loop, settings, admin if present). Use Mermaid `flowchart` or `sequenceDiagram` in `user-flows.md`. Label steps with domain terms from the glossary.
5. **Features**: Inventory shipped capabilities grouped by area. For each: purpose, entry points (routes/screens/commands), primary actors, dependencies, flags if any. Skip wishlist items unless clearly documented as planned.
6. **Domain glossary**: Canonical terms, definitions, aliases/synonyms to avoid, where defined in code or docs, and bounded-context notes when the same word differs by area. Align with domain-language rules; challenge collisions instead of flattening them.
7. **Data models**: Core entities/tables/collections, relationships, ownership, identity fields, lifecycle states. Prefer Mermaid `erDiagram` or structured tables derived from schema/types. Note migrations or multi-store splits when relevant.
8. **Other essentials**: Only when evidenced: integrations, env/config map, observability, permission model, test strategy pointers, important scripts.
9. **Sources and gaps**: List every major source (repo path or attachment). List open questions and missing materials for a later refresh.
10. **Index**: `INDEX.md` summarizes purpose, how to use the bank, doc links, severity of gaps, and last-updated date/revision.

## Writing Standards

- Clear and concise. Absolute paths in the chat summary when pointing the user at files.
- Use the project's domain language throughout; do not rename concepts for taste.
- Diagrams in Mermaid inside markdown unless the user requires another format.
- Quote or paraphrase attachments with attribution; do not dump huge verbatim copyrighted specs when a structured summary suffices.
- Follow no-em-dashes and token-efficiency guidance in prose.
- Refresh mode: if a knowledge bank already exists, update in place, keep stable filenames, and note what changed in `INDEX.md`.

## Done Criteria

- User was prompted for attachments (or explicitly waived).
- `INDEX.md` plus the core docs exist for topics with evidence.
- Glossary and feature/architecture docs agree on terminology.
- Chat reply gives the absolute path to the bank, what was included, what was missing, and any conflicts between attachments and code.

## Optional Follow-ups

Only if the user asks: export PDF/HTML of the bank, deepen one doc, or reconcile glossary conflicts in the codebase (that may use tough-critic or direct refactors).
