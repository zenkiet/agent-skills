# Colour

## Contents
1. Contrast requirements
2. Never colour alone
3. Colour jobs
4. Palette architecture: primitives → semantic roles
5. Building a shade scale
6. HSL, saturation and hue rotation
7. Greys and temperature
8. Colour and hierarchy
9. Accessible doesn't have to mean ugly
10. Dark mode
11. Transparent colours
12. Interaction-state colours
13. Generating the palette

---

## 1. Contrast requirements

**WCAG 2.1 AA:** 4.5:1 for normal text; 3:1 for large text (≥ 24px regular / ≥ ~19px bold) and for non-text UI
needed to identify or operate controls (input borders, checkbox/radio outlines, toggle tracks, meaningful icons,
focus indicators; button shapes when the shape is what identifies them). Decorative elements: no minimum.

**APCA (WCAG 3 draft)** — Lc value, depends on size/weight and on which colour is text vs background; fixes WCAG 2
oddities (e.g., black vs white on orange) and is far better for dark UIs:

| Lc | Use |
|---|---|
| 90 | Preferred body text |
| 75 | Minimum body text (18px+ regular) |
| 60 | Other text (24px regular / 16px bold) |
| 45 | Large text (36px regular / 24px bold), UI elements |
| 30 | Absolute minimum: placeholder, disabled text |
| 15 | Minimum non-text |

Policy: compliance work must pass WCAG 2; aim to pass APCA too; always check dark themes with APCA.
`python scripts/palette.py check "#fg" "#bg"`.

## 2. Never colour alone

Errors: red + icon + thicker border + tint + message. Links in text: underline. Status: icon/label. Trend deltas:
arrows. Charts: vary **lightness** as well as hue (survives colour blindness), add labels/patterns.

## 3. Colour jobs

- **Brand (action) colour = interactive only:** links, buttons, selected/active states, focus ring. Never on
  non-interactive headings or decorative icons — it teaches "coloured = clickable".
- **System colours = status only:** red error/destructive, amber warning, green success. Paired with icons.
- **Accent colour(s) = decoration/categorisation only:** accent bars, highlights ("new"), illustrations, chart
  series, tags. Never for actions, so it can't be confused with the brand colour.
- One interactive colour. With multiple brand colours, the highest-contrast one becomes the action colour; the
  rest decorate.
- **Light brand colours** (yellow, lime, cyan): use a darker shade for links/buttons, or text-strong for actions
  and keep the brand decorative; brand-filled buttons then take dark text. Mirror for dark brands on dark UI.
- **Brand hue that already means something** (red/green/amber): don't use it for actions; use a neutral or
  near-black action colour and keep the brand decorative (`palette.py` warns about this).

## 4. Palette architecture: primitives → semantic roles

**Primitives** are fixed shade scales: `--grey-100…900`, `--primary-…`, `--red-…`, `--yellow-…`, `--green-…`,
`--accent-…` (100 lightest tint, 500 base = good button background, 900 darkest text). You need more colours
than a "5-colour generator": 8–10 greys, 5–10 shades per primary, accents with shades — up to ~10 colours × 9
shades in complex UIs. Never derive variants on the fly with `lighten()`/`darken()`.

**Semantic roles** are what components use, mapped to primitives per theme (`assets/tokens.css`):

| Role | Use | Requirement |
|---|---|---|
| `--color-background` / `-raised` / `-overlay` / `-sunken` | page, cards, menus/dialogs, wells | content on them passes |
| `--color-fill` | tags, badges, hover rows, secondary panels | content on it passes |
| `--color-stroke-weak` | decorative dividers | none |
| `--color-stroke-strong` | input/control borders, meaningful icons | ≥ 3:1 vs darkest bg |
| `--color-text-subtle` / `-weak` / `-strong` | tertiary / secondary / primary text | ≥ 4.5:1 vs darkest bg |
| `--color-brand` (+ `-hover`, `-weak`, `--color-on-brand`) | actions; tint for selected/secondary; text on brand | ≥ 4.5:1 |
| `--color-text-/stroke-/fill-{error,warning,success}` | status text, borders, tinted backgrounds | 4.5:1 / 3:1 |
| `--color-accent` / `-weak` / `--color-text-accent` | decoration, highlights, categories | text 4.5:1 |
| `--color-state-hover` / `-press` | transparent state layers | — |

