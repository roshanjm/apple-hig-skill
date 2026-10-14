---
name: apple-hig
description: Apple's complete Human Interface Guidelines and the whole developer.apple.com/design site (crawled 2026-10-14 — 173 HIG pages, Liquid Glass design system, Apple Design Resources, SF Symbols, Icon Composer, fonts, What's New changelog, 192 design videos, Apple Design Awards) with exact specs. Use this whenever you design, build, review, critique or "make it feel native" for any Apple platform — iOS, iPadOS, macOS, tvOS, visionOS, watchOS, iPhone Duo, CarPlay — or a web / React Native UI that is meant to look and behave like Apple's own apps. Trigger on any mention of HIG, Liquid Glass, Apple design language, Dynamic Type, SF Symbols, SF Pro, app icons, widgets, Live Activities, tab bars, toolbars, sidebars, sheets, alerts, menus, navigation, gestures, accessibility on Apple devices, Apple Pay / Wallet / Sign in with Apple / Siri UI, "what does Apple say about…", "is this HIG compliant", "Apple design templates / Figma kit / fonts", or WWDC design sessions — even if the user doesn't say "HIG".
---

# Apple HIG (Human Interface Guidelines) — the skill

This skill is Apple's own design guidance, not a paraphrase of it. Every page of the HIG is bundled in full under `references/hig/`, condensed into per-section digests under `references/*.md`, and summarized here. Treat the full pages as the source of truth; this file tells you which rules matter most and where to look.

## How to use it (progressive disclosure)

1. **Start here** for the principles, the Liquid Glass model, the numbers everyone needs, and the routing table.
2. **Read the digest** for the section you're working in (`references/foundations.md`, `platforms.md`, `patterns.md`, `components-*.md`, `inputs.md`, `technologies-*.md`). Each digest keeps every rule and every number from the pages, minus the prose. Expect 300–1400 lines; list the sections first with `grep -n '^##\+ '` (component digests nest pages as `###` under group `##` headings) and read only what you need. Digest bullets lightly shorten Apple's bold lead-ins, so when you grep a full page for a rule, search by a distinctive keyword rather than the digest's wording.
3. **Open the full page** (`references/hig/<section>/<slug>.md`) when you need the surrounding prose, the platform section, or a rule the digest only summarizes. The numbers in this file and in the digests are verbatim from the pages and can be quoted with the page name without re-opening it. `references/INDEX.md` lists every page with its abstract, platform list and last-changed date (use that date in review headers). Each page carries its source URL, section, platform list and date of last change, so you can cite it.
4. Cross-cutting references: `references/liquid-glass.md` (the current design system in one place), `references/site.md` (templates, fonts, tools, awards, pathway), `references/changelog.md` (every dated change since 2022), `references/videos.md` (all design sessions).

When answering, name the page you relied on ("HIG › Components › Tab bars") and keep Apple's imperative phrasing; people act on these rules. Don't invent numbers — if a value isn't in the pages, say so.

## Working alongside other design skills

