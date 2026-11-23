# Actions and commands

## Contents
1. Ways to act
2. Affordance and direct manipulation
3. Patterns

---

## 1. Ways to act

- **Gestures:** tap, double-tap, long-press, swipe, pinch, rotate, shake (mobile); always offer a visible alternative
  for hidden gestures.
- **Buttons:** visible, readable, obvious; grouped semantically.
- **Menu bars:** the complete, predictable command set in desktop apps (File, Edit, View…).
- **Pop-up (context) menus:** context-specific common actions on right-click/long-press — never the only route.
- **Drop-downs** are for choosing values in forms, not for triggering actions.
- **Toolbars:** rows of icon buttons (with tooltips) for frequent commands.
- **Links:** navigation; styled text.
- **Action panels:** always-visible menus, good when actions are better described in words than icons.
- **Hover tools:** actions revealed on hover (plus focus/tap equivalents).
- **Single vs double click:** single-click selects, double-click opens (desktop object conventions).
- **Keyboard:** shortcuts following platform conventions (Ctrl/⌘-S…) and a logical tab order — for experts and
  accessibility.
- **Drag-and-drop:** "move this here" or "do this to that"; show drop targets and feedback; provide a non-drag
  alternative.
- **Typed commands:** command lines and command palettes for power users.

## 2. Affordance and direct manipulation

Things should look like what they do. Cues that something is actionable: distinctive shapes or icons, text styled
unlike body copy, hover/tap reactions, high-contrast treatment, manipulable look (shadows, highlights), separation by
whitespace. On touch devices, assume direct manipulation (tap, swipe a row, drag, pinch) — with visible fallbacks.

## 3. Patterns

### Button Groups
Related actions clustered as small, aligned groups with similar styling (2–5 per group).
- How: group by function or scope (app-wide, item-specific); short verb labels; separate groups with space or
  dividers; apply the primary/secondary/tertiary hierarchy (`../buttons.md`); place groups near what they affect.

### Hover or Pop-Up Tools
Per-item actions hidden until hover (desktop) or tap (mobile), shown next to the item.
- Use when: many items, several actions each, and permanent buttons would clutter.
- How: reserve space so layout doesn't jump; also reveal on keyboard focus; on touch show via tap or a "⋯" button;
  keep the primary action always visible if it's essential.

### Action Panel
A visible panel of commands that adapts to selection or context, more discoverable than menus.
- Use when: many actions per item, too many for hover tools; users wouldn't find a menu bar.
- How: group commands with headings; show only applicable actions (or explain unavailable ones); place beside the
  selection (side panel) or as a contextual toolbar.

### Prominent "Done" Button or Assumed Next Step
The preferred next step or final commit is the most obvious control.
- How: looks like a real button (filled, brand colour, clear label such as "Install", "Pay $42", "Search flights");
  set off by whitespace; placed right after the last field/content in the reading flow; one per screen. (This skill:
  left-aligned under the last field, verb + noun label.)

### Smart Menu Items
Menu labels that state exactly what they'll do: "Undo typing", "Close 'Report.docx'", "Delete 3 items".
- How: update labels with the current selection/last action; disable or hide when nothing applies.

### Preview
A lightweight rendering of the outcome before committing a heavy or costly action.
- Use when: printing, applying filters, configuring products, submitting purchases or long forms.
- How: show exactly what will happen (print preview, filter thumbnails, order summary, live configurator); allow
  edits from the preview; preview is proactive, not an extra step people must request.

### Spinners and Loading Indicators
Feedback between an action and its result.
- Spinners: indeterminate "working" animation for short waits. Loading/progress indicators: determinate bars with
  percentage, steps or time remaining for longer tasks.
- How: respond within ~100ms; spinner for waits of about 1–10s; progress bar with estimate beyond that; show partial
  results early; keep the rest of the UI usable.

### Cancelability
A way to stop a time-consuming operation instantly with no side effects.
- Use when: operations longer than ~2s, or modal states that block other work.
- How: first try to make it fast (or feel fast); put Cancel next to the progress indicator; cancel immediately and
  restore the previous state; Esc works in dialogs.

### Multilevel Undo
Reverse a sequence of actions step by step (with redo).
- Why: makes exploration safe for everyone (Safe Exploration, Incremental Construction).
- How: model reversible operations in the user's terms (text edits, object changes, layout, file operations,
  create/delete/reorder); don't track selection, navigation, scrolling or window changes; group trivial steps;
  Ctrl/⌘-Z / Shift-Z; show the action name in the Undo menu ("Undo delete row"). Irreversible actions (sending,
  purchasing, posting) need Preview/confirmation instead.

### Command History
A visible, reviewable record of actions (editing history, browser history).
- How: list actions with object and time; allow jumping back to a state, re-applying or reordering steps; search by
  keyword or date.

### Macros
Single commands composed of recorded or assembled action sequences, reusable and runnable over sets of objects.
- Use when: users repeat long sequences or apply the same steps to many files/records.
- How: record/playback, name and save, edit steps, run on a batch, share; build on Command History.
