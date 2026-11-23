# Showing complex data

## Contents
1. Questions an information graphic must answer
2. Organisational models
3. Preattentive variables
4. Exploring, rearranging, filtering, reading values
5. Patterns
6. Aesthetics serve understanding

---

## 1. Questions an information graphic must answer

How is the data organised? What's related to what? How can I explore it? Can I rearrange it? How can I see only what
I need? What are the exact values? Know what the user needs to learn, then pick representations.

## 2. Organisational models

| Model | Common graphics |
|---|---|
| Linear | List, single-variable plot |
| Tabular | Spreadsheet, sortable table, multicolumn list, Multi-Y Graph, multivariable plots |
| Hierarchical | Tree, tree table, nested list, treemap |
| Network | Directed graph, flowchart |
| Geographic/spatial | Map, schematic, scatter plot |
| Textual | Word cloud |
| Other | Parallel coordinates and specialised plots |
If several fit, choose the one that foregrounds the relationship users care about.

## 3. Preattentive variables

Colour hue, lightness/saturation, size, position, orientation, shape, texture and motion are perceived before conscious
attention. Use them to make related data pop out and to layer data (items sharing a colour read as one layer). Text
tables force reading; encode the important comparison visually. Never rely on hue alone (pair with lightness, shape or
labels).

## 4. Exploring, rearranging, filtering, reading values

- **Navigation & browsing:** scroll, pan, zoom, overview + detail (minimap); for huge or indeterminate data, page with
  buttons rather than inaccurate scroll bars; link search results to the view (zoom to the found city).
- **Sorting & rearranging:** by value, alphabetically, by time, category, popularity, user arrangement — reordering can
  reveal patterns.
- **Searching & filtering:** narrow to relevant subsets; iterative refinement; show what's filtered out.
- **Actual values:** labels, gridlines, legends **on the same screen and close to the graphic**, Datatips on demand.

## 5. Patterns

### Datatips
Values and details appear when pointing at or tapping a data point.
- How: concise tooltip near the point with the exact value, label and context; don't obscure the area being read;
  touch: tap to show, tap elsewhere to hide; keyboard-focusable points for accessibility.

### Data Spotlight
Hovering a slice (series, layer, category) highlights it and dims the rest.
- Use when: dense graphics where structure is hard to trace.
- How: dim others strongly; highlight connected elements; pair with a legend that also triggers the spotlight.

### Dynamic Queries
Standard controls next to the display filter the data immediately.
- Use when: large multivariate data with predictable attributes (numeric ranges, dates, categories).
- How: sliders for a single value, double sliders for ranges, radio/drop-downs for one value or data set,
  checkboxes/toggles for subsets and layers, text fields for precise values; update results instantly; show counts.

### Data Brushing
Selecting points in one view highlights the same items in linked views.
- How: support single, range and multiple selection (click, drag-box, lasso, keyword); update linked views instantly;
  consistent highlight colour across views.

### Multi-Y Graph
Several graphs stacked with a shared x-axis and separate y-axes.
- Use when: related series share the x-axis (usually time) but differ in units or scale.
- How: one x-axis; distinct vertical bands per series; label each y-axis or omit axes when exact values aren't needed.

### Small Multiples
A grid of small charts, each showing the same view for a different slice of extra dimensions.
- Use when: more dimensions than one chart can show; users would otherwise flip between charts.
- How: identical scales and layout across tiles; order tiles meaningfully (time, rank, geography); label tiles
  concisely.

## 6. Aesthetics serve understanding

A well-designed visualization can be both beautiful and informative (e.g., warming stripes: one row of coloured bars
conveying 170 years of temperature change). Remove chart junk; keep encoding honest (zero baselines for bars,
consistent scales).
