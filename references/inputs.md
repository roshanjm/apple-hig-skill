# Inputs — HIG digest

Apple's HIG **Inputs** section covers the physical and sensed ways people control an app or game and enter data: hardware buttons (Action button, Camera Control, Digital Crown), Apple Pencil and Scribble, eyes (visionOS), the focus system, game controllers and virtual touch controls, gestures on every platform, motion sensors, physical keyboards and shortcuts, Ultra Wideband nearby interactions, trackpads/mice and the iPadOS pointer, and the Siri Remote. Crawled from developer.apple.com on 2026-10-14. Full page renders live in `hig/inputs/<slug>.md`; this digest keeps every rule, every number and every table but drops examples, images and explanatory prose. Three source tables lost image-only columns in the crawl (tvOS focus-state names, modifier-key glyphs, macOS pointer pictures); they are reproduced as-is and flagged.

## Action button
Full page: hig/inputs/action-button.md · Platforms: ios,watchos
Hardware button on supported iPhone and Apple Watch (Ultra) models that runs an App Shortcut or a system function (e.g. flashlight) the person picks at setup or in Settings; on Apple Watch Ultra it also supports activity actions (workouts, dives). Pressing it runs the App Shortcut the same way Siri or Spotlight would.

**Rules**
- **Support the Action button with a set of your app's essential functions.** Don't offer an "open my app" shortcut — the system, app icon, widgets and complications already do that.
- **Write a short label for each action.** Title-style capitalization, starts with a verb, present tense, no articles or prepositions, maximum three words ("Start Race", not "Started Race" or "Start the Race"). Labels appear in Settings.
- **Prefer letting the system show people how to use the Action button.** Don't repeat the guidance Settings already gives or other system usage tips.

**Platform notes**
- iOS: **Let people use your actions without leaving their current context** — prefer Live Activities and custom snippets over launching the app (e.g. "Set Timer" prompts for a duration, then starts a Live Activity).
- watchOS: first press can drop a waypoint, start a dive or begin a workout; later presses can mark a segment or move to the next modality. **Consider offering a secondary function that supports or advances the primary action** — people press without looking, so it must flow logically; think hard before offering more than one secondary function. **Prefer subsequent presses for additional functionality, not to stop or conclude** — put Stop in your UI instead. **Pause the current function when the Action button and side button are pressed together**; the only exception is a dive app where pausing is dangerous.
- Not supported: iPadOS, macOS, tvOS, visionOS.

## Apple Pencil and Scribble
Full page: hig/inputs/apple-pencil-and-scribble.md · Platforms: ipados
Apple Pencil gives iPad apps pixel-level precision for drawing, handwriting and markup and also works as a pointer/UI tool; Scribble converts handwriting into text in any text field on-device. Apple Pencil Pro adds squeeze and barrel roll (guidance added 2024-05-07).

**Rules**
- **Support the behaviors people expect from a marking instrument** (e.g. writing in document margins).
- **Let people choose when to switch between Apple Pencil and finger input.** Every control must respond to Pencil; one that doesn't looks broken or out of battery. Scribble itself supports Pencil only.
- **Let people make a mark the moment Apple Pencil touches the screen** — no button, no special mode.
- **Respond to how people use the Pencil.** Use tilt (altitude), force (pressure), orientation (azimuth) and barrel roll to vary stroke thickness/intensity; map pressure to continuous properties such as opacity or brush size.
- **Provide visual feedback showing a direct connection with content.** Pencil must appear to manipulate what it touches immediately, never trigger disconnected actions elsewhere on screen.
- **Design a great left- and right-handed experience.** Avoid control positions either hand obscures; let people reposition controls if they might be hidden.
- Hover: **Use hover to help people predict what a touch will do** (preview mark size/colour); avoid continuously changing the preview with height — distracting and unclear.
- Hover: **Avoid using hover to initiate an action.** Hover is imprecise; never let proximity trigger a destructive action.
- Hover: **Prefer a preview value near the middle of a dynamic range** — max pressure occludes the area, min pressure is nearly invisible.
- Hover: **Consider using hover to support interactions close to where people are marking** (e.g. tool-size menu on squeeze or a keyboard modifier) so hands don't move away.
- Hover: **Prefer showing hover previews for Apple Pencil, not for a pointing device**; identical feedback for both can confuse.
- Double tap: **Respect people's double-tap settings when they make sense in your app.** Default toggles current tool/eraser; people can choose current/previous tool, show/hide colour picker, or nothing. If the systemwide options don't fit, double tap may change interaction mode instead (e.g. raise/lower in a mesh tool).
- Double tap: **Give people a way to specify custom double-tap behavior if necessary**; make the mode visible and discoverable, but off by default.
- Double tap: **Avoid using double tap for an action that modifies content.** Accidental double taps happen; prefer easily undoable actions and never anything destructive.
- Squeeze (Pencil Pro): works only while the paired iPad screen is on and the Pencil is not touching it; people may remap squeeze to an App Shortcut. **Treat squeeze as a single, quick gesture that performs a discrete — not continuous — action** and show the result promptly.
- Squeeze: **If squeeze reveals UI such as a contextual menu, display it close to Apple Pencil Pro's tip.**
- Squeeze: **Define squeeze actions that are nondestructive and easy to undo.**
- Barrel roll (Pencil Pro): **Use barrel roll only to modify marking behavior**, never for navigation or showing controls.
- Scribble: **Make text entry feel fluid and effortless.** Scribble works by default in all standard text components (text fields, text views, search fields, editable web fields) except password fields; custom fields must not require a tap or selection before writing.
- Scribble: **Make Scribble available everywhere people might want to enter text**, including areas without a text field (e.g. blank space below the last reminder).
- Scribble: **Avoid distracting people while they write** — no autocompletion text while writing; hide placeholder text the moment writing starts.
- Scribble: **Keep the text field stationary while people write**; if it must move or resize, delay until they pause.
- Scribble: **Prevent autoscrolling text while people write or edit** — it causes wrong selections.
- Scribble: **Give people enough space to write.** Enlarge the field before writing begins or when they pause; never resize mid-writing.
- Custom drawing: **Help people draw on top of existing content.** PencilKit canvas colours adapt to Dark Mode by default; disable that when drawing over a PDF or photo so markup stays sharp.
- Custom drawing: **Consider custom undo/redo buttons in a compact environment** (the tool picker shows them only in a regular environment); also support the standard 3-finger undo/redo gesture.

**Platform notes**
- Not supported: iOS, macOS, tvOS, visionOS, watchOS.

**Dev refs**
PencilKit, PaperKit, UIScribbleInteraction, UIIndirectScribbleInteraction, UIKit "Adopting hover support for Apple Pencil"

