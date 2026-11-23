# Implementation (HTML/CSS, Angular, Tailwind)

## Contents
1. Contents
2. Base layer
3. Focus ring
4. Buttons: hierarchy, state layers, raised primary, sizes
5. Hit areas and icons
6. Forms
7. Displaying data
8. Layout
9. Depth
10. Text on images
11. User-uploaded images
12. Finishing touches
13. Theme switching
14. Responsive type
15. Data robustness
16. Angular notes
17. Tailwind and Angular Material mapping

---

All snippets use `assets/tokens.css` names: semantic `--color-*`, `--shadow-*`, `--space-*`, `--text-*`,
`--leading-*`, `--radius-*`. Components never reference primitives (`--grey-500`) directly, except inside the
token file and for one-off decorative art.

## Contents
1. Base layer
2. Focus ring
3. Buttons: hierarchy, state layers, raised primary, sizes
4. Hit areas and icons
5. Forms: field anatomy, ARIA, inputs, steppers, choices, error summary
6. Displaying data: no naive labels, stats, tables
7. Layout: grid, fixed sidebar, max-width, measure, grouping
8. Depth: elevation, raised/inset, flat, overlap
9. Text on images
10. User-uploaded images
11. Finishing touches: accent bars, lists, quotes, links, backgrounds, empty states
12. Theme switching
13. Responsive type
14. Data robustness
15. Angular notes
16. Tailwind and Angular Material mapping

---

## 1. Base layer

```css
*, *::before, *::after { box-sizing: border-box; }   /* widths include padding + border */
html {
  font-family: var(--font-sans);
  color: var(--color-text-strong);
  background: var(--color-background);
  -webkit-text-size-adjust: 100%;
}
body { margin: 0; font-size: var(--text-base); line-height: var(--leading-normal); }

h1, h2, h3, h4 { margin: 0; font-weight: var(--weight-bold); color: var(--color-text-strong); line-height: var(--leading-tight); }
h1 { font-size: var(--text-2xl); letter-spacing: var(--tracking-tight); }
h2 { font-size: var(--text-xl); }
h3 { font-size: var(--text-lg); }
@media (min-width: 768px) {
  h1 { font-size: var(--text-4xl); }
  h2 { font-size: var(--text-3xl); letter-spacing: var(--tracking-tight); }
  h3 { font-size: var(--text-2xl); }
}
.display { font-size: var(--text-5xl); line-height: var(--leading-none); letter-spacing: var(--tracking-tight); }

.text-weak   { color: var(--color-text-weak); }
.text-subtle { color: var(--color-text-subtle); }
.text-sm     { font-size: var(--text-sm); }
.prose       { max-inline-size: var(--measure); font-size: var(--text-lg); line-height: var(--leading-relaxed); }
.caps        { font-size: var(--text-xs); font-weight: var(--weight-bold); text-transform: uppercase;
               letter-spacing: var(--tracking-caps); color: var(--color-text-weak); }
.num         { font-variant-numeric: tabular-nums; }

/* Links in running text: colour + underline */
a { color: var(--color-link); text-decoration-line: underline;
    text-decoration-thickness: from-font; text-underline-offset: 0.15em; }
a:hover { text-decoration-line: none; }
/* UI chrome links carry other cues */
.nav a, .tabs a, a.card { color: inherit; text-decoration: none; }
.nav a[aria-current="page"] { color: var(--color-text-strong); font-weight: var(--weight-bold);
                              box-shadow: inset 0 -3px 0 var(--color-brand); }   /* active state = interactive -> brand */
.nav a:not([aria-current]) { color: var(--color-text-weak); }                     /* de-emphasise the rest */
```

## 2. Focus ring

```css
:focus-visible { outline: var(--focus-ring-width) solid var(--color-focus-ring); outline-offset: var(--focus-ring-offset); }
:focus:not(:focus-visible) { outline: none; }
```

## 3. Buttons: hierarchy, state layers, raised primary, sizes

