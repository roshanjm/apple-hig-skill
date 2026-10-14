# developer.apple.com/design — site map, resources, tools, awards

Everything on the Apple design site outside the HIG itself, as of 2026-10-14. Use this file to point people at the right download, template, font, tool or video, and to know what the Design Pathway recommends.

## Site map

| Section | URL | What's there | In this skill |
|---|---|---|---|
| Design overview | https://developer.apple.com/design/ | Entry page: HIG, Resources, Icon Composer, SF Symbols, Pass Designer, Reality Composer Pro, featured videos, developer stories, ADA, Pathway | this file |
| What's New | https://developer.apple.com/design/whats-new/ | Dated feed of HIG changes, resource releases, videos, articles (June 2022 → today) | changelog.md |
| Get Started (Design Pathway) | https://developer.apple.com/design/get-started/ | Curated learning path | below |
| Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | 173 pages: Getting started, Foundations, Patterns, Components, Inputs, Technologies | INDEX.md + hig/ |
| Resources | https://developer.apple.com/design/resources/ | UI kits, icon templates, technology templates, fonts, tools, product bezels | below |
| Apple Design Awards | https://developer.apple.com/design/awards/ (+ /2025/, /2024/) | Winners and finalists per year and category | below |
| SF Symbols | https://developer.apple.com/sf-symbols/ | The SF Symbols Mac app and library | below + hig/foundations/sf-symbols.md |
| Icon Composer | https://developer.apple.com/icon-composer/ | Tool for layered Liquid Glass app icons | below + hig/foundations/app-icons.md |
| Pass Designer | https://developer.apple.com/pass-designer/ | Tool for Wallet passes | below + hig/technologies/wallet.md |
| Fonts | https://developer.apple.com/fonts/ (+ /system-fonts/) | SF and NY downloads, system font list | below + hig/foundations/typography.md |
| Design videos | https://developer.apple.com/videos/design/ | 192 WWDC / Tech Talk / Meet with Apple sessions | videos.md |

## Design Pathway (Apple's recommended order for newcomers)

1. **Learn the building blocks** — watch *The qualities of great design* (WWDC18 801), *Essential design principles* (WWDC17 802), *Design foundations from idea to interface* (WWDC25 359).
2. **Interface with the HIG** — start with Getting started → Foundations → Patterns → Components → Inputs → Technologies.
3. **Assemble your toolbox** — download Apple Design Resources (fonts, icons, bezels, Figma/Sketch/Photoshop/Keynote templates) and the SF Symbols app.
4. **Produce your prototypes** — *Prototyping: Fake it till you make it* (WWDC14 223), *60-second prototyping* (WWDC17 818), *Design with SwiftUI* (WWDC23 10115).
5. **Get inspiration** — What's New articles, Apple Design Awards, *10 Questions with Design Evangelism*, *Meet the prototypers*.
6. **Go further** — design videos, Meet with Apple design labs and workshops, Developer Centers, WWDC.

## Apple Design Resources (developer.apple.com/design/resources/)

### UI kits (current)

| Platform | Kit version | Formats |
|---|---|---|
| iOS & iPadOS | iOS 27 / iPadOS 27 UI Kit | Figma (community file 1651309003795292092), Sketch |
| iOS, iPadOS, watchOS | App Icon Template (27) | Figma (1645923469870515372), Sketch, Photoshop + Illustrator (.dmg) |
| macOS | macOS 27 UI Kit | Figma (1651309434229735362), Sketch |
| tvOS | tvOS 18 UI Kit, Design Templates, Production Templates | Sketch library, Sketch .dmg, Photoshop .dmg |
| watchOS | watchOS 26 UI Kit | Figma (1540060090060216489), Sketch |
| visionOS | visionOS 26 UI Kit; visionOS 2 kit and templates still listed | Figma (1540071341298017505), Sketch |