## Camera Control
Full page: hig/inputs/camera-control.md · Platforms: ios
Hardware control on iPhone 16 / iPhone 16 Pro models that opens your camera experience. A light press shows an overlay extending from the bezel; a light double-press lists available controls; sliding a finger adjusts the selected control's value.

Anatomy: a *slider* offers a range of values (e.g. contrast); a *picker* offers discrete options (e.g. grid on/off). System-provided standard controls you can optionally include: zoom factor and exposure bias.

**Rules**
- **Use SF Symbols to represent control functionality.** Custom symbols are not supported; symbols denote behaviour, not current state. See the Camera & Photos section of the SF Symbols app.
- **Keep names of controls short.** Labels follow Dynamic Type; long names obscure the viewfinder.
- **Include units or symbols with slider values** (EV, %, or a custom string) so people know what the slider controls.
- **Define prominent values for a slider control** — most-chosen values or evenly spaced ones (e.g. major zoom increments); the system lands on them more easily.
- **Make space for the overlay in the viewfinder.** The overlay and labels occupy the screen area adjacent to the Camera Control in both portrait and landscape; keep your UI out of those areas, maximise viewfinder height and width, and let the overlay appear over it.
- **Minimize distractions in the viewfinder.** Don't duplicate overlay sliders/toggles in your own UI while the overlay is showing.
- **Enable or disable controls depending on the camera mode** (e.g. disable video controls in photo mode). Controls can't be added or removed at runtime.
- **Consider how to arrange your controls.** Common controls toward the middle, lesser-used on either side; the system remembers the last control used in your app.
- **Allow people to use the Camera Control to launch your experience from anywhere** via a locked camera capture extension (lock screen, Home Screen, inside other apps).

**Platform notes**
- Not supported: iPadOS, macOS, watchOS, tvOS, visionOS.

**Dev refs**
AVCaptureControl, AVCaptureSlider.localizedValueFormat, AVCaptureSlider.prominentValues, LockedCameraCapture, AVFoundation "Enhancing your app experience with the Camera Control"

## Digital Crown
Full page: hig/inputs/digital-crown.md · Platforms: visionos,watchos
Rotating hardware input on Apple Vision Pro and Apple Watch. On Apple Vision Pro it is system-only (apps receive no direct Crown information): volume, immersion level in a portal/Environment/Full Space, recentering content, Accessibility settings, exiting to the Home View. On Apple Watch (watchOS 10+) it is the primary navigation input and apps can read its rotation.

**Rules**
- **Anchor your app's navigation to the Digital Crown** (watchOS 10+): list, tab and scroll views are vertical so the Crown moves between the app's important elements; always back Crown interactions with equivalent touch interactions.
- **Consider using the Digital Crown to inspect data where navigation isn't needed** (e.g. World Clock advances the time of day).
- **Provide visual feedback in response to Digital Crown interactions**; without it people assume turning does nothing. If you track turns directly, update the UI programmatically.
- **Update your interface to match the speed with which people turn the Digital Crown**; avoid update rates that make values hard to select.
- **Use the default haptic feedback when it makes sense.** Turn detents off if they don't match your animation; tables can switch from row-based to linear detents (useful when row heights differ a lot).
- Apps don't respond to Crown presses — watchOS reserves them (e.g. revealing the Home Screen).
- Most Apple Watch models give linear haptic detents per fixed rotation distance; some system controls (table views) give detents as items scroll on.

**Platform notes**
- Not supported: iOS, iPadOS, macOS, tvOS.

**Dev refs**
WKCrownDelegate (WatchKit)

## Eyes
Full page: hig/inputs/eyes.md · Platforms: visionos
In visionOS people look at a virtual object to target it; the system shows a *hover effect* on interactive elements to confirm the target before an indirect gesture (e.g. tap). Some components expand on look (tab bar reveals labels, button shows tooltip). Privacy: visionOS never tells your app where people are looking before they tap; system components report the tap. Focus effects (keyboard/game controller) are unrelated to hover.

**Rules**
- **Always give people multiple ways to interact with your app**; support the accessibility features people rely on.
- **Design for visual comfort.** Keep needed objects within the field of view; the system places the first window/volume in front of the person; a Full Space app can request head-pose data for placing 3D content; avoid requiring multiple quick eye adjustments across a large area or across depth levels.
- **Place content at a comfortable viewing distance** — at least one meter away for anything read or used over time; only very brief content may sit close.
- **Prefer using standard UI components**; they respond to looks consistently, custom cues are harder to learn.
- **Minimize visual distractions.** Movement, especially peripheral, pulls the eyes involuntarily; don't reveal content next to a button someone is looking at.
- **Provide enough space around each interactive item**: a margin of at least 16 points around each item's bounds, or centers at least 60 points apart.
- **Avoid a repeating pattern or texture that fills the field of view** (eyes lock onto elements at false depths); confine patterns to a smaller area.
- **Consider subtle visual cues to draw people to the item they most likely want** — near the centre of the field of view, gentle motion, higher contrast, colour or scale changes; noticeable, not flashy.
- **In general, give an interactive item a rounded shape.** Eyes drift to corners; the rounder the shape, the easier to target.
- **For a multi-element interactive component, provide an overall containing shape** (custom region) so visionOS highlights the whole thing whichever part is looked at.
- Custom hover effects run out-of-process: you define two states (with/without effect), the system swaps them when looked at, and your code never learns when or in what state — an effect can show a Favorites symbol but cannot perform the favoriting.
- **Prefer a custom hover effect to emphasize or enhance a special moment.** Too many, or using them where standard effects suffice, dilutes the design, distracts, and can cause visual discomfort.
- **Choose the right delay.** No delay (default): subtle or inviting effects, e.g. a knob appearing on a slider. Short delay: lets people look and act quickly, e.g. tab bar expansion. Long delay: additional information like a tooltip under a button.
- **Keep one or more of the element's primary views unchanged in both states** so the transition has a stable anchor; if everything moves, people lose track.
- **Thoroughly test custom hover effects** while wearing Apple Vision Pro.

**Platform notes**
- Not supported: iOS, iPadOS, macOS, tvOS, watchOS.

**Dev refs**
visionOS "Adopting best practices for privacy and user preferences"

## Focus and selection
Full page: hig/inputs/focus-and-selection.md · Platforms: ipados,macos,tvos,visionos
Focus lets people confirm the target of a remote, game controller or keyboard interaction before acting. Focusing often selects, except where auto-selection would cause a context shift (tvOS requires a separate select gesture). iPadOS/macOS show focus with a ring or highlight; tvOS uses the parallax effect.

