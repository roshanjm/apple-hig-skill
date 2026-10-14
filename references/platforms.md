# Platforms & design principles — HIG digest

This file condenses the HIG **Getting started** section (crawled 2026-10-14, Liquid Glass era): the eight design principles, one "Designing for" page per platform (iOS, iPadOS, macOS, tvOS, visionOS, watchOS, iPhone Duo) and the cross-platform games page. Full pages live in `hig/getting-started/` (collection index: `hig/getting-started.md`; HIG root: `hig/human-interface-guidelines.md`). This digest keeps every rule and every number from those pages but drops examples, video blurbs, and connective prose. Link targets are given as paths inside `hig/` so you can open the full page a rule points to.

## Design principles
Full page: hig/getting-started/design-principles.md (reintroduced June 8, 2026)

There is no one right way to apply these principles; they are tools for weighing competing priorities. Guidance throughout the HIG is built on them.

**Purpose.** Make something meaningful — start with intention; identify what matters most to the people you design for and make those things great.
- **Create value.** At every stage of development, ask what the product is for and whether the design serves that purpose.
- **Keep focused.** Prioritize the most important features by aligning with how people want to use the app; make those features truly great.
- **Find new ways to solve the problem.** Investigate existing solutions and avoid re-creating them; define what sets the product apart and reflect it in the design.

**Agency.** Let people do things their own way — give freedom to act, keep people informed, make mistakes easy to recover from.
- **Stay out of the way.** Get people directly to the task or content; the best designs are unobtrusive and present only when needed.
- **Give people the freedom to explore.** Don't lock people into flows or modes; when a guided flow is necessary, make it easy to skip or escape.
- **Help people recover from mistakes.** Make actions reversible and previous states reachable; recovering from the unexpected must not cost time or work.

**Responsibility.** Act in people's best interest — earn trust through safety, privacy, and transparency about what the product does and why.
- **Be fully transparent about what your product does and why.** Make intentions clear from the first interaction; give a clear rationale when asking permission; state what data you collect and how you use it.
- **Keep people's information safe.** Collect only what the product needs to function; anticipate misuse and harm and put protections in place.

**Familiarity.** Build on what people know — ground the experience in established physical and digital patterns and apply them consistently.
- **Use concepts that people know.** Draw on knowledge of the real world and of other software.
- **Keep visuals and interactions consistent.** Once a behavior or appearance is established for an element, apply it throughout; consistency speeds learning and builds confidence.
- **Provide clear feedback.** Show when controls are available, indicate when content changes, use system patterns for alerts and choices.

**Flexibility.** Adapt to diverse contexts and needs — support as many devices, interaction types, and perspectives as possible.
- **Design for everyone.** Treat accessibility as a priority from the start; design inclusively for the broadest audience.
- **Preserve a person's context.** As the design adapts across platforms and configurations, keep content and controls in consistent, predictable positions and use natural animations to ease transitions.
- **Consider a variety of input methods.** Design for voice, touch, keyboard, and more so people can use the product the way that works for them.
- **Approach every platform with intention.** Give each supported platform the same level of care; the software must feel polished and at home wherever it runs.

**Simplicity.** Be clear and direct — remove the unnecessary; every element earns its place.
- **Include just what's necessary.** Simplicity is not minimalism: keep the important things close and let the others fall away.
- **Be concise.** Choose exactly the words needed to convey a concept or label a control.
- **Establish hierarchy.** Prioritize recognizable controls and a consistent structure so people know where they are and what comes next.

**Craft.** Care about every detail — the design reflects how much you care; do the work well.
- **Quality sets the tone.** Be deliberate with each decision; strive for stunning visuals, smooth animations, precise wording, and thoughtful audio.
- **Experiment and iterate.** Prototype early, discard what doesn't work, set a high bar per feature, and test in real-world settings for durability, reliability, and performance.
- **Maintain your craft.** Shipping isn't the finish line; keep the interface current with the latest platform capabilities and design patterns.

**Delight.** Make it human — people remember how a product makes them feel; deliver the right emotions in a satisfying, enriching way.
- **Identify the emotion you want to inspire.** Know the feeling to evoke (energize, calm, thrill) and let it shape the design.
- **Create defining moments.** Treat each interaction, from a button press to an error message, as a chance to add character.
- **Don't mistake delight for decoration.** Never let pursuit of delight for its own sake obstruct the core task; balance practical touches against whimsy.
- **Consider the whole.** Delight is the sum of intent, focus, and care across the entire experience: freedom to act, safety to explore, familiar metaphors, smooth transitions between contexts.

## Designing for iOS
Full page: hig/getting-started/designing-for-ios.md

iPhone is used on the go, in one or both hands, for sessions that range from a minute or two to an hour or more. Design for a medium-size, high-resolution display held close, with frequent switching among open apps.

