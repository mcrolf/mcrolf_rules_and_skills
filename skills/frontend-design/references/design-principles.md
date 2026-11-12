# Design principles in practice

Read the sections relevant to the interface being built or changed. These are original working interpretations informed by the public author and publisher material below. They do not reproduce the books or imply access to their full paid text. Use current platform guidance and verified component behavior when implementation details matter.

## Apple Human Interface Guidelines

Apply Apple's interaction and layout principles to the target platform. A web interface should respect browser conventions; it does not need to imitate an Apple app or copy a platform-specific material.

- Organize by importance and reading order. Use alignment, spacing, and grouping to reveal relationships. Keep secondary choices available through understandable disclosure.
- Adapt to space, text enlargement, orientation, and localization. Allow content to grow rather than clipping it inside fixed containers.
- Use recognizable interactions and consistent control behavior. Communicate information through more than a single sensory channel. Support accessibility preferences and assistive technology.
- Provide clear feedback for an action and its outcome; avoid leaving people uncertain whether an operation completed. Keep essential content available when effects are reduced.

Sources: [HIG overview](https://developer.apple.com/design/human-interface-guidelines/), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [Motion](https://developer.apple.com/design/human-interface-guidelines/motion).

Use the W3C criteria in [accessibility.md](accessibility.md) for the web's WCAG thresholds. Native platform typography and target-size recommendations are not interchangeable with CSS-pixel requirements.

## Inclusive Components, Heydon Pickering

- Start from the content and simplest suitable HTML. Enhance it with behavior that works across input methods and assistive technology.
- Choose a pattern by what it does. Site navigation usually needs links and disclosures, not application menu roles and their keyboard model.
- Tabs require coordinated focus, selected state, panel relationships, and keyboard behavior. Use ordinary sections if switching panels adds no value.
- For disclosures, expose expanded state and the controlled content. Hidden content must not retain reachable hidden controls. Verify the transition with keyboard and screen reader.
- Cards must preserve headings, meaningful links, text selection, and independent actions. Avoid nested interactive elements or a click target that makes the entire card an unreadable link name.
- Announce meaningful asynchronous updates without moving focus unnecessarily. Use live regions sparingly so background updates do not drown out the task.

Sources: [author's project and book](https://inclusive-components.design/), [Menus and menu buttons](https://inclusive-components.design/menus-menu-buttons/), [Tabbed interfaces](https://inclusive-components.design/tabbed-interfaces/), [Collapsible sections](https://inclusive-components.design/collapsible-sections/), [Cards](https://inclusive-components.design/cards/), [Notifications](https://inclusive-components.design/notifications/).

## Form Design Patterns, Adam Silver

- Justify every question by how its answer is used. Remove unnecessary fields before attempting space-saving styling.
- Give inputs persistent, associated labels. Put essential instructions beside the control and associate hints programmatically. Placeholders cannot carry labels or essential guidance.
- Choose input types, autocomplete, and mobile keyboards for the expected answer. Give related choices a fieldset and legend; make inputs look operable.
- Prefer a readable, usually single-column flow, with labels closer to their controls than adjacent questions. Use clear action labels.
- Usually validate on submission. Avoid errors while someone is still composing an answer. Keep submission available so people can discover and correct mistakes.
- Explain the problem and correction beside each affected field. For multiple errors, provide a focused summary with links to the fields. Preserve entries during recovery. Validate on the server as well.
- For complex forms, divide work around meaningful tasks, preserve progress, and make back/review behavior predictable.

Sources: [publisher's registration-form excerpt](https://www.smashingmagazine.com/2018/10/form-design-patterns-excerpt-a-registration-form/), [publisher's book overview](https://www.smashingmagazine.com/2018/10/form-design-patterns-release/), [author's form-design workshop](https://smashingconf.com/online-workshops/workshops/form-design-adam-silver).

Implementation rule: only replace browser validation when a complete accessible alternative handles submission, errors, focus, and recovery. Prevent duplicate requests during an active submission without making pre-submission validity an unexplained disabled-button gate.

## Refactoring UI, Adam Wathan and Steve Schoger

- Begin with the important feature and its real content. Resolve layout and hierarchy before decoration.
- Establish a coherent set of type sizes, spacing, widths, and color shades. Limit arbitrary one-off values.
- Communicate importance through weight, contrast, placement, and spacing as well as size. Quiet surrounding elements to emphasize the primary one.
- Separate groups with space or surface differences before adding borders everywhere. Tie shadows to a coherent elevation model.
- Give text a readable measure, appropriate line height, and deliberate alignment. Let different content types use different proportions.
- Refine empty states, imagery, and small details alongside the populated state. Keep text over images legible across actual backgrounds.

Source: [official book overview and contents](https://www.refactoringui.com/).

Guardrails when applying visual advice: maintain semantic HTML, visible form labels, accessible names, and WCAG contrast. Visual de-emphasis cannot make necessary information illegible. A component gallery offers possible treatments; it does not determine this product's composition.
