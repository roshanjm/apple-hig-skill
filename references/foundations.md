# Foundations — HIG digest

The Foundations section of Apple's Human Interface Guidelines (crawled 2026-10-14, Liquid Glass era) covers the cross-cutting design fundamentals every Apple-platform app builds on: accessibility, app icons, branding, color, Dark Mode, interface icons, images, immersive experiences, inclusion, layout, materials, motion, privacy, right-to-left, SF Symbols, spatial layout, typography, and writing. The full page renders live in `hig/foundations/<slug>.md`; this digest keeps every rule and every number from those pages but drops the examples, imagery and explanatory prose.

## Accessibility
Full page: hig/foundations/accessibility.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
An accessible interface is intuitive, perceivable (never relies on one sense), and adaptable (supports system accessibility features). Audit with Accessibility Inspector; declare support with Accessibility Nutrition Labels in App Store Connect.

**Rules**
- **Support larger text sizes.** Let people enlarge text by at least 200 percent (140 percent in watchOS), via Dynamic Type or custom UI.
- **Use recommended defaults for custom type sizes.** Follow each platform's default/minimum (table below); thin-weight custom fonts need larger-than-recommended sizes.
- **Strive to meet color contrast minimum standards.** WCAG AA values (table below); if not met by default, provide a higher-contrast scheme when Increase Contrast is on; check both light and dark appearances.
- **Prefer system-defined colors.** They have accessible variants that adapt to Increase Contrast and light/dark.
- **Convey information with more than color alone.** Add shapes or icons; consider letting people customize color schemes (chart colors, game characters).
- **Describe your app's interface and content for VoiceOver.**
- **Support text-based ways to enjoy audio and video.** Captions (synced text), subtitles (translated dialogue), audio descriptions (narration in pauses), transcripts (complete text); let people customize their presentation.
- **Use haptics in addition to audio cues.** Pair success/error sounds with matching haptics; Music Haptics and Audio graphs on iOS/iPadOS.
- **Augment audio cues with visual cues**, especially for off-screen content in games and spatial apps.
- **Offer sufficiently sized controls.** Meet the per-platform minimum control size (table below).
- **Consider spacing between controls as important as size.** About 12 pt padding around bezelled elements; about 24 pt around the visible edges of elements without a bezel.
- **Support simple gestures for common interactions.** Avoid custom multifinger and multihand gestures for frequent actions.
- **Offer alternatives to gestures.** Core functionality must be reachable by more than one physical interaction (e.g., a button in addition to swipe-to-dismiss).
- **Let people use Voice Control**; label interface elements appropriately.
- **Integrate with Siri and Shortcuts** so tasks can be done by voice alone, the Action button, Home Screen or Control Center.
- **Support mobility-related assistive technologies**: VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control, Switch Control; test and label elements.
- **Let people use the keyboard alone** (Full Keyboard Access); avoid overriding system keyboard shortcuts.
- **Support Switch Control** (external hardware, game controllers, or sounds).
- **Keep actions simple and intuitive.** Prefer system gestures over custom ones people must learn.
- **Minimize use of time-boxed interface elements.** Prefer explicit dismissal over auto-dismiss timers.
- **Consider offering difficulty accommodations in games** (reduced completion criteria, reaction time, control assistance).
- **Let people control audio and video playback.** Never autoplay without discoverable start/stop controls; consider a global opt-out.
- **Allow people to opt out of flashing lights**: respond to the Dim Flashing Lights setting in video playback.
- **Be cautious with fast-moving and blinking animations.** With Reduce Motion on: reduce automatic/repetitive animation, zooming, scaling and peripheral motion; tighten springs to reduce bounce; track animations directly with gestures; avoid animating z-axis depth changes; replace x/y/z transitions with fades; avoid animating into and out of blurs.
- **Optimize your app's UI for Assistive Access.** Remove noncritical workflows/UI, one interaction per screen, and always ask for confirmation twice before hard-to-recover actions like deleting a file.

**Platform notes**
- iOS/iPadOS, macOS, tvOS, watchOS: no additional considerations.
- visionOS: offers hand and head Pointer Control and Zoom. **Prioritize comfort**: keep elements within the field of view, prefer horizontal layouts to vertical (neck strain), don't demand attention in different locations in quick succession; reduce speed/intensity of animated objects, especially peripheral; be gentle with camera/video motion; avoid head-anchored content (feels confining and blocks Pointer Control); minimize large and repetitive gestures.

**Specs**

| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

| Text size | Text weight | Minimum contrast ratio |
|---|---|---|
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |

| Platform | Default control size | Minimum control size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Padding: ~12 pt around bezelled elements, ~24 pt around unbezelled elements. Text enlargement target: 200% (watchOS 140%).

**Dev refs**
Accessibility Inspector, Accessibility Nutrition Labels (App Store Connect), Accessibility framework, Selecting subtitles and alternative audio tracks (AVFoundation), Music Haptics, Audio graphs, Voice Control, Switch Control, Performing accessibility testing for your app, Animated images, UIAccessibility.isVideoAutoplayEnabled, Flashing lights (MediaAccessibility), Assistive Access, Support Full Keyboard Access in your iOS app (WWDC21)

## App icons
Full page: hig/foundations/app-icons.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Layered app icons receive Liquid Glass effects (specular highlights, refraction, translucency) on iOS, iPadOS, macOS and watchOS; tvOS icons use 2–5 parallax layers; visionOS icons use a background plus one or two upper layers. Build iOS/iPadOS/macOS/watchOS icons in Icon Composer; tvOS/visionOS layers go into an Xcode image stack.

**Rules**
- **Prefer clearly defined edges in foreground layers.** Avoid soft or feathered edges so system highlights and shadows render well.
- **Vary opacity in foreground layers** to increase depth and liveliness; import opaque layers and adjust transparency in Icon Composer.
- **Design a background that both stands out and emphasizes foreground content.** Gradients must respond well to system lighting; Icon Composer supports solid colors and gradients, so custom background images are rarely needed — if imported, make them full-bleed and opaque.
- **Prefer vector graphics (SVG or PDF) for layers**; outline artwork and convert text to outlines; use PNG only for mesh gradients and raster artwork.
- **Produce appropriately shaped, unmasked layers.** Square layers for iOS/iPadOS/macOS (system rounds corners), square for visionOS/watchOS (system applies circular mask), rectangular for tvOS. Pre-masked layers harm specular highlights and look jagged.
- **Keep primary content centered** to avoid truncation under masking, especially on visionOS and watchOS; use the grids in the app icon production templates.
- **Embrace simplicity**: one concept, minimal shapes, simple solid or gradient background; don't fill the whole canvas.
- **Provide a visually consistent icon design across all platforms** you support.
- **Consider basing the design around filled, overlapping shapes** paired with transparency and blurring for depth.
- **Include text only when essential**; avoid words like "Watch", "Play", "New", "For visionOS"; a mnemonic first letter is acceptable; in tvOS keep text above other layers so parallax doesn't crop it.
- **Prefer illustrations to photos and avoid replicating UI components**; avoid extremely thin line weights and sharp corners; don't use screenshots.
- **Don't use replicas of Apple hardware products** (copyrighted).
- **Let the system handle blurring and other visual effects.** Don't bake in specular highlights, inter-layer drop shadows, bevels, blurs or glows; if you add custom effects, test them in Icon Composer, Device Hub, or on device.
- **Create layer groupings to apply effects to multiple layers at once**; groups get extra Liquid Glass controls (specular, refraction, translucency).
- **Keep your icon's features consistent across appearances** (default, dark, clear, tinted); don't swap elements between variants.
- **Design dark and tinted icons that feel at home beside system icons**; dark icons are more subdued, clear and tinted even more so.
- **Use your light icon as the basis for your dark icon**; complementary colors, no excessively bright images; color backgrounds give the most contrast in dark icons.
- **Consider offering alternate app icons** (iOS, iPadOS, tvOS, compatible apps on visionOS); keep each closely related to your content and never confusable with another app. Alternate icons on iOS/iPadOS require their own dark, clear and tinted variants and are subject to App Review.

**Platform notes**
- iOS/iPadOS, macOS: no additional considerations.
- tvOS: **Include a safe zone** — focus scaling/motion may crop edges; foreground layers are cropped more than background layers.
- visionOS: **Avoid shapes meant to look like a hole or concave area** in the background layer; system shadows and highlights make them stand out instead of recede.
- watchOS: **Avoid black icon backgrounds**; lighten them so the icon doesn't blend into the display.

**Specs**

| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
|---|---|---|---|---|---|
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

Layer counts: tvOS 2–5 layers; visionOS background + 1–2 layers. The system scales the icon for smaller contexts (Settings, notifications). Color spaces: sRGB (color), Gray Gamma 2.2 (grayscale), Display P3 (wide-gamut; iOS, iPadOS, macOS, tvOS, watchOS only).

**Dev refs**
Icon Composer, Creating your app icon using Icon Composer, Configuring your app icon using an asset catalog, Parallax Previewer / Parallax Exporter (Apple Design Resources), Device Hub, App Review Guidelines (design)

## Branding
Full page: hig/foundations/branding.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Express brand through voice, color, type and components while staying at home on the platform; the App Store offers additional branding surfaces (App Store Marketing Guidelines).

**Rules**
- **Use your brand's unique voice and tone in all written communication.**
- **Apply your app's accent color judiciously.** Minimize it on controls; reserve it for primary actions or status (unread badges, selected tab). To express brand color, move it into the content layer where it scrolls beneath Liquid Glass controls and is picked up dynamically.
- **Consider using a custom font** only if legible at all sizes and supporting Bold Text and Dynamic Type; custom for headlines/subheads with system fonts for body and captions works well.
- **Express your brand with familiar components.** If customizing, preserve sizing, placement and behavior appropriate to the platform.
- **Ensure branding always defers to content.** Don't spend screen space on elements that only display a brand asset.
- **Help people feel comfortable by using standard patterns consistently**: expected UI locations, standard symbols, conventional navigation and modality.
- **Resist displaying your logo throughout the app** unless essential for context.
- **Avoid using a launch screen as a branding opportunity**; use a welcome or onboarding screen instead.
- **Follow Apple's trademark guidelines.** No Apple trademarks in app name or images.

**Platform notes**
- No additional considerations on any platform.

**Dev refs**
App Store Marketing Guidelines, Apple Trademark List, Guidelines for Using Apple Trademarks, Launch screens (Launching), Onboarding

## Color
Full page: hig/foundations/color.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
System colors adapt to appearance, vibrancy and accessibility settings; dynamic semantic colors describe purpose (label, separator, background) rather than value. Liquid Glass has no inherent color by default and takes color from the content behind it.