**Rules**
- **Display.** Medium-size, high-resolution.
- **Ergonomics.** Held in one or both hands; switches between landscape and portrait as needed; viewing distance tends to be no more than a foot or two.
- **Inputs.** Multi-Touch gestures, virtual keyboards, and voice control; people also expect apps to use personal data and gyroscope/accelerometer input, and may want spatial (nearby) interactions.
- **App interactions.** Sessions of a minute or two (checking updates, tracking data, messaging) or an hour or more (browsing, games, media); multiple apps open at once with frequent switching.
- **System features.** Integrate with Widgets, Home Screen quick actions, Spotlight, Shortcuts, and Activity views.

**Best practices / links**
- Limit the number of onscreen controls so people concentrate on primary tasks and content; make secondary details and actions discoverable with minimal interaction.
- Adapt seamlessly to appearance changes (device orientation, Dark Mode, Dynamic Type) so people choose the configurations that work for them.
- Support interactions that match how people hold the device: controls in the middle or bottom of the display are easier to reach, so let people swipe to navigate back or to initiate actions in a list row.
- With permission, integrate platform capabilities so people don't re-enter data: accept payments, use biometric authentication, use device location.
- Gestures (hig/inputs/gestures.md) · Virtual keyboards (hig/components/virtual-keyboards.md) · Siri / voice / Shortcuts (hig/technologies/siri.md) · Privacy (hig/foundations/privacy.md) · Gyro and accelerometer (hig/inputs/gyro-and-accelerometer.md) · Spatial interactions (hig/inputs/nearby-interactions.md — page links the `spatial-interactions` slug) · Widgets (hig/components/widgets.md) · Home Screen quick actions (hig/components/home-screen-quick-actions.md) · Spotlight / Searching (hig/patterns/searching.md) · Activity views (hig/components/activity-views.md)
- Videos cited: Meet Liquid Glass (WWDC25 219), Get to know the new design system (WWDC25 356).

## Designing for iPadOS
Full page: hig/getting-started/designing-for-ipados.md

iPad pairs a large display with mobility: it is held, set on a surface, or placed on a stand, and driven by touch, keyboard, pointer, and Apple Pencil, often combined. People run multiple apps onscreen at once.

**Rules**
- **Display.** Large, high-resolution.
- **Ergonomics.** Often held, but also set on a surface or stand; positioning changes viewing distance, though people are typically within about 3 feet.
- **Inputs.** Multi-Touch gestures, virtual keyboards, an attached keyboard or pointing device, Apple Pencil, or voice; people often combine multiple input modes.
- **App interactions.** A few quick actions or hours immersed in games, media, content creation, or productivity; multiple apps open, more than one onscreen at once, inter-app capabilities such as drag and drop.
- **System features.** Integrate with Multitasking, Widgets, and Drag and drop.

**Best practices / links**
- Use the large display to elevate content: minimize modal interfaces and full-screen transitions; put onscreen controls where they are easy to reach but not in the way.
- Use viewing distance and input mode to determine the size and density of onscreen content.
- Let people use Multi-Touch gestures, a physical keyboard or trackpad, or Apple Pencil; consider unique interactions that combine input modes.
- Adapt seamlessly to device orientation, multitasking modes, Dark Mode, and Dynamic Type, and transition effortlessly to running in macOS.
- Gestures (hig/inputs/gestures.md) · Virtual keyboards (hig/components/virtual-keyboards.md) · Keyboards (hig/inputs/keyboards.md) · Pointing devices (hig/inputs/pointing-devices.md) · Apple Pencil and Scribble (hig/inputs/apple-pencil-and-scribble.md) · Siri (hig/technologies/siri.md) · Multitasking (hig/patterns/multitasking.md) · Widgets (hig/components/widgets.md) · Drag and drop (hig/patterns/drag-and-drop.md)
- Videos cited: Elevate the design of your iPad app (WWDC25 208 — resizable app windows, window controls, menu bar, new pointer), Meet Liquid Glass (WWDC25 219), Get to know the new design system (WWDC25 356).

## Designing for macOS
Full page: hig/getting-started/designing-for-macos.md

Mac is a stationary, spacious, multi-window environment for in-depth work: large (and multiple) displays, precise keyboard and pointer input, several apps open at once, sessions from minutes to hours.

**Rules**
- **Display.** Typically large, high-resolution; people extend their workspace with additional displays, including their iPad.
- **Ergonomics.** Used while stationary, often on a desk or table; typical viewing distance about 1 to 3 feet.
- **Inputs.** Any combination of physical keyboards, pointing devices, game controls, and Siri.
- **App interactions.** A few minutes of quick tasks to several hours of deep concentration; multiple apps open; people expect smooth transitions between active and inactive states when switching apps.
- **System features.** Integrate with the menu bar, file management, full-screen mode, and Dock menus.

