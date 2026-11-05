---
name: clean-code
description: Working checks for names, functions, layout, errors, boundaries, modules, tests, and design smells. Use when writing, changing, reviewing, or refactoring code, or when the user mentions clean code, craftsmanship, naming, function size, duplication, or code smells.
---

# Clean Code

Use this when writing, changing, or reviewing code. Match the file you are editing. Project conventions and `~/.agents/rules/domain-language.mdc` win on conflict; name the conflict when it changes the result. This is an original working guide associated with Robert C. Martin's *Clean Code*, not a copy of the book. Use [heuristics.md](heuristics.md) to judge a design choice.

## How to apply

1. Read the surrounding code and name the local pattern you will follow.
2. Use only the sections that match the change. A bugfix in an existing function uses Functions, Errors, and Tests. A new type also uses Modules and Names.
3. Read [heuristics.md](heuristics.md) when reviewing, extracting, splitting a type, struggling to name something, spreading a conditional or error path, or when you see duplication, a call chain through several objects, or a switch that grows with each feature.
4. Skip the heuristics file for a typo, a one-line fix whose structure is already clear, or a change that only extends an existing local pattern.
5. Stop when the change is clear. Fix a local clarity problem in code you are already changing. Leave unrelated violations unless the user asked for a cleanup.

## Simple design

In order: the change works and the relevant checks pass; duplicated knowledge of one concept is collapsed; names and structure say what the reader needs; an extra type or function exists only because it removes a real confusion, duplication, or reason to change.

## Names

- Types and variables are nouns. Functions are verbs. Predicates read as questions (`isOpen`, `hasAccess`).
- One word per concept in the module. A second word is a second concept; challenge it as domain-language says.
- Name at the level the reader needs. `customers` at a use site beats `data`. A helper inside a parser may use the parser's term.
- Let scope carry context. `User.email` stays `email`. A wide or public name includes context the caller lacks. Short names fit tiny scopes; longer names fit wider ones.
- Put side effects in the name, or split them. `createOrder` that also charges is two functions, or `createOrderAndCharge`.
- Replace a bare literal whose meaning is not obvious with a named constant.
- Drop type prefixes (`IAccount`, `strName`) unless the project requires that encoding.

## Functions

- A function does one thing, and its name is that thing. If you can extract a function whose name is not a restatement of the parent, the parent still does more than one thing.
- Statements sit at one level of abstraction. A high-level step calls a named function; indexes, parsing, and bit work live there.
- Prefer zero to two arguments. Three needs a one-sentence reason. Four or more become a parameter object or a split.
- A boolean or mode argument is two functions. Split them and name each behavior.
- Return the result. An output argument is only for a language or API with no other channel.
- A function either answers a question or changes state. `set` and `update` change state. `get`, `is`, and `calculate` return a value.
- Put a non-trivial failure path in its own function so the happy path is the story.
- Keep a boundary condition (`index == last`, `age >= minimum`) in one named place.
- Order the file downward: caller above callee, public entry above details.

## Comments

Comment only what the name and structure cannot carry: why a non-obvious decision was made, a consequence the caller will miss (ordering, units, lifetime, a required lock), a nearby hazard, a public API note when this project documents public APIs, or a required legal header.

Delete a comment that restates the next line, narrates history, marks a closing brace, or comments out code. Version control holds history. Update a comment you touch so it matches the code.

## Layout

- Follow the project's formatter.
- Separate concepts with a blank line. Keep a concept's lines together.
- Declare a name near its first use. Keep a private helper next to its caller, below it.
- A difference between two similar blocks must be a difference you can name. Otherwise make the blocks the same.

## Data, objects, and boundaries

- A behavior type hides data and exposes operations. A data carrier exposes fields and has no behavior. Pick one per type.
- A caller asks a collaborator to do work. A chain such as `order.customer.address.city` means the caller knows a structure it does not own. Give the owner a method that answers the caller's question.
- Translate a third-party type, raw payload, or external error at the edge. Inner code uses project types and names.
- Pin a subtle third-party behavior with a small test at that boundary.
- Prefer a value object when a primitive hides a unit or invites a mix-up (identifiers, money, quantities) and the project already has a place for that kind of type.

## Errors

- Use the project's failure style (exceptions, result types, or error codes) and stick to it in one function.
- Put context on a failure in the project's error shape: operation, identity, and what the caller should understand.
- Return an empty collection for "no items". Use the project's absence type for a missing single value.
- A default belongs on the parameter or in a named policy. A null that secretly means "use the default" is a second function.

## Modules and classes

- One reason to change. When methods cluster around different fields or callers, split along that cluster.
- An instance method uses the instance's data. A method that ignores it moves to the type whose data it uses, or becomes a plain function.
- The public surface is what callers need. Keep helpers unexported.
- A switch or if-chain that will grow with new variants belongs where the object is created, or becomes separate types. A switch that maps one external code once, at a boundary, can stay.
- A parent type does not mention its children. Children plug into the parent.
- Operator-facing configuration lives in one high-level place.
- If `initialize` must run before `process`, make that order structural: a constructor, or one function that runs both.

## Tests

Treat tests as production code. The scenario should be visible without decoding the scaffolding.

- Fast, independent, repeatable, self-validating. Write the test with the change.
- One concept per test. Group related assertions when splitting them would hide that concept.
- Shape the body as situation, action, expected result.
- Cover the boundaries you touched: empty, one, just inside, just outside, and the failure path. A bug fix adds the case that failed.
- A skipped test names the open question in the skip message.
- Add domain helpers (`anActiveMember()`, `submitNewOrder()`) when raw setup hides the scenario. Helpers stay free of hidden control flow.

## Concurrency

Leave the threading and async model alone unless the task is about concurrency or you must touch shared mutable state.

When you do: keep the policy (what runs concurrently, what is shared, how it stops) separate from the work. Shrink shared mutable data; prefer values not mutated after publication. Protect only the shared update, and do slow work outside it. Make cancellation, shutdown, and failure visible in the project's existing async style.

## Finish

For the code you changed: names match domain language and real side effects; each new function has one job and one level of abstraction; error and test style match the file; you added no public method, flag, or abstraction for later; a relevant check covers the behavior and the boundary you touched. If a check conflicts with a smaller, clearer local pattern, follow the local pattern.
