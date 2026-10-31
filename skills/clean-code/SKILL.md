---
name: clean-code
description: Applies Clean Code working checks for names, functions, layout, errors, boundaries, modules, tests, and design smells. Use when writing, changing, reviewing, or refactoring code, or when the user mentions clean code, craftsmanship, naming, function size, duplication, or code smells.
---

# Clean Code

Apply this skill when writing, changing, or reviewing code. Match the file you are editing. Project conventions and `~/.agents/rules/domain-language.mdc` win when they conflict with a check here; name that conflict when it changes the result.

This is an original working guide to principles associated with Robert C. Martin, *Clean Code*. It is not a copy of the book. Use it to decide what to write. Use [heuristics.md](heuristics.md) to judge a design choice.

## How to apply

1. Read the surrounding code and name the local pattern you will follow.
2. Run only the sections that match the change. A bugfix in an existing function uses Functions, Errors, and Tests. A new type also uses Modules and Names.
3. Read [heuristics.md](heuristics.md) when you are reviewing, extracting, splitting a type, struggling to name a function, spreading a conditional or error path, or you see duplication, a call chain through several objects, or a switch that grows with each feature.
4. Skip the heuristics file for a typo, a one-line fix whose structure is already clear, or a change that only extends an existing local pattern.
5. Stop when the change is clear. Leave unrelated violations in place unless the user asked for a cleanup.

## Simple design

Satisfy these in order:

1. The change works, and the relevant checks pass.
2. Duplicated knowledge that hides one concept is collapsed.
3. Names and structure express the intent a reader needs.
4. Extra types and functions exist because they remove a real confusion, duplication, or reason-to-change.

## Names

- Types and variables are nouns. Functions are verbs. Predicates read as questions (`isOpen`, `hasAccess`).
- Use one word for one concept across the module. A second word for the same idea is a second concept; challenge it the way domain-language says to.
- Pick a name at the level the reader needs. `customers` at a use site beats `data`. A helper buried in a parser can use the parser's term.
- Make the scope carry the context. `User.email` stays `email`. A wide or public name includes the context the caller lacks.
- Short names fit tiny scopes (a loop index, a one-line lambda). Longer names fit wider scopes.
- Include side effects in the name. `createOrder` that also charges the card is `createOrderAndCharge` or, better, two functions.
- Replace a bare literal whose meaning is not obvious at the use site with a named constant.
- Drop type prefixes and encodings (`IAccount`, `strName`) unless the project already requires that encoding.

## Functions

- A function does one thing, and its name is that thing. If you can extract another function with a name that is not a restatement of the parent, the parent is still doing more than one thing.
- Statements inside a function sit at one level of abstraction. A high-level step calls a named function; the indexes, parsing, and bit work live in that function.
- Prefer zero to two arguments. Three arguments need a one-sentence reason. Four or more become a parameter object or a split.
- A boolean or mode argument selects between two functions. Split them and name each behavior.
- Return the result. An output argument is for a language or API that has no other channel.
- A function either answers a question or changes state. `set` and `update` change state. `get`, `is`, and `calculate` return a value.
- Put a non-trivial failure path in its own function so the happy path reads as the main story.
- Keep a boundary condition (`index == last`, `age >= minimum`) in one named place.
- Order the file downward: the caller above the callee, the public entry above the details.

```text
submit(order)           // policy and steps
  validate(order)
  price(order)
  charge(order)
  record(order)
```

## Comments

Write a comment when the name and the structure cannot carry the message:

- why a non-obvious decision was made
- a consequence a caller will miss (ordering, units, lifetime, a required lock)
- a warning about a nearby hazard
- a public API note, when this project documents public APIs
- a required legal header

Delete a comment that restates the next line, narrates the change history, marks a closing brace, or disables a block of code. Version control holds history. Update a comment you touched so it matches the code.

## Layout

- Follow the project's formatter. Hand-formatting yields to the tool.
- Separate concepts with a blank line. Keep a concept's lines together.
- Declare a name near its first use.
- Keep a private helper next to its caller, below it.
- A difference between two similar blocks is a real difference. If you cannot name it, make the blocks the same.

## Data, objects, and boundaries

- A behavior type hides its data and exposes operations. A data carrier exposes fields and has no behavior. Choose one for each type.
- A caller asks a collaborator to do work. A chain such as `order.customer.address.city` means the caller knows a structure it does not own. Give the owning type a method that answers the caller's actual question.
- Translate a third-party type, raw payload, or external error at the edge module. Inner code uses project types and project names.
- When you depend on a subtle third-party behavior, pin it with a small test at that boundary.
- Prefer a value object when a primitive hides a unit or invites a mix-up (identifiers, money, quantities) and the project already has a place for that kind of type.

## Errors

- Use the project's failure style: exceptions, result types, or error codes. One function sticks to that style.
- Put context on a failure: which operation, which identity, what the caller should understand. Do this in the project's existing error shape.
- Return an empty collection when the answer is "no items". Use the project's absence type for a missing single value.
- A default belongs on the parameter or in a named policy. A null argument that secretly means "use the default" is a second, hidden function.

## Modules and classes

- A module or type has one reason to change. When methods cluster around different fields or different callers, split along that cluster.
- An instance method uses the instance's data. A method that ignores that data moves to the type whose data it does use, or becomes a plain function.
- The public surface is the set of operations callers actually need. Keep helpers unexported.
- A switch or if-chain that picks a behavior and will grow with new variants belongs where the object is created, or becomes separate types. A switch that maps one external code once, at a boundary, can stay.
- A parent type does not mention its children. Children plug into the parent.
- Configurable values that an operator might change live in one high-level place.
- If `initialize` must run before `process`, make that order structural: a constructor, or one function that runs both in order.

## Tests

Treat test code as production code. A reader should see the scenario without decoding the scaffolding.

- Fast, independent, repeatable, self-validating. Write the test with the change, in the same change.
- One concept per test. Group closely related assertions when splitting them would hide that concept.
- Shape the body as the situation, the action, and the expected result.
- Cover the boundaries of the behavior you touched: empty, one, just inside, just outside, and the failure path.
- When you fix a bug, add the case that failed.
- A skipped test names the open question in the skip message.
- Build domain helpers (`anActiveMember()`, `submitNewOrder()`) when raw setup hides the scenario. Those helpers stay free of hidden control flow.

## Concurrency

Leave the threading and async model alone unless the task is about concurrency or you must touch shared mutable state.

When you do:

- Keep the policy (what runs concurrently, what is shared, how it stops) separate from the work being protected.
- Shrink the mutable shared data. Prefer values that are not mutated after publication.
- Keep the protected section to the shared update. Do the slow work outside it.
- Make cancellation, shutdown, and failure visible in the project's existing async style.

## Finish check

Before you stop, confirm for the code you changed:

- The names match domain language and the function's real side effects.
- Each new function has one job and one level of abstraction.
- You followed the local error and test style.
- You did not add a public method, configuration flag, or abstraction "for later".
- A relevant check covers the behavior, including the boundary you touched.

If a check here conflicts with a smaller, clearer local pattern, follow the local pattern.
