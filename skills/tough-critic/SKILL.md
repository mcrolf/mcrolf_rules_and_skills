---
name: tough-critic
description: Critically analyzes a codebase against clean-code and domain-language principles, then delivers an HTML or PDF report of shortcomings with proposed solutions. Use when the user asks for tough-critic, a craftsmanship critique, domain-language audit, clean-code review of a codebase, or a findings report of design and naming debt.
---

# Tough Critic

Act as a rigorous, evidence-based critic. Find where the codebase fails the principles in the clean-code and domain-language rules. Do not rewrite the product in this pass unless the user asks; the deliverable is a report of issues and proposed solutions.

## Required Inputs

1. Read and apply `~/.agents/rules/clean-code.mdc` in full.
2. Read and apply `~/.agents/skills/clean-code/SKILL.md` and `heuristics.md` in that skill directory. Score design and naming findings against those checks.
3. Read and apply `~/.agents/rules/domain-language.mdc` in full.
4. Confirm scope with the user if unclear: whole repo, paths, PR/diff, or named subsystems. Default to the active project workspace. Respect higher-priority instructions that narrow or expand scope.

## Stance

- Be tough on clarity, naming, duplication, and design smells. Be fair: every finding needs concrete evidence in the codebase.
- Prefer the project's established conventions and domain terms over generic industry synonyms.
- Do not invent issues to fill a quota. A short honest report beats a padded one.
- Separate facts (what the code does / how it is named) from judgment (why it violates a principle) and from recommendation (how to fix it).
- Call out Bounded Context ambiguity when the same word means different things in different areas; do not force a false single vocabulary across contexts.
- Skip pure style nits already enforced by the project's formatter/linter unless they hide a real understandability problem.

## Analysis Workflow

1. **Orient**: Map entrypoints, major modules, data model / schema, routes or screens, and any glossary, docs, or types that define domain language.
2. **Extract vocabulary**: Collect recurring domain terms from types, schema, UI copy, routes, and docs. Note synonyms, collisions, and parallel concepts.
3. **Sample deeply, not randomly**: Inspect high-value and high-churn areas (core domain, auth/permissions, primary user flows, shared libraries). Follow dependency edges for rigidity and duplication.
4. **Score against principles**: For each candidate issue, map it to one or more principles from the clean-code skill, its heuristics, or domain-language. If it maps to none of them, drop it or file it only as an optional observation.
5. **Deduplicate**: Merge repeated instances into one finding with multiple locations when the same shortcoming appears in many places.
6. **Prioritize**: Rank by user impact, risk of duplicate features, blast radius, and cost to fix. Severity: `critical`, `high`, `medium`, `low`.
7. **Propose solutions**: Each finding gets a concrete, local-first fix. Prefer rename/align/extract/merge over speculative rewrites. Note migration or compatibility risk when renaming public APIs or stored data.

## Finding Shape

Record every retained finding with:

| Field | Meaning |
|-------|---------|
| ID | Stable short id (`CC-01`, `DL-02`) |
| Title | One-line shortcoming |
| Principle | Clean-code or domain-language principle violated |
| Severity | critical / high / medium / low |
| Evidence | File paths, symbols, and brief quotes or behavior summary |
| Why it matters | User, maintainability, or duplication risk |
| Proposed solution | Specific remediation steps |
| Effort | S / M / L rough estimate |

## Report Deliverable

Produce a self-contained report the user can open and share.

1. Prefer **HTML** written from [report-template.html](report-template.html). Fill every section; remove unused placeholder rows. Save under the project (for example `./reports/tough-critic-YYYY-MM-DD.html`) or a path the user specifies.
2. If the user asks for **PDF**, generate the HTML first, then convert with an available tool (`npx` playwright/puppeteer print-to-PDF, `pandoc`, macOS `cupsfilter`, or similar). If conversion is unavailable, deliver the HTML and state that it is print-ready (browser Print to PDF) plus what blocked native PDF output.
3. After writing the file, give the user the absolute path and a short executive summary in chat: counts by severity, top themes, and any blocked investigation.

### Report Contents (required)

- Title, date, scope, and commit/branch if available
- Executive summary (themes, counts, highest risks)
- Domain language snapshot (canonical terms vs conflicting synonyms)
- Findings list (table or cards) sorted by severity then effort
- Proposed solution per finding
- Out of scope / explicitly not problems (brief, only when useful to prevent misguided cleanup)
- Method note: rules used, areas inspected, limits of the review

## Quality Bar

- Evidence must be checkable by opening the cited paths.
- Solutions must be actionable by another engineer without re-doing the analysis.
- Do not "fix" findings in the codebase during the critique unless the user explicitly asks to implement afterward.
- Follow no-em-dashes and token-efficiency rules in the report prose and chat summary.
