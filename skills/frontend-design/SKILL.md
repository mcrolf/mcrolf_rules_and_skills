---
name: frontend-design
description: Design, build, refine, or review frontend pages, components, and applications with a product-specific identity and WCAG 2.1 AA checks. Use for UI styling, forms, and interactions.
---

# Frontend Design

Build working UI around the product's audience, content, and primary task. Preserve its framework, domain language, brand, and existing conventions unless asked to redesign. Accessibility and usability take priority over visual novelty.

## Design deliberately

- Inspect existing UI, assets, components, tokens, and tooling. For new designs or substantial redesigns, briefly state the visual direction and how content shapes layout, density, typography, color, and imagery. Small edits follow the established direction.
- Reuse a coherent token set for type, spacing, color, borders, radii, and elevation. Keep semantic heading levels independent of visual size, secondary text legible, and form labels persistent.

Read only the relevant sections of [design-principles.md](references/design-principles.md):

| When | Principles |
| --- | --- |
| Layout and interaction | Apple HIG: hierarchy, familiar behavior, adaptability, feedback, user control |
| Interactive components | *Inclusive Components*: semantic HTML, progressive enhancement, equivalent input access |
| Forms | *Form Design Patterns*: fewer questions, clear labels, validation and recovery |
| Visual refinement | *Refactoring UI*: hierarchy, consistent scales, deliberate spacing and depth |

## Avoid template and AI slop

Use Tailwind or component libraries when appropriate; retain reliable behavior while choosing a composition suited to the task. Revise these signals when they lack a product reason:

- Interchangeable hero/features/testimonials/pricing sequences or dashboards of identical cards regardless of content.
- Default gradients, glowing blobs, glass panels, pills, radii, shadows, trendy fonts, noise, or animation supplying all the identity.
- Decorative charts, generic icons, empty marketing copy, or fabricated metrics/testimonials concealing unfinished work.

Review the whole composition: without the logo, what connects it to this audience and task? If unrelated products need only a text swap, revisit information priority, proportions, rhythm, imagery, or structure. Keep the primary action obvious and simplify decoration that hinders use. Familiar controls, system fonts, restrained layouts, and a user-supplied template remain valid choices.

## Implement and verify

- Use semantic HTML and established accessible behavior; justify custom interaction. Implement applicable default, hover, focus, selected, disabled, loading, empty, error, and success states. Controls must work within scope; identify mocks.
- Adapt to available space and long, realistic content; align DOM, reading, and keyboard order. Use brief, purposeful, optional motion with input alternatives. Keep assets, dependencies, and rendering cost proportional.
- Target every applicable WCAG 2.1 A/AA criterion throughout implementation. Read relevant sections of [accessibility.md](references/accessibility.md), then use its verification workflow for affected surfaces and journeys. Do not preload unrelated reference sections or expand a small edit into a site-wide audit.
- Inspect rendered UI at narrow/wide sizes and meaningful states. Check hierarchy, alignment, typography, clipping, and template signals. Combine automated accessibility checks with manual keyboard/focus, contrast, zoom/reflow, and screen-reader checks. Fix failures and recheck affected behavior.

Report design decisions, changes, actual checks/results, and remaining failures or unverified checks using the reference's evidence guidance. If tools are unavailable, perform useful source checks and name the limitation. A scanner, screenshot, or source review alone cannot establish conformance or replace unrun manual tests.
