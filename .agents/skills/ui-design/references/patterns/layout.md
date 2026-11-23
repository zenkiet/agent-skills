# Screen layout patterns

## Contents
1. Layout fundamentals (additions)
2. Patterns

---

Visual hierarchy, Gestalt grouping, spacing and alignment are covered in `../hierarchy.md` and
`../layout-spacing.md`. This file adds the layout fundamentals specific to interactive screens and the layout patterns.

## 1. Layout fundamentals (additions)

- **What makes things look important:** size, position (top, left, upper-right corner for small items), density
  (more surrounding space = more weight), background colour, rhythm (repeated lists/grids draw the eye), contrast.
  To make a *small* item stand out: put it top/left/upper-right, high contrast, set off by whitespace.
- **Closure** (fourth Gestalt principle, with proximity, similarity, continuity): the eye completes implied shapes, so
  aligned edges and whitespace can define regions without drawn boxes.
- **Visual flow:** strong focal points lead to secondary content in reading order; avoid elements that pull the eye
  against the intended sequence.
- **Dynamic displays:** scroll vertically, not horizontally for text; chunk content with tabs/accordions/panels.
- **Responsive enabling:** controls become available as prerequisites are met — prefer progressive disclosure
  (reveal the next part) over greyed-out controls, and explain anything disabled.
- **UI regions:** header/title (branding, global nav, toolbars), navigation (side or top), main content, secondary
  panels, footer. Keep their positions stable across screens.

## 2. Patterns

### Visual Framework
All screens share one layout, style and set of signposts so the product hangs together.
- How: common colours, fonts, writing style; titles, logos, breadcrumbs and navigation in the same places; consistent
  spacing, alignment and section styling; home screens may differ but share the framework. Implement as templates and
  tokens (separates style from content).

### Center Stage
The main task/content occupies the largest central area; secondary tools cluster around in smaller panels.
- Use when: the screen shows one coherent thing (document, form, article, editor, table).
- How: make the centre visibly dominant (size, position, contrast); keep side panels narrow and quieter; nothing
  competes with it in the header.

### Grid of Equals
Peer items in a grid with a common template and similar visual weight.
- Use when: many items of similar importance (articles, products, results).
- How: one card template (image, title, metadata, action) used for all; equal sizes; consistent behaviour so learning
  one item teaches them all; highlight a special item subtly within the same template.

### Titled Sections
Content divided into visually separated sections with strong titles, all visible.
- Use when: lots of content to scan; it groups into themes or tasks.
- How: get the IA right first; short descriptive titles; separate with spacing, rules or backgrounds; consistent title
  styling (see `../hierarchy.md` on sizing titles by role).

### Module Tabs
Modules in a tabbed area; one visible at a time.
- Use when: users need one module at a time; modules are similar in size; fewer than ~10 (ideally a handful); the set
  is stable.
- How: short one- or two-word labels; selected tab clearly connected to its panel; keep tab order stable; test the
  grouping (hidden content is only found if the labels make sense).

### Accordion
A vertical stack of panels opened and closed independently.
- Use when: users may want several modules open; modules differ in height; part of a menu or tool palette.
- How: concise headers with a chevron/triangle that rotates; whole header clickable; remember open state; allow
  several open unless space forbids; animate briefly.

### Collapsible Panels
Secondary or optional modules in panels the user opens/closes.
- Use when: supporting content whose value varies by user and moment; modules unrelated to each other; the main
  content should get the space when they're closed.
- How: one click to toggle; label with the module name (or "More"); chevron/icon cue; closing gives space back to the
  main content; animate; remember state.

### Movable Panels
Users rearrange, resize, show or hide modules.
- Use when: users have very different needs and spend long periods in the tool (dashboards, IDEs, portals).
- How: title bars as drag handles; sensible default layout; snap to a grid; reset-to-default option; persist the layout.