**Best practices / links**
- Use large displays to present more content in fewer nested levels and with less modality, while keeping a comfortable information density that doesn't make people strain.
- Let people resize, hide, show, and move windows; support full-screen mode as a distraction-free context.
- Use the menu bar to give access to all the commands the app offers.
- Support high-precision input for pixel-perfect selections and edits.
- Handle keyboard shortcuts to accelerate actions and support keyboard-only work styles.
- Support personalization: customizable toolbars, windows configured to show the views people use most, user-chosen colors and fonts.
- Keyboards (hig/inputs/keyboards.md) · Pointing devices (hig/inputs/pointing-devices.md) · Game controls (hig/inputs/game-controls.md) · Siri (hig/technologies/siri.md) · The menu bar (hig/components/the-menu-bar.md) · File management (hig/patterns/file-management.md) · Going full screen (hig/patterns/going-full-screen.md) · Dock menus (hig/components/dock-menus.md)
- Videos cited: Meet Liquid Glass (WWDC25 219), Get to know the new design system (WWDC25 356), Build an AppKit app with the new design (WWDC25 310).

## Designing for tvOS
Full page: hig/getting-started/designing-for-tvos.md

Apple TV is viewed from across the room on a very large display and driven by remote, controller, or voice through the focus system. Experiences are cinematic, immersive, and often shared by several people.

**Rules**
- **Display.** Very large, high-resolution.
- **Ergonomics.** People stay many feet from a stationary TV — often 8 feet or more — and sometimes keep interacting while moving around the room.
- **Inputs.** A remote, a game controller, voice, and apps running on people's other devices.
- **App interactions.** Deep immersion in a single experience, often for hours; picture-in-picture to follow a second app or video at the same time.
- **System features.** Integrate with the TV app, SharePlay, Top Shelf, and TV provider accounts.

**Best practices / links**
- Support powerful interactions through the fluid, familiar gestures of the Siri Remote.
- Embrace the tvOS focus system: let it highlight and expand onscreen items as people move among them so they always know what to do and where they are.
- Deliver edge-to-edge artwork, subtle fluid animation, and engaging audio; keep everything clear and legible from across the room.
- Support multiple users: make sign-in easy and infrequent, handle shared sign-in, and switch profiles automatically when the current viewer changes.
- Remotes (hig/inputs/remotes.md) · Game controls (hig/inputs/game-controls.md) · Siri (hig/technologies/siri.md) · Integrating with the TV app — Playing video (hig/patterns/playing-video.md) · SharePlay (hig/technologies/shareplay.md) · Top Shelf (hig/components/top-shelf.md) · TV provider accounts — Managing accounts (hig/patterns/managing-accounts.md)
- Video cited: Build SwiftUI apps for tvOS (WWDC20 10042). Change log: Sept 14, 2022 — refined multiuser best practices.

## Designing for visionOS
Full page: hig/getting-started/designing-for-visionos.md

Apple Vision Pro places apps in an infinite 3D space that people control with their eyes and hands while remaining connected to their surroundings through passthrough. Visual comfort is paramount because people see everything, real and virtual, through the device's cameras.

**Rules**
- **Space.** A limitless canvas for windows, volumes, and 3D objects; people can enter deeply immersive experiences that transport them elsewhere.
- **Immersion.** Apps launch by default in the *Shared Space* (multiple apps side by side; people open, close, and relocate windows). People can move an app to a *Full Space* where it is the only app running, with 3D content blended into the surroundings, a portal to another place, or a different world.
- **Passthrough.** Live video from external cameras lets people see their surroundings while interacting with virtual content; people turn the Digital Crown to control how much passthrough they see.
- **Spatial Audio.** The device models the acoustics of the surroundings so audio sounds natural; with permission to access surroundings data, an app can fine-tune Spatial Audio.
- **Eyes and hands.** Most actions: look at a virtual object, then make an *indirect* gesture (e.g. tap) to activate it. *Direct* gestures (touching an object with a finger) are also supported.
- **Ergonomics.** People rely entirely on the cameras for everything they see, so maintain visual comfort. The system places content relative to the wearer's head regardless of height or whether they sit, stand, or lie down; bring content to people so they can stay at rest.
- **Accessibility.** Supports VoiceOver, Switch Control, Dwell Control, Guided Access, Head Pointer, and more; system UI components build in accessibility by default.
- **Safety (Important).** Consider the device's unique characteristics and the user's safety (see Apple Vision Pro User Guide). Not for use while operating a vehicle or heavy machinery; not designed for moving around unsafe environments (balconies, streets, stairs, other hazards); designed to be fit and used only by individuals 13 years of age or older.