The iOS/iPadOS and macOS kits were "rebuilt from the ground up" in June 2025 for Liquid Glass (materials, app icons, system colors, Home Screen / Lock Screen / Control Center / Widgets / Notifications) and updated June and September 2026 for the 27 releases.

### Technology templates and assets

| Asset | Formats | HIG page |
|---|---|---|
| App Clips design template | Figma, Sketch | hig/technologies/app-clips.md |
| Apple Pay design template | Figma, Sketch | hig/technologies/apple-pay.md |
| Live Activities template | Figma, Sketch | hig/components/live-activities.md |
| Messages (iMessage apps and stickers) template | Figma, Sketch | hig/technologies/imessage-apps-and-stickers.md |
| Sign in with Apple buttons + logo | Figma, Sketch; PNG/PDF/SVG logo | hig/technologies/sign-in-with-apple.md |
| Siri and App Shortcuts template; Siri icons | Figma, Sketch; PNG | hig/technologies/siri.md, hig/components/app-shortcuts.md |
| Tap to Pay on iPhone template | Figma, Sketch | hig/technologies/tap-to-pay-on-iphone.md |
| TipKit template | Figma, Sketch | hig/patterns/offering-help.md |
| Wallet template | Figma, Sketch | hig/technologies/wallet.md |
| Camera Control template | Sketch | hig/inputs/camera-control.md |
| Glyphs / badges: AirPlay (PDF), ARKit badge and glyph (PDF), Apple Health icon (PNG), HomeKit icon and glyph (PNG/PDF), Games and Game Center (PNG/PDF), Add Apple Watch Face (PNG/PDF/SVG) | — | airplay.md, augmented-reality.md, healthkit.md, homekit.md, game-center.md, watch-faces.md |
| Badges and logos for marketing (Apple Pay, Wallet, Music, Health…) | https://developer.apple.com/licensing-trademarks/ | hig/foundations/branding.md |

### Product bezels (Photoshop + PNG, for marketing; follow the App Store Marketing Guidelines)

Apple TV · Apple Watch Ultra 3 (2025) · Apple Watch Ultra 2 (2024) · Apple Watch Series 11 · Studio Displays · iMac (M4) · iPad (A16) · iPad Air (M4) · iPad mini (A17 Pro) · iPad Pro (M5) · iPhone Duo · iPhone 18 · iPhone 17 · iPhone 16 · MacBook Air M5 · MacBook Pro M5 · MacBook Neo · iPhone and iPad bezels for Keynote live video.

### Parallax image tools

Parallax Previewer app (v2 for macOS 13.5+, v1 for 10.10.5+) and the Parallax Exporter Photoshop plug-in preview layered images for tvOS and visionOS. User guide: https://help.apple.com/itc/parallaxpreviewer/

## Fonts (developer.apple.com/fonts/)

| Family | Role | Facts |
|---|---|---|
| SF Pro | System font for iOS, iPadOS, macOS, tvOS, visionOS | 9 weights incl. italics, 4 widths (incl. Condensed, Compressed, Expanded), rounded variant, variable optical sizes, 150+ languages (Latin, Greek, Cyrillic) |
| SF Compact | System font for watchOS | Optimized for small sizes and narrow columns; rounded variant (complications use SF Compact Rounded) |
| SF Mono | Monospaced (Xcode) | 6 weights; Latin, Greek, Cyrillic |
| New York | Serif companion | 6 weights, variable optical sizes; text face small, display face large |
| SF Arabic, SF Armenian, SF Georgian, SF Hebrew | Script extensions | 9 weights, rounded variant, optical sizes, tuned to sit with SF Pro |

Downloads: https://devimages-cdn.apple.com/design/resources/download/SF-Pro.dmg (SF-Compact, SF-Mono, NY, SF-Arabic, SF-Armenian, SF-Georgian, SF-Hebrew follow the same pattern). Don't embed system fonts in an app; use `Font.Design.default` / `.serif` / `.rounded` / `.monospaced`. The full list of preinstalled and downloadable fonts per platform is at https://developer.apple.com/fonts/system-fonts/. Behaviours worth knowing: dynamic tracking per point size, proportional numerals by default, vertically centered colon when showing time, size-specific features applied automatically by each OS.

