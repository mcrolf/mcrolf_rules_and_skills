# WCAG 2.1 Level AA acceptance checks

Read sections relevant to changed UI, plus Verification. Target every applicable A/AA criterion in [WCAG 2.1](https://www.w3.org/TR/WCAG21/), including errata; this selective checklist does not replace normative requirements and exceptions.

Component checks establish component evidence. [Conformance](https://www.w3.org/TR/WCAG21/#conformance-reqs) requires full pages, complete processes, accessibility-supported technology, and non-interference. Scanner passes or sampled routes cannot establish product-wide conformance.

## Structure and comprehension

- Preserve meaningful DOM order and semantic headings, lists, landmarks, table headers, and relationships (1.3.1, 1.3.2).
- Give informative images, charts, and diagrams equivalent alternatives; decorative images get empty alternatives (1.1.1).
- Use descriptive titles, headings, labels, and link purpose; bypass repeated blocks and provide multiple page-finding methods where required (2.4.1, 2.4.2, 2.4.4, 2.4.5, 2.4.6).
- Set page/passage languages; keep repeated navigation and identification consistent (3.1.1, 3.1.2, 3.2.3, 3.2.4).
- Instructions cannot rely solely on shape, position, sound, or color (1.3.3, 1.4.1).

## Contrast and scalable presentation

- Measure rendered color pairs across backgrounds and interaction states: text **4.5:1**, large text **3:1**. Large means at least 18 pt/24 CSS px, or 14 pt bold/about 18.67 CSS px. Never round failures up. Inactive/incidental/logo exceptions do not exempt secondary text (1.4.3; [contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)).
- Essential control/state/graphic information, including custom focus indicators, needs **3:1** against adjacent colors, subject to exceptions; decorative borders need not qualify (1.4.11; [non-text contrast](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html)).
- Preserve content/functionality at **200%** text resize; enable browser zoom. Prefer real text over text images except where permitted (1.4.4, 1.4.5).
- Reflow vertically scrolling pages at **320 CSS px** width (1280 px viewport at **400% zoom**); horizontally scrolling content at 256 CSS px height. Avoid clipping/two-dimensional page scrolling; isolate genuine table/map exceptions (1.4.10; [reflow](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html)).
- Together override line height to **1.5**, paragraph spacing **2**, letter spacing **0.12**, and word spacing **0.16** times font size without losing content/functionality. These are tolerance tests, not default styles; language/script exceptions apply (1.4.12; [spacing](https://www.w3.org/WAI/WCAG21/Understanding/text-spacing.html)).
- Hover/focus content must remain dismissible where required, pointer-hoverable, and persistent until dismissal, trigger removal, or invalidation. Test entering tooltips and dismissing obstructions without moving focus (1.4.13; [hover/focus](https://www.w3.org/WAI/WCAG21/Understanding/content-on-hover-or-focus.html)).

## Keyboard, focus, and input

- Complete tasks by keyboard without timed keystrokes, except genuinely path-dependent functions; check Tab, Shift+Tab, Enter, Space, Escape, and widget arrow keys (2.1.1; [keyboard](https://www.w3.org/WAI/WCAG21/Understanding/keyboard.html)).
- Keep focus visible, ordered, and untrapped. Modals contain interaction, allow dismissal, and restore focus appropriately. Avoid positive `tabindex` (2.1.2, 2.4.3, 2.4.7).
- Single-character shortcuts must be disableable/remappable or active only within component focus (2.1.4).
- Offer simple single-pointer alternatives to multipoint/path-based gestures unless essential; allow cancellation, usually by activating on release (2.5.1, 2.5.2; [gestures](https://www.w3.org/WAI/WCAG21/Understanding/pointer-gestures.html)).
- Include visible label text in accessible names, preferably first, for speech input (2.5.3).
- Support both orientations unless one is essential; provide alternatives to motion activation and allow disabling it, except where exempt (1.3.4, 2.5.4).

## Forms and dynamic interfaces

- Associate persistent labels/instructions, required status, and formats with inputs; expose standardized personal-data input purposes, such as `autocomplete` tokens (1.3.5, 3.3.2).
- Identify errors/fields in text, suggest known corrections where appropriate, preserve entries, associate inline errors programmatically, and expose submission failures (3.3.1, 3.3.3; [errors](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)).
- Covered legal/financial actions and stored user-data changes/deletions need reversibility, checking/correction, or review/confirmation (3.3.4).
- Avoid unexpected context changes on focus/input; warn before input-triggered changes (3.2.1, 3.2.2).
- Expose correct names, roles, values, and synchronized expanded/checked/selected/disabled states (4.1.2).
- Announce qualifying counts, progress, success, and errors through appropriate status/live regions without moving focus or excessive repetition (4.1.3; [status](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html)).
- Preserve markup/ID associations. Errata considers 4.1.1 satisfied for HTML/XML; report resulting semantic/name/role/value failures under affected criteria ([parsing](https://www.w3.org/WAI/WCAG21/Understanding/parsing.html)).

## Media, timing, and flashing

- Provide applicable audio/video alternatives, prerecorded/live captions, and prerecorded audio descriptions. Transcripts cannot replace required description of visuals absent from the soundtrack (1.2.1 through 1.2.5; [captions](https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html)).
- Avoid autoplay audio; beyond three seconds, provide independent volume or pause/stop controls (1.4.2).
- Allow disabling/adjusting/extending time limits, except genuine exemptions. Warning/extension requires at least 20 seconds to respond and ten extensions (2.2.1; [timing](https://www.w3.org/WAI/WCAG21/Understanding/timing-adjustable.html)).
- Control automatic moving/blinking/scrolling and updating content alongside other content through pause/stop/hide or update frequency. The five-second threshold applies to moving/blinking/scrolling, not all updates (2.2.2).
- Avoid flashes; otherwise verify the three-flashes-or-below-threshold rule (2.3.1).

## Additional usability defaults, distinct from the AA baseline

- Prefer separated **44 by 44 CSS px** targets: 2.5.5 is 2.1 **AAA**, with exceptions, not AA ([targets](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html)). Apple's platform points are not interchangeable with CSS pixels.
- Respect `prefers-reduced-motion`; suppress unnecessary movement while preserving meaning. Interaction animation (2.3.3) is 2.1 **AAA**; timing/flashing requirements still apply.
- Keep focus clear of sticky overlays. Focus Not Obscured (2.4.11) and Target Size (Minimum) (2.5.8) are additional **WCAG 2.2** checks.

## Verification and evidence

1. Define affected routes, journeys, and states, including empty/loading/error/success, dialogs, and validation where present.
2. Run existing tooling such as axe on rendered states with WCAG 2.1 A/AA coverage; inspect manual-review items. [Automation alone is insufficient](https://www.w3.org/WAI/test-evaluate/tools/selecting/).
3. Complete journeys by keyboard, including bypass links, focus, dialogs, tooltips, validation/recovery, and custom widgets.
4. Measure rendered contrast; separately check reflow, 200% text resize, spacing overrides, supported themes, and relevant reduced-motion/touch operation.
5. Use an available screen reader/browser pairing to navigate headings/controls, complete the action, and hear errors/status. DOM/accessibility-tree inspection does not replace interaction testing.
6. Fix failures and repeat affected checks. Add focused regressions for fragile behavior, not static wording or CSS-value mirrors.
7. Report scope/states, commands/tools, browser/screen-reader pairing, results, unresolved barriers with criterion/correction, and checks **not run** with reasons. When tools are unavailable, do useful available checks without reporting omissions as passes. Failures or material coverage gaps preclude conformance claims.