**Best practices / links**
- **Embrace the unique features of Apple Vision Pro.** Use space, Spatial Audio, and immersion; integrate passthrough and spatial input from eyes and hands in ways that feel at home.
- **Consider different types of immersion for the app's most distinctive moments.** Options run from windowed/UI-centric to fully immersive; for each key moment find the *minimum* level of immersion that suits it — don't assume every moment needs full immersion.
- **Use windows for contained, UI-centric experiences.** Prefer standard windows (planes in space with familiar controls) for standard tasks; people can relocate them anywhere and dynamic scaling keeps content legible near or far.
- **Prioritize comfort.**
  - Display content within the person's field of view, positioned relative to their head; don't make people turn their head or change position to interact.
  - Avoid motion that is overwhelming, jarring, too fast, or missing a stationary frame of reference.
  - Support indirect gestures so people can interact with hands resting in their lap or at their sides.
  - If supporting direct gestures, keep interactive content close and don't require extended interaction.
  - Avoid encouraging people to move much while in a fully immersive experience.
- **Help people share activities with others.** With SharePlay, participants see each other's *spatial Personas* as if together in the same space.
- Windows / volumes (hig/components/windows.md) · Immersive experiences, immersion and passthrough (hig/foundations/immersive-experiences.md) · Digital Crown (hig/inputs/digital-crown.md) · Playing audio — visionOS Spatial Audio (hig/patterns/playing-audio.md) · Eyes (hig/inputs/eyes.md) · Gestures — visionOS (hig/inputs/gestures.md) · Accessibility (hig/foundations/accessibility.md) · Spatial layout — scale, field of view (hig/foundations/spatial-layout.md) · Motion — visionOS (hig/foundations/motion.md) · SharePlay — visionOS (hig/technologies/shareplay.md)
- Videos cited: Design interactive experiences for visionOS (WWDC24 10096), Design great visionOS apps (WWDC24 10086), Principles of spatial design (WWDC23 10072). Change log: Feb 2, 2024 — link to Vision Pro User Guide; Sept 12, 2023 — intro artwork; June 21, 2023 — new page.

## Designing for watchOS
Full page: hig/getting-started/designing-for-watchos.md

Apple Watch is glanced at many times a day for sub-minute, single-screen interactions, stationary or in motion. Complications, notifications, and Siri are used more than the app itself, so the app must be streamlined, specialized, and independent.

**Rules**
- **Display.** Small, wrist-sized, easy-to-read, high-resolution.
- **Ergonomics.** Worn on the wrist, usually no more than a foot from the eyes; people raise the wrist to look and use the opposite hand to interact; the Always On display shows the watch face when the wrist drops.
- **Inputs.** Digital Crown for vertical navigation and inspecting data (consistent on the watch face, Home Screen, and in apps); tap, swipe, and drag gestures usable while in motion; the Action button triggers an essential action without looking at the screen; shortcuts for routine tasks; device data from GPS, blood-oxygen and heart sensors, altimeter, accelerometer, and gyroscope.
- **App interactions.** Many glances per day at the Always On display; concise interactions lasting less than a minute each; related experiences (complications, notifications, Siri) used more than the app.
- **System features.** Integrate with Complications, Notifications, Always On, and Watch faces.

**Best practices / links**
- Support quick, glanceable, single-screen interactions that deliver critical information succinctly and allow targeted actions with a gesture or two.
- Minimize navigation hierarchy depth; use the Digital Crown for vertical navigation — scrolling or switching between screens.
- Personalize by anticipating needs and using on-device data to provide actionable content relevant now or very soon.
- Use complications for relevant, potentially dynamic data and graphics on the watch face, visible on every wrist raise and tappable straight into the app.
- Use notifications for timely, high-value information and let people act without opening the app.
- Use background content such as color to convey supporting information, and materials to show hierarchy and sense of place.
- Design the app to function independently, complementing notifications and complications with additional detail and functionality.
- Digital Crown (hig/inputs/digital-crown.md) · Gestures (hig/inputs/gestures.md) · Action button (hig/inputs/action-button.md) · Shortcuts — Siri (hig/technologies/siri.md) · Complications (hig/components/complications.md) · Notifications (hig/components/notifications.md) · Always On (hig/technologies/always-on.md) · Watch faces (hig/components/watch-faces.md) · Color (hig/foundations/color.md) · Materials (hig/foundations/materials.md)
- Video cited: What's new in watchOS 26 (WWDC25 334). Change log: June 5, 2023 — glanceable experience and Digital Crown navigation guidance.

## Designing for iPhone Duo
Full page: hig/getting-started/designing-for-iphone-duo.md (new page, Sept 9, 2026)

