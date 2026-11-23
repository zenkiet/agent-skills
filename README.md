<h1 align="center">Zen Agent Skills</h1>

<p align="center">
  Reusable, battle-tested skills that teach AI coding agents <i>how</i> to do specialised work — not just what to write.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/zenkiet/agent-skills?style=flat-square&color=blue"></a>
  <a href="#available-skills"><img alt="Skills: 1" src="https://img.shields.io/badge/skills-1-success?style=flat-square"></a>
  <a href="https://agentskills.io"><img alt="Agent Skills spec" src="https://img.shields.io/badge/spec-Agent%20Skills-8A2BE2?style=flat-square"></a>
  <a href="https://github.com/zenkiet/agent-skills/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/zenkiet/agent-skills?style=flat-square"></a>
  <a href="#contributing"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square"></a>
</p>

<p align="center">
  <a href="https://code.claude.com/docs/en/skills"><img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=claude&logoColor=white"></a>
  <a href="https://developers.openai.com/codex/skills"><img alt="Codex" src="https://img.shields.io/badge/Codex-000000?style=flat-square"></a>
  <a href="https://cursor.com/docs/context/skills"><img alt="Cursor" src="https://img.shields.io/badge/Cursor-000000?style=flat-square&logo=cursor&logoColor=white"></a>
  <a href="https://geminicli.com/docs/cli/skills/"><img alt="Gemini CLI" src="https://img.shields.io/badge/Gemini%20CLI-8E75B2?style=flat-square&logo=googlegemini&logoColor=white"></a>
  <a href="https://docs.github.com/en/copilot/concepts/agents/about-agent-skills"><img alt="GitHub Copilot" src="https://img.shields.io/badge/GitHub%20Copilot-000000?style=flat-square&logo=githubcopilot&logoColor=white"></a>
  <a href="https://opencode.ai/docs/skills"><img alt="OpenCode" src="https://img.shields.io/badge/OpenCode-1F1F1F?style=flat-square"></a>
  <a href="https://zed.dev"><img alt="Zed" src="https://img.shields.io/badge/Zed-084CCF?style=flat-square&logo=zedindustries&logoColor=white"></a>
</p>

<p align="center">
  <a href="#available-skills">Skills</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#repository-structure">Structure</a> ·
  <a href="#contributing">Contributing</a> ·
  <a href="#license">License</a>
</p>

---

## Overview

A **skill** is a folder with a `SKILL.md` (YAML frontmatter + instructions) and optional references, assets and
scripts. Agents load the short description up front and read the full instructions — and only the reference
files they need — when a task matches. The result: consistent, expert-level output without stuffing every
prompt with the same rules.

