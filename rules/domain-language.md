---
description: Use the codebase's domain language. Challenge mismatched terms. Do not duplicate a concept under a synonym.
alwaysApply: true
---

# Domain Language

Use the project's names for entities, relationships, roles, actions, screens, and product concepts in code, UI, docs, and conversation. Do not invent a near-synonym when the codebase already names the thing. The same word can mean different models in different bounded contexts; do not merge those into one type or label until the contexts are confirmed to match.

## Prefer existing terms

- Before naming or proposing work, check types, schema, routes, UI copy, docs, tests, and prior conversation in that repo.
- Use the project term even when an industry synonym sounds clearer. A "landing page" stays a landing page unless the project also uses "home page" for a distinct surface.
- Match role, action, and entity names exactly (`moderator` and `admin`, `archive` and `delete`, `workspace` and `organization`).
- Keep existing identifiers, labels, and routes. Propose a rename only when the user asks, or the current term is inconsistent and wrong.
- When the repo uses specialist vocabulary, keep it. Do not translate it into generic tech jargon.

## Challenge mismatches

- If the user, docs, or a change uses a term that conflicts with or loosely maps onto the domain language, say the codebase term, where it appears, and which concept is intended before building.
- If two synonyms might be one concept or two, stop and resolve it.
- If a request restates an existing capability in different words, extend that capability. Do not add a parallel one.

## New concepts

- Do not add a model, endpoint, screen, flag, or doc that restates an existing concept under a new name.
- A genuinely new concept gets one term, used the same way in code, UI, and docs, and distinguished from nearby terms.
- If a synonym is needed once for clarity, pair it with the canonical term, then use only the canonical term.

This is Ubiquitous Language and Bounded Context, from Eric Evans, *Domain-Driven Design*.
