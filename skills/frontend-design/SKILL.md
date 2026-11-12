---
name: frontend-design
description: Design, build, refine, or review web interfaces with a product-specific visual identity and WCAG 2.1 Level AA checks. Use for frontend pages, components, applications, and UI styling, including accessible forms and interactions. Applies Apple Human Interface Guidelines and principles from Inclusive Components, Form Design Patterns, and Refactoring UI.
---

# Frontend Design

Create working interfaces whose layout, content, and visual details belong to the product. Check accessibility throughout implementation and before delivery. Avoid generic template composition and decorative novelty that makes the interface harder to use.

## Start with the product

- Inspect the existing interface, design tokens, components, content, and frontend tooling. Preserve an established design language unless the user requests a redesign. Match the user's framework and scope.
- Identify the audience, primary task, important content, device constraints, and relevant interaction states. Use the project's domain language in labels and realistic sample content.
- For new designs or substantial redesigns, state a short visual direction before implementation: what the product should feel like, how its content shapes the layout, and which typography, spacing, color, and imagery choices support that direction. A small edit follows the existing direction.
- Choose an appropriate density and hierarchy for the actual work. An operational dashboard, reading experience, and checkout have different needs. Do not force an unusual aesthetic into a familiar task.

## Design from principles

Apply the relevant sections of [design-principles.md](references/design-principles.md): Apple guidance for hierarchy, adaptability, feedback, and user control; *Inclusive Components* for interactive components; *Form Design Patterns* for forms; *Refactoring UI* for visual refinement. These are original working interpretations linked to public primary sources, not reproductions of the books.

Accessibility and the user's task take priority over a visual tactic. For example, quieter secondary text must retain contrast, and simplifying visual labels must preserve accessible names and persistent form labels. Keep semantic heading levels independent of their visual size.

## Avoid template and AI slop

Tailwind and component libraries are implementation tools. Use them when appropriate, with tokens and compositions chosen for this product. Reuse reliable component behavior; make deliberate visual decisions.

Treat these as signals to investigate and revise when they lack a product reason:

- A centered slogan and two buttons followed by interchangeable feature cards, logo strips, testimonials, and pricing sections, regardless of what the user needs.
- A dashboard made entirely of equal rounded cards when the content calls for a table, timeline, document, or other specific structure.
- Default purple gradients, glowing blobs, glass panels, excessive pills, oversized radii, or identical shadows applied across unrelated surfaces.
- Decorative charts, fabricated metrics or testimonials, generic icons, and empty marketing phrases used to make an unfinished screen appear complete.
- Choosing a fashionable font, adding noise or animation, or breaking the grid as the only source of identity.

Review the whole composition, not just individual widgets. A color swap on a starter template does not establish a product identity. Change information priority, proportions, rhythm, imagery, or content structure where the product calls for it. Do not remove useful conventional navigation, form controls, or tables merely because they are familiar.

Use these review questions:

1. If the logo and product name disappeared, which decisions would still connect the interface to this audience and task?
2. Could the same screen serve an unrelated product with only text changes? If so, revisit the content structure and visual direction.
3. Can someone identify the primary action and understand the information hierarchy without relying on decoration?
4. Is any visual flourish interfering with reading, input, focus, performance, or responsiveness? Simplify it.

System fonts, restrained palettes, rectangular controls, and plain layouts are valid intentional choices. Distinctiveness comes from the combined design and its fit to the product. The user's supplied template or existing brand remains a valid constraint.

## Implement the full interaction

- Use semantic HTML and established accessible behavior. Add custom interaction only when it serves a real requirement.
- Build the meaningful states for the changed feature: default, hover, focus, selected, disabled, loading, empty, error, and success, as applicable. Make controls perform their stated actions within the requested scope; identify mocked data and integrations.
- Define or reuse a small set of tokens for spacing, type, colors, borders, radii, and elevation. Use them consistently while giving different content appropriate structure.
- Make layouts adapt to available space and content length. Test real labels, long values, and narrow screens. Keep DOM order consistent with the reading and keyboard order.
- Use purposeful, brief motion when it clarifies change. Respect reduced-motion preferences and provide alternatives to gesture-only or hover-only interaction. Avoid animation that delays access to content.
- Keep font and image loading, dependencies, and rendering work proportional to the interface. Use the project's existing assets and tooling where suitable.

## Check accessibility and visual quality

Read and apply [accessibility.md](references/accessibility.md) when implementing or reviewing UI. Target every applicable WCAG 2.1 Level A and AA success criterion. Scale verification to the changed surfaces and affected journeys; a component change does not require an unrelated site-wide audit.

Use the project's available accessibility tooling, such as axe, plus manual keyboard, focus, contrast, zoom/reflow, and screen-reader checks. Scan interactive states as well as the initial page. An automated pass or a screenshot alone cannot establish conformance.

Inspect the rendered result when the environment permits, at narrow and wide sizes and in relevant interaction states. Check alignment, hierarchy, typography, content, clipping, focus visibility, and the template signals above. Fix concrete problems and recheck affected behavior. Follow the current environment's browser and permission rules; never claim visual or assistive-technology testing that did not run.

When tools are unavailable, complete the checks possible from the source and report the remaining rendered/manual checks as unverified. Do not silently substitute a source review for a browser or screen-reader test.

## Deliver

Briefly report what changed, the product-specific design decisions, checks actually performed and their results, and remaining issues or unverified checks. Include paths, viewport/state coverage, tools, and browser/screen-reader pairing when relevant. For an accessibility finding, identify the affected control or journey, the barrier, the relevant criterion, and the correction.

Describe the implemented accessibility target and tested scope accurately. Reserve a conformance claim for an evaluation of all applicable criteria across complete pages and processes; do not call a partial check WCAG certification.