The state layer is a transparent overlay painted between background and content, so hover/press work on any
fill in either theme.

```css
.btn {
  position: relative; isolation: isolate;
  display: inline-flex; align-items: center; justify-content: center; gap: var(--space-xs);
  min-block-size: var(--target-min);
  padding-inline: var(--space-m);
  border: var(--border-2) solid transparent; border-radius: var(--radius-s);
  font: var(--weight-bold) var(--text-base) / var(--leading-tight) var(--font-sans);
  text-decoration: none; cursor: pointer;
  transition: box-shadow var(--duration-fast) var(--ease-standard), transform var(--duration-fast) var(--ease-standard);
}
.btn::before {
  content: ""; position: absolute; inset: calc(-1 * var(--border-2)); z-index: -1;
  border-radius: inherit; pointer-events: none;
  transition: background-color var(--duration-fast) var(--ease-standard);
}
.btn:hover::before  { background: var(--color-state-hover); }
.btn:active::before { background: var(--color-state-press); }

/* Primary — one per view; raised: lighter top edge + small sharp shadow; pressed: sinks */
.btn-primary {
  background: var(--color-brand); color: var(--color-on-brand);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--color-brand), white 18%), var(--shadow-raised);
}
/* text-strong is dark in light mode, light in dark mode: the overlay always raises label contrast */
.btn-primary:hover::before  { background: color-mix(in srgb, var(--color-text-strong) 14%, transparent); }
.btn-primary:active         { box-shadow: none; transform: translateY(1px); }
.btn-primary:active::before { background: color-mix(in srgb, var(--color-text-strong) 24%, transparent); }

/* Secondary — outline, optionally tinted; the border keeps the shape >= 3:1 */
.btn-secondary { background: transparent; color: var(--color-brand); border-color: var(--color-brand); }
.btn-secondary.is-tinted { background: var(--color-brand-weak); }

/* Tertiary — link style, underlined so it's never colour-only */
.btn-tertiary { background: transparent; color: var(--color-brand); padding-inline: var(--space-xs);
                text-decoration: underline; text-underline-offset: 0.15em; }
.btn-tertiary.is-quiet { color: var(--color-text-weak); }
.btn-tertiary:hover { text-decoration: none; }

/* Destructive: tertiary on normal pages; loud only inside the confirmation dialog */
.btn-danger { background: var(--color-text-error); color: #fff; box-shadow: var(--shadow-raised); }

/* Sizes scale padding non-proportionally */
.btn-sm { min-block-size: 40px; padding-inline: var(--space-s); font-size: var(--text-sm); }  /* 40px visual; extend hit area if used for touch */
.btn-lg { min-block-size: 56px; padding-inline: var(--space-l); font-size: var(--text-lg); }

/* Prefer alternatives to disabled; if unavoidable, keep it focusable and explained */
.btn[aria-disabled="true"] { opacity: 0.4; cursor: not-allowed; box-shadow: none; }
.btn[aria-disabled="true"]::before { display: none; }

/* Group: left-aligned, priority order; stacked full-width on mobile */
.btn-group { display: flex; flex-wrap: wrap; gap: var(--space-s); }
@media (max-width: 767px) {
  .btn-group { flex-direction: column; align-items: stretch; }
}
```
```html
<div class="btn-group">
  <button class="btn btn-primary" type="submit">Save post</button>
  <button class="btn btn-secondary" type="button">Preview post</button>
  <button class="btn btn-tertiary is-quiet" type="button">Discard draft</button>
</div>
<button class="btn btn-primary" type="button" aria-disabled="true" aria-describedby="why">Register</button>
<p id="why" class="text-weak text-sm">Fill out all required fields to register</p>
```
Block the click in code when `aria-disabled="true"`.

## 4. Hit areas and icons

