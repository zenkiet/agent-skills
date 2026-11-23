# Images and icons

## Contents
1. Use good photos
2. Text needs consistent contrast
3. Everything has an intended size
4. User-uploaded content
5. Composition: rule of thirds
6. Colour temperature

---

## 1. Use good photos

Bad photos ruin otherwise great designs. Either hire a professional photographer (specific needs: lighting,
composition, colour are years of skill) or use high-quality stock (free sources like Unsplash exist). Never design with
placeholders planning to swap in smartphone photos later — it never works out. People follow a pictured person's
gaze, so point faces toward the content or call to action; avoid stock clichés (handshakes, kite-flying kids, generic
smiling teams) — custom imagery has far more impact.

## 2. Text needs consistent contrast

The problem with text on photos isn't the text colour, it's the image's dynamic range: white text vanishes on light
areas, dark text on dark areas. Reduce the image's dynamics:
- **Overlay:** semi-transparent black (for light text) or white (for dark text). Simple, but darkens/lightens
  everything, not just problem areas.
- **Lower image contrast** (then rebalance brightness) for finer control.
- **Colorize:** lower contrast → desaturate → solid colour fill in *multiply* blend mode. Also ties photos to brand
  colours.
- **Text shadow as glow:** large blur, zero offset — adds contrast only around the letters, letting you keep more of the
  image's character. Combine with a milder contrast reduction.
Concrete starting points:
- **Gradient scrim:** dark grey ≈ 90% opacity at the text edge fading to 0% about halfway across the image.
- **Uniform overlay:** dark grey ≈ 50% over the whole image.
- **Blurred translucent panel** (frosted) behind the text.
- **Solid caption background:** white text on dark grey (video-caption style).
Text must meet 4.5:1 (small) or 3:1 (large) over the brightest region likely to sit under it.

## 3. Everything has an intended size

- **Don't scale up icons:** icons drawn for 16–24px look chunky and crude at 3–4×, even as vectors. For big feature
  icons, put the small icon inside a larger coloured shape (circle/rounded square with a tinted background).
- **Don't scale down screenshots:** a full-app screenshot shrunk 70% turns 16px text into ~4px mush. Options: capture at
  a smaller layout (tablet) and give it lots of room; show a partial screenshot; or draw a simplified UI illustration
  with text replaced by lines.
- **Don't scale down icons either:** a 128px logo shrunk to a 16px favicon becomes mush. Redraw a simplified version at
  the target size so you control the compromises.

## 4. User-uploaded content

You can't art-direct users' images, but you can contain them:
- **Control shape and size:** display in fixed-ratio containers, centred and cropped (`object-fit: cover` or a
  background image with `background-size: cover`) rather than at intrinsic aspect ratios that wreck the layout.
- **Prevent background bleed:** an image whose background matches your UI loses its edges. Instead of a border (clashes
  with image colours), use a subtle **inner shadow** or a **semi-transparent inner border** — barely noticed, keeps the
  shape.

## 5. Composition: rule of thirds

Overlay a 3×3 grid and put the focal point (eyes, a surfer, a tree) on one of the four intersections, with
horizons on a horizontal line. Off-centre feels natural and dynamic; dead-centre feels static. It also leaves
calm space for overlaid text.

## 6. Colour temperature

Decorative photos look more cohesive when their white balance matches the palette (cooler photos with a blue
palette, warmer with warm palettes). Don't alter product photos where colour accuracy matters.
