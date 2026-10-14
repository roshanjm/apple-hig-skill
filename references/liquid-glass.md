# Liquid Glass — the current Apple design system, cross-cutting digest

Liquid Glass is the material and design language Apple introduced at WWDC25 and has refined through iOS/iPadOS/macOS/tvOS/watchOS 26 and 27. Guidance about it is spread across 17 HIG pages; this file gathers every rule in one place. Sources: hig/foundations/materials.md, color.md, layout.md, motion.md, app-icons.md, branding.md, dark-mode.md; hig/components/buttons.md, toolbars.md, tab-bars.md, sidebars.md, scroll-views.md, status-bars.md, widgets.md, virtual-keyboards.md, live-activities.md. Read those pages for the full text.

## 1. The mental model: two layers

- **Content layer** — your app's actual content: lists, photos, text, maps, canvases. Backgrounds here use solid colors or *standard materials* (ultra-thin / thin / regular / thick, plus vibrancy).
- **Functional layer** — controls and navigation (tab bars, toolbars, sidebars, search fields, buttons, sheets' chrome). This layer is made of Liquid Glass and *floats above* the content, which scrolls and peeks through from underneath. The material keeps controls legible while letting content stay visible.
- The whole point is a clear visual distinction between "things you act with" and "things you read". Every rule below protects that distinction.

## 2. Where to use it (and where not)

- **Don't use Liquid Glass in the content layer.** Backgrounds, cards, list rows and media stay on standard materials or solid colors. Putting glass in content creates "unnecessary complexity and a confusing visual hierarchy".
- Exception: controls that live inside content with a transient interactive element (sliders, toggles) take on a glass appearance only while a person is actively using them.
- **Standard system components get Liquid Glass automatically.** Tab bars, toolbars, sidebars, search fields, alerts, popovers, sheets, menus and bar buttons already have the right behavior. Using them is the primary way to adopt the design system.
- **Use custom glass sparingly.** If you apply `glassEffect` to a custom control, limit it to the one or two most important functional elements. Glass exists to bring attention to the content beneath it; many glass pieces compete with the content.

## 3. Regular vs. clear

| Variant | Behavior | Use when |
|---|---|---|
| `regular` | Blurs and adjusts luminosity of what's behind it; scroll edge effects add further blur/opacity reduction | Default. Anything with much text (alerts, sidebars, popovers) or where background content could hurt legibility. Most system components use it. |
| `clear` | Highly translucent; prioritizes visibility of what's behind | Only over visually rich backgrounds such as photos and video, e.g. media playback controls. |

- With clear glass, add a dark dimming layer of **35% opacity** behind the component if the underlying content is bright. Skip the dimming layer if the content is already dark or you use AVKit's standard playback controls (they bring their own).
- Both variants look different when people pick a preferred Liquid Glass look in Settings, or turn on Reduce Transparency / Increase Contrast. Design so legibility holds in all of those states.

## 4. Color on glass

- Liquid Glass has **no inherent color**; it picks up color from the content behind it. Symbols and text on small glass elements (toolbars, tab bars) are **monochromatic by default**, turning darker over light content and lighter over dark content. Larger glass elements such as sidebars are more opaque to stay legible over complex backgrounds.
- **Apply color sparingly** to the material and to symbols/text on it. Reserve it for status indicators and primary actions. The two sanctioned accent spots in chrome are the *selected tab bar item* and the *one prominent button* per view (Color and Branding pages agree on this); everything else in a bar stays monochrome.
- To emphasize a primary action, **put color on the control's background, not on its glyph or label**. That is the system's "prominent" button style (e.g. a tinted Done button). Don't tint the backgrounds of several controls at once.
- **Colorful content under bars?** Prefer a monochrome toolbar/tab bar, or an accent color with clearly different hue from the content. Avoid label colors similar to the content layer's colors. In mostly monochrome apps, using your brand color as the app accent works well.
- **Brand color belongs in the content layer**, where it scrolls beneath the glass and is picked up dynamically, rather than painted across controls (Branding page, refined Sept 2026).
- Check the **resting state** of scrollable content (the top of the screen) for contrast under bars; momentary overlap while scrolling is fine.
- **Provide light and dark variants of every custom color even if your app ships in one appearance**, because glass adapts between light and dark on its own.

## 5. Layout rules that come with glass

- **Differentiate controls from content with the material, not with painted bar backgrounds.** Remove solid or semi-opaque backgrounds beneath bars; use a *scroll edge effect* to lift controls above content.
- **Extend full-screen background content under sidebars, toolbars and tab bars** so it fills the whole window.
- If a full-bleed background image would be hidden under a sidebar or inspector, use the **background extension effect** (`backgroundExtensionEffect()` in SwiftUI, `UIBackgroundExtensionView` in UIKit): it mirrors and blurs the image beneath the adjacent component so it appears to continue.
- Sidebars on iOS, iPadOS and macOS float in the glass layer; either let content scroll horizontally beneath them or apply the background extension effect.
- **Concentric corners.** Standard buttons, text fields, headers and footers in a toolbar have corner radii concentric with the bar's own corners; a custom component in a bar must match. App icon corners match the curvature of other rounded system elements and the device bezel. Live Activities keep even margins concentric to the outer edge and use `ContainerRelativeShape` instead of hard-coded radii.

## 6. Scroll edge effects (iOS, iPadOS, macOS)

- A scroll edge effect is the visual separation between a bar and the scrolling content behind it. Standard bars have it; add it manually only for custom bars that need extra clarity.
- **Prefer the `automatic` style.** It becomes more opaque for top toolbars with many controls, for text that sits outside glass controls, and for pinned table headers. `hard` and `soft` styles exist; if you use `soft`, test legibility thoroughly.
- **Only use a scroll edge effect when a scroll view is behind floating interface elements.** It is not decoration and doesn't darken like an overlay; it exists to keep controls distinct.
- **One scroll edge effect per view.** In split views each pane can have its own; keep their heights consistent so they align.
- Status bar: its background is transparent. Prefer a scroll edge effect to blur what's behind it, keep it readable, and never imply that content behind it is interactive.

## 7. Components with specific Liquid Glass guidance

- **Toolbars** — bar items grouped (`ToolbarItemGroup` / `UIBarButtonItemGroup`), symbols preferred, navigation-bar guidance now lives on the Toolbars page; corner buttons get glass automatically; monochrome labels by default.
- **Tab bars** — float at the bottom over a glass background; content peeks through; on iOS search can be a tab; tab bar can minimize when scrolling in task-oriented screens (see Tab bars page); fill-variant symbols.
- **Sidebars** — float in the glass layer; adaptable sidebar style; updated icon-color guidance (June 2026).
- **Buttons** — prominent style = accent color in the background; glass bar buttons; keep labels monochrome over colorful content.
- **Search fields** — placement in iOS updated, tokens, search as a tab.
- **Alerts / popovers / sheets** — the Materials page names alerts, sidebars and popovers as text-heavy components that use the *regular* variant; the component pages themselves carry no glass-specific wording (Sheets' button placement was updated March 2026).
- **Widgets** — Home Screen widgets have light, dark, **clear** and tinted appearances; clear uses desaturation plus translucency, highlights and a Liquid Glass background (accented rendering mode; `widgetAccentable`).
- **Virtual keyboard accessory views** — if other views use glass, apply it to the custom control container above the keyboard for consistency; a standard toolbar there adopts glass automatically.
- **Menus** — menu items may carry icons (July 2025 / June 2026 guidance); visionOS breakthrough effects.
- **Windows (iPadOS)** — resizable windows, window controls and the menu bar in iPadOS 26+ change how layouts must adapt.

## 8. App icons in the Liquid Glass era

- Icons are **layered**: a background layer plus one or more foreground layers. The system adds specular highlights, refraction and translucency; effects scale with icon size and can change between OS versions.
- Build iOS/iPadOS/macOS/watchOS icons in **Icon Composer**; tvOS and visionOS icons go into an Xcode image stack.
- Provide **square, unmasked layers** (rectangular for tvOS); the system applies rounded-rectangle or circular masks. Pre-masked layers break highlights and look jagged.
- **Don't bake in effects** (highlights, shadows between layers, bevels, blurs, glows). Prefer clearly defined edges, vector layers (SVG/PDF; PNG for raster/mesh gradients), filled overlapping shapes, varied opacity, a simple solid or gradient background.
- iOS/iPadOS/macOS appearances: **default, dark, clear light, clear dark, tinted light, tinted dark**. Keep core features identical across appearances; base dark on light; the system generates any variant you don't supply. Alternate icons need their own variants.
- Canvas: 1024×1024 px (iOS/iPadOS/macOS/visionOS), 800×480 px (tvOS), 1088×1088 px (watchOS). sRGB, Gray Gamma 2.2, or Display P3.

## 9. Motion

- Liquid Glass responds to **direct touch with more emphasis** and to a trackpad with a more subdued effect. The system handles this; custom motion should stay purposeful, brief, cancelable and optional (Reduce Motion).

## 10. Platform notes

- **iOS / iPadOS** — four standard materials remain for the content layer (ultraThin, thin, regular, thick) with vibrant label/fill/separator levels. iPadOS 26+ adds resizable windows, window controls and a menu bar; design responsive layouts.
- **macOS** — same two-layer model; standard `NSVisualEffectView` materials and vibrant system colors in content; behind-window vs within-window blending.
- **tvOS** — glass appears in navigation, Top Shelf and Control Center; image views and buttons adopt glass when focused; standard materials by thickness for overlays.
- **visionOS** — windows use the system *glass* material (adaptive, unmodifiable), there is no Dark Mode, prefer translucency to opaque fills, vibrancy levels for text hierarchy.
- **watchOS** — keep the material backgrounds the system gives modal sheets.
- **iPhone Duo** — bars move to the vertical axis on the outer display; same glass rules apply.

## 11. Adoption checklist for an existing app

1. Replace custom bars and chrome with standard components wherever possible.
2. Delete painted bar backgrounds; rely on the material plus the automatic scroll edge effect.
3. Extend backgrounds under bars; add the background extension effect under sidebars/inspectors.
4. Audit accent color: keep it for one primary action and status; move brand color into content.
5. Limit custom `glassEffect` to the most important one or two elements; choose regular unless over media.
6. Make every custom color a light/dark pair; verify contrast at the resting scroll position.
7. Check custom components inside bars for concentric corner radii.
8. Rebuild the app icon as layers in Icon Composer with all six appearances; remove baked-in effects.
9. Test with Reduce Transparency, Increase Contrast, the alternate Liquid Glass look, light and dark, and colorful content under bars.
10. On iPad, test resizable windows, the menu bar and multiple windows; on iPhone Duo, test every pose.

## 12. Developer references and videos

APIs: `glassEffect(_:in:)`, `Glass.regular`, `Glass.clear`, `backgroundExtensionEffect()`, `UIBackgroundExtensionView`, `ScrollEdgeEffectStyle`, `UIScrollEdgeEffect`, `Material`, `UIVisualEffectView`, `NSVisualEffectView`, `ContainerRelativeShape`, `widgetAccentable(_:)`. Docs: "Adopting Liquid Glass" (Technology Overviews), "Applying Liquid Glass to custom views", "Creating your app icon using Icon Composer".

Videos: Meet Liquid Glass (WWDC25 219); Get to know the new design system (WWDC25 356); Build a SwiftUI app with the new design (323); Build a UIKit app with the new design (284); Build an AppKit app with the new design (310); Say hello to the new look of app icons (220); Create icons with Icon Composer (361); Elevate the design of your iPad app (208); Showcase: how apps are integrating the new design and Liquid Glass (Meet with Apple 208, 116 min) and the short Liquid Glass showcases for LTK, Tide Guide, Slack and CNN. Full list in videos.md.

## 13. Translating to non-native surfaces (web, React Native)

Liquid Glass is a system material; outside UIKit/AppKit/SwiftUI you approximate it. The properties that matter, in order: a functional layer that floats over scrolling content; backdrop blur plus luminosity adaptation (lighter over dark content, darker over light); a monochrome default for glyphs with color reserved for one primary action; a scroll-edge fade instead of a painted bar; concentric corner radii; a subtle specular edge highlight; and respect for Reduce Transparency / Reduce Motion. Keep glass out of cards and content, exactly as on native platforms.
