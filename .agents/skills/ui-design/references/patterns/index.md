# Interaction pattern selector

## Contents
1. How to choose
2. Screen types
3. Problem → pattern
4. Where patterns were adjusted to this skill's guardrails

---

Patterns are proven solutions to recurring interaction problems, distilled from *Designing Interfaces* (3rd ed.,
Tidwell, Brewer & Valencia) and aligned with this skill's guardrails. Use this file to pick patterns; each pattern
is described in the domain file linked in the table.

## 1. How to choose

1. **Know the people and the goal** (`behavior.md`): who, skill level, what they're really trying to achieve.
2. **Pick the screen type** for each screen (below) and the **navigation model** for the app (`navigation.md`).
3. **Pick patterns per problem** from the table in §3. Prefer the conventional pattern users already know.
4. **Apply the visual rules** of this skill (hierarchy, spacing, type, colour, components) on top.

## 2. Screen types

| Type | Job | Typical patterns |
|---|---|---|
| **Overview** | Show a list or grid of things/options | Feature, Search, and Browse · Streams and Feeds · Media Browser · Grid of Equals · list patterns (`lists.md`) |
| **Focus** | Show one thing (article, map, video, record) | Center Stage · Alternative Views · Deep Links · Touch Tools (mobile) |
| **Make** | Create or edit an object | Canvas Plus Palette · Many Workspaces · Multilevel Undo · Preview |
| **Do** | Get a single task done (sign in, buy, configure) | Wizard · Settings Editor · Modal Panel · Prominent Done Button · input patterns (`input.md`) |

Most products combine these; give each screen one dominant organising principle.

## 3. Problem → pattern

| Problem | Pattern(s) | File |
|---|---|---|
| New/infrequent users don't know where to start | Clear Entry Points · Feature, Search, and Browse | navigation · information-architecture |
| Catalogue or content home page | Feature, Search, and Browse | information-architecture |
| Fresh, continuously updated content | Streams and Feeds (+ Infinite List / Pagination) | information-architecture · lists |
| Status and KPIs at a glance | Dashboard | information-architecture |
| Library of photos/videos/documents | Media Browser · Thumbnail Grid | information-architecture · lists |
| Graphical editor / creation tool | Canvas Plus Palette · Many Workspaces · Multilevel Undo | information-architecture · actions |
| Long, novel or branching task | Wizard + Progress Indicator | information-architecture · navigation |
| Preferences, account, profile | Settings Editor | information-architecture |
| Same data needs different "lenses" (map/list, edit/preview) | Alternative Views | information-architecture |
| Work on several documents/contexts at once | Many Workspaces | information-architecture |
| Users need explanation or onboarding | Help Systems (inline → tooltips → guided tours → docs → support) | information-architecture |
| User-generated classification | Tags | information-architecture |
| Mobile app known for one main job | Mobile Direct Access | information-architecture |
| Screen that is purely a table of contents | Menu Page | navigation |
| Sequence viewable in order or out of order | Pyramid | navigation |
| Short focused subtask without losing context | Modal Panel | navigation |
| Return to / share an exact place or state | Deep Links | navigation |
| Dead ends, limited navigation, users lost | Escape Hatch | navigation |
| Big site, hard to discover sections | Fat Menus · Sitemap Footer | navigation |
| Account/cart/help tools for signed-in users | Sign-In Tools | navigation |
| "How far along am I?" in a linear flow | Progress Indicator | navigation |
| "Where am I?" in a hierarchy | Breadcrumbs | navigation |
| Position in a long document / where the alerts are | Annotated Scroll Bar | navigation |
| State changes disorient users | Animated Transition | navigation |
| Screens should feel like one product | Visual Framework | layout |
| One primary thing per screen | Center Stage | layout |
| Many peer items of equal importance | Grid of Equals | layout |
| Lots of content that should all stay visible | Titled Sections | layout |
| Too much content: one module at a time | Module Tabs | layout |
| Too much content: several modules, stacked | Accordion | layout |
| Optional supporting modules | Collapsible Panels | layout |
| Users arrange their own workspace | Movable Panels | layout |
| Mobile screen structure | Vertical Stack | mobile |
| Parallel top-level mobile screens | Filmstrip | mobile |
| Controls over immersive content | Touch Tools | mobile |
| Low-priority global nav on mobile web | Bottom Navigation | mobile |
| Rich items in a mobile list | Collections and Cards | mobile |
| Small touch targets | Generous Borders | mobile |
| Hand off to dialer/maps/camera/calendar | Richly Connected Apps | mobile |
| List + details, wide screen | Two-Panel Selector (Split View) | lists |
| List + details, narrow screen | One-Window Drilldown | lists |
| Details are small; keep list context | List Inlay | lists |
| Visual items | Cards · Thumbnail Grid · Carousel | lists |
| Very long or bottomless list | Pagination · Infinite List | lists · mobile |
| Find an item in a long sorted list | Jump to Item · Alpha/Numeric Scroller | lists |
| Add items quickly in place | New-Item Row | lists |
| Several related actions, always visible | Button Groups | actions |
| Per-item actions without clutter | Hover or Pop-Up Tools | actions |
| Many contextual commands, discoverable | Action Panel | actions |
| The final / most likely next step | Prominent "Done" Button (Assumed Next Step) | actions |
| Menu commands that act on a selection | Smart Menu Items | actions |
| Costly or hard-to-reverse action | Preview | actions |
| Waiting | Spinners and Loading Indicators · Loading or Progress Indicators | actions · mobile |
| Long operation users may abandon | Cancelability | actions |
| Mistakes in complex editing | Multilevel Undo · Command History | actions |
| Repetitive sequences | Macros (Streamlined Repetition) | actions · behavior |
| Exact values in a chart/map on demand | Datatips | data |
| Busy graphic; follow one slice | Data Spotlight | data |
| Filter a multivariate data set | Dynamic Queries | data |
| Linked views of the same data | Data Brushing | data |
| Several series sharing an x-axis | Multi-Y Graph | data |
| More dimensions than one chart can show | Small Multiples | data |
| Inputs typed in many formats | Forgiving Format | input |
| Fixed, well-known input format | Structured Format | input |
| Rules or criteria | Fill-in-the-Blanks | input |
| Field purpose/format not obvious | Input Hints · Input Prompt | input |
| New password | Password Strength Meter | input |
| Predictable typing | Autocompletion | input |
| Rich choice in little space | Drop-down Chooser | input |
| Pick a subset from a big set | List Builder | input |
| Reduce effort | Good Defaults and Smart Prefills | input |
| Invalid input | Error Messages | input |

## 4. Where patterns were adjusted to this skill's guardrails

The book documents common practice; where practice conflicts with this skill's accessibility/usability rules, the
rule wins:
- **Input Prompt (placeholder):** only *in addition to* a visible label; hints go **above** fields, not below.
- **Error Messages:** no disabled submit buttons as the "modern" fix; validate on submit/blur; no "Sorry/Oops".
- **Prominent "Done" Button:** prominent yes, but left-aligned under the last field (OS-native dialogs excepted).
- **Wizard:** primary "Next" left-aligned under the fields; tertiary "Back" at top-left.
- **Responsive Enabling** (disable later steps until earlier ones are done): prefer progressive disclosure; if
  controls must be disabled, say why.
- **Hover Tools:** must also appear on keyboard focus and be reachable on touch.
- **Carousel / Filmstrip:** keep important content out of hidden slides; show that more exists; auto-advance
  needs a pause control.
