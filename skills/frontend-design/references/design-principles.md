# Design principles in practice

Read relevant sections only. These original working interpretations use public primary sources, not the books' full paid text. Verify current platform and component details when needed.

## Apple Human Interface Guidelines

Adapt the principles to the target platform and browser conventions; copying Apple's appearance is optional.

- Express importance and relationships through reading order, alignment, spacing, and grouping. Disclose secondary choices clearly.
- Adapt to space, enlarged text, orientation, and localization without clipping.
- Keep controls familiar and consistent. Support assistive technology, accessibility preferences, and multiple sensory channels.
- Communicate actions and outcomes clearly. Preserve essential information when effects are reduced; keep people in control.

Sources: [HIG](https://developer.apple.com/design/human-interface-guidelines/), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), [Motion](https://developer.apple.com/design/human-interface-guidelines/motion).

Use [WCAG web thresholds](accessibility.md); native point sizes are not CSS pixels.

## Inclusive Components, Heydon Pickering

- Enhance suitable semantic HTML across input methods and assistive technology.
- Match patterns to behavior: site navigation usually needs links/disclosures, not application menu roles.
- Tabs coordinate focus, selection, panels, and keyboard behavior; use sections if switching adds no value.
- Disclosures expose expanded state and content relationships; hidden content has no reachable controls. Verify keyboard and screen-reader transitions.
- Cards retain headings, meaningful links, text selection, and independent actions. Avoid nested controls and verbose whole-card link names.
- Announce meaningful asynchronous updates sparingly, without unnecessary focus movement.

Sources: [Project/book](https://inclusive-components.design/), [Menus](https://inclusive-components.design/menus-menu-buttons/), [Tabs](https://inclusive-components.design/tabbed-interfaces/), [Disclosures](https://inclusive-components.design/collapsible-sections/), [Cards](https://inclusive-components.design/cards/), [Notifications](https://inclusive-components.design/notifications/).

## Form Design Patterns, Adam Silver

- Justify each question by its use; remove unnecessary fields before shrinking their presentation.
- Keep associated labels and essential hints visible beside inputs; connect hints programmatically. Placeholders cannot replace them.
- Match input types, autocomplete, and keyboards to answers. Group related choices with fieldset/legend; make controls look operable.
- Prefer a readable single-column flow, labels nearer their controls, and clear action labels.
- Usually validate on submission, not during composition. Keep submission available to reveal mistakes.
- Explain corrections beside fields; focus a linked summary for multiple errors. Preserve entries and validate server-side.
- Divide complex forms into meaningful tasks with saved progress and predictable back/review behavior.

Sources: [Book excerpt](https://www.smashingmagazine.com/2018/10/form-design-patterns-excerpt-a-registration-form/), [Overview](https://www.smashingmagazine.com/2018/10/form-design-patterns-release/), [Author's workshop](https://smashingconf.com/online-workshops/workshops/form-design-adam-silver).

Replace browser validation only with a complete accessible submission/error/focus/recovery flow. Prevent duplicate active requests without an unexplained validity gate.

## Refactoring UI, Adam Wathan and Steve Schoger

- Resolve the important feature, real content, layout, and hierarchy before decoration.
- Use consistent type, spacing, width, and color scales.
- Express importance through weight, contrast, placement, and spacing, not size alone; de-emphasize surroundings.
- Separate groups with space/surfaces before borders; use coherent elevation and shadows.
- Refine text measure, line height, alignment, and proportions for each content type.
- Design empty states, imagery, and details; check text contrast over actual images.

Source: [Book overview/contents](https://www.refactoringui.com/).

Visual tactics must preserve semantic HTML, persistent labels, accessible names, and contrast. Galleries suggest treatments, not this product's composition.