iPhone Duo is a folding iPhone with an outer display (used closed) and an inner display (used open), each with a front-facing camera, joined by a center hinge that supports many poses. It is still iPhone: Designing for iOS patterns apply, and an app built on standard components that supports resizing adapts to poses with little adjustment. Controls move to the side of the display to preserve vertical space.

**Rules**

Anatomy and poses
- **Outer display** is used when closed; the system places toolbars and tab bars on the side to maximize vertical space; controls stay on the side when the device opens in landscape for consistency across displays.
- **Hinge** supports many holding/placing poses and affects the space available for content as the device folds.
- **Outer front-facing camera** sits in the corner, always visible, vertically aligned with the side controls; the **inner camera** is behind the display and hidden until active.
- **Poses**: partially folded like a book, placed on a surface, standing on its edges. Don't design a custom layout per pose: use size classes — compact width for the outer display, regular width for the inner display — and let the existing layout expand into available space rather than reinventing it.
- Preview and test poses with Device Hub in Xcode.

Best practices (page section)
- **Build your app to resize.** Two displays, many poses, and Split View multitasking mean many sizes; use size classes, layout margins, and safe area insets; avoid fixed widths and display-specific dependencies.
- **Create a consistent experience across displays.** Keep functionality and element state the same between displays; keep the information hierarchy but show an additional level on the larger inner display where it makes sense (e.g. list-or-detail closed, list-and-detail open).
- **Maintain the same functionality across device poses.** Controls may overflow and content may move or resize, but provide access to the same controls and content in every pose.
- **Follow the system's vertical layout for toolbars, tab bars, and navigation controls.** The outer display is wider and shorter than other iPhones, so the system moves controls to the side; on the inner display controls stay on the side in landscape at the same vertical height. Standard components get this automatically; refine only as the app needs.
- **Make your game playable in every device pose.** You may lock to portrait or landscape, but fill the screen as the pose changes; keep text and control sizes consistent; prefer changing aspect ratio over letterboxing/pillarboxing; if unavoidable, add artwork to the padding so it feels full screen.

Dynamic layouts and reserved regions
- Build layouts with layout margins and safe area insets (SwiftUI/UIKit `safeAreaInsets`); steer clear of fixed widths or anything tied to a specific display. Margins and safe areas are in Apple Design Resources.
- **Reserved regions** are areas content avoids or components adapt to (like iPad window controls):
  - The outer front-facing camera — always present; expands into the Dynamic Island for Live Activities; with side controls the system accounts for it automatically.
  - The inner front-facing camera — present only when the camera is active; UI moves aside when it activates.
  - The folding region — conditional; when partially open it divides the inner display into multiple usable regions, excluding the center.
- Alerts, context menus, and sheets move automatically to account for the fold; split views adapt column width and margins to the inner display's symmetry. Custom components use `ReservedRegion` (SwiftUI) / `UIView.ReservedRegion` (UIKit) to reposition away from reserved regions.
- **Adapt your layout when the device folds.** Prefer a container that adapts automatically (e.g. a split view that resizes panes); in grid layouts prefer an even number of columns so content divides cleanly; use `ReservedRegion` to keep important elements clear of the center when the system doesn't move them.
- **Avoid extreme layout changes as people fold the device.** Move only what's necessary to keep elements visible and tappable; favor small adjustments over rearrangement.

Split views and arrangement views
- A split view expands on the inner display and collapses to a single pane on the outer display (regular vs compact), and adapts to reserved regions automatically when built with standard components (`NavigationSplitView` / `UISplitViewController`).
- An **arrangement view** holds a primary and a secondary view and organizes them by display size, orientation, and reserved regions (`ArrangementView` / `UIArrangementViewController`). Two types:
  - *Split* — divides its area between the two views; splits horizontally when wider than tall, vertically when taller than wide. You can limit which axes it uses.
  - *Overlay* — stacks the views; when partially folded each view occupies one side, otherwise primary sits atop secondary. You can collapse the secondary view.
- **Consider an arrangement view when your layout already resembles one.** HStack/VStack-style layouts map to split; ZStack-style layouts map to overlay.
- **Keep navigation outside of arrangement views.** They lay out content only; wrap navigation split views and tab views around them, not inside.