Every skill in this repo follows the open [Agent Skills](https://agentskills.io) format and installs with the
[`skills`](https://github.com/vercel-labs/skills) CLI into any compatible agent.

## Available skills

| Skill                                              | Category                       | What it does                                                                                                                                                                                                                               | Bundled                                     |
| -------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| [**ui-design**](.agents/skills/ui-design/SKILL.md) | Design · UI/UX · Accessibility | One logic-driven system for building, polishing and reviewing interfaces: visual hierarchy, spacing and layout, typography, colour and contrast (WCAG 2.1 AA + APCA), depth, images, interface copy, buttons, forms and finishing touches. | 13 references · `tokens.css` · `palette.py` |

---

### 🎨 ui-design

![WCAG 2.1 AA](https://img.shields.io/badge/WCAG-2.1%20AA-005A9C?style=flat-square)
![APCA](https://img.shields.io/badge/contrast-APCA-005A9C?style=flat-square)
![Python](https://img.shields.io/badge/Python-3%20·%20stdlib%20only-3776AB?style=flat-square&logo=python&logoColor=white)
![Frameworks](https://img.shields.io/badge/works%20with-HTML%20·%20CSS%20·%20Tailwind%20·%20React%20·%20Angular%20·%20Vue-555?style=flat-square)

One system for interfaces that are usable, accessible and visually polished, distilled and reconciled from
_[Practical UI](https://www.practical-ui.com/)_ (Adham Dannaway — usability and accessibility guardrails, forms,
copy) and _[Refactoring UI](https://www.refactoringui.com/)_ (Adam Wathan & Steve Schoger — visual craft,
systems, depth, polish). It ships build, refactor and review procedures, one shared token system and a palette
tool. Every visual decision gets a reason you can say out loud — "it looks nicer" is never the only one.

**Activates automatically** whenever the agent creates or changes anything user-facing, sets up a theme, picks
colours/fonts/spacing, writes UI text, is asked to make a UI "look better", or audits a screen, screenshot, Figma
frame or frontend code — even if the request never says "UI" or "design".

| Workflow              | When                      | What the agent does                                                                                                                                                              |
| --------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A · Build**         | Creating or changing UI   | Ranks content → ~400px and greyscale first → applies tokens → hierarchy, layout, type, colour, components, depth, finishing touches → covers every state → runs the checklist    |
| **B · Refactor**      | "Make it look better"     | Works through passes in impact order (hierarchy → spacing → widths → type → colour → depth → images → finishing touches) using a symptom → fix catalogue                         |
| **C · Review**        | Auditing a design or code | Squint test, then category passes; reports findings by severity, each with the rule broken, why it matters and a concrete fix. Contrast is verified numerically, never eyeballed |
| **D · Design system** | Setting up a theme        | Generates 100–900 shade scales and semantic light/dark tokens from a brand colour, with every role auto-picked to meet its WCAG/APCA contrast target                             |

**Opinionated defaults** (overridable by your project's design system):

- Text contrast ≥ 4.5:1 (large ≥ 3:1) · control boundaries and meaningful icons ≥ 3:1
- Spacing scale `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96 …` · 12 → 8 → 4 column grid
- Type scale `12 / 14 / 16 / 18 / 20 / 24 / 30 / 36 / 48 / 60 / 72` · two weights
- 9-shade palettes (100–900) mapped to semantic roles · 5 shadow elevations · radius `6 / 12 / 20`
- Hit areas ≥ 48 × 48 px · max one primary button per view · sentence-case copy

<details>
<summary><b>Bundled resources</b></summary>

| File                                   | Purpose                                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------------------- |
| `references/principles-and-process.md` | Principles, psychology laws, accessibility context, process, interaction states           |
| `references/hierarchy.md`              | Emphasis and de-emphasis, text colours and weights, labels vs data, squint test           |
| `references/layout-spacing.md`         | Grouping, spacing scale, white space, widths, grids, alignment                            |
| `references/typography.md`             | Typeface choice, type scale, weights, line height and length, letter spacing              |
| `references/colour.md`                 | Contrast, palette architecture (shades → roles), dark mode, transparent tokens, naming    |
| `references/depth.md`                  | Light source, elevation system, two-part shadows, flat depth, dark-mode elevation         |
| `references/images.md`                 | Photos, text on images, icon and screenshot sizing, user uploads                          |
| `references/copywriting.md`            | Headings, labels, buttons, links, errors, numbers, tone                                   |
| `references/buttons.md`                | Button weights, placement, disabled alternatives, target size, destructive actions        |
| `references/forms.md`                  | Layout, control choice, required/optional, hints, multi-step forms, validation            |
| `references/finishing-touches.md`      | Accent borders, background decoration, empty states, fewer borders                        |
| `references/review-and-refactor.md`    | Audit procedure, refactor pass order, severity rubric, symptom → fix catalogue, templates |
| `references/implementation.md`         | HTML/CSS patterns, theming, Angular, Tailwind and Angular Material token mapping          |
| `assets/tokens.css`                    | Drop-in shade primitives, semantic light/dark roles, shadows, spacing, type, radius, grid |
| `scripts/palette.py`                   | Contrast checker, shade-scale generator and verified light/dark token generator           |

</details>

<details>
<summary><b>Palette & contrast tool</b></summary>

No dependencies — standard-library Python 3 only.

```bash
cd .agents/skills/ui-design

# Check any foreground/background pair (WCAG 2.x ratio + APCA Lc)
python3 scripts/palette.py check "#767676" "#FFFFFF"

# 100–900 shade scale from a base colour (table | css | tailwind | json)
python3 scripts/palette.py shades brand "#4A63D9" --format table

# Semantic light/dark roles with each one's WCAG/APCA result
python3 scripts/palette.py tokens --brand "#4A63D9" --grey cool --format table

# Full token file: colour + spacing, type, radius, motion and grid
python3 scripts/palette.py tokens --brand "#4A63D9" --grey cool --full > tokens.css
```

</details>

**Try it:**

```text
Build a pricing page with three plans in Tailwind.
Make this dashboard look more professional and less cluttered.
Review this checkout form for usability and accessibility.
Set up light and dark design tokens for brand colour #4A63D9.
```

---

## Installation

### With the `skills` CLI (recommended)

Requires Node.js 22.20+. Run from your project root:

```bash
# Pick skills and agents interactively
npx skills add zenkiet/agent-skills

# Install a single skill
npx skills add zenkiet/agent-skills --skill ui-design

# Install globally for a specific agent
npx skills add zenkiet/agent-skills --skill ui-design -a claude-code -g
```

List what's available without installing:

```bash
npx skills add zenkiet/agent-skills --list
```

### Manually

Copy the skill folder into your agent's skills directory:

```bash
git clone https://github.com/zenkiet/agent-skills.git
cp -R agent-skills/.agents/skills/ui-design <your-project>/.agents/skills/
```

| Agent                                                    | Project path      | Global path                                                                                                      |
| -------------------------------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------- |
| Claude Code                                              | `.claude/skills/` | `~/.claude/skills/`                                                                                              |
| Codex, Cursor, Gemini CLI, GitHub Copilot, OpenCode, Zed | `.agents/skills/` | Agent-specific — see the [supported agents list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) |

## Repository structure

```text
agent-skills/
├── .agents/
│   └── skills/
│       └── ui-design/
│           ├── SKILL.md          # Entry point: principles, workflows, hard numbers
│           ├── references/       # Deep-dive guides, loaded only when needed
│           ├── assets/           # tokens.css — drop-in design tokens
│           └── scripts/          # palette.py — shades, tokens + contrast checker
├── LICENSE
└── README.md
```

## Contributing

New skills and improvements are welcome.

1. Scaffold a skill: `npx skills init <skill-name>` and move it to `.agents/skills/<skill-name>/`.
2. Fill in the `SKILL.md` frontmatter — `name` (lowercase, hyphenated) and a `description` that states
   **what** the skill does and **when** to use it.
3. Keep `SKILL.md` focused; move long material into `references/` and point to it from a reference map.
4. Check the skill is discovered: `npx skills add . --list`.
5. Add a row to [Available skills](#available-skills) and open a pull request.

## Credits

`ui-design` is distilled from _[Practical UI](https://www.practical-ui.com/)_ by Adham Dannaway and
_[Refactoring UI](https://www.refactoringui.com/)_ by Adam Wathan & Steve Schoger. This project is not affiliated
with or endorsed by the authors — buy the books for the full reasoning and examples.

## License

[MIT](LICENSE) © 2026 Kiet Le
