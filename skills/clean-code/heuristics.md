# Clean Code Heuristics

Read this when `SKILL.md` tells you to. Judge the code you are changing. Fix smells that change introduces or touches. Leave unrelated debt unless the user asked for a cleanup.

Each item says what to do when you see the smell.

## Comments

- **Obsolete comment.** Update it to match the code, or delete it.
- **Restated code.** Delete a comment that says the same thing as the next line.
- **Commented-out code.** Delete it. History stays in version control.
- **Journal or byline.** Delete change logs and author notes from the source. Keep a legal header the repository requires.
- **Noise marker.** Delete banner comments and closing-brace comments.
- **Non-local information.** A comment describes the code it sits on. Move system-wide notes to the doc the project already uses.
- **Bad public note.** If the project documents public APIs, the note names the contract, the units, and the failure. Delete a note that repeats the signature.

## Names

- **Name and behavior disagree.** Rename, or change the behavior so the name becomes true. `includeInactive` that drops inactive records gets a name that matches the filter.
- **Pun.** The same word used for two ideas gets two names. Two words for one idea collapse to the project's word.
- **Wrong level.** `data`, `info`, `manager`, `processor`, and `helper` get replaced with the domain noun or the verb actually performed, unless that word is the project's real term.
- **Encoded name.** Drop Hungarian prefixes and interface markers the project does not require.
- **Hidden side effect.** Put the extra effect in the name, or move it to the function that owns that effect.
- **Wide scope, private name.** A public or long-lived name carries the context callers need. A local name stays short.

## Functions

- **Too many arguments.** Zero to two is the normal case. Three needs a stated reason. Four or more becomes a parameter object or a split function.
- **Flag argument.** Replace a boolean or mode switch with two named functions.
- **Output argument.** Return the result. Keep an out-parameter only where the language or the existing API requires one.
- **Mixed levels.** Move low-level parsing, indexing, and arithmetic under a name the high-level function can call.
- **Two jobs.** If a meaningful extract exists whose name is not a restatement of the parent, extract it.
- **Command and query mixed.** Split the state change from the answer, or name the function so both effects are obvious and match the local style.
- **Large failure block.** Move a non-trivial try/catch or error branch into a function that handles the failure. Leave the caller as the story of the work.
- **Dead function.** Delete unused functions when you are sure no caller remains, including reflection and framework entry points the project uses.
- **Hidden order.** If one call must precede another, encode that in the constructor or in one function that runs the steps.
- **Selector argument.** A parameter that chooses which field or strategy to use is two operations or a real object. Split or name the strategy.

## Structure

- **Duplicated knowledge.** Collapse the copies into one owner of the rule. Leave incidental similarity (two loops that look alike and mean different things) alone.
- **Feature envy.** A function that mostly uses another type's data moves onto that type, or that data moves to where the behavior already lives.
- **Train wreck.** `a.b().c().d()` becomes a method on the owning type that answers the question being asked.
- **Hybrid type.** Decide. Either the type hides data behind operations, or it is a field carrier with no behavior.
- **Parent knows its children.** Remove the child type from the parent. Register or construct the variant at the edge.
- **Growing behavior switch.** Move a switch that gains a branch per feature to the creation site, or split into types. Keep a one-time mapping of an external code at the boundary.
- **Artificial coupling.** Two types that change for different reasons and share a module only for convenience get split when you are already changing that module.
- **Misplaced rule.** The code that knows the rule owns the rule. Move a condition that inspects another module's internals back to that module.
- **Too much published.** Unexport helpers that no caller outside the module uses.
- **Base class depending on details.** A general type stays free of a specific caller's needs. Push the special case to the caller or a new type.
- **Inappropriate static.** A stateless pure function can be static or module-level. A function that needs a collaborator, a clock, or a test double takes that dependency in a way the project already uses.
- **Buried configuration.** Move operator-facing values to the one high-level place this project already configures. Leave true constants next to their single use when the project does that.
- **Transitive navigation.** A caller that walks someone else's structure to reach a value gets an operation from the object it already holds.
- **Inconsistent twin.** Two similar blocks in one module work the same way. Keep a difference only when you can name it.
- **Arbitrary shape.** A private order, grouping, or naming scheme that differs from the file's scheme gets aligned with the file.
- **Wrong abstraction level in the file.** High-level policy stays at the top. Details stay below their callers.
- **Vertical scatter.** A variable declared far above its use, or a helper parked far from its caller, moves next to the use.

## General

- **Obvious behavior missing.** Implement the behavior the name promises, or change the name.
- **Boundary wrong.** Check empty, one, off-by-one, just inside, just outside, and the absent value for the logic you touched.
- **Overridden safety.** Restore the validation, timeout, type check, or test you were tempted to disable. Fix the cause.
- **Dead code.** Delete unused branches, parameters, and variables you have confirmed are unused.
- **Obscured intent.** Name an intermediate value when a condition or calculation takes a second reading to parse.
- **Negative conditional.** Write the main path as the positive condition when that reading is shorter.
- **Unbounded special case.** A special case that papers over a wrong model gets replaced with the model fix when that fix is local. Keep the special case when the local fix is not actually local.
- **Needless indirection.** Delete a wrapper, flag, or interface that has one implementation and no variation you were asked to support.
- **Opacity.** If you cannot explain the algorithm in a few sentences, replace it with named steps or a known library routine the project already accepts.
- **Logical dependency left informal.** If A must exist before B, make a type, a parameter, or a call structure that requires A.
- **Precision.** Use the project's money, time, and identifier types when a primitive would blur units or allow a mix-up.
- **Foreign language inline.** Keep SQL, HTML, and similar in the project's existing home for them when you are adding more than a trivial fragment.
- **Build or test ritual.** Use the one command the repository already documents. Do not add a manual multi-step sequence for this change.

## Tests

- **Missing behavior test.** Add a test for the behavior you changed when the project has a test harness for that area.
- **Missing boundary.** Add the empty, single, and off-by-one cases that the change can get wrong.
- **Bug without a pin.** Add the case that reproduced the bug.
- **Several concepts.** Split a test that fails for unrelated reasons into one concept per test.
- **Unreadable setup.** Extract a domain helper when construction hides the scenario. Keep assertions in the test.
- **Hidden dependency.** A test that needs a sibling test to run first gets its own setup.
- **Slow for no reason.** Keep unit tests free of network, sleep, and shared process state when the project already isolates those.
- **Silent skip.** A skipped test states what question is still open.
- **Dirty test code.** Rename, delete duplication, and remove dead helpers in the tests you touched, the same way you would in production code.

## Smells to name in a review

When you report or refuse a structure, use these words so the finding stays specific:

| Smell | Meaning |
| --- | --- |
| Rigidity | A small change forces edits in many modules |
| Fragility | A change breaks something that should have been unrelated |
| Immobility | Useful logic cannot be reused without dragging a large context |
| Needless complexity | Structure that no current caller requires |
| Needless repetition | The same rule written more than once |
| Opacity | A reader cannot tell what the code does or why |

One finding, one smell, one concrete change. Skip a smell you cannot point to in the diff.
