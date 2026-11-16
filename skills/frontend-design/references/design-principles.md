# Design principles in practice

Read relevant sections only. These are original working interpretations in our own words, drawn from public primary sources or a user-supplied copy, not reproductions of the books. Verify current platform and component details when needed.

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

## A Dictionary of Color Combinations, Sanzo Wada

Use these concepts from the book's usage chapter when choosing or reviewing a palette. The book is a catalog of 348 combinations; you do not need it to apply them.

- **Choose a combination, not a single color.** Build the palette as a set of 2, 3, or 4 colors chosen to work together, with neutrals counted as members. A brand hue plus framework defaults is not a combination. Add colors only when the UI needs another role.
- **Decide the harmony on purpose.** *Same-tone* harmony pairs colors of similar lightness and strength (all light, all dark, all pale, or all deep). It is easy to get right and reads calm. *Contrasting-tone* harmony joins different tones; it is harder and more interesting, so it needs a product reason. *Pan-tone* mixes light, dark, pale, and deep freely and is hardest to control. Name which one the UI uses.
- **One family can carry a whole UI.** Shades of one hue family at different lightness stay harmonious, the way a pale-blue coat, an indigo kimono, and a blue-tinted sash work together. This suits dense, task-heavy screens.
- **Never use colors in equal amounts.** The book shows swatches at equal size only for comparison and warns that equal areas are rare and usually wrong in practice. Assign a dominant color (backgrounds, large surfaces), a secondary color, and an accent used sparingly (primary action, focus, selection). The accent is the smallest area and the strongest signal.
- **Judge color at its real size.** A color covering a large area reads differently from a small chip; the book notes large areas look paler and weaker than the swatch. Check colors at real size in the rendered UI, not in a token list or small palette preview.
- **Match temperature.** Every hue has warm and cool versions (a yellow-green is warm, a blue-green is cool; some yellows read cool). Keep temperatures consistent across neutrals and accents, or contrast them deliberately. Warm grays beside cool blues look accidental.
- **Treat the surface as part of the combination.** The book tests each combination against the white page, and the same dye looks different on silk, cotton, and linen. On screens, the background, light and dark themes, images, and elevation surfaces change how a color reads. Test the palette on each surface it appears on, and treat white or the base background as one of its colors.

Combine with [contrast requirements](accessibility.md#contrast-and-scalable-presentation): harmony never excuses text, focus, or control contrast below WCAG AA, and color is never the only signal.

Source: Sanzo Wada, *Haishoku Sōkan* (1933 to 1934), published as *A Dictionary of Color Combinations* (Seigensha). [Archive.org record](https://archive.org/details/dictionaryofcolo0000vari).
