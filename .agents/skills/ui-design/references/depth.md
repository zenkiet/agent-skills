# Depth and elevation

## Contents
1. Light comes from above
2. Raised elements (e.g., a button with flat top/bottom)
3. Inset elements (wells, text inputs, checkboxes)
4. Don't get carried away
5. Shadows convey elevation
6. An elevation system (5 levels)
7. Shadows and interaction
8. Two-part shadows
9. Depth in flat designs
10. Overlap elements to create layers
11. Dark-mode elevation
12. Depth for hierarchy

---

## 1. Light comes from above

Raised panels on a door look raised because their top edges catch light (lighter) and bottom edges are shaded
(darker); inset panels show a shadow at the top (the lip blocks light) and a lighter bottom edge. Decide the profile you
want, then imitate how overhead light would hit it. Users look slightly *down* at screens, so show top edges of raised
things and bottom lips of inset things.

## 2. Raised elements (e.g., a button with flat top/bottom)

- **Top edge highlight:** slightly lighter than the face — a top border or `inset 0 1px 0` shadow. Hand-pick the lighter
  colour (same hue, lighter) rather than overlaying semi-transparent white, which drains saturation.
- **Shadow below:** a small dark shadow with a little positive y-offset so it only appears beneath; small blur (a couple
  of px) — sharp edges, like the shadow under a window frame.

## 3. Inset elements (wells, text inputs, checkboxes)

- **Bottom lip highlight:** slightly lighter bottom edge — bottom border or inset shadow with negative y-offset.
- **Top inner shadow:** small dark inset shadow with slight positive y-offset (the rim above blocks light from the top
  of the well), kept from showing at the bottom.

## 4. Don't get carried away

Borrow cues from the real world for a bit of depth; photo-realism makes interfaces busy and unclear.

## 5. Shadows convey elevation

Shadows place elements on a z-axis: small, tight shadow = barely raised; large, blurry shadow = close to the user. The
closer something feels, the more focus it attracts:
- Small: buttons (noticeable, not dominant).
- Medium: dropdowns/popovers (above the UI).
- Large: modal dialogs (demand attention).

## 6. An elevation system (5 levels)

Like colour and type, fix a set — five is usually plenty. Define the smallest and the largest first, then fill the
middle with roughly linear growth in offset and blur. Assign by *where the element sits on the z-axis*, not by what
looks nice in isolation. Tokens: `--shadow-1` … `--shadow-5`, with aliases `--shadow-raised` (1),
`--shadow-hover` (2), `--shadow-overlay` (3), `--shadow-drag` (4), `--shadow-modal` (5). Tint light-mode
shadows with the darkest grey rather than pure black so they belong to the palette.

## 7. Shadows and interaction

- Dragging a list item: increase its shadow on grab so it pops above its siblings and signals draggability.
- Pressing a button: switch to a smaller shadow (or none) so it feels pushed into the page.

## 8. Two-part shadows

Nice shadows often stack two, each with a job:
- **Direct light shadow:** larger, softer, noticeable y-offset, big blur — cast behind the object.
- **Ambient-occlusion shadow:** tighter, darker, small offset and blur — the dark area right under the object.
Two shadows let the soft one stay subtle while edges stay crisp. As elevation increases, the tight dark shadow fades
(lift something off your desk to see it) — make it distinct at the lowest level and nearly/completely gone at the
highest.

## 9. Depth in flat designs

- **Colour:** lighter feels closer, darker feels further (especially shades of one hue). Lighter than the background
  = raised; darker = inset well. Works in non-flat designs too.
- **Solid shadows:** short, vertically offset shadows with zero blur lift cards/buttons while keeping the flat look.

## 10. Overlap elements to create layers

- Offset a card so it straddles the boundary between two background sections.
- Make an element taller than its parent so it overlaps both edges.
- Smaller scale: carousel controls overlapping the slide edges.
- Overlapping images clash — give them an "invisible border" in the background colour so a gap always separates them.

## 11. Dark-mode elevation

Shadows barely show on dark backgrounds, so elevation is carried mostly by **surface lightness**: page
`--color-background` (darkest) < cards `--color-background-raised` < menus/dialogs `--color-background-overlay`,
each slightly lighter. Keep shadows (stronger, neutral black) as a secondary cue, keep each elevation level
visually equivalent across light and dark themes, and test text contrast on the brightest surface. A
`--color-background-sunken` (darker than the page) serves wells and inset areas.

## 12. Depth for hierarchy

Use elevation to rank, not decorate: sticky headers above scrolling content, the primary action bar above
everything on mobile (sticky bottom, `--shadow-drag`), modals highest. Elevation also signals interactivity
(raised cards invite clicks), so don't elevate static content just for looks.