Vertical controls
- Toolbars, tab bars, and navigation controls move from top/bottom to the side, except on the inner display in portrait, which keeps standard horizontal bars. Side controls include the Dynamic Island, status bar, toolbar (with navigation buttons), and tab bar.
- In Split View multitasking on the inner display, each app places controls along its outer edge (left app: left).
- Side controls stay aligned with hardware: same position relative to the outer camera, and the same side in right-to-left languages.
- **Account for asymmetry in your layouts.** Use safe areas so controls (including those on the opposite edge in Split View) don't cover content.
- **Keep controls consistent across device poses.** Not every pose has side controls or the same space; keep relative positions as similar as possible.
- **Follow the standard placement order for toolbar items.** Top of the vertical axis: primary navigation (Back, Close), then prominent actions (Done); keep remaining items in their original groupings — the system separates top-bar and bottom-bar items with vertical space.
- **Prioritize frequently used toolbar items.** Items overflow bottom-to-top by default; set visibility priority (`ToolbarItemVisibilityPriority` / `UIBarButtonItemVisibilityPriority`) on whole groups, then individual items. Preserve frequent actions (Compose, New Note) first and keep status-bearing items (badges) visible longer.
- **In general, don't override the default bar placement.** Side placement is a core iPhone Duo pattern.
- **Consider using the full display width where bars aren't necessary.** Works for non-scrolling, visual, immersive interfaces as long as nothing conflicts with the Dynamic Island or status bar; or combine: full-width background/header with inset scrollable content.
- **Group related toolbar items instead of spacing them manually.** `ToolbarItemGroup` / `UIBarButtonItemGroup` space items automatically and adapt to available space; add no fixed spacing.
- **Locate controls near the content they affect.** Controls belonging to a content area other than the trailing edge stay with that area (e.g. list controls above the leading pane).
- **Provide both a title and a symbol for each toolbar item that isn't text-only.** The system picks the representation; the title is used in overflow menus and expanded forms (`Label` / `UIBarButtonItem`).
- **Keep text-based buttons to a minimum.** Text labels stay in a horizontal bar; prefer a symbol wherever one works.
- **When space is limited, preserve either the toolbar or the tab bar based on the view's purpose.** Navigation-focused: move toolbar items into overflow so the tab bar stays (default compression). Task-oriented: minimize the tab bar to keep toolbar actions (`ToolbarVerticalCompressionBehavior` / `UIVerticalBarCompressionBehavior`).
- **Use the system overflow menu.** Move any custom overflow actions into it; reserve the ellipsis symbol for overflow and give other menus a distinct symbol (`ToolbarOverflowMenu` / `additionalOverflowItems`).

**Best practices / links**
- Layout, size classes (hig/foundations/layout.md) · Designing for iOS (hig/getting-started/designing-for-ios.md) · Split views (hig/components/split-views.md) · Toolbars (hig/components/toolbars.md) · Designing for games (hig/getting-started/designing-for-games.md)
- Developer docs cited: Preparing your app for iPhone Duo; Device Hub; ReservedRegion / UIView.ReservedRegion; ArrangementView / UIArrangementViewController; Screenshot specifications.
- Videos cited (Tech Talks): Design for iPhone Duo (111466), Raise the bar with iPhone Duo (111462), Strike a pose with adaptive layouts on iPhone Duo (111463).

## Designing for games
Full page: hig/getting-started/designing-for-games.md (updated June 9, 2025; new June 10, 2024)

Games run across every Apple platform; the page is cross-platform and defers to each Designing-for page for platform character. Get players into gameplay fast, keep text and buttons usable on every display, support each platform's default input, welcome everyone, and adopt Game Center, GameSave, haptics, and Spatial Audio.

**Rules**