## SF Symbols app (developer.apple.com/sf-symbols/)

- Library of **7,000+ symbols** in **9 weights** and **3 scales**, aligned with San Francisco; localized designs for 20+ scripts; automatic RTL adaptation.
- Current release: SF Symbols 27 (macOS Sonoma or later); SF Symbols 8 beta shipped June 2026, SF Symbols 7 at WWDC25.
- Features: **Enhanced Search** (semantic, describe what you want); **Draw On / Draw Off** animations (Whole Symbol, By Layer, Individually playback) with annotation tools and guide points; **Variable Rendering** (Variable Color, Variable Draw) for progress/strength; animation presets Bounce, Wiggle, Rotate, Breathe, Pulse, Scale, Appear/Disappear, Replace, **Magic Replace**; four rendering modes (Monochrome, Hierarchical, Palette, Multicolor) plus optional **gradient** rendering; export templates to make custom symbols; component library for enclosures/badges.
- Terms: don't use symbols (or confusingly similar images) in app icons, logos or trademarks; Apple-product symbols can't be customized.
- Videos: What's new in SF Symbols 7 (WWDC25 337), What's new in SF Symbols 6 (WWDC24 10188). Design rules: hig/foundations/sf-symbols.md; action-to-symbol table: hig/foundations/icons.md.

## Icon Composer (developer.apple.com/icon-composer/)

- Creates **layered app icons out of Liquid Glass** from one design for iPhone, iPad, Mac and Apple Watch; multi-layer `.icon` format annotated across **Default, Dark and Mono** rendering modes; exports a flattened icon for marketing; syncs into Xcode.
- Controls per layer or group: **refraction** (edge bend to lens-like distortion), **specular highlights** (inside/outside/automatic; vertical light from above), translucency, shadows. Shared grid and consistent enclosure shapes across platforms; a single design by default, customizable per platform.
- Icon Composer 2 beta (June 2026) re-renders imported files with sharper material. Requires macOS Tahoe 26.4 or later; also bundled with Xcode.
- Videos: Say hello to the new look of app icons (WWDC25 220), Create icons with Icon Composer (WWDC25 361), Icon Composer for Beginners Group Lab (WWDC26). Rules: hig/foundations/app-icons.md.

## Pass Designer (developer.apple.com/pass-designer/)

Beta Mac app (macOS 27+) for Apple Wallet passes: start from Apple or custom templates, bring in logos/backgrounds/strip images, edit background/foreground/label colors, edit standard fields, real-time preview using the same renderer as iOS and watchOS, validation of required keys, **semantic tags** for boarding passes and event tickets (dates, venues, flights → Siri Suggestions, Calendar, Maps), automatic backward-compatible pass structure. Rules: hig/technologies/wallet.md.

## Reality Composer Pro

Beta tool to iterate, preview and prepare 3D content for visionOS; Reality Composer Pro 3 adds ScriptGraph for no-code interactions (WWDC26 252). Rules: hig/foundations/immersive-experiences.md, hig/foundations/spatial-layout.md.

## Apple Design Awards

Categories: Delight and Fun · Inclusivity · Innovation · Interaction · Social Impact · Visuals and Graphics (2024 also had Spatial Computing). Each category has an app winner and a game winner plus finalists. Useful as reference points when someone asks for "an app Apple considers well designed".

### 2026 winners (finalists in parentheses)