**Rules**
- **Rely on system-provided focus effects.** Create custom focus effects only if absolutely necessary.
- **Avoid changing focus without people's interaction.** Exception: when a discrete directional device (keyboard, remote, controller) is in use and the focused item disappears, move focus to one of the few adjacent items; otherwise just hide the focus indicator when the focused object disappears.
- **Be consistent with the platform in how focus reaches items.** iPadOS/macOS: Full Keyboard Access handles controls, so support focus only for content elements (list items, text fields, search fields), not buttons/sliders/toggles. tvOS: every onscreen element must be focusable via directional gestures or arrow keys.
- **Indicate focus with platform-consistent appearance.** iPadOS/macOS focused list items: white text on an accent-colour highlight; unfocused: standard text on a gray highlight.
- **Use a focus ring for a text or search field, but a highlight in a list or collection**; a whole-row highlight is easier to read even though a ring works on cell-filling items like photos.

**Platform notes**
- iPadOS: iPadOS 15+ focus system covers text fields, text views, sidebars, collection views and custom views. Uses *focus groups* (sidebar, grid, list): Tab moves between groups; arrow keys move within a group. The *halo* focus effect (focus ring) is a customizable outline for custom views and opaque cell content; **customize the halo when necessary** to match rounded corners/Bézier shapes or reposition it when a badge or parent view occludes/clips it. The *highlighted* appearance (text in accent colour) indicates focus but is not a focus effect; it is automatic for cells with content configurations. **Ensure focus moves through custom views in ways that make sense** — Tab follows reading order leading→trailing, top→bottom; mark a vertical stack as one focus group to traverse it first. **Adjust an item's priority** so the group's primary item receives focus when the group does.
- tvOS: **In a full-screen experience, gestures act on the content, not on focus** (no focus is shown). **Avoid displaying a pointer**; use the focus model for menus/UI, and if a pointer is essential make it highly visible and integrated. **Design for up to five focus states**; focused items usually scale up, so supply larger assets and leave room so they don't crowd neighbours.
- visionOS: same focus system as iPadOS/tvOS for a connected keyboard or game controller; the eye-driven hover effect is not part of the focus system.
- Not supported: iOS, watchOS.

**Specs**
tvOS focus states (the State column is blank in the crawl — names were rendered as images; rows are in source order):

| State | Description |
|---|---|
|  | The viewer hasn't brought focus to the item. Unfocused items appear less prominent than focused items. |
|  | The viewer brings focus to the item. A focused item visually stands out from the other onscreen content through elevation to the foreground, illumination, and animation. |
|  | The viewer chooses the focused item. A focused item provides instant visual feedback when people choose it. For example, a button might briefly invert its colors and animate before it transitions to its selected appearance. |
|  | The viewer has chosen or activated the item in some way. For example, a heart-shaped button that people can use to favorite a photo might appear filled in the selected state and empty in the deselected state. |
|  | The viewer can't bring focus to the item or choose it. An unavailable item appears inactive. |

**Dev refs**
UICollectionView, NSTableView, UIFocusHaloEffect, UICollectionViewCell, UIFocusEnvironment.focusGroupIdentifier, UIFocusGroupPriority, UIKit "Focus-based navigation", UIKit "Adding user-focusable elements to a tvOS app", UIKit "About focus interactions for Apple TV", TVML Focus Attributes

## Game controls
Full page: hig/inputs/game-controls.md · Platforms: ios,ipados,macos,tvos,visionos
Games can take input from physical game controllers or the platform's default method (touch, remote, mouse/keyboard, eyes and hands). All platforms except watchOS support physical controllers, but not every player has one, and players like using the method they already know. Updated 2025-06-09 (touch controls, UI button mapping, spatial controllers).

**Rules**
- **Determine whether virtual controls on top of game content make sense.** They suit games with many actions or movement; otherwise prefer direct interaction with in-game objects (tap to select instead of a select button).
- **Place virtual buttons where they're easy to access.** Respect device boundaries and safe areas; don't overlap the Home indicator or Dynamic Island; frequent buttons near the thumb, outside the circular regions used for movement and camera; secondary controls like menus at the top.
- **Make sure controls are large enough**: frequently used controls minimum 44x44 pt; less important controls such as menus minimum 28x28 pt.
- **Always include visible and tactile press states** — a visual effect (e.g. glow) visible even under the finger, plus sound and haptics.
- **Use symbols that communicate the actions they perform** (e.g. a weapon for attack); avoid abstract shapes or controller names like A, X, R1.
- **Show and hide virtual controls to reflect gameplay**; hide unavailable/irrelevant controls, e.g. hide movement controls until the player touches the screen.
- **Combine functionality into a single control.** Avoid simultaneous or sequential multi-button presses; use double tap and touch-and-hold variants (hold for a powered-up attack); merge walk/sprint into one control.
- **Map movement and camera controls to predictable behavior**: movement on the left side, camera on the right; use the largest input areas possible; show the virtual thumbstick where the thumb lands rather than a fixed spot; pan the camera with direct touch, not a thumbstick.
- **Support the platform's default interaction method** as a fallback for game-controller input.
- **Tell people about game controller requirements.** tvOS and visionOS can require a controller (App Store shows "Game Controller Required"); still check for presence at launch and prompt gracefully.
- **Automatically detect whether a controller is paired** and read its profile instead of manual setup.
- **Customize onscreen content to match the connected game controller.** The framework names elements by placement; use the actual controller's colours/labels in your UI.
- **Map controller buttons to expected UI behavior** outside gameplay (table below).
- **Support multiple connected controllers**; match labels/glyphs to the active controller, per player in multiplayer; list buttons together when referring to several controllers.
- **Prefer symbols, not text, to refer to controller elements** (SF Symbols available for most buttons across brands).
- **Prioritize single-key commands** for keyboard play (I for Inventory, M for Map, Space for the main action).
- **Test key binding comfort using an Apple keyboard**; remap Control (^) bindings to Command (⌘), which sits next to the Space bar and is easy to reach from W, A, S, D.
- **Take the proximity of keys into account** — high-value commands near WASD; related actions on adjacent keys (number keys for inventory categories).
- **Let players customize key bindings.**

**Platform notes**
- visionOS: **Match spatial game controller behavior to hand input** (e.g. PlayStation VR2 Sense): look at an object and press the left/right trigger to interact indirectly; reach out and press the trigger to interact directly.
- No additional considerations for iOS, iPadOS, macOS, tvOS. Not supported: watchOS.

**Specs**
Controller buttons → UI behaviour (all Apple platforms, when not controlling gameplay):

