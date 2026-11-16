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
| Color choices | *A Dictionary of Color Combinations*: 2 to 4 color sets, tone harmony, proportion, area, temperature |

## Avoid template and AI slop

Use Tailwind or component libraries when appropriate; retain reliable behavior while choosing a composition suited to the task. Revise these signals when they lack a product reason:

- Interchangeable hero/features/testimonials/pricing sequences or dashboards of identical cards regardless of content.
- Default gradients, glowing blobs, glass panels, pills, radii, shadows, trendy fonts, noise, or animation supplying all the identity.
- Decorative charts, generic icons, empty marketing copy, or fabricated metrics/testimonials concealing unfinished work.

Do not add eyebrow text: a small label above a heading, often uppercase or letter-spaced ("FEATURES", "How it works", "Why teams choose us"). It reads as a template. Let the heading, its placement, and the content name the section. In an existing UI that already has eyebrows, leave them unless asked to redesign, and flag them in reviews.

Review the whole composition: without the logo, what connects it to this audience and task? If unrelated products need only a text swap, revisit information priority, proportions, rhythm, imagery, or structure. Keep the primary action obvious and simplify decoration that hinders use. Familiar controls, system fonts, restrained layouts, and a user-supplied template remain valid choices.

## Implement and verify

- Use semantic HTML and established accessible behavior; justify custom interaction. Implement applicable default, hover, focus, selected, disabled, loading, empty, error, and success states. Controls must work within scope; identify mocks.
- Adapt to available space and long, realistic content; align DOM, reading, and keyboard order. Use brief, purposeful, optional motion with input alternatives. Keep assets, dependencies, and rendering cost proportional.
- Target every applicable WCAG 2.1 A/AA criterion throughout implementation. Read relevant sections of [accessibility.md](references/accessibility.md), then use its verification workflow for affected surfaces and journeys. Do not preload unrelated reference sections or expand a small edit into a site-wide audit.
- Inspect rendered UI at narrow/wide sizes and meaningful states. Check hierarchy, alignment, typography, clipping, and template signals, plus these layout details:
  - **Scrollbars:** no scrollbar covers text, controls, focus rings, or the last item in a scroll area. Check with overlay scrollbars and with always-visible ones (macOS "Show scroll bars: Always", Windows). Reserve room with padding or `scrollbar-gutter: stable` where a scrollbar would cover content or shift layout. No nested double scrollbars and no horizontal page scroll at narrow widths.
  - **Spacing:** every gap comes from the spacing scale. Related items sit closer than unrelated ones, like components share padding, and content never touches a container edge, border, or icon. Check sections, card interiors, form rows, button groups, and table cells, including with long content.
  - **Corner radii:** radii come from the radius tokens. A rounded element nested inside another uses inner radius = outer radius minus the padding between them (zero or small when the padding is large), so corners stay concentric. A child flush with a rounded parent's edge shares the parent's radius or is clipped by it, so no square corner pokes out. Elements in one group (inputs and their buttons, segmented controls, joined cards) use matching or deliberately joined radii, and sharp and rounded corners mix only for a stated reason.
- Combine automated accessibility checks with manual keyboard/focus, contrast, zoom/reflow, and screen-reader checks. Fix failures and recheck affected behavior.

Report design decisions, changes, actual checks/results, and remaining failures or unverified checks using the reference's evidence guidance. If tools are unavailable, perform useful source checks and name the limitation. A scanner, screenshot, or source review alone cannot establish conformance or replace unrun manual tests.