**Rules**
- **Avoid using the same color to mean different things** (e.g., brand color for interactive borderless buttons and for noninteractive text).
- **Make sure all colors work in light, dark and increased-contrast contexts.** Custom colors need light and dark variants plus an increased-contrast option for each; even single-appearance apps must supply both light and dark colors to support Liquid Glass adaptivity.
- **Test your color scheme under a variety of lighting conditions** (bright: darker/muted; dark: brighter/saturated; visionOS: surroundings reflect into colors).
- **Test on different devices**: True Tone (specify a white point adaptivity style for reading/photo/video/gaming apps); multiple HD/4K TVs for tvOS; P3 vs sRGB profiles on Mac.
- **Consider how artwork and translucency affect nearby colors** (e.g., Maps switches to a dark scheme in satellite mode).
- **Prefer system-provided color controls** (ColorPicker) if people choose colors.
- **Avoid relying solely on color to differentiate objects, indicate interactivity or communicate essential information**; add text labels or glyph shapes.
- **Avoid colors that make content hard to perceive** (insufficient contrast, color-blind-indistinguishable pairs).
- **Consider how colors are perceived in other cultures** (e.g., red is danger in some, positive in others — Stocks uses green for gains in English, red in Chinese).
- **Avoid hard-coding system color values**; values fluctuate between releases — use the Color APIs.
- **Avoid redefining the semantic meanings of dynamic system colors** (don't use separator as text color or secondaryLabel as a background).
- **Apply color sparingly to the Liquid Glass material and to symbols or text on it.** Reserve it for status indicators or primary actions; to emphasize a primary action apply color to the glass background (as the system does for prominent buttons such as Done), not to the symbol or text; don't color the background of multiple controls.
- **Avoid similar colors in control labels when the app has a colorful background.** With colorful backgrounds or rich content, prefer monochromatic toolbars and tab bars or an accent with sufficient differentiation; with mostly monochromatic content, the brand color works well as the accent color.
- **Be aware of color placement in the content layer.** Avoid overlapping similar colors between content and controls; the default/resting state (top of a scrollable screen) must stay clearly legible even if colorful content scrolls under controls intermittently.
- **Apply color profiles to your images**; sRGB is accurate on most displays.
- **Use wide color (Display P3) on compatible displays**: Display P3 profile at 16 bits per pixel per channel, export as PNG; a wide-color display is required to design P3 content.
- **Provide color-space-specific image and color variations if necessary** via the asset catalog (similar P3 colors or P3 gradients can clip on sRGB).

**Platform notes**
- iOS/iPadOS: two dynamic background sets — *system* (systemBackground, secondarySystemBackground, tertiarySystemBackground) and *grouped* (systemGroupedBackground, secondarySystemGroupedBackground, tertiarySystemGroupedBackground; use for grouped table views). Primary = overall view, secondary = grouping within the view, tertiary = grouping within secondary elements. Foreground dynamic colors: label, secondaryLabel, tertiaryLabel, quaternaryLabel, placeholderText, separator (translucent), opaqueSeparator, link.
- macOS: dynamic system colors (Developer palette of the Color panel): alternateSelectedControlTextColor, alternatingContentBackgroundColors, controlAccentColor, controlBackgroundColor, controlColor, controlTextColor, currentControlTint, disabledControlTextColor, findHighlightColor, gridColor, headerTextColor, highlightColor, keyboardFocusIndicatorColor, labelColor, linkColor, placeholderTextColor, quaternaryLabelColor, secondaryLabelColor, selectedContentBackgroundColor, selectedControlColor, selectedControlTextColor, selectedMenuItemTextColor, selectedTextBackgroundColor, selectedTextColor, separatorColor, shadowColor, tertiaryLabelColor, textBackgroundColor, textColor, underPageBackgroundColor, unemphasizedSelectedContentBackgroundColor, unemphasizedSelectedTextBackgroundColor, unemphasizedSelectedTextColor, windowBackgroundColor, windowFrameTextColor. App accent color (macOS 11+) applies to buttons, selection highlighting and sidebar icons only while General > Accent color is *multicolor*; otherwise the user's chosen color replaces it, except fixed-color sidebar icons.
- tvOS: **Consider a limited palette that coordinates with your app logo.** **Avoid using only color to indicate focus** — scaling and responsive animation are primary.
- visionOS: **Use color sparingly, especially on glass** (surroundings show through and affect legibility). **Prefer color in bold text and large areas.** **In fully immersive experiences keep brightness levels balanced**; avoid a bright object on a very dark/black background, especially if it flashes or moves. visionOS system colors use the default dark values.
- watchOS: **Use background color to support content or supply information** (e.g., Activity ring colors), not as flourish; avoid full-screen background color in long-lived views (workouts, audio playback). **Expect graphic complications to be shown in tinted mode** (single wearer-selected color).

**Specs**
System colors (SwiftUI `Color`): red, orange, yellow, green, mint, teal, cyan, blue, indigo, purple, pink, brown — each with default light/dark and increased-contrast light/dark variants (the crawl's swatch cells carry no RGB values). iOS/iPadOS grays (UIKit): systemGray, systemGray2, systemGray3, systemGray4, systemGray5, systemGray6; SwiftUI `gray` = systemGray. Wide color: Display P3 at 16 bits per channel, PNG.

**Dev refs**
Color (SwiftUI), UIColor (UIKit), NSColor / Color (AppKit), ColorPicker, UIWhitePointAdaptivityStyle, UIColor.label / secondaryLabel / tertiaryLabel / quaternaryLabel / placeholderText / separator / opaqueSeparator / link, UIColor.systemBackground family, UIColor.systemGroupedBackground family, NSColor.controlAccentColor

## Dark Mode
Full page: hig/foundations/dark-mode.md · Platforms: iOS, iPadOS, macOS, tvOS
Systemwide dark palette with brighter foregrounds and higher perceptual contrast; not supported in visionOS or watchOS. Dark colors are not simple inversions of light ones.

**Rules**
- **Avoid offering an app-specific appearance setting**; respect the systemwide choice.
- **Ensure your app looks good in both appearance modes**, including the Auto setting that may switch while the app runs.
- **Test legibility in both modes** with Increase Contrast and Reduce Transparency on, separately and together.
- **In rare cases, consider a dark-only appearance** (e.g., immersive media viewing, Stocks).
- **Embrace colors that adapt to the current appearance**: semantic colors (labelColor, controlColor, separator) or Color Set assets with light and dark variants; no hard-coded or non-adapting colors.
- **Aim for sufficient contrast in all appearances**: at minimum 4.5:1; strive for 7:1 for custom foreground/background pairs, especially small text.
- **Soften the color of white backgrounds** in content images so they don't glow in Dark Mode.
- **Use SF Symbols wherever possible**; they adapt automatically with dynamic colors or vibrancy.
- **Design separate interface icons for light and dark if necessary** (e.g., an outline needed in only one appearance).
- **Make sure full-color images and icons look good in both appearances**; supply separate light/dark assets in the asset catalog when needed.
- **Use the system label colors** (primary, secondary, tertiary, quaternary).
- **Use system views to draw text fields and text views** so vibrancy is handled automatically.

**Platform notes**
- iOS/iPadOS: Dark Mode has *base* (dimmer, receding) and *elevated* (brighter, advancing) background sets; the system switches to elevated automatically for foreground interfaces such as popovers and sheets, between apps in multitasking, and between windows. **Prefer the system background colors** so these distinctions survive.
- macOS: with the graphite accent, windows pick up desktop color (*desktop tinting*). **Include some transparency in custom component backgrounds** only on components with a visible background or bezel and only in neutral (non-colored) states, so colored states don't fluctuate with the desktop.
- tvOS: no additional considerations. visionOS, watchOS: Dark Mode not supported.

**Specs**
Minimum contrast 4.5:1; target 7:1 for custom colors and small text.

**Dev refs**
NSColor.labelColor, NSColor.controlColor, UIColor.separator, Color Set assets (Xcode asset catalog), SF Symbols

## Icons
Full page: hig/foundations/icons.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Interface icons (glyphs) express one concept with streamlined shapes; both custom glyphs and SF Symbols use black and clear to define shape and receive system color. Prefer SF Symbols; design custom ones to match.

**Rules**
- **Create a recognizable, highly simplified design** using familiar visual metaphors.
- **Maintain visual consistency across all interface icons**: consistent size, detail level, stroke weight and perspective; adjust dimensions per icon for equal visual weight.
- **In general, match the weights of interface icons and adjacent text.**
- **Add padding to achieve optical alignment if necessary** (asymmetric icons look off-center when geometrically centered; bake the offset into the asset's padding).
- **Provide a selected-state version only if necessary**; toolbars, tab bars and buttons handle selection automatically.
- **Use inclusive images**: gender-neutral figures, culturally recognizable imagery.
- **Include text only when essential** (e.g., text-formatting glyphs); localize individual characters; use abstract text representations and provide RTL-flipped versions.
- **Use a vector format (PDF or SVG) for custom icons** so the system scales them; PNG needs multiple resolutions. Alternatively create a custom SF Symbol and pick a scale that matches adjacent text.
- **Provide alternative text labels (accessibility descriptions) for custom icons.**
- **Avoid replicas of Apple hardware**; if required, use only Apple Design Resources images or the Apple-product SF Symbols.

**Platform notes**
- iOS/iPadOS, tvOS, visionOS, watchOS: no additional considerations.
- macOS document icons: supply any combination of background fill, center image and text; the system composites them onto the folded-corner shape (default is app icon + extension if you supply nothing). **Design simple images that clearly communicate the document type** (can render as small as 16x16 px). **A single expressive background image** can replace a center image. **Reduce complexity in small versions** (fewer/thicker grid lines at 32x32; none at 16x16). **Avoid important content in the top-right corner** of the fill (folded corner drawn on top). **Center image measures half the icon canvas** (16x16 canvas for a 32x32 icon). **Define a margin of about 10% of the canvas** — image occupies about 80% (205x205 px in a 256x256 canvas). **Specify a succinct term** instead of an unfamiliar extension (e.g., *scene* for scn); the system scales and capitalizes it.

**Specs**
macOS document icon background fill sizes: 512x512 px @1x / 1024x1024 px @2x; 256x256 @1x / 512x512 @2x; 128x128 @1x / 256x256 @2x; 32x32 @1x / 64x64 @2x; 16x16 @1x / 32x32 @2x. Center image sizes: 256x256 @1x / 512x512 @2x; 128x128 @1x / 256x256 @2x; 32x32 @1x / 64x64 @2x; 16x16 @1x / 32x32 @2x. Margin ≈10% of canvas; image ≈80%.

Standard SF Symbols for common actions (names as listed in the crawl; blank entries had no name in the source):

| Group | Action → symbol |
|---|---|
| Editing | Cut `scissors` · Copy `document.on.document` · Paste `document.on.clipboard` · Done `checkmark` · Save (none listed) · Cancel `xmark` · Close (none listed) · Delete `trash` · Undo `arrow.uturn.backward` · Redo `arrow.uturn.forward` · Compose `square.and.pencil` · Duplicate `plus.square.on.square` · Rename `pencil` · Move to `folder` · Folder (none listed) · Attach `paperclip` · Add `plus` · More `ellipsis` |
| Selection | Select `checkmark.circle` · Deselect `xmark` · Close (none listed) · Delete `trash` |
| Text formatting | Superscript `textformat.superscript` · Subscript `textformat.subscript` · Bold `bold` · Italic `italic` · Underline `underline` · Align Left `text.alignleft` · Center `text.aligncenter` · Justified `text.justify` · Align Right `text.alignright` |
| Search | Search `magnifyingglass` · Find `text.page.badge.magnifyingglass` · Find and Replace / Find Next / Find Previous / Use Selection for Find (none listed) · Filter `line.3.horizontal.decrease` |
| Sharing and exporting | Share `square.and.arrow.up` · Export (none listed) · Print `printer` |
| Users and accounts | Account `person.crop.circle` · User / Profile (none listed) |
| Ratings | Dislike `hand.thumbsdown` · Like `hand.thumbsup` |
| Layer ordering | Bring to Front `square.3.layers.3d.top.filled` · Send to Back `square.3.layers.3d.bottom.filled` · Bring Forward `square.2.layers.3d.top.filled` · Send Backward `square.2.layers.3d.bottom.filled` |
| Other | Alarm `alarm` · Archive `archivebox` · Calendar `calendar` |

**Dev refs**
SF Symbols app, Apple Design Resources, VoiceOver (HIG), Right to left (HIG)

## Images
Full page: hig/foundations/images.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
A point is an abstract unit (pixels per point vary by display; in visionOS a point is an angular value). Bitmap images need a scale factor (@1x = 1:1, @2x = 2:1, @3x = 3:1) for every device you support.

**Rules**
- **Provide high-resolution assets for all bitmap images for every device you support**, naming them @1x/@2x/@3x in the asset catalog (table below).
- **Design images at the lowest resolution and scale up**; place vector control points on whole values so they align to the raster grid at 1x, 2x and 3x.
- **Include a color profile with each image.**
- **Always test images on a range of actual devices** (pixelation, stretching, compression).
- **Use standard interface elements to display layered images** (tvOS) so focus APIs such as FocusState apply parallax automatically.
- **Identify logical foreground, middle and background elements** (tvOS): prominent elements in front, secondary content and shadows in the middle, opaque backdrop behind.
- **Generally, keep text in the foreground** layer (tvOS).
- **Keep the background layer opaque** (tvOS) — a non-opaque background is an error.
- **Keep layering simple and subtle** (tvOS); excessive 3D effects look unrealistic.
- **Leave a safe zone around foreground layers** (tvOS); focus scaling crops edges.
- **Always preview layered images** in Xcode, Parallax Previewer (macOS) or Parallax Exporter (Photoshop), then on a real TV.
- **Create a layered app icon** for visionOS (two to three layers).
- **Prefer vector-based art for 2D images** in visionOS; bitmaps may not scale well.
- **If you must use rasterized images in visionOS, balance quality with performance**: @2x is fine at common distances but fixed; higher resolutions help close viewing but cost file size and runtime performance, especially over @6x; apply high-quality image filtering above @2x.
- **Make sure spatial photos render correctly**: use stereo HEIC with spatial metadata so visionOS applies comfort treatments.
- **Prefer the feathered glass background effect for text over spatial photos** (GlassBackgroundEffect).
- **Take visual comfort into account when making spatial photos from 2D content** (disparity adjustment can cause discomfort from some viewing positions).
- **Display spatial photos and spatial scenes in standalone views** (sheet or window), not inline; if inline stereoscopic images are unavoidable, give generous spacing.
- **Use spatial scenes for specific moments** — each takes several seconds to generate; avoid many at once; use scroll views, pagination or explicit actions.
- **When displaying immersively, prefer minimal UI** (single caption, single Back button, swipe navigation).
- **Prefer larger spatial scenes centered in the field of view**; small scenes give little parallax.
- **In general, avoid transparency to keep image files small** (watchOS), except in template images (complications, menu icons, interface icons) where the system uses it to apply color.
- **Use autoscaling PDFs** (watchOS): design for the 40mm and 42mm screens at 2x; WatchKit scales per device (table below).

**Platform notes**
- iOS/iPadOS, macOS: no additional considerations.
- tvOS: layered images (2–5 layers) are required for the app icon and strongly encouraged for other focusable images including Top Shelf; parallax elevates, sways and illuminates the focused element, dims out-of-focus content after inactivity. Runtime layered images downloaded from a server must be `.lcr` files generated with `layerutil`; don't embed them.
- visionOS: images display over a wider range of sizes; the system scales resolution dynamically; pixels may not align 1:1 with screen pixels.
- watchOS: see transparency and autoscaling PDF rules above.

**Specs**

| Platform | Scale factors |
|---|---|
| iPadOS, watchOS | @2x |
| iOS | @2x and @3x |
| visionOS | @2x or higher (see visionOS) |
| macOS, tvOS | @1x and @2x |

| Image type | Format |
|---|---|
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that don't require full 24-bit color | An 8-bit color palette |
| Photos | JPEG files, optimized as necessary, or HEIC files |
| Stereo or spatial photos | Stereo HEIC |
| Flat icons, interface icons, and other flat artwork that requires high-resolution scaling | PDF or SVG files |

watchOS autoscaling PDF image scale:

| Screen size | Image scale |
|---|---|
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

tvOS layered images: 2 to 5 layers, opaque background. visionOS raster: @2x baseline; performance impact notable over @6x.

**Dev refs**
FocusState (SwiftUI), layerutil, Parallax Previewer User Guide, ImagePresentationComponent (RealityKit), GlassBackgroundEffect (SwiftUI), Creating spatial photos and videos with spatial metadata (ImageIO), CALayer.filters, Drawing sharp layer-based content in visionOS, Images (SwiftUI), UIImageView (UIKit), NSImageView (AppKit)

## Immersive experiences
Full page: hig/foundations/immersive-experiences.md · Platforms: visionOS
Apps launch in the Shared Space (alongside other apps) or a Full Space (alone) and can move between them. Passthrough shows real surroundings; the Digital Crown recenters content (press and hold) or briefly shows passthrough (double-click). Immersion styles: `mixed`, `progressive`, `full`.

**Rules**
- **Use dimmed passthrough to bring attention to your content** (SurroundingsEffect); passthrough tints black by default and can take a custom tint.
- **Create unbounded 3D experiences** with `mixed` immersion in a Full Space; no boundary — nearby content becomes semi-opaque when a person gets too close to a physical object.
- **Use `progressive` immersion to blend a custom environment with surroundings**; Digital Crown adjusts immersion within the default 120- to 360-degree range or a custom range; portrait or landscape; ~1.5-meter boundary.
- **Use `full` immersion for a 360-degree environment** that fully replaces passthrough; ~1.5-meter boundary.
- **Offer multiple ways to use your app or game** and support accessibility features.
- **Prefer launching in the Shared Space or in `mixed` immersion** so people choose when to increase immersion.
- **Reserve immersion for meaningful moments and content**; let people immerse per task (e.g., examining one photo).
- **Help people engage with key moments regardless of immersion level** using dimming, tinting, motion, scale and Spatial Audio; start subtle, strengthen only with good reason.
- **Prefer subtle tint colors for passthrough** (visionOS 2+); avoid bright or dramatic tints.
- **Be mindful of visual comfort**: keep 3D content within the field of view; display motion comfortably.
- **Choose an immersion style that supports the movements people might make**; avoid `progressive`/`full` (or return to `mixed`) if people may need to move beyond the 1.5-meter boundary.
- **Avoid encouraging people to move** in progressive or full immersion; bring objects to them instead.
- **If you use `mixed`, avoid obscuring passthrough too much**; switch to `full` or `progressive` if virtual objects would block the view substantially.
- **Adopt ARKit to blend custom content with surroundings** (hand positions, room data) and request permission for that data.
- **Design smooth, predictable transitions when changing immersion**; no sudden, jarring changes.
- **Let people choose when to enter or exit immersion** with a clear action (e.g., Keynote's Exit button); don't require system controls to reduce immersion.
- **Indicate the purpose of an exit control** (back to a less immersive context vs. quit); offer pause/save before quitting.
- **Prefer virtual hands that match familiar characteristics** (positions and gestures of the viewer's hands).
- **Use caution with virtual hands larger than the viewer's hands** (occlude content, feel clumsy, seem too close).
- **If hand-tracking data is interrupted, fade out virtual hands and reveal the viewer's own hands**; fade back in when data returns.
- **Minimize distracting content in environments**; use highest-quality assets where attention belongs, lower quality and dimming elsewhere.
- **Help people distinguish interactive objects** — proximity signals interactivity.
- **Keep animation subtle** (drifting clouds); avoid motion near field-of-view edges.
- **Create an expansive environment**; small restrictive spaces feel claustrophobic.
- **Use Spatial Audio to create atmosphere**; avoid repetition/looping; lower or stop the soundscape when other audio plays.
- **In general, avoid a flat 360-degree image** as an environment; prefer lit object meshes with shader-driven subtle animation.
- **Help people feel grounded**: always provide a ground plane mesh.
- **Minimize asset redundancy**; repeated models feel less realistic.

**Platform notes**
- Not supported in iOS, iPadOS, macOS, tvOS or watchOS.

**Specs**
System boundary for `progressive` and `full`: about 1.5 meters from the initial head position (experience fades as the head nears it; beyond it, visuals are replaced by the app icon until the wearer returns or recenters). `progressive` default immersion range: 120 to 360 degrees. `full`: 360-degree environment.

**Dev refs**
ImmersionStyle (automatic, mixed, progressive, full), SurroundingsEffect, ARKit, SceneReconstructionProvider, CoordinateSpaceProtocol, Immersive spaces (SwiftUI), Creating fully immersive experiences in your app, Incorporating real-world surroundings in an immersive experience, Digital Crown (HIG)

## Inclusion
Full page: hig/foundations/inclusion.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Inclusive design examines copy, images and experiences from many perspectives (age, gender identity, race and ethnicity, sexuality, physical and cognitive attributes, permanent/temporary/situational disabilities, language and culture, religion, education, political opinions, social and economic context). Inoffensive is not the same as inclusive.

**Rules**
- **Consider the tone of your copy from different perspectives**; be clear, direct and respectful (an academic tone can feel exclusive).
- **Pay attention to how you refer to people**: use *you*/*your*; avoid *the user*/*the player*; reserve *we*/*our* for your software or company.
- **Avoid specialized or technical terms without defining them**; plain language reads and translates better.
- **Replace colloquial expressions with plain language** (culture-specific, hard to translate, sometimes exclusionary — e.g., "peanut gallery", "grandfathered in").
- **Consider carefully before including humor** (subjective, hard to translate, tiring on repeat).
- **Be approachable**: present a clear, straightforward interface and build in ways to learn (onboarding that can be skipped).
- **Avoid unnecessary references to specific genders** in copy ("Subscribers can post recipes" rather than "his or her"), and in avatars, emoji, glyphs and characters; let people customize them.
- **Use a nongendered human image for a generic person** (SF Symbols person/figure glyphs).
- **If you must collect gender**, offer inclusive options (nonbinary, self-identify, decline to state) and consider letting people specify pronouns.
- **Portray a range of human characteristics and activities** (race, body type, age, physical capability); avoid stereotyped occupations or hero/villain tropes.
- **Review the settings and objects you show**; prefer familiar, relatable places, homes, activities and items over conspicuous affluence.
- **Avoid stereotypes and assumptions** (e.g., a narrow definition of *family*; security questions that assume college, cars or sight — prefer universal experiences like favorite activity or first friend's name).
- **Support accessibility features** (VoiceOver, Display Accommodations, closed captioning, Switch Control, Speak Screen); never assume a disability prevents someone wanting your experience. Each disability is a spectrum; everyone experiences temporary and situational disabilities.
- **Avoid images and language that exclude people with disabilities**; include them in representations; don't use disability as a negative descriptor.
- **Take a people-first approach when writing about disability**; find out how people self-identify.
- **Prioritize simplicity and perceivability** across sight, hearing and touch.
- **Internationalize first, then localize**; inclusive writing eases localization. Use SF Symbols (language-specific and LTR/RTL glyphs).
- **Check color meanings per locale** (white = grief in some places, purity/peace in others).

**Platform notes**
- No additional considerations on any platform.

**Dev refs**
Localization (Xcode), Writing inclusively / Writing about disability (Apple Style Guide), Expanding your app to new markets, SF Symbols, Onboarding (HIG)

## Layout
Full page: hig/foundations/layout.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Layout gives structure through reading order, alignment, grouping and progressive disclosure, and must adapt to size classes, screens, orientations, the Dynamic Island, external displays, resizable windows, text size and locale. Liquid Glass separates controls from content.

**Rules**
- **Order content by relative importance**: most important near the top and leading side; prefer standard components that adapt to RTL.
- **Align elements to make them easier to scan, and use indentation to convey hierarchy.**
- **Group related items** with negative space, container shapes or separator lines.
- **Use progressive disclosure** (disclosure triangles, menus, nested views, scrollable sections) to keep layouts clean.
- **Differentiate controls from content.** Use Liquid Glass for controls; instead of a solid or semi-opaque background beneath controls, use a scroll edge effect to elevate them. Extend full-screen background content underneath sidebars, toolbars and tab bars. If a scaled background image would be covered by sidebars/inspectors, use a background extension effect (flip-and-blur mirror beneath adjacent components).
- **Design a layout that adapts gracefully and consistently** across rotation, resizing, external displays and devices; respect safe areas, margins and layout guides. Even orientation-locked apps (landscape-only games) must resize well.
- **Be prepared for text-size changes**: stack horizontally adjacent views, let rows grow, allow multiple lines; Unity games use Apple's accessibility plug-in.
- **Preview on multiple devices, size classes, localizations and text sizes**; test the largest and smallest layouts first; use Device Hub (e.g., resized iPad windows, iPhone Mirroring on Mac).
- **Scale background artwork in response to display changes** when needed — never change its aspect ratio; scale to fill; expect very wide/short or tall/narrow windows.
- **Determine layout based on size classes, not device type or orientation**; idiom and orientation don't tell you how much space exists (iPhone Mirroring, iPad multitasking, iPad apps on Mac).
- **Consider all possible combinations of size classes** (compact/regular × horizontal/vertical) in portrait and landscape.
- **Keep functionality the same as size classes change**; vary how much is visible (tab bar → sidebar, surface overflow-menu items), and keep the layout recognizable for the platform's idiom.
- **Respect layout guides and safe areas** so hardware (Dynamic Island) and system UI (toolbar, tab bar, status bar) don't obstruct content.

**Platform notes**
- iOS/iPadOS: no additional considerations beyond size classes.
- macOS: **Avoid placing controls or critical information at the bottom of a window** (people drag windows partly offscreen). **Avoid displaying content behind the camera housing** at the top edge (NSPrefersDisplaySafeAreaCompatibilityMode).
- tvOS: **Adhere to the screen's safe area**: inset primary content 60 points from top and bottom and 80 points from the sides. **Include appropriate padding between focusable elements** (they grow on focus). Grids: **Include additional vertical spacing for titled rows**; **Use consistent spacing**; **Make partially hidden content look symmetrical** (equal offscreen width on each side). UICollectionViewFlowLayout derives column count automatically.
- visionOS: **In general, support resizing**; keep content horizontally centered at very large sizes; set min/max sizes to avoid overlap or unwieldy layouts, never to block resizing (Safari's navigation ornament has a fixed max). **Use 3D content sparingly in windows**, inset to avoid collisions; use a volume or immersive space for large models. **Display supplemental content in an adjacent window, not in an ornament** (defaultWindowPlacement(_:)); ornaments are for toolbars and playback controls. **Include enough space around controls** — button centers at least 60 points apart — so the hover effect doesn't obscure other content.
- watchOS: **Avoid more than two or three controls side by side**: no more than three glyph buttons or two text buttons in a row; full-width text buttons are usually better; two side-by-side short-label buttons work only if the screen doesn't scroll. **Support autorotation** for views people show to others (images, QR codes).

**Specs**

tvOS safe area: 60 pt top and bottom, 80 pt sides.

tvOS grid layouts (horizontal spacing 40 pt and minimum vertical spacing 100 pt in every case):

| Grid | Unfocused content width | Horizontal spacing | Minimum vertical spacing |
|---|---|---|---|
| Two-column | 860 pt | 40 pt | 100 pt |
| Three-column | 560 pt | 40 pt | 100 pt |
| Four-column | 410 pt | 40 pt | 100 pt |
| Five-column | 320 pt | 40 pt | 100 pt |
| Six-column | 260 pt | 40 pt | 100 pt |
| Seven-column | 217 pt | 40 pt | 100 pt |
| Eight-column | 184 pt | 40 pt | 100 pt |
| Nine-column | 160 pt | 40 pt | 100 pt |

visionOS: button centers ≥ 60 pt apart. watchOS: ≤ 3 glyph buttons or ≤ 2 text buttons per row. Size classes: compact or regular, per horizontal and vertical dimension. (The crawled page contains no device-dimension table despite change-log entries referencing device specs.)

**Dev refs**
backgroundExtensionEffect() (SwiftUI), UIBackgroundExtensionView (UIKit), UITraitChangeObservable, UserInterfaceSizeClass, UILayoutGuide, NSLayoutGuide, SafeAreaRegions, Positioning content relative to the safe area, NSPrefersDisplaySafeAreaCompatibilityMode, About focus interactions for Apple TV, UICollectionViewFlowLayout, Positioning and sizing windows (visionOS), defaultWindowPlacement(_:), WKExtension.isAutorotating, Device Hub, Composing custom layouts with SwiftUI, Apple – Accessibility Unity plug-in, Scroll views / Sidebars / Tab bars / Ornaments / Eyes / Buttons (HIG)

## Materials
Full page: hig/foundations/materials.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Two material families: Liquid Glass — a dynamic functional layer for controls and navigation (tab bars, sidebars, toolbars) floating above content — and standard materials (blur, vibrancy, blending) for structure within the content layer.

**Rules**
- **Don't use Liquid Glass in the content layer.** Use standard materials for content-layer elements such as app backgrounds. Exception: content-layer controls with a transient interactive element (sliders, toggles) take on Liquid Glass while a person activates them.
- **Use Liquid Glass effects sparingly.** System components adopt it automatically; apply it to custom controls only for the most important functional elements — overuse distracts from content.
- **Only use clear Liquid Glass for components over visually rich backgrounds.** Two variants: *regular* (blurs and adjusts luminosity of background; scroll edge effects add legibility; used by most system components; use when background may hurt legibility or the component has much text — alerts, sidebars, popovers) and *clear* (highly translucent; for components floating over media such as photos and video). Appearance can change with the user's preferred Liquid Glass look and with Reduce Transparency / Increase Contrast.
- **Decide whether to add a dimming layer behind clear Liquid Glass**: over bright content, consider a dark dimming layer at 35% opacity; over sufficiently dark content, or with AVKit standard playback controls (which dim on their own), none is needed.
- **Choose materials and effects based on semantic meaning and recommended usage**, not on the apparent color they impart (system settings can change it).
- **Help ensure legibility by using vibrant colors on top of materials**, whatever the material.
- **Consider contrast and visual separation when choosing a material**: thicker (more opaque) materials give better contrast for text and fine features; thinner (more translucent) materials preserve context.

**Platform notes**
- iOS/iPadOS: four standard materials for the content layer — ultraThin, thin, regular (default), thick. Vibrancy for labels: label (default), secondaryLabel, tertiaryLabel, quaternaryLabel (avoid quaternary on thin and ultraThin — contrast too low). Fills: fill (default), secondaryFill, tertiaryFill (all materials). Separator: one default vibrancy value, works on all materials. Default level = highest contrast; quaternary = lowest.
- macOS: standard materials with designated purposes plus vibrant versions of all system colors (NSVisualEffectView.Material). **Choose when to allow vibrancy in custom views and controls**; test in many contexts. **Choose a background blending mode** — behind window or within window (NSVisualEffectView.BlendingMode).
- tvOS: Liquid Glass appears in navigation elements and system experiences (Top Shelf, Control Center); image views and buttons adopt Liquid Glass on focus. Standard materials for the content layer (table below).
- visionOS: windows use the unmodifiable system *glass* material (adapts to surroundings; no Dark Mode setting — glass adapts to luminance behind it). **Prefer translucency to opaque colors in windows.** **If needed, choose materials for separation or interactivity**: thin = attention to interactive elements (buttons, selected items); regular = separate sections (sidebar, grouped table); thick = a dark element that stays distinct over a regular background. Vibrancy: label for standard text; secondaryLabel for footnotes and subtitles; tertiaryLabel for inactive elements only when high legibility isn't needed.
- watchOS: **Use materials to provide context in full-screen modal views**; don't remove or replace default material backgrounds of modal sheets.

**Specs**
Clear Liquid Glass dimming layer: dark, 35% opacity over bright content. iOS/iPadOS material thicknesses: ultraThin, thin, regular, thick.

| tvOS material | Recommended for |
|---|---|
| ultraThin | Full-screen views that require a light color scheme |
| thin | Overlay views that partially obscure onscreen content and require a light color scheme |
| regular | Overlay views that partially obscure onscreen content |
| thick | Overlay views that partially obscure onscreen content and require a dark color scheme |

**Dev refs**
Adopting Liquid Glass, Applying Liquid Glass to custom views, glassEffect(_:in:) (SwiftUI), Glass.regular / Glass.clear, Material (SwiftUI: ultraThin, thin, regular, thick), UIVisualEffectView, UIBlurEffect, UIVibrancyEffect, UIVibrancyEffectStyle (label, secondaryLabel, tertiaryLabel, quaternaryLabel, fill, secondaryFill, tertiaryFill, separator), NSVisualEffectView, NSVisualEffectView.Material, NSVisualEffectView.BlendingMode, Sliders / Toggles / Scroll views (HIG)

## Motion
Full page: hig/foundations/motion.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
System components include motion that adapts to accessibility settings and input method — Liquid Glass responds to direct touch with greater emphasis and more subtly to a trackpad. Guidelines below apply to custom motion.

**Rules**
- **Add motion purposefully, supporting the experience without overshadowing it.** No gratuitous or excessive animation (distraction, disconnection, physical discomfort).
- **Make motion optional.** Never make motion the only channel for important information; supplement with haptics and audio.
- **Strive for realistic feedback motion that follows people's gestures and expectations** (a view revealed by sliding down isn't dismissed by sliding sideways).
- **Aim for brevity and precision in feedback animations**; brief, precise feedback feels lightweight and communicates better.
- **In apps, generally avoid adding motion to UI interactions that occur frequently**; the system already animates standard elements.
- **Let people cancel motion.** Don't make people wait for an animation to finish, especially repeated ones.
- **Consider using animated symbols** (SF Symbols 5 or later) where it makes sense.
- **Make sure your game's motion looks great by default on each platform**: a consistent 30 to 60 fps is typically smooth; enable good defaults per device without requiring settings changes.
- **Let people customize the visual experience of your game** for performance or battery (e.g., power modes when external power is detected).

**Platform notes**
- iOS/iPadOS, macOS, tvOS: no additional considerations.
- visionOS: motion combines with depth for feedback and is a large part of the experience. **Avoid displaying motion at the edges of the field of view**; if peripheral motion is needed, match its brightness to the rest of the content. **Help people remain comfortable when moving large virtual objects** (that fill much of the view): increase translucency or lower contrast; keep windows fairly small. **Consider fades when relocating an object** (fade out, move, fade in). **In general, avoid letting people rotate a virtual world**; use instantaneous directional changes during a quick fade-out. **Consider giving people a stationary frame of reference**. **Avoid sustained oscillation**, especially around 0.2 Hz; keep amplitude low and content translucent.
- watchOS: prefer SwiftUI; WatchKit layout/appearance animations and animated image sequences via WKInterfaceImage. All layout- and appearance-based animations include built-in easing at start and end that cannot be turned off or customized.

**Specs**
Game frame rate: 30–60 fps consistent. visionOS: avoid oscillation around 0.2 Hz.

**Dev refs**
Animating views and transitions (SwiftUI), WKInterfaceImage (WatchKit), SF Symbols animations (HIG), Playing haptics / Playing audio / Feedback (HIG)

## Privacy
Full page: hig/foundations/privacy.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Be transparent about data and resources you require and protect what people grant. App Store privacy details (managed in App Store Connect) must describe your practices. Permission is required for personal data (location, health, financial, contacts), user content (mail, messages, calendar, photos, audio/video, HomeKit, Apple Music activity, gameplay), protected resources (Bluetooth, home automation, Wi-Fi, local network), camera and microphone, visionOS ARKit data in a Full Space, and the advertising identifier.

**Rules**
- **Request access only to data you actually need**, as specifically as possible, and not before the person shows interest in the feature.
- **Be transparent about how your app collects and uses data**; respect Hide My Email and Mail Privacy Protection; understand app-tracking obligations.
- **Process data on the device where possible** (Apple Neural Engine, CreateML).
- **Adopt system-defined privacy protections and security best practices** (e.g., CloudKit encryption for strings, numbers, dates in iOS 15+).
- **Request permission only when the app clearly needs access**; ideally when the person uses the feature (e.g., via the location button).
- **Avoid requesting permission at launch unless required to function** (navigation app location; visionOS game needing surroundings).
- **Write copy that clearly describes how your app uses the requested ability** (purpose string): one brief, complete, specific sentence, active voice, sentence case, ending with a period. Good: "The app records during the night to detect snoring sounds." Bad: "Microphone access is needed for a better experience." / "Turn on microphone access."
- **Pre-alert screens: include only one button and make it clear it opens the system alert**; title it "Continue" or "Next", never "Allow".
- **Don't include additional actions in a pre-alert screen** (no close or cancel) unless needed for legal consent.
- **Tracking: show the system-provided App Tracking Transparency alert before collecting any tracking data.**
- **Never precede the tracking alert with a custom screen that could confuse or mislead.** Prohibited (App Review rejection): offering incentives, withholding functionality until tracking is allowed, imitating the system request (including "Allow" buttons), showing a modified image of the alert, annotating the screen behind the alert. A legally required consent screen before or after the ATT alert is allowed (App Review Guidelines 5.1.1 (iv)).
- **Consider the location button** (iOS, iPadOS, watchOS) for lightweight one-time location sharing (attach location to a post, find a store, identify a plant); especially if people usually choose *Allow Once*. First tap shows a one-time explanatory alert; with no authorization status a tap equals *Allow Once*; with *While Using the App* it changes nothing.
- **Consider customizing the location button only within limits**: choose a system title ("Current Location", "Share My Current Location"), filled or outlined glyph, background/title/glyph colors, corner radius; nothing else. Text must fit without truncation at all accessibility sizes and in all languages. The system warns about low contrast or too much translucency, and withholds location access from a button with consistent problems.
- **Avoid relying solely on passwords**: prefer passkeys; otherwise require two-factor authentication; use Face ID, Optic ID or Touch ID for logged-in apps.
- **Store sensitive information in a keychain.**
- **Never store passwords or other secure content in plain-text files**, even with file permissions.
- **Avoid inventing custom authentication schemes**; use passkeys, Sign in with Apple or Password AutoFill.

**Platform notes**
- iOS/iPadOS, tvOS, watchOS: no additional considerations.
- macOS: **Sign your app with a valid Developer ID** for distribution outside the store. **Protect people's data with app sandboxing** (required for the Mac App Store). **Avoid making assumptions about who is signed in** (fast user switching).
- visionOS: ARKit runs always but sends no data to apps in the Shared Space; apps need a Full Space to access ARKit APIs, and Plane Estimation, Scene Reconstruction, Image Anchoring and Hand Tracking require permission. Eye input is private by design — hover effects give feedback without exposing gaze before a tap. Back camera provides blank input (compatibility only); front camera feeds spatial Personas only after permission; remove or replace camera features in iOS/iPadOS apps brought to visionOS (offer import instead).

**Specs**
Purpose string: one sentence, active voice, sentence case, period at end. Pre-alert screen: exactly one button ("Continue"/"Next"). Location button: customizable title (system-provided options), glyph style (filled/outlined), colors, corner radius only.

**Dev refs**
Requesting access to protected resources (UIKit), App Tracking Transparency, LocationButton (SwiftUI), CLLocationButton, Requesting authorization to use location services (CoreLocation), passkeys (AuthenticationServices), Securing Logins with iCloud Keychain Verification Codes, Local Authentication, Keychain services, Password AutoFill, Sign in with Apple (HIG), Managing accounts (HIG), Configuring the macOS App Sandbox, Setting up access to ARKit data, Making your existing app compatible with visionOS, Security framework, App privacy details on the App Store, User privacy and data use

## Right to left
Full page: hig/foundations/right-to-left.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
System UI frameworks flip automatically for Arabic, Hebrew and other RTL languages; these rules cover fine-tuning text alignment, numerals, controls, images and icons.

**Rules**
- **Adjust text alignment to match the interface direction** if the system doesn't (left-aligned LTR text becomes right-aligned in RTL).
- **Align a paragraph (three or more lines) based on its language, not on the current context**; one- and two-line blocks follow the context's reading direction.
- **Use a consistent alignment for all text items in a list**, including items in a different script.
- **Don't reverse the order of numerals in a specific number** (541, phone numbers, card numbers) regardless of language.
- **Reverse the order of numerals that show progress or counting direction; never flip the numerals themselves** (progress bars, sliders, rating controls, ordered sequences).
- **Use the appropriate numeral system per locale** if the app is number-centric (Hebrew uses Western Arabic numerals; Arabic may use Western or Eastern Arabic numerals, varying by region); otherwise rely on system number representations.
- **Flip controls that show progress from one value to another** (sliders, progress indicators) and reverse the positions of their beginning/end glyphs.
- **Flip controls that help people navigate or access items in a fixed order** (back button points right; next/previous flip).
- **Preserve the direction of a control that refers to an actual direction or points to an onscreen area** ("to the right" always points right).
- **Visually balance adjacent Latin and RTL scripts**: Arabic/Hebrew next to all-caps Latin often needs its font size increased by about 2 points.
- **Avoid flipping images like photographs, illustrations and general artwork** (changes meaning; copyright risk); create a new version if direction matters.
- **Reverse the positions of images when their order is meaningful** (chronological, alphabetical, favorites).
- **Flip interface icons that represent text or reading direction** (text-line bars align right in RTL).
- **Consider a localized version of an interface icon that displays text** (signature, rich text, I-beam exist for Latin, Hebrew, Arabic); for text that conveys an unrelated concept, design a text-free alternative.
- **Flip an interface icon that shows forward or backward motion** (speaker waves emanate from the right in RTL).
- **Don't flip logos or universal signs and marks** (checkmark); always show logos in original form even with text.
- **In general, avoid flipping icons that depict real-world objects** (clocks; right-handed tools) unless used for directionality.
- **Before flipping a complex custom icon, consider its components and visual balance**: a prohibition backslash stays the same in LTR and RTL; a badge representing real UI flips with the UI; a modifier badge flips only if meaning and balance survive; preserve a tool's handedness while flipping the base image if necessary.

**Platform notes**
- No additional considerations on any platform.

**Specs**
Paragraph = 3+ lines. RTL script beside uppercase Latin: +about 2 pt font size.

**Dev refs**
Creating custom symbols (directionality), Preparing views for localization (SwiftUI), Localization, SF Symbols (HIG)

## SF Symbols
Full page: hig/foundations/sf-symbols.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Thousands of symbols that align with San Francisco text in all weights and sizes, usable in toolbars, tab bars, context menus and inline text. Availability depends on OS version; symbols may not be used in app icons, logos or trademarked contexts.

**Rules**
- **Rendering modes**: Monochrome (one color, all layers), Hierarchical (one color, opacity per layer level), Palette (two or more colors, one per layer; two colors on a three-level symbol → secondary and tertiary share), Multicolor (intrinsic colors, e.g., green `leaf`, red `trash.slash`). Use system colors so symbols adapt to accessibility, vibrancy and Dark Mode.
- **Confirm that a symbol's rendering mode works well in every context**; the automatic setting gives the preferred mode but check legibility (size, background contrast).
- **Gradients (SF Symbols 7+)**: smooth linear gradient from a single source color; works in all rendering modes, system and custom colors, custom symbols; best at larger sizes.
- **Use variable color to communicate change — don't use it to communicate depth.** Variable color fills layers as a value crosses thresholds between 0 and 100 percent; layers can opt out (the speaker body in `speaker.wave.3`). Use Hierarchical mode for depth.
- **Weights and scales**: nine weights from ultralight to black match San Francisco weights; three scales — small, medium (default), large — defined relative to the SF cap height; scale changes emphasis without breaking weight matching at the same point size.
- **Design variants**: outline (most common; text-like), fill (solid areas, more emphasis — iOS tab bars, swipe actions, accent-color selection), slash (unavailable), enclosed (circle/square/rectangle; improves legibility at small sizes); many combine. Language/script variants (Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari, Indic numerals) switch automatically. The host view often decides outline vs. fill (tab bar prefers fill; toolbar takes outline).
- **Animations** (all symbols, modes, weights, scales, custom symbols; playback once/indefinite, speed, autoreverse): Appear, Disappear, Bounce (plays once; action occurred/needed), Scale (persists until changed), Pulse (opacity; annotated layers or all), Variable color (cumulative or iterative; autoreverse; hide inactive layers; open-loop vs closed-loop layer annotation for seamless repeats), Replace (down-up = state change; up-up = forward progression; off-up = emphasize next state), Magic Replace (default; smart transition between related shapes — slashes draw on/off, badges appear/disappear; falls back to down-up for unrelated symbols, fallback direction configurable), Wiggle (directional axis; highlight overlooked change or CTA), Breathe (opacity + size; ongoing activity such as recording), Rotate (whole symbol or By Layer, e.g., fan blades), Draw On / Draw Off (SF Symbols 7+; along guide points; all layers, staggered or one at a time; progress or directional meaning).
- **Apply symbol animations judiciously**; too many overwhelm and distract.
- **Make sure animations serve a clear purpose** in communicating the symbol's intent; consider how combinations may be misread.
- **Use symbol animations to communicate information more efficiently** (feedback, compact presentation of complex info).
- **Consider your app's tone when adding animations** (brand alignment).
- **Custom symbols: use the template as a guide** — consistent detail, optical weight, alignment, position, perspective; simple, recognizable, inclusive, directly related to the action/content. Annotate layers with colors or hierarchy levels.
- **Assign negative side margins if necessary** for optical horizontal alignment (badged symbols); follow the naming pattern (e.g., "left-margin-Regular-M").
- **Optimize layers for animation**: annotate layers in the SF Symbols app; Z-order sets variable-color order (front-to-back or back-to-front); animate by layer groups.
- **Test animations for custom symbols** with all presets; draw whole shapes plus an offset "erase" path rather than cutouts (e.g., `person.2.fill`).
- **Avoid custom symbols that include common variants** (enclosures, badges); use the SF Symbols component library instead.
- **Provide alternative text labels for custom symbols.**
- **Don't design replicas of Apple products**, and don't customize symbols the SF Symbols app marks (Info badge) as Apple product/feature symbols.

**Platform notes**
- No additional considerations on any platform.

**Specs**
Weights: 9 (ultralight, thin, light, regular, medium, semibold, bold, heavy, black — matching San Francisco). Scales: 3 (small, medium default, large). Rendering modes: 4. Variable color thresholds: 0–100 percent. Gradients, Draw On/Off: SF Symbols 7+. Animated symbols: SF Symbols 5+. (The crawled page contains no numeric weight/scale size table.)

**Dev refs**
Symbols framework, SymbolEffect, renderingMode(_:) (SwiftUI), imageScale(_:) (SwiftUI), UIImage.SymbolScale (UIKit), NSImage.SymbolConfiguration (AppKit), Configuring and displaying symbol images in your UI (UIKit), Creating custom symbols, SF Symbols app

## Spatial layout
Full page: hig/foundations/spatial-layout.md · Platforms: visionOS
Lay out for an infinite canvas using field of view, depth and scale. The system does not report a person's field of view; points are angular, so content keeps apparent size with distance (dynamic scale) unless fixed scale is chosen.

**Rules**
- **Center important content within the field of view**; in immersive experiences keep it centered and avoid distracting motion or bright high-contrast objects in the periphery.
- **Avoid anchoring content to the wearer's head**; anchor in the space so people can look around.
- **Provide visual cues that accurately communicate depth**; missing or conflicting cues cause discomfort.
- **Use depth to communicate hierarchy** (a sheet comes forward as the window recedes on the z-axis).
- **In general, avoid adding depth to text** — hovering text is hard to read.
- **Make sure depth adds value**: separate large important elements (tab bar, toolbar), not small ones (a button's symbol); limit how many distinct depths people must refocus on.
- **Consider fixed scale when a virtual object should look exactly like a physical object** (life-size product); use it sparingly and only for noninteractive objects — interactive content needs dynamic scale.
- **Avoid displaying too many windows** (obscure surroundings; hard to relocate).
- **Prioritize standard, indirect gestures**; reserve direct gestures for nearby objects inspected or manipulated briefly.
- **Rely on the Digital Crown to recenter windows**; no app work needed.
- **Include enough space around interactive components**: regular-size button centers at least 60 points apart, leaving 16 points or more between them; never let controls overlap other interactive elements or views.
- **Let people use your app with minimal or no physical movement.**
- **Use the floor to place a large immersive experience** that extends up from the floor (flat horizontal plane aligned with the floor).

**Platform notes**
- Not supported in iOS, iPadOS, macOS, tvOS or watchOS.

**Specs**
Interactive spacing: centers ≥ 60 pt apart, ≥ 16 pt gap between regular-size buttons. Point = angular unit in visionOS. Scale types: dynamic (default, keeps apparent size) and fixed.

**Dev refs**
Adding 3D content to your app, RealityKit, Presenting windows and spaces, Positioning and sizing windows, visionOS volumes / Windows / Gestures / Eyes / Digital Crown / Buttons (HIG)

## Typography
Full page: hig/foundations/typography.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Legible, hierarchical text using the system families San Francisco (SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew, SF Mono; rounded variants of all but Mono) and New York (serif), delivered as variable fonts with dynamic optical sizing, plus system text styles that scale with Dynamic Type (iOS, iPadOS, tvOS, visionOS, watchOS — not macOS).

**Rules**
- **Use font sizes that most people can read easily.** Follow per-platform default and minimum sizes for custom and system fonts (table below); thin custom weights need larger sizes.
- **Test legibility in different contexts** (each platform a game runs on); fix with larger size, more contrast or legibility-optimized typefaces.
- **In general, avoid light font weights.** Prefer Regular, Medium, Semibold or Bold; avoid Ultralight, Thin and Light, especially for small text.
- **Adjust font weight, size and color to emphasize important information** and keep relative hierarchy when text sizes change.
- **Minimize the number of typefaces**, even in a highly customized interface.
- **Prioritize important content when responding to text-size changes** (tab titles needn't grow; dialogue matters more than hit-damage values).
- **Consider using the built-in text styles**; they encode weight, size and leading per text size and give Dynamic Type and accessibility sizes for free.
- **Modify the built-in text styles if necessary** with symbolic traits: bold for another hierarchy level; loose leading for wide columns or long passages; tight leading in height-constrained areas such as list rows — but never tight leading for three or more lines.
- **Don't embed system fonts**; access them with Font.Design (default = system font; serif = New York).
- **If necessary, adjust tracking in interface mockups** (the running system adjusts tracking at every point size; tables below); discrete optical sizes aren't needed unless the design tool lacks variable-font support.
- **Make sure custom fonts are legible** at various distances and conditions, guided by the minimum sizes in Specs.
- **Implement accessibility features for custom fonts**: Dynamic Type (where available) and Bold Text; Unity games use Apple's Unity plug-ins or another way to adjust text size.
- **Make sure your layout adapts to all font sizes**; test with Larger Accessibility Text Sizes (Settings > Accessibility > Display & Text Size > Larger Text).
- **Increase the size of meaningful interface icons as font size increases**; SF Symbols scale automatically.
- **Keep text truncation to a minimum as font size increases**; show as much useful text at the largest accessibility size as at the largest standard size; avoid truncating in scrollable regions unless a separate view shows the rest; let labels use as many lines as needed.
- **Consider adjusting your layout at large font sizes**: stack text above secondary inline items; reduce the number of columns (isAccessibilityCategory).
- **Maintain a consistent information hierarchy regardless of font size** (primary elements stay toward the top).

**Platform notes**
- iOS/iPadOS: system font SF Pro; NY also available.
- macOS: system font SF Pro; NY only in Mac Catalyst apps; no Dynamic Type. **When necessary, use dynamic system font variants to match standard controls** (table below).
- tvOS: SF Pro; NY available.
- visionOS: SF Pro; NY requires specifying type styles. Uses bolder Dynamic Type body and title styles and adds Extra Large Title 1 and Extra Large Title 2 for wide editorial layouts. **In general, prefer 2D text** (depth hurts readability). **Make sure text looks good and remains legible when people scale it.** **Maximize contrast between text and its container's background** (default text is white over the system material). **If text has no background, consider bold to improve legibility** and avoid shadows (no predictable surface or Environment lighting). **Keep text facing people** — billboard labels anchored to 3D objects so the baseline stays perpendicular to the line of sight.
- watchOS: system font SF Compact; NY available; complications use SF Compact Rounded.

**Specs**

Default and minimum text sizes:

| Platform | Default size | Minimum size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

macOS dynamic system font variants:

| Dynamic font variant | API |
|---|---|
| Control content | controlContentFont(ofSize:) |
| Label | labelFont(ofSize:) |
| Menu | menuFont(ofSize:) |
| Menu bar | menuBarFont(ofSize:) |
| Message | messageFont(ofSize:) |
| Palette | paletteFont(ofSize:) |
| Title | titleBarFont(ofSize:) |
| Tool tips | toolTipsFont(ofSize:) |
| Document text (user) | userFont(ofSize:) |
| Monospaced document text (user fixed pitch) | userFixedPitchFont(ofSize:) |
| Bold system font | boldSystemFont(ofSize:) |
| System font | systemFont(ofSize:) |

Emphasized variants: SwiftUI `bold()` modifier or UIKit `traitBold` in UIFontDescriptor; emphasized weights are medium, semibold, bold or heavy as listed per style. The per-size source tables are merged below (one column per Dynamic Type size); every size/leading value is reproduced exactly. No visionOS size table exists on the crawled page (visionOS uses the iOS styles with bolder body/title plus Extra Large Title 1 and 2).

**iOS, iPadOS Dynamic Type sizes** — cells are Size / Leading in points; Weight and Emphasized weight are the same at every size.

| Style | Weight | Emphasized | xSmall | Small | Medium | Large (default) | xLarge | xxLarge | xxxLarge |
|---|---|---|---|---|---|---|---|---|---|
| Large Title | Regular | Bold | 31 / 38 | 32 / 39 | 33 / 40 | 34 / 41 | 36 / 43 | 38 / 46 | 40 / 48 |
| Title 1 | Regular | Bold | 25 / 31 | 26 / 32 | 27 / 33 | 28 / 34 | 30 / 37 | 32 / 39 | 34 / 41 |
| Title 2 | Regular | Bold | 19 / 24 | 20 / 25 | 21 / 26 | 22 / 28 | 24 / 30 | 26 / 32 | 28 / 34 |
| Title 3 | Regular | Semibold | 17 / 22 | 18 / 23 | 19 / 24 | 20 / 25 | 22 / 28 | 24 / 30 | 26 / 32 |
| Headline | Semibold | Semibold | 14 / 19 | 15 / 20 | 16 / 21 | 17 / 22 | 19 / 24 | 21 / 26 | 23 / 29 |
| Body | Regular | Semibold | 14 / 19 | 15 / 20 | 16 / 21 | 17 / 22 | 19 / 24 | 21 / 26 | 23 / 29 |
| Callout | Regular | Semibold | 13 / 18 | 14 / 19 | 15 / 20 | 16 / 21 | 18 / 23 | 20 / 25 | 22 / 28 |
| Subhead | Regular | Semibold | 12 / 16 | 13 / 18 | 14 / 19 | 15 / 20 | 17 / 22 | 19 / 24 | 21 / 28 |
| Footnote | Regular | Semibold | 12 / 16 | 12 / 16 | 12 / 16 | 13 / 18 | 15 / 20 | 17 / 22 | 19 / 24 |
| Caption 1 | Regular | Semibold | 11 / 13 | 11 / 13 | 11 / 13 | 12 / 16 | 14 / 19 | 16 / 21 | 18 / 23 |
| Caption 2 | Regular | Semibold | 11 / 13 | 11 / 13 | 11 / 13 | 11 / 13 | 13 / 18 | 15 / 20 | 17 / 22 |

_Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs._

**iOS, iPadOS larger accessibility type sizes** — cells are Size / Leading in points; Weight and Emphasized weight are the same at every size.

| Style | Weight | Emphasized | AX1 | AX2 | AX3 | AX4 | AX5 |
|---|---|---|---|---|---|---|---|
| Large Title | Regular | Bold | 44 / 52 | 48 / 57 | 52 / 61 | 56 / 66 | 60 / 70 |
| Title 1 | Regular | Bold | 38 / 46 | 43 / 51 | 48 / 57 | 53 / 62 | 58 / 68 |
| Title 2 | Regular | Bold | 34 / 41 | 39 / 47 | 44 / 52 | 50 / 59 | 56 / 66 |
| Title 3 | Regular | Semibold | 31 / 38 | 37 / 44 | 43 / 51 | 49 / 58 | 55 / 65 |
| Headline | Semibold | Semibold | 28 / 34 | 33 / 40 | 40 / 48 | 47 / 56 | 53 / 62 |
| Body | Regular | Semibold | 28 / 34 | 33 / 40 | 40 / 48 | 47 / 56 | 53 / 62 |
| Callout | Regular | Semibold | 26 / 32 | 32 / 39 | 38 / 46 | 44 / 52 | 51 / 60 |
| Subhead | Regular | Semibold | 25 / 31 | 30 / 37 | 36 / 43 | 42 / 50 | 49 / 58 |
| Footnote | Regular | Semibold | 23 / 29 | 27 / 33 | 33 / 40 | 38 / 46 | 44 / 52 |
| Caption 1 | Regular | Semibold | 22 / 28 | 26 / 32 | 32 / 39 | 37 / 44 | 43 / 51 |
| Caption 2 | Regular | Semibold | 20 / 25 | 24 / 30 | 29 / 35 | 34 / 41 | 40 / 48 |

**macOS built-in text styles (no Dynamic Type)**

| Text style | Weight | Size (points) | Line height (points) | Emphasized weight |
|---|---|---|---|---|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

_Point size based on image resolution of 144 ppi for @2x designs._

**tvOS built-in text styles**

| Text style | Weight | Size (points) | Leading (points) | Emphasized weight |
|---|---|---|---|---|
| Title 1 | Medium | 76 | 96 | Bold |
| Title 2 | Medium | 57 | 66 | Bold |
| Title 3 | Medium | 48 | 56 | Bold |
| Headline | Medium | 38 | 46 | Bold |
| Subtitle 1 | Regular | 38 | 46 | Medium |
| Callout | Medium | 31 | 38 | Bold |
| Body | Medium | 29 | 36 | Bold |
| Caption 1 | Medium | 25 | 32 | Bold |
| Caption 2 | Medium | 23 | 30 | Bold |

_Point size based on image resolution of 72 ppi for @1x and 144 ppi for @2x designs._

**watchOS Dynamic Type sizes** — cells are Size / Leading in points; Weight and Emphasized weight are the same at every size.

| Style | Weight | Emphasized | xSmall | Small (default 38mm) | Large (default 40mm/41mm/42mm) | xLarge (default 44mm/45mm/49mm) | xxLarge | xxxLarge |
|---|---|---|---|---|---|---|---|---|
| Large Title | Regular | Bold | 30 / 32.5 | 32 / 34.5 | 36 / 38.5 | 40 / 42.5 | 41 / 43.5 | 42 / 44.5 |
| Title 1 | Regular | Semibold | 28 / 30.5 | 30 / 32.5 | 34 / 36.5 | 38 / 40.5 | 39 / 41.5 | 40 / 42.5 |
| Title 2 | Regular | Semibold | 24 / 26.5 | 26 / 28.5 | 28 / 30.5 | 30 / 32.5 | 31 / 33.5 | 32 / 34.5 |
| Title 3 | Regular | Semibold | 17 / 19.5 | 18 / 20.5 | 19 / 21.5 | 20 / 22.5 | 21 / 23.5 | 22 / 24.5 |
| Headline | Semibold | Semibold | 14 / 16.5 | 15 / 17.5 | 16 / 18.5 | 17 / 19.5 | 18 / 20.5 | 19 / 21.5 |
| Body | Regular | Semibold | 14 / 16.5 | 15 / 17.5 | 16 / 18.5 | 17 / 19.5 | 18 / 20.5 | 19 / 21.5 |
| Caption 1 | Regular | Semibold | 13 / 15.5 | 14 / 16.5 | 15 / 17.5 | 16 / 18.5 | 17 / 19.5 | 18 / 20.5 |
| Caption 2 | Regular | Semibold | 12 / 14.5 | 13 / 15.5 | 14 / 16.5 | 15 / 17.5 | 16 / 18.5 | 17 / 19.5 |
| Footnote 1 | Regular | Semibold | 11 / 13.5 | 12 / 14.5 | 13 / 15.5 | 14 / 16.5 | 15 / 17.5 | 16 / 18.5 |
| Footnote 2 | Regular | Semibold | 10 / 12.5 | 11 / 13.5 | 12 / 14.5 | 13 / 15.5 | 14 / 16.5 | 15 / 17.5 |

**watchOS larger accessibility type sizes** — cells are Size / Leading in points; Weight and Emphasized weight are the same at every size.

| Style | Weight | Emphasized | AX1 | AX2 | AX3 |
|---|---|---|---|---|---|
| Large Title | Regular | Bold | 44 / 46.5 | 45 / 47.5 | 46 / 48.5 |
| Title 1 | Regular | Semibold | 42 / 44.5 | 43 / 46 | 44 / 47 |
| Title 2 | Regular | Semibold | 34 / 41 | 35 / 37.5 | 36 / 38.5 |
| Title 3 | Regular | Semibold | 24 / 26.5 | 25 / 27.5 | 26 / 28.5 |
| Headline | Semibold | Semibold | 21 / 23.5 | 22 / 24.5 | 23 / 25.5 |
| Body | Regular | Semibold | 21 / 23.5 | 22 / 24.5 | 23 / 25.5 |
| Caption 1 | Regular | Semibold | 18 / 20.5 | 19 / 21.5 | 20 / 22.5 |
| Caption 2 | Regular | Semibold | 17 / 19.5 | 18 / 20.5 | 19 / 21.5 |
| Footnote 1 | Regular | Semibold | 16 / 18.5 | 17 / 19.5 | 18 / 20.5 |
| Footnote 2 | Regular | Semibold | 15 / 17.5 | 16 / 17.5 | 17 / 19.5 |

**Tracking values — SF Pro (iOS, iPadOS, visionOS), SF Pro Rounded (iOS, iPadOS, visionOS), and the macOS / tvOS system font.** Columns are Tracking (1/1000 em) · Tracking (points). The macOS and tvOS tables are identical to each other and differ from the SF Pro table only at 52, 53 pt.

| Size (pt) | SF Pro (em) | SF Pro (pt) | SF Pro Rounded (em) | SF Pro Rounded (pt) | macOS, tvOS (em) | macOS, tvOS (pt) |
|---|---|---|---|---|---|---|
| 6 | +41 | +0.24 | +87 | +0.51 | +41 | +0.24 |
| 7 | +34 | +0.23 | +80 | +0.54 | +34 | +0.23 |
| 8 | +26 | +0.21 | +72 | +0.57 | +26 | +0.21 |
| 9 | +19 | +0.17 | +65 | +0.57 | +19 | +0.17 |
| 10 | +12 | +0.12 | +58 | +0.57 | +12 | +0.12 |
| 11 | +6 | +0.06 | +52 | +0.56 | +6 | +0.06 |
| 12 | 0 | 0.0 | +46 | +0.54 | 0 | 0.0 |
| 13 | -6 | -0.08 | +40 | +0.51 | -6 | -0.08 |
| 14 | -11 | -0.15 | +35 | +0.48 | -11 | -0.15 |
| 15 | -16 | -0.23 | +30 | +0.44 | -16 | -0.23 |
| 16 | -20 | -0.31 | +26 | +0.41 | -20 | -0.31 |
| 17 | -26 | -0.43 | +22 | +0.37 | -26 | -0.43 |
| 18 | -25 | -0.44 | +21 | +0.37 | -25 | -0.44 |
| 19 | -24 | -0.45 | +20 | +0.37 | -24 | -0.45 |
| 20 | -23 | -0.45 | +18 | +0.36 | -23 | -0.45 |
| 21 | -18 | -0.36 | +17 | +0.35 | -18 | -0.36 |
| 22 | -12 | -0.26 | +16 | +0.34 | -12 | -0.26 |
| 23 | -4 | -0.10 | +16 | +0.35 | -4 | -0.10 |
| 24 | +3 | +0.07 | +15 | +0.35 | +3 | +0.07 |
| 25 | +6 | +0.15 | +14 | +0.35 | +6 | +0.15 |
| 26 | +8 | +0.22 | +14 | +0.36 | +8 | +0.22 |
| 27 | +11 | +0.29 | +14 | +0.36 | +11 | +0.29 |
| 28 | +14 | +0.38 | +13 | +0.36 | +14 | +0.38 |
| 29 | +14 | +0.40 | +13 | +0.37 | +14 | +0.40 |
| 30 | +14 | +0.40 | +12 | +0.37 | +14 | +0.40 |
| 31 | +13 | +0.39 | +12 | +0.36 | +13 | +0.39 |
| 32 | +13 | +0.41 | +12 | +0.38 | +13 | +0.41 |
| 33 | +12 | +0.40 | +12 | +0.39 | +12 | +0.40 |
| 34 | +12 | +0.40 | +12 | +0.38 | +12 | +0.40 |
| 35 | +11 | +0.38 | +11 | +0.38 | +11 | +0.38 |
| 36 | +10 | +0.37 | +11 | +0.39 | +10 | +0.37 |
| 37 | +10 | +0.36 | +10 | +0.38 | +10 | +0.36 |
| 38 | +10 | +0.37 | +10 | +0.39 | +10 | +0.37 |
| 39 | +10 | +0.38 | +10 | +0.38 | +10 | +0.38 |
| 40 | +10 | +0.37 | +10 | +0.39 | +10 | +0.37 |
| 41 | +9 | +0.36 | +10 | +0.38 | +9 | +0.36 |
| 42 | +9 | +0.37 | +10 | +0.39 | +9 | +0.37 |
| 43 | +9 | +0.38 | +9 | +0.38 | +9 | +0.38 |
| 44 | +8 | +0.37 | +8 | +0.37 | +8 | +0.37 |
| 45 | +8 | +0.35 | +8 | +0.37 | +8 | +0.35 |
| 46 | +8 | +0.36 | +8 | +0.36 | +8 | +0.36 |
| 47 | +8 | +0.37 | +8 | +0.37 | +8 | +0.37 |
| 48 | +8 | +0.35 | +8 | +0.35 | +8 | +0.35 |
| 49 | +7 | +0.33 | +8 | +0.36 | +7 | +0.33 |
| 50 | +7 | +0.34 | +7 | +0.34 | +7 | +0.34 |
| 51 | +7 | +0.35 | +6 | +0.32 | +7 | +0.35 |
| 52 | +6 | +0.33 | +6 | +0.33 | +6 | +0.31 |
| 53 | +6 | +0.31 | +6 | +0.31 | +6 | +0.33 |
| 54 | +6 | +0.32 | +6 | +0.32 | +6 | +0.32 |
| 56 | +6 | +0.30 | +6 | +0.30 | +6 | +0.30 |
| 58 | +5 | +0.28 | +4 | +0.25 | +5 | +0.28 |
| 60 | +4 | +0.26 | +4 | +0.23 | +4 | +0.26 |
| 62 | +4 | +0.24 | +4 | +0.21 | +4 | +0.24 |
| 64 | +4 | +0.22 | +3 | +0.19 | +4 | +0.22 |
| 66 | +3 | +0.19 | +2 | +0.16 | +3 | +0.19 |
| 68 | +2 | +0.17 | +2 | +0.13 | +2 | +0.17 |
| 70 | +2 | +0.14 | +2 | +0.14 | +2 | +0.14 |
| 72 | +2 | +0.14 | +2 | +0.11 | +2 | +0.14 |
| 76 | +1 | +0.07 | +1 | +0.07 | +1 | +0.07 |
| 80 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 84 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 88 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 92 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 96 | 0 | 0 | 0 | 0.00 | 0 | 0 |

_Not all apps express tracking values as 1/1000 em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs._

**Tracking values — New York (iOS, iPadOS, visionOS)**

| Size (points) | Tracking (1/1000 em) | Tracking (points) |
|---|---|---|
| 6 | +40 | +0.23 |
| 7 | +32 | +0.22 |
| 8 | +25 | +0.20 |
| 9 | +20 | +0.18 |
| 10 | +16 | +0.15 |
| 11 | +11 | +.12 |
| 12 | +6 | +0.07 |
| 13 | +4 | +0.05 |
| 14 | +2 | +0.03 |
| 15 | +0 | +0.00 |
| 16 | -2 | -0.03 |
| 17 | -4 | -0.07 |
| 18 | -6 | -0.11 |
| 19 | -8 | -0.15 |
| 20 | -10 | -0.20 |
| 21 | -10 | -0.21 |
| 22 | -10 | -0.23 |
| 23 | -11 | -0.25 |
| 24 | -11 | -0.26 |
| 25 | -11 | -0.27 |
| 26 | -12 | -0.29 |
| 27 | -12 | -0.32 |
| 28 | -12 | -0.33 |
| 29 | -12 | -0.34 |
| 30 | -12 | -0.37 |
| 31 | -13 | -0.39 |
| 32 | -13 | -0.41 |
| 33 | -13 | -0.42 |
| 34 | -14 | -0.45 |
| 35 | -14 | -0.48 |
| 36 | -14 | -0.49 |
| 38 | -14 | -0.52 |
| 40 | -14 | -0.55 |
| 42 | -14 | -0.57 |
| 44 | -14 | -0.62 |
| 46 | -14 | -0.65 |
| 48 | -14 | -0.68 |
| 50 | -14 | -0.71 |
| 52 | -14 | -0.74 |
| 54 | -15 | -0.79 |
| 58 | -15 | -0.85 |
| 62 | -15 | -0.91 |
| 66 | -15 | -0.97 |
| 70 | -16 | -1.06 |
| 72 | -16 | -1.09 |
| 80 | -16 | -1.21 |
| 88 | -16 | -1.33 |
| 96 | -16 | -1.50 |
| 100 | -16 | -1.56 |
| 120 | -16 | -1.88 |
| 140 | -16 | -2.26 |
| 160 | -16 | -2.58 |
| 180 | -17 | -2.99 |
| 200 | -17 | -3.32 |
| 220 | -18 | -3.76 |
| 240 | -18 | -4.22 |
| 260 | -18 | -4.57 |

_Not all apps express tracking values as 1/1000 em. Point size based on image resolution of 144 ppi for @2x and 216 ppi for @3x designs._

**Tracking values — watchOS: SF Compact and SF Compact Rounded.**

| Size (pt) | SF Compact (em) | SF Compact (pt) | SF Compact Rounded (em) | SF Compact Rounded (pt) |
|---|---|---|---|---|
| 6 | +50 | +0.29 | +28 | +0.16 |
| 7 | +30 | +0.21 | +26 | +0.18 |
| 8 | +30 | +0.23 | +24 | +0.19 |
| 9 | +30 | +0.26 | +22 | +0.19 |
| 10 | +30 | +0.29 | +20 | +0.20 |
| 11 | +24 | +0.26 | +18 | +0.19 |
| 12 | +20 | +0.23 | +16 | +0.19 |
| 13 | +16 | +0.20 | +14 | +0.18 |
| 14 | +14 | +0.19 | +12 | +0.16 |
| 15 | +4 | +0.06 | +10 | +0.15 |
| 16 | 0 | 0.00 | +8 | +0.12 |
| 17 | -4 | -0.07 | +6 | +0.10 |
| 18 | -8 | -0.14 | +4 | +0.07 |
| 19 | -12 | -0.22 | +2 | +0.04 |
| 20 | 0 | 0.00 | 0 | 0.00 |
| 21 | -2 | -0.04 | -2 | -0.04 |
| 22 | -4 | -0.09 | -4 | -0.09 |
| 23 | -6 | -0.13 | -6 | -0.13 |
| 24 | -8 | -0.19 | -8 | -0.19 |
| 25 | -10 | -0.24 | -10 | -0.24 |
| 26 | -11 | -0.28 | -11 | -0.28 |
| 27 | -12 | -0.30 | -12 | -0.30 |
| 28 | -12 | -0.34 | -12 | -0.34 |
| 29 | -14 | -0.38 | -14 | -0.38 |
| 30 | -14 | -0.42 | -14 | -0.42 |
| 31 | -15 | -0.45 | -15 | -0.45 |
| 32 | -16 | -0.50 | -16 | -0.50 |
| 33 | -17 | -0.55 | -17 | -0.55 |
| 34 | -18 | -0.60 | -18 | -0.60 |
| 35 | -18 | -0.63 | -18 | -0.63 |
| 36 | -20 | -0.69 | -20 | -0.69 |
| 37 | -20 | -0.72 | -20 | -0.72 |
| 38 | -20 | -0.74 | -20 | -0.74 |
| 39 | -20 | -0.76 | -20 | -0.76 |
| 40 | -20 | -0.78 | -20 | -0.78 |
| 41 | -20 | -0.80 | -20 | -0.80 |
| 42 | -20 | -0.82 | -20 | -0.82 |
| 43 | -20 | -0.84 | -20 | -0.84 |
| 44 | -20 | -0.86 | -20 | -0.86 |
| 45 | -20 | -0.88 | -20 | -0.88 |
| 46 | -20 | -0.92 | -20 | -0.92 |
| 47 | -20 | -0.94 | -20 | -0.94 |
| 48 | -20 | -0.96 | -20 | -0.96 |
| 49 | -21 | -1.00 | -21 | -1.00 |
| 50 | -21 | -1.03 | -21 | -1.03 |
| 51 | -21 | -1.05 | -21 | -1.05 |
| 52 | -21 | -1.07 | -21 | -1.07 |
| 53 | -22 | -1.11 | -22 | -1.11 |
| 54 | -22 | -1.13 | -22 | -1.13 |
| 56 | -22 | -1.20 | -22 | -1.20 |
| 58 | -22 | -1.25 | -22 | -1.25 |
| 60 | -22 | -1.32 | -22 | -1.32 |
| 62 | -22 | -1.36 | -22 | -1.36 |
| 64 | -23 | -1.44 | -23 | -1.44 |
| 66 | -24 | -1.51 | -24 | -1.51 |
| 68 | -24 | -1.56 | -24 | -1.56 |
| 70 | -24 | -1.64 | -24 | -1.64 |
| 72 | -24 | -1.69 | -24 | -1.69 |
| 76 | -25 | -1.86 | -25 | -1.86 |
| 80 | -26 | -1.99 | -26 | -1.99 |
| 84 | -26 | -2.13 | -26 | -2.13 |
| 88 | -26 | -2.28 | -26 | -2.28 |
| 92 | -28 | -2.47 | -28 | -2.47 |
| 96 | -28 | -2.62 | -28 | -2.62 |

_Not all apps express tracking values as 1/1000 em. Point size based on image resolution of 144 ppi for @2x designs._

**Dev refs**
Font.Design (default, serif), leading(_:) (SwiftUI), bold() (SwiftUI), UIFontDescriptor.SymbolicTraits.traitBold, UILabel.numberOfLines, UIContentSizeCategory.isAccessibilityCategory, Applying custom fonts to text (SwiftUI), Text input and output (SwiftUI), Text display and fonts (UIKit), Fonts (AppKit), NSFont dynamic variants (table above), Apple's Unity plug-ins, Fonts for Apple platforms (download), Dynamic Type size tables (Apple Design Resources)

## Writing
Full page: hig/foundations/writing.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
The words in onboarding, alerts, labels, errors and accessibility descriptions are part of the experience: establish a voice, vary tone by context, be clear, and write for everyone.

**Rules**
- **Determine your app's voice**: who you're talking to, how they should feel; keep a list of common terms for consistency.
- **Match your tone to the context** (serious and direct for a safety alert; light and congratulatory for a reached goal).
- **Be clear.** Fewer words; check each word is needed; read it out loud.
- **Write for everyone**: plain language, accessibility and localization in mind, no jargon or gendered terminology.
- **Consider each screen's purpose**: most important information first; split multiple ideas across screens.
- **Be action oriented**: active voice; verbs on buttons and links ("Send", not "Let's do it!"); descriptive link text, never "Click here" (important for screen readers).
- **Build language patterns** for consistency and faster writing.
- **Adopt capitalization rules and apply them consistently** per UI element type (title case = formal; sentence case = casual); button labels have their own guidance.
- **Give clear guidance and consistent language in multistep flows**: start with "Get Started", move with "Continue" or "Next" (pick one), finish with "Done".
- **Use possessive pronouns sparingly** ("Favorites" over "Your Favorites"); be consistent in perspective; avoid *we* entirely ("Unable to load content", not "We're having trouble loading this content").
- **Write for how people use each device**: say "tap" on touch devices, not "click"; iPhone and Apple Watch need brevity; TV text is seen by several people and must be large, so keep it brief.
- **Provide clear next steps on any blank screen**: empty states welcome and educate; give a button or link; don't put crucial information only there (they disappear).
- **Write clear error messages**: show near the problem, avoid blame, say how to fix it ("Choose a password with at least 8 characters" rather than "That password is too short"); skip "oops!"/"uh-oh"; if language can't fix a common error, rethink the interaction.
- **Choose the right delivery method** by urgency, importance, context and needed detail (notifications, alerts, action sheets) with a matching tone.
- **Keep settings labels clear and simple**; describe what happens when on (the off state is implied); link directly to a setting instead of describing its location.
- **Show hints in text fields**: label every field; placeholder examples ("name@example.com", "Your name"); errors right next to the field with instructions ("Use only letters for your name", not "Don't use numbers or symbols" or "Invalid name").

**Platform notes**
- No additional considerations on any platform.

**Dev refs**
Apple Style Guide, Writing inclusively, Localization (Xcode), VoiceOver / Notifications / Alerts / Action sheets / Settings / Text fields / Buttons (HIG)
