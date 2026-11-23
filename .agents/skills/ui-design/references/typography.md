# Typography

## Contents
1. Typeface
2. Optional heading typeface
3. Weights
4. Type scale
5. Body size
6. Line height
7. Line length
8. Alignment
9. Letter spacing
10. Links
11. Text colour

---

## 1. Typeface

Default to **one neutral sans serif** for the UI — legible at all sizes, neutral to any brand, simple. Safe
choices: a popular, proven family (e.g., Inter) or the system stack (familiar, zero load). Choosing:
- Many weights (≥ 5; filter directories by 10+ styles incl. italics) usually signals quality.
- Large x-height and slightly open spacing for small text; avoid condensed, short-x-height faces for UI text.
- Popular = vetted; inspect sites you admire.
- Full coverage for your languages (e.g., Vietnamese diacritics) and OpenType features (tabular figures).
Classes: serif (classic), sans (modern), script/display (large sizes only), monospace (code, comparable numbers).

## 2. Optional heading typeface

Add a second family **for headings only** to express personality (serif = established, rounded = friendly,
light sans = chic). Never more than two. Pair clearly *different* faces (typically a serif with a sans); two
similar faces look like a mistake. Within one family, differentiate with weight or style. Check how numerals look.

## 3. Weights

Regular (400–500) + bold (600–700). Thin/heavy weights only for large display text.

## 4. Type scale

- Hand-crafted UI scale: `12 14 16 18 20 24 30 36 48 60 72` px (`--text-xs` … `--text-7xl`), in rem/px —
  never em (nested em compounds off-scale: .875em inside 1.25em = 17.5px).
- Modular (ratio) scales suit long-form typography but give fractional values (round them) and too few UI sizes.
- Dense apps use fewer, closer sizes; marketing pages use bigger jumps; switch to smaller headline sizes on mobile.
- Line-heights land on a 4px grid where practical. Only define styles you use.

| Role | Size | Leading | Weight |
|---|---|---|---|
| Display/hero | 48–72 | 1 | bold |
| H1 | 36 (mobile 24–30) | 1.25 | bold |
| H2 | 30 | 1.25 | bold |
| H3 | 24 | 1.25 | bold |
| H4 | 20 | 1.4 | bold |
| Long-form body | 18 | 1.6–1.75 | regular |
| UI body | 16 | 1.5 | regular |
| Small/meta | 14 / 12 | 1.4–1.5 | regular |

## 5. Body size

People read at arm's length; designers pick text too small. Long-form body ≥ 18px; 16px for UI text and
controls; 14px/12px only for short meta and captions.

## 6. Line height

Proportional, not fixed: **inverse to font size** (headlines ~1, headings 1.25, body ≥ 1.5) and **growing with
line length** (narrow 1.5, wide up to 2). Heavier or large-looking typefaces need a bit more.

## 7. Line length

45–75 characters per line (~65ch, `--measure`); constrain paragraphs even inside wide content areas with
images — mixed widths in one area look more polished.

## 8. Alignment

- Left-align (language direction). Centre only headlines and blocks ≤ 2–3 lines; if one centred block runs long,
  rewrite it shorter.
- **No justified body text** (uneven spacing, "rivers", harder with dyslexia); if a print look is mandatory,
  add `hyphens: auto`.
- **Right-align numbers** in tables with tabular figures so decimals line up.
- **Baseline-align** mixed sizes on one line (`align-items: baseline`), not vertical centre.

## 9. Letter spacing

Trust the type designer, except: **tighten large headings** set in text-oriented families (≈ −0.025em) — never
the reverse (headline faces don't work small) — and **widen ALL CAPS** (≈ +0.06em). UPPERCASE only for short,
small, bold labels.

## 10. Links

- In running text: colour **and** underline (colour alone fails colour-blind users).
- In link-heavy UI chrome (nav, lists, cards): heavier weight or darker colour instead of paragraph styling;
  nav/tabs/cards carry other cues.
- Ancillary links off the main path may stay plain and reveal underline/colour on hover — use sparingly.

## 11. Text colour

Avoid light grey (fails readers) and pure black on white (glare) — use the text roles. Thin weights lower
effective contrast at small sizes even when the colour passes.
