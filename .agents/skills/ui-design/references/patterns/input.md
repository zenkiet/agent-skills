# Input patterns (forms and controls)

## Contents
1. Form basics (additions)
2. Patterns

---

Layout, labels, required/optional marking, validation and control choice are governed by `../forms.md`. These
patterns add techniques for making individual inputs easier.

## 1. Form basics (additions)

- Respect people's time and attention: every field costs more than designers think.
- Long, complicated forms: show/hide sections dynamically so people aren't intimidated and don't skip steps.
- Validation messages must say which field, what's wrong and how to fix it.
- Form conventions evolve (floating labels, inline validation): adopt new idioms only when they're tested and
  accessible.

## 2. Patterns

### Forgiving Format
Accept input in many formats and interpret it intelligently.
- Use when: users may type unpredictable spacing, punctuation, abbreviations or capitalisation (phone and card numbers,
  dates, addresses, "city or zip", stock names).
- How: normalise behind the scenes (strip spaces/hyphens, parse "tomorrow 3pm", map names to symbols); show the
  interpreted value back; only reject what truly can't be parsed. It turns a UI problem into a programming one —
  budget for it.

### Structured Format
Several short fields (or one masked field) mirroring a fixed, well-known format.
- Use when: the format is familiar and never varies (verification codes, some ID or date formats).
- How: field widths match segment lengths; auto-advance between segments without trapping Backspace; accept paste of
  the whole value; prefer a single field with Forgiving Format when users might deviate.

### Fill-in-the-Blanks
Controls embedded in a sentence: "Show items where [price] [is less than] [$100]".
- Use when: building rules, conditions or queries where label-value pairs are unclear.
- How: write a natural sentence; controls replace words; keep it short; stack sentences for multiple rules; ensure
  each control still has an accessible label.

### Input Hints
A short explanation or example near the field ("e.g., 2024-05-31", "At least 8 characters").
- How: in this skill, place hints **between the label and the field** (above), always visible when needed to avoid
  errors; conditional hints (e.g., password rules) may appear while typing.

### Input Prompt (placeholder)
Example or instructional text shown inside an empty field or as the empty option of a drop-down.
- This skill's rule: never a substitute for the visible label; avoid instructional verbs ("Type…", "Enter…"); text
  disappears on typing, so nothing essential goes here; if used, ≥ 4.5:1 contrast. A drop-down's empty first
  option ("Choose a state") is acceptable when there's no good default. Distinct from floating labels.

### Password Strength Meter
Live feedback on password validity and strength.
- How: show requirements as a checklist that ticks off while typing (better than a vague meter alone); label
  weak/medium/strong with text, not colour only; allow show/hide password; don't impose arbitrary composition rules
  beyond what security requires.

### Autocompletion
Suggest likely completions while typing and complete when chosen.
- Use when: input is predictable (addresses, names, URLs, products, search terms, contacts).
- Sources: the user's history, common phrases, matching content, organisational directories, popular queries.
- How: suggestions appear quickly below the field; keyboard navigable; default to *not* accepting a completion
  automatically; don't hijack normal typing; stop offering a completion the user keeps rejecting; ≤ ~10 suggestions;
  bold the differing part; guess well.

### Drop-down Chooser
A drop-down/pop-up panel with a richer selector than a list (calendar, colour grid, tree, thumbnails).
- How: closed state shows the current value with a down arrow; panel opens adjacent; supports keyboard and Esc;
  allow typing the value directly when practical (dates).

### List Builder
Source and destination lists side by side to build a subset from a large set.
- How: Add/Remove buttons (or drag-and-drop) between lists; search in the source; clear confirmation of moved items;
  allow reordering the destination; for small sets, checkboxes are simpler.

### Good Defaults and Smart Prefills
Prefill fields with likely values (previous entries, account data, location, date/time, context).
- How: default to what most people choose or what context implies (search dates a few weeks out, current city);
  make defaults easy to change; don't default sensitive answers (gender, passwords) or consent checkboxes.

### Error Messages
Place clear, specific messages on the form, at the problem.
- How: prevent errors first (constrained controls, forgiving formats, good defaults); then follow `../forms.md`:
  message above the field plus an error summary on submit, colour + icon + text, plain language that names the field
  and the fix ("Enter your street address", "Is that a letter in your zip code?"). Don't disable submit until the
  form is valid, and skip "Sorry/Oops" filler.