| Button | Expected behavior for UI |
|---|---|
| A | Activates a control |
| B | Cancels an action or returns to previous screen |
| X | — |
| Y | — |
| Left shoulder | Navigates left to a different screen or section |
| Right shoulder | Navigates right to a different screen or section |
| Left trigger | — |
| Right trigger | — |
| Left/right thumbstick | Moves selection |
| Directional pad | Moves selection |
| Home/logo | Reserved for system controls |
| Menu | Opens game settings or pauses gameplay |

**Dev refs**
Touch Controller framework, Game Controller framework, GCControllerElement, GCRequiresControllerUserInteraction (Info.plist), GameController "Adding virtual controls to games that support game controllers in iOS"

## Gestures
Full page: hig/inputs/gestures.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
A gesture is a physical motion that directly affects an object — on a touchscreen, in the air (visionOS), or on a trackpad, mouse, remote or controller touch surface. Every platform supports tap, swipe and drag; exact motions vary but expected behaviour is the same everywhere.

**Rules**
- **Give people more than one way to interact with your app** (voice, keyboard, Switch Control); never assume a specific gesture is possible.
- **Respond to gestures in ways consistent with people's expectations.** Tap activates/selects everywhere; don't repurpose tap or swipe for an app-unique action, and don't invent a unique gesture for a standard action like activating a button or scrolling.
- **Handle gestures as responsively as possible**, with feedback that predicts the result and shows the extent/type of movement still required.
- **Indicate when a gesture isn't available** — e.g. a locked object that won't drag, or an unavailable button that looks identical to an available one, reads as a frozen app.
- **Add custom gestures only when necessary** — for frequent specialised tasks not covered by existing gestures (games, drawing). A custom gesture must be discoverable, straightforward to perform, distinct from other gestures, and not the only way to perform an important action.
- **Make custom gestures easy to learn**; teach them in-app, test in real use; if it's hard to describe with simple language and graphics it will be hard to learn.
- **Use shortcut gestures to supplement standard gestures, not replace them** — keep the Back button even if you add an edge-swipe shortcut.
- **Avoid conflicting with gestures that access system UI** (edge swipe in watchOS, hand roll in visionOS); games/immersive experiences may defer the system gesture in specific circumstances.
- iOS/iPadOS: **Consider allowing simultaneous recognition of multiple gestures if it enhances the experience** — mainly games (joystick plus fire buttons at once).
- visionOS: *indirect* gestures = look to target, then manipulate from a distance with the hands (comfortable at any distance, minimal movement); *direct* gestures = physically touch the object (must be within reach; tiring over time; best for infrequent use). Direct versions of all standard gestures exist.
- visionOS: **Support standard gestures everywhere you can** — tap is the first thing people try after looking at an object.
- visionOS: **Offer both indirect and direct interactions when possible.** Prefer indirect for UI and common components like buttons; reserve direct and custom gestures for close-up objects or specific game motions.
- visionOS: **Avoid requiring specific body movements or positions for input**; offer alternative inputs.
- visionOS custom gestures need the app running in a Full Space and the person's permission for hand data (ARKit). **Prioritize comfort** — test ergonomics continually; raised arms tire quickly; repeated similar movements stress muscles and joints.
- visionOS: **Carefully consider complex custom gestures involving multiple fingers or both hands**; offer a lower-movement alternative.
- visionOS: **Avoid custom gestures that require a specific hand** (cognitive load; excludes people with strong hand dominance or limb differences).
- visionOS 2+: looking at the palm reveals the Home indicator; turning the hand reveals the status bar with a tap to open Control Center. These are reserved systemwide (the visionOS 1 look-up behaviour remains as an accessibility setting). **Reserve the area around a person's hand for system overlays** — don't anchor content to hands or wrists; keep hand-anchored game content outside the immediate hand area.
- visionOS: **Consider deferring the system overlay behavior in an immersive app or game** running in a Full Space (require a tap before the Home indicator appears). Apps built for visionOS 1 defer by default.
- visionOS: **Use caution with custom gestures involving a rolling motion of the hand, wrist and forearm** — reserved for system overlays, which draw on top of your content without notifying you.
- watchOS 11+: double tap scrolls lists/scroll views and advances vertical tab views; you may designate a toggle or button as the *primary action* in a view, widget or Live Activity in the Smart Stack (double tap highlights then performs it); in notifications it triggers the first nondestructive action.
- watchOS: **Avoid setting a primary action in views with lists, scroll views, or vertical tabs** — it conflicts with default double-tap navigation.
- watchOS: **Choose the button people use most commonly as the primary action** in a nonscrolling view (e.g. play/pause in media controls).

**Platform notes**
- macOS: primarily keyboard and mouse; standard gestures work on Magic Trackpad, Magic Mouse and touch-surface game controllers.
- tvOS: standard gestures via a compatible remote, Siri Remote or touch-surface game controller (see Remotes).

**Specs**
Standard gestures (all platforms; touchscreen, visionOS indirect, or trackpad/mouse/remote/controller):

| Gesture | Supported in | Common action |
|---|---|---|
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Activate a control; select an item. |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal actions and controls; dismiss views; scroll. |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Move a UI element. |
| Touch (or pinch) and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Reveal additional controls or functionality. |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Zoom in; zoom out if already zoomed in; perform a primary action on Apple Watch Series 9 and Apple Watch Ultra 2. |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | Zoom a view; magnify content. |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate a selected item. |

Additional iOS/iPadOS gestures:

| Gesture | Common action |
|---|---|
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |
| Shake | Initiate undo; initiate redo. |

Standard direct gestures in visionOS:

| Direct gesture | Common use |
|---|---|
| Touch | Directly select or activate an object. |
| Touch and hold | Open a contextual menu. |
| Touch and drag | Move an object to a new location. |
| Double touch | Preview an object or file; select a word in an editing context. |
| Swipe | Reveal actions and controls; dismiss views; scroll. |
| With two hands, pinch and drag together or apart | Zoom in or out. |
| With two hands, pinch and drag in a circular motion | Rotate an object. |

**Dev refs**
SwiftUI Gestures, UITouch, persistentSystemOverlays(_:), handGestureShortcut(_:isEnabled:), HandGestureShortcut.primaryAction, visionOS "Setting up access to ARKit data"

## Gyroscope and accelerometer
Full page: hig/inputs/gyro-and-accelerometer.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
On-device motion sensors supply real-time movement data for apps and games on iOS, iPadOS and watchOS; tvOS apps can use gyroscope data from the Siri Remote. Access goes through Core Motion.