Jump into gameplay
- **Let people play as soon as installation completes.** Include as much playable content as possible in the initial install while keeping download time to 30 minutes or less; download additional content in the background.
- **Provide great default settings.** Use device information to pick defaults (resolution, auto-recognized paired accessories and controllers, the player's accessibility settings); support the platform's most common interaction methods.
- **Teach through play.** Integrate configuration and onboarding into a playable tutorial; offer any written tutorial as a reference, not a prerequisite.
- **Defer requests until the right time.** Don't bombard people before play; permission for sensors or data such as hand tracking is required and should be requested inside the scenario that needs it; ask for ratings/reviews only after quality time with the game.

Look stunning on every display
- **Make sure text is always legible.** Contrast well with the background and use at least each platform's minimum text size (table below).
- **Make sure buttons are always easy to use.** Each platform defines a minimum button size for its default interaction; e.g. iOS buttons must be at least 44x44 pt for touch (table below).
- **Prefer resolution-independent textures and graphics.** Otherwise match game resolution to device resolution; in visionOS prefer vector art that survives dynamic scaling at different distances and angles.
- **Integrate device features into your layout.** Accommodate rounded corners and camera housings using platform safe areas; Apple Design Resources include safe-area templates.
- **Make sure in-game menus adapt to different aspect ratios.** Support 16:10, 19.5:9, and 4:3 (and both orientations on iPhone and iPad if supported) without obscuring content; use dynamic layouts with relative constraints; avoid fixed layouts; create device-specific layouts only when necessary.
- **Design for the full-screen experience.** macOS, iOS, and iPadOS full-screen mode hides other apps and system UI; in visionOS a Full Space game can completely surround the player.

Enable intuitive interactions
- **Support each platform's default interaction method.** Touch on iPhone; keyboard and mouse/trackpad on Mac; eyes and hands with indirect and direct gestures in visionOS (table below). Pay special attention to control sizing and menu behavior when bringing a pointer-based game to touch.
- **Support physical game controllers, while also giving people alternatives.** Every platform except watchOS supports them; not every player can use one, so offer alternative input.
- **Offer touch-based game controls that embrace the touchscreen on iPhone and iPad.** Allow direct interaction with game elements and virtual controls over game content.

Welcome everyone
- **Prioritize perceivability.** Content must be perceivable by sight, hearing, or touch: never rely solely on color for important details; cutscenes need descriptive subtitles or another way to read the content. Page lists sub-topics: text sizes, color and effects, motion, interactions, buttons.
- **Help players personalize their experience.** Let players customize type size, control mapping, motion intensity, and sound balance; use Apple accessibility technologies via system frameworks or Unity plug-ins.
- **Give players the tools they need to represent themselves.** Avatars, names, and descriptions should support the spectrum of self-identity and as many human characteristics as possible.
- **Avoid stereotypes in your stories and characters.** Review for depictions tying enemies to a race, gender, or cultural heritage; keep necessary cultural/language references respectful.

Adopt Apple technologies
- **Integrate Game Center** for cross-device discovery, friends, progress, achievements, leaderboards, challenges, and multiplayer; available on all platforms.
- **Let players pick up their game on any of their devices.** Support GameSave so game state follows the player's iCloud account.
- **Support haptics to help players feel the action.** Core Haptics (custom patterns, optionally with audio) is available in iOS, iPadOS, tvOS, and visionOS and on many game controllers.
- **Use Spatial Audio to immerse players.** Provide multichannel audio so it adapts to the device and enables Spatial Audio where supported.
- **Take advantage of Apple technologies for unique mechanics.** Augmented reality, machine learning, HealthKit, location, camera, microphone.

**Best practices / links**
- Launching (hig/patterns/launching.md) · Onboarding (hig/patterns/onboarding.md) · Loading (hig/patterns/loading.md) · Settings (hig/patterns/settings.md) · Privacy (hig/foundations/privacy.md) · Ratings and reviews (hig/patterns/ratings-and-reviews.md)
- Layout (hig/foundations/layout.md) · Typography (hig/foundations/typography.md) · Buttons (hig/components/buttons.md) · Images (hig/foundations/images.md) · In-game menus — Menus (hig/components/menus.md) · Going full screen (hig/patterns/going-full-screen.md)
- Game controls — physical and touch (hig/inputs/game-controls.md) · Gestures (hig/inputs/gestures.md) · Pointing devices (hig/inputs/pointing-devices.md)
- Accessibility (hig/foundations/accessibility.md) · Inclusion (hig/foundations/inclusion.md)
- Game Center (hig/technologies/game-center.md) · iCloud (hig/technologies/icloud.md) · Apple In-App Purchase (hig/technologies/apple-in-app-purchase.md) · Playing haptics (hig/patterns/playing-haptics.md) · Playing audio — visionOS (hig/patterns/playing-audio.md) · Technologies index (hig/technologies.md)
- Developer docs cited: Games Pathway; Adapting your game interface for smaller screens; Positioning content relative to the safe area; GameKit; GameSave; Core Haptics; Playing Haptics on Game Controllers; Unity plug-ins.
- Videos cited: Bringing Cyberpunk 2077 to Mac (WWDC26 356), Design no-code games with Reality Composer Pro 3 (WWDC26 252), Level up your games (WWDC25 209).

**Specs**

Text size by platform (default / minimum):

| Platform | Default text size | Minimum text size |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

Button size by platform (default / minimum):

| Platform | Default button size | Minimum button size |
|---|---|---|
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Interaction methods by platform:

| Platform | Default interaction methods | Additional interaction methods |
|---|---|---|
| iOS | Touch | Game controller |
| iPadOS | Touch | Game controller, keyboard, mouse, trackpad, Apple Pencil |
| macOS | Keyboard, mouse, trackpad | Game controller |
| tvOS | Remote | Game controller, keyboard, mouse, trackpad |
| visionOS | Touch | Game controller, keyboard, mouse, trackpad, spatial game controller |
| watchOS | Touch | – |

Other numbers on the page: initial download time 30 minutes or less; iOS touch buttons at least 44x44 pt; in-game menus must handle 16:10, 19.5:9, and 4:3 aspect ratios.

## Platform comparison

Built only from facts stated in the pages above. Games-page tables add the per-platform interaction, text-size, and button-size figures.

| Platform | Primary input | Distance / posture | Navigation idiom | Window / multitasking model | Distinctive constraints |
|---|---|---|---|---|---|
| iOS | Multi-Touch gestures, virtual keyboard, voice; gyro/accelerometer, nearby interactions. Games: touch (+ controller) | Held in one or both hands; portrait or landscape; no more than a foot or two away | Few onscreen controls; secondary actions one interaction away; swipe to go back and to act on list rows; controls in middle/bottom for reach | Many apps open, frequent switching between them | Sessions of 1–2 min or 1 h+; adapt to orientation, Dark Mode, Dynamic Type; widgets, quick actions, Spotlight, Shortcuts, activity views. Text 17/11 pt, buttons 44/28 pt |
| iPadOS | Multi-Touch, virtual keyboard, attached keyboard, pointing device, Apple Pencil, voice — often combined. Games: touch (+ controller, keyboard, mouse, trackpad, Pencil) | Held, on a surface, or on a stand; typically within about 3 feet | Minimize modals and full-screen transitions; controls easy to reach but out of the way; density set by viewing distance and input mode | Multiple apps onscreen at once; multitasking modes; drag and drop between apps; can also run in macOS | Adapt to orientation, multitasking modes, Dark Mode, Dynamic Type. Text 17/11 pt, buttons 44/28 pt |
| macOS | Physical keyboard, pointing device, game controls, Siri in any combination; high-precision input; keyboard shortcuts. Games: keyboard, mouse, trackpad (+ controller) | Stationary at a desk or table; about 1 to 3 feet | Menu bar exposes all commands; fewer nested levels, less modality; keyboard-only work styles | Multiple apps and windows; resize/hide/show/move windows; full-screen mode; extra displays incl. iPad; active/inactive window transitions | Comfortable information density; personalization of toolbars, windows, colors, fonts; file management, Dock menus. Text 13/10 pt, buttons 28/20 pt |
| tvOS | Remote (Siri Remote gestures), game controller, voice, other devices' apps. Games: remote (+ controller, keyboard, mouse, trackpad) | Many feet from a stationary TV, often 8 feet or more; may move around the room | Focus system highlights and expands the focused item | One immersive experience at a time, often hours; picture-in-picture for a second app or video | Edge-to-edge artwork legible from across the room; multiuser sign-in and profile switching; TV app, SharePlay, Top Shelf, TV provider accounts. Text 29/23 pt, buttons 66/56 pt |
| visionOS | Eyes to target + indirect gesture (tap); direct gestures (touch); Digital Crown for passthrough amount. Games: touch (+ controller, keyboard, mouse, trackpad, spatial game controller) | Content placed relative to the head; sitting, standing, or lying down; stays within field of view so people remain at rest | Standard windows as relocatable planes in space; dynamic scaling keeps content legible near or far; minimum immersion that suits each moment | Shared Space by default (apps side by side; windows, volumes, 3D objects); Full Space for a single app with blended 3D content, portals, or full worlds | Visual comfort paramount; avoid jarring/fast motion or missing stationary reference; indirect gestures with hands at rest; not while driving or near hazards; age 13+; Spatial Audio; SharePlay spatial Personas. Text 17/12 pt, buttons 60/28 pt |
| watchOS | Digital Crown (vertical navigation), tap/swipe/drag, Action button, shortcuts; GPS, blood-oxygen and heart sensors, altimeter, accelerometer, gyroscope. Games: touch only, no controller | On the wrist, no more than a foot away; wrist raise to view, opposite hand to interact; stationary or in motion | Single-screen, glanceable; minimal hierarchy depth; Digital Crown scrolls or switches screens | One app, interactions under a minute; complications, notifications, Siri used more than the app; Always On shows the face on wrist drop | Small display; app must work independently of its complications/notifications; color and materials convey hierarchy and status. Text 16/12 pt, buttons 44/28 pt |
| iPhone Duo | Same as iOS (Designing for iOS applies); touch | Closed (outer display) or open (inner display); partially folded like a book, on a surface, standing on its edges | Toolbars, tab bars, and navigation controls on the side (except inner display in portrait); Back/Close at top of the axis, then Done; items overflow bottom-to-top; system overflow menu with ellipsis | Outer display = compact width, inner = regular width; split views collapse closed and expand open; Split View multitasking on the inner display with each app's controls on its outer edge; arrangement views (split / overlay) | Reserved regions: outer camera (always, grows into Dynamic Island), inner camera (when active), folding region (when partially open); hinge; side controls keep the same side in RTL; even column counts in grids; games fill the screen in every pose and prefer aspect-ratio change over letterboxing |
