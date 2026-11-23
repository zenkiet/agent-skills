#!/usr/bin/env python3
"""
ui-design palette tool — one colour system:
  shade scales 100-900 (PRIMITIVES)  ->  semantic role tokens for light + dark (what components use),
  every role auto-picked from the shades so it meets its contrast target (WCAG 2) and, in dark mode, APCA.

Subcommands
  check FG BG
      WCAG 2 ratio + APCA Lc for a foreground/background pair, with pass/fail per use.
  shades NAME BASE [--rotate N] [--format table|css|tailwind|json]
  shades --grey cool|warm|neutral [--grey-hue H]
  shades --preset
      9-step scales: 500 = base (good button background), 100 = lightest tint, 900 = darkest text.
      Lighter/darker shades get extra saturation and a small hue rotation (toward 60/180/300 deg to
      lighten, 0/120/240 deg to darken; max 30) so they stay rich instead of washed-out or muddy.
  tokens [--brand HEX] [--grey cool|warm|neutral] [--grey-hue H] [--accent HEX] [--full]
         [--format css|table|json]
      Complete token file: primitives + semantic roles (light, dark via prefers-color-scheme and
      [data-theme]). --full adds spacing, type, leading, tracking, radius, motion and grid tokens.

Examples
  python palette.py check "#64748C" "#F5F7FA"
  python palette.py shades brand "#7C3AED" --format table
  python palette.py tokens --brand "#7C3AED" --grey warm --format table
  python palette.py tokens --brand "#7C3AED" --grey warm --full > tokens.css
"""
import argparse
import colorsys
import json
import math
import sys

STEPS = [100, 200, 300, 400, 500, 600, 700, 800, 900]
BRIGHT_HUES = [60, 180, 300]
DARK_HUES = [0, 120, 240]
GREY_L = {100: 97, 200: 92, 300: 83, 400: 55, 500: 45, 600: 36, 700: 27, 800: 19, 900: 12}
GREY_TEMPS = {"cool": (215, 16), "warm": (35, 12), "neutral": (0, 0)}
DEFAULT_BASES = {"primary": "#2F6FED", "red": "#E02D3C", "yellow": "#F2B705",
                 "green": "#137F45", "accent": "#0B7F86"}
ROTATE_OVERRIDE = {"yellow": 24}
SYSTEM = {"error": "red", "warning": "yellow", "success": "green"}
SYSTEM_HUES = {"error": 356, "warning": 45, "success": 146}

# ----------------------------------------------------------------------------- colour math

def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"invalid hex colour: #{h}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def to_css(c):
    """hex for (r,g,b); rgba() for (r,g,b,a)."""
    if len(c) == 4:
        r, g, b, a = c
        return f"rgba({int(r)}, {int(g)}, {int(b)}, {a:.2f})"
    return "#%02X%02X%02X" % tuple(max(0, min(255, round(x))) for x in c)


def rgb_to_hsl(rgb):
    h, l, s = colorsys.rgb_to_hls(*(c / 255 for c in rgb))
    return h * 360, s * 100, l * 100


def hsl_to_rgb(h, s, l):
    r, g, b = colorsys.hls_to_rgb((h % 360) / 360, max(0, min(100, l)) / 100, max(0, min(100, s)) / 100)
    return tuple(round(c * 255) for c in (r, g, b))


def blend(fg, bg, alpha):
    return tuple(round(f * alpha + b * (1 - alpha)) for f, b in zip(fg[:3], bg[:3]))


def perceived_brightness(rgb):
    r, g, b = rgb
    return math.sqrt(0.299 * r * r + 0.587 * g * g + 0.114 * b * b) / 255


