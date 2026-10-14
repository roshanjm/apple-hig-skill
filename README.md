# Apple HIG skill for Claude

Apple's complete Human Interface Guidelines, packaged as an [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) so Claude quotes Apple's actual rules and numbers instead of guessing.

- **Every HIG page** (173 pages, crawled 2026-10-14) rendered to Markdown, each with its source URL, platform list and "latest change" date.
- **Per-section digests** that keep every rule and number but drop the prose, so Claude reads only what the task needs.
- **The rest of developer.apple.com/design**: the Liquid Glass design system, Apple Design Resources (Figma and Sketch kits, bezels, icon templates), SF Symbols, Icon Composer, Pass Designer, system fonts, the dated What's New changelog since 2022, 192 design videos and the Apple Design Awards.
- **A fixed review template** so "is this HIG compliant?" always comes back as Must fix / Should fix / Consider / Already right, with page citations.
- **Scripts** to re-crawl the site when Apple ships the next update.

Covers iOS, iPadOS, macOS, tvOS, visionOS, watchOS, iPhone Duo and CarPlay as of the iOS 27 / macOS 27 generation.

## What it does once installed

Claude loads the skill on its own whenever a task touches Apple-platform design: HIG, Liquid Glass, Dynamic Type, SF Symbols, app icons, widgets, Live Activities, tab bars, toolbars, sidebars, sheets, alerts, menus, navigation, gestures, accessibility, Apple Pay, Wallet, Sign in with Apple, Siri, WWDC design sessions, or "make it feel native". You do not need to say "HIG".

Prompts that work well:

- "Review this iOS settings screen against the HIG."
- "What does Apple say about tab bars in Liquid Glass? Give me the sizes."
- "Design a visionOS media player that follows Apple's comfort rules."
- "Is a 40×40 tap target OK on iPhone? On watchOS?"
- "Make this React Native screen feel like a native iOS 27 app."
- "When did Apple change the sheet button placement, and to what?"

Answers cite the page they came from ("HIG › Components › Tab bars, last changed 2026-06-08") and keep Apple's imperative phrasing.

## Install

### Claude Code, as a plugin

Inside Claude Code:

```
/plugin marketplace add roshanjm/apple-hig-skill
/plugin install apple-hig@apple-hig-skill
```

Or in one step (Claude Code 2.1.275 or later):

```
/plugin install apple-hig --marketplace roshanjm/apple-hig-skill
```

From a shell:

```bash
claude plugin marketplace add roshanjm/apple-hig-skill
claude plugin install apple-hig@apple-hig-skill
```

Update later with `claude plugin update apple-hig@apple-hig-skill`.

### Claude Code, as a plain skill folder

The repo root *is* the skill folder, so clone it straight into your skills directory.

Personal (every project on this machine):

```bash
git clone --depth 1 https://github.com/roshanjm/apple-hig-skill.git ~/.claude/skills/apple-hig
```

Project (committed with the code, shared with your team):

```bash
git clone --depth 1 https://github.com/roshanjm/apple-hig-skill.git .claude/skills/apple-hig
rm -rf .claude/skills/apple-hig/.git   # or add it as a submodule instead
```

Update with `git -C ~/.claude/skills/apple-hig pull`. Pick one of the two Claude Code methods, not both, or the skill shows up twice.

### claude.ai (web, desktop, mobile)

1. Click **Code → Download ZIP** on this page.
2. In claude.ai open **Settings → Capabilities → Skills** and upload the zip. `SKILL.md` is at the top of the zipped folder, which is what the upload expects.

To build the zip yourself without the `.git` folder:

```bash
git archive --format=zip --prefix=apple-hig/ -o apple-hig.zip HEAD
```

### Claude API

Upload the folder once with the [Skills API](https://platform.claude.com/docs/en/api/skills-guide) and reference the returned skill id in your requests. Every file is sent as a `files[]` part whose filename is its path under `apple-hig/`:

```bash
args=()
while IFS= read -r f; do args+=(-F "files[]=@$f;filename=apple-hig/$f"); done < <(git ls-files)
curl https://api.anthropic.com/v1/skills \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -F "display_title=Apple HIG" "${args[@]}"
```

### Other agents

The folder follows the open [Agent Skills](https://agentskills.io) format (a `SKILL.md` with `name` and `description` frontmatter, plus files it references), so any tool that reads that format can use it as-is.

## How it is organized

Progressive disclosure keeps the context cost low. Only `SKILL.md` (about 3,600 words) loads when the skill triggers. Everything else is read on demand.

| Path | What it holds | When Claude reads it |
|---|---|---|
| `SKILL.md` | The eight design principles, Liquid Glass in twelve rules, the numbers everyone needs (type sizes, hit targets, contrast, icon sizes, scale factors), routing tables, the review template, known gaps | On every trigger |
| `references/foundations.md`, `platforms.md`, `patterns.md`, `inputs.md` | One digest per HIG section | When working in that section |
| `references/components-layout-nav-menus.md`, `components-presentation-input-status.md` | Component digests, one `###` per component | When a component is involved |
| `references/technologies-a-i.md`, `technologies-j-z.md` | Apple Pay, CarPlay, HealthKit, Sign in with Apple, Siri, Wallet, and so on, including the branding rules App Review checks | When a technology is involved |
| `references/liquid-glass.md` | The current design system in one place | For any Liquid Glass question |
| `references/site.md` | Templates, fonts, tools, Apple Design Awards, the design pathway | For resources and tooling |
| `references/changelog.md` | Every dated HIG change since June 2022 | To say when a rule changed |
| `references/videos.md` | All 192 design sessions with a "start here" list | For WWDC sessions |
| `references/INDEX.md` | Every page with abstract, platforms and last-changed date | To find the right page |
| `references/hig/<section>/<slug>.md` | The full text of all 173 pages | When the surrounding prose or a platform section is needed |
| `scripts/` | The crawler and renderer | Only when refreshing |

## Keeping it current

Apple ships large HIG updates at WWDC in June, at the September hardware event, and in the December and March point releases. The What's New page is the signal that a refresh is due.

```bash
scripts/refresh.sh
```

That re-crawls the DocC JSON behind the site (about two minutes, needs network) and renders fresh pages into a temporary folder. Copy them into `references/hig/`, rebuild `INDEX.md`, then regenerate the digests. The digests are written by hand or by an agent, not by the scripts, so they must be redone after each refresh. Python 3.10 or later, no third-party packages.

## Known gaps

The site renders a few table cells as images, which the JSON crawl cannot carry. Those cells are blank in the pages: the system color RGB swatches, the standard-icon glyph column, tvOS focus-state names, modifier-key glyphs, and some button images on the technology pages. `SKILL.md` lists every one of them and tells Claude to say "look at the live page" rather than "Apple gives no value". Per-device screen sizes and safe-area insets are no longer on the Layout page; Apple moved them into the downloadable design templates.

## Versions

| Version | Crawl date | Notes |
|---|---|---|
| 1.0.0 | 2026-10-14 | First release. Covers the June 2026 design principles, iPhone Duo, the September 2026 Layout and Branding rewrites, and the October 2026 Widgets and Live Activities updates. |

## License

The skill files written for this repository (`SKILL.md`, the digests under `references/*.md`, `scripts/`, this README) are MIT licensed. The rendered HIG pages under `references/hig/` are Apple's text, reproduced for reference; see [NOTICE.md](NOTICE.md). This project is not affiliated with or endorsed by Apple Inc.
