# Principles and process

## Contents
1. Decision-making principles
2. Psychology laws worth citing
3. Accessibility context
4. Process: feature first, fidelity later
5. Personality
6. Systems
7. Interaction states
8. Simplification ("less is more")
9. Reducing choice
10. Cost awareness

---

## 1. Decision-making principles

**Risk-based design.** For each detail ask "could someone have trouble with this?" Risks that look fine to
designers: thin light-grey text, icon-only buttons, coloured headings that read as links, faint input borders,
hidden actions, subtle selected states. Testing only catches big risks with the people you happened to test, so
remove small risks proactively.

**A rationale for every detail.** Justify each style choice in usability terms (hierarchy, grouping,
affordance, readability, contrast, consistency). It also makes feedback objective: "this heading competes with
the primary action" instead of "I don't like it".

**Interaction cost** = physical + mental effort for a task (looking, scrolling, searching, reading, clicking,
waiting, typing, thinking, remembering). It's countable: count clicks/scrolls/pointer travel for the main task
before and after a change (a quantity dropdown → a +/- stepper next to "Add to cart" turns 3 clicks + a scroll
into 2 clicks).

**Cognitive load** = brain power needed. Reduce it by removing unnecessary styles/info/choices, grouping,
familiar patterns, consistency and clear importance; split big tasks into steps.

## 2. Psychology laws worth citing

| Law / principle | Implication |
|---|---|
| Fitts's Law | Closer + bigger targets are faster: actions beside what they affect; ≥ 48px targets |
| Hick's Law | More/complex options = slower decisions: remove, group, step, recommend |
| Jakob's Law | People expect your UI to work like others they know: prefer conventions |
| Pareto (80/20) | Optimise the few tasks most people do; edge cases mustn't shape the main flow |
| Serial position | First and last items are remembered best (price last, next to the button) |
| Goal-gradient | Motivation rises near the end: show progress in multi-step flows |
| Common region | A shared container groups items (strongest cue) |
| Proximity | Near = related; space separates groups |
| Similarity | Look alike = same kind; a small difference highlights one item |
| Continuity | Items on one line/list read as a set; break the line to end a group |

## 3. Accessibility context

- WCAG 2.1 AA minimum (often legally required). Design for blindness, low vision, colour blindness (mostly
  red/green), motor and cognitive impairments, plus temporary (injury) and situational (sunlight, one hand)
  limits — accessible UI is simply better UI and good business.
- **Screen readers:** users jump through lists of headings, links and buttons, so those must make sense out of
  context.
- **Screen magnifiers** (more common): users see a small zoomed area — keep related content and actions close,
  left-align primary actions, avoid multi-column forms.

## 4. Process: feature first, fidelity later

- **Start with a feature, not a layout.** An app is a set of features; the shell (top nav vs sidebar, container
  vs full width) can't be decided well until a few exist. Design one concrete function first ("search
  flights": from, to, dates, search button). The nav may turn out unnecessary.
- **Low fidelity first:** explore layouts quickly (a thick marker on paper makes detail impossible — good).
  Don't fuss over typefaces, shadows or icons yet.
- **Hold the colour:** design in greyscale so spacing, contrast and size carry the hierarchy; colour later
  enhances it.
- **Don't over-invest in mockups;** build the real thing early. **Work in cycles:** simple design → build →
  fix what the working UI reveals → next feature. Edge cases are easier to solve in a usable UI than in your head.
- **Be a pessimist:** don't design functionality you can't build yet. Ship the smallest useful version; add
  nice-to-haves later.

## 5. Personality

Decide it deliberately; it's set by a few levers:
- **Typeface:** serif → elegant/classic; rounded sans → playful; neutral sans → plain (other elements carry it).
- **Colour:** go by feel more than psychology tables (blue = safe/familiar, gold = premium, pink = fun); test it.
- **Border radius:** none → serious; small → neutral; large → playful. Never mix square and rounded corners.
- **Language:** formal = professional; casual = friendly (see `copywriting.md`).
Unsure? Look at what your audience already uses, without imitating direct competitors.

**Visual style ranges:** skeuomorphic (mimics real objects; useful in small doses for affordance), illustrated
(warmth and personality), flat (solid colours, simple icons, sans serif; truly digital — keep affordances visible),
minimalistic (only what's essential; mind the "minimal ≠ simple" risk), adaptive/parametric (form generated from
context, e.g. AR measuring). Enterprise products: accessibility first, density and consistency over flourish.
Mood levers beyond colour and type: spaciousness vs crowding, angles vs curves (diagonals add energy), texture
(rarely behind text), imagery, cultural references and repeated visual motifs that give unity.

## 6. Systems

**Three layers:**
1. **Tokens** — small predefined sets: colour shades + semantic roles, type scale, spacing/sizing scale,
   shadows, radii, border widths, opacity, durations.
2. **Components** — smallest first (button, avatar, input) → composites (avatar + text → card → list) → page
   templates, kept in one library.
3. **Usage guidelines** — written rules (brand colour = interactive only, sentence case, left-aligned buttons,
   avoid disabled buttons, front-load text…) so a team stays consistent.

**Atomic design** gives the component layer a vocabulary: **atoms** (button, input, label, icon) → **molecules**
(search field + button) → **organisms** (header, product card grid) → **templates** (layouts with placeholders) →
**pages** (templates with real content). Goals: consistency (avoid "UX debt"), modularity, nesting from universal
style rules up. Established systems (Material, Fluent, Apple HIG) and UI frameworks (Bootstrap, Angular Material,
etc.) are a floor, not a ceiling: start from them, style them with your tokens, design the system rather than one-off
screens.

**Limit your choices.** Unlimited options cause paralysis (12 or 13px? 10% or 15% shadow? medium or semibold?)
and inconsistency. Systematise anything you catch yourself agonising over; never make the same micro-decision
twice.

**Decide by elimination.** Guess a value (16px icon), compare its neighbours on the scale (12, 24); usually two
look obviously wrong. If an outer value wins, repeat with it in the middle.

## 7. Interaction states

Every interactive element needs distinct **default** (already looks interactive), **hover**, **pressed**,
**focus-visible** (outline/ring ≥ 3:1; never removed) and, if used, **disabled**. Express them with one
consistent method: transparent state layers (hover = fill alpha, press = stroke-weak alpha), swapping to the
next shade, elevation change (raise on hover, drop on press), underline toggles, or quick subtle motion
(~100–200ms, respecting reduced-motion).

## 8. Simplification ("less is more")

- **Remove repetition** (lift a repeated prefix into one subheading).
- **Remove decorative noise** that carries no meaning or implies false meaning (random colours on list items,
  icons that look like buttons, coloured non-link headings).
- **Trends fade:** glass/neumorphic effects make hierarchy and contrast hard; experiment only if both still pass.
- **Progressive disclosure:** show what the current step needs; reveal detail via descriptive controls; show
  conditional fields only when relevant.
- **Minimal ≠ simple:** stripping labels, contrast and visible actions makes UIs vague.
- **Keep important things visible;** if space forces hiding, make it discoverable (peeking carousel cards).
- **Smallest screen first** to force prioritisation; large screens don't need to be filled.

## 9. Reducing choice

1. **Remove** options/fields that don't earn their place.
2. **Group/categorise** long lists.
3. **Split into steps** (multi-step forms, multi-level navigation).
4. **Recommend** popular options, suggestions, sensible defaults.

## 10. Cost awareness

Reuse existing systems, templates and icon sets; stick to familiar patterns (cheaper testing); learn front-end
constraints; talk to developers early — the simpler solution is usually cheaper *and* easier to use.
