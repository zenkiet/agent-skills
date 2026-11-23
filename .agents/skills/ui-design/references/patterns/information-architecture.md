# Information architecture and application structure

## Contents
1. What IA is
2. Approach
3. Patterns

---

## 1. What IA is

Organising and labelling an information space so people understand and use it with minimal strain: structures and
categories, ways to navigate, workflows, labels and language, search/browse/filter tools, and a consistent system of
screen types. Good IA anticipates needs, speaks the user's vocabulary, offers clear next steps, makes "where am I /
what's happening" obvious and confirms completion.

## 2. Approach

- **Separate information from presentation:** first decide what information and tools exist, when to show them,
  how they're categorised and ordered, what people do with them and how many ways they can be presented — only
  then design visuals.
- **MECE:** top-level categories should be mutually exclusive (no item fits two places) and collectively
  exhaustive (everything has a home).
- **Organising schemes:** alphabetical, numeric (integer, ordinal, ranges), time (often reverse-chronological),
  location (geographic/spatial), hierarchy (parent–child), category/facet. Pick the one that matches how people look
  for things; offer more than one when needs differ.
- **Task-heavy apps:** make frequent tasks immediately visible; chunk long jobs into steps; design for both
  novices (guidance) and experts (speed).
- **Multichannel reality:** desktop, mobile, messaging and voice — cards are a good building block that adapt
  across sizes.
- **System of screen types:** overview, focus, make, do (see `index.md`).

## 3. Patterns

### Feature, Search, and Browse
Home screen combining a featured item, a search box and browsable categories/lists.
- Use when: long lists of products/articles/media; engage visitors immediately. If the site is mainly search or
  transactions, search dominates and features/browse are secondary.
- How: search in a prominent, consistent spot (top corner or a central banner), visually set apart; browse by the
  categories users think in; feature something genuinely interesting; results can reuse list patterns.

### Mobile Direct Access
The first screen delivers useful, actionable output without input (using location, time, recent context).
- Use when: the app is known for one primary job.
- How: assume sensible parameters from device data (with permission) and show results immediately; allow easy
  correction of the assumptions.

### Streams and Feeds
A continuously updated, usually reverse-chronological strip of items (news, social posts, activity).
- Use when: content is published or aggregated continuously; new items make each visit rewarding.
- How: show new items first; per item show source, time, title/teaser or the whole micro-post, and a thumbnail;
  inline actions (reply, share, like); load more via Infinite List or Pagination; filtering by source/topic;
  activity streams for one entity's actions.

### Media Browser
Grid of thumbnails for browsing and managing photos, videos or documents, with item views and slideshow/playlist.
- How: Thumbnail Grid overview, a focused item view with next/previous, sorting/filtering, selection for bulk
  actions, editing tools near the selected item.

### Dashboard
An information-dense overview of key metrics, status, alerts and tasks, updated regularly; often the first screen after
sign-in.
- How: research which few indicators matter and cut the rest; arrange by importance; use clear charts and labels;
  link each tile to details; highlight what needs attention; let users customise when needs vary.

### Canvas Plus Palette
A large canvas where objects are created/arranged, with palettes of tools around it.
- Use when: any graphical editor (images, diagrams, layouts, slides).
- How: big empty canvas; tool palettes grouped by function with recognisable icons + tooltips; consistent create
  gesture (click-click, drag, pen pressure); properties panel for the selection; combine with Multilevel Undo and
  Many Workspaces.

### Wizard
Leads people step by step through a long, novel or branching task in a prescribed order.
- Use when: the task is rare for users and the designer knows the best path; steps affect later choices.
- How: chunk into a few meaningful steps; show a Progress Indicator; allow Back without losing data; summarise
  before commit. On one page, use numbered Titled Sections or progressive disclosure. Don't wizard-ify tasks
  experts do often — offer a direct form too. (Buttons: primary left-aligned; tertiary Back top-left.)

### Settings Editor
A findable, self-contained place to change preferences, account or object properties, with random access.
- How: put it where the platform/site convention says (app menu, avatar menu top-right); group settings into
  categories (tabs, side list or a grid of category cards); apply immediately (toggles) or with clear Save; show
  current values; never force a sequence.

### Alternative Views
Substantially different views of the same content (map/list, grid/list/table, edit/preview, print, timeline).
- Use when: one design can't serve conflicting needs or preferences.
- How: identify scenarios the main view serves badly; design dedicated views; switch in place with an obvious
  toggle; keep selection and filters across views.

### Many Workspaces
Multiple documents, projects or contexts visible at once (tabs, panels, windows, side by side).
- How: tabs/windows with clear names; allow side-by-side comparison; restore the workspace set on return.

### Help Systems
Layered help so assistance exists in the right form at the right moment.
- Layers: inline copy (meaningful headings, instructions, examples, Input Hints) → tooltips (essential for icon-only
  controls) → hover/expandable explanations (Collapsible Panels) → onboarding (intro screens, guided tours, videos)
  → searchable help centre/manual → live support (chat, email, phone) → community forums.
- How: put the most help in the interface itself; make deeper help findable from context; let tours be skipped and
  replayed.

### Tags
User- or system-applied labels that classify content and power associative browsing and search.
- How: easy tag entry with autocompletion; every tag links to a results page; show tags on items; search indexes
  tags; curate to avoid near-duplicates.
