# Components (presentation · selection & input · status · system experiences) — HIG digest

These four component groups cover how an app presents transient and modal content (action sheets, alerts, page controls, panels, popovers, scroll views, sheets, windows), how people enter and select values (color wells, combo boxes, digit entry views, image wells, pickers, segmented controls, sliders, steppers, text fields, toggles, virtual keyboards), how an app reports state (activity rings, gauges, progress indicators, rating indicators), and how it extends into system surfaces outside its own UI (App Shortcuts, complications, controls, Live Activities, notifications, snippets, status bars, Top Shelf, watch faces, widgets). The full crawled pages live in `hig/components/<slug>.md`; this digest keeps every rule and every number from those pages but drops Apple's examples, screenshots, videos and connective prose. Platform lists come from each page's header. Where a page carries Liquid Glass-era guidance (scroll edge effects, keyboard accessory views, visionOS glass windows, clear/accented widgets) it is kept explicitly; pages without such wording in the 2026-10-14 crawl get none invented.

## Presentation

### Action sheets
Full page: hig/components/action-sheets.md · Platforms: iOS, iPadOS, macOS, tvOS, watchOS
A modal view presenting choices related to an action people just initiated (e.g. cancel a draft → delete or save). Not for unexpected problems (use an alert) and not for options people choose to reveal (use a menu). Not supported in visionOS.

**Rules**
- **Use an action sheet — not an alert — to offer choices related to an intentional action.** Alerts are usually unexpected and don't offer additional choices.
- **Use action sheets sparingly.** They interrupt the current task.
- **Keep titles short enough to display on a single line.** Long titles truncate or force scrolling.
- **Provide a message only if necessary.** Title plus the action's context is normally enough.
- **If necessary, provide a Cancel button** so people can reject an action that might destroy data. Place it at the bottom (watchOS: upper-left corner). A SwiftUI confirmation dialog includes Cancel by default.
- **Make destructive choices visually prominent.** Use the destructive button style and place destructive buttons at the top of the sheet.

**Platform notes**
- iOS/iPadOS: Use an action sheet — not a menu — for choices related to an action (people expect a menu only when they reveal it). Avoid letting an action sheet scroll (more buttons = slower choice; scrolling risks accidental taps). · macOS/tvOS: no additional considerations. · visionOS: not supported. · watchOS: system style = title, optional message, Cancel button, one or more additional buttons; appearance varies by device. Avoid more than four buttons including Cancel → no more than three additional choices.

**Specs**

watchOS button styles:

| Style | Meaning |
|---|---|
| Default | The button has no special meaning. |
| Destructive | The button destroys user data or performs a destructive action in the app. |
| Cancel | The button dismisses the view without taking any action. |

**Dev refs**
confirmationDialog(_:isPresented:titleVisibility:actions:) (SwiftUI), ButtonRole.destructive (SwiftUI), UIAlertController.Style.actionSheet (UIKit), UIAlertAction.Style.destructive (UIKit)

### Alerts
Full page: hig/components/alerts.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
A modal view giving critical information people need right away: a problem, a warning that an action might destroy data, or confirmation of a purchase or other important action they initiated. Not for purely informational messages and not for offering choices about an intentional action (use an action sheet).

