# Copywriting (interface text)

## Contents
1. Be concise
2. Sentence case
3. Plain language
4. Front-load and inverted pyramid
5. Abbreviations and uppercase
6. Structure: headings and bullets
7. Labels: no "my"
8. Consistent vocabulary
9. Numbers
10. Punctuation and length
11. Links
12. Buttons
13. Error messages
14. Before/after examples
15. Tone and personality

---

## 1. Be concise

Words must earn their place; people skim and rarely read blocks. If a word can go without losing meaning or
usability, cut it.
- Cut filler: actually, basically, really, truthfully, quite.
- Cut articles where natural in UI fragments: a, an, the.
- Cut lead-ins: "would you like to", "in order to", "when it comes to", "are you sure", "there are", "it is".
- Prefer short words to long ones with the same meaning.
- Keep sentences under ~20 words.

## 2. Sentence case

Capitalise only the first word and proper nouns: "Save post for later?" not "Save Post For Later?". Title case
has inconsistent rules and the extra capitals interrupt scanning. Apply to headings, buttons, labels, menus,
tabs.

## 3. Plain language

Write for a 12-year-old (6th grade) who doesn't know the topic: no jargon, no slang, short common words,
natural contractions (you're, they're, who's). Plain language helps people with reading or cognitive
difficulties and everyone in a hurry. ("Add a custom domain so customers can find you" beats "Facilitate discoverability by
provisioning a bespoke domain".)

## 4. Front-load and inverted pyramid

- **Front-load**: put the key information/benefit in the first words of headings, list items, links and
  buttons. "30% off if you sign up today" beats "Sign up today for 30% off". "5 UI design ebooks you should
  read" beats "You should read these 5 UI design ebooks".
- **Inverted pyramid** for longer text: most important first (ideally the heading alone lets people act),
  then supporting detail, then background details — which can move to another screen or behind disclosure.

## 5. Abbreviations and uppercase

- Avoid abbreviations/acronyms ("dept.", "COB", "ETA", "DOB") — they make people decode. Spell them out; if
  you must use one, expand it on first use. Longer but clearer is the right trade.
- **UPPERCASE is shouting** and slower to read (all words become the same rectangle shape, so you read letter
  by letter). Only for short labels/eyebrows: small size, bold, extra letter spacing. Never for names,
  sentences or paragraphs.

## 6. Structure: headings and bullets

Break large content into smaller chunks; use **descriptive headings** that state the key point ("Fast check-in
— 95% of guests rated it 5 stars"), not vague labels. Headings must make sense out of context: screen-reader
users navigate by a list of headings. Use bullets for parallel items.

## 7. Labels: no "my"

"My email address" literally means the product's email (the UI is the speaker). "Your" is correct but usually
unnecessary: just "Email". Never mix "my" and "your" across the product.

## 8. Consistent vocabulary

One word per concept, everywhere. Pick one of each pair and stick to it: publish/post, sign up/register, log
in/sign in, delete/remove, subscribe/join, cart/bag. A button "Add to cart" with a header icon labelled "Bag"
creates doubt. Keep a product glossary in the design system.

## 9. Numbers

- Numerals, not words: "Join 899 designers" not "eight hundred and ninety nine". Numerals are scannable and
  expected for facts.
- Thousands separators: 1,000 (locale-aware formatting in code: `Intl.NumberFormat`).
- Very large numbers: "1 billion", "2.4M" instead of counting zeros.

## 10. Punctuation and length

- No full stops on fragments (labels, headings, list items, short descriptions, buttons). Use full stops only
  for full sentences — and then consistently across sibling elements.
- Sibling blocks in a row (feature cards, tiles) should have similar text length so their edges align and the
  row looks orderly; edit copy rather than letting one card run 3× longer.

## 11. Links

- Link text must describe the destination and make sense alone (screen readers list links out of context).
  Avoid "Learn more", "Read more", "Click here". Three "Learn more" links look like they go to the same place.
- Options: use the destination name as the link ("5 UI design ebooks to improve your skills"), make the card
  heading the link, or write "Learn more about email campaigns".
- "Click" is wrong for touch, keyboard and voice users and states the obvious — just make links look like links.

## 12. Buttons

**Verb + noun**: "Save post", "Discard message", "Edit article", "Send invite", "Start workout". The label
must make sense without reading the dialog text — many people read buttons first, and screen-reader users jump
straight to them. Avoid "OK", "Yes", "Submit", "Continue" when a specific action exists.

## 13. Error messages

Say **what happened, why (if useful), and how to fix it** so people can move on.
- Never blame the user; stay positive and helpful.
- No "Oops", "Sorry", "Please", "Something went wrong" filler.
- Human, not robotic; no codes or jargon (log codes separately if support needs them).
- Descriptive heading + action button so people needn't read the body.
- Example: "Oops! Sorry, an unexpected error occurred while processing your transaction (code 402)" →
  heading "Payment failed", body "Your card was declined. Try another card or contact your bank.", button
  "Update payment details".
- Field errors say the fix: "Enter an email address like name@example.com", "Password needs at least 8
  characters".

## 14. Before/after examples

| Before | After | Rule |
|---|---|---|
| Would you like to archive this project? Don't worry, you can always restore archived projects later from your settings page. | **Archive project?** You can restore it later from Settings. [Archive project] | concise, inverted pyramid, verb+noun |
| Save Post For Later? | Save post for later? | sentence case |
| ANNA NGUYEN | Anna Nguyen | limit uppercase |
| Leverage our synergistic onboarding paradigm to expedite your initial configuration journey. | Set up your account in 3 quick steps. | plain language, numerals |
| Click here for 5 UI design ebooks | 5 UI design ebooks to improve your interface design | descriptive link |
| Let's go! (button) | Start free trial | button describes action |
| My email address | Email | no "my" |

## 15. Tone and personality

Wording shapes personality as much as colour or type: impersonal, formal phrasing reads official/professional;
casual, friendly phrasing reads approachable. Pick the tone that matches the product's personality and keep it
consistent across headings, buttons, empty states and errors.