def rel_lum(rgb):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def wcag(a, b):
    la, lb = rel_lum(a), rel_lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def apca(txt, bg):
    """APCA-W3 0.1.9 Lc. Positive: dark text on light bg; negative: light text on dark bg."""
    def y(rgb):
        r, g, b = (c / 255 for c in rgb[:3])
        yy = 0.2126729 * r ** 2.4 + 0.7151522 * g ** 2.4 + 0.0721750 * b ** 2.4
        return yy + (0.022 - yy) ** 1.414 if yy < 0.022 else yy
    yt, yb = y(txt), y(bg)
    if abs(yb - yt) < 0.0005:
        return 0.0
    if yb > yt:
        s = (yb ** 0.56 - yt ** 0.57) * 1.14
        return 0.0 if s < 0.1 else (s - 0.027) * 100
    s = (yb ** 0.65 - yt ** 0.62) * 1.14
    return 0.0 if s > -0.1 else (s + 0.027) * 100


def hue_dist(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def rotate_toward(h, targets, amount):
    t = min(targets, key=lambda x: hue_dist(h, x))
    d = hue_dist(h, t)
    step = min(d, amount)
    return (h + step) % 360 if (h + d) % 360 == t % 360 else (h - step) % 360


# ----------------------------------------------------------------------------- shade scales

def chromatic_scale(base_hex, rotate=10.0, light_edge=96.0, dark_edge=16.0):
    rotate = max(0.0, min(30.0, rotate))
    bh, bs, bl = rgb_to_hsl(hex_to_rgb(base_hex))
    lighter = {400: 0.28, 300: 0.55, 200: 0.78, 100: 1.0}
    darker = {600: 0.24, 700: 0.48, 800: 0.73, 900: 1.0}
    out = {}
    for step in STEPS:
        if step == 500:
            out[step] = hex_to_rgb(base_hex)
            continue
        if step < 500:
            f = lighter[step]
            l = bl + (light_edge - bl) * f
            h = rotate_toward(bh, BRIGHT_HUES, rotate * f) if bs > 5 else bh
        else:
            f = darker[step]
            l = bl - (bl - dark_edge) * f
            h = rotate_toward(bh, DARK_HUES, rotate * f) if bs > 5 else bh
        extra = max(0.0, abs(l - 50) - abs(bl - 50)) / 50       # keep saturation away from L 50%
        s = min(100.0, bs + (100 - bs) * 0.55 * extra) if bs > 5 else bs
        out[step] = hsl_to_rgb(h, s, l)
    return out


def grey_scale(temp="cool", hue=None):
    h, s = GREY_TEMPS[temp]
    if hue is not None:
        h = hue
        s = s or 12
    return {step: hsl_to_rgb(h, min(s * (1 + 0.9 * abs(GREY_L[step] - 50) / 50), 60) if s else 0, GREY_L[step])
            for step in STEPS}


def build_scales(brand=None, grey="cool", grey_hue=None, accent=None, rotate=10.0):
    bases = dict(DEFAULT_BASES)
    if brand:
        bases["primary"] = brand
    if accent:
        bases["accent"] = accent
    scales = {"grey": grey_scale(grey, grey_hue)}
    for name, base in bases.items():
        scales[name] = chromatic_scale(base, ROTATE_OVERRIDE.get(name, rotate))
    return scales


# ----------------------------------------------------------------------------- semantic roles

class Roles:
    def __init__(self):
        self.light, self.dark, self.report = {}, {}, []

    def check(self, mode, role, fg, bg, need, apca_need=0):
        ok = wcag(fg, bg) >= need and abs(apca(fg, bg)) >= apca_need
        self.report.append((mode, role, fg, bg, need, apca_need, ok))
        return ok


def pick(scale, order, ok):
    for st in order:
        if ok(scale[st]):
            return st, True
    return order[-1], False


def build_roles(sc):
    R = Roles()
    W = (255, 255, 255)
    g, p, acc = sc["grey"], sc["primary"], sc["accent"]
    var = lambda name, st: f"var(--{name}-{st})"

    # ------------------------------------------------ light
    L = R.light
    worst = g[100]  # darkest light background that text sits on (fill / sunken)
    L.update({"background": "#FFFFFF", "background-raised": "#FFFFFF", "background-overlay": "#FFFFFF",
              "background-sunken": var("grey", 100), "fill": var("grey", 100), "stroke-weak": var("grey", 200)})

    st, _ = pick(g, [400, 500, 600, 700], lambda c: wcag(c, worst) >= 4.5)
    weak = STEPS[min(STEPS.index(st) + 1, 7)]
    for role, step in (("text-subtle", st), ("text-weak", weak), ("text-strong", 900)):
        L[role] = var("grey", step)
        R.check("light", role, g[step], worst, 4.5)
    st, _ = pick(g, [300, 400, 500, 600], lambda c: wcag(c, worst) >= 3.0)
    L["stroke-strong"] = var("grey", st)
    R.check("light", "stroke-strong", g[st], worst, 3.0)

    st, _ = pick(p, [400, 500, 600, 700, 800, 900], lambda c: wcag(c, worst) >= 4.5)
    L["brand"] = var("primary", st)
    L["brand-hover"] = var("primary", STEPS[min(STEPS.index(st) + 1, 8)])
    L["brand-weak"] = var("primary", 100)
    L["on-brand"] = "#FFFFFF"
    R.check("light", "brand (links, buttons)", p[st], worst, 4.5)
    R.check("light", "on-brand (white on brand)", W, p[st], 4.5)

    for tone, name in SYSTEM.items():
        s = sc[name]
        L[f"fill-{tone}-weak"] = var(name, 100)
        st, _ = pick(s, [500, 600, 700, 800, 900], lambda c: wcag(c, s[100]) >= 4.5)
        L[f"text-{tone}"] = var(name, st)
        R.check("light", f"text-{tone}", s[st], s[100], 4.5)
        st, _ = pick(s, [400, 500, 600, 700, 800], lambda c: wcag(c, s[100]) >= 3.0)
        L[f"stroke-{tone}"] = var(name, st)
        R.check("light", f"stroke-{tone}", s[st], s[100], 3.0)

    L["accent"] = var("accent", 500)          # decorative only: accent bars, highlights, charts
    L["accent-weak"] = var("accent", 100)
    st, _ = pick(acc, [500, 600, 700, 800, 900], lambda c: wcag(c, acc[100]) >= 4.5)
    L["text-accent"] = var("accent", st)
    R.check("light", "text-accent", acc[st], acc[100], 4.5)

    gr, gg, gb = g[900]
    L.update({
        "state-hover": f"rgba({gr}, {gg}, {gb}, 0.04)",
        "state-press": f"rgba({gr}, {gg}, {gb}, 0.10)",
        "shadow-1": f"0 1px 3px rgba({gr}, {gg}, {gb}, 0.12), 0 1px 2px rgba({gr}, {gg}, {gb}, 0.20)",
        "shadow-2": f"0 3px 6px rgba({gr}, {gg}, {gb}, 0.14), 0 2px 4px rgba({gr}, {gg}, {gb}, 0.10)",
        "shadow-3": f"0 10px 20px rgba({gr}, {gg}, {gb}, 0.14), 0 3px 6px rgba({gr}, {gg}, {gb}, 0.08)",
        "shadow-4": f"0 15px 25px rgba({gr}, {gg}, {gb}, 0.15), 0 5px 10px rgba({gr}, {gg}, {gb}, 0.04)",
        "shadow-5": f"0 20px 40px rgba({gr}, {gg}, {gb}, 0.20)",
        "shadow-inset": f"inset 0 2px 4px rgba({gr}, {gg}, {gb}, 0.08)",
        "shadow-image-edge": f"inset 0 0 0 1px rgba({gr}, {gg}, {gb}, 0.10)",
    })

    # ------------------------------------------------ dark
    D = R.dark
    gh, gs, _ = rgb_to_hsl(g[500])
    ds = min(gs * 1.3, 30)
    surf = {"background-sunken": hsl_to_rgb(gh, ds, 6), "background": hsl_to_rgb(gh, ds, 9),
            "background-raised": hsl_to_rgb(gh, ds, 13), "background-overlay": hsl_to_rgb(gh, ds, 17)}
    for k, v in surf.items():
        D[k] = to_css(v)
    D["fill"] = "rgba(255, 255, 255, 0.06)"        # transparent: same prominence on every surface
    D["stroke-weak"] = "rgba(255, 255, 255, 0.12)"
    worst_d = blend(W, surf["background-overlay"], 0.06)  # fill on overlay = brightest bg under text

    D["text-strong"] = var("grey", 100)
    R.check("dark", "text-strong", g[100], worst_d, 4.5, 75)
    weak, _ = pick(g, [500, 400, 300, 200, 100], lambda c: wcag(c, worst_d) >= 4.5 and abs(apca(c, worst_d)) >= 60)
    D["text-weak"] = var("grey", weak)
    R.check("dark", "text-weak", g[weak], worst_d, 4.5, 60)
    sub, ok = pick(g, [600, 500, 400], lambda c: wcag(c, worst_d) >= 4.5 and abs(apca(c, worst_d)) >= 45)
    if ok and STEPS.index(sub) > STEPS.index(weak):
        D["text-subtle"] = var("grey", sub)
        R.check("dark", "text-subtle", g[sub], worst_d, 4.5, 45)
    else:
        # no grey shade sits between text-weak and failing: use translucent white (works on every surface)
        alpha = 0.50
        while alpha < 0.95:
            comp = blend(g[100], worst_d, alpha)
            if wcag(comp, worst_d) >= 4.5 and abs(apca(comp, worst_d)) >= 45:
                break
            alpha += 0.02
        r_, g_, b_ = g[100]
        D["text-subtle"] = f"rgba({r_}, {g_}, {b_}, {alpha:.2f})"
        R.check("dark", "text-subtle (translucent)", blend(g[100], worst_d, alpha), worst_d, 4.5, 45)
    st, _ = pick(g, [700, 600, 500, 400, 300], lambda c: wcag(c, worst_d) >= 3.0)
    D["stroke-strong"] = var("grey", st)
    R.check("dark", "stroke-strong", g[st], worst_d, 3.0)

    st, ok = pick(p, [500, 400, 300, 200, 100], lambda c: wcag(c, worst_d) >= 4.5 and abs(apca(c, worst_d)) >= 60)
    D["brand"] = var("primary", st)
    D["brand-hover"] = var("primary", STEPS[max(STEPS.index(st) - 1, 0)])
    pr, pg_, pb = p[500]
    D["brand-weak"] = f"rgba({pr}, {pg_}, {pb}, 0.18)"
    D["on-brand"] = D["background"]
    R.check("dark", "brand (links, buttons)", p[st], worst_d, 4.5, 60)
    R.check("dark", "on-brand (dark text on brand)", surf["background"], p[st], 4.5)

    for tone, name in SYSTEM.items():
        s = sc[name]
        sr, sg_, sb = s[500]
        D[f"fill-{tone}-weak"] = f"rgba({sr}, {sg_}, {sb}, 0.16)"
        comp = blend(s[500], surf["background-overlay"], 0.16)
        st, _ = pick(s, [400, 300, 200, 100], lambda c: wcag(c, comp) >= 4.5 and abs(apca(c, comp)) >= 60)
        D[f"text-{tone}"] = var(name, st)
        R.check("dark", f"text-{tone}", s[st], comp, 4.5, 60)
        st, _ = pick(s, [600, 500, 400, 300, 200], lambda c: wcag(c, comp) >= 3.0)
        D[f"stroke-{tone}"] = var(name, st)
        R.check("dark", f"stroke-{tone}", s[st], comp, 3.0)

    D["accent"] = var("accent", 400)
    ar, ag, ab = acc[500]
    D["accent-weak"] = f"rgba({ar}, {ag}, {ab}, 0.18)"
    st, _ = pick(acc, [400, 300, 200, 100], lambda c: wcag(c, worst_d) >= 4.5 and abs(apca(c, worst_d)) >= 60)
    D["text-accent"] = var("accent", st)
    R.check("dark", "text-accent", acc[st], worst_d, 4.5, 60)

    D.update({
        "state-hover": "rgba(255, 255, 255, 0.06)",
        "state-press": "rgba(255, 255, 255, 0.12)",
        "shadow-1": "0 1px 2px rgba(0, 0, 0, 0.45)",
        "shadow-2": "0 3px 6px rgba(0, 0, 0, 0.45), 0 2px 4px rgba(0, 0, 0, 0.30)",
        "shadow-3": "0 10px 20px rgba(0, 0, 0, 0.50), 0 3px 6px rgba(0, 0, 0, 0.30)",
        "shadow-4": "0 15px 25px rgba(0, 0, 0, 0.55), 0 5px 10px rgba(0, 0, 0, 0.20)",
        "shadow-5": "0 20px 40px rgba(0, 0, 0, 0.60)",
        "shadow-inset": "inset 0 2px 4px rgba(0, 0, 0, 0.35)",
        "shadow-image-edge": "inset 0 0 0 1px rgba(255, 255, 255, 0.10)",
    })
    return R


def brand_warnings(brand_hex):
    if not brand_hex:
        return []
    h, s, _ = rgb_to_hsl(hex_to_rgb(brand_hex))
    if s < 25:
        return []
    return [f"brand hue {h:.0f} is close to the {tone} system colour: use a neutral/near-black action colour "
            f"and keep the brand colour decorative, so each colour keeps one meaning."
            for tone, sh in SYSTEM_HUES.items() if hue_dist(h, sh) <= 18]


# ----------------------------------------------------------------------------- output

ROLE_ORDER = ["background", "background-raised", "background-overlay", "background-sunken", "fill",
              "stroke-weak", "stroke-strong", "text-subtle", "text-weak", "text-strong",
              "brand", "brand-hover", "brand-weak", "on-brand",
              "text-error", "stroke-error", "fill-error-weak", "text-warning", "stroke-warning", "fill-warning-weak",
              "text-success", "stroke-success", "fill-success-weak", "accent", "accent-weak", "text-accent",
              "state-hover", "state-press"]
SHADOWS = ["shadow-1", "shadow-2", "shadow-3", "shadow-4", "shadow-5", "shadow-inset", "shadow-image-edge"]
ALIASES = """  /* aliases components reach for */
  --color-link: var(--color-brand);
  --color-focus-ring: var(--color-brand);
  --color-icon: var(--color-stroke-strong);
  --color-border-input: var(--color-stroke-strong);
  --color-divider: var(--color-stroke-weak);
  --shadow-raised: var(--shadow-1);   /* buttons, cards at rest */
  --shadow-hover: var(--shadow-2);    /* hovered cards, raised panels */
  --shadow-overlay: var(--shadow-3);  /* dropdowns, popovers, menus */
  --shadow-drag: var(--shadow-4);     /* dragged items, sticky bars */
  --shadow-modal: var(--shadow-5);    /* dialogs */"""


def role_block(selector, roles, mode, indent=""):
    out = [f"{indent}{selector} {{", f"{indent}  color-scheme: {mode};"]
    for k in ROLE_ORDER:
        out.append(f"{indent}  --color-{k}: {roles[k]};")
    for k in SHADOWS:
        out.append(f"{indent}  --{k}: {roles[k]};")
    out += [indent + l if l else l for l in ALIASES.splitlines()]
    out.append(f"{indent}}}")
    return "\n".join(out)


def primitives_block(scales):
    out = [":root {"]
    for name, sc in scales.items():
        out.append(f"  /* {name} */")
        for st in STEPS:
            h, s, l = rgb_to_hsl(sc[st])
            out.append(f"  --{name}-{st}: {to_css(sc[st])}; /* hsl({h:.0f} {s:.0f}% {l:.0f}%) */")
    out.append("}")
    return "\n".join(out)


STATIC = """
/* ===================================================================== NON-COLOUR TOKENS */
:root {
  /* Spacing & sizing: one scale for padding, margins, gaps AND sizes. Adjacent steps >= ~25% apart.
     Small spacing inside groups, larger between groups. */
  --space-1: 4px;   --space-2: 8px;    --space-3: 12px;   --space-4: 16px;
  --space-5: 24px;  --space-6: 32px;   --space-7: 48px;   --space-8: 64px;
  --space-9: 96px;  --space-10: 128px; --space-11: 192px; --space-12: 256px;
  --space-13: 384px; --space-14: 512px; --space-15: 640px; --space-16: 768px;
  --space-2xs: var(--space-1);  /* dense UI only */
  --space-xs: var(--space-2);   /* label->input, icon->text, title->meta */
  --space-s: var(--space-4);    /* inside components; between buttons */
  --space-m: var(--space-5);    /* component padding (cards, dialogs) */
  --space-l: var(--space-6);    /* between cards/columns; desktop gutter */
  --space-xl: var(--space-7);   /* between major blocks */
  --space-2xl: var(--space-8);  /* desktop page margin; mobile section padding */
  --space-3xl: var(--space-9);  /* desktop section padding */

  /* Typography: one sans serif, two weights, hand-crafted scale (px/rem only, never em) */
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
  --text-xs: 0.75rem;   /* 12 meta only, never body */
  --text-sm: 0.875rem;  /* 14 captions, secondary UI */
  --text-base: 1rem;    /* 16 UI text, controls */
  --text-lg: 1.125rem;  /* 18 long-form body */
  --text-xl: 1.25rem;   /* 20 h4 */
  --text-2xl: 1.5rem;   /* 24 h3 / mobile h1 */
  --text-3xl: 1.875rem; /* 30 h2 */
  --text-4xl: 2.25rem;  /* 36 h1 */
  --text-5xl: 3rem;     /* 48 display */
  --text-6xl: 3.75rem;  /* 60 display */
  --text-7xl: 4.5rem;   /* 72 hero */
  --weight-regular: 400;  /* 400 or 500 depending on the typeface */
  --weight-bold: 600;     /* 600 or 700; nothing under 400 for UI text */
  --leading-none: 1;        /* big headlines */
  --leading-tight: 1.25;    /* headings */
  --leading-normal: 1.5;    /* UI text, narrow paragraphs (minimum for body) */
  --leading-relaxed: 1.75;  /* long-form / wider paragraphs */
  --leading-loose: 2;       /* very wide lines (better: narrow them) */
  --tracking-tight: -0.025em; /* large headings set in text typefaces */
  --tracking-caps: 0.06em;    /* short UPPERCASE labels */
  --measure: 65ch;            /* 45-75 characters per line */

  /* Shape: pick ONE personality (serious 0-2px | neutral 4-6px | friendly 8-12px | playful 16px+, pills) */
  --radius-s: 6px;    /* inputs, buttons, tags */
  --radius-m: 12px;   /* cards, menus */
  --radius-l: 20px;   /* dialogs, sheets, large surfaces */
  --radius-full: 9999px; /* badges/chips/avatars: keeps them distinct from buttons */
  --border-1: 1px;
  --border-2: 2px;    /* soft colour + more width = emphasis without harshness */
  --accent-bar: 4px;  /* decorative accent borders */

  /* Interaction */
  --target-min: 48px;
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;
  --duration-fast: 120ms;
  --duration-base: 200ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);

  /* Layout */
  --grid-columns: 4;
  --grid-gutter: var(--space-s);
  --grid-margin: var(--space-s);
  --content-max: 1280px;
  --sidebar-width: 256px;   /* fixed, not a percentage */
}
@media (min-width: 768px) {
  :root { --grid-columns: 8; --grid-gutter: var(--space-m); --grid-margin: var(--space-l); }
}
@media (min-width: 1024px) {
  :root { --grid-columns: 12; --grid-gutter: var(--space-l); --grid-margin: var(--space-2xl); }
}
@media (prefers-reduced-motion: reduce) {
  :root { --duration-fast: 0ms; --duration-base: 0ms; }
}
"""


def emit_css(scales, R, args, warnings):
    head = ["/* ui-design tokens — generated by scripts/palette.py",
            f" * brand={args.brand or DEFAULT_BASES['primary']} grey={args.grey} accent={args.accent or DEFAULT_BASES['accent']}",
            " * Layer 1 PRIMITIVES (--grey-100 ... --accent-900): raw shades. Don't use directly in components.",
            " * Layer 2 SEMANTIC (--color-*, --shadow-*): what components use; remapped per theme.",
            " * Light: text >= 4.5:1 and controls >= 3:1 against the darkest light background (grey-100).",
            " * Dark: same against fill-on-overlay (brightest dark surface) + APCA |Lc| floors for text.",
            " * --color-brand = INTERACTIVE only. --color-accent = decorative only (accent bars, highlights, charts)."]
    head += [f" * WARNING: {w}" for w in warnings]
    head.append(" */")
    parts = ["\n".join(head), "/* ===================================================================== PRIMITIVES */",
             primitives_block(scales),
             "/* ===================================================================== SEMANTIC: LIGHT */",
             role_block(':root,\n[data-theme="light"]', R.light, "light"),
             "/* ===================================================================== SEMANTIC: DARK */",
             "@media (prefers-color-scheme: dark) {\n" + role_block(':root:not([data-theme="light"])', R.dark, "dark", "  ") + "\n}",
             role_block('[data-theme="dark"]', R.dark, "dark")]
    if args.full:
        parts.append(STATIC.strip("\n"))
    return "\n\n".join(parts) + "\n"


def emit_report(report):
    rows = ["mode   role                            fg       bg       WCAG  need  APCA    need  status"]
    for mode, role, fg, bg, need, an, ok in report:
        rows.append(f"{mode:<6} {role:<31} {to_css(fg)}  {to_css(bg)}  {wcag(fg, bg):5.2f}  {need:>4}  "
                    f"{apca(fg, bg):6.1f}  {an:>4}  {'PASS' if ok else 'FAIL'}")
    return "\n".join(rows)


def shade_table(name, sc):
    W, B = (255, 255, 255), (0, 0, 0)
    rows = [f"\n{name}", "step  hex      HSL                 bright  vs white  vs black  hint"]
    for st in STEPS:
        c = sc[st]
        h, s, l = rgb_to_hsl(c)
        cw, cb = wcag(c, W), wcag(c, B)
        hint = ("text on white / white text on it" if cw >= 4.5 else
                "large-bold white text or UI border only" if cw >= 3 else
                "tinted background / dark text on it" if cb >= 4.5 else "")
        rows.append(f"{st:<5} {to_css(c)}  hsl({h:5.1f},{s:5.1f}%,{l:5.1f}%)  {perceived_brightness(c):.2f}"
                    f"    {cw:5.2f}    {cb:5.2f}   {hint}")
    return "\n".join(rows)


def cmd_check(fg_hex, bg_hex):
    fg, bg = hex_to_rgb(fg_hex), hex_to_rgb(bg_hex)
    r, lc = wcag(fg, bg), apca(fg, bg)
    print(f"fg {to_css(fg)} on bg {to_css(bg)}")
    print(f"WCAG 2.x : {r:.2f}:1")
    print(f"  normal text (< 24px regular / < ~19px bold) needs 4.5 -> {'PASS' if r >= 4.5 else 'FAIL'}")
    print(f"  large text, UI components, borders, icons needs 3.0   -> {'PASS' if r >= 3 else 'FAIL'}")
    print(f"APCA Lc  : {lc:.1f}")
    for need, label in [(90, "preferred body text"), (75, "min body text (18px+ regular)"),
                        (60, "other text (24px regular / 16px bold)"),
                        (45, "large text (36px reg / 24px bold) & UI elements"),
                        (30, "absolute min: placeholder / disabled text"), (15, "min non-text")]:
        print(f"  Lc {need:<3} {label:<48} {'PASS' if abs(lc) >= need else 'FAIL'}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        if len(sys.argv) != 4:
            sys.exit("usage: palette.py check <fg-hex> <bg-hex>")
        cmd_check(sys.argv[2], sys.argv[3])
        return

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("shades", help="generate 100-900 shade scales")
    s.add_argument("name", nargs="?")
    s.add_argument("base", nargs="?")
    s.add_argument("--rotate", type=float, default=10)
    s.add_argument("--grey", choices=list(GREY_TEMPS))
    s.add_argument("--grey-hue", type=float)
    s.add_argument("--preset", action="store_true")
    s.add_argument("--format", choices=["table", "css", "tailwind", "json"], default="table")

    t = sub.add_parser("tokens", help="primitives + semantic light/dark tokens")
    t.add_argument("--brand", help="brand/primary base colour (good button background)")
    t.add_argument("--grey", choices=list(GREY_TEMPS), default="cool")
    t.add_argument("--grey-hue", type=float, help="tint greys with this hue (e.g. the brand hue)")
    t.add_argument("--accent", help="decorative accent base colour")
    t.add_argument("--rotate", type=float, default=10)
    t.add_argument("--full", action="store_true", help="also emit spacing/type/radius/motion/grid tokens")
    t.add_argument("--format", choices=["css", "table", "json"], default="css")
    a = ap.parse_args()

    if a.cmd == "shades":
        scales = {}
        if a.preset:
            scales = build_scales(None, a.grey or "cool", a.grey_hue, None, a.rotate)
        else:
            if a.grey:
                scales["grey"] = grey_scale(a.grey, a.grey_hue)
            if a.name and a.base:
                scales[a.name] = chromatic_scale(a.base, a.rotate)
            if not scales:
                s.error("give NAME BASE, --grey TEMP, or --preset")
        if a.format == "table":
            print("\n".join(shade_table(n, sc) for n, sc in scales.items()))
        elif a.format == "css":
            print(primitives_block(scales))
        else:
            obj = {n: {str(k): to_css(v) for k, v in sc.items()} for n, sc in scales.items()}
            prefix = "// tailwind.config.js -> theme.extend.colors\n" if a.format == "tailwind" else ""
            print(prefix + json.dumps(obj, indent=2))
        return

    scales = build_scales(a.brand, a.grey, a.grey_hue, a.accent, a.rotate)
    R = build_roles(scales)
    warnings = brand_warnings(a.brand)
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    failed = [r for r in R.report if not r[-1]]
    if a.format == "table":
        print(emit_report(R.report))
        if failed:
            print(f"\n{len(failed)} role(s) could not meet target from the scale: adjust the base colour.")
    elif a.format == "json":
        print(json.dumps({"primitives": {n: {str(k): to_css(v) for k, v in sc.items()} for n, sc in scales.items()},
                          "light": R.light, "dark": R.dark}, indent=2))
    else:
        if failed:
            print(f"WARNING: {len(failed)} role(s) miss their contrast target; run --format table", file=sys.stderr)
        sys.stdout.write(emit_css(scales, R, a, warnings))


if __name__ == "__main__":
    main()