```css
.icon-btn { position: relative; inline-size: 24px; block-size: 24px; display: inline-grid; place-items: center;
            color: var(--color-icon); background: none; border: 0; padding: 0; cursor: pointer; }
.icon-btn::after { content: ""; position: absolute; left: 50%; top: 50%;
                   inline-size: max(100%, var(--target-min)); block-size: max(100%, var(--target-min));
                   transform: translate(-50%, -50%); }               /* invisible 48px hit area */

/* Big feature icon = small icon at its drawn size inside a tinted shape (never scale icons up) */
.feature-icon { inline-size: var(--space-7); block-size: var(--space-7); border-radius: var(--radius-full);
                display: grid; place-items: center; background: var(--color-brand-weak); color: var(--color-brand); }
.feature-icon svg { inline-size: 24px; block-size: 24px; }
```
Icon-only buttons need `aria-label`, and a visible text label unless universally understood.

## 5. Forms

Order: label → hint → error → input (hint and error **above**). Label→input gap `--space-xs`; field→field gap
`--space-l` so groups never look ambiguous.

```html
<div class="field" data-invalid="true">
  <label class="field__label" for="email">Email <span aria-hidden="true">*</span></label>
  <p class="field__hint" id="email-hint">We'll send your receipt here</p>
  <p class="field__error" id="email-error"><svg aria-hidden="true" width="20" height="20"></svg>Enter an email address like name@example.com</p>
  <input class="field__input" id="email" type="email" autocomplete="email" required
         aria-invalid="true" aria-describedby="email-hint email-error">
</div>
<div class="field">
  <label class="field__label" for="company">Company <span class="field__optional">(optional)</span></label>
  <input class="field__input" id="company" autocomplete="organization">
</div>
```
```css
.field { display: grid; gap: var(--space-xs); justify-items: start; }
.field + .field { margin-block-start: var(--space-l); }
.field__label { font-weight: var(--weight-bold); color: var(--color-text-strong); }
.field__optional { font-weight: var(--weight-regular); color: var(--color-text-weak); }
.field__hint { margin: 0; color: var(--color-text-weak); }
.field__error { display: none; margin: 0; gap: var(--space-xs); align-items: flex-start;
                color: var(--color-text-error); font-weight: var(--weight-bold); }
.field__input {
  inline-size: 100%; max-inline-size: 32rem; min-block-size: var(--target-min);
  padding-inline: var(--space-s);
  border: var(--border-1) solid var(--color-border-input); border-radius: var(--radius-s);
  background: var(--color-background-raised); color: var(--color-text-strong); font: inherit;
  box-shadow: var(--shadow-inset);                       /* slight inset: "type here" */
}
.field__input:hover { border-color: var(--color-text-weak); }
.field[data-invalid="true"] .field__error { display: flex; }
.field[data-invalid="true"] .field__input { border: var(--border-2) solid var(--color-stroke-error);
                                             background: var(--color-fill-error-weak); }
/* width matches expected input */
.field__input--postcode, .field__input--cvc { inline-size: calc(4ch + 2 * var(--space-s) + 4px); }
.field__input--phone { inline-size: calc(15ch + 2 * var(--space-s) + 4px); }

input[type="checkbox"], input[type="radio"] { accent-color: var(--color-brand); inline-size: 18px; block-size: 18px; }

/* Selectable cards for important single choices — radio circle stays visible */
.choice-cards { display: grid; gap: var(--space-s); border: 0; padding: 0; margin: 0; }
.choice { display: flex; gap: var(--space-s); align-items: flex-start; padding: var(--space-s);
          border-radius: var(--radius-m); background: var(--color-background-raised);
          box-shadow: var(--shadow-raised); cursor: pointer; }
.choice:has(input:checked) { box-shadow: 0 0 0 var(--border-2) var(--color-brand), var(--shadow-hover);
                             background: var(--color-brand-weak); }

/* Stepper: horizontal -/+ at 48px, typable value */
.stepper { display: inline-flex; align-items: center; gap: var(--space-xs); }
.stepper input { inline-size: 6ch; text-align: center; }

/* Error summary (validate on submit): focus it, link each error to its field */
.error-summary { padding: var(--space-m); border: var(--border-2) solid var(--color-stroke-error);
                 border-radius: var(--radius-s); background: var(--color-fill-error-weak); }
.error-summary a { color: var(--color-text-error); }
```
```html
<div class="stepper" role="group" aria-labelledby="adults">
  <span id="adults">Adults</span>
  <button class="btn btn-secondary" type="button" aria-label="Remove 1 adult">−</button>
  <input class="field__input num" type="number" inputmode="numeric" min="0" value="2" aria-labelledby="adults">
  <button class="btn btn-secondary" type="button" aria-label="Add 1 adult">+</button>
</div>
<div class="error-summary" role="alert" tabindex="-1">
  <h2 class="field__label">2 errors were found</h2>
  <ul><li><a href="#street">Enter street address</a></li><li><a href="#city">Enter suburb, town or city</a></li></ul>
</div>
```