**Rules**
- **Use alerts sparingly.** Each one must offer only essential information and useful actions.
- **Avoid using an alert merely to provide information.** Non-actionable information belongs in context (e.g. Mail's server-unavailable indicator people can tap to learn more).
- **Avoid alerts for common, undoable actions, even when destructive** (deleting an email or file). Do alert for uncommon destructive actions that can't be undone.
- **Avoid showing an alert when your app starts.** Make new information discoverable; for startup problems like no network, show cached/placeholder data plus a nonintrusive label.
- **Content:** every alert has a title, optional informative text, and up to three buttons. iOS/iPadOS/macOS/visionOS alerts can include a text field; macOS/visionOS alerts an icon and an accessory view; macOS alerts a suppression checkbox and a Help button.
- **Be direct, neutral, approachable in all alert copy.** Don't be oblique or accusatory, and don't mask severity.
- **Write a title that clearly and succinctly describes the situation** — what happened, in what context, and why. Avoid "Error" or "Error 329347 occurred"; avoid titles that wrap to more than two lines. Complete sentence → sentence-style capitalization and ending punctuation; fragment → title-style capitalization, no ending punctuation.
- **Include informative text only if it adds value.** Keep it short; complete sentences, sentence-style capitalization, proper punctuation.
- **Avoid explaining alert buttons.** If you must, use "choose" (device-agnostic) and refer to the button by its exact title without quotes.
- **Include a text field only if you need people's input to resolve the situation** (e.g. a secure password field).
- **Create succinct, logical button titles:** one or two words describing the result; verbs/verb phrases tied to the alert text ("View All," "Reply," "Ignore"). "OK" only in informational alerts; never "Yes"/"No"; always "Cancel" for the cancel button; title-style capitalization, no ending punctuation.
- **Avoid "OK" as the default button title unless the alert is purely informational.** Prefer specific titles like "Erase," "Convert," "Clear," "Delete."
- **Place buttons where people expect:** the most likely choice on the trailing side of a row or at the top of a stack; the default button always trailing/top; Cancel typically leading/bottom.
- **Use the destructive style only for a destructive action people didn't deliberately choose.** A confirmation of a deliberately chosen destructive action (Empty Trash) doesn't style that button destructive, so Return can confirm it.
- **If there's a destructive action, include a Cancel button.** Never make Cancel the default. To force people to read, make no button the default. A single-button default alert uses Done, not Cancel.
- **Provide alternative ways to cancel** (see Specs).

**Platform notes**
- iOS/iPadOS: Use an action sheet — not an alert — to offer choices related to an intentional action. Avoid alerts that scroll: short titles, brief message only when necessary. · macOS: the app icon is shown automatically (alternative icon/symbol allowed); can configure repeating alerts with a suppression checkbox, append an accessory view, include a Help button. Use a caution symbol (`exclamationmark.triangle`) sparingly — only when extra attention is really needed (unexpected data loss), never for save or empty-trash tasks. · tvOS/watchOS: no additional considerations. · visionOS: in the Shared Space the alert appears in front of the app window, slightly forward on the z-axis, and stays anchored if the window moves; in a Full Space it's centered in the field of view. An accessory view has a maximum height of 154 pt and a 16-pt corner radius.

**Specs**

Alternative ways to cancel an alert:

| Action | Platform |
|---|---|
| Exit to the Home Screen | iOS, iPadOS |
| Pressing Escape (Esc) or Command-Period (.) on an attached keyboard | iOS, iPadOS, macOS, visionOS |
| Pressing Menu on the remote | tvOS |

visionOS accessory view: max height 154 pt, corner radius 16 pt.

**Dev refs**
alert(_:isPresented:actions:) (SwiftUI), UIAlertController (UIKit), NSAlert, NSAlert.accessoryView (AppKit)

### Page controls
Full page: hig/components/page-controls.md · Platforms: iOS, iPadOS, tvOS, visionOS, watchOS
A row of indicator dots, one per page in a flat ordered list; the solid dot is the current page; dots are equidistant and clip when too many fit. Not supported in macOS. Not for hierarchical or nonsequential relationships.

**Rules**
- **Use page controls to represent movement between an ordered list of pages.** For hierarchical/nonsequential navigation use a sidebar or split view.
- **Center a page control horizontally at the bottom of the view or window.**
- **Don't display too many pages.** More than about 10 dots are hard to count; for more than 10 peer pages consider a grid.
- **Make custom indicator images simple and clear.** No complex shapes, negative space, text, or inner lines; consider simple SF Symbols.
- **Customize the default indicator image only when it enhances the control's overall meaning** (e.g. `bookmark.fill` when every page holds bookmarks).
- **Avoid using more than two different indicator images in a page control.** One unique image for a special page (Weather's `location.fill`) is fine; several is hard to learn and looks messy.
- **Avoid coloring indicator images.** Let the system color them to keep current-page contrast.

**Platform notes**
- iOS/iPadOS: the control highlights the current indicator and shrinks indicators at both sides when more pages exist than fit. Tapping leading/trailing of the current dot = next/previous page (discrete); scrubbing (touch and drag) opens pages in sequence and past the edges jumps to first/last (continuous); iPadOS pointer can target a specific dot. Avoid animating page transitions during scrubbing — use the animated scrolling transition only for taps. Background styles: Automatic (background only during interaction; use when the control isn't the primary navigation), Prominent (always shown; only when it is the primary navigation control), Minimal (never shown; position only, no scrub feedback). Avoid supporting the scrubber with the minimal style. · tvOS: use page controls on collections of full-screen peer pages; extra controls make focus hard to maintain. · visionOS: page controls show pages and the current page but people don't interact with them. · watchOS: shown at the bottom for horizontal pagination or next to the Digital Crown for a vertical tab view, where the indicator shows position within the page and within the set. Use vertical pagination to separate views into distinct, purposeful pages (better than horizontal pagination or deep hierarchy). Consider limiting each page to a single screen height; use variable-height pages judiciously and place them after fixed-height pages.

**Dev refs**
PageTabViewStyle (SwiftUI), UIPageControl, UIPageControl.preferredIndicatorImage, setIndicatorImage(_:forPage:), UIPageControl.InteractionState, UIPageControl.backgroundStyle (UIKit)

### Panels
Full page: hig/components/panels.md · Platforms: macOS
A window that floats above other windows with supplementary controls, options or information for the active window or selection; less prominent than a main window, with an optional dark translucent HUD style. On other platforms use a modal view instead.

**Rules**
- **Use a panel for quick access to important controls or information related to the content people are working with** (settings affecting the selected item).
- **Consider a panel for inspector functionality** (updates as the selection changes). An Info window whose contents never change belongs in a regular window, not a panel; a split-view pane is another inspector option.
- **Prefer simple adjustment controls** (sliders, steppers); avoid controls that require typing or multi-step selection.
- **Write a brief title describing the panel's purpose:** a noun or noun phrase in title-style capitalization ("Fonts," "Colors," "Inspector"). Panels need a title bar so people can position them.
- **Show and hide panels appropriately:** bring all open panels to the front when the app becomes active; hide them all when it's inactive.
- **Avoid including panels in the Window menu's documents list.** Show/hide commands in the Window menu are fine.
- **In general, avoid making a panel's minimize button available.**
- **Refer to panels by title:** menus say "Show Fonts," "Show Colors," "Show Inspector" (no "panel"); in help, use the title or append "window" ("Fonts window") for clarity.
- **Prefer standard panels over HUDs.** Use a HUD only in a media-oriented app (movies, photos, slides), when a standard panel would obscure essential content, or when no controls are needed (most system controls don't match a HUD, the disclosure triangle excepted).
- **Maintain one panel style when your app switches modes** (keep the HUD when leaving full screen if you used it there).
- **Use color sparingly in HUDs** — small amounts of high-contrast color only.
- **Keep HUDs small.** Don't obscure the content a HUD adjusts or compete with it for attention.

**Dev refs**
NSPanel, NSWindow.StyleMask.hudWindow (AppKit)

### Popovers
Full page: hig/components/popovers.md · Platforms: iOS, iPadOS, macOS, visionOS
A transient view that appears above content when people click or tap a control or interactive area, for a small amount of related information or functionality. Not supported in tvOS or watchOS. Not for warnings (use an alert).

**Rules**
- **Use a popover to expose a small amount of information or functionality** — a few related tasks (e.g. change an event's date/time/calendar).
- **Consider popovers when you want more room for content** than a persistent sidebar or panel justifies for temporary content.
- **Position popovers appropriately:** the arrow points as directly as possible at the element that revealed it; don't cover that element or essential content.
- **Use a Close button (Cancel/Done) for confirmation and guidance only** (e.g. exit with or without saving). Otherwise a popover closes on outside click/tap or item selection; with multiple selections keep it open until explicit dismiss or outside tap.
- **Always save work when automatically closing a nonmodal popover.** Discard only on an explicit Cancel.
- **Show one popover at a time.** Never cascade or nest popovers; close the open one before showing another.
- **Don't show another view over a popover** — except an alert.
- **When possible, let people close one popover and open another with a single click or tap** (e.g. several bar buttons each with a popover).
- **Avoid making a popover too big.** Only large enough for its contents and to point at its source; the system may adjust size to fit.
- **Provide a smooth, animated transition when changing a popover's size** (condensed ↔ expanded) so it doesn't look like a new popover.
- **Avoid the word "popover" in help documentation.** Refer to the task or selection instead.
- **Avoid using a popover to show a warning.** People can miss or accidentally close it; use an alert.

**Platform notes**
- iOS/iPadOS: Avoid displaying popovers in compact views; adjust layout by size class, reserve popovers for wide views, and use a full-screen modal such as a sheet in compact views. · macOS: a popover can be detachable — dragging it turns it into a separate panel that stays visible. Consider letting people detach a popover. Make minimal appearance changes to a detached popover so people keep context. · visionOS: no additional considerations.

**Dev refs**
popover(isPresented:attachmentAnchor:arrowEdge:content:) (SwiftUI), UIPopoverPresentationController (UIKit), NSPopover (AppKit)

### Scroll views
Full page: hig/components/scroll-views.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Lets people move content larger than the view's bounds vertically or horizontally; has no appearance of its own beyond a translucent scroll indicator that shows position (beginning/middle/end) on iOS, iPadOS, macOS, visionOS and watchOS. Latest change 2026-06-08: scroll edge effect guidance.

**Rules**
- **Support default scrolling gestures and keyboard shortcuts.** Custom scrolling must keep the elastic indicator behavior people expect.
- **Make it apparent when content is scrollable** — e.g. show partial content at the edge of the view.
- **Avoid putting a scroll view inside another scroll view with the same orientation.** Horizontal inside vertical (or vice versa) is fine.
- **Consider page-by-page scrolling when it suits the content.** Page = current view height or width; subtract a unit of overlap (a line of text, a row of glyphs, part of a picture) to keep context.
- **Scroll automatically only to help people find their place:** when the app selects content or places the insertion point offscreen; when people start typing at a hidden insertion point; when the pointer moves past the view edge during selection; when a selection is offscreen before an operation. Scroll only as much as necessary (a partially visible selection needn't be fully scrolled in).
- **If you support zoom, set appropriate maximum and minimum scale values.**
- **Scroll edge effects (iOS, iPadOS, macOS)** visually separate floating elements such as toolbars from the scrolling content behind them. With custom bars, add the effect manually if the top layer needs clarity, and choose the automatic, hard or soft style.
- **Prefer the automatic scroll edge effect style.** It gives a more opaque separation for top toolbars with many controls, for text that sits outside Liquid Glass controls, and for pinned table headers. If you use the soft style, test legibility thoroughly across contexts.
- **Only use a scroll edge effect when a scroll view is behind floating interface elements.** It isn't decorative and doesn't block or darken like an overlay; it exists to keep controls distinct.
- **Apply one scroll edge effect per view.** In iPad/Mac split views each pane can have its own; keep their heights consistent for alignment.
- **iOS/iPadOS — Consider showing a page control when a scroll view is in page-by-page mode;** don't show the scroll indicator on the same axis as the page control.
- **macOS — If necessary, use small or mini scroll bars in a panel** that must coexist with other windows, and use the same control size for everything in that panel.
- **visionOS — If necessary, account for the size of the scroll indicator.** It's a little thicker than iOS's; widen tight margins so it doesn't overlap content.
- **visionOS — Support Look to Scroll for reading or browsing views.** It isn't on by default — add it to each scroll view.
- **visionOS — Avoid using Look to Scroll for secondary content** — views with UI controls or dense information needing quick, precise scrolling (Notes supports it in the main view, not the notes list).
- **visionOS — Maintain consistency across content:** if one view supports Look to Scroll, support it in all similar views.
- **visionOS — Define clear scroll areas:** prefer views that span the window's full width or height; an inset scroll view needs clear boundaries so people know where to look.
- **visionOS — Remove custom scroll effects or animations (parallax, scroll-position-driven changes) before supporting Look to Scroll.**
- **watchOS — Prefer vertically scrolling content;** the Digital Crown scrolls vertically when content is taller than the display.
- **watchOS — Use tab views to provide page-by-page scrolling.** A vertical stack of tab views pages with the Crown and shows a page indicator beside it (position within the page and within the set).
- **watchOS — When displaying paged content, consider limiting each page to a single screen height.** For long pages the indicator expands into a scroll indicator; use variable-height pages judiciously and after fixed-height pages.

**Platform notes**
- iOS/iPadOS: see Rules. · macOS: the indicator is called a scroll bar. · tvOS: views scroll but have no indicators; the system scrolls automatically to keep focused items visible. · visionOS: the indicator is small and fixed-size, vertically centered at the trailing edge (vertical scrolling) or horizontally centered at the bottom edge (horizontal); it appears when people start swiping; looking at it and dragging enables a jog bar with tick marks that controls scrolling speed rather than position. Look to Scroll starts when people look near the scroll view's boundary (top/bottom for vertical, sides for horizontal) and coexists with gestures. · watchOS: see Rules.

**Dev refs**
ScrollView, PagingScrollTargetBehavior, ScrollEdgeEffectStyle, ScrollEdgeEffectStyle.automatic, ScrollInputKind, ScrollInputKind.look (SwiftUI), UIScrollView, UIScrollEdgeEffect.Style (UIKit), NSScrollView, NSScrollEdgeEffectStyle (AppKit), WKPageOrientation (WatchKit)

### Sheets
Full page: hig/components/sheets.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
A view for a scoped task closely related to the current context — requesting specific information or a simple task completed before returning to the parent (attach a file, choose a save location). Always modal in macOS, tvOS, visionOS and watchOS; modal or nonmodal in iOS/iPadOS (Notes' format sheet is nonmodal). Latest change 2026-03-24: button placement.

**Rules**
- **Sheet buttons:** Cancel (or Close) dismisses without saving; Done dismisses after completing a task or explicitly saving; Back goes to the previous step or parent view and is not for dismissing. Placement varies by platform.
- **For complex or prolonged flows, consider alternatives to sheets:** iOS/iPadOS full-screen modal (video, photos, camera, document/photo editing); macOS a new window or full-screen mode; visionOS a Full Space.
- **Display only one sheet at a time from the main interface.** If a sheet must lead to another, close the first before showing the second (re-show the first afterwards if needed).
- **Use a nonmodal view for supplementary items that affect the main task:** split view in visionOS, panel in macOS, nonmodal sheet in iOS/iPadOS.
- **Provide an alternative to the Done button.** Always pair Done with Cancel (dismiss without saving) or Back (previous step); Done alone implies completing the task is the only exit.
- **Avoid showing Cancel, Done and Back together.**
- **iOS/iPadOS — Put Cancel on the leading edge of the top toolbar and Done (when present) on the trailing edge** of a single-view sheet. Multi-step flow: first step Cancel leading and Done trailing but inactive; subsequent steps Back replaces Cancel; final step Done becomes active to confirm and dismiss.
- **iOS/iPadOS — In an iPhone app, consider supporting the medium detent** for progressive disclosure (a share sheet shows the most relevant items at medium); skip it when content needs full height (Messages/Mail compose).
- **iOS/iPadOS — Include a grabber in a resizable sheet.** It signals resizability, taps cycle through detents, and it works with VoiceOver.
- **iOS/iPadOS — Support swiping to dismiss a sheet.** If there are unsaved changes when the swipe begins, confirm with an action sheet.
- **iPadOS — Prefer the page or form sheet presentation styles** (default size, centered over a dimmed background).
- **macOS — Present a sheet in a reasonable default size;** people don't expect to resize sheets, but support resizing when expanding content helps.
- **macOS — Let people interact with other app windows without first dismissing a sheet.** Opening a sheet brings its parent window — and a document's modeless panels — forward; other windows must still be bringable to the front.
- **macOS — Use a panel instead of a sheet when people repeatedly provide input and observe results** (find and replace).
- **visionOS — Avoid a sheet that emerges from the bottom edge of a window;** center it in the field of view.
- **visionOS — Present a default size that helps people retain context;** don't cover most or all of the window; consider letting people resize.
- **watchOS — Use a sheet only when the modal task requires a custom title or custom content presentation;** otherwise use an alert or action sheet.
- **watchOS — Keep sheet interactions brief and occasional;** a temporary interruption for an important task, never for navigating content.
- **watchOS — If you change the default dismiss label, prefer an SF Symbol;** avoid labels that imply hierarchical navigation or look like a page/app title.

**Platform notes**
- iOS/iPadOS: a resizable sheet expands when people scroll its contents or drag the grabber (a small horizontal indicator at the top edge). Detents (designed for iPhone) are heights at which a sheet rests: system detents are large (fully expanded) and medium (about half); custom detents allowed. Large is supported automatically; adding medium rests at both heights; medium alone prevents full height. · macOS: a cardlike rounded view floating over its dimmed parent window; people still expect to use other app windows. · tvOS: no additional considerations. · visionOS: the sheet floats in front of its dimmed parent window and takes the interactions. · watchOS: a full-screen view sliding over the current content, semitransparent with a blurred, desaturated material behind.

**Dev refs**
sheet(item:onDismiss:content:) (SwiftUI), UISheetPresentationController, UISheetPresentationController.detents, prefersGrabberVisible, UIModalPresentationStyle, UIModalPresentationStyle.fullScreen (UIKit), NSViewController.presentAsSheet(_:) (AppKit)

### Windows
Full page: hig/components/windows.md · Platforms: iPadOS, macOS, visionOS
Presents an app's views and components; defines content boundaries and enables multitasking. Primary windows carry main navigation and content; auxiliary windows are dedicated to one task, don't allow navigation elsewhere and usually include a close button. Not supported in iOS, tvOS or watchOS. Latest change 2025-06-09: resizable iPadOS windows.

**Rules**
- **Make sure windows adapt fluidly to different sizes** for multitasking and multiwindow workflows.
- **Choose the right moment to open a new window** (Mail opens Compose in a new window to keep the original visible). Opening windows excessively creates clutter; avoid it as default behavior.
- **Consider offering "view in new window"** via a context menu or File menu command.
- **Avoid creating custom window UI.** Don't make custom frames or controls or replicate the system look; imperfect copies feel broken.
- **Use the term "window" in user-facing content** — never "scene."
- **iPadOS — Make sure window controls don't overlap toolbar items.** Windowed apps show window controls at the toolbar's leading edge; move leading toolbar buttons inward when the controls appear.
- **iPadOS — Consider letting people use a gesture to open content in a new window** (pinch to expand a Notes item).
- **macOS — Make sure custom windows use the system-defined appearances** for main, key and inactive states; system components update automatically, custom ones must do it themselves.
- **macOS — Avoid putting critical information or actions in a bottom bar,** since people often hide a window's bottom edge; use it only for a small amount of content-related info (Finder's status bar: item counts, free space); use an inspector on the trailing side of a split view for more.
- **visionOS — Prefer a window to present a familiar interface and support familiar tasks;** reserve immersive experiences for meaningful content; use a volume for bounded 3D content like a game board.
- **visionOS — Retain the window's glass background.** It adapts to lighting with specular reflections and shadows that convey scale and position; removing it makes UI and text less legible and unrelated; an opaque background obscures surroundings and feels constricting and heavy.
- **visionOS — Choose an initial window size that minimizes empty areas.** Default 1280x720 pt, placed about two meters in front with an apparent width of about three meters; empty space looks oversized and hides other content.
- **visionOS — Aim for an initial shape that suits the content** (Keynote wide, Safari tall; a tower game tall, a driving game wide).
- **visionOS — Choose a minimum and maximum size for each window** so UI never overlaps when tiny or becomes unusable when huge.
- **visionOS — Minimize the depth of 3D content in a window.** The system adds highlights and shadows for depth, but clips content that extends too far from the surface; use a volume for deeper 3D.
- **visionOS volumes — Prefer a volume to display rich 3D content;** a UI-centric interface works best in a window.
- **visionOS volumes — Place 2D content so it looks good from multiple angles;** pin 2D content to areas of 3D content with an attachment.
- **visionOS volumes — In general, use dynamic scaling** to keep content legible at a distance; fixed scaling (the default) suits real-world-size objects like retail products.
- **visionOS volumes — Take advantage of the default baseplate glow** (visionOS 2+) that outlines the volume's floor on look and keeps the resize control findable; skip it when content is full-bleed or you draw a custom baseplate.
- **visionOS volumes — Consider offering high-value content in an ornament** (visionOS 2+) anchored e.g. `topBack` or `bottomFront` so it stays put relative to the viewer; not on the same edge as a toolbar or tab bar; prefer only one extra ornament.
- **visionOS volumes — Choose an alignment that supports interaction:** a baseplate parallel to the floor suits low-interaction content; tilting to match the viewer's gaze keeps content usable when reclining.

**Platform notes**
- iPadOS: windows present Full screen (switch via the app switcher) or Windowed (freely resizable, multiple onscreen, repositionable; size and placement remembered) per the Multitasking & Gestures setting. To preview a single file without your own window you still must support multiple windows (QLPreviewSceneActivationConfiguration). · macOS: anatomy = frame (above the body: window controls, toolbar; rarely a bottom bar below the body) + body; drag the frame to move, edges to resize. States: Main (frontmost; one per app), Key/active (accepts input; one onscreen; may be a floating panel rather than the main window; clicking the Dock icon makes only the most recent window key), Inactive (background; no vibrancy, looks subdued and farther away). Key windows use colored close/minimize/zoom controls; inactive and main-but-not-key windows use gray. Panels like Colors/Fonts become key only when people click their title bar or a keyboard-input component. · visionOS: styles are window (upright plane with an unmodifiable glass background, close button, window bar and resize controls; may add a Share button, tab bar, toolbar and ornaments; dynamic scale keeps apparent size constant) and volume (window-management controls whose close button and window bar turn to face the viewer); a plain style omits the glass background. The system positions the first window/volume; people can move them in the Shared Space and a Full Space.

**Specs**

| Item | Value |
|---|---|
| visionOS default window size | 1280x720 pt |
| Initial placement | about 2 m in front of the wearer |
| Apparent initial width | about 3 m |

**Dev refs**
Windows, WindowGroup, OpenWindowAction, DefaultWindowStyle, VolumetricWindowStyle, PlainWindowStyle, ornament(visibility:attachmentAnchor:contentAlignment:ornament:) (SwiftUI), UIWindow, UICollectionViewDelegate.collectionView(_:sceneActivationConfigurationForItemAt:point:), UIWindowScene.ActivationInteraction (UIKit), NSWindow (AppKit), QLPreviewSceneActivationConfiguration (QuickLook)

## Selection and input

### Color wells
Full page: hig/components/color-wells.md · Platforms: iOS, iPadOS, macOS, visionOS
A control that opens a color picker (system-provided or custom) so people can adjust the color of text, shapes, guides and other elements. Not supported in tvOS or watchOS.

**Rules**
- **Consider the system-provided color picker for a familiar experience.** It's consistent, lets people save a set of colors usable in any app, and matches across iOS, iPadOS and macOS.

**Platform notes**
- iOS/iPadOS/visionOS: no additional considerations. · macOS: clicking a color well highlights it (active), opens the color picker, and the well updates to the chosen color. Color wells support drag and drop between wells and from the picker to a well.

**Dev refs**
UIColorWell, UIColorPickerViewController (UIKit), NSColorWell (AppKit)

### Combo boxes
Full page: hig/components/combo-boxes.md · Platforms: macOS
A text field combined with a pull-down button: people type a custom value or choose from predefined values; custom values aren't added to the list. Not supported on other platforms.

**Rules**
- **Populate the field with a meaningful default value from the list** (needn't be the first item); an empty default is allowed but less helpful.
- **Use an introductory label** so people know what items to expect; title-style capitalization, ending with a colon.
- **Provide relevant choices** — the most likely values — alongside custom entry.
- **Make sure list items aren't wider than the text field** or they truncate.

**Dev refs**
NSComboBox (AppKit)

### Digit entry views
Full page: hig/components/digit-entry-views.md · Platforms: tvOS
A full-screen view prompting for a series of digits (a PIN) with a digit-specific keyboard; optional title and prompt above the digits. Not supported on other platforms.

**Rules**
- **Use secure digit fields** (asterisks instead of digits) whenever asking for sensitive data.
- **Clearly state the purpose** with a title and prompt explaining why digits are needed.

**Dev refs**
TVDigitEntryViewController (TVUIKit)

### Image wells
Full page: hig/components/image-wells.md · Platforms: macOS
An editable image view: once selected people can copy, paste or delete its image, and they can drag a new image in without selecting it first. Not supported on other platforms.

**Rules**
- **Revert to a default image when necessary** — if the well requires an image, show the default again when people clear it.
- **If the well supports copy and paste, make the standard Edit menu items and keyboard shortcuts available.**

**Dev refs**
NSImageView (AppKit)

### Pickers
Full page: hig/components/pickers.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
One or more scrollable lists of distinct values (values and order depend on device language); date pickers add calendar views and numeric keypad entry. Not for short lists (pull-down button) or very large sets (list/table).

**Rules**
- **Consider a picker for medium-to-long lists.** A short list → pull-down button (a picker adds too much visual weight); a very large set → list or table (adjustable height, index).
- **Use predictable, logically ordered values** (alphabetized countries) so hidden values are easy to anticipate.
- **Avoid switching views to show a picker.** Show it in context below or near the field being edited — typically at the bottom of a window or in a popover.
- **Consider less granularity for minutes in a date picker.** Default is 60 values (0–59); any interval that divides evenly into 60 is allowed (e.g. 0, 15, 30, 45).
- **iOS/iPadOS — Use a compact date picker when space is constrained.** Its button shows the current value in the accent color; the modal calendar and time editor allows multiple edits before tapping outside to confirm.
- **macOS — Choose a date picker style that suits your app:** textual for limited space and specific selections; graphical to browse a calendar, select a date range, or show a clock face.

**Platform notes**
- iOS/iPadOS: date picker styles — Compact (a button opening a modal editor), Inline (time only: wheels; date and time: an inline calendar), Wheels (also supports built-in/external keyboard entry), Automatic (system chooses by platform and mode). Modes — Date (months, days, years); Time (hours, minutes, optional AM/PM); Date and time; Countdown timer (hours and minutes up to 23 hours 59 minutes; not available in inline or compact). Values and order depend on device location. · macOS: textual and graphical styles. · tvOS: pickers available via SwiftUI Picker. · visionOS: no additional considerations. · watchOS: navigated with the Digital Crown; wheels style for lists and for date/time pickers; can show an outline, caption and scrolling indicator; for longer lists the navigationLink style shows the picker as a button that opens the options, and people can scrub options with the Crown without tapping.

**Dev refs**
Picker, DatePicker, PickerStyle.navigationLink (SwiftUI), UIDatePicker, UIPickerView (UIKit), NSDatePicker (AppKit)

### Segmented controls
Full page: hig/components/segmented-controls.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS
A linear set of two or more equal-width segments acting as buttons with text or images (optionally labeled beneath); offers a single choice, in macOS single or multiple choices, or momentary actions without selection state (Mail's Reply/Reply All/Forward). Not supported in watchOS. Not for switching between separate app sections (tab bar).

**Rules**
- **Use a segmented control for closely related choices that affect an object, state, or view** (attributes in an inspector, actions on the current view).
- **Consider a segmented control when grouping functions or showing selection state clearly matters;** grouping is preserved regardless of view size.
- **Keep control types consistent within one control.** Don't mix action segments into a selection control or show selection on an action control.
- **Limit the number of segments:** no more than about five to seven in a wide interface; no more than about five on iPhone.
- **Keep segment size consistent** (equal widths; consistent icon and title widths).
- **Prefer either text or images — not a mix — in a single control.**
- **Use content of similar size in each segment** so no segment looks over- or under-filled.
- **Use nouns or noun phrases for segment labels,** title-style capitalization; a text-labeled control needs no introductory text.

**Platform notes**
- iOS/iPadOS: Consider a segmented control to switch between closely related subviews (Calendar's New Event vs New Reminder); use a tab bar for separate app sections. · macOS: Consider introductory text, labels below symbol segments, and a tooltip per segment. Use a tab view — not a segmented control — for view switching in the main window area; use segmented controls in toolbars or inspector panes. Consider supporting spring loading (drag items over a segment and force click to activate without dropping). · tvOS: Consider a split view instead of a segmented control for content-filtering screens. Avoid placing other focusable elements close to a segmented control — segments select on focus, not click. · visionOS: looking at an icon segment shows a tooltip with the descriptive text you supply.

**Dev refs**
PickerStyle.segmented (SwiftUI), UISegmentedControl, UISegmentedControl.isMomentary (UIKit), NSSegmentedControl, NSSegmentedControl.SwitchTracking.momentary (AppKit)

### Sliders
Full page: hig/components/sliders.md · Platforms: iOS, iPadOS, macOS, visionOS, watchOS
A horizontal track with a thumb adjusted between minimum and maximum; the track fills with color up to the thumb; optional left/right icons illustrate the extremes. Not supported in tvOS. Not for audio volume on iOS/iPadOS.

**Rules**
- **Customize a slider's appearance if it adds value** — track color, thumb image and tint, left/right icons (small image icon → large image icon for an image-size slider).
- **Use familiar slider directions:** minimum on the leading side, maximum trailing (horizontal); minimum at the bottom, maximum at the top (vertical). A percentage runs 0 % leading to 100 % trailing.
- **Consider supplementing a slider with a text field and stepper** for wide ranges — the field shows/accepts exact values, the stepper increments whole values.
- **iOS/iPadOS — Don't use a slider to adjust audio volume.** Use a volume view (customizable; includes a volume slider and an output-device control).
- **macOS — Consider giving live feedback as the value changes** (Dock icons scale while dragging the Size slider).
- **macOS — Choose a slider style that matches expectations:** horizontal for a fixed start and end (opacity 0 to 100 percent); circular when values repeat or continue indefinitely (rotation 0 to 360 degrees; four spins = 1440 degrees).
- **macOS — Consider using a label to introduce a slider** (sentence-style capitalization, ending colon).
- **macOS — Use tick marks to increase clarity and accuracy** of the scale.
- **macOS — Consider adding labels to tick marks:** numbers or words; labeling only min and max is often enough; periodic labels help nonlinear scales (Energy Saver); also provide a tooltip showing the thumb's value on hover.
- **visionOS — Prefer horizontal sliders;** side-to-side gestures are easier than up-and-down.
- **watchOS — If necessary, create custom glyphs** for the slider's buttons (the system shows plus and minus by default).

**Platform notes**
- macOS: sliders can include tick marks. A linear slider's thumb is a narrow lozenge with the track filled up to it, often with min/max icons; a circular slider's thumb is a small circle and its tick marks are evenly spaced dots around the circumference. · visionOS: see Rules. · watchOS: a slider is a track shown as discrete steps or a continuous bar representing a finite range; people tap buttons at either side to change the value by a predefined amount. · tvOS: not supported.

**Dev refs**
Slider (SwiftUI), UISlider (UIKit), NSSlider (AppKit)

### Steppers
Full page: hig/components/steppers.md · Platforms: iOS, iPadOS, macOS, visionOS
A two-segment control that increases or decreases an incremental value; it displays no value itself, so it sits next to a field that does. Not supported in watchOS or tvOS.

**Rules**
- **Make the value a stepper affects obvious.**
- **Consider pairing a stepper with a text field when large value changes are likely** (number of copies on a print screen); steppers alone suit small changes.

**Platform notes**
- iOS/iPadOS/visionOS: no additional considerations. · macOS: For large value ranges, consider supporting Shift-click to change the value by more than the default increment (e.g. 10×).

**Dev refs**
UIStepper (UIKit), NSStepper (AppKit)

### Text fields
Full page: hig/components/text-fields.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
A rectangular area for entering or editing a small, specific piece of text (name, email). Not for larger amounts of text (use a text view).

**Rules**
- **Use a text field to request a small amount of information;** use a text view for larger amounts.
- **Show a hint (placeholder such as "Email" or "Password") when the field is empty;** because it disappears on typing, also consider a separate label describing the field.
- **Use secure text fields to hide private data** such as passwords.
- **Match the field's size to the quantity of anticipated text** so people can gauge how much to enter.
- **Evenly space multiple text fields;** stack them vertically when possible with consistent widths per kind (first/last name one width; address/city another).
- **Ensure tabbing between fields flows logically** (the system usually handles it).
- **Validate fields when it makes sense:** e.g. digits-only fields alert on non-digits; validate an email when people switch fields; validate a user name or password before they switch.
- **Use a number formatter for numeric data** (accepts only numbers; formats decimals, percentages, currency); don't assume the presentation — it varies by locale.
- **Adjust line breaks to the field's needs:** default clips text beyond the bounds; alternatively wrap at character or word level, or truncate with an ellipsis at the beginning, middle or end.
- **Consider an expansion tooltip** to show the full text of clipped/truncated content on pointer hover.
- **In iOS, iPadOS, tvOS and visionOS, show the appropriate keyboard type** for the content (numbers, URLs…).
- **Minimize text entry in tvOS and watchOS apps;** gather information with buttons where possible.

**Platform notes**
- iOS/iPadOS: Display a Clear button at the trailing end so people can erase input in one tap. Use images and buttons in text fields: the leading end indicates the field's purpose; the trailing end offers features such as a Bookmarks button. · macOS: Consider a combo box to pair text input with a list of choices. · tvOS/visionOS: no additional considerations. · watchOS: Present a text field only when necessary; prefer a list of options.

**Dev refs**
TextField, SecureField (SwiftUI), UITextField (UIKit), NSTextField (AppKit)

### Toggles
Full page: hig/components/toggles.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Lets people choose between two opposing states (on/off) with a distinct appearance per state; styles include switch and checkbox, and every platform also supports buttons that behave like toggles. Not for choosing from a list (pop-up button). Latest change 2024-03-29: macOS switches, checkbox titles, radio buttons.

**Rules**
- **Use a toggle for two opposing values that affect the state of content or a view.** For other actions, such as choosing from a list, use a different component (pop-up button).
- **Clearly identify the setting, view or content the toggle affects.** Context usually suffices; macOS apps often add a label; a toggle-style button uses an icon and changes its background per state.
- **Make the visual differences between states obvious** — add/remove a fill, show/hide a background shape, change inner details (checkmark, dot). Don't rely on color alone.
- **iOS/iPadOS — Use the switch toggle style only in a list row;** the row content supplies the label.
- **iOS/iPadOS — Change the default green only if necessary;** your accent color is acceptable if it contrasts enough with the uncolored (off) appearance.
- **iOS/iPadOS — Outside a list, use a button that behaves like a toggle, not a switch** (Phone's filter button gains a blue highlight when active and loses it when inactive).
- **iOS/iPadOS — Avoid supplying a label that explains such a button's purpose;** the icon plus alternate backgrounds carry the meaning.
- **macOS — Use switches, checkboxes and radio buttons in the window body, not the window frame** (never in a toolbar or status bar).
- **macOS — Prefer a switch for settings you want to emphasize;** it has more visual weight, so it suits controlling a group of settings rather than one.
- **macOS — Within a grouped form, consider a mini switch per row** (its height matches other controls); use a regular switch for a primary setting and mini switches for subordinates.
- **macOS — In general, don't replace a checkbox with a switch.**
- **macOS — Use a checkbox instead of a switch for a hierarchy of settings;** leading-edge alignment and indentation show dependencies.
- **macOS — Consider radio buttons for a set of more than two mutually exclusive options,** each with a unique label.
- **macOS — Consider a label to introduce a group of checkboxes** whose relationship isn't clear; align its baseline with the first checkbox.
- **macOS — Accurately reflect a checkbox's state:** on, off or mixed; a parent that controls subordinate checkboxes shows mixed when they differ (bold/italic/underline).
- **macOS — Prefer a set of radio buttons for mutually exclusive options;** use checkboxes when people can choose several.
- **macOS — Avoid listing too many radio buttons;** more than about five → pop-up button.
- **macOS — To present a single on/off setting, prefer a checkbox;** use a pair of labeled radio buttons only in rare cases where one checkbox can't communicate the opposing states.
- **macOS — Use consistent spacing for horizontal radio buttons,** sized to the longest label.

**Platform notes**
- macOS: checkbox = small square, empty off, checkmark on, dash mixed, usually with a trailing title (none in an editable checklist). Radio button = small circle plus label, typically in groups of two to five; selected = filled, deselected = empty; a mixed (dash) state is rarely useful — use a checkbox for mixed state. · tvOS/visionOS/watchOS: no additional considerations.

**Dev refs**
Toggle, ToggleStyle, ToggleStyle.switch, GroupedFormStyle, ControlSize (SwiftUI), UISwitch, UIButton.changesSelectionAsPrimaryAction (UIKit), NSButton.ButtonType.toggle, NSSwitch, NSButton.allowsMixedState (AppKit)

### Virtual keyboards
Full page: hig/components/virtual-keyboards.md · Platforms: iOS, iPadOS, tvOS, visionOS, watchOS
System keyboards on devices without physical keyboards, optimized per task (email keyboard adds "@" and ".com"); no keyboard shortcuts. Apps can substitute a custom input view in-app, and on iOS/iPadOS/tvOS ship a custom keyboard extension usable systemwide. Not supported in macOS. Latest change 2025-06-09: custom controls above the keyboard (Liquid Glass), watchOS keyboard.

**Rules**
- **Choose a keyboard that matches the content people are editing** (numbers-and-punctuation for numeric data). Specify the text input's semantic content type so the system picks a matching keyboard and refines corrections. Keyboard types: ASCII capable, ASCII capable number pad, Decimal pad, Default, Email address, Name phone pad, Number pad, Numbers and punctuation, Phone pad, Twitter, URL, Web search.
- **Consider customizing the Return key type** when it clarifies the task (a Search return key for search fields).
- **Custom input views** replace the system keyboard while in your app (Numbers' numeric entry view). Make sure yours makes sense in context — otherwise people wonder why they can't get the system keyboard back.
- **Play the standard keyboard sound while people type in a custom input view** (people can disable it in Settings > Sounds).
- **Custom keyboards (app extensions)** work in any app once chosen in Settings, except in secure text fields and phone number fields; people can install several and switch. Use them for systemwide novel input methods or unsupported languages; for in-app-only use, build a custom input view instead.
- **Provide an obvious, easy way to switch between keyboards** — people expect the Globe-key behavior (it replaces the Emoji key when multiple keyboards exist).
- **Avoid duplicating system-provided keyboard features.** On some devices the Emoji/Globe and Dictation keys appear beneath the keyboard automatically, even with custom keyboards.
- **Consider providing a keyboard tutorial in your app** (how to choose, activate, use and switch back), not inside the keyboard itself.

**Platform notes**
- iOS/iPadOS: Use the keyboard layout guide so the keyboard feels integrated and important UI stays visible. Place custom controls above the keyboard thoughtfully: an input accessory view should hold controls relevant to the current task (Numbers' calculation controls). If other views in your app use Liquid Glass, or the view looks out of place above the keyboard, apply Liquid Glass to the view containing the controls; a standard toolbar adopts Liquid Glass automatically. Use the keyboard layout guide and standard padding so the system positions the controls as expected. · tvOS: a linear keyboard appears for Siri Remote; a grid keyboard for other devices (layout adapts automatically); a digit-specific keyboard for digit entry views. · visionOS: the system keyboard supports direct and indirect gestures and appears in a separate, movable window — don't account for its location in layouts. · watchOS: a text field shows a keyboard if the screen is large enough, otherwise dictation or Scribble; you can't change the keyboard type but can set the content type to improve suggestions; a nearby paired iPhone can also enter text.

**Dev refs**
keyboardType(_:), textContentType(_:), submitLabel(_:), ToolbarItemPlacement (SwiftUI), UIKeyboardType, UITextContentType, UIReturnKeyType, UIResponder.inputViewController, UIResponder.inputAccessoryView, UIKeyboardLayoutGuide, UIDevice.playInputClick() (UIKit)

## Status

### Activity rings
Full page: hig/components/activity-rings.md · Platforms: iOS, iPadOS, watchOS
Shows one person's daily progress toward Move, Exercise and Stand goals. watchOS always shows three rings; iOS shows a single Move ring (approximated from steps and other apps' workouts) or all three when an Apple Watch is paired. Not supported in macOS, tvOS or visionOS. Never for other data, decoration or branding.

**Rules**
- **Display Activity rings when they're relevant to your app's purpose** (health/fitness apps, especially HealthKit contributors): e.g. on a workout metrics screen or an end-of-workout summary.
- **Use Activity rings only to show Move, Exercise and Stand information.** Never replicate or modify them for other data, and never show Move/Exercise/Stand progress in another ring-like element.
- **Use Activity rings for a single person.** Never represent more than one person; make it obvious whose progress it is with a label, photo or avatar.
- **Keep the visual appearance identical everywhere:** never change ring colors (no filters or opacity changes); always display on a black background; prefer enclosing rings and background in a circle by adjusting the enclosing view's corner radius rather than a circular mask; keep the black background visible around the outermost ring (add a thin black stroke if needed; no gradient, shadow or other effect); scale rings appropriately; design the surrounding interface to blend with the rings, never the reverse.
- **Use the matching ring colors for directly associated labels and values** (the Move/Exercise/Stand labels, current and goal values). The page gives these as RGB swatches (see Specs).
- **Maintain Activity ring margins:** minimum outer margin no less than the distance between rings; never let other elements crop, obstruct or encroach on it or the rings.
- **Differentiate other ring-like elements** with padding, lines, labels, color or scale.
- **Don't send notifications that repeat Activity app information,** and don't show an Activity ring element in your notifications; referencing progress in an app-specific way is fine.
- **Don't use Activity rings for decoration** (labels, background graphics).
- **Don't use Activity rings for branding** (app icon, marketing).

**Platform notes**
- iOS: available via HKActivityRingView; with an Apple Watch paired all three rings appear; without, only the Move ring; history can mix both styles. · iPadOS/watchOS: no additional considerations.

**Specs**

Label/value colors by ring (RGB values are rendered as colour swatches on the live page and did not survive the crawl — consult the source page):

| Move | Exercise | Stand |
|---|---|---|
|  |  |  |

**Dev refs**
HKActivityRingView (HealthKit)

### Gauges
Full page: hig/components/gauges.md · Platforms: iOS, iPadOS, macOS, visionOS, watchOS
Shows a specific numerical value within a range on a circular or linear path; the standard style marks the value with an indicator, the capacity style fills up to it; an accessory variant mirrors watchOS complications for Lock Screen widgets. macOS also offers level indicators. Not supported in tvOS.

**Rules**
- **Write succinct labels for the current value and both endpoints of the range.** Not every style shows them all, but VoiceOver reads the visible ones.
- **Consider filling the path with a gradient that communicates purpose** (red→blue for hot→cold).

**Platform notes**
- iOS/iPadOS/visionOS/watchOS: no additional considerations. · macOS: level indicators convey capacity, rating, or (rarely) relevance. Capacity is continuous (a translucent track filling with a solid bar) or discrete (a row of equal rectangular segments, one per unit of capacity, filling completely — never partially). Consider the continuous style for large ranges (discrete segments become too small). Consider changing the fill color at significant levels (default fill is green) — for the whole indicator, or with the tiered state showing a sequence of colors in one indicator. Rating style → see Rating indicators. Relevance style shades a horizontal bar, e.g. in sorted search results.

**Dev refs**
Gauge (SwiftUI), NSLevelIndicator (AppKit)

### Progress indicators
Full page: hig/components/progress-indicators.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Transient indicators that show the app isn't stalled during loading or lengthy operations. Determinate (known duration): a progress bar fills leading→trailing, a circular indicator fills clockwise. Indeterminate (activity indicator/spinner): an animated spinning image on all platforms; macOS also has an indeterminate bar.

**Rules**
- **When possible, use a determinate progress indicator** so people can decide whether to wait, restart later or abandon.
- **Be as accurate as possible and even out the pace.** 90 % in five seconds then 10 % in five minutes feels stalled or deceptive.
- **Keep progress indicators moving.** A stationary indicator reads as a frozen app; if a process stalls, explain the problem and what people can do.
- **Switch from indeterminate to determinate** as soon as the duration becomes known.
- **Don't switch from the circular style to the bar style.** Different shapes and sizes disrupt the interface.
- **If helpful, display a succinct description of the task.** Avoid vague terms like "loading" or "authenticating."
- **Display a progress indicator in a consistent location** across apps and platforms.
- **When feasible, let people halt processing:** a Cancel button when interruption is harmless; add Pause when cancelling loses work (partial download).
- **Let people know when halting has a negative consequence** — an alert offering to confirm the cancellation or resume.

**Platform notes**
- iOS/iPadOS: a refresh control is a hidden activity indicator that appears when people drag down a view (Mail's inbox). Perform automatic content updates too — don't make people initiate every refresh. Supply a short title only if it adds value (Podcasts shows the last update time); never use it to explain how to refresh. · macOS: indeterminate indicators come as a bar or a circular spinner. Prefer a spinner for background operations or constrained space (inside a text field, next to a button). Avoid labeling a spinner. · tvOS/visionOS: no additional considerations. · watchOS: indicators draw in white over the scene background by default; change the color via tint.

**Dev refs**
ProgressView (SwiftUI), UIProgressView, UIActivityIndicatorView, UIRefreshControl (UIKit), NSProgressIndicator (AppKit)

### Rating indicators
Full page: hig/components/rating-indicators.md · Platforms: macOS
A row of horizontally arranged symbols (stars by default) conveying a ranking level; values round to whole symbols (no partials); symbol spacing is fixed and doesn't stretch to the component width. Not supported on other platforms.

**Rules**
- **Make it easy to change rankings** — let people adjust an item's rank inline in a ranked list, without a separate editing screen.
- **If you replace the star with a custom symbol, make sure its purpose is clear;** the star is the universally recognized ranking symbol.

**Dev refs**
NSLevelIndicator.Style.rating (AppKit)

## System experiences

### App Shortcuts
Full page: hig/components/app-shortcuts.md · Platforms: iOS, iPadOS, visionOS, watchOS
Gives people access to an app's key functions or content throughout the system — via Siri, Spotlight, the Shortcuts app, the Action button on iPhone/Apple Watch, or an Apple Pencil squeeze. Built on App Intents; available the moment installation finishes; each app can include up to 10 App Shortcuts, each with one or more actions. Not supported in tvOS; macOS supports App Intents actions in the Shortcuts app but not App Shortcuts. Latest change 2026-06-08: app schemas.

**Rules**
- **To surface common types of functionality, consider adopting app schemas instead.** Apps in common domains adopt app schemas so Siri and system experiences surface features contextually via Apple Intelligence; App Shortcuts remain for unique features or custom content outside those domains.
- **Offer App Shortcuts for your app's most common and important tasks.** Prefer tasks people complete without leaving their context; opening the app is fine when it eases a multistep task.
- **Add flexibility with a single optional parameter** ("Start [morning, daily, sleep] meditation"). Use predictable, familiar values — people won't have the list in front of them.
- **Ask for clarification when a request lacks optional information** — suggest the most recently used value or one based on time of day; present the most likely option as a default plus a short list of alternatives.
- **Keep voice interactions simple.** A phrase that feels complicated aloud is hard to remember; avoid two parameters in one phrase ("Start [sleep] meditation with nature sounds") — ask for extra information in a subsequent step.
- **Make App Shortcuts discoverable in your app** — occasional tips when people perform the matching action (SiriTipUIView).
- **Respond appropriately:** use snippets for static information or dialog options (weather at a location, order confirmation); use Live Activities for information that stays relevant and changes over time (timers, countdowns).
- **Provide enough detail for audio-only devices** (AirPods, HomePod): put all critical information in the full dialogue text.
- **Provide brief, memorable activation phrases and natural variants.** Phrases must include the app name but can be creative (Keynote: "Create a Keynote" and "Add a new presentation in Keynote").
- **Write "App Shortcuts" and "the Shortcuts app" in title case with plural "Shortcuts";** write individual shortcuts in lowercase ("Run a shortcut by asking Siri").

**Platform notes**
- iOS/iPadOS: App Shortcuts appear in Spotlight's Top Hit area when people search for the app, or in the Shortcuts area below; each shows an SF Symbol you choose or a preview image of the linked item. Order shortcuts by importance — your order is the initial order in Spotlight and the Shortcuts app; the system later promotes the most-used ones. · macOS: App Shortcuts aren't supported, but App Intents actions let people build custom shortcuts in Shortcuts on Mac. · visionOS/watchOS: no additional considerations. · tvOS: not supported.

**Specs**

| Item | Value |
|---|---|
| App Shortcuts per app | up to 10 |
| Optional parameters per App Shortcut | one |

**Dev refs**
App Intents, App Shortcuts, AppShortcutPhrase, SiriTipUIView, LiveActivityIntent, IntentDialog.init(full:supporting:systemImageName:), app schema domains, SiriKit

### Complications
Full page: hig/components/complications.md · Platforms: watchOS
Displays timely, relevant information on the watch face; most faces show at least one, some four or more. Since watchOS 9 complications (accessories) are organized into families — circular, corner, inline, rectangular — with recommended layouts; legacy templates (circular small, modular small, modular large, extra large) are nongraphic styles that don't take the wearer's color. Build with WidgetKit for watchOS 9+, ClockKit for earlier.

**Rules**
- **Identify essential, dynamic content people want at a glance.** A static complication that doesn't show meaningful data is unlikely to keep a prominent spot.
- **Support all complication families when possible** so you're available on more faces; if a family can't show useful data, show an image (your app icon) that still launches the app.
- **Consider multiple complications per family** — e.g. one circular complication per triathlon segment, each deep-linking to its area — and offer a preconfigured shareable watch face.
- **Define a different deep link for each complication;** identical destinations make them feel less useful.
- **Keep privacy in mind:** the Always-On display may be visible to others.
- **Carefully consider when to update data.** Data is a timeline of entries with display times; timeline updates per day and stored entries per app are limited, so choose times that maximize usefulness (meeting info an hour before; forecast at the forecast time).
- **Choose a ring or gauge style by data type:** closed = a percentage of a whole (battery); open = arbitrary min/max not a percentage (speed); segmented = app-defined range conveying rapid changes (Noise).
- **Make images look good in tinted mode.** Tinted mode applies a single wearer-selected color to text, gauges and images and desaturates full-color images unless you supply tinted versions (legacy templates: graphic complications only). Don't use color as the only carrier of information; provide tinted-mode image variants when a desaturated image looks poor.
- **Recognize that people may prefer tinted mode** over full color.
- **Use line widths of two points or greater;** thinner lines are hard to see in motion.
- **Provide static placeholder images for each complication** (used on first install, and in the complication carousel). Sizes vary per layout/template and may not match the real image size.
- **Rectangular layouts may appear in the Smart Stack (watchOS 10+):** supply a background color or content that aids recognition, use intents to declare relevancy so it appears at useful times, and consider a custom Smart Stack-optimized layout.

**Platform notes**
- watchOS only; not supported in iOS, iPadOS, macOS, tvOS or visionOS.

**Specs**

Circular — regular-size images (system applies a circular mask):

| Image | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Image | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Closed gauge | 27x27 pt (54x54 px @2x) | 28.5x28.5 pt (57x57 px @2x) | 31x31 pt (62x62 px @2x) | 32x32 pt (64x64 px @2x) |
| Open gauge | 11x11 pt (22x22 px @2x) | 11.5x11.5 pt (23x23 px @2x) | 12x12 pt (24x24 px @2x) | 13x13 pt (26x26 px @2x) |
| Stack (not text) | 28x14 pt (56x28 px @2x) | 29.5x15 pt (59X30 px @2x) | 31x16 pt (62x32px @ 2x) | 33.5x16.5 pt (67x33 px @2x) |

Circular bezel text can fill nearly 180 degrees of the bezel before truncating. Regular circular default text: Rounded, Medium, 12 pt (40mm), 12.5 pt (41mm), 13 pt (44mm), 14.5 pt (45mm/49mm).

Circular — extra-large images (circular mask on circular, open-gauge and closed-gauge images):

| Image | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Image | 120x120 pt (240x240 px @2x) | 127x127 pt (254x254 px @2x) | 132x132 pt (264x264 px @2x) | 143x143 pt (286x286 px @2x) |
| Open gauge | 31x31 pt (62x62 px @2x) | 33x33 pt (66x66 px @2x) | 33x33 pt (66x66 px @2x) | 37x37 pt (74x74 px @2x) |
| Closed gauge | 77x77 pt (154x154 px @2x) | 81.5x81.5 (163x163 px @2x) | 87x87 pt (174x174 px @2x) | 91.5x91.5 (183x183 px @2x) |
| Stack | 80x40 pt (160x80 px @2x) | 85x42 (170x84 px @2x) | 87x44 pt (174x88 px @2x) | 95x48 pt (190x96 px @2x ) |

Circular-family placeholder images:

| Layout | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Circular | – | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Bezel | – | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Extra Large | – | 120x120 pt (240x240 px @2x) | 127x127 pt (254x254 px @2x) | 132x132 pt (264x264 px @2x) | 143x143 pt (286x286 px @2x) |

Extra-large circular default text: Rounded, Medium, 34.5 pt (40mm), 36.5 pt (41mm), 36.5 pt (44mm), 41 pt (45mm/49mm).

Corner images (circular mask on each):

| Image | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Circular | 32x32 pt (64x64 px @2x) | 34x34 pt (68x68 px @2x) | 36x36 pt (72x72 px @2x) | 38x38 pt (76x76 px @2x ) |
| Gauge | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |
| Text | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |

Corner placeholder images:

| 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| – | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |

Corner default text: Rounded, Semibold, 10 pt (40mm), 10.5 pt (41mm), 11 pt (44mm), 12 pt (45mm/49mm).

Inline — utilitarian small (corner rectangle; image, icon or circular graph):

| Content | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Flat | 9-21x9 pt (18-42x18 px @2x) | 10-22x10 pt (20-44x20 px @2x) | 10.5-23.5x21 pt (21-47x21 @2x) | N/A | 12-26x12 pt (24-52x24 px @2x) |
| Ring | 14x14 pt (28x28 px @2x) | 14x14 pt (28x28 px @2x) | 15x15 pt (30x30 px @2x) | 16x16 pt (32x32 px @2x) | 16.5x16.5 pt (33x33 px @2x) |
| Square | 20x20 pt (40x40 px @2x) | 22x22 pt (44x44 px @2x) | 23.5x23.5 pt (47x47 px @2x) | 25x25 pt (50x50 px @2x) | 26x26 pt (52x52 px @2x) |

Inline — utilitarian large (text-based, spans the face bottom; optional leading icon):

| Content | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Flat | 9-21x9 pt (18-42x18 px @2x) | 10-22x10 pt (20-44x20 px @2x) | 10.5-23.5x10.5 pt (21-47x21 px @2x) | N/A | 12-26x12 pt (24-52x24 px @2x) |

Rectangular images (both large-image layouts automatically include a four-point corner radius):

| Content | 40mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|
| Large image with title * | 150x47 pt (300x94 px @2x) | 159x50 pt (318x100 px @2x) | 171x54 pt (342x108 px @2x) | 178.5x56 pt (357x112 px @2x) |
| Large image without title * | 162x69 pt (324x138 px @2x) | 171.5x73 pt (343x146 px @2x) | 184x78 pt (368x156 px @2x) | 193x82 pt (386x164 px @2x) |
| Standard body | 12x12 pt (24x24 px @2x) | 12.5x12.5 pt (25x25 px @2x) | 13.5x13.5 pt (27x27 px @2x) | 14.5x14.5 pt (29x29 px @2x) |
| Text gauge | 12x12 pt (24x24 px @2x) | 12.5x12.5 pt (25x25 px @2x) | 13.5x13.5 pt (27x27 px @2x) | 14.5x14.5 pt (29x29 px @2x) |

Rectangular default text: Rounded, Medium, 16.5 pt (40mm), 17.5 pt (41mm), 18 pt (44mm), 19.5 pt (45mm/49mm).

Legacy — circular small (stack width = maximum):

| Image | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Ring | 20x20 pt (40x40 px @2x) | 22x22 pt (44x44 px @2x) | 23.5x23.5 pt (47x47 px @2x) | 24x24 pt (48x48 px @2x) | 26x26 pt (52x52 px @2x) |
| Simple | 16x16 pt (32x32 px @2x) | 18x18 pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21.5x21.5 pt (43x43 px @2x) |
| Stack | 16x7 pt (32x14 px @2x) | 17x8 pt (34x16 px @2x) | 18x8.5 pt (36x17 px @2x) | 19x9 pt (38x18 px @2x) | 19x9.5 pt (38x19 px @2x) |
| Placeholder | 16x16 pt (32x32 px @2x) | 18x18x pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21.5x21.5 pt (43x43 px @2x) |

Legacy — modular small (stack width = maximum):

| Image | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Ring | 18x18 pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22.5x22.5 pt (45x45 px @2x) |
| Simple | 26x26 pt (52x52 px @2x) | 29x29 pt (58x58 px @2x) | 30.5x30.5 pt (61x61 px @2x) | 32x32 pt (64x64 px @2x) | 34.5x34.5 pt (69x69 px @2x) |
| Stack | 26x14 pt (52x28 px @2x) | 29x15 pt (58x30 px @2x) | 30.5x16 pt (61x32 px @2x) | 32x17 pt (64x34 px @2x) | 34.5x18 pt (69x36 px @2x) |
| Placeholder | 26x26 pt (52x52 px @2x) | 29x29 pt (58x58 px @2x) | 30.5x30.5 pt (61x61 px @2x) | 32x32 pt (64x64 px @2x) | 34.5x34.5 pt (69x69 px @2x) |

Legacy — modular large (up to three rows):

| Content | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Columns | 11-32x11 pt (22-64x22 px @2x) | 12-37x12 pt (24-74x24 px @2x) | 12.5-39x12.5 pt (25-78x25 px @2x) | 14-42x14 pt (28-84x28 px @2x) | 14.5-44x14.5 pt (29-88x29 px @2x) |
| Standard body | 11-32x11 pt (22-64x22 px @2x) | 12-37x12 pt (24-74x24 px @2x) | 12.5-39x12.5 pt (25-78x25 px @2x) | 14-42x14 pt (28-84x28 px @2x) | 14.5-44x14.5 pt (29-88x29 px @2x) |
| Table | 11-32x11 pt (22-64x22 px @2x) | 12-37x12 pt (24-74x24 px @2x) | 12.5-39x12.5 pt (25-78x25 px @2x) | 14-42x14 pt (28-84x28 px @2x) | 14.5-44x14.5 pt (29-88x29 px @2x) |

Legacy — extra large (stack width = maximum):

| Image | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
|---|---|---|---|---|---|
| Ring | 63x63 pt (126x126 px @2x) | 66.5x66.5 pt (133x133 px @2x) | 70.5x70.5 pt (141x141 px @2x) | 73x73 pt (146x146 px @2x) | 79x79 pt (158x158 px @2x) |
| Simple | 91x91 pt (182x182 px @2x) | 101.5x101.5 pt (203x203 px @2x) | 107.5x107.5 pt (215x215 px @2x) | 112x112 pt (224x224 px @2x) | 121x121 pt (242x242 px @2x ) |
| Stack | 78x42 pt (156x84 px @2x) | 87x45 pt (174x90 px @2x) | 92x47.5 pt (184x95 px @2x) | 96x51 pt (192x102 px @2x) | 103.5x53.5 pt (207x107 px @2x) |
| Placeholder | 91x91 pt (182x182 px @2x) | 101.5x101.5 pt (203x203 px @2x) | 107.5x107.5 pt (215x215 px @2x) | 112x112 pt (224x224 px @2x) | 121x121 pt (242x242 px @2x) |

Minimum line width for complication content: 2 pt.

**Dev refs**
WidgetKit, WidgetRenderingMode, TimelineProvider.placeholder(in:), WidgetFamily.accessoryRectangular, App Intents (relevancy), CLKComplicationDataSource (ClockKit, pre-watchOS 9)

### Controls
Full page: hig/components/controls.md · Platforms: iOS, iPadOS, macOS
A button or toggle giving quick access to an app feature from Control Center, the Lock Screen or the Action button. Buttons perform an action, deep-link into the app, or launch a camera experience on a locked device; toggles switch between two states. People add controls by pressing and holding an empty area of Control Center, customizing the Lock Screen, or configuring the Action button in Settings. Not supported in watchOS, tvOS or visionOS.

**Rules**
- **Anatomy:** a symbol image (SF Symbol or custom), a title, and an optional value (state). Control Center shows the symbol, plus title and value at larger sizes; the Lock Screen shows the symbol only; pressing and holding an Action-button control shows the symbol and value in the Dynamic Island.
- **Offer controls for actions that provide the most benefit without launching your app** (e.g. starting a Live Activity from a control).
- **Update controls when people interact, when an action completes, or remotely via push notification** so state and in-progress status are accurate.
- **Choose a descriptive symbol that suggests the control's behavior,** since title and value may not be shown; toggles need both an on and an off symbol (`door.garage.open` / `door.garage.closed`).
- **Use symbol animations to highlight state changes:** animate a toggle's on/off transition; for buttons with a duration, animate indefinitely until the action completes.
- **Select a tint color that works with your brand.** It's applied to a toggle's on-state symbol and to the value and symbol shown in the Dynamic Island from the Action button.
- **Help people supply configuration the control needs** (which light to control); prompt when the control is first added; people can reconfigure any time.
- **Provide hint text for the Action button** — shown on press to explain what press-and-hold does; construct it with verbs.
- **If the title or value can vary, include a placeholder** shown in the controls gallery and before Action-button assignment.
- **Hide sensitive information when the device is locked:** have the system redact title and value, and optionally the symbol state (symbol then shows the off state).
- **Require authentication for actions that affect security** (unlock a door, start a car).
- **Camera experiences on a locked device (iOS 18+):** a control can launch straight into your camera experience while locked; anything beyond capture requires unlocking. Use the same camera UI in your app and the locked experience so the transition is seamless. Provide instructions for adding the control.

**Platform notes**
- iOS/iPadOS/macOS: no additional considerations. · watchOS/tvOS/visionOS: not supported.

**Dev refs**
WidgetKit, LockedCameraCapture, ControlWidgetConfiguration.promptsForUserConfiguration(), controlWidgetActionHint(_:), IntentAuthenticationPolicy (App Intents), Symbols, SymbolEffect

### Live Activities
Full page: hig/components/live-activities.md · Platforms: iOS, iPadOS, macOS, watchOS
Lets people track the progress of an activity, event or task at a glance, with frequent updates over a few hours and optional interaction (delivery ETA, live score, workout controls). Starts on iPhone or iPad and appears automatically on the Lock Screen, Home Screen, Dynamic Island and StandBy (iPhone), the Mac menu bar, the Apple Watch Smart Stack and the CarPlay Dashboard. Not for ads/promotions, and not for tasks without a defined end. Not supported in tvOS or visionOS. Latest change 2026-10-13: limited-width layouts, updated platforms and specs.

**Rules**
- **Support every presentation:** Compact (Dynamic Island with one active Live Activity; two elements, leading and trailing of the TrueDepth camera), Minimal (up to three Live Activities — one attached to the Dynamic Island, others detached as circles or ovals; tap opens the app, touch and hold expands), Expanded (shown on touch and hold of compact or minimal), Lock Screen (banner at the bottom of the Lock Screen; also the banner shown over the Home Screen/apps on devices without a Dynamic Island; lay it out like the expanded presentation). In StandBy the minimal presentation is shown; tapping switches to the Lock Screen presentation scaled 2x to fill the screen, with a custom background color extended edge to edge.
- **Offer Live Activities for tasks and events with a defined beginning and end** — short to medium duration, not exceeding eight hours.
- **Focus on the important, glanceable information;** tapping opens the app for detail.
- **Don't use a Live Activity to display ads or promotions.**
- **Avoid displaying sensitive information** (visible on the Lock Screen and Always-On): show an innocuous summary, or redact views and let people choose whether to show sensitive data.
- **Match your app's visual aesthetic and personality in both dark and light appearances.**
- **If you include a logo mark, display it without a container** and don't use the entire app icon.
- **Don't add elements to your app that draw attention to the Dynamic Island.**
- **Ensure text is easy to read:** large text, medium weight or heavier; use small text sparingly; key information legible at a glance.
- **Adapt to different screen sizes and presentations** using the Specs values; actual onscreen size may vary.
- **Adjust element size and placement for efficient use of space** — use only the space the content needs.
- **Support limited-width presentations** (Dynamic Island on iPhone in landscape): adapt compact and minimal presentations to fit a 28 pt-diameter circle using an abbreviation or graphic; if both leading and trailing can't make sense that small, adopt a leading view only and leave the trailing view empty (the system hides it).
- **Use familiar layouts for custom views** — Apple Design Resources templates with default system margins and recommended text sizes.
- **Use consistent margins and concentric placement:** even margins between rounded shapes and the Live Activity's edge; use ContainerRelativeShape to match corner radius near corners rather than hard-coding; keep content snug within a margin concentric to the outer edge.
- **When separating a block of content, place it in an inset container shape or use a thick line;** don't draw content to the edge of the Dynamic Island.
- **Dynamically change the height on the Lock Screen and in the expanded presentation** — shrink when there's less to show, grow as details (pickup time, driver details) arrive.
- **Carefully consider custom background color and opacity.** Compact, minimal and expanded backgrounds can't be customized; the Lock Screen presentation can — ensure contrast, especially for tints on an Always-On display with reduced luminance.
- **Use color to express your app's character.** The Dynamic Island background is opaque black; bold colors for text and objects make the Live Activity recognizable and reinforce relationships between elements.
- **Tint the key line color to match your content.** On dark backgrounds (Dark Mode) a key line surrounds the Dynamic Island; keep its color consistent with your other elements.
- **Animations run at most two seconds** (system or custom) and don't play on Always-On displays with reduced luminance.
- **Use animations to reinforce information and bring attention to updates** — move elements, use the default content-replace transition, or custom scale/opacity/movement transitions (numeric transitions for score changes; fade a timer out at zero).
- **Animate layout changes** (expanding in StandBy, new information) by moving existing elements to their new positions instead of removing and re-adding them.
- **Try to avoid overlapping elements;** in lists animate only the element that moves and fade the others.
- **Make sure tapping the Live Activity opens your app at the right location** (deep link to related details and actions).
- **Focus on simple, direct actions.** Interactive elements cost space; include them only for essential functionality people activate once or pause/resume (playback, workouts, recording); prefer a single interactive element to avoid mis-taps.
- **Consider letting people respond to updates** with a button or toggle (contact the driver while waiting).
- **Start Live Activities at appropriate times and make them easy to turn off in your app** (an unfollow button for a game/team); unexpected Live Activities feel unwanted and lead people to disable them in Settings.
- **Offer an App Shortcut that starts your Live Activity** (e.g. from the Action button).
- **Update a Live Activity only when new content is available.**
- **Alert people only for essential updates.** Alerts light the screen, play the notification sound by default, and show the expanded presentation (or a banner without a Dynamic Island); don't over-alert, and don't send push notifications for the same updates.
- **Let people track multiple events in a single Live Activity** with a dynamic layout that rotates through them, rather than several Live Activities.
- **Always end a Live Activity immediately when the task or event ends, and consider a custom dismissal time.** It's removed at once from the Dynamic Island and CarPlay; on the Lock Screen, the Mac menu bar and the watchOS Smart Stack it remains up to four hours. Choose a dismissal time proportional to the activity — 15 to 30 minutes is usually adequate (a rideshare summary stays 30 minutes for tipping).
- **Start with the iPhone design, then refine for other contexts** (StandBy, CarPlay, Apple Watch).
- **Compact:** show the most important dynamic information (two team logos and the score); design leading and trailing elements as one piece of information with consistent color and typography; keep content narrow and snug against the TrueDepth camera with no padding, don't obscure status bar information, keep both sides similarly sized (shortened units, less precise data); both elements must link to the same screen.
- **Minimal:** stay recognizable; prefer updated information over a static logo (Timer shows remaining time).
- **Expanded:** maintain the relative placement of elements from compact/minimal so layouts expand predictably; wrap content tightly around the TrueDepth camera to diminish its presence.
- **Lock Screen:** don't replicate notification layouts; choose colors that work on a personalized Lock Screen (use custom background/tint and opacity sparingly); by default light background in light appearance and dark in dark — a custom color must work in both or vary per appearance; verify on an Always-On display with reduced luminance; verify the system-generated dismiss button color and adjust if needed; standard layout margin is 14 points (tighter margins only for graphics or buttons).
- **StandBy:** update the layout for the larger scale and extra space; consider the default background color (blends with the bezel, softer look, and the system can scale the Live Activity slightly larger); use standard margins and don't extend graphics to the screen edge; verify in Night Mode, where the system applies a red tint.
- **CarPlay:** the system combines the compact leading and trailing elements into one Dashboard layout; interactive elements are deactivated. Consider a custom layout via the ActivityFamily.small supplemental family for larger text or more information; prefer timely content over buttons and toggles if people will see it while driving.

**Platform notes**
- iOS/iPadOS: no additional considerations. · macOS: active Live Activities appear in the menu bar of a paired Mac using the compact, minimal and expanded presentations; clicking launches iPhone Mirroring to show the app. · watchOS: appears at the top of the Smart Stack; the default view combines the compact leading and trailing elements; tapping opens your watchOS app, or without one a full-screen view with a button to open the iPhone app. Consider a custom watchOS layout to show more information and add a button or toggle — but the same layout is used in CarPlay where interactivity is deactivated, so omit buttons/toggles if people may be driving. Focus on essential information and significant updates: progress (delivery ETA), interactive elements (stopwatch/timer controls), significant updates (score changes). · tvOS/visionOS: not supported.

**Specs**

Where a Live Activity appears:

| Platform or system experience | Location |
|---|---|
| iPad and iPhone | Lock Screen, Home Screen, in the Dynamic Island and StandBy on iPhone |
| Mac | The menu bar |
| Apple Watch | Smart Stack |
| CarPlay | CarPlay Dashboard |

Limits: maximum recommended duration 8 hours; animations ≤ 2 s; limited-width compact/minimal target 28 pt-diameter circle; Lock Screen standard margin 14 pt; lingering after end up to 4 hours (Lock Screen, Mac menu bar, Smart Stack); recommended custom dismissal 15–30 min; StandBy scale 2x; prefer one interactive element.

CarPlay dimensions (pt; system may scale to the vehicle screen):

| Live Activity size (pt) |
|---|
| 240x78 |
| 240x100 |
| 170x78 |

CarPlay Smart Display Zoom test configurations (Settings > Display in CarPlay):

| Configuration | Resolution (pt) |
|---|---|
| Widescreen | 1920x720 |
| Portrait | 900x1200 |
| Standard | 800x480 |

iOS dimensions (pt):

| Screen dimensions (portrait) | Compact (leading and trailing) | Minimal (width given as a range) | Expanded (height given as a range) | Lock Screen (height given as a range) | Limited width |
|---|---|---|---|---|---|
| 430x932 | 62.33x36.67 | 36.67–45x36.67 | 408x84–160 | 408x84–160 | 28x28 |
| 393x852 | 52.33x36.67 | 36.67–45x36.67 | 371x84–160 | 371x84–160 | 28x28 |

iPadOS dimensions (pt):

| Screen dimensions (portrait) | Lock Screen (height given as a range) |
|---|---|
| 1366x1024 | 500x84–160 |
| 1194x834 | 425x84–160 |
| 1012x834 | 425x84–160 |
| 1080x810 | 425x84–160 |
| 1024x768 | 425x84–160 |

macOS dimensions: use the iOS dimensions.

watchOS dimensions (same as watchOS widgets in the Smart Stack):

| Apple Watch size | Size of a Live Activity in the Smart Stack (pt) |
|---|---|
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 42mm | 176x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 46mm | 194x80.5 |
| 49mm (Ultra 3, 4) | 198x81.5 |
| 49mm (Ultra 1, 2) | 191x81.5 |

**Dev refs**
ActivityKit, WidgetKit, SwiftUI, LiveActivityIntent (App Intents), ActivityFamily.small, EnvironmentValues.isDynamicIslandLimitedInWidth, ContainerRelativeShape, activitySystemActionForegroundColor(_:), padding(_:_:)

### Notifications
Full page: hig/components/notifications.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Timely, high-value information people understand at a glance; requires prior consent, after which people choose styles and delivery timing per urgency. Styles: a banner or view on the Lock Screen, Home Screen, Home View or desktop; a badge on the app icon; an item in Notification Center. Communication notifications (calls, messages) show contact avatars and group names instead of the app icon. Not for error messages (use an alert).

**Rules**
- **Provide concise, informative notifications.**
- **Avoid sending multiple notifications for the same thing,** even when unanswered — it fills Notification Center and invites people to turn you off.
- **Avoid telling people to perform specific tasks in your app;** offer notification actions for simple tasks instead, since instructions are forgotten after dismissal.
- **Use an alert — not a notification — to display an error message.**
- **Handle notifications gracefully when your app is in the foreground:** they aren't displayed, but the app receives the data — present it discoverably but unobtrusively (increment a badge, insert new data into the current view, as Mail does).
- **Avoid including sensitive, personal or confidential information** that others might see.
- **Create a short title if it provides context** (headline, event name, email subject) — brief enough to read at a glance, especially on Apple Watch. For a generic title like "New Document," let the system show the app name instead. Title-style capitalization, no ending punctuation. Communication notifications show the sender's name in the title area automatically.
- **Write succinct, easy-to-read content:** complete sentences, sentence case, proper punctuation; don't truncate — the system does.
- **Provide generically descriptive placeholder text for when previews are hidden** (the system then shows only the icon and the title "Notification"): e.g. "Friend request," "New comment," "Reminder," "Shipment"; sentence-style capitalization.
- **Avoid including your app name or icon;** the system shows a large app icon at the leading edge (communication: sender image badged with your icon).
- **Consider a sound** — custom (short, distinctive, professionally produced) or a system alert sound; don't rely on it for important information; you can't add a vibration programmatically.
- **Notification actions:** a detail view can hold up to four buttons for actions without opening the app (Calendar's Snooze). Provide beneficial, context-relevant, time-saving actions; short title-case labels; no app name or extraneous words; keep text brief to avoid truncation; account for localization.
- **Avoid an action that merely opens your app** — tapping the notification already does that.
- **Prefer nondestructive actions;** if you must include a destructive one, give enough context; the system styles destructive actions distinctly.
- **Provide a simple, recognizable icon for each action** (SF Symbols, existing or customized), shown on the trailing side of the action title.
- **Badging — use a badge only to show the number of unread notifications,** never weather, dates/times, stock prices or scores.
- **Make sure badging isn't your only way to communicate essential information;** people can turn badges off.
- **Keep badges up to date** as people open notifications; reducing the count to zero removes all related notifications from Notification Center.
- **Avoid custom images or components that mimic a badge;** people who disabled badges will be frustrated.
- **watchOS — Avoid using a short look as the only way to communicate important information;** it appears only briefly.
- **watchOS — Keep privacy in mind in short looks:** basic information only; no potentially sensitive information in the title.
- **watchOS — Consider a rich, custom long-look notification** so people get what they need without launching the app (SwiftUI Animations, SpriteKit or SceneKit).
- **watchOS — At minimum provide a static long-look interface; prefer a dynamic one too.** The static interface is used when there's no network or the iPhone companion app is unreachable; create and bundle its resources in advance.
- **watchOS — Choose a background appearance for the sash:** a custom color, or a light, translucent blurred look that works over a photo at the top of the content.
- **watchOS — Choose a background color for the content area:** transparent by default; white at 18 % opacity matches other system notifications; or a custom brand color.
- **watchOS — Provide up to four custom actions below the content area.** The system picks them by notification type (sharing the actionable types registered by your iPhone app) and always appends a Dismiss button at the bottom.
- **watchOS — Keep double tap in mind when ordering actions.** Double tap runs the first nondestructive action, so put the most-used action first (parking: extend 5 minutes, then 15 minutes, then an hour).

**Platform notes**
- iOS/iPadOS/macOS/tvOS/visionOS: no additional considerations. · watchOS: notifications arrive in two stages — a short look (appears on wrist raise, disappears on lower) and a long look (more detail; scroll by swipe or Digital Crown; dismiss by tap or lowering the wrist) — and are also listed in Notification Center; supported devices allow a double-tap response. A companion iPhone app that supports notifications lets watchOS provide default short- and long-look interfaces. Long looks are static (message plus static text/images) or dynamic (full content, more configuration); the content area is customizable but the overall structure isn't — a sash at the top showing the app icon and name, and a Dismiss button at the bottom below all custom buttons.

**Specs**

| Item | Value |
|---|---|
| Buttons in a notification detail view | up to 4 |
| Custom actions in a watchOS long look | up to 4 (plus system Dismiss) |
| watchOS long-look content background matching system notifications | white at 18 % opacity |

**Dev refs**
UNNotificationSound, UNNotificationCategory.hiddenPreviewsBodyPlaceholder, User Notifications, User Notifications UI (asking permission, handling notifications and actions), SwiftUI Animations, SpriteKit, SceneKit

### Snippets
Full page: hig/components/snippets.md · Platforms: iOS, iPadOS, macOS
A compact view shown when someone performs a task with Siri, Spotlight, the Shortcuts app or an App Shortcut, presented from an app intent. Two types: a confirmation snippet (confirm or cancel, optionally with options affecting the result) and a result snippet (information needing no further action; an intent that shows a snippet always shows a result, the confirmation step is optional). Not supported in tvOS, visionOS or watchOS. New page 2026-06-08.

**Rules**
- **Anatomy:** dialogue (the intent dialogue Siri speaks, shown above the custom view by default), a custom view (may include buttons to modify content, get more information or take another action), and system-provided buttons — confirmation: a secondary Cancel and a primary button with a customizable label; result: a single Done button.
- **Ensure legibility:** sufficient contrast between custom content and the system background in light and dark, with consistent content margins.
- **Keep content concise.** Custom views must be no taller than the 400-point maximum height; remember fonts scale with preferred text size; for more detail in a result snippet, deep-link into the app instead.
- **Choose a descriptive label for a confirmation snippet's primary button** — a system-provided name or a custom one ("Order," not "OK" or "Proceed"); the default is Continue.
- **Communicate a snippet's purpose visually.** Spoken dialogue matters when people aren't looking; prefer omitting the dialogue text from the visual snippet and let the custom view carry the information.

**Platform notes**
- iOS/iPadOS/macOS: no additional considerations. · tvOS/visionOS/watchOS: not supported.

**Specs**

| Item | Value |
|---|---|
| Maximum custom view height | 400 pt |
| Default primary button label (confirmation) | Continue |

**Dev refs**
App Intents, ConfirmationActionName, Displaying static and interactive snippets

### Status bars
Full page: hig/components/status-bars.md · Platforms: iOS, iPadOS
The strip along the upper screen edge showing device state — time, carrier, battery. Not supported in macOS, tvOS, visionOS or watchOS.

**Rules**
- **Obscure content under the status bar.** Its background is transparent by default, so content can make it unreadable and people may try to tap controls behind it; keep it readable and don't imply content behind it is interactive. Prefer a scroll edge effect to place a blurred view behind the status bar.
- **Consider temporarily hiding the status bar when displaying full-screen media** (Photos hides it and other UI while browsing full-screen photos).
- **Avoid permanently hiding the status bar;** people shouldn't leave your app to check the time or Wi-Fi. Provide a simple, discoverable gesture to bring it back (a single tap in Photos).

**Platform notes**
- iOS/iPadOS: no additional considerations. · other platforms: not supported.

**Dev refs**
UIStatusBarStyle, UIViewController.preferredStatusBarStyle, UIScrollEdgeEffect (UIKit), ScrollEdgeEffectStyle (SwiftUI)

### Top Shelf
Full page: hig/components/top-shelf.md · Platforms: tvOS
The area of the Apple TV Home Screen that showcases your content when people select your app in the Dock — full-screen swipeable previews, trailers, and More Info — with system layout templates downloadable from Apple Design Resources. Not supported on other platforms. Not for ads or prices.

**Rules**
- **Help people jump right into your content.** The carousel actions and carousel details templates each include two buttons by default: a primary button to begin playback and a More Info button opening a detail view in your app.
- **Feature new content** — new releases, episodes, upcoming movies and shows; avoid promoting content people already purchased, rented or watched.
- **Personalize people's favorite content** — targeted recommendations, resume playback, jump back into gameplay.
- **Avoid showing advertisements or prices.** Purchasable content is fine; show prices only when people show interest.
- **Showcase compelling dynamic content;** prefer layered images over static ones.
- **If you don't provide full-screen content, supply at least one static image as a fallback** — shown when the app is in the Dock and focused; tvOS flips and blurs it to fit a width of 1920 pixels at 16:9.
- **Avoid implying interactivity in a static image;** it isn't focusable.
- **Carousel actions** (full-screen video and images, unobtrusive controls; for content people already know — user-generated photos, a known franchise): provide a succinct title (show, movie, album) and optionally a brief subtitle (date range, show name).
- **Carousel details** (adds plot summary, cast, metadata): provide a title identifying the currently playing content near the top; optionally a succinct phrase or attribution above it ("Featured on *My App*").
- **Sectioned content row** (a labeled, focusable row for recent, new or favorite content; the label appears on focus; remote movement animates the focused image; multiple labels allowed): provide enough content to fill a complete row — at least enough images to span the screen width — and at least one label.
- **Be aware of additional scaling when combining image sizes in a row:** images scale up to the height of the tallest, e.g. a 16:9 image becomes 500 pixels high next to a poster or square image.
- **Scrolling inset banner** (large images spanning nearly the full width; auto-scrolls on a timer until one is focused; loops; focus adds lighting and a 3D effect for layered images; swipe moves between banners): provide three to eight images (fewer than three feels ineffective, more than eight is hard to navigate).
- **If you need text in a banner, add it to the image itself** (no labels are shown); in layered images put text on a dedicated top layer; add the text to the image's accessibility label for VoiceOver.

**Platform notes**
- tvOS only; not supported in iOS, iPadOS, macOS, visionOS or watchOS.

**Specs**

Static fallback image:

| Image size |
|---|
| 2320x720 pt (2320x720 px @1x, 4640x1440 px @2x) |

Sectioned content row — Poster (2:3):

| Aspect | Image size |
|---|---|
| Actual size | 404x608 pt (404x608 px @1x, 808x1216 px @2x) |
| Focused/Safe zone size | 380x570 pt (380x570 px @1x, 760x1140 px @2x) |
| Unfocused size | 333x570 pt (333x570 px @1x, 666x1140 px @2x) |

Sectioned content row — Square (1:1):

| Aspect | Image size |
|---|---|
| Actual size | 608x608 pt (608x608 px @1x, 1216x1216 px @2x) |
| Focused/Safe zone size | 570x570 pt (570x570 px @1x, 1140x1140 px @2x) |
| Unfocused size | 500x500 pt (500x500 px @1x, 1000x1000 px @2x) |

Sectioned content row — 16:9:

| Aspect | Image size |
|---|---|
| Actual size | 908x512 pt (908x512 px @1x, 1816x1024 px @2x) |
| Focused/Safe zone size | 852x479 pt (852x479 px @1x, 1704x958 px @2x) |
| Unfocused size | 782x440 pt (782x440 px @1x, 1564x880 px @2x) |

Scrolling inset banner:

| Aspect | Image size |
|---|---|
| Actual size | 1940x692 pt (1940x692 px @1x, 3880x1384 px  @2x) |
| Focused/Safe zone size | 1740x620 pt (1740x620 px @1x, 3480x1240 px @2x) |
| Unfocused size | 1740x560 pt (1740x560 px @1x, 3480x1120 px @2x) |

Other numbers: static image is blurred to fit a 1920 px width at 16:9; banners 3–8 images; mixed-size rows scale to the tallest image (16:9 → 500 px high beside poster/square).

### Watch faces
Full page: hig/components/watch-faces.md · Platforms: watchOS
The primary view people choose in watchOS and customize with complications, often different faces per activity; in watchOS 7 and later faces can be shared, including from your app, website, Messages, Mail or social media. Not supported on other platforms.

**Rules**
- **Help people discover your app by sharing watch faces that feature your complications.** Ideally support multiple complications to curate a face; some faces also accept a system accent color, images or styles; if the app isn't installed, the system prompts to install it.
- **Display a preview of each watch face you share.** Get one by emailing the face to yourself from the iOS Watch app; it includes an illustrated bezel suitable for websites and apps, or composite a high-fidelity hardware bezel from Apple Design Resources.
- **Aim to offer shareable watch faces for all Apple Watch devices.** California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact and Solar Dial require Series 4 or later; Explorer requires Series 3 (cellular) or later. If you use one of these, offer a similar configuration on a face available on Series 3 and earlier, and label each face with the devices it supports.
- **Respond gracefully if people choose an incompatible watch face.** The system sends your app an error on Series 3 or earlier; immediately offer an alternative compatible configuration instead of showing the error, and set expectations in your previews.

**Platform notes**
- watchOS only; not supported in iOS, iPadOS, macOS, tvOS or visionOS.

**Dev refs**
Sharing an Apple Watch face (ClockKit)

### Widgets
Full page: hig/components/widgets.md · Platforms: iOS, iPadOS, macOS, watchOS, visionOS
Quick access to essential information and focused interactions from an app or game outside the app: on the iPhone/iPad Home Screen and Lock Screen, the Mac desktop and Notification Center, visionOS horizontal/vertical surfaces, the Apple Watch Smart Stack, and the Home Screen and Modular face of Apple HomeView. Widgets refresh periodically, not in real time (use Live Activities for that). Not supported in tvOS. Latest change 2026-10-13: Apple HomeView, watchOS specs.

**Rules**
- **Design for the size, the context (devices and system experiences), and the rendering mode/color treatment** the widget receives; WidgetKit provides defaults, but custom designs per context give the best experience.
- **System family sizes:** small, medium, large, extra large, extra large portrait (see Specs for supported contexts). **Accessory sizes:** circular, corner, inline, rectangular.
- **Appearances:** on the iPad/iPhone/Apple HomeView Home Screen people choose light, dark, clear or tinted — light/dark are full-color; clear desaturates and adds translucency, highlights and the Liquid Glass material; tinted desaturates and applies the person's tint color. On Apple Vision Pro a widget is a 3D object in a frame with a glass- or paper-like coating responding to light, optionally tinted from system palettes. On the iPad Lock Screen widgets are monochrome without tint. In StandBy and on the HomeView Modular face the widget is scaled up with its background removed, and rendered in monochrome red below an ambient-light threshold. Rectangular accessory widgets are monochrome on the iPhone/iPad Lock Screen and full-color or tinted as Watch complications and in the Smart Stack.
- **Rendering modes:** full color (system family, all platforms; views untouched); accented (system family on all platforms and accessory widgets on Apple Watch; background removed and replaced by a tint effect for tinted or a Liquid Glass background for clear; views split into an accent group and a primary group, each solid-colored); vibrant (Lock Screen on iPhone/iPad and StandBy low light; desaturates text, images and gauges and colors them for the Lock Screen background or Mac desktop; red tint in StandBy low light).
- **Choose simple ideas that relate to your app's main purpose** with timely content and relevant functionality (Weather: current high/low and conditions).
- **Give people quick access to the content they want** — meaningful content, useful actions, deep links; replicating the app icon adds little value.
- **Prefer dynamic information that changes throughout the day;** static content loses its prominent position.
- **Look for opportunities to surprise and delight** (special treatment on birthdays, holidays).
- **Offer multiple sizes only when each adds value.** Don't just expand a small widget's content; one widget in its best size beats all sizes.
- **Balance information density:** essential information at a glance, details on a longer look; if too dense, use a larger size or replace text with graphics.
- **Display only information directly related to the widget's main purpose** (Calendar widgets stay centered on upcoming events at every size).
- **Use brand elements thoughtfully** — colors, typefaces, stylized glyphs without overpowering content; a small logo in the top-right corner only when needed (multi-source content).
- **Choose between automatic content and user configuration** (Stocks configurable; Podcasts automatic).
- **Avoid mirroring your widget's appearance within your app;** look-alike elements that don't behave like widgets confuse.
- **Let people know when authentication adds value** ("Sign in to view reservations").
- **Keep your widget up to date** at a frequency matching the data (hourly tide conditions); if people check more often than you can update, show when data was last updated.
- **Use system functionality to refresh dates and times** to preserve update opportunities; show content quickly rather than hiding stale data behind placeholders.
- **Use animated transitions (up to two seconds) to bring attention to data updates;** many SwiftUI views animate by default.
- **Interactivity:** tap/click launches the app; buttons and toggles offer functionality without launching (Reminders' completion toggles); anything outside buttons/toggles launches the app.
- **Offer simple, relevant functionality and reserve complexity for your app.**
- **Ensure a widget interaction opens your app at the right location** (medium Stocks widget → the tapped symbol's page).
- **Offer interactivity while remaining glanceable and uncluttered:** multiple targets (links, buttons, toggles) are allowed but avoid app-like layouts; size targets for confident taps; inline accessory widgets offer only one tap target.
- **In general, use standard margins:** 16 points for most widgets; 11 points works for tighter groupings of graphics, buttons or background shapes; margins are smaller on the Mac desktop and on the Lock Screen including StandBy. iOS resizes content designed for large devices onto small ones; iPadOS renders at a large size then scales down for the Home Screen; supply content at appropriate sizes and let the system scale.
- **Coordinate your content's corner radius with the widget's** using a SwiftUI container (ContainerRelativeShape).
- **Prefer the system font, text styles and SF Symbols;** use a custom font sparingly (works for the large text, with SF Pro for small text).
- **Avoid font sizes smaller than 11 points.**
- **Avoid rasterizing text** — keep it as text for scaling and VoiceOver. In iOS, iPadOS and visionOS widgets support Dynamic Type sizes from Large to AX5 with system or custom fonts.
- **Use color to enhance without competing with content;** specify asset-catalog colors for the system-generated editing-mode UI.
- **Convey meaning without relying on specific colors** — widgets can be monochrome, and watchOS may invert colors per face; use text and iconography too.
- **Use full-color images judiciously.** In tinted or clear appearances the system desaturates them by default; opting into full color draws attention and can feel out of place (especially in clear); reserve it for media content like album art, at dimensions smaller than the widget.
- **Full-color mode: support light and dark appearances** — light backgrounds for light, dark for dark; semantic system colors or asset-catalog color variants.
- **Accented mode: group components into an accent group and a primary group.** iPhone, iPad and Mac tint both groups white; Apple Watch tints primary white and accented in the watch face color.
- **Vibrant mode: offer enough contrast.** Pixel opacity controls the strength of the blurred material (transparent pixels pass it through); pixel brightness controls vibrancy — brighter grays give more contrast. Create optimized assets: render images, numbers and text at full opacity; white or light gray for prominent content, darker grayscale for secondary; verify grayscale contrast; use opaque grayscale values rather than white at reduced opacity.
- **Design a realistic preview for the widget gallery** (real data, or realistic simulated data if real data loads slowly).
- **Design placeholder content that helps people recognize your widget:** static components plus semi-opaque shapes — rectangles of varied widths for text, circles/squares for glyphs and images.
- **Write a succinct widget description** beginning with an action verb ("See the current weather conditions and forecast for a location"); avoid "This widget shows…," "Use this widget to…," "Add this widget"; sentence-style capitalization.
- **Group your widget's sizes together with a single description.**
- **Consider coloring the Add button** shown below your widgets in the gallery to echo your brand.
- **iOS/iPadOS — Support the Always-On display on iPhone.** Lock Screen widgets render with reduced luminance; use gray levels with enough contrast so content stays legible.
- **iOS/iPadOS — Offer Live Activities to show real-time updates;** widgets don't. They share frameworks and design with widgets, so develop them in tandem and reuse code and components.
- **iOS/iPadOS — Limit rich images or color to convey meaning in StandBy.** Use the extra space to scale up and rearrange text for reading at a distance, and mark the widget's background as removable so it can appear in StandBy.
- **visionOS — Adapt your design and content for the spatial experience.** Widgets live in rooms, kitchens and offices (Music becomes a poster with large type and a high-resolution image; a productivity widget fits on a desk).
- **visionOS — Test widgets across the full range of system color palettes and lighting conditions;** if you exclude elements from tinting, verify they stay legible in every palette.
- **visionOS — Design a responsive layout for the two distance thresholds:** simplified (viewed at a distance — fewer details, larger type, no buttons or toggles) and default (nearby — more detail, smaller type); keep shared elements across both so the layout feels continuous.
- **visionOS — Offer widget family sizes that fit a person's surroundings** (a small widget for a desk; an extra large one for wall art or photography).
- **visionOS — Display content so it remains legible from a range of distances.** People can scale a widget from 75 to 125 percent; use print-design hierarchy, strong typography and scale, and include high-resolution assets.
- **visionOS — Choose the mounting style that fits your content.** Elevated (default) suits content that should stand out (reminders, media, glanceable data); recessed suits immersive or ambient content (weather, editorial) and only vertical surfaces; opt out of a style per widget (a weather app might make large/extra-large widgets recessed-only and the small one elevated-only). Declare styles per WidgetConfiguration and use separate configurations for widgets with different support.
- **visionOS — Test elevated widget designs with each system-provided frame width;** the layout can't change per frame width, so it must stay balanced in all of them.
- **visionOS — Choose the paper style for a print-like look that feels like a real object** (Music poster); the whole widget responds to ambient light.
- **visionOS — Choose the glass style for information-rich widgets;** foreground elements stay in full color and crisp regardless of lighting (News headlines over soft editorial images).
- **watchOS — Provide a colorful background that conveys meaning.** Smart Stack widgets default to black; Stocks uses red for falling and green for rising values.
- **watchOS — Encourage the system to display or elevate your widget in the Smart Stack** with relevancy information — location-based or tied to ongoing system actions like a workout.

**Platform notes**
- iOS/iPadOS: Lock Screen widgets are functionally like complications and follow complication guidance too; a complication design often works as a Lock Screen widget and vice versa. Three Lock Screen styles: inline text above the clock, circular and rectangular below it. StandBy shows two small system widgets side by side, scaled up to fill the Lock Screen; supporting StandBy also makes widgets work in CarPlay — both use the small family with the background removed, scaled to the Widgets screen grid, where glanceable large text matters. StandBy in low light renders widgets monochrome with a red tint. Apple HomeView uses small system widgets sharing the iPhone appearance, chosen from those installed on HomeView (Weather, World Clock) or on a connected iPad/iPhone; the Modular face holds up to four widgets, which may come from different household members' iPhones (one Modular face per household); each enrolled member has a personalized Home Screen of widgets and apps. · macOS: no additional considerations. · visionOS: widgets are 3D objects placed on horizontal or vertical surfaces that persist across power cycles at a consistent real-world scale; full-color by default, accented when people tint them from system palettes; people can change the frame width of elevated widgets and any widget-specific options (Music poster offers a light/dark theme generated from album art, since visionOS has no systemwide light/dark appearance). Thresholds: simplified (distance) and default (nearby). Mounting styles: elevated — on horizontal surfaces the widget sits raised, tilts back slightly and casts a soft shadow; on vertical surfaces it sits flush like a picture frame; recessed — vertical surfaces only, content set back into the surface like a cutout. Treatment styles: paper (grounded, print-like; darkens or lightens with ambient light) and glass (lighter, layered; foreground never dims or brightens). · watchOS: see Rules. · tvOS: not supported.

**Specs**

Supported contexts per system family size:

| Widget size | iPhone | iPad | Mac | Apple Vision Pro |
|---|---|---|---|---|
| System small | Home Screen, Today View, StandBy, CarPlay, and Apple HomeView | Home Screen, Today View, and Lock Screen | Desktop and Notification Center | Horizontal and vertical surfaces |
| System medium | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System large | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large | Not supported | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large portrait | Not supported | Not supported | Not supported | Horizontal and vertical surfaces |

Accessory widgets:

| Widget size | iPhone | iPad | Apple Watch |
|---|---|---|---|
| Accessory circular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |
| Accessory corner | Not supported | Not supported | Watch complications |
| Accessory inline | Lock Screen | Lock Screen | Watch complications |
| Accessory rectangular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |

Rendering mode occurrences per platform:

| Platform | Full-color | Accented | Vibrant |
|---|---|---|---|
| iPhone | Home Screen, Today view, StandBy and CarPlay (with the background removed) | Home Screen and Today view | Lock Screen, StandBy in Night Mode |
| iPad | Home Screen and Today view | Home Screen and Today view | Lock Screen |
| Apple Watch | Smart Stack, complications | Smart Stack, complications | Not supported |
| Mac | Desktop and Notification Center | Not supported | Desktop |
| Apple Vision Pro | Horizontal and vertical surfaces | Horizontal and vertical surfaces | Not supported |
| Apple HomeView | Home Screen, Modular face (with the background removed) | Home Screen, Modular face (with the background removed) | Modular face in Night Mode |

Layout numbers: standard margin 16 pt; tight margin 11 pt; minimum font size 11 pt; Dynamic Type Large–AX5 (iOS/iPadOS/visionOS); update animations ≤ 2 s; visionOS user scaling 75–125 %; HomeView Modular face up to 4 widgets; StandBy shows 2 small widgets.

iOS dimensions:

| Screen size (portrait, pt) | Small (pt) | Medium (pt) | Large (pt) | Circular (pt) | Rectangular (pt) | Inline (pt) |
|---|---|---|---|---|---|---|
| 430×932 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 428x926 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 414x896 | 169x169 | 360x169 | 360x379 | 76x76 | 160x72 | 248x26 |
| 414x736 | 159x159 | 348x157 | 348x357 | 76x76 | 170x76 | 248x26 |
| 393x852 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 390x844 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 375x812 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 375x667 | 148x148 | 321x148 | 321x324 | 68x68 | 153x68 | 225x26 |
| 360x780 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 320x568 | 141x141 | 292x141 | 292x311 | N/A | N/A | N/A |

iPadOS dimensions:

| Screen size (portrait, pt) | Target | Small (pt) | Medium (pt) | Large (pt) | Extra large (pt) |
|---|---|---|---|---|---|
| 768x1024 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
|  | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 744x1133 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
|  | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 810x1080 | Canvas | 146x146 | 320.5x146 | 320.5x320.5 | 669x320.5 |
|  | Device | 124x124 | 272x124 | 272x272 | 568x272 |
| 820x1180 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
|  | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 834x1112 | Canvas | 150x150 | 327.5x150 | 327.5x327.5 | 682x327.5 |
|  | Device | 132x132 | 288x132 | 288x288 | 600x288 |
| 834x1194 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
|  | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 954x1373 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
|  | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 970x1389 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
|  | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 1024x1366 | Canvas | 170x170 | 378.5x170 | 378.5x378.5 | 795x378.5 |
|  | Device | 160x160 | 356x160 | 356x356 | 748x356 |
| 1192x1590 * | Canvas | 188x188 | 412x188 | 412x412 | 860x412 |
|  | Device | 188x188 | 412x188 | 412x412 | 860x412 |

_* When Display Zoom is set to More Space._

visionOS dimensions:

| Widget | Size in pt | Size in mm (scaled to 100%) |
|---|---|---|
| Small | 158x158 | 268x268 |
| Medium | 338x158 | 574x268 |
| Large | 338x354 | 574x600 |
| Extra large | 450x338 | 763x574 |
| Extra large portrait | 338x450 | 574x763 |

watchOS dimensions:

| Apple Watch size | Size of a widget in the Smart Stack (pt) |
|---|---|
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 42mm | 176x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 46mm | 194x80.5 |
| 49mm (Ultra 3, 4) | 198x81.5 |
| 49mm (Ultra 1, 2) | 191x81.5 |

**Dev refs**
WidgetKit, WidgetRenderingMode (.fullColor, .accented, .vibrant), widgetAccentable(_:), ContainerRelativeShape, padding(_:_:), Font, Font.custom(_:size:), LevelOfDetail (.simplified, .default), WidgetMountingStyle (.elevated, .recessed), WidgetConfiguration.supportedMountingStyles(_:), WidgetTexture (.paper, .glass), RelevanceKit, ActivityKit, Making a configurable widget, Keeping a widget up to date, Displaying the right widget background, Optimizing your widget for accented rendering mode and Liquid Glass
