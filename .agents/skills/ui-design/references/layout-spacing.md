# Layout and spacing

## Contents
1. Grouping
2. Spacing and sizing scale
3. Avoid ambiguous spacing
4. White space
5. Units
6. Widths: don't fill the screen
7. Grids, fixed widths and max-widths
8. Responsive sizing
9. Alignment
10. Placement and Fitts's Law
11. Unbreakable layouts

---

## 1. Grouping

Four cues, strongest to subtlest:
1. **Same container** (common region) — border, background or shadow. Page structure and components (cards,
   dialogs). Use it when spacing alone is ambiguous (variable-length card text makes the author line drift
   toward the next card).
2. **Proximity** — related things close, unrelated far apart.
3. **Similarity** — same size/shape/colour = same kind; one slightly different item stands out (recommended plan).
4. **Continuity** — items on one line/list read as a set.

Don't box everything: when proximity + similarity + continuity already group items (table rows, nav links),
remove the outer container. **Look alike ⇒ work alike:** non-interactive icons styled like buttons or badges
styled like the primary button get clicked — give badges a pill shape, non-action colour and lower prominence.

## 2. Spacing and sizing scale

- Relative difference matters: 12→16px is +33% (big for padding/icons), 500→520px is +4% (invisible). Keep
  adjacent steps ≥ ~25% apart, tight at the small end and wide at the large end:
  `4 8 12 16 24 32 48 64 96 128 192 256 384 512 640 768` px (`--space-1` … `--space-16`).
- Aliases for common jobs: `--space-xs` 8 (label→input, icon→text), `--space-s` 16 (inside components, between
  buttons), `--space-m` 24 (component padding), `--space-l` 32 (between cards/columns), `--space-xl` 48
  (between blocks), `--space-2xl` 64 (desktop page margin), `--space-3xl` 96 (desktop section padding).
- Use the same scale for **sizes** (icon boxes, avatars, widths). Not enough? The next step up is usually right.
- **Apply innermost first:** break the layout into nested rectangles (margin / border / padding); smallest gaps
  inside, growing outward. One value everywhere flattens grouping.
- Write spacing rules down (cards = m padding, columns = l gaps, sections = 3xl vertical padding).

## 3. Avoid ambiguous spacing

Without separators, **space around a group must exceed space within it**:
- Forms: label→input gap smaller than field→field gap.
- Articles: more space above a heading than below it.
- Lists: extra space between multi-line bullets.
- Horizontal groups: bigger gaps between pairs than within them.

## 4. White space

Start with too much and remove until it looks right; "a bit much" on one element becomes "just enough" in the
full UI. When unsure, go a step bigger. Generous space makes groups and hierarchy legible and looks calmer. Dense
layouts (dashboards, admin tables) are fine as a deliberate choice.

## 5. Units

Design at @1x in points (≈ CSS px). Never in device pixels.

## 6. Widths: don't fill the screen

- If something needs 600px, give it 600px; over-wide layouts are harder to read. Sections needn't be full-width
  because the nav is.
- **Mobile first** (~400px), then enlarge and fix only what felt compromised.
- **Columns instead of stretching:** a lonely narrow form gets a side column (help text, summary).
- Don't cram either: if something needs space, give it.

## 7. Grids, fixed widths and max-widths

- Use a 12-column grid for the **main layout** (12 desktop → 8 tablet → 4 mobile; gutters 32/24/16; margins
  64/32/16). Gutters stay empty; small elements inside containers use the spacing scale, not the grid.
- **Not everything should be fluid:** a 25% sidebar wastes space when wide and breaks when narrow → fixed width
  (`--sidebar-width`), fluid main area with its own grid.
- **Don't shrink until you must:** a "6 of 12 columns" card can be narrower on large screens than on medium
  ones → `width: 100%; max-width: <ideal>`.

## 8. Responsive sizing

- Relationships change across breakpoints: a 2.5em headline (45px over 18px body) becomes 35px over 14px mobile
  body — too big; 20–24px is right. Big things shrink faster; set sizes per breakpoint from the scales, not as em
  multiples.
- Within components: larger buttons get disproportionately more padding, smaller ones tighter padding.

## 9. Alignment

- Left-align text and keep a straight left edge (icons shouldn't break it). Centre only short blocks.
- One alignment per component (mixed centre/left/right makes the eye zig-zag); one outlier is OK.
- Baseline-align different sizes on one line; right-align numbers in tables.

## 10. Placement and Fitts's Law

Actions next to what they affect; close button where the open button was; menu items start at the top, are
large and show their full hit area; primary CTA bottom and full-width on mobile; left-aligned actions are less
likely to be missed. Small savings add up on repeated tasks.

## 11. Unbreakable layouts

Design with extreme data: long names/translations, huge numbers, many items, zero items. Let components wrap and
reflow; avoid hiding overflow that may hold key info; truncate in the middle when items share a prefix and show
the full value on hover/focus.
