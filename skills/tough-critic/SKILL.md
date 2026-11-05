---
name: tough-critic
description: Critiques a codebase against clean-code and domain-language, then writes an HTML or PDF report of shortcomings and fixes. Use when the user asks for tough-critic, a craftsmanship critique, a domain-language audit, a clean-code review of a codebase, or a findings report of design and naming debt.
---

# Tough Critic

Find where the codebase fails the clean-code and domain-language principles. Deliver a report of issues and proposed fixes. Do not change the product in this pass unless the user asks.

## Inputs

1. Read `~/.agents/rules/clean-code.md`, `~/.agents/skills/clean-code/SKILL.md`, and `heuristics.md` beside that skill. Score design and naming against those checks.
2. Read `~/.agents/rules/domain-language.md`.
3. If scope is unclear, ask: whole repo, paths, a diff, or named subsystems. Default to the active workspace. Honor instructions that narrow or widen scope.

## Stance

Be tough on clarity, naming, duplication, and design smells. Every finding needs evidence in the codebase. Prefer the project's conventions and domain terms. Do not invent issues to fill a quota. Separate fact (what the code does or how it is named), judgment (which principle it violates), and the fix. When one word means different things in different areas, say so; do not force one vocabulary across bounded contexts. Skip formatter or linter nits unless they hide a real understanding problem.

## Workflow

1. Map entrypoints, major modules, schema, routes or screens, and any glossary or types that define domain language.
2. Collect recurring terms. Note synonyms, collisions, and parallel concepts.
3. Inspect high-churn, high-value areas (core domain, auth, primary flows, shared libraries) and follow edges for rigidity and duplication.
4. Map each candidate to a clean-code check, a heuristic, or domain-language. Drop it if it maps to none. Keep it as an optional observation only when that is honestly useful.
5. Merge repeated instances into one finding with several locations.
6. Rank by user impact, duplicate-feature risk, blast radius, and fix cost. Severity is `critical`, `high`, `medium`, or `low`.
7. Give each finding a concrete local fix: rename, align, extract, or merge before a speculative rewrite. Note migration risk for a public API or stored data.

## Finding

| Field | Meaning |
| --- | --- |
| ID | Short stable id (`CC-01`, `DL-02`) |
| Title | One-line shortcoming |
| Principle | Clean-code or domain-language check violated |
| Severity | critical, high, medium, or low |
| Evidence | Paths, symbols, and a brief quote or behavior |
| Why it matters | User, maintainability, or duplication risk |
| Proposed solution | Specific remediation |
| Effort | S, M, or L |

## Report

Write a self-contained file from [report-template.html](report-template.html). Fill every section and remove unused placeholder rows. Default path: `./reports/tough-critic-YYYY-MM-DD.html`, or a path the user names.

If they ask for PDF, write the HTML first, then convert with an available tool (Playwright or Puppeteer print, pandoc, or macOS `cupsfilter`). If conversion fails, deliver the HTML, say it is print-ready, and name what blocked PDF.

Include title, date, scope, and commit or branch; an executive summary with themes, counts, and highest risks; a domain-language snapshot of canonical terms and conflicting synonyms; findings sorted by severity then effort, each with a solution; a short "not a problem" note only when it prevents a bad cleanup; and a method note naming the rules, the areas inspected, and the limits.

Then give the absolute path and a short summary: counts by severity, top themes, and any blocked investigation.

Evidence must be checkable by opening the cited paths. A fix must be actionable without repeating the analysis. Do not edit the codebase during the critique unless the user asks. Follow the no-em-dash and token-efficiency rules in the report and the summary.