## 6. Displaying data

```html
<!-- not  Name: / Department: / Email: / Stock: -->
<p class="t-name">Jane Doe</p>
<p class="text-weak">Customer Support · janedoe@example.com</p>
<p><strong>12</strong> left in stock</p>
<div class="stat"><p class="stat__label">Revenue</p><p class="stat__value num">$24,580</p></div>
```
```css
.t-name { font-weight: var(--weight-bold); font-size: var(--text-lg); margin: 0; }
.stat__label { margin: 0; font-size: var(--text-sm); color: var(--color-text-weak); }
.stat__value { margin: 0; font-size: var(--text-3xl); font-weight: var(--weight-bold); line-height: var(--leading-tight); }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
.cell-primary { font-weight: var(--weight-bold); }   /* combine related columns: name + weak email underneath */
.cell-secondary { display: block; color: var(--color-text-weak); font-size: var(--text-sm); }
.sr-only { position: absolute; inline-size: 1px; block-size: 1px; overflow: hidden; clip: rect(0 0 0 0);
           white-space: nowrap; margin: -1px; padding: 0; border: 0; }   /* visually hidden section titles */
.section-title { font-size: var(--text-sm); font-weight: var(--weight-bold); color: var(--color-text-weak);
                 text-transform: uppercase; letter-spacing: var(--tracking-caps); margin: 0; }
```

## 7. Layout

```css
.layout { display: grid; grid-template-columns: repeat(var(--grid-columns), minmax(0, 1fr));
          column-gap: var(--grid-gutter); row-gap: var(--space-l);
          padding-inline: var(--grid-margin); max-inline-size: var(--content-max); margin-inline: auto; }
.layout > * { grid-column: 1 / -1; }
@media (min-width: 1024px) { .layout > .third { grid-column: span 4; } .layout > .half { grid-column: span 6; } }

.app { display: grid; grid-template-columns: 1fr; min-block-size: 100dvh; }
@media (min-width: 1024px) { .app { grid-template-columns: var(--sidebar-width) minmax(0, 1fr); } }  /* fixed sidebar */
.sidebar { background: transparent; }   /* if it competes with content, drop its background */

.narrow-card { inline-size: 100%; max-inline-size: 448px; margin-inline: auto; }  /* shrinks only when forced */
.section { padding-block: var(--space-2xl); }
@media (min-width: 1024px) { .section { padding-block: var(--space-3xl); } }
.form-with-aside { display: grid; gap: var(--space-l); }
@media (min-width: 1024px) { .form-with-aside { grid-template-columns: 1fr 2fr; } }  /* help text | form */

.stack > * + * { margin-block-start: var(--stack-gap, var(--space-s)); }
.prose h2 { margin-block: var(--space-xl) var(--space-s); }   /* more space above headings than below */
.prose li + li { margin-block-start: var(--space-xs); }
.cluster { display: flex; flex-wrap: wrap; gap: var(--space-l); }          /* between pairs */
.cluster > .pair { display: flex; gap: var(--space-xs); align-items: baseline; }  /* within a pair */
.row-baseline { display: flex; justify-content: space-between; align-items: baseline; }
```