**Rules**
- **Use motion data only to offer a tangible benefit to people** (fitness feedback, gameplay); don't collect it just to have it.
- You **must provide copy explaining why you need motion data**; the system shows it in the first-time permission request where people grant or deny access.
- **Outside of active gameplay, avoid using accelerometers or gyroscopes for direct manipulation of your interface** — motion gestures are hard to repeat precisely, physically challenging for some people, and cost battery.

**Platform notes**
- No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

**Dev refs**
Core Motion, Core Motion "Getting processed device-motion data"

## Keyboards
Full page: hig/inputs/keyboards.md · Platforms: ios,ipados,macos,tvos,visionos
A physical keyboard connects to any device except Apple Watch; Mac users use one constantly, iPad users often. A *keyboard shortcut* = primary key + one or more modifiers (Control, Option, Shift, Command); a game's single-key shortcut is a *key binding* (see Game controls). Apple's standard shortcuts work the same across the system and most apps.

**Rules**
- **Support Full Keyboard Access when possible** (iOS, iPadOS, macOS, visionOS): keyboard-only navigation and activation of windows, menus, controls and system features. Test by enabling it in the Accessibility area of Settings.
- iPadOS: **avoid supporting keyboard navigation for controls** (buttons, segmented controls, switches). Support it for text fields, text views, sidebars and (via API) collection/custom views; let Full Keyboard Access activate controls, reach every component and perform gesture interactions like drag and drop.
- **Respect standard keyboard shortcuts.** For a unique frequent action, create a custom shortcut rather than repurposing a standard one. Games: people still expect e.g. Command-Q to quit, while being able to remap key bindings.
- **In general, don't repurpose standard keyboard shortcuts for custom actions.** Redefine one only when its action has no meaning in your app (e.g. no text editing → Command-I can become Get Info).
- **Define custom keyboard shortcuts for only the most frequently used app-specific commands**; too many make the app seem hard to learn.
- **Use modifier keys in ways that people expect**: Command-drag moves items as a group; Shift while drag-resizing constrains to the aspect ratio; holding an arrow key keeps moving the selection by the smallest app-defined unit until released.
- **List modifier keys in the correct order**: Control, Option, Shift, Command.
- **Avoid adding Shift to a shortcut that uses the upper character of a two-character key** — Help is Command-Question mark, not Shift-Command-Slash (Hide Status Bar is Command-Slash).
- **Let the system localize and mirror your keyboard shortcuts** for the connected keyboard and for right-to-left layouts.
- **Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command** (Shift-Command-Z must stay tied to undo/redo).
- Localisation tip: some layouts need modifiers to type characters (French: Option-5 = "{"). Command alone is usually safe; avoid an additional modifier with characters not on all keyboards; if you must use a non-Command modifier, prefer it only with alphabetic characters.

**Platform notes**
- visionOS: holding Command on a connected keyboard shows a shortcut interface organised like menu bar menus (File, Edit, View…) but with every category in one view, listing only available commands that have shortcuts. **Write descriptive shortcut titles** — the list is flat, so submenu titles can't supply context. **Recognize that people see a virtual keyboard overlay** (typing completion and other controls) whenever a physical keyboard is connected to your visionOS app.
- No additional considerations for iOS, iPadOS, macOS, tvOS. Not supported: watchOS.

**Specs**
Standard keyboard shortcuts (people expect each to perform the listed action):

