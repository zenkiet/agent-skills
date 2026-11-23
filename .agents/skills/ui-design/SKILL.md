---
name: ui-design
description: Complete UI/UX design system for building, polishing and reviewing interfaces — interaction patterns (navigation, information architecture, lists, tables, dashboards, data visualization, mobile, search, wizards, settings), visual hierarchy, spacing, typography, colour (shade palettes, light/dark tokens, WCAG/APCA contrast), depth, images, UI copy, buttons, forms and validation, states and finishing touches. Use this skill whenever you create or change anything user-facing (web pages, app screens, components, dashboards, landing pages, admin panels, mockups, HTML/CSS/Tailwind/Angular/React/Vue templates), set up a design system or theme, pick colours, fonts or spacing, write interface text, make a UI "look better", "more professional" or "less cluttered", or critique/audit a screen, screenshot, Figma frame or frontend code — even if the request never says "UI", "UX" or "design".
---

# UI design

One logic-driven system for interfaces that are **usable, accessible and visually polished**. Distilled and
reconciled from *Practical UI* (Adham Dannaway: usability/accessibility guardrails, forms, copy),
*Refactoring UI* (Adam Wathan & Steve Schoger: visual craft, systems, depth, polish) and *Designing Interfaces*
(Tidwell, Brewer & Valencia: interaction patterns, information architecture, navigation), with one shared token
system and tools. Premise: good UI comes from a small set of rules about how people see, read, think and tap —
not taste. Every visual detail should have a reason you can state.

## Principles (always on)

1. **Hierarchy first.** Rank content before styling; make one thing clearly most important. Emphasise with
   weight and colour before size, and by *de-emphasising competitors* rather than shouting louder.
2. **Accessible = usable.** WCAG 2.1 AA is the floor (text 4.5:1, large text and controls 3:1, never colour
   alone, ≥ 48px targets). Accessibility outranks aesthetics whenever they conflict.