**Naming** follows `element.tone.emphasis.state` (element: text, stroke, icon, fill, background · tone: neutral,
brand, error, warning, success, accent · emphasis: strong, weak · state: hover, press, focus, disabled), written
`--color-text-error`, `--color-fill-success-weak`. Component-specific tokens are usually overkill.

## 5. Building a shade scale

1. **Base (500):** a shade that works as a button background — trust your eyes, no fixed lightness rule.
2. **Edges:** 900 (darkest, text) and 100 (lightest, tinted backgrounds) in the same hue; an alert (tinted bg +
   dark text) is a good place to pick both.
3. **Fill gaps:** 700 and 300 as perfect compromises, then 800/600/400/200. Nine steps is a sweet spot; five
   the minimum.
4. **Greys:** darkest = darkest text colour; lightest = subtle off-white background; fill the middle.
5. Tweak by eye once in use, but resist adding shades.
`python scripts/palette.py shades name "#base"` does this with the adjustments below and prints contrast per shade.

## 6. HSL, saturation and hue rotation

- Use **HSL** in code (hue 0–360, saturation, lightness 0 black/100 white/50 pure). Design tools often use
  **HSB**: 100% brightness = white only at 0% saturation.
- **Keep saturation away from L 50%:** the same S looks washed out near light/dark extremes, so raise
  saturation for lighter and darker shades.
- **Perceived brightness** differs by hue (`sqrt(.299r² + .587g² + .114b²)/255`): minima at red/green/blue
  (0/120/240°), maxima at yellow/cyan/magenta (60/180/300°). Rotate hue **toward 60/180/300° to lighten** and
  **toward 0/120/240° to darken**, max 20–30°, keeping shades rich (yellow → warm orange instead of brown).

## 7. Greys and temperature

Greys don't have to be neutral: a little blue = cool, a little yellow/orange = warm; saturate the lightest and
darkest greys more to keep temperature consistent. Avoid pure black text and pure black dark backgrounds.

## 8. Colour and hierarchy

Design in greyscale first; then use saturation (vivid for actions), hue (red reserved for urgency) and contrast
(darker headings, weaker secondary text) to support the hierarchy.

## 9. Accessible doesn't have to mean ugly

- **Flip the contrast:** white text on colour often needs a very dark shade that steals attention; use dark
  shade text (700–900) on a light tint (100) for badges, alerts and secondary buttons.
- **Rotate the hue** for coloured text on coloured panels: shift toward cyan/magenta/yellow to gain contrast
  without going nearly white.
- **No grey on colour:** hand-pick same-hue tints.

## 10. Dark mode

- Same roles, inverted: text near-white → weaker greys; push contrast well above the minimum; check APCA.
- Never pure black backgrounds; 3 surfaces for elevation (base < raised < overlay, slightly lighter each) plus a
  darker sunken surface.
- Brand colours usually need lightening/desaturating; primary buttons then use dark text. If it no longer looks
  on-brand, use white for actions and keep the brand decorative.
- Test foreground roles against the brightest surface (fill on overlay).

## 11. Transparent colours

Solid fills change prominence on different backgrounds (a grey tag disappears on a grey panel; in dark mode it
differs per surface). Transparent foregrounds keep prominence consistent. Neutral starting opacities — light:
black 90/60/45/10/4% (text-strong, text-weak, stroke-strong, stroke-weak, fill); dark: white 100/78/60/12/6%.
Brand/system: 100% text, 80% stroke-strong, 20% stroke-weak, 5% fill. The bundled tokens use transparent
fill/stroke-weak/tints in dark mode and solid shades in light mode.

## 12. Interaction-state colours

Pick one method and apply it everywhere: transparent **state layers** (hover = fill alpha, press = stroke-weak
alpha; works on any colour and theme — recommended), next-shade swaps (`--color-brand-hover`), opacity, or
elevation changes. See `implementation.md`.

## 13. Generating the palette

`python scripts/palette.py tokens --brand "#hex" --grey cool|warm|neutral [--accent "#hex"] --format table`
shows every role's chosen shade with WCAG and APCA results; `--full > tokens.css` writes the file. Roles are
auto-picked from the shades (lightest shade that passes for text on light, darkest that passes on dark).