| Category | App | Game |
|---|---|---|
| Delight and Fun | grug — Ocho (Blippo+ — Panic; Metaballs — Apposite) | Is This Seat Taken? — Poti Poti Studio (Ball x Pit; PowerWash Simulator) |
| Inclusivity | Guitar Wiz — Bijoy Thangaraj (Hearing Buddy; Structured) | Pine Hearts — Hyper Luminal (Sago Mini Jinja's Garden; Civilization VII) |
| Innovation | NBA: Live Games & Scores (visionOS) (D-Day: The Camera Soldier; Detail: AI Video Editor) | Blue Prince — Dogubomb (Pickle Pro; TR-49) |
| Interaction | Moonlitt: Moon Phase Tracker — Flipping Hues (The Outsiders; Tide Guide) | Sago Mini Jinja's Garden (Grand Mountain Adventure 2; TR-49) |
| Social Impact | Primary: News in Depth (visionOS) (Katha Room; Harvee) | Consume Me (Despelote; Spilled!) |
| Visuals and Graphics | Tide Guide: Charts & Tables — Condor Digital ((Not Boring) Camera; Caradise) | Cyberpunk 2077 Ultimate Edition — CD PROJEKT RED (Arknights: Endfield; SILT) |

Apple's 2026 write-ups single out Moonlitt and Tide Guide for "best-in-class Liquid Glass integration".

### 2025 winners

| Category | App | Game |
|---|---|---|
| Delight and Fun | CapWords — HappyPlan Tech | Balatro — LocalThunk |
| Inclusivity | Speechify | Art of Fauna — Klemens Strasser |
| Innovation | Play — Rabbit 3 Times | PBJ — The Musical — Philipp Stollenmayer |
| Interaction | Taobao | DREDGE — Black Salt Games |
| Social Impact | Watch Duty: Wildfire Maps | Neva — Devolver Digital |
| Visuals and Graphics | Feather: Draw in 3D — Sketchsoft | Infinity Nikki — Infold Games |

Finalists 2025: Lumy, Denim, Thank Goodness You're Here!, Prince of Persia: The Lost Crown, Evolve, Train Fitness, puffies., Land of Livia, Moises, Capybara AI Meeting Translator, Pawz, Gears & Goo, iA Writer, Mela, Skate City: New York, Ground News, Opal, Ahoy! From Picardy, Vocabulary, CellWalk, Control Ultimate Edition.

### 2024 winners

| Category | App | Game |
|---|---|---|
| Delight and Fun | Bears Gratitude — Isuru Wanasinghe | NYT Games |
| Inclusivity | oko — AYES | Crayola Adventures — RED GAMES CO |
| Innovation | Procreate Dreams — Savage Interactive | Lost in Play — Happy Juice Games |
| Interaction | Crouton — Devin Davies | Rytmos — Floppy Club |
| Social Impact | Gentler Streak Fitness Tracker — Gentler Stories | The Wreck — The Pixel Hunt |
| Visuals and Graphics | Rooms — Things Inc. | Lies of P — NEOWIZ |
| Spatial Computing | djay — Algoriddim | Blackbox — Shapes and Stories |

Finalists 2024: Rooms, Dudel Draw, WHAT THE CAR?, Hello Kitty Island Adventure, Complete Anatomy 2024, Tiimo, Unpacking, quadline, Copilot Money, SmartGym, Wavelength, Call of Duty: Warzone Mobile, Arc Search, Little Nightmares, finity., How We Feel, Ahead, Cityscapes, The Bear, Sunlitt, Meditate, DEATH STRANDING DIRECTOR'S CUT, Honkai: Star Rail, Sky Guide, NBA, Synth Riders, Loóna.

## Developer stories and articles linked from the design site

- How Klemens Strasser prioritized inclusivity with Art of Fauna — https://developer.apple.com/news/?id=dgmr27r7
- A sit-down interview with the creators of Is This Seat Taken? — https://developer.apple.com/news/?id=z12xq8fa
- grug team make app good — https://developer.apple.com/news/?id=ux44ymcr
- Behind the appealing design of CapWords — https://developer.apple.com/articles/capwords/
- 10 Questions with Design Evangelism — https://developer.apple.com/news/?id=s8sl4tpa
- Meet the prototypers — https://developer.apple.com/news/?id=97dgimaa
- Behind the Design series (The Wreck, Rooms, and others) — see changelog.md "articles" rows.
