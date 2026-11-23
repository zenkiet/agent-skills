# Forms

## Contents
1. Layout: single column, labels on top
2. Fewer fields
3. Required and optional
4. Field width
5. Conventional field styles
6. Labels, hints, placeholders
7. Choosing the right control
8. Long forms: steps and groups
9. Field contrast
10. Validation
11. Field anatomy (summary)
12. Input techniques
13. Styling notes

---

## 1. Layout: single column, labels on top

- **One column.** Constant downward momentum, no "which field next?" decisions, fewer skipped fields, and
  magnifier users won't miss a second column.
- **Labels above inputs**, close to them. Left-side labels create a zig-zag between label and input
  (inconsistent gaps); right-aligned left labels fix the gap but create a ragged, hard-to-scan edge; long labels
  wrap badly. Top labels let the eye take label + field in one fixation.
- **Spacing that groups:** the label→input gap (8px) must be clearly smaller than the gap between field
  groups (24–32px); equal gaps make labels float between fields and invite wrong entries.
- **Stack checkboxes and radios vertically** — easier to scan, less mis-selection.
- Height concern: single column is taller, but the benefits outweigh it. Short, related fields may sit side by
  side *within* the column width (card expiry + CVC; first/last name only if short). If length hurts
  completion, split into steps.

## 2. Fewer fields

Every field costs completion rate, effort, error risk and build time. Ask only what's essential to deliver
the service now (a newsletter needs an email, not name + company).

## 3. Required and optional

- Default: **mark both**. Required: asterisk `*` (concise, familiar) or the word "required" (clearest, no
  legend needed). Optional: the word "(optional)". Don't colour the asterisk red (red = error).
- With asterisks, still add a one-line legend at the top ("Required fields are marked with an asterisk *") —
  but nothing breaks if people skip it.
- "All fields required unless marked optional" alone fails: instructions get skipped. Screen-reader users
  need required state anyway (`required`/`aria-required`), so mirror it visually.
- **Prefer opt-ins over optional fields**: "☐ Send me updates by SMS" → reveal a *required* mobile field only
  when ticked (progressive disclosure).
- You may leave required unmarked when: the product has no optional fields at all; tiny familiar forms
  (login, single-field subscribe); one-question-per-screen flows that explain each question; or testing shows
  it's fine.

## 4. Field width

Width signals expected input length. Don't make every field full width "for neatness": a 4-digit postcode
field should fit about 4 digits; CVC ~4; phone ~15; email/address wide. For variable input, size for the
common or longest-likely case.

## 5. Conventional field styles

Use rectangles with visible borders and labels above. Unconventional styles (label inside the field, no
borders, only an underline) make empty fields look filled and hide where to type. If you customise, keep the
**iconic parts**: the radio circle on the left (means "pick one"), the checkbox square (means "pick any"), the
input box. A big tappable "radio card" without the circle leaves people guessing whether it's single-select,
multi-select or a link.

## 6. Labels, hints, placeholders

- Always a short, visible, descriptive label above the field.
- Need more explanation? Add a **hint between the label and the field** (above, not below): people read it
  before typing ("At least 8 characters"), it keeps downward flow, and the area below fields gets covered by
  autofill dropdowns and on-screen keyboards. Don't hide critical hints in tooltips.
- **No placeholder as label**: it disappears on typing (memory load), makes fields look pre-filled (skipped),
  and placeholder grey is almost always below 4.5:1. Avoid placeholders generally.
- Exception: a lone search field may use placeholder text if it's ≥ 4.5:1 and the input has an accessible name
  (visually hidden label or `aria-label`).
- No instructional verbs in labels/hints ("Enter your email here") — the field implies it.

## 7. Choosing the right control

| Situation | Use | Why |
|---|---|---|
| ≤ ~10 options, pick one | **Radio buttons** (stacked) | One tap, all options visible and comparable. Use a dropdown only when space truly matters |
| Long list where the user knows the answer (country, product, article) | **Autocomplete** (predictive search) | Faster than scrolling; show ≤ ~10 suggestions; bold the part that differs |
| Long list the user must browse (occupation) | Split into 2 dependent selects (industry → occupation) | Smaller decisions |
| Small numeric quantity (guests, items) | **Stepper** with horizontal −/+ buttons ≥ 48px, typable value | E.g., 2 adults + 1 child + 1 infant: 4 taps vs 6 clicks + 3 scrolls with dropdowns. Don't use up/down chevrons (look like dropdown/accordion). Not for large changes |
| One on/off option applied **after submit** | **Checkbox** | Label describes what happens when checked |
| One on/off option applied **immediately** | **Toggle switch** | Label describes what happens when on (e.g., "Pay annually and save 10%" updating prices live) |
| Dropdowns in general | Last resort | Multiple precise interactions, options hidden, often skipped as "already filled", hard with motor impairments |

