---
name: react-best-practices
description: React principles for hooks, effects, refs, state, lists, and component design, including escape hatches and correct effect usage. Must use when reading or writing React components (.tsx, .jsx files with React imports).
---

# React Best Practices

Apply this when reading or writing React components. Prefer principles over rote patterns. Follow the project's React and TypeScript conventions first. Names and structure follow the domain-language rule and the clean-code skill. When the project uses TypeScript, also load `typescript-best-practices` if that skill exists.

## Effects are escape hatches

Effects synchronize React with an external system. Most component logic does not belong in an Effect. Before adding one, try render, an event handler, or a framework or data library.

Use Effects for browser APIs, non-React libraries, window or document listeners, and imperative non-React DOM (media, maps, host modals). Prefer React Query or the project's data library over fetch-in-Effect when that stack exists.

## Prefer these over Effects

- Derived values: compute from props and state during render. Do not mirror them into other state with an Effect.
- Expensive pure calculations: memoize only when measured or clearly costly. Do not cache with Effect plus state.
- Resetting state when an identity changes: remount with a stable `key` on the subtree that owns the state.
- User-triggered work: put it in the event handler that caused it.
- Notifying parents: update parent and child in the same event, or make the component fully controlled. Do not Effect-sync local state upward.
- Several reactions to one event: keep the chain in the event handler. Do not cascade Effects.

## Effect dependencies and cleanup

- Never suppress `react-hooks/exhaustive-deps`. Fix the dependency model.
- Prefer a functional state updater when the next value depends on the previous, so that state is not an Effect dependency.
- Build options objects and unstable callbacks inside the Effect, or stabilize them, so a new identity does not retrigger the sync.
- Use `useEffectEvent` when it exists for a non-reactive read inside an Effect: latest props or callbacks without a dependency that restarts the sync.
- Clean up every subscription, timer, connection, and listener. Ignore or abort a fetch after deps change or the component unmounts.
- Development double-mounting proves cleanup. Do not hide missing cleanup with a "run once" ref.

## Refs

- Refs hold values that must not drive rendering: timer IDs, DOM nodes, previous values, imperative handles.
- Do not read or write `ref.current` during render. Touch refs in event handlers and Effects.
- For a dynamic list of DOM nodes, use a ref callback (often a Map keyed by item id), not hooks inside a loop.
- Expose an imperative parent API sparingly with `useImperativeHandle`, and only the surface the parent needs.

## Custom hooks

- A custom Hook shares stateful logic. Each call gets its own state.
- Name it `useXxx` only if it calls Hooks. Pure helpers stay ordinary functions.
- Prefer a focused Hook (`useChatRoom`, `useOnlineStatus`) over a lifecycle wrapper (`useMount`, `useEffectOnce`) that hides dependencies.

## Components, state, and composition

- Keep a component small and single-purpose. Extract repeated UI. Leave broader craftsmanship to the clean-code skill.
- Name components, props, events, and view-model fields with the project's domain language. Do not add a synonym prop or screen for an existing concept.
- Prefer composition (`children`, slots) over deep prop drilling. Use Context for a truly cross-cutting value, not as the default for every shared prop.
- Co-locate state with the components that use it. Lift it only when siblings must share it.
- Controlled when the parent must own the value; uncontrolled when ownership can stay local.
- Use a reducer when several related values update together or the transitions are non-trivial.
- Use `flushSync` only to read layout from the DOM immediately after a state update in the same event.

## Lists and keys

- Key list items with a stable id, not the array index, when order can change.
- Put `key` on the element created at the map site, not on an inner node of the child.
- Changing `key` remounts the subtree. Use that for an identity reset, not casually.

## Rendering and props

- `&&` for optional UI, a ternary for either/or, and an extracted variable or function when branches multiply.
- Destructure props in the parameter list when that stays clear. Default optional props at the boundary.
- Keep prop names aligned with domain language and existing component APIs.

## Project data layout

If the project uses this layout, keep it. Otherwise follow the repository.

- Static config, lookup tables, and constants live in `./src/lib`.
- Shared dynamic data types live in `./src/types/types.ts` or the project's types entry.
- Import static data from lib modules, and types with `import type` where that fits.

## Decision order

1. User interaction: event handler.
2. Value from props or state: compute during render.
3. Expensive pure work: memoize only when justified.
4. Reset state on identity change: `key`.
5. Sync with an external system: Effect, with cleanup.
6. Non-reactive read inside an Effect: `useEffectEvent`.
7. Mutable non-visual value: ref.
8. Shared UI or logic: a component or a focused Hook.
9. Naming and structure: domain-language and the clean-code skill.
