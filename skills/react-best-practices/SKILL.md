---
name: react-best-practices
description: Provides React principles for hooks, effects, refs, state, lists, and component design. Covers escape hatches, anti-patterns, and correct effect usage. Must use when reading or writing React components (.tsx, .jsx files with React imports).
---

# React Best Practices

Apply this skill when reading or writing React components. Prefer principles over rote patterns. Follow the active project's React and TypeScript conventions first.

## Related Guidance

- Design, naming, structure, comments, and tests: apply `~/.agents/rules/clean-code.mdc` and `~/.agents/skills/clean-code/SKILL.md`.
- Domain terms for entities, roles, actions, screens, and props: apply `~/.agents/rules/domain-language.mdc`. Challenge mismatched vocabulary before inventing parallel UI or state concepts.
- When TypeScript is in use, also load `typescript-best-practices` if available. Type-first modeling, discriminated unions, and boundary validation still apply inside React code.

## Core Principle: Effects Are Escape Hatches

Effects synchronize React with external systems. Most component logic should not use Effects. Before adding one, ask whether the work can happen during render, in an event handler, or via a framework/data library instead.

Use Effects for external systems: browser APIs, third-party non-React libraries, window/document listeners, imperative non-React DOM (media, maps, host modals), and similar subscriptions. Prefer React Query or framework data fetching over ad-hoc fetch-in-Effect when the project already has that stack.

## Prefer These Over Effects

- Derived values: compute from props and state during render. Do not mirror props/state into other state via Effect.
- Expensive pure calculations: memoize only when measured or clearly costly; do not use Effect plus state as a cache.
- Resetting state when an identity changes: remount with a stable `key` on the subtree that owns the state.
- User-triggered logic: put it in the event handler that caused it (notifications, analytics, navigation after click).
- Notifying parents: update parent and child together in the same event, or make the component fully controlled. Do not Effect-sync local state upward.
- Multi-step reactions to one event: keep the chain in the event handler with derived values, not a cascade of Effects.

## Effect Dependencies and Cleanup

- Never suppress `react-hooks/exhaustive-deps` to silence warnings. Fix the dependency model.
- Prefer functional state updaters when the next value depends on the previous, so the Effect does not need that state as a dependency.
- Build options objects and unstable callbacks inside the Effect, or stabilize them deliberately, so new identities do not retrigger sync work every render.
- Use `useEffectEvent` (when available) for non-reactive logic read inside an Effect: latest props/callbacks without adding them as reactive dependencies that would restart the sync.
- Every subscription, timer, connection, and listener must clean up. Data fetches started in Effects should ignore or abort stale responses after deps change or unmount.
- Development double-mounting exists to prove cleanup is correct. Do not guard with "run once" refs to hide missing cleanup.

## Refs

- Refs hold values that must not drive rendering: timer IDs, DOM nodes, previous values, imperative handles.
- Do not read or write `ref.current` during render. Touch refs in event handlers and Effects.
- For dynamic lists of DOM nodes, use a ref callback (often with a Map keyed by item id), not hooks inside loops.
- Expose imperative parent APIs sparingly with `useImperativeHandle`; limit the surface to what the parent truly needs.

## Custom Hooks

- Custom Hooks share stateful logic; each call gets its own state instance.
- Name something `useXxx` only if it calls Hooks. Pure helpers stay ordinary functions.
- Prefer focused, concrete Hooks (`useChatRoom`, `useOnlineStatus`) over generic lifecycle wrappers (`useMount`, `useEffectOnce`) that hide dependencies from the linter and reader.

## Components, State, and Composition

- Keep components small and single-purpose. Extract repeated UI into dedicated components. Defer broader craftsmanship (size, coupling, comments, smells) to clean-code.
- Name components, props, events, and view-model fields with the project's domain language. Do not introduce synonym props or screens that duplicate existing concepts.
- Prefer composition (`children`, slots) over deep prop drilling. Use Context for truly cross-cutting values, not as a default for every shared prop.
- Co-locate state with the components that use it. Lift only when siblings must share it.
- Prefer controlled components when the parent must own the value; uncontrolled when ownership can stay local.
- Use a reducer when several related values update together or transition rules are non-trivial.
- Reach for `flushSync` only when you must read layout from the DOM immediately after a state update in the same event.

## Lists and Keys

- Give list items stable unique keys from identity (ids), not array indexes, especially when order can change.
- Put `key` on the element created at the map site, not on an inner node inside the child component.
- Changing `key` remounts the subtree; use that deliberately for identity resets, not casually.

## Rendering and Props

- Prefer simple conditional rendering: `&&` for optional UI, ternary for either/or, and extracted variables/functions when branches multiply.
- Destructure props in the parameter list when it stays clear. Supply defaults for optional props at the boundary.
- Keep prop names aligned with domain language and existing component APIs in the repo.

## Project Data Layout (When Present)

If the project uses this layout, keep it; otherwise follow the repository's existing structure.

- Static config, lookup tables, and constants: `./src/lib` modules.
- Shared dynamic data types (API, records, shared props): `./src/types/types.ts` or the project's equivalent types entrypoint.
- Import static data from lib modules and types with `import type` where appropriate.

## Decision Order

1. User interaction: event handler.
2. Value from props/state: compute during render.
3. Expensive pure work: memoize only when justified.
4. Reset state on identity change: `key`.
5. Sync with an external system: Effect with cleanup.
6. Non-reactive read inside Effect: `useEffectEvent`.
7. Mutable non-visual value: ref.
8. Shared UI or logic: extract a component or focused Hook.
9. Naming and structure: domain-language rule and the clean-code skill.