- `apple-hig` (this skill) = what Apple says, for native platforms, with specs. Treat it as canonical for structure, behavior, sizes and accessibility.
- A motion / web-implementation skill (for example one distilled from Apple's WWDC "fluid interfaces" talks) owns *how* to implement springs, gestures and interruptible transitions on the web.
- A brand or product design-system skill owns color, type identity and component tokens.
When they conflict, follow brand tokens for color/type identity and this skill for everything else.

## The eight design principles (June 2026)

Apple reintroduced explicit principles with WWDC26. They are the tie-breakers for every other rule.

| Principle | One line | Rules it carries |
|---|---|---|
| **Purpose** | Make something meaningful. | Create value; keep focused on the few features that matter; find new ways to solve the problem. |
| **Agency** | Let people do things their own way. | Stay out of the way; let people explore (skippable flows); help people recover from mistakes. |
| **Responsibility** | Act in people's best interest. | Be fully transparent about what the product does and why; keep people's information safe. |
| **Familiarity** | Build on what people know. | Use known concepts; keep visuals and interactions consistent; provide clear feedback. |
| **Flexibility** | Adapt to diverse contexts and needs. | Design for everyone; preserve context across platforms; support many input methods; treat each platform with intention. |
| **Simplicity** | Be clear and direct. | Include just what's necessary ("simplicity isn't minimalism"); be concise; establish hierarchy. |
| **Craft** | Care about every detail. | Quality sets the tone; experiment and iterate; maintain craft after shipping. |
| **Delight** | Make it human. | Identify the emotion; create defining moments; don't mistake delight for decoration; consider the whole. |

## Liquid Glass in twelve rules

Full digest: `references/liquid-glass.md`. The design system since WWDC25; most component pages were rewritten for it between June 2025 and October 2026.

1. Two layers: **content** (standard materials, solid colors) and a floating **functional layer** of Liquid Glass for controls and navigation. Content scrolls and peeks through underneath.
2. **Never put Liquid Glass in the content layer** (cards, backgrounds, rows). Only sliders/toggles take on glass while being used.
3. **Standard components get it for free.** Use them. Custom `glassEffect` is for one or two key elements, not a theme.
4. Pick **regular** (blurred, luminosity-adjusted; default; anything with text) or **clear** (very translucent; only over photos/video; add a 35% dark dimming layer when the content is bright).
5. Glass has **no color of its own**. Glyphs and text on toolbars and tab bars are monochrome by default (dark over light content, light over dark).
6. **Color is for one primary action and for status.** Tint the *background* of the prominent button (Done), not its label; never tint several controls.
7. **Brand color goes in the content layer**, where glass picks it up, not across chrome. Over colorful content prefer monochrome bars.
8. **No painted bar backgrounds.** Use the automatic **scroll edge effect** to separate bars from content; one effect per view; it is not decoration.
9. **Extend content under bars and sidebars**; mirror-blur full-bleed images under them with the background extension effect.
10. **Concentric corners**: anything inside a bar, Live Activity or icon matches the container's radius.
11. **Every custom color ships as a light/dark pair**, even in single-appearance apps; test Reduce Transparency and Increase Contrast.
12. **App icons are layered** (background + foregrounds, square unmasked layers, no baked-in effects) built in Icon Composer with default, dark, clear and tinted appearances.

## Numbers you will need constantly

All from the Foundations pages; the full tables (every Dynamic Type size, tracking per point size, every platform) are in `references/foundations.md` and `references/hig/foundations/typography.md`.

**Text size (points)** — default / minimum: iOS & iPadOS 17 / 11 · macOS 13 / 10 · tvOS 29 / 23 · visionOS 17 / 12 · watchOS 16 / 12. Avoid Ultralight/Thin/Light weights. Support text enlargement to at least 200% (140% on watchOS).

**iOS/iPadOS text styles at the default (Large) size** — size/leading, emphasized weight:
Large Title 34/41 Bold · Title 1 28/34 Bold · Title 2 22/28 Bold · Title 3 20/25 Semibold · Headline 17/22 Semibold (already semibold) · Body 17/22 · Callout 16/21 · Subhead 15/20 · Footnote 13/18 · Caption 1 12/16 · Caption 2 11/13 (Semibold emphasis for Headline and below). Sizes run from xSmall through xxxLarge and AX1–AX5 (Body reaches 53 pt at AX5).

**macOS text styles** — Large Title 26/32 · Title 1 22/26 · Title 2 17/22 · Title 3 15/20 · Headline 13/16 Bold · Body 13/16 · Callout 12/15 · Subheadline 11/14 · Footnote 10/13 · Caption 1 10/13 · Caption 2 10/13 Medium. macOS has no Dynamic Type.

**Controls** — default / minimum hit size: iOS & iPadOS 44×44 / 28×28 · macOS 28×28 / 20×20 · tvOS 66×66 / 56×56 · visionOS 60×60 / 28×28 · watchOS 44×44 / 28×28. Padding: about 12 pt around bezeled elements, about 24 pt around elements without a bezel. visionOS: button centers at least 60 pt apart, 16 pt or more between them; never overlap interactive elements.

**Contrast** — 4.5:1 for text up to 17 pt; 3:1 at 18 pt or for bold; aim for 7:1 with custom colors in Dark Mode. Never rely on color alone.

**Layout** — Determine layout from size classes (compact/regular × horizontal/vertical), never from device type or orientation. Respect safe areas (Dynamic Island, camera housing, bars). tvOS: inset content 60 pt top/bottom and 80 pt sides; grids use 40 pt horizontal spacing and 100 pt minimum vertical spacing. watchOS: at most three glyph buttons or two text buttons in a row. macOS: nothing critical at the bottom of a window. iPhone Duo: compact-width layout for the outer display, regular-width for the inner; bars move to the vertical axis.

**Images** — scale factors: iOS @2x and @3x; iPadOS and watchOS @2x; macOS and tvOS @1x and @2x; visionOS @2x or higher (prefer vectors). PNG for raster, JPEG/HEIC for photos, PDF/SVG for flat artwork, stereo HEIC for spatial photos. Include a color profile; P3 for wide color.

**App icons** — 1024×1024 px square (iOS, iPadOS, macOS, visionOS), 800×480 px (tvOS), 1088×1088 px (watchOS); system masks to rounded rectangle (iOS/iPadOS/macOS/tvOS) or circle (visionOS/watchOS). No text unless essential; no photos; no Apple hardware; no replicated UI.

**SF Symbols** — 9 weights matching SF, 3 scales (small, medium, large); outline for toolbars and lists, fill for iOS tab bars and selection; four rendering modes plus gradients; animations (Bounce, Scale, Pulse, Variable Color, Replace / Magic Replace, Wiggle, Breathe, Rotate, Draw On/Off). Standard action symbols: `plus` Add, `ellipsis` More, `square.and.arrow.up` Share, `magnifyingglass` Search, `line.3.horizontal.decrease` Filter, `trash` Delete, `square.and.pencil` Compose, `pencil` Rename, `checkmark` Done, `xmark` Cancel, `arrow.uturn.backward` Undo, `person.crop.circle` Account (full table: `hig/foundations/icons.md`).

**visionOS** — immersion styles mixed / progressive (120°–360°) / full; a 1.5 m boundary ends progressive and full experiences; keep content in the field of view; avoid motion at the periphery and sustained oscillation near 0.2 Hz; prefer indirect gestures.

**Games** — initial download playable within 30 minutes; support each platform's default input (touch on iPhone/iPad, keyboard + mouse/trackpad on Mac, remote on tvOS, eyes and hands on visionOS) and offer alternatives to physical controllers.

## Foundations — the rules most often broken

Digest: `references/foundations.md`. Pages: accessibility, app-icons, branding, color, dark-mode, icons, images, immersive-experiences, inclusion, layout, materials, motion, privacy, right-to-left, sf-symbols, spatial-layout, typography, writing.

- **Accessibility** is a foundation, not a feature: Dynamic Type, VoiceOver labels on every custom icon and symbol, Reduce Motion (tighten springs, track gestures, replace x/y/z transitions with fades, don't animate into blurs), no auto-dismissing timed UI, alternatives to every gesture, Voice Control and Full Keyboard Access, Assistive Access layouts (one task per screen, confirm destructive actions twice). Ship Accessibility Nutrition Labels.
- **Color**: use system and semantic colors; never redefine a semantic color's meaning; don't hard-code system values; test light, dark and Increased Contrast; mind cultural meanings; prefer system color pickers.
- **Dark Mode**: never offer an app-level appearance toggle; use base vs elevated backgrounds; soften white image backgrounds; separate light/dark assets only when needed; SF Symbols adapt automatically.
- **Typography**: system text styles first; minimize typefaces; custom fonts must support Dynamic Type and Bold Text; keep hierarchy as sizes grow (stack instead of truncating); loose leading for long passages, never tight leading for three or more lines.
- **Layout**: reading-order hierarchy, alignment and indentation, grouping, progressive disclosure; same functionality across size classes; preview smallest and largest layouts first.
- **Materials**: semantics over looks; vibrant colors on materials; thicker materials for text contrast.
- **Motion**: purposeful, brief, cancelable, optional; don't animate frequent interactions; feedback motion follows the gesture that caused it.
- **Branding**: accent color judiciously; familiar components; branding defers to content; no logo everywhere; no launch-screen branding; respect Apple trademarks.
- **Writing**: a voice, then tone by context; verbs on buttons ("Send", not "Let's do it!"); consistent capitalization; no "we"; clear next steps in empty states; error messages say how to fix, no "oops"; purpose strings are one active sentence ending in a period.
- **Privacy**: request only what a feature needs, at the moment it's needed; purpose strings explain how data is used; pre-permission screens have one button ("Continue"/"Next"), no incentives, no fake alerts; passkeys over passwords; keychain for secrets.
- **Inclusion**: plain language, "you" not "the user", no idioms or humor that won't translate, gender-neutral imagery and copy, diverse people and settings, universal security questions.
- **Right to left**: flip navigation and progress controls and text-direction icons; never flip logos, universal marks, real-world objects or the digits inside a number; bump Arabic/Hebrew up about 2 pt next to all-caps Latin.

## Platforms — what defines each (digest: `references/platforms.md`)

| Platform | Distance / posture | Primary input | What to prioritize |
|---|---|---|---|
| iOS | in hand, 1–2 ft | Multi-Touch, virtual keyboard, voice | few onscreen controls, reachability (bottom/middle), swipe back and row actions, adapts to orientation/Dark Mode/Dynamic Type, uses device capabilities with permission |
| iPadOS | held or on a stand, ~3 ft | touch + keyboard, trackpad, Apple Pencil | large-display layouts, fewer modals, resizable windows and the menu bar, multitasking, drag and drop, combined inputs |
| macOS | stationary at a desk, 1–3 ft | keyboard, pointer, game controllers | density without strain, resizable/hide-able windows, full menu bar, keyboard shortcuts, precision editing, personalization |
| tvOS | 8+ ft from the couch | Siri Remote, controllers, voice | focus system (expand on focus), edge-to-edge artwork, cinematic motion, infrequent sign-in, multiuser |
| visionOS | seated/standing, content brought to you | eyes + indirect hand gestures | Shared Space first, minimum immersion that suits the moment, comfort (field of view, no peripheral motion), Spatial Audio, SharePlay |
| watchOS | wrist raise, <1 ft | Digital Crown, tap/swipe, Action button | glanceable single-screen tasks, shallow hierarchy, complications and notifications over the app itself |
| iPhone Duo | folding phone, many poses | touch | size-class driven layouts, reserved regions (cameras, fold), bars on the vertical axis, arrangement views (split / overlay), same functionality in every pose |

## Components — route and cross-cutting rules

Digests: `references/components-layout-nav-menus.md` (Content: Charts, Image views, Text views, Web views · Layout and organization: Boxes, Collections, Column views, Disclosure controls, Labels, Lists and tables, Lockups, Outline views, Split views, Tab views · Menus and actions: Activity views, Buttons, Context menus, Dock menus, Edit menus, Home Screen quick actions, Menus, Ornaments, Pop-up buttons, Pull-down buttons, The menu bar, Toolbars · Navigation and search: Path controls, Search fields, Sidebars, Tab bars, Token fields) and `references/components-presentation-input-status.md` (Presentation: Action sheets, Alerts, Page controls, Panels, Popovers, Scroll views, Sheets, Windows · Selection and input: Color wells, Combo boxes, Digit entry views, Image wells, Pickers, Segmented controls, Sliders, Steppers, Text fields, Toggles, Virtual keyboards · Status: Activity rings, Gauges, Progress indicators, Rating indicators · System experiences: App Shortcuts, Complications, Controls, Live Activities, Notifications, Snippets, Status bars, Top Shelf, Watch faces, Widgets).

Rules that apply to every component:
- Prefer the system component; customize appearance only when behavior, sizing and placement stay familiar. Don't rebuild a system control to change one color.
- Pick the component by *semantics*: alert for critical interruptions with a decision; action sheet for a choice triggered by an action; sheet for a scoped task; popover (iPad/Mac) for transient context; menu for commands; context menu for item-specific actions.
- Labels: title-case button labels with a verb; symbol plus title for bar items so overflow menus have text; `ellipsis` is reserved for the system overflow.
- Give every control an accessibility label and a minimum hit area; keep destructive actions separated and confirmable.
- Follow the pages' platform sections: the same component often differs on macOS (pull-down vs pop-up, panels, menu bar) and watchOS (full-screen modals, Digital Crown).

## Patterns — route (digest: `references/patterns.md`)

Charting data · Collaboration and sharing · Drag and drop · Entering data · Feedback · File management · Going full screen · Launching (restore state, no splash branding) · Live-viewing apps · Loading (show progress, download large assets in the background) · Managing accounts (delay sign-in; Sign in with Apple; account deletion) · Managing notifications · Modality (minimize it; keep tasks simple; always provide an obvious exit) · Multitasking · Offering help (TipKit) · Onboarding (fast, skippable, teach through use) · Playing audio · Playing haptics · Playing video · Printing · Ratings and reviews (ask after value, never interrupt) · Searching (search as tab on iOS, scoped search, tokens) · Settings (system Settings for permissions; in-app for preferences) · Undo and redo · Workouts.

## Inputs — route (digest: `references/inputs.md`)

Action button · Apple Pencil and Scribble · Camera Control · Digital Crown · Eyes · Focus and selection · Game controls · Gestures (standard gesture table; don't repurpose system gestures; alternatives to multi-finger gestures) · Gyroscope and accelerometer · Keyboards (standard shortcuts table; don't override system shortcuts) · Nearby interactions · Pointing devices (pointer effects, hover) · Remotes · Virtual keyboards (keyboard types, input accessory views with Liquid Glass).

## Technologies — route (digests: `references/technologies-a-i.md`, `references/technologies-j-z.md`)

AirPlay · Always On · App Clips · Apple In-App Purchase (renamed Sept 2026) · Apple Pay · Augmented reality · CareKit · CarPlay · Game Center · Generative AI (new June 2025; let people refine results and give feedback during generation; choose the model type deliberately) · HealthKit · HomeKit · iCloud · ID Verifier · iMessage apps and stickers · Live Photos · Mac Catalyst · Machine learning · Maps · NFC · Photo editing · ResearchKit · ShazamKit · SharePlay · Sign in with Apple (button rules and sizes) · Siri (revised for Siri AI, June 2026) · Tap to Pay on iPhone · VoiceOver · Wallet (Pass Designer, poster tickets, pass image dimensions). These pages also carry the mandatory branding/badge rules that App Review checks.

## Resources, tools and what's new (digest: `references/site.md`)

- **Templates**: iOS/iPadOS 27, macOS 27, watchOS 26, visionOS 26, tvOS 18 UI kits for Figma and Sketch; app icon templates; technology templates (App Clips, Apple Pay, Live Activities, Messages, Sign in with Apple, Siri/App Shortcuts, Tap to Pay, TipKit, Wallet, Camera Control); product bezels through iPhone 18 and iPhone Duo.
- **Fonts**: SF Pro, SF Compact, SF Mono, New York, SF Arabic/Armenian/Georgian/Hebrew. Never embed system fonts; use `Font.Design`.
- **Tools**: SF Symbols app (7,000+ symbols; Enhanced Search; Draw animations; Variable Rendering), Icon Composer (layered Liquid Glass icons; needs macOS 26.4+), Pass Designer (Wallet passes; macOS 27 beta), Reality Composer Pro, Parallax Previewer.
- **What's new**: `references/changelog.md` has every dated change since June 2022 — use it to say *when* a rule changed (e.g. Sheets button placement March 2026; Design principles, Snippets, Siri AI, search-as-tab June 2026; iPhone Duo, Layout, Branding September 2026; Widgets and Live Activities October 2026).
- **Videos**: `references/videos.md` — 192 sessions; the "start here" list covers the Liquid Glass era.

## Reviewing a design against the HIG

When asked to review, critique or "check against Apple guidelines", produce this and nothing looser:

```
# HIG review — <screen / component / flow>
Platform(s): …   Reviewed against: HIG pages <list>, last changed <dates>

## Must fix (violates a stated rule)
- [Page › Section] Rule quoted or tightly paraphrased. → What is wrong here. → The change to make.

## Should fix (contradicts best practice)
- …

## Consider (judgment calls, platform conventions, Liquid Glass adoption)
- …

## Already right
- Short list, so the reader keeps what works.
```

Rank by user impact. Quote numbers (sizes, contrast, spacing) from the pages. If the surface is web or React Native, say which rules are native-only (materials, system components) and which still apply (hierarchy, sizes, contrast, motion, writing, accessibility).

## Building a new screen or component

1. Name the platform(s) and size classes; pull the platform row above and `platforms.md`.
2. Choose system components by semantics (section above) and read their digest entries; note platform differences.
3. Apply the Liquid Glass layer model: content vs chrome, scroll edge effect, accent color only on the primary action.
4. Set type with system text styles, controls at default sizes, 12/24 pt padding, safe areas, Dynamic Type growth plan.
5. Write the copy per the Writing rules; label every control for VoiceOver.
6. Run the review template on your own output before handing it over.

## Known gaps in the crawl (don't mistake a blank for "no value")

The site renders a few table cells as images, which the JSON crawl can't carry. Blank cells in these places mean "look at the live page", not "Apple gives no value":

- `hig/foundations/color.md` › Specifications: the system color and iOS gray RGB swatches (light/dark/increased-contrast values). Use the API names (`Color.blue`, `systemGray2`…) and the Figma/Sketch UI kits for values; Apple also warns not to hard-code them.
- `hig/foundations/icons.md` › Standard icons: the glyph column; symbol names are present.
- `hig/inputs/focus-and-selection.md`: tvOS focus-state names; `hig/inputs/keyboards.md`: modifier-key glyphs; `hig/inputs/pointing-devices.md`: pointer pictures.
- Technology pages (Apple Pay, ID Verifier, AirPlay, HomeKit): button-image and do/don't icon columns; the digests label those rows from the rule text and say so.
- `hig/foundations/layout.md` no longer carries per-device screen sizes and safe-area insets (Apple moved them to the downloadable Apple Design Resources templates; the page's change log still mentions them). `hig/foundations/typography.md` has no visionOS size table, only prose. `hig/components/activity-rings.md`: ring color swatches blank. `hig/technologies/sign-in-with-apple.md`: the button-title list was an image (titles are Sign in / Sign up / Continue with Apple).
- Figure captions sometimes survive as bare bold lines (e.g. "**Outer display**"); the page `designing-for-ios.md` links a `spatial-interactions` slug that now lives at `hig/inputs/nearby-interactions.md`.

## Keeping the skill current

Crawled 2026-10-14 from the DocC JSON behind the site (`scripts/crawl_hig.py`, `scripts/docc_to_md.py`, `scripts/refresh.sh`). The What's New feed is the signal that a refresh is due; Apple ships large HIG updates each WWDC (June), each September hardware event, and in December/March point releases.