**Positive checkbox phrasing**: describe what happens when selected. Test: replace the tick with "yes" — if
the sentence becomes confusing ("Yes, don't send me emails"), rephrase ("Send me product updates").

## 8. Long forms: steps and groups

**Multi-step forms** reduce load, errors and abandonment:
- Say up front how long it takes and what people need to have ready.
- Group into a few steps of related questions (30 questions → ~6 steps of 5, not 30 screens).
- Easy questions first (early wins).
- Show progress (motivation rises near the end — goal-gradient).
- Review-and-edit step before submit; then a success screen saying what happens next.
- Primary "Next" left-aligned under the fields; tertiary "Back" top-left (see `buttons.md`).

If it must stay one page: **group related fields under headings** (Personal details / Address / Payment).

## 9. Field contrast

Input, checkbox, radio, toggle, stepper and button boundaries need **≥ 3:1** against the background (use
stroke-strong). Pale borders are one of the most common UI failures — invisible to low-vision users and in
sunlight. Rule of thumb: anything not purely decorative needs enough contrast to show what it is and how it
works.

## 10. Validation

People will make mistakes; validation tells them what's missing/wrong and how to fix it. Approaches (you can
mix per field):

| Approach | Pros | Cons | Use for |
|---|---|---|---|
| **On submit** | Simplest to build; no interruptions while filling | Errors discovered late, possibly many at once; user must hunt back with lost context; can't guide as you type | Default when time is short; short forms |
| **On blur** (after leaving a field, "inline") | Immediate feedback with context; can confirm correct input | Switching between filling and fixing; awkward for checkbox groups; more complex | Format-checkable fields (email, phone, postcode) |
| **As you type** (debounced) | Guides toward a valid answer (password rules, username availability) | Premature errors are annoying; typing speed varies; complex | Password strength/criteria, availability checks; also to *clear* an error as soon as it's fixed |

Rules whatever the approach:
- Put the error message **above the field** (just under the label/hint), not below — below gets covered by
  autofill/keyboards.
- Invalid field: red border (thicker) + light red background + error icon + text. Never colour alone.
- Multiple errors on submit: an **error summary at the top** with the count ("2 errors were found") and each
  error as a link that focuses the field; move focus to the summary.
- Messages state the fix ("Enter street address", "Enter a date in the past").
- Remove the error as soon as it's resolved (validate on input once an error is shown).
- Don't disable the submit button to prevent errors.
- Don't validate an empty field just because it received focus and lost it; wait for input or submit.

## 11. Field anatomy (summary)

Top to bottom, left-aligned, xs (8px) gaps inside the field group, m–l (24–32px) between field groups:

```
Label *                       ← text-strong, regular/bold, sentence case
Hint text (optional)          ← text-weak
⚠ Error message (if invalid)  ← text-error + icon
[ input                    ]  ← stroke-strong border (≥3:1); error: stroke-error, thicker, fill-error-weak bg
```
Markup and ARIA wiring: see `implementation.md`.

## 12. Input techniques

For Forgiving/Structured Format, Fill-in-the-Blanks, Autocompletion, Drop-down Chooser, List Builder, Password
Strength Meter and Good Defaults, see `patterns/input.md`.

## 13. Styling notes

- Inputs can read as slightly *inset* (subtle inner top shadow, `--shadow-inset`) — a natural depth cue that
  says "type here". Keep the border ≥ 3:1 regardless.
- Brand the checked state of native checkboxes/radios with `accent-color: var(--color-brand)` instead of
  rebuilding them; it keeps native accessibility and instantly looks more polished.
- Selectable cards are fine for important single choices, but keep the visible radio circle (see §5).
- Labels are always required for inputs; "labels are a last resort" (see `hierarchy.md`) applies only to
  *displaying* data, never to form fields.