## 8. Depth

```css
.card { background: var(--color-background-raised); border-radius: var(--radius-m);
        box-shadow: var(--shadow-raised); padding: var(--space-m); }
.card:hover { box-shadow: var(--shadow-hover); }
.menu, .popover { background: var(--color-background-overlay); box-shadow: var(--shadow-overlay); border-radius: var(--radius-m); }
.dialog { background: var(--color-background-overlay); box-shadow: var(--shadow-modal); border-radius: var(--radius-l); }
.is-dragging { box-shadow: var(--shadow-drag); }
.well { background: var(--color-background-sunken); box-shadow: var(--shadow-inset); border-radius: var(--radius-m); }

/* Flat style: zero-blur offset shadow */
.solid-shadow { box-shadow: 0 4px 0 color-mix(in srgb, var(--color-brand), black 35%); }

/* Overlap: card straddling two sections; image stack with "invisible border" */
.hero { background: var(--color-brand); padding-block-end: var(--space-10); }
.overlap { margin-block-start: calc(-1 * var(--space-9)); position: relative; }
.avatar-stack img { border-radius: var(--radius-full); box-shadow: 0 0 0 3px var(--color-background-raised); }
.avatar-stack img + img { margin-inline-start: calc(-1 * var(--space-3)); }
```

## 9. Text on images

```css
.media { position: relative; isolation: isolate; overflow: hidden; border-radius: var(--radius-m); color: #fff; }
.media > img { position: absolute; inset: 0; inline-size: 100%; block-size: 100%; object-fit: cover; z-index: -2; }
.media::before { content: ""; position: absolute; inset: 0; z-index: -1;
                 background: linear-gradient(to top, rgb(0 0 0 / 0.75) 0%, rgb(0 0 0 / 0) 55%); }  /* scrim */
.media.is-overlay::before   { background: rgb(0 0 0 / 0.5); }
.media.is-colorized > img   { filter: contrast(0.75) grayscale(1); }
.media.is-colorized::before { background: var(--primary-700); mix-blend-mode: multiply; }
.media__text { position: absolute; inset: auto var(--space-m) var(--space-m); text-shadow: 0 0 24px rgb(0 0 0 / 0.5); } /* glow */
```
Check contrast over the brightest area likely under the text.

## 10. User-uploaded images

```css
.thumb { position: relative; aspect-ratio: 1; border-radius: var(--radius-m); overflow: hidden; }
.thumb img { inline-size: 100%; block-size: 100%; object-fit: cover; display: block; }
.thumb::after { content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
                box-shadow: var(--shadow-image-edge); }   /* inset shadow on <img> itself is painted under the image */
```

## 11. Finishing touches