| Primary key | Keyboard shortcut | Action |
|---|---|---|
| Space | Command-Space | Show or hide the Spotlight search field. |
|  | Shift-Command-Space | Varies. |
|  | Option-Command-Space | Show the Spotlight search results window. |
|  | Control-Command-Space | Show the Special Characters window. |
| Tab | Shift-Tab | Navigate through controls in a reverse direction. |
|  | Command-Tab | Move forward to the next most recently used app in a list of open apps. |
|  | Shift-Command-Tab | Move backward through a list of open apps (sorted by recent use). |
|  | Control-Tab | Move focus to the next group of controls in a dialog or the next table (when Tab moves to the next cell). |
|  | Control-Shift-Tab | Move focus to the previous group of controls. |
| Esc | Esc | Cancel the current action or process. |
| Esc | Option-Command-Esc | Open the Force Quit dialog. |
| Eject | Control-Command-Eject | Quit all apps (after changes have been saved to open documents) and restart the computer. |
|  | Control-Option-Command-Eject | Quit all apps (after changes have been saved to open documents) and shut the computer down. |
| F1 | Control-F1 | Toggle full keyboard access on or off. |
| F2 | Control-F2 | Move focus to the menu bar. |
| F3 | Control- F3 | Move focus to the Dock. |
| F4 | Control-F4 | Move focus to the active (or next) window. |
|  | Control-Shift-F4 | Move focus to the previously active window. |
| F5 | Control-F5 | Move focus to the toolbar. |
|  | Command-F5 | Turn VoiceOver on or off. |
| F6 | Control-F6 | Move focus to the first (or next) panel. |
|  | Control-Shift-F6 | Move focus to the previous panel. |
| F7 | Control-F7 | Temporarily override the current keyboard access mode in windows and dialogs. |
| F8 |  | Varies. |
| F9 |  | Varies. |
| F10 |  | Varies. |
| F11 |  | Show desktop. |
| F12 |  | Hide or display Dashboard. |
| Grave accent (`) | Command-Grave accent | Activate the next open window in the frontmost app. |
|  | Shift-Command-Grave accent | Activate the previous open window in the frontmost app. |
|  | Option-Command-Grave accent | Move focus to the window drawer. |
| Hyphen (-) | Command-Hyphen | Decrease the size of the selection. |
|  | Option-Command-Hyphen | Zoom out when screen zooming is on. |
| Left bracket ({) | Command-Left bracket | Left-align a selection. |
| Right bracket (}) | Command-Right bracket | Right-align a selection. |
| Pipe (\|) | Command-Pipe | Center-align a selection. |
| Colon (:) | Command-Colon | Display the Spelling window. |
| Semicolon (;) | Command-Semicolon | Find misspelled words in the document. |
| Comma (,) | Command-Comma | Open the app's settings window. |
|  | Control-Option-Command-Comma | Decrease screen contrast. |
| Period (.) | Command-Period | Cancel an operation. |
|  | Control-Option-Command-Period | Increase screen contrast. |
| Question mark (?) | Command-Question mark | Open the app's Help menu. |
| Forward slash (/) | Option-Command-Forward slash | Turn font smoothing on or off. |
| Equal sign (=) | Shift-Command-Equal sign | Increase the size of the selection. |
|  | Option-Command-Equal sign | Zoom in when screen zooming is on. |
| 3 | Shift-Command-3 | Capture the screen to a file. |
|  | Control-Shift-Command-3 | Capture the screen to the Clipboard. |
| 4 | Shift-Command-4 | Capture a selection to a file. |
|  | Control-Shift-Command-4 | Capture a selection to the Clipboard. |
| 8 | Option-Command-8 | Turn screen zooming on or off. |
|  | Control-Option-Command-8 | Invert the screen colors. |
| A | Command-A | Select every item in a document or window, or all characters in a text field. |
|  | Shift-Command-A | Deselect all selections or characters. |
| B | Command-B | Boldface the selected text or toggle boldfaced text on and off. |
| C | Command-C | Copy the selection to the Clipboard. |
|  | Shift-Command-C | Display the Colors window. |
|  | Option-Command-C | Copy the style of the selected text. |
|  | Control-Command-C | Copy the formatting settings of the selection and store on the Clipboard. |
| D | Option-Command-D | Show or hide the Dock. |
|  | Control-Command-D | Display the definition of the selected word in the Dictionary app. |
| E | Command-E | Use the selection for a find operation. |
| F | Command-F | Open a Find window. |
|  | Option-Command-F | Jump to the search field control. |
|  | Control-Command-F | Enter full screen. |
| G | Command-G | Find the next occurrence of the selection. |
|  | Shift-Command-G | Find the previous occurrence of the selection. |
| H | Command-H | Hide the windows of the currently running app. |
|  | Option-Command-H | Hide the windows of all other running apps. |
| I | Command-I | Italicize the selected text or toggle italic text on or off. |
|  | Command-I | Display an Info window. |
|  | Option-Command-I | Display an inspector window. |
| J | Command-J | Scroll to a selection. |
| M | Command-M | Minimize the active window to the Dock. |
|  | Option-Command-M | Minimize all windows of the active app to the Dock. |
| N | Command-N | Open a new document. |
| O | Command-O | Display a dialog for choosing a document to open. |
| P | Command-P | Display the Print dialog. |
|  | Shift-Command-P | Display the Page Setup dialog. |
| Q | Command-Q | Quit the app. |
|  | Shift-Command-Q | Log out the person currently logged in. |
|  | Option-Shift-Command-Q | Log out the person currently logged in without confirmation. |
| S | Command-S | Save a new document or save a version of a document. |
|  | Shift-Command-S | Duplicate the active document or initiate a Save As. |
| T | Command-T | Display the Fonts window. |
|  | Option-Command-T | Show or hide a toolbar. |
| U | Command-U | Underline the selected text or turn underlining on or off. |
| V | Command-V | Paste the Clipboard contents at the insertion point. |
|  | Shift-Command-V | Paste as (Paste as Quotation, for example). |
|  | Option-Command-V | Apply the style of one object to the selection. |
|  | Option-Shift-Command-V | Paste the Clipboard contents at the insertion point and apply the style of the surrounding text to the inserted object. |
|  | Control-Command-V | Apply formatting settings to the selection. |
| W | Command-W | Close the active window. |
|  | Shift-Command-W | Close a file and its associated windows. |
|  | Option-Command-W | Close all windows in the app. |
| X | Command-X | Remove the selection and store on the Clipboard. |
| Z | Command-Z | Undo the previous operation. |
|  | Shift-Command-Z | Redo (when Undo and Redo are separate commands rather than toggled using Command-Z). |
| Right arrow | Command-Right arrow | Change the keyboard layout to current layout of Roman script. |
|  | Shift-Command-Right arrow | Extend selection to the next semantic unit, typically the end of the current line. |
|  | Shift-Right arrow | Extend selection one character to the right. |
|  | Option-Shift-Right arrow | Extend selection to the end of the current word, then to the end of the next word. |
|  | Control-Right arrow | Move focus to another value or cell within a view, such as a table. |
| Left arrow | Command-Left arrow | Change the keyboard layout to current layout of system script. |
|  | Shift-Command-Left arrow | Extend selection to the previous semantic unit, typically the beginning of the current line. |
|  | Shift-Left arrow | Extend selection one character to the left. |
|  | Option-Shift-Left arrow | Extend selection to the beginning of the current word, then to the beginning of the previous word. |
|  | Control-Left arrow | Move focus to another value or cell within a view, such as a table. |
| Up arrow | Shift-Command-Up arrow | Extend selection upward in the next semantic unit, typically the beginning of the document. |
|  | Shift-Up arrow | Extend selection to the line above, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Up arrow | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. |
|  | Control-Up arrow | Move focus to another value or cell within a view, such as a table. |
| Down arrow | Shift-Command-Down arrow | Extend selection downward in the next semantic unit, typically the end of the document. |
|  | Shift-Down arrow | Extend selection to the line below, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Down arrow | Extend selection to the end of the current paragraph, then to the end of the next paragraph (include the paragraph terminator, such as Return, in cut, copy, and paste operations). |
|  | Control-Down arrow | Move focus to another value or cell within a view, such as a table. |

Shortcuts for localized systems, keyboards, layouts and input methods (not tied to menu commands):

| Keyboard shortcut | Action |
|---|---|
| Control-Space | Toggle between the current and last input source. |
| Control-Option-Space | Switch to the next input source in the list. |
| [Modifier key]-Command-Space | Varies. |
| Command-Right arrow | Change keyboard layout to current layout of Roman script. |
| Command-Left arrow | Change keyboard layout to current layout of system script. |

Modifier keys (the Symbol column is blank in the crawl — glyphs were images):

| Modifier key | Symbol | Recommended usage |
|---|---|---|
| Command |  | Prefer the Command key as the main modifier key in a custom keyboard shortcut. |
| Shift |  | Prefer the Shift key as a secondary modifier that complements a related shortcut. |
| Option |  | Use the Option modifier sparingly for less-common commands or power features. |
| Control |  | Avoid using the Control key as a modifier. The system uses Control in many systemwide features and shortcuts, like moving focus or capturing screenshots. |

**Dev refs**
KeyboardShortcut (SwiftUI), SwiftUI Input events, UIKeyCommand.discoverabilityTitle, NSApplication.isFullKeyboardAccessEnabled, UIKit "Handling key presses made on a physical keyboard", UIKit "Focus-based navigation", AppKit "Mouse, Keyboard, and Trackpad"

## Nearby interactions
Full page: hig/inputs/nearby-interactions.md · Platforms: ios,ipados,watchos
Experiences that react to the presence, distance and direction of nearby people and objects (e.g. handing audio from iPhone to HomePod mini by bringing them together). Requires Ultra Wideband hardware and the Nearby Interaction framework; people grant permission per app, and sessions use random device identifiers that last only for the session.

**Rules**
- **Consider a task from the perspective of the physical world** to find the physical action that makes it feel natural (bring devices together to transfer a song).
- **Use distance, direction, and context to inform an interaction** — e.g. the share sheet combining frequent/recent contacts with the closest U1 device the person is facing.
- **Consider how changes in physical distance can guide a nearby interaction**; sharpen feedback as people get closer (AirTag: directional arrow → pulsing circle).
- **Provide continuous feedback** that responds to people's movements without interruption (Find My direction/proximity updates).
- **Consider using multiple feedback types** — visual while people look at the screen; audible and haptic while they interact with the environment; transition fluidly between them.
- **Avoid using a nearby interaction as the only way to perform a task**; always provide an alternative.
- **Encourage people to hold the device in portrait orientation**; landscape reduces accuracy and availability of distance/direction. Prefer implicit visual cues over explicit "hold in portrait" instructions.
- **Design for the device's directional field of view** (similar to the Ultra Wide camera on iPhone 11 and later); a peer outside it may report distance but not direction.
- **Help people understand that intervening objects degrade the experience** (people, animals, large objects between devices); add advice to onboarding or tutorials.

**Platform notes**
- iOS: APIs provide a peer device's distance and direction.
- watchOS: APIs provide distance only; all participating watchOS apps must be in the foreground.
- No additional considerations for iPadOS. Not supported: macOS, tvOS, visionOS.

**Dev refs**
Nearby Interaction framework

## Pointing devices
Full page: hig/inputs/pointing-devices.md · Platforms: ios,ipados,macos,visionos
Trackpads and mice offer precision; on Mac they pair with the keyboard as the primary input, on iPad and Apple Vision Pro they add to touch, eyes and gestures without replacing them. Covers iPadOS pointer effects, magnetism, accessories, macOS gestures and pointer styles, and visionOS pointer behaviour.

**Rules**
- **Be consistent when responding to mouse and trackpad gestures**; "Swipe between pages" must work the same across document pages, web pages and images.
- **Avoid redefining systemwide trackpad gestures** (reveal Dock, Mission Control) even in games; people can also customise those gestures.
- **Provide a consistent experience whether people use gestures, eyes, a pointing device, or a keyboard**; people move fluidly between inputs.
- **Let people use the pointer to reveal and hide controls that automatically minimize or fade out** (hover over the minimised Safari toolbar; move the pointer to show full-screen video controls).
- **Provide a consistent experience for modifier keys held while interacting** — Option-drag must duplicate whether the drag is by touch or pointer.
- iPadOS: **Allow multiple selection in custom views when necessary.** iPadOS 15+ band selection (click-drag rectangle) works in standard nonlist collection views by default; implement it yourself in custom views.
- iPadOS: **Distinguish between pointer and finger input only if it provides value** (a scrubber can accept a precise click-to-seek with the pointer while still supporting drag by either).
- iPadOS content effects: the pointer is a circle by default and becomes an I-beam over text. *Highlight* turns the pointer into a translucent rounded rect behind a control with gentle parallax (default for bar buttons, tab bars, segmented controls, edit menus). *Lift* fades the pointer out and scales the element up with a shadow and specular highlight (default for app icons and Control Center buttons). *Hover* applies custom scale, tint or shadow without changing the pointer shape.
- iPadOS: **When possible, support the system-provided content effects**: highlight for a small element with a transparent background; lift for a small element with an opaque background; hover for large elements (customise scale, tint, shadow).
- iPadOS: **Prefer the system-provided pointer appearances for standard buttons and text-entry areas.**
- iPadOS: **Add padding around interactive elements to create comfortable hit regions** — about 12 points around elements with a bezel; about 24 points around the visible edges of elements without a bezel. Too small feels fiddly; too large makes the pointer hard to pull away.
- iPadOS: **Create contiguous hit regions for custom bar buttons** so the pointer doesn't flicker back to its default shape between them.
- iPadOS: **Specify the corner radius of a nonstandard element that receives the lift effect** (e.g. a circle) so the pointer can morph into its shape.
- iPadOS accessories (small indicators such as resize arrows that combine with any pointer): **Use clear, simple images for custom accessories**; **consider the accessory transition to signal a state change** (e.g. `plus` → `circle.slash` when add becomes unavailable).
- iPadOS magnetism: the pointer starts morphing when it enters an element's hit region (which extends past its visible bounds) and is pulled to the centre of an element in a flick's trajectory. Applied by default to lift and highlight elements and to text-entry areas (prevents line-skipping while selecting), not to hover elements.
- iPadOS: **Prefer system-provided pointer effects for custom elements that behave like standard elements** (custom toolbar buttons without highlight look broken).
- iPadOS: **Use pointer effects in consistent ways throughout your app** (same pointer experience in every drawing area).
- iPadOS: **Avoid creating gratuitous pointer and content effects**; decorative changes distract and irritate.
- iPadOS: **Keep custom pointer shapes simple**; the shape should signal the available action without drawing attention.
- iPadOS: **Consider custom annotations that provide useful information** (X/Y values over a graph; Keynote shows width/height while resizing).
- iPadOS: **Avoid displaying instructional text with a pointer**; it makes the app seem complicated.
- iPadOS: **Consider the interplay of shadow, scale, and element spacing in custom hover effects.** Reserve scaling for elements with room to grow (not table rows); for tightly packed elements use tint without scale or shadow; never use shadow without scale.

**Platform notes**
- macOS: wide range of customisable mouse/trackpad interactions; people can turn clicks/gestures on or off, assign mouse/trackpad regions for secondary click, and choose finger combinations. See gesture and pointer tables below.
- visionOS: with an external pointing device attached, looking at an element and then moving the pointer brings focus to the element under the pointer (no app work needed); the pointer's context follows the eyes between windows; while people gesture on a trackpad/mouse the pointer hides, reappearing where they are looking when moved again.
- No additional considerations for iOS. Not supported: tvOS, watchOS.

**Specs**
macOS clicks and gestures:

| Click or gesture | Expected behavior | Mouse | Trackpad |
|---|---|---|---|
| Primary click | Select or activate an item, such as a file or button. | ● | ● |
| Secondary click | Reveal contextual menus. | ● | ● |
| Scrolling | Move content up, down, left, or right within a view. | ● | ● |
| Smart zoom | Zoom in or out on content, such as a web page or PDF. | ● | ● |
| Swipe between pages | Navigate forward or backward between individually displayed pages. | ● | ● |
| Swipe between full-screen apps | Navigate forward or backward between full-screen apps and spaces. | ● | ● |
| Mission Control (double-tap the mouse with two fingers or swipe up on the trackpad with three or four fingers) | Activate Mission Control. | ● | ● |
| Lookup and data detectors (force click with one finger or tap with three fingers) | Display a lookup window above selected content. |  | ● |
| Tap to click | Perform the primary click action using a tap rather than a click. |  | ● |
| Force click | Click then press firmly to display a Quick Look window or lookup window above selected content. Apply a variable amount of pressure to affect pressure-sensitive controls, such as variable speed media controls. |  | ● |
| Zoom in or out (pinch with two fingers) | Zoom in or out. |  | ● |
| Rotate (move two fingers in a circular motion) | Rotate content, such as an image. |  | ● |
| Notification Center (swipe from the edge of the trackpad) | Display Notification Center. |  | ● |
| App Exposé (swipe down with three or four fingers) | Display the current app's windows in Exposé. |  | ● |
| Launchpad (pinch with thumb and three fingers) | Display the Launchpad. |  | ● |
| Show Desktop (spread with thumb and three fingers) | Slide all windows out of the way to reveal the desktop. |  | ● |

macOS standard pointers (image column dropped — it is blank in the crawl):

| Name | Meaning | AppKit API (NSCursor) |
|---|---|---|
| Arrow | Standard pointer for selecting and interacting with content and interface elements. | arrow |
| Closed hand | Dragging to reposition the display of content within a view—for example, dragging a map around in Maps. | closedHand |
| Contextual menu | A contextual menu is available for the content below the pointer. This pointer is generally shown only when the Control key is pressed. | contextualMenu |
| Crosshair | Precise rectangular selection is possible, such as when viewing an image in Preview. | crosshair |
| Disappearing item | A dragged item will disappear when dropped. If the item references an original item, the original is unaffected. For example, when dragging a mailbox out of the favorites bar in Mail, the original mailbox isn't removed. | disappearingItem |
| Drag copy | Duplicates a dragged—not moved—item when dropped into the destination. Appears when pressing the Option key during a drag operation. | dragCopy |
| Drag link | During a drag and drop operation, creates an alias of the selected file when dropped. The alias points to the original file, which remains unmoved. Appears when pressing the Option and Command keys during a drag operation. | dragLink |
| Horizontal I beam | Selection and insertion of text is possible in a horizontal layout, such as a TextEdit or Pages document. | iBeam |
| Open hand | Dragging to reposition content within a view is possible. | openHand |
| Operation not allowed | A dragged item can't be dropped in the current location. | operationNotAllowed |
| Pointing hand | The content beneath the pointer is a URL link to a webpage, document, or other item. | pointingHand |
| Resize down | Resize or move a window, view, or element downward. | resizeDown |
| Resize left | Resize or move a window, view, or element to the left. | resizeLeft |
| Resize left/right | Resize or move a window, view, or element to the left or right. | resizeLeftRight |
| Resize right | Resize or move a window, view, or element to the right. | resizeRight |
| Resize up | Resize or move a window, view, or element upward. | resizeUp |
| Resize up/down | Resize or move a window, view, or element upward or downward. | resizeUpDown |
| Vertical I beam | Selection and insertion of text is possible in a vertical layout. | iBeamCursorForVerticalLayout |

**Dev refs**
UIBandSelectionInteraction, UIPointerAccessory, UIPointerShape.roundedRect(_:radius:), UIKit "Pointer interactions", NSCursor (arrow, closedHand, contextualMenu, crosshair, disappearingItem, dragCopy, dragLink, iBeam, openHand, operationNotAllowed, pointingHand, resizeDown, resizeLeft, resizeLeftRight, resizeRight, resizeUp, resizeUpDown, iBeamCursorForVerticalLayout), SwiftUI Input events, AppKit "Mouse, Keyboard, and Trackpad"

## Remotes
Full page: hig/inputs/remotes.md · Platforms: tvos
The Siri Remote is the primary Apple TV input: dedicated buttons plus a clickpad/touch surface for swipe and press, used to navigate apps, browse content, play/pause media and select items. Compatible third-party remotes may add EPG/channel buttons.

**Rules**
- **Prefer using standard gestures to perform standard actions**; outside active gameplay, redefining remote behaviour confuses people.
- **Be consistent with the tvOS focus experience** — always move focus in the same direction as the gesture.
- **Provide clear feedback that shows people what happens when they make gestures** (e.g. a resting thumb hints where to swipe down for an info area).
- **Define new gestures only when it makes sense** (fine within gameplay; elsewhere people expect standard gestures).
- **Differentiate between press and tap, and avoid responding to an inadvertent tap.** Press is intentional (choose a button, confirm, act in a game); taps suit navigation or extra info but happen accidentally when resting a thumb or handing the remote over — usually ignore taps during live video playback.
- **Consider using the position of a tap** (up/down/left/right on the touch surface) for navigation or gameplay only when intuitive and discoverable.
- **In almost all cases, open the parent of the current screen when people press Back.** Top level → Apple TV Home Screen; within the app the parent is defined by hierarchy, not necessarily the previous screen. In active gameplay, Back opens an in-game pause menu; Back while the pause menu is open closes it and resumes. Press-and-hold Back always goes to the Home Screen.
- **Respond correctly to the Play/Pause button during media playback** — play, pause or resume.
- Swipe scrolls with momentum (fast then slowing by swipe strength); swiping up/down on the remote's edge speeds through items. Press activates or selects; pressing before swiping enters scrubbing mode.
- **If your live-viewing app provides an EPG, respond to a remote's EPG-browsing buttons in ways people expect**: "guide"/"browse" opens the EPG; "page up"/"page down" navigate within it (don't repurpose them while browsing); tapping the upper/lower area of the touch surface also browses. Without an EPG, the system routes these presses to the default guide app.
- **While your content plays, respond to "page up"/"page down" by changing the channel.**

**Platform notes**
- Not supported: iOS, iPadOS, macOS, visionOS, watchOS.

**Specs**
Siri Remote buttons and areas:

| Button or area | Expected behavior in an app | Expected behavior in a game |
|---|---|---|
| Touch surface (swipe) | Navigates. Changes focus. | Performs directional pad behavior. |
| Touch surface (press) | Activates a control or an item. Navigates deeper. | Performs primary button behavior. |
| Back | Returns to previous screen. Exits to Apple TV Home Screen. | Pauses/resumes gameplay. Returns to previous screen, exits to main game menu, or exits to Apple TV Home Screen. |
| Play/Pause | Activates media playback. Pauses/resumes media playback. | Performs secondary button behavior. Skips intro video. |

**Dev refs**
TVServices "Providing Channel Navigation"
