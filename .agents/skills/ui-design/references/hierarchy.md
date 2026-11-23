# Visual hierarchy

## Contents
1. Why hierarchy matters most
2. Levers, and why size isn't everything
3. Text colours and weights
4. No grey text on coloured backgrounds
5. Emphasise by de-emphasising
6. Labels are a last resort (displaying data, never form inputs)
7. Visual hierarchy ≠ document hierarchy
8. Balance weight and contrast
9. Step-by-step hierarchy fix
10. The squint test
11. Actions follow the same pyramid

---

## 1. Why hierarchy matters most

Hierarchy — how important elements look relative to each other — is the most effective tool for making an
interface both easy to scan and "designed". When everything competes, the UI is a noisy wall; deliberately
quieting secondary and tertiary information improves the result even with identical colours, fonts and layout.

## 2. Levers, and why size isn't everything

Make important things more prominent with: **size**, **weight**, **colour** (richer, higher contrast),
**treatment** (different style from neighbours), **spacing** (more room), **position** (top/first), **depth**
(elevated = closer). Leaning only on font size makes primary content too big and secondary text too small —
emphasise with **weight**, de-emphasise with **colour**, keep sizes readable.

## 3. Text colours and weights

- Three text colours: `--color-text-strong` (primary: titles, body, labels), `--color-text-weak` (secondary:
  dates, meta, hints) and `--color-text-subtle` (tertiary: footers, fine print). All pass 4.5:1.
- Two weights: regular (400/500) for most text, bold (600/700) for emphasis. No weights under 400 for UI text;
  to quiet text use colour or a smaller step, not a thinner weight.

## 4. No grey text on coloured backgrounds

Grey-on-white works because it lowers contrast; grey on colour looks dirty, and white-at-reduced-opacity looks
washed out (even disabled) and lets images show through. Hand-pick a **same-hue tint** (adjust saturation and
lightness) that's quieter but still passes contrast.

## 5. Emphasise by de-emphasising

When the key element won't stand out and nothing more can be added (a coloured active nav item still blends
in), soften its competitors (quieter inactive items). At page scale: if a sidebar competes with content, drop its
background so it sits on the page.

## 6. Labels are a last resort (displaying data, never form inputs)

Naive `Label: value` gives every datum equal weight.
- **No label** when format or context explains it (an email, a phone number, a price; "Customer Support" under
  a name in a directory).
- **Merge label into value:** "In stock: 12" → "12 left in stock"; "Bedrooms: 3" → "3 bedrooms".
- **Necessary labels are supporting:** smaller, quieter and/or lighter than the value (dashboards).
- **Emphasise the label** when users scan for it (spec sheets: "Depth" matters more than "7.6mm"): darker
  label, slightly lighter value.

## 7. Visual hierarchy ≠ document hierarchy

Use semantic headings for structure but style by role. App section titles often behave like labels — small and
quiet — while content is the focus; some titles can be visually hidden but present for screen readers.

## 8. Balance weight and contrast

- **Contrast offsets weight:** solid icons are heavy and overpower adjacent text → give them a softer colour
  (`--color-icon`), match icon stroke to text weight and icon size to text size, keep one icon style
  (all outlined; filled implies "selected").
- **Weight offsets contrast:** a soft 1px border too faint? Make it 2px in the soft colour instead of darkening
  it into harshness (meaningful control borders still need 3:1).

## 9. Step-by-step hierarchy fix

1. Group related information into sections; order items within sections, then order sections; important
   sections go higher.
2. Identity section: name large/bold/text-strong; location smaller/regular/text-weak; rating as star icons.
3. Decision section: price + primary action; on mobile a sticky bottom bar (elevated, within thumb reach),
   brand-filled primary, price bigger and placed last beside the button.
4. Detail section (short label–value pairs): icon + text pairs that look alike; outlined icons in
   `--color-icon`, labels in text-weak.
5. Long description: drop obvious labels ("Description:"); text-weak, regular weight.

## 10. The squint test

Squint, blur, zoom out or step back: the most important element, the primary action and the screen's purpose
must still be obvious. If elements blur together, add spacing; if several compete for first, demote all but one.

## 11. Actions follow the same pyramid

One primary (solid, high contrast), a few secondary (outline or tint with border), some tertiary (link style).
Destructive actions aren't automatically big and red — that styling belongs on the confirmation step. Details in
`buttons.md`.