```css
/* Accent bars use the decorative accent colour, not the brand colour */
.card--accent { border-block-start: var(--accent-bar) solid var(--color-accent); }
.headline-accent::after { content: ""; display: block; inline-size: var(--space-7); block-size: 4px;
                          margin-block-start: var(--space-3); border-radius: 2px; background: var(--color-accent); }
.alert { padding: var(--space-s); border-radius: var(--radius-s); border-inline-start: var(--accent-bar) solid;
         display: flex; gap: var(--space-xs); }
.alert--success { background: var(--color-fill-success-weak); color: var(--color-text-success); border-color: var(--color-stroke-success); }
.alert--warning { background: var(--color-fill-warning-weak); color: var(--color-text-warning); border-color: var(--color-stroke-warning); }
.alert--error   { background: var(--color-fill-error-weak);   color: var(--color-text-error);   border-color: var(--color-stroke-error); }

/* Icon bullets */
.check-list { list-style: none; padding: 0; margin: 0; }
.check-list li { display: flex; gap: var(--space-3); align-items: flex-start; }
.check-list li + li { margin-block-start: var(--space-3); }
.check-list li::before { content: "✓"; flex: none; inline-size: 24px; block-size: 24px; border-radius: var(--radius-full);
                         display: grid; place-items: center; font-size: var(--text-sm); font-weight: var(--weight-bold);
                         background: var(--color-fill-success-weak); color: var(--color-text-success); }
/* Promoted quote mark */
.quote { position: relative; padding-inline-start: var(--space-7); }
.quote::before { content: "\201C"; position: absolute; inset-inline-start: 0; inset-block-start: -0.2em;
                 font: var(--weight-bold) var(--text-7xl)/1 Georgia, serif; color: var(--color-accent-weak); }
/* Fancy link (in body text keep the underline) */
.link-fancy { color: var(--color-text-strong); font-weight: var(--weight-bold); text-decoration: underline;
              text-decoration-color: var(--color-accent); text-decoration-thickness: 0.3em;
              text-underline-offset: -0.12em; text-decoration-skip-ink: none; }
/* Backgrounds */
.section--tint { background: var(--color-fill); }
.section--gradient { background: linear-gradient(135deg, var(--primary-600), color-mix(in oklch, var(--primary-600), var(--accent-500) 35%)); } /* keep hues ≤ ~30° apart */
.section--pattern { background-color: var(--color-background-sunken);
  background-image: radial-gradient(color-mix(in srgb, var(--color-stroke-strong) 30%, transparent) 1px, transparent 1px);
  background-size: 16px 16px; }   /* low-contrast pattern */
/* Fewer borders: spacing, shadow or background change instead */
.list-item + .list-item { margin-block-start: var(--space-1); }
/* Empty state */
.empty { display: grid; justify-items: center; text-align: center; gap: var(--space-3);
         padding: var(--space-9) var(--space-m); max-inline-size: 448px; margin-inline: auto; }
.empty__art { inline-size: var(--space-10); block-size: var(--space-10); color: var(--color-accent); }
```
```html
<section class="empty">
  <svg class="empty__art" aria-hidden="true"></svg>
  <h2>No projects yet</h2>
  <p class="text-weak">Create your first project to start tracking work.</p>
  <button class="btn btn-primary">Create project</button>
</section>   <!-- render tabs/filters only once content exists -->
```

## 12. Theme switching

`tokens.css` follows `prefers-color-scheme` and honours `[data-theme="light|dark"]` overrides. Avoid a flash:
```html
<script>(function(){var t=localStorage.getItem('theme');if(t==='light'||t==='dark')document.documentElement.dataset.theme=t;})();</script>
```
```js
export function setTheme(theme /* 'light' | 'dark' | 'system' */) {
  const root = document.documentElement;
  if (theme === 'system') { delete root.dataset.theme; localStorage.removeItem('theme'); }
  else { root.dataset.theme = theme; localStorage.setItem('theme', theme); }
}
```

## 13. Responsive type

Set sizes per breakpoint from the scale (see §1); big sizes shrink more on small screens than body text does.
Never chain em sizes.

## 14. Data robustness

```js
export function truncateMiddle(text, max) {              // keep the distinguishing end visible
  if (text.length <= max) return text;
  const keep = max - 1, head = Math.ceil(keep / 2), tail = Math.floor(keep / 2);
  return text.slice(0, head) + '…' + text.slice(text.length - tail);
}
const fmt = new Intl.NumberFormat(navigator.language);                                // 125,840
const compact = new Intl.NumberFormat(navigator.language, { notation: 'compact' });   // 1.2B
```
Show the full value in a tooltip; prefer wrapping (`overflow-wrap: anywhere`) over clipping.

## 15. Angular notes

- Load `tokens.css` globally (`angular.json` → `styles`) so components and the CDK overlay container (rendered
  at body level) see the variables.
