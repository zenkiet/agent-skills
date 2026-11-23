# Navigation, signposts and wayfinding

## Contents
1. Goals of navigation
2. Types of navigation
3. Design considerations
4. Navigation models
5. Patterns

---

## 1. Goals of navigation

Help people understand the space: what's available, how it's structured, **where am I, where can I go, where did I
come from and how do I get back.** Every page jump has a cognitive cost (re-orienting to a new screen), so keep
distances short.

- **Signposts** tell people where they are: page/window titles, logos, tabs, selection indicators, breadcrumbs.
- **Wayfinding** relies on good signage, environmental clues (close "×" top-right of dialogs, logo top-left) and
  maps (sitemaps, progress indicators).

## 2. Types of navigation

- **Global:** on every main screen (top bar, tabs, sidebar; top/left, not right).
- **Utility:** sign-in, help, settings, language, cart — usually top-right.
- **Associative/inline:** links within content.
- **Related content:** "related articles" panels.
- **Tags:** link items sharing a topic.
- **Social:** shared/trending content, people.

## 3. Design considerations

- Design the navigation model separately from its visual rendering (tabs vs menu vs sidebar comes later).
- **Broad and shallow:** more choices at the top level, fewer levels.
- **Put frequent destinations in global navigation;** bury rarely used ones.
- **Bring steps together:** frequent tasks shouldn't need several sub-screens and dialogs.

## 4. Navigation models

| Model | Shape | Typical use |
|---|---|---|
| Hub and spoke | Home lists all sections; go out, do the job, return | Mobile apps |
| Fully connected | Every page links to every main section (global nav) | Most websites/apps |
| Multilevel (tree) | Main sections connected; subpages connected within their section | Large sites, enterprise suites |
| Step by step | Prescribed sequence with Back/Next | Wizards, checkouts, slideshows |
| Pyramid | Hub lists a sequence; items also link Back/Next | Galleries, chapters, product sets |
| Flat | Little navigation; tools via menus/toolbars/palettes | Editors (Photoshop, Excel) |

## 5. Patterns

### Clear Entry Points
A few obvious starting points ("doors") for first-time and infrequent users.
- How: a small number of well-labelled options matching common goals; let global navigation recede visually;
  startup screens in apps (recent files + templates); guide gently until users have context.

### Menu Page
A screen whose job is purely a table of contents.
- Use when: home/start screens with many destinations and no need for featured content (common on mobile as a
  one-column list). Not when the page must hook or explain value.
- How: well-organised, descriptive links (short descriptions help); group with Titled Sections; no distractions.

### Pyramid
A parent page lists the whole sequence; each item has Back/Next links.
- Why: fewer clicks than "pogo-sticking" to the parent; shows the sequential relationship.
- How: list items on the parent in a suitable list form (Thumbnail Grid for photos); Back/Next plus "up" to the parent.

### Modal Panel
A dialog/sheet with no navigation except completing or dismissing it.
- Use when: focusing a single decision or quick subtask without losing the underlying context (sign-in at
  checkout, confirmations, "added to cart").
- How: place it where attention is; dim the background; clear title; obvious way out (close/cancel, Esc); keep it
  short; don't open modals over modals; don't use for content people need to compare with the page behind.

### Deep Links
Capture location *and state* (filters, selection, step, zoom) in a URL/link that can be bookmarked or shared and
restores the exact view.
- How: encode state in the URL; restore gracefully (sign-in, then return to the deep-linked place); mobile deep
  links open the right app screen.

### Escape Hatch
A clearly labelled way back to a known safe place.
- Use when: limited navigation (wizards, modals), dead ends, error states, or out-of-context arrivals from search.
- How: logo → home, "Cancel"/"Back to …" links, close buttons; no strings attached.

### Fat Menus (mega menus)
Drop-down or fly-out menus showing many links, grouped.
- Use when: many pages in a deep hierarchy and you want casual visitors to discover them.
- How: organise links into Titled Sections; consistent width/grid across menus; open on click or with hover delay;
  keyboard and touch accessible; don't cover critical content longer than needed.

### Sitemap Footer
A page-wide footer listing major sections and key subpages plus utility info.
- Contents: main categories, about/contact/careers, sister sites, community, help, contact info, promotions,
  legal/privacy, language. Keeps the header focused on primary tasks.

### Sign-In Tools
User-related utility tools in the top-right corner.
- How: show the signed-in name/avatar; menu with account, profile, settings, help, notifications, cart/saved items
  and **sign out**; keep it unobtrusive; place search consistently nearby; when signed out, show sign-in/sign-up there.

### Progress Indicator
A map of the steps in a linear process with "you are here".
- How: one compact row/column near the top; step titles short; mark done/current/upcoming; let users jump back to
  completed steps when safe; show page counts for slideshows.

### Breadcrumbs
The path from the top of the hierarchy to the current page, each level a link.
- Use when: two or more levels; users arrive deep via search or links.
- How: near the top above the title; separators (› or /); current page last and not a link; reflect the IA, not the
  click history; truncate the middle on small screens.

### Annotated Scroll Bar
Marks on/near the scroll bar showing position, sections or points of interest (search hits, errors, diffs).
- How: static marks for fixed landmarks, dynamic labels (current page/section) while scrolling.

### Animated Transition
Short animations connecting the before and after of a state change.
- Why: abrupt changes disorient; motion shows where things came from and went.
- How: brighten/dim, expand/collapse, fade/cross-fade, slide, zoom, spotlight; keep it brief (≈100–300ms) and purposeful;
  respect reduced-motion preferences.
