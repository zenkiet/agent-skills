# Review, audit and refactor

## Contents
1. Audit procedure
2. Refactor pass order (biggest impact first)
3. Severity rubric
4. Checklist
5. Audit report template
6. Symptom → fix catalogue
7. Polish report template

---

Use for auditing (screenshots, Figma frames, live pages, frontend code) **and** for polishing ("make it look
better", "clean up", "modernise"). Audits rank problems by severity; refactors apply fixes in pass order.

## Audit procedure

1. **Understand the screen's job.** What's the user's main task here? What's the single most important
   action? (If you can't tell, that's finding #1.)
2. **Squint test.** Blur/zoom out mentally: is the primary action and main content obvious? Do groups read as
   groups?
3. **Category passes** using the checklist below. For code, read the actual values (colours, spacing, font
   sizes, ARIA) rather than guessing; compute contrast with `python scripts/palette.py check <fg> <bg>`.
4. **Rank findings by severity**, merge duplicates, and propose concrete fixes (token names, values, rewritten
   copy, component swaps). Max ~10–15 findings; group minor nits.
5. Note what already works (briefly) so it isn't "fixed" away.

## Refactor pass order (biggest impact first)

1. **Hierarchy** — find the one primary thing; demote everything else (weight/colour before size).
2. **Spacing** — add generous space, then remove; snap to the scale; fix ambiguous groupings.
3. **Layout widths** — max-widths, fixed sidebars, constrained paragraphs, columns instead of stretching.
4. **Typography** — scale sizes, 2 weights, line-height by size/length, baseline alignment, tracking.
5. **Colour** — palette shades only; primary on actions; flipped-contrast tints for badges/alerts; tinted greys.
6. **Depth** — elevation-appropriate shadows, raised/inset cues, lighter = closer, fewer borders.
7. **Images** — consistent text contrast, intended icon sizes, contained user images.
8. **Finishing touches** — accent borders, supercharged defaults, background decoration, empty states.
Re-check contrast (≥ 4.5:1 text, ≥ 3:1 large text & controls) after colour changes.


## Severity rubric

| Severity | Meaning | Typical examples |
|---|---|---|
| **Critical** | Blocks a task or fails accessibility for a group of users (WCAG AA failure on essential content) | Text < 4.5:1, input borders < 3:1, colour-only errors/links, placeholder used as the only label, no focus indicator, disabled submit with no explanation, targets far below 44px, destructive action with no confirmation/undo |
| **High** | Likely to cause errors, confusion or noticeable slowdown | Multiple primary buttons, non-interactive elements styled as interactive (coloured headings, button-like badges), hidden key actions, dropdown for 3 options, multi-column form, hints below fields, generic "Learn more"/"OK" labels, right-aligned buttons missed on wide layouts |
| **Medium** | Hurts scannability/consistency/aesthetics; adds cognitive load | Flat hierarchy, inconsistent spacing not from a scale, mixed alignments, >2 font weights or multiple typefaces, long line length, body < 16–18px, line-height < 1.5, title case, inconsistent vocabulary |
| **Low** | Polish | Full stops on fragments, uneven text lengths across cards, unbalanced icon/text weight, untightened large headings, photo composition |

## Checklist

### Hierarchy and simplicity
- [ ] One clear most-important element and one primary action per view.
- [ ] Content ordered by importance (top/first = most important); important sections visually stronger.
- [ ] No unnecessary decoration, repeated text, extra containers or competing icons.
- [ ] Important actions visible (not buried in "⋯" when space exists); hidden content discoverable.
- [ ] Minimal but not vague: icons labelled, selected states obvious.

### Colour and contrast
- [ ] Text ≥ 4.5:1 (large ≥ 3:1) on its actual background (including fills, photos, hover states).
- [ ] Control boundaries, meaningful icons, focus rings ≥ 3:1.
- [ ] Colour never the only signal (links underlined, errors with icon/text, status labelled).
- [ ] Brand/action colour only on interactive elements; system colours only for status; one interactive colour.
- [ ] No pure black text on white; no light grey body text; dark mode checked with APCA, no pure black bg.
- [ ] Colours come from a role-based palette/tokens, not ad-hoc hex values.

### Layout and spacing
- [ ] Related items closer than unrelated; spacing values from the scale (8/16/24/32/48/80); inner < outer.
- [ ] Grouping via proximity/similarity/continuity before boxes; containers only where needed.
- [ ] Look-alike elements behave alike; different behaviour looks different.
- [ ] Main layout on a grid; single alignment per component; straight left edges; baseline alignment.
- [ ] Generous white space; nothing cramped under the squint test.
- [ ] Handles long strings, large numbers, empty and error states, narrow screens, 200% zoom.

### Typography
- [ ] One sans serif (optional second for headings only); regular + bold only.
- [ ] Sizes from a type scale; long body ≥ 18px; line-height ≥ 1.5 for body, tighter for headings.
- [ ] 40–80 characters per line; left-aligned; no justified body; centre only short text.
- [ ] Text on images has an overlay/scrim and passes contrast.

### Copy
- [ ] Sentence case; concise; plain words; no jargon/abbreviations; numerals.
- [ ] Front-loaded headings, links, buttons; descriptive headings that work out of context.
- [ ] Buttons = verb + noun; links name their destination (no "click here"/"learn more").
- [ ] Error messages: what happened + how to fix; no blame, no "oops".
- [ ] Consistent vocabulary; no "my" in labels; no all-caps beyond short labels.

### Buttons and actions
- [ ] Primary / secondary / tertiary distinguishable without colour; ≤ 1 primary.
- [ ] Buttons left-aligned in priority order (stacked full-width on mobile); multi-step "Back" top-left tertiary.
- [ ] Hit areas ≥ 48px; ≥ 8–16px between targets; small controls have extended hit areas.
- [ ] Disabled buttons avoided or explained (message/tooltip, still focusable).
- [ ] Destructive actions: low prominence trigger, friction proportional to severity, undo where possible.

### Forms
- [ ] Single column; labels above and close; radios/checkboxes stacked.
- [ ] Only essential fields; opt-ins instead of optional fields where possible.
- [ ] Required (*) and optional marked; field widths match expected input.
- [ ] Hints above fields; no placeholder-as-label.
- [ ] Right control: radios ≤ 10 options, autocomplete for long known lists, steppers for small numbers,
      checkbox (on submit) vs toggle (immediate); positive checkbox phrasing.
- [ ] Long forms split into steps with progress, or grouped under headings.
- [ ] Validation: errors above fields, colour + icon + text, summary with links on submit, errors clear when fixed.

### Structure, navigation and interaction
- [ ] Screen type and patterns fit the job (`patterns/index.md`); conventional patterns preferred.
- [ ] Users can tell where they are (titles, selected nav, breadcrumbs, progress) and get back (Back works,
      escape hatches in modals/wizards/dead ends).
- [ ] Navigation is broad and shallow; frequent destinations are one step away; deep links restore state.
- [ ] Lists use an appropriate list/detail pattern; long lists have search/filter and pagination or load-more.
- [ ] Costly actions get Preview or confirmation; reversible ones get Undo; long operations show progress and Cancel.
- [ ] Defaults and autocompletion reduce typing; inputs accept forgiving formats.

### States and accessibility
- [ ] Hover, pressed, focus-visible, disabled/selected states exist and are distinct.
- [ ] Keyboard: everything reachable and operable, logical order, visible focus.
- [ ] Semantics (code): real `<button>`/`<a>`, labelled inputs, `aria-describedby` for hints/errors,
      `aria-invalid`, headings in order, alt text, `prefers-reduced-motion` respected.
- [ ] Platform conventions respected (iOS/Android/web) unless they fail accessibility.

## Audit report template

```
## Summary
<1–3 sentences: what the screen is for, overall verdict, top 3 issues>

## Findings
### Critical
1. <Issue> — <where>
   Rule: <rule name> · Why: <impact on which users/task>
   Fix: <concrete change: token/value/component/copy>

### High
...
### Medium
...
### Low (grouped)
- ...

## What works
- <brief>

## Suggested next step
<e.g., apply fixes 1–5, then re-run contrast check / squint test>
```

When fixing code directly instead of reporting, apply Critical and High fixes first, keep changes inside the
existing design system's tokens, and list what changed and why in the same rule/why/fix format.

## Symptom → fix catalogue

| Symptom | Likely cause | Tactic / fix |
|---|---|---|
| Everything looks equally important; "wall of content" | No deliberate hierarchy | Pick the primary element; secondary → grey (`--color-text-weak`), tertiary → lighter grey; 2 weights; remove competing colour |
| Headings huge, metadata tiny | Size doing all the work | Reduce size gap; use bold for primary, softer colour for secondary at readable size |
| Important element won't stand out | Competitors too loud | De-emphasise neighbours (inactive nav softer, sidebar bg removed) |
| Data screen looks like a form printout | `Label: value` everywhere | Drop labels where format/context suffices; merge ("3 bedrooms"); de-emphasise remaining labels |
| Page titles shout | Styled by h1 default | Size titles for their role; content is the focus |
| Icons dominate text | Heavy icons at full contrast | Softer icon colour (`--color-icon`) |
| Light borders invisible, dark ones harsh | Contrast vs weight | 2px border in a soft colour |
| Too many coloured buttons | Styled by semantics | Primary solid / secondary outline or tint / tertiary link; destructive stays quiet until the confirm step |
| Feels cramped | Minimum spacing | Double the spacing, then trim; inner < outer spacing |
| Spacing feels random | Off-scale values | Snap to the spacing scale (4/8/12/16/24/32/48/64…) |
| Labels float between fields; headings belong to the wrong section | Ambiguous spacing | More space between groups/above headings than within |
| Stretched across wide screens | Filling the canvas | `max-width` per element; paragraphs ≤ 65ch; split into columns |
| Sidebar too wide/narrow at some sizes | Percentage widths | Fixed sidebar width, fluid main area |
| Card narrower on large screens than medium | Grid-column sizing | `width: 100%; max-width: <ideal>` |
| Mobile headings enormous | em-relative sizes | Per-breakpoint sizes from the scale; big things shrink faster |
| Buttons look zoomed rather than sized | Padding as % of font size | Larger buttons: more generous padding; small: tighter |
| Too many font sizes/weights | No type system | Map everything to the type scale; regular + bold only (no < 400) |
| Paragraphs hard to read | Long lines / flat leading | 45–75ch; leading 1.5–2 depending on width; headings ~1–1.25 |
| Mixed-size text on a row looks misaligned | Centre alignment | `align-items: baseline` |
| Numbers hard to compare | Left-aligned, proportional digits | Right-align, `font-variant-numeric: tabular-nums` |
| Nav full of blue underlined links | Paragraph link style everywhere | Weight/darker colour for UI links; hover underline for ancillary ones |
| Uppercase labels look cramped | Default tracking | `letter-spacing: 0.05em` |
| Headline in text font looks loose | Text-family spacing | `letter-spacing: -0.025em` on large headings |
| Colours look like a "5-colour generator" site | Too few shades | Build 9-shade scales for greys, primary, accents (`scripts/palette.py shades` / `tokens`) |
| Light/dark variants look washed-out or muddy | Lightness killed saturation; no hue shift | Boost saturation away from L 50%; rotate hue ≤ 20–30° |
| Greys feel lifeless or clash with brand | Pure neutral greys | Tint greys cool or warm, saturating the edges more |
| Grey text on coloured panel looks dirty | Grey on colour | Hand-pick same-hue lighter/darker tint |
| Coloured badge/alert too loud | White on dark colour | Flip: dark shade text on 100 tint |
| Status shown only by red/green | Colour-only meaning | Add icons/arrows; vary lightness in charts |
| UI looks flat and dated | No depth cues | Elevation shadows, top highlight on buttons, inset wells, lighter cards on off-white page, overlap layers |
| Shadows look fake/muddy | One-part, wrong size | Two-part shadows; elevation-appropriate; light from above |
| Busy grid of boxes | Too many borders | Replace with shadow, background shade or spacing |
| Hero text unreadable | Dynamic photo | Overlay, lower contrast, colorize, or glow text-shadow |
| Feature icons look chunky | Scaled-up small icons | Small icon inside a tinted shape |
| Screenshot unreadable | Scaled-down full screenshot | Smaller layout capture, partial crop, or simplified illustration |
| Avatars/thumbnails break layout or bleed | Raw user images | Fixed-ratio `object-fit: cover`; inner shadow/translucent inner border |
| Looks correct but plain | No finishing touches | Accent border, icon bullets, styled quotes, decorated section bg, custom checkbox colour |
| New feature looks broken on first use | Empty state ignored | Illustration + primary CTA; hide tabs/filters until content exists |

## Polish report template

```
## Verdict
<1–2 sentences: what works, the 3 changes with the biggest visual payoff>

## Changes (in pass order)
1. [Hierarchy] <symptom> → <tactic>. Change: <CSS/token/value>
2. [Spacing] ...

## Optional polish
- <finishing touches>
```
When editing code directly: fix Critical/High accessibility issues first, then apply refactor passes in order,
stay inside the token system, and summarise what changed and why.