- Validate on submit/blur; never `[disabled]="form.invalid"` on submit:
```ts
submitted = signal(false);
form = this.fb.group({
  email: this.fb.control('', { validators: [Validators.required, Validators.email], updateOn: 'blur' }),
});
showError(name: string) { const c = this.form.get(name)!; return c.invalid && (c.touched || this.submitted()); }
submit() { this.submitted.set(true); if (this.form.invalid) { /* render + focus error summary */ return; } }
```
```html
<div class="field" [attr.data-invalid]="showError('email')">
  <label class="field__label" for="email">Email <span aria-hidden="true">*</span></label>
  <p class="field__hint" id="email-hint">We'll send your receipt here</p>
  @if (showError('email')) { <p class="field__error" id="email-error">Enter an email address like name&#64;example.com</p> }
  <input class="field__input" id="email" type="email" formControlName="email" required
         [attr.aria-invalid]="showError('email')"
         [attr.aria-describedby]="showError('email') ? 'email-hint email-error' : 'email-hint'">
</div>
```
- CDK drag-and-drop elevation: `.cdk-drag-preview { box-shadow: var(--shadow-drag); } .cdk-drag-placeholder { opacity: .4; }`.
- Empty states: `@if (items().length) { …filters, tabs, list… } @else { <section class="empty">…</section> }`.
- Dialogs: `cdkTrapFocus`, restore focus on close; announce async results with `LiveAnnouncer`; prefer undo
  snackbars for reversible deletes.

## 16. Tailwind and Angular Material mapping

**Tailwind v3** — point utilities at the variables so themes switch for free:
```js
theme: { extend: {
  colors: {
    brand: 'var(--color-brand)', 'brand-weak': 'var(--color-brand-weak)', 'on-brand': 'var(--color-on-brand)',
    'text-strong': 'var(--color-text-strong)', 'text-weak': 'var(--color-text-weak)', 'text-subtle': 'var(--color-text-subtle)',
    'stroke-strong': 'var(--color-stroke-strong)', 'stroke-weak': 'var(--color-stroke-weak)', fill: 'var(--color-fill)',
    surface: 'var(--color-background)', 'surface-raised': 'var(--color-background-raised)',
    'surface-overlay': 'var(--color-background-overlay)', accent: 'var(--color-accent)',
  },
  spacing: { '2xs': 'var(--space-2xs)', xs: 'var(--space-xs)', s: 'var(--space-s)', m: 'var(--space-m)',
             l: 'var(--space-l)', xl: 'var(--space-xl)', '2xl': 'var(--space-2xl)', '3xl': 'var(--space-3xl)' },
  borderRadius: { s: 'var(--radius-s)', m: 'var(--radius-m)', l: 'var(--radius-l)' },
  boxShadow: { raised: 'var(--shadow-raised)', hover: 'var(--shadow-hover)', overlay: 'var(--shadow-overlay)',
               drag: 'var(--shadow-drag)', modal: 'var(--shadow-modal)' },
} }
```
Tailwind's default numeric scales already resemble these systems; restrict spacing to the ~25%-apart steps
(4, 8, 12, 16, 24, 32, 48, 64, 96, 128…), use only `font-normal`/`font-semibold`, `leading-none/tight` on
headings, `tracking-tight` on large headings, `tracking-wide` on uppercase, `max-w-prose` on paragraphs.
**Tailwind v4** builds utilities from `@theme` variables referenced as `var(--color-*)`; register the light values
there and let the dark overrides from `tokens.css` cascade (verify against the installed version).

**Angular Material (v19+, `mat.theme`)** emits `--mat-sys-*`; map after including the theme (`:root` beats `html`):
```scss
:root {
  --mat-sys-primary: var(--color-brand);           --mat-sys-on-primary: var(--color-on-brand);
  --mat-sys-surface: var(--color-background);      --mat-sys-on-surface: var(--color-text-strong);
  --mat-sys-on-surface-variant: var(--color-text-weak);
  --mat-sys-outline: var(--color-stroke-strong);   --mat-sys-outline-variant: var(--color-stroke-weak);
  --mat-sys-error: var(--color-text-error);
}
```
Check names against the installed version. Material form fields float labels inside and put hints/errors below —
an accepted platform convention; if kept, use `floatLabel="always"` and keep critical hints short.
