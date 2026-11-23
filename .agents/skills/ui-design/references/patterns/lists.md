# Lists of things

## Contents
1. Start from the use case
2. Patterns

---

## 1. Start from the use case

What will people do with the list? Get an overview, browse, search for a specific item, sort/filter, rearrange,
add/edit/delete items. Then answer the IA questions:
- **Length:** fits the space? could it be bottomless?
- **Order:** natural order (alphabetical, time)? can users change it?
- **Grouping:** natural categories users understand? one level or a hierarchy?
- **Item types:** simple text or rich (images, metadata)? stand-ins for larger things?
- **Interaction:** show the whole item or a summary? where do details appear?
- **Dynamic behaviour:** load time, updates, real-time changes.

Common questions → patterns: *where do details go?* Two-Panel Selector (wide), One-Window Drilldown (narrow),
List Inlay (small details). *Heavy visuals?* Cards, Thumbnail Grid, Carousel. *Very long?* Pagination, Infinite
List, plus search/filter. *Categories or hierarchy?* Titled Sections for one level; trees/accordions or drilldown for
deeper ones.

## 2. Patterns

### Two-Panel Selector (Split View)
List in one panel; the selected item's details in the adjacent panel.
- Why: low effort (no screen change), low cognitive load, the list stays visible as a reminder, fast.
- How: list on the left or top, details right or below (reverse for RTL); clear selected state; keyboard up/down
  changes selection; on narrow screens collapse to One-Window Drilldown.

### One-Window Drilldown
Selecting an item replaces the list with its details; Back returns to the list.
- Use when: small screens, or both list and details need the full width.
- How: obvious Back; restore scroll position and selection on return; optional next/previous within details.

### List Inlay
Selecting a row expands its details in place; rows open and close independently.
- Use when: details are moderate in size and list context should stay visible.
- How: clear expand cue (chevron); smooth expansion; allow several open; keep the row header visible.

### Cards
Self-contained units combining image, text and actions; usually in a Grid of Equals.
- How: decide what users do with items and give every card the same template (media, title, key metadata, primary
  action); equal visual weight; whole card clickable for the main action, with separate secondary actions.

### Thumbnail Grid
Grid of visual items with small metadata.
- Use when: items have identifying images of similar size/style; users scan an overview; can be grouped into Titled
  Sections.
- How: consistent thumbnail size and aspect ratio (crop to fit); short labels below; selection and bulk actions;
  zoom/size control for dense libraries.

### Carousel
A horizontal strip of visual items scrolled or swiped.
- Use when: little vertical space but the list should look attractive; browsing and serendipity are welcome.
- How: equal-sized thumbnails; arrows or peeking edges to show there's more; metadata under items; don't hide
  must-see content in later slides; auto-advance only with pause control.

### Pagination
Split a long list into pages with navigation controls.
- Use when: very long lists, most users look near the top, loading everything is slow or impossible.
- How: prev/next plus page numbers (first, last, current ± a few); show total results; let users change page size;
  keep sort/filter across pages.

### Jump to Item
Typing in a focused sorted list jumps to the first match, refining as more characters are typed.
- Use when: long sorted lists, tables, dropdowns, trees (countries, names, file lists).
- How: type-ahead selects and scrolls to the match; reset after a pause; a live search variant filters results.

### Alpha/Numeric Scroller
Letters, numbers or dates along the scroll bar; tapping one jumps there.
- Use when: users seek specific items in a long sorted list (contacts).

### New-Item Row
The first or last row of a table/list is used to create a new item in place.
- Why: creation happens where the item will live; saves space and navigation.
- How: an empty row labelled "New task…" or a "+ Add" row; Enter saves and opens the next new row; defaults
  prefilled; easy cancel.
