# Finishing touches

## Contents
1. Supercharge the defaults
2. Accent borders
3. Decorate backgrounds
4. Empty states
5. Use fewer borders
6. Think outside the box
7. Leveling up

---

## 1. Supercharge the defaults

Add flair by upgrading what's already there instead of adding new elements:
- **Bulleted lists → icons:** checkmarks or arrows generically, or content-specific icons (padlock for security
  features). Coloured icon in a soft circle works well.
- **Testimonials:** promote the quotation marks into a visual element — large and in a brand tint.
- **Links:** colour + heavier weight, or a thick colourful custom underline that partially overlaps the text.
- **Forms:** brand-coloured checked states (`accent-color: var(--color-brand)`) instead of browser defaults —
  often enough to go from boring to polished, while keeping native accessibility.

## 2. Accent borders

A no-talent-required way to add colour: a coloured bar
- across the top of a card,
- under/next to the active nav item,
- along the left side of an alert,
- as a short line under a headline,
- across the very top of the whole layout.
It's just a coloured rectangle, yet it makes things feel designed.

Colour rule: decorative bars use `--color-accent` (or a system colour on alerts), **not** the brand/action colour —
the brand colour is reserved for interactive elements. Exception: the active-nav indicator *is* interactive
state, so brand colour fits there.

## 3. Decorate backgrounds

When hierarchy, spacing and type are right but it still feels plain:
- **Change the background colour** of a panel to emphasise it, or of whole page sections to separate them; for more
  energy, a subtle gradient between **two hues no more than ~30° apart**.
- **Repeating pattern** (e.g., subtle SVG patterns), across the whole background or just along one edge. Keep
  pattern/background contrast low for readability.
- **A simple shape or illustration** in specific spots: geometric shapes, a chunk of a pattern, a simplified world
  map — again low contrast so it never interferes with content.

## 4. Empty states

Designers perfect the screen full of realistic sample data; users first see it empty. For features driven by user
content, the empty state is a priority:
- Add an image/illustration to grab attention and an emphasised call to action for the next step.
- Hide supporting UI that does nothing yet (tabs, filters, sort controls) until content exists.
- It's often the first interaction with a feature — make it interesting, not a blank table.

## 5. Use fewer borders

Borders separate things but too many make a UI busy. Alternatives:
- **Box shadow** — outlines more subtly; works best when the element's colour differs from the background.
- **Two background colours** — adjacent elements in slightly different shades are usually distinct enough; if you
  already have different backgrounds *and* a border, try removing the border.
- **Extra spacing** — the simplest separator; no new UI at all.

## 6. Think outside the box

Components don't have to look the way convention pictures them:
- **Dropdowns** are just floating boxes: sections, multiple columns, supporting text, colourful icons.
- **Tables:** combine related non-sortable columns into one cell with internal hierarchy (name bold + email grey);
  add images (avatars, thumbnails) and colour (status pills) to enrich data.
- **Radio buttons:** for an important choice, use selectable cards (keep a visible radio indicator).
Constraints are powerful, but a bit of freedom can take an interface up a level.

## Leveling up

- When you admire a design, ask "what did they do that I never would have?" — an inverted date-picker background, a
  button placed inside a text input, a two-colour headline.
- Rebuild favourite interfaces from scratch without peeking at dev tools; the differences teach tricks like tighter
  heading line-height, tracked-out uppercase and layered shadows.
