# Buttons

## Contents
1. Three button weights
2. Common button mistakes (avoid)
3. Button rules summary
4. Primary / secondary / tertiary usage
5. Avoid disabled buttons — alternatives
6. Alignment and order
7. Labels
8. Target size and spacing
9. Icon + text balance
10. Destructive actions: graded friction + undo
11. Visual polish for buttons

---

## 1. Three button weights

| Weight | Safe default style | Use |
|---|---|---|
| **Primary** | Rounded rectangle, solid brand fill, white (on-brand) text | The single most important action in the view |
| **Secondary** | Rounded rectangle, transparent fill **or** a light brand tint (`--color-brand-weak`), always with a brand-colour border (≥ 3:1) and brand text | Alternatives; several actions of equal importance |
| **Tertiary** | No container; **underlined** text in brand colour (or `--color-text-weak` for very low-priority actions) | Least important, many actions, destructive actions you want quiet, "Back" |

Their hierarchy doesn't depend on colour alone (fill vs outline vs underline), which is the point. Add size
variants (small/large) only if the product needs them. All three share shape and radius — same function,
same form.

## 2. Common button mistakes (avoid)

- Secondary button with a light grey fill or light grey outline → reads as **disabled**; text often < 4.5:1.
- Secondary button defined only by a pale tinted fill < 3:1 against the background → shape invisible to low
  vision users; it's just coloured text. Add a ≥ 3:1 border.
- Primary and secondary with the **same style in different colours** → hierarchy unclear, indistinguishable
  for colour-blind users, often < 3:1 between them.
- Two filled buttons of similar weight → competing actions.
- Tertiary as coloured text **without underline** → colour is the only cue of interactivity.
- Tertiary with a faint outline < 3:1 → border doesn't identify it.
- Primary and secondary with **different shapes/radii** for no functional reason → implies different
  behaviour.
- Similar visual weight across all three → no hierarchy.

## 3. Button rules summary

- Hierarchy is visible without colour.
- Button shape/boundary ≥ 3:1 against its background; button text ≥ 4.5:1 against the button fill.
- If two buttons share a style, they must differ by ≥ 3:1 from each other.
- Hit area ≥ 48×48px; ≥ 16px between adjacent buttons (8px absolute minimum).

## 4. Primary / secondary / tertiary usage

- **One primary per view.** Several primaries say "everything is most important", so nothing is. If no single
  action dominates (e.g., a list of items each with "View"), use secondary or tertiary for all of them.
- **Secondary for equal choices.** When the user's choice should be unbiased (e.g., "Report as junk" vs "Not
  junk"), give both secondary styling — don't nudge with a primary.
- **Tertiary** to keep many or risky actions quiet: e.g., "Remove" on each row of an editors list, so the
  primary "Send invite" stays dominant.

## 5. Avoid disabled buttons — alternatives

Why disabled buttons hurt: no explanation of why (people get stuck), low contrast (hard to see), usually not
keyboard-focusable (keyboard/screen-reader users can't discover them).

Alternatives, in order of preference:
1. **Keep submit enabled and validate on submit** — the user who skipped a field instantly sees which one.
2. **Remove unavailable actions** and say why ("Request to follow this person to see their work and contact
   them" instead of greyed-out "Message" / "Hire" buttons).
3. **Lock icon** on a normal-contrast button for gated/premium features, plus a message about how to unlock
   (shown nearby or on press).
4. If you must disable: add a visible message nearby explaining what's needed ("Fill out all fields to
   register"), add a tooltip on hover/focus, and keep it focusable (`aria-disabled="true"` instead of the
   `disabled` attribute, and block the action in code).

## 6. Alignment and order

- **Left-align buttons, ordered left → right from most to least important** (primary first). Reasons: LTR
  F-pattern scanning hugs the left edge; right-aligned buttons are missed on wide screens and by magnifier
  users; the action most people need gets the shortest path.
- **Mobile:** stack vertically, most important on top, full-width (reachable with either thumb).
- **Small dialogs:** left alignment keeps the product consistent; right alignment (OS convention, "forward"
  momentum) is acceptable if the product is consistent and hierarchy is clear. Pick one and keep it.
- **Multi-step forms:** don't put "Back" in the bottom-left with "Next" far right — people hit Back by
  accident and lose input, and Next drifts far from the fields. Keep the primary "Next/Continue" left-aligned
  under the fields; put a tertiary "Back" at the **top-left** (where back lives in browsers, apps and
  breadcrumbs).
- **Exception:** single-field forms (search, newsletter email) attach the primary button to the right of the
  field — saves space and binds the action to the field.

## 7. Labels

Verb + noun describing the outcome ("Save post", "Delete account", "Start workout") — never "OK"/"Yes" when a
specific label is possible. Must make sense out of context. Sentence case. See `copywriting.md`.

## 8. Target size and spacing

- ≥ 48×48px (aligns to the 8pt grid, above WCAG's 44); make frequent actions bigger.
- ≥ 8px between targets (16px between buttons is safer).
- Small icons/controls: **extend the hit area beyond the visible bounds** (padding or a pseudo-element), and
  where possible **show** the hit area (row background/border) so people don't aim precisely.
- Stepper arrows that are tiny and stacked vertically are a classic failure → large horizontal −/+ buttons.

## 9. Icon + text balance

Pair icons and text with similar visual weight: match stroke thickness to the font weight, match icon size to
text size (roughly cap-height to line-height). If the icon is still heavier, lower its contrast (icon in
stroke-strong, text in text-weak). Use one icon style throughout (all outlined, consistent stroke width) —
mixing filled and outlined suggests filled = selected.

## 10. Destructive actions: graded friction + undo

Destructive = harmful or irreversible. Add friction proportional to severity:

| Level | Technique | Example |
|---|---|---|
| Initial | Make the action less prominent, farther away, or behind disclosure. **Don't** make the trigger red (that makes it louder) | "Delete" as a tertiary link inside a menu |
| Light | Confirmation dialog | "Delete message?" [Delete message] [Cancel] |
| Moderate | Confirmation with red emphasis and consequence stated | "Delete article? You won't be able to recover it." red [Delete article] |
| Heavy | Red + explicit confirmation checkbox (or typing a name) required before the button works | "Delete account? Your profile and all articles will be permanently deleted." ☐ I confirm I want to delete my account |

Best of all: **allow undo** (soft delete + "Message deleted · Restore message" toast). More engineering, far
less risk — mistakes happen even with friction.

## 11. Visual polish for buttons

- **Style by place in the hierarchy, not by meaning.** Most pages have one primary action, a couple of
  secondary ones and a few rarely used tertiary ones; a page where every action is a filled coloured button is
  noisy and unclear.
- **Raised primary:** a hand-picked lighter top edge (`inset 0 1px 0` in a lighter shade of the same hue —
  not semi-transparent white, which drains saturation) plus `--shadow-raised`. On press, drop to no shadow
  (and optionally 1px down) so it feels pushed in.
- **Size variants scale independently:** large buttons get disproportionately more padding, small buttons
  tighter padding — not a zoomed copy of the medium one. Don't derive padding from font size in em.
- **Buttons vs look-alikes:** badges/chips use a pill shape, non-action colours and lower prominence so they're
  never mistaken for buttons.