3. **Minimise usability risk; prefer convention** (Jakob's Law). Innovate only where the product's value is.
4. **Minimise interaction cost and cognitive load**: actions near what they affect (Fitts), fewer/simpler
   choices (Hick), remove what doesn't earn its place, progressive disclosure for the rest.
5. **Systems for everything.** Pick from constrained scales (spacing, type, colour shades, shadows, radius);
   never invent one-off values. Decide by elimination between neighbouring steps.
6. **Feature first, greyscale first, low fidelity first.** Design the actual functionality before the shell;
   get hierarchy from spacing/size/contrast, then add colour with purpose. Build the real thing early, iterate
   in cycles, design the smallest shippable version.
7. **Start with too much white space, then remove.** Dense layouts are a deliberate exception.
8. **Consistency both ways:** same function → same look; different function → different look.
9. **Colour has jobs:** brand colour = interactive only; system colours = status only; accent colour =
   decoration/categorisation only. Colour supports meaning, never carries it alone.
10. **Polish is a pass, not a foundation:** depth, decoration and finishing touches come after hierarchy,
    spacing and type are right.
11. **Design for real behaviour:** people explore if it's safe (undo, cancel, predictable Back), want a quick
    first success, satisfice (pick the first plausible option), change tasks midstream and rely on spatial memory.
    Always answer "where am I, where can I go, how do I get back".
12. **Use established patterns** for structure and interaction before inventing (`references/patterns/index.md`).

## Workflows

**A — Build a new screen/component**
1. Identify users, goal and screen type (overview / focus / make / do); pick navigation model and interaction
   patterns from `references/patterns/index.md`. Inventory data and actions; rank them (primary / secondary /
   tertiary); remove or defer the rest.
2. Lay out at ~400px first, in greyscale, with generous space.
3. Use the project's tokens, else `assets/tokens.css` (brand version: `python scripts/palette.py tokens
   --brand "#hex" --grey cool --full`). Components use semantic tokens (`--color-*`, `--space-*`, `--shadow-*`).
4. Hierarchy (`references/hierarchy.md`) → layout/spacing (`layout-spacing.md`) → type (`typography.md`) →
   colour (`colour.md`) → components (`buttons.md`, `forms.md`, copy in `copywriting.md`) → depth (`depth.md`)
   → finishing touches (`finishing-touches.md`).
5. Cover all states: hover, pressed, focus-visible, disabled-alternative, loading, empty, error, long data.
6. Run the quick checklist below. Code patterns: `references/implementation.md`.

**B — "Make it look better" / refactor existing UI**
Use `references/review-and-refactor.md`: pass order (hierarchy → spacing → widths → type → colour → depth →
images → finishing touches) and the symptom → fix catalogue. Biggest-impact changes first.

**C — Review / audit**
Same file: squint test, category checklist, severity rubric (Critical / High / Medium / Low), report template.
Verify contrast numerically: `python scripts/palette.py check <fg> <bg>`.

**E — Structure, navigation and interaction**
For IA, navigation, lists/tables, dashboards, data visualization, mobile structure, actions, undo/cancel/loading,
or input techniques: start at `references/patterns/index.md` (problem → pattern table, screen types, guardrail
adjustments), then read the relevant pattern file.

**D — Design system / theme**
Read `references/colour.md` (palette architecture, dark mode, naming) and generate with
`scripts/palette.py tokens` (table format shows every role's WCAG/APCA result).

## Hard numbers (defaults unless the project's system says otherwise)

| Topic | Rule |
|---|---|
| Text contrast | ≥ 4.5:1 normal text; ≥ 3:1 large text (≥ 24px regular / ≥ ~19px bold). De-emphasised text still passes |
| Non-text contrast | ≥ 3:1 for input borders, checkbox/radio outlines, meaningful icons, focus rings, and button boundaries when the boundary identifies the button |
| APCA (check too, especially dark UI) | Lc 90 preferred body · 75 min body · 60 other text · 45 large text & UI · 30 placeholder/disabled · 15 non-text |
| Spacing & sizing scale | 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768 px (steps ≥ ~25% apart); aliases xs 8 · s 16 · m 24 · l 32 · xl 48 · 2xl 64 · 3xl 96 |
| Grouping | Space around a group > space within it (label→input 8, field→field 24–32) |
| Grid & widths | 12 cols desktop → 8 tablet → 4 mobile (gutters 32/24/16, margins 64/32/16); fixed sidebars; `max-width` for cards; don't fill the screen |
| Type scale | 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72 px in rem (never em). Body UI 16, long-form ≥ 18 |
| Weights | Regular (400–500) + bold (600–700) only; nothing under 400 for UI text |
| Line height | Inverse to size: ~1 big headlines, 1.25 headings, ≥ 1.5 body, up to 2 for wide lines |
| Line length | 45–75 characters (~65ch) |
| Alignment | Left-align text; centre only ≤ 2–3 lines; one alignment per component; baseline-align mixed sizes; right-align numbers (tabular figures); no justified text |
| Letter spacing | Default, except tighten large headings in text typefaces (−0.025em) and widen ALL CAPS (+0.06em) |
| Palette | Primitives: 9 shades (100–900) for greys (8–10, tinted, no pure black), primary, red/yellow/green, accent(s). Semantic roles map onto shades per theme |
| Shadows | 5 elevations (1 rest · 2 hover · 3 dropdown · 4 drag · 5 modal), two-part, light from above; dark mode uses lighter surfaces for elevation |
| Radius | One personality, used consistently: 6 / 12 / 20 px (small / medium / large); pills for badges |
| Targets | ≥ 48×48px hit area; ≥ 8px between targets, 16px between buttons |
| Buttons | Primary (solid) · secondary (outline, or tint + ≥ 3:1 border) · tertiary (underlined link style); ≤ 1 primary per view; verb + noun labels; left-aligned, priority order |
| Forms | Single column; labels above; required * and "(optional)"; hints and errors above the field; ≤ ~10 options → radios |
| Copy | Sentence case; < 20 words per sentence; front-load; numerals; descriptive links (no "click here") |
| Icons/images | Icons at intended size (put small icons in a tinted shape); text on photos always gets a scrim/overlay; user images in fixed-ratio crops |

## Quick checklist

- [ ] Squint test: the primary content and single primary action stand out; secondary info is quieter.
- [ ] Hierarchy by weight/colour, not only size; data shown without naive `Label: value` where context suffices;
      section titles sized by role, not by heading tag.
- [ ] All values from the scales; spacing groups things unambiguously; generous white space.
- [ ] Sensible widths (max-width, fixed sidebars, paragraphs ≤ 75ch); left-aligned text; baseline alignment.
- [ ] One typeface (+ optional heading face), two weights, body ≥ 16 (long-form ≥ 18), leading ≥ 1.5.
- [ ] Contrast verified: text ≥ 4.5:1, controls/icons ≥ 3:1; no colour-only meaning; links in text underlined.
- [ ] Brand colour only on interactive elements; accent colour only decorative; no grey text on coloured
      backgrounds (hand-pick a same-hue tint); loud colour panels flipped to dark text on light tint.
- [ ] Buttons: clear 3-level hierarchy, one primary, verb+noun, hit area ≥ 48px, disabled avoided or explained,
      destructive actions quiet until the confirmation step (+ undo where possible).
- [ ] Forms: labels above, required/optional marked, hints/errors above fields, right control types, errors say how to fix.
- [ ] States: hover, pressed, focus-visible, empty, loading, error, long data, narrow viewport, 200% zoom.
- [ ] Depth matches elevation; borders reduced (shadow / background change / spacing instead).
- [ ] Images: consistent text contrast, intended icon sizes, contained user uploads.
- [ ] Copy: sentence case, concise, plain, consistent vocabulary, descriptive headings/links/buttons.
- [ ] Structure: right pattern for the job (list/detail, navigation model); signposts show where users are; escape
      hatches from limited flows; deep links restore state.
- [ ] Safety and feedback: undo or preview for costly actions, cancel for long ones, loading feedback within ~100ms.

## Reference map (read only what the task needs)

| File | Read when |
|---|---|
| `references/patterns/index.md` | Choosing interaction patterns: screen types, problem → pattern table, guardrail adjustments |
| `references/patterns/behavior.md` | Users, goals, research methods, behavior patterns (safe exploration, satisficing…), smart systems |
| `references/patterns/information-architecture.md` | IA approach and app structures: feature/search/browse, feeds, dashboards, canvas, wizard, settings, help, tags |
| `references/patterns/navigation.md` | Navigation types and models, signposts, menus, modals, deep links, breadcrumbs, progress, transitions |
| `references/patterns/layout.md` | Screen layout patterns: visual framework, center stage, grid of equals, sections, tabs, accordion, panels |
| `references/patterns/mobile.md` | Mobile constraints and patterns: vertical stack, filmstrip, touch tools, cards, infinite list, connected apps |
| `references/patterns/lists.md` | List/detail patterns, cards, grids, carousel, pagination, jump-to, new-item row |
| `references/patterns/actions.md` | Action mechanisms, affordance, button groups, hover tools, action panels, preview, loading, cancel, undo, macros |
| `references/patterns/data.md` | Information graphics: models, preattentive variables, datatips, spotlight, dynamic queries, brushing, small multiples |
| `references/patterns/input.md` | Input techniques: forgiving/structured format, hints, prompts, password meter, autocompletion, choosers, defaults |
| `references/principles-and-process.md` | Reasoning and laws behind decisions; accessibility context; process (feature-first, cycles); personality; systems; simplification and reducing choice; interaction states |
| `references/hierarchy.md` | Emphasis/de-emphasis, text colours and weights, labels vs data, visual vs document hierarchy, weight vs contrast balance, step-by-step hierarchy fix, squint test |
| `references/layout-spacing.md` | Grouping, spacing scale and how to apply it, white space, widths, grids vs fixed widths, responsive sizing, alignment, Fitts placement, robust layouts |
| `references/typography.md` | Typeface choice, type scale, sizes, weights, line height/length, alignment, letter spacing, links |
| `references/colour.md` | Contrast (WCAG/APCA), palette architecture (shades → roles), building shades, HSL tricks, tinted greys, brand/accent/system usage, dark mode, transparent tokens, state colours, naming |
| `references/depth.md` | Light source, raised/inset, elevation system, two-part shadows, flat depth, overlap, dark-mode elevation |
| `references/images.md` | Photos, text on images, icon/screenshot sizing, user uploads, rule of thirds, colour temperature |
| `references/copywriting.md` | Any UI text: headings, labels, buttons, links, errors, numbers, tone |
| `references/buttons.md` | Button styles/hierarchy, placement, disabled alternatives, target size, icon+text, destructive friction |
| `references/forms.md` | Form layout, required/optional, hints, placeholders, control choice, multi-step, validation |
| `references/finishing-touches.md` | Supercharged defaults, accent borders, background decoration, empty states, fewer borders, rethinking components |
| `references/review-and-refactor.md` | Auditing or polishing: procedure, severity rubric, pass order, symptom → fix catalogue, report template |
| `references/implementation.md` | CSS/HTML patterns for all of the above, theming, Angular/Tailwind/Angular Material mapping |
| `assets/tokens.css` | Drop-in tokens: shade primitives, semantic light/dark roles, shadows, spacing, type, radius, motion, grid |
| `scripts/palette.py` | `check` a colour pair · `shades` generate 100–900 scales · `tokens` full verified light/dark token file |

## When guidance conflicts

Accessibility and clarity beat aesthetics. The project's existing design system and platform conventions
(iOS, Material, Windows/macOS dialogs) beat these defaults unless they fail accessibility or testing. Defaults
here are safe starting points: deviate when you have a stated reason, and say what it is.
