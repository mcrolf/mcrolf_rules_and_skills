# WCAG 2.1 Level AA acceptance checks

Read this reference when planning and verifying frontend changes. Target all applicable Level A and AA criteria in [WCAG 2.1](https://www.w3.org/TR/WCAG21/), including its errata. These working checks are deliberately selective; use the normative standard to resolve exceptions and requirements outside this list.

A component review establishes evidence about that component. A conformance claim requires evaluation of full pages, complete processes, accessibility-supported technology use, and non-interference, as described in [WCAG conformance requirements](https://www.w3.org/TR/WCAG21/#conformance-reqs). Do not turn a passing scanner result or a sampled route into a claim that the entire product conforms.

## Structure and comprehension

- Preserve meaningful reading and interaction order in the DOM. Use real headings, lists, landmarks, table headers, and relationships; visual position alone must not convey structure (1.3.1, 1.3.2).
- Give informative images useful alternatives and decorative images empty alternatives. Supply equivalent information for meaningful charts and diagrams (1.1.1).
- Use descriptive page titles, headings, labels, and link purpose. Provide a way to bypass repeated blocks, and multiple ways to locate pages where required (2.4.1, 2.4.2, 2.4.4, 2.4.5, 2.4.6).
- Set the page language and mark passages in another language where applicable (3.1.1, 3.1.2). Keep repeated navigation and component identification consistent (3.2.3, 3.2.4).
- Instructions must identify controls through more than shape, location, sound, or color alone (1.3.3, 1.4.1).

## Contrast and scalable presentation

- Measure actual foreground/background combinations, including overlays, images, gradients, focus, error, selected, and hover states. Normal text needs at least **4.5:1**; large text needs **3:1**. Large means at least 18 pt (24 CSS px), or 14 pt bold (approximately 18.67 CSS px). Do not round a failing ratio up to a pass. Apply the actual exceptions for inactive controls, incidental content, and logotypes, not a blanket exception for secondary text (1.4.3; [contrast guidance](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)).
- Essential visual information identifying controls, states, and meaningful graphics needs **3:1** against adjacent colors, subject to the criterion's exceptions. This does not require every decorative border to meet 3:1. Check custom focus indicators as well (1.4.11; [non-text contrast guidance](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html)).
- Support text resizing to **200%** without loss of content or functionality; keep browser zoom enabled. Prefer actual text over images of text except where permitted (1.4.4, 1.4.5).
- For vertically scrolling pages, verify reflow at **320 CSS px** width, equivalent to a 1280 CSS px viewport at **400% zoom**. Avoid two-dimensional page scrolling and clipped controls. Horizontally scrolling content has the corresponding 256 CSS px height requirement. Isolate genuinely two-dimensional content, such as a data table or map, rather than exempting the whole page (1.4.10; [reflow guidance](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html)).
- Apply these text-spacing overrides together and check for clipping or lost functionality: line height 1.5 times font size, paragraph spacing 2 times font size, letter spacing 0.12 times font size, and word spacing 0.16 times font size. These are override tolerance tests, not mandatory default typography. Account for language/script exceptions (1.4.12; [text-spacing guidance](https://www.w3.org/WAI/WCAG21/Understanding/text-spacing.html)).
- Hover/focus content must be dismissible where required, hoverable when pointer-triggered, and persistent until dismissal, trigger removal, or invalidation. Test moving the pointer onto a tooltip and dismissing obstructive content without moving focus (1.4.13; [hover/focus guidance](https://www.w3.org/WAI/WCAG21/Understanding/content-on-hover-or-focus.html)).

## Keyboard, focus, and input

- Complete every task using the keyboard, without pointer input or timed keystrokes, except genuinely path-dependent underlying functions. Verify Tab, Shift+Tab, Enter, Space, Escape, and widget-specific arrow keys as appropriate (2.1.1; [keyboard guidance](https://www.w3.org/WAI/WCAG21/Understanding/keyboard.html)).
- Keep focus visible, order it meaningfully, and avoid traps. A modal contains interaction while open and allows dismissal through its intended controls; return focus appropriately afterward. Do not use positive `tabindex` to repair a confusing DOM order (2.1.2, 2.4.3, 2.4.7).
- For single-character shortcuts, provide a way to disable/remap them or activate them only while the relevant component has focus (2.1.4).
- Offer simple single-pointer alternatives to multipoint/path-based gestures unless essential. Use cancellable pointer actions, usually activation on release, rather than committing actions on press (2.5.1, 2.5.2; [gesture guidance](https://www.w3.org/WAI/WCAG21/Understanding/pointer-gestures.html)).
- Keep visible label text in the accessible name, preferably at its start, so speech users can invoke the control (2.5.3).
- Support both orientations unless one is essential. If device/user motion operates the UI, provide a conventional control alternative and allow disabling motion activation except where exempt (1.3.4, 2.5.4).

## Forms and dynamic interfaces

- Associate inputs with persistent labels and instructions; identify required fields and expected formats. For supported fields collecting the user's information, expose the appropriate standardized input purpose, such as `autocomplete` tokens (1.3.5, 3.3.2).
- Describe detected errors in text and identify the affected field. Suggest corrections when known and appropriate. Preserve useful entered values; associate inline errors programmatically and make submission failures discoverable (3.3.1, 3.3.3; [error guidance](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html)).
- For covered legal commitments, financial transactions, and changes/deletion of user-controlled stored data, provide reversibility, input checking with correction, or review and confirmation as required (3.3.4).
- Do not unexpectedly change context merely on focus or input. Warn users before input changes trigger such behavior (3.2.1, 3.2.2).
- Expose correct accessible names, roles, values, and states. Keep expanded, checked, selected, and disabled states synchronized with behavior (4.1.2).
- Announce qualifying result counts, waiting/progress updates, success, and errors without requiring focus to move to the message. Choose appropriate status/live-region semantics and avoid duplicate or excessively chatty announcements (4.1.3; [status-message guidance](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html)).
- Keep markup and ID associations correct. Current WCAG 2.1 errata considers 4.1.1 always satisfied for HTML/XML; report resulting semantic or name/role/value failures under the affected criteria instead of inventing a separate parsing failure ([parsing clarification](https://www.w3.org/WAI/WCAG21/Understanding/parsing.html)).

## Media, timing, and flashing

- Check applicable prerecorded audio/video alternatives, synchronized captions, live synchronized captions, and prerecorded audio descriptions. A transcript alone does not satisfy the AA requirement for audio description when relevant visual information is missing from the soundtrack (1.2.1 through 1.2.5; [caption guidance](https://www.w3.org/WAI/WCAG21/Understanding/captions-prerecorded.html)).
- Avoid autoplay audio. If audio plays automatically for more than three seconds, provide the required independent volume or pause/stop control (1.4.2).
- Let people disable, adjust, or extend content-imposed time limits using a method satisfying the criterion; apply only genuine exceptions. If using the warning/extension method, allow at least 20 seconds to respond and at least ten extensions (2.2.1; [timing guidance](https://www.w3.org/WAI/WCAG21/Understanding/timing-adjustable.html)).
- Provide the required pause/stop/hide or update-frequency controls for automatically moving, blinking, scrolling, or updating content alongside other content. The five-second threshold applies to moving/blinking/scrolling content, not all auto-updates (2.2.2).
- Avoid flashing content. If present, verify the three-flashes or below-threshold rule rather than assuming an animation is safe (2.3.1).

## Additional usability defaults, distinct from the AA baseline

- Prefer touch targets around **44 by 44 CSS px** with enough separation. WCAG 2.1 target size (2.5.5) is **AAA**, with exceptions, not a 2.1 AA minimum ([target-size guidance](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html)). Apple uses platform-specific point units; do not silently equate its metrics to CSS pixels.
- Respect `prefers-reduced-motion`, suppress unnecessary parallax/large movement, and keep state changes understandable without animation. Animation from interactions (2.3.3) is **AAA** in WCAG 2.1; motion reduction is an additional design practice, while applicable timing/flashing criteria remain A requirements.
- Keep focused controls clear of sticky overlays. WCAG 2.2 criteria such as Focus Not Obscured (2.4.11) and Target Size (Minimum) (2.5.8) are useful additional checks; do not label them WCAG 2.1 AA criteria.

## Verification and evidence

1. Define the changed routes, components, states, and complete user journeys to exercise. Include empty, loading, error, success, open-dialog, and validation states when present; a default-state screenshot is insufficient.
2. Run the project's existing automated accessibility tooling, or an available equivalent such as axe, against rendered UI states. Enable the applicable WCAG 2.1 A/AA rule coverage and inspect items requiring manual review. Reuse established commands and dependencies where possible. [W3C explains the limits of automated tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/).
3. Manually complete the changed journey with keyboard input. Check focus, bypass links, dialogs, tooltips, form submission/recovery, and any custom widget interaction.
4. Measure contrast using rendered colors. Check narrow/reflow and 200% text resize separately, apply text-spacing overrides, and inspect changed states in supported themes. Check reduced motion and touch operation where relevant.
5. With an available screen reader/browser combination, navigate headings and controls, complete the main action, trigger validation, and listen for status updates. Record the actual combination used. A DOM or accessibility-tree inspection helps diagnose problems but does not replace a screen-reader interaction check.
6. Fix discovered failures in scope, then repeat the affected checks. Add focused regression coverage for fragile behavior such as lost dialog focus or unannounced validation; do not create tests that merely repeat CSS values or static wording.
7. Report tested scope, commands/tools and their results, manual checks performed, unresolved failures, and checks **not run**, with the reason. If a scanner, browser, or screen reader is unavailable, state that limitation and perform useful available checks. Do not report missing checks as passes, and do not claim conformance while applicable failures or material coverage gaps remain.
