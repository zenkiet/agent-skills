# Mobile interfaces

## Contents
1. Constraints and opportunities
2. Approach
3. Patterns

---

## 1. Constraints and opportunities

Tiny and variable screen widths (design the width intelligently; vertical scrolling is cheap), touch input (big targets,
no hover), typing is painful, harsh environments (sunlight, darkness, motion), limited attention and frequent
interruption, but also location, camera, sensors, notifications and integration with other apps.

## 2. Approach

1. **What do mobile users actually need?** Typical intents: know a fact now; fill a few spare minutes; connect
   socially; be told what matters now; what's relevant here.
2. **Strip it to the essence.** Remove sidebars, decorative images, pull quotes, extra links. Either a focused mobile
   subset or a complete parallel mobile design — but not the desktop crammed into 360px.
3. **Use the hardware:** location, camera, microphone, sensors, notifications, biometrics, payments.
4. **Linearise content** into one column.
5. **Optimise the most common sequences:** eliminate typing (pickers, defaults, autocompletion, scanning),
   minimise screen loads and data, prefer one long scrolling screen over many small ones, minimise taps, use large
   targets.

## 3. Patterns

### Vertical Stack
Content ordered in a single column that wraps text and scrolls; little or no side-by-side layout.
- Use when: most mobile web screens and forms, especially across sizes; when screen loads are expensive.
- How: order by importance; full-width controls; labels above fields; collapse secondary sections.

### Filmstrip
Swipe between parallel full-screen views (cities in a weather app, news sections).
- Use when: few parallel screens, all potentially interesting; browsing is welcome.
- Watch: doesn't scale to many screens; hidden screens are less discoverable — show position dots/labels and allow
  direct tapping.

### Touch Tools
Controls appear over immersive content on tap and fade after a few seconds of inactivity.
- Use when: video, photos, maps, reading, games.
- How: tap to show/hide; auto-hide (~5s) but never while interacting; keep critical controls reachable; consistent
  positions.

### Bottom Navigation
Global navigation placed at the bottom of a mobile web page, leaving the top of the screen for content.
- Use when: global links are low priority compared with fresh content on the front screen.
- How: full-width, large, readable tap targets stacked at the page bottom; keep only 2–3 key links at the top.
  (Native app tab bars at the bottom are a related platform convention for primary sections — follow iOS/Material
  guidance there: 3–5 destinations, icons + labels.)

### Collections and Cards
Lists of items with thumbnails (collections) or self-contained content + actions (cards).
- Why: images identify items, look inviting and give generous row heights for tapping.
- How: thumbnail on the left (or top in grids); title and one or two metadata lines; consistent aspect ratios.

### Infinite List
More items load as the user reaches the end of a long list.
- Use when: effectively bottomless lists (feeds, search results, archives) where most targets are near the top.
- How: fast initial load; load the next chunk automatically or via a "Load more" button (keeps footers reachable and
  gives control); show loading feedback; preserve scroll position when returning from an item.

### Generous Borders
Ample padding and space around every tappable element.
- How: targets at least 44×44pt (iOS) / 48×48dp (Android) — this skill uses ≥ 48px; make surrounding whitespace part
  of the hit area; separate adjacent targets.

### Loading or Progress Indicators
Microinteractions that show something is coming (spinner, progress bar, skeleton screens).
- How: show partial content as soon as it arrives; indicate duration when known; keep the UI responsive; branded
  animations can make waits pleasant.

### Richly Connected Apps
Hand data to the right app or device capability.
- How: phone numbers → dialer, addresses → maps, dates → calendar, emails → mail, links → browser, media → player;
  capture via camera/microphone in context; prefill from the device (payment, address, passwords) with permission.
