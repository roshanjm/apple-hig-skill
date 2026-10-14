# Patterns — HIG digest

The HIG Patterns section covers recurring user tasks and experiences that cut across individual components: launching, loading, onboarding, modality, searching, settings, entering data, feedback, notifications, accounts, files, printing, undo, media playback, haptics, drag and drop, collaboration, charts, workouts and live TV. Full pages live in `hig/patterns/` (one file per pattern, same slug as developer.apple.com; crawled 2026-10-14). This digest keeps every rule, every platform-specific instruction and every number from those pages, but drops Apple's examples, illustrations, video lists and explanatory prose. Read the full page when you need the reasoning behind a rule.

## Charting data
Full page: hig/patterns/charting-data.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Use a chart to communicate what a dataset means — trends over time, the current state of a changing quantity, or comparisons across categories. If you only need to provide data without conveying information about it, use a scrollable, searchable, sortable list or table instead. Chart components are covered on the Charts page.

**Rules**
- **Use a chart when you want to highlight important information about a dataset.** Charts are visually prominent and draw attention; make clear what people can learn.
- **Keep a chart simple, letting people choose when they want additional details.** Don't pack in data; reveal large datasets or functionality gradually (levels of detail, subsets, progressively richer versions of the chart).
- **Make every chart in your app accessible.** Provide accessibility labels describing values and components plus accessibility elements for interaction. Descriptive headline text never replaces accessibility labels.
- **In general, prefer common chart types** (bar, line) so people already know how to read them.
- **If a chart presents data in a novel way, help people learn how to interpret it** (e.g., animate each element individually on first encounter).
- **Examine the data from multiple levels or perspectives** — macro (totals, averages), mid-level (useful subsets), individual points (notable values) — to find details worth displaying.
- **Aid comprehension by adding descriptive text:** titles, subtitles, annotations, and a brief headline or summary that emphasizes the most important information and actionable takeaways.
- **Match the size of a chart to its functionality, topic and level of detail.** Large enough to read labels and annotations and to support the interactivity you offer; small charts for glanceable info or as a preview of a larger chart shown elsewhere.
- **Prefer consistency across multiple charts, deviating only to highlight differences.** Charts with a similar purpose share type and style; use different types/styles only to signal meaningful differences.
- **Maintain continuity among multiple charts that use the same data.** One chart type and consistent colors, annotations, layouts and descriptive text across small and expanded versions.

**Dev refs**
- Swift Charts (incl. Chart3D)

## Collaboration and sharing
Full page: hig/patterns/collaboration-and-sharing.md · Platforms: ios,ipados,macos,visionos,watchos
Use the system share sheet / sharing popover and Messages integration so people can share content or start a collaboration; works with CloudKit, iCloud Drive or a custom infrastructure (custom requires universal links). Real-time co-participation is SharePlay (separate page).

**Rules**
- **Place the Share button in a convenient location, like a toolbar.** The share sheet (iOS 16+) and sharing popover (iPadOS 16+, macOS 13+) include choosing a file-sharing method and setting permissions for a new collaboration; in SwiftUI, a `ShareLink` opens the share sheet.
- **If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports.** CloudKit: pass both the file and your collaboration object to get "send copy". iCloud Drive: "send copy" supported by default. Custom: include a file (or a plain-text representation) in your collaboration object.
- **Write succinct phrases that summarize the sharing permissions you support** ("Only invited people can edit", "Everyone can make changes"); the system shows them in the permission-summary button.
- **Provide a set of simple sharing options that streamline collaboration setup** — who can access, edit vs. read-only, whether collaborators can add participants. Keep custom choices to a minimum and group them for at-a-glance understanding.
- **Prominently display the Collaboration button as soon as collaboration starts.** It shows that content is shared and by whom; place it next to the Share button.
- **Provide custom actions in the collaboration popover only if needed.** The popover has three sections: collaborators + Messages/FaceTime buttons (top), your custom items (middle), the manage-shared-file button (bottom). Offer only essentials.
- **If it makes sense, customize the title of the collaboration-management button** (default "Manage Shared File"). CloudKit provides the management view; otherwise build your own.
- **Consider posting collaboration event notifications in Messages** — content change, membership change, or a mention — with a universal link to the relevant view (`SWHighlightEvent`).
- A custom collaboration infrastructure must support universal links to get Messages integration and system sharing UI.

**Platform notes**
- iOS/iPadOS/macOS: no additional · tvOS: not available · visionOS: screen sharing in the Shared Space streams the current window to collaborators; if someone moves the app to a Full Space the stream pauses for others until it returns to the Shared Space · watchOS: use `ShareLink` to present the system share sheet.

**Dev refs**
- ShareLink (SwiftUI), Shared with You, SWHighlightEvent, CloudKit, Supporting universal links in your app

## Drag and drop
Full page: hig/patterns/drag-and-drop.md · Platforms: ios,ipados,macos,visionos
Move or copy selected content from a *source* to a *destination* within one container, between containers, or between apps. Defaults: same container = move; different container = copy; between apps = always copy. Input methods by platform:
- visionOS: pinch and hold a virtual object while dragging it anywhere, including along the z-axis.
- iOS/iPadOS: touchscreen gestures, a pointing device, or Full Keyboard Access mode.
- Universal Control: drag content between a Mac and an iPad.
- macOS: a pointing device, Full Keyboard Access mode, or VoiceOver.

**Rules**
- **As much as possible, support drag and drop throughout your app.** System components (text fields, text views) have it built in.
- **Offer alternative ways to accomplish drag-and-drop actions** — menu commands to copy/move; in iOS/iPadOS identify sources and destinations with accessibility APIs so assistive technologies can drag and drop.
- **Determine when dragging within your app results in a move or a copy.** Same container → move; different container → copy. Before changing defaults, prefer the behavior least likely to cause frustration or data loss.
- **Support multi-item drag and drop when it makes sense.** iOS/iPadOS/macOS/visionOS: select multiple and drag as a group; macOS also from several apps at once; iPadOS lets people add items to an in-progress drag.
- **Prefer letting people undo a drag-and-drop operation.** Ask for confirmation before an operation that can't be undone (e.g., dropping into a write-only folder); otherwise give a way to reverse the result afterward.
- **Consider offering multiple versions of dragged content, ordered from highest to lowest fidelity** (e.g., PDF vector → lossless PNG with transparency → lossy JPEG; native chart object → image) so the destination picks the best it accepts.
- **Consider supporting spring loading** — buttons and segmented controls activate when content is dragged over them. Mac with Magic Trackpad: force-click while holding content; iPad: hover while holding content.
- **Display a drag image as soon as people drag a selection about three points.** Make it translucent so it's distinct from the original and destinations show through; keep it until the drop.
- **If it adds clarity, modify the drag image to predict the result** (e.g., expand to the photo's default size in a document); use drag *flocking* to group multiple items, ungrouping on drop. Avoid a drag image that changes constantly and radically.
- **Show people whether a destination can accept dragged content.** Insertion point or container highlight only when it accepts; no feedback or an explicit "not allowed" image (`circle.slash`) when it doesn't. Show cues only while content is over the destination; with several destinations, identify one at a time.
- **When a drop lands on an invalid destination or fails, provide visual feedback** — the item moves back to its source (if visible) or scales up and fades out.
- **Scroll the contents of a destination when necessary** as an item is dragged within a long scrolling container; stop auto-scrolling once the drag leaves the container (system text views/fields do this by default).
- **When there's a choice, pick the richest version of dropped content your app can accept.**
- **Extract only the relevant portion of dropped content if necessary** (a dropped contact in a recipient field yields name + email only).
- **When a physical keyboard is attached, check for the Option key at drop time.** Option held forces a same-container drag to copy; released before the drop → move.
- **Provide feedback when dropped content needs time to transfer** — progress indicator; placeholder at the drop location in collections, lists and tables. The system may alert on time-consuming cross-app transfers.
- **Provide feedback when dropped content initiates a task or action** (e.g., printing): show it began and report progress.
- **Apply appropriate styling to dropped text.** Keep original font, typeface, size and attributes when source and destination support the same styles; otherwise apply the destination's style.
- **After a drop, maintain the content's selection state in the destination, updating the source as needed.** Same-container move: content disappears from the original location; same-container copy: deselect the original; different container: deselect in the source.

**Platform notes**
- iOS/iPadOS: **Let people perform multiple simultaneous drag activities** — allow adding items during a drag (with flocking feedback) and accept multiple simultaneous drops.
- macOS:
  - **Consider letting people drag content from your app into the Finder** in a format your app can reopen (e.g., `.ics`), or as a *clipping* — a temporary container for dragged content, unrelated to the Clipboard.
  - **Let people drag selected content from an inactive window without first making it active.** A *background selection* looks different from an active selection and drags to the active window without bringing the inactive window forward.
  - **When possible, let people drag individual items from an inactive window** without affecting its existing background selection.
  - **Consider displaying a badge during multi-item drag operations** — a small filled oval containing the item count; update it if the destination accepts only a subset.
  - **Consider changing the pointer appearance to indicate what a drop will do** — copy, drag link, disappearing item, or operation not allowed (see Pointers).
  - **As much as possible, let people select and drag content with a single motion** unless they're selecting multiple items.
- visionOS: **When possible, launch your app to handle content dropped into empty space** by associating a user activity with draggable content (`NSUserActivity`); a dropped URL launches Safari, Quick Look–supported content launches Quick Look.
- tvOS/watchOS: not supported.

**Dev refs**
- Drag and drop (UIKit), Drag and Drop (AppKit), File Provider, accessibilityDragSourceDescriptors, accessibilityDropPointDescriptors, NSUserActivity

## Entering data
Full page: hig/patterns/entering-data.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Minimize what people must type by pre-gathering information and supporting every available input method.

**Rules**
- **Get information from the system whenever possible.** Don't ask for what you can read from settings or obtain with permission (location, calendar).
- **Be clear about the data you need** — a placeholder prompt ("username@company.com") or an introductory label ("Email"); prefill reasonable defaults.
- **Use a secure text-entry field when appropriate** (`SecureField`; tvOS digit entry view with `isSecureDigitEntry`). The visionOS system text field shows entered data only to the wearer and blurs automatically under AirPlay.
- **Never prepopulate a password field.** Always ask for the password or use biometric/keychain authentication (see Managing accounts).
- **When possible, offer choices instead of requiring text entry** — picker, menu or other selection component.
- **As much as possible, let people provide data by dragging and dropping or pasting it.**
- **Dynamically validate field values.** Verify as soon as a value is entered and give feedback immediately. For numeric data use a number formatter (accepts only numbers; can format decimals, percentage, currency).
- **Make sure people understand that required data must be provided before they can proceed** — e.g., enable Next/Continue only after the required fields are filled.

**Platform notes**
- macOS: **Consider an expansion tooltip to show the full version of clipped or truncated field text** (appears when the pointer rests on the field; also for iOS/iPadOS apps running on a Mac) · iOS/iPadOS/tvOS/visionOS/watchOS: no additional.

**Dev refs**
- SecureField (SwiftUI), isSecureDigitEntry (TVDigitEntryViewController), Input events (SwiftUI)

## Feedback
Full page: hig/patterns/feedback.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Feedback communicates status, success or failure, warnings, and chances to correct a mistake. Match delivery to significance: passive display for status; interruption for possible data loss.

**Rules**
- **Make sure all feedback is accessible.** Deliver it through several channels (color, text, sound, haptics) so it works when the device is silenced, people look away, or they use VoiceOver.
- **Consider integrating status feedback into your interface** near the items it describes, so people get it without leaving their context (e.g., last-update text and unread count in a mailbox toolbar).
- **Use alerts to deliver critical — and ideally actionable — information.** Alerts disrupt; match importance to interruption. Overuse or trivial content drains their impact.
- **Warn people when they initiate a task that can cause unexpected and irreversible data loss.** Don't warn when data loss is the expected result (e.g., deleting a file).
- **When it makes sense, confirm that a significant action or task has completed** (e.g., a successful Apple Pay transaction). Reserve confirmations for sufficiently important activities — people expect success and mainly need to know about failure.
- **Show people when a command can't be carried out and help them understand why.**

**Platform notes**
- watchOS: **Avoid displaying an indeterminate progress indicator (loading indicator).** An animated indicator makes people feel they must keep watching; instead reassure them they'll get a notification when the process completes · other platforms: no additional.

**Dev refs**
- Animation and haptics (UIKit)

## File management
Full page: hig/patterns/file-management.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Document-based apps create, edit and save files that people also manage system-wide — via the Finder on Mac and the Files app on iPhone, iPad and Apple Vision Pro. watchOS and tvOS provide no document-browsing interface.

**Rules**
- **Use app menus and keyboard shortcuts to let people create and open documents.** iPadOS surfaces New/Open in the Command-key shortcuts interface, macOS in the File menu. Regardless, include an Add (+) button to create a new document; in macOS the add action lives in the File menu.
- **If your app requires a custom file browser, support people's understanding of the platform's file system.** Open to the most relevant location (Documents, iCloud, last-used) but let people navigate the rest of the file system.
- **Help people be confident that their work is always preserved unless they cancel or delete it.** Avoid explicit save actions; autosave periodically while editing, on close, and on app switch.
- **Hide file extensions by default, but let people view them if they choose.** Reflect the current choice in every save/open interface.
- **Use a Quick Look viewer to let people preview a file even when your app can't open it**, without leaving your app.
- **Consider implementing a Quick Look generator if your app produces custom file types**, so the Finder, Files and Spotlight can preview your documents.

**Platform notes**
- iOS/iPadOS — Document launcher (iOS 18 / iPadOS 18 and later, `DocumentGroupLaunchScene`): a full-screen experience with a *title card* (app title + two app-specific buttons), a background image plus *accessory* images around the card, and a sheet holding the file browser with optional custom toolbar controls. All three parts are customizable; the system supplies the app name.
  - **Assign the title card's buttons to your app's most important functions.** Primary typically creates a new document; secondary offers additional options (e.g., Start Writing / Choose a Template).
  - **Provide a background that's clearly distinct from the accessories and title card** — solid color, gradient or pattern; avoid complex images or patterns that distract from foreground elements.
  - **Be mindful of accessory placement.** Accessories can sit in front of and behind the card for depth, but the app name and both buttons must remain clearly visible; avoid clutter; test across all supported screen sizes and orientations.
  - **Use animation sparingly.** If accessories animate, use gentle, repeating, subtle motion (breathe, sway softly).
- iOS/iPadOS — File provider app extension (custom UI for importing, exporting, opening and moving your documents):
  - **Display only documents that are appropriate in the current context** (a PDF editor loading your extension sees only PDFs); optionally show modification dates, sizes, and local/remote status.
  - **Let people select a destination when exporting and moving documents** unless you store everything in a single directory; consider letting them add subdirectories.
  - **Avoid including a custom top toolbar** — the extension loads in a modal view that already has one.
  - Your app can also let people browse and open other apps' files with the system document browser.
- macOS:
  - **Use the default file browser unless you have an important reason to create a custom one.**
  - **Make your custom file-opening interface convenient** — an "open recent" action, filter criteria, multi-select; customize the Open button title to the task (e.g., Insert when inserting a file's contents).
  - **Provide a save interface to let people change a file's name, format or location.** New documents are "Untitled" until renamed; default to a logical location; offer a format choice if you support several.
  - **Consider extending the Save dialog** with a custom accessory view of useful options (e.g., include attachments).
  - Finder Sync extension (if you sync local and remote files): badges showing sync status, custom contextual-menu items for file/folder tasks (favoriting, password protection), custom toolbar buttons for global actions (start a sync).
  - **Help people avoid losing work if they turn off autosaving** ("Ask to keep changes when closing documents" in Desktop & Dock settings): show that a document has unsaved changes and present a save dialog on close, quit, log out or restart.
  - **When autosaving is off, make sure people know a document has unsaved changes** — a dot on the window's close button and next to the document name in the Window menu. Never show the dot when autosave is on. Regardless of autosave, you may append "Edited" to the title-bar name, but remove it as soon as autosave or an explicit save occurs.
- tvOS/visionOS/watchOS: no additional.

**Dev refs**
- DocumentGroupLaunchScene, Documents (SwiftUI), File Provider, Finder Sync, Adding a document browser to your app (UIKit)

## Going full screen
Full page: hig/patterns/going-full-screen.md · Platforms: ios,ipados,macos
Full-screen modes let a window fill the screen and hide system controls for a distraction-free environment. tvOS and watchOS apps already fill the screen; visionOS has no full-screen mode (people expand windows or use the Digital Crown to reduce passthrough — see Immersive experiences).

**Rules**
- **Support full-screen mode when it makes sense** — games, viewing media (video, slideshows), in-depth tasks that benefit from no distractions.
- **If necessary, adjust your layout in full-screen mode, but don't programmatically resize your window.** Keep essential content prominent, use the extra space, keep adjustments subtle so transitions aren't jarring and the same items remain.
- **Continue to provide access to essential features and controls** so tasks complete without exiting (e.g., playback controls persistently available or easy to reveal).
- **Except in games, let people reveal the Dock while your iPadOS or macOS app is in full-screen mode.** A full-screen game may ask iPadOS to ignore an initial swipe up from the bottom edge, or hide the Dock entirely in macOS.
- **After people switch away from your full-screen experience, help them resume where they left off** — games and slideshows pause automatically.
- **Let people choose when to exit full-screen mode.** Don't end it automatically when they switch experiences or finish an activity.
- **Prioritize content by temporarily hiding toolbars and navigation controls** when content is the focus (full-screen photos, reading). Let people restore them with a familiar gesture — tap, swipe down, move the cursor to the top. Keep controls visible when essential for navigation or tasks. (A visionOS window can hide its chrome, but people expect immersive experiences there instead.)

**Platform notes**
- iOS/iPadOS: **Consider deferring system gestures to prevent accidental exits.** The Home Screen indicator hides shortly after switching to your app and reappears on interaction with the bottom of the screen; one swipe then exits. Retain this default whenever possible; if it causes unexpected exits, require two swipes instead of one (`preferredScreenEdgesDeferringSystemGestures`).
- macOS:
  - **Use the system-provided full-screen experience** (`toggleFullScreen(_:)`) so the window works in every context — it automatically accommodates the camera housing on some Mac models.
  - **In a game, don't change the display mode when players go full screen.** People expect to control their display mode, and changing it doesn't improve performance.
  - **Always let people choose when to enter full-screen mode** — the window's Enter Full Screen button, the View menu item, or Control-Command-F. Avoid a custom menu of window modes; a game may add a custom full-screen toggle.
- tvOS/visionOS/watchOS: not supported.

**Dev refs**
- preferredScreenEdgesDeferringSystemGestures (UIHostingController / UIViewController), hideDock (NSApplication.PresentationOptions), toggleFullScreen(_:), fullScreenCover(item:onDismiss:content:), NSScreen, NSWindow.CollectionBehavior, Managing your game window for Metal in macOS

## Launching
Full page: hig/patterns/launching.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Launching begins when someone opens the app, includes any initial download, and ends when the first screen is ready. Onboarding, if any, comes after.

**Rules**
- **Launch instantly.** People sometimes won't wait more than a couple of seconds.
- **If the platform requires it, provide a launch screen.** iOS, iPadOS and tvOS show it the moment the app starts and replace it with the first screen. macOS, visionOS and watchOS don't require one.
- **If you need a splash screen, consider displaying it at the beginning of your onboarding flow;** with no onboarding, show it as soon as launching completes.
- **Restore the previous state when your app restarts.** Restore granular details — scroll position, windows in the same state and location — so people never retrace steps.
- **Downplay the launch experience.** A launch screen isn't onboarding, a splash screen, or artistic expression; its sole job is to make launch feel quick and ready.
- **Design a launch screen that's nearly identical to the first screen.** Different elements cause an unpleasant flash. If the first screen starts as a solid color, the launch screen is only that color. Match the device's current orientation and appearance mode.
- **Avoid including text on your launch screen, even if the first screen has text** — launch-screen content is static and won't be localized.
- **Don't advertise.** No logos or branding unless they're a fixed part of the first screen; don't mimic a splash or About screen.

**Platform notes**
- iOS/iPadOS: **Launch in the appropriate orientation** — the device's current orientation if you support both; your single supported orientation otherwise, letting people rotate. A landscape-only interface must respond correctly whether the device is rotated left or right.
- tvOS: the launch screen is static, unlike the layered images used elsewhere in a tvOS app.
  - **In a live-viewing app, consider automatically starting playback soon after people start the app** — new or recently viewed live content after a few seconds of inactivity (see Live-viewing apps).
- visionOS: **Consider launching in the Shared Space even if your app is fully immersive** — a window gives context, time to load, and a control to open the Full Space; people prefer choosing when to transition, especially with other apps open.
- macOS/watchOS: no additional.

**Dev refs**
- Specifying your app's launch screen (Xcode), Responding to the launch of your app (UIKit)

## Live-viewing apps
Full page: hig/patterns/live-viewing-apps.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Prioritize live content on every screen and make it distinguishable from video-on-demand (VOD) at a glance; minimize the time between launch and playback.

**Rules**
- **Feature live content prominently and make it easy to access.** Live content in the first tab means at most one tap to start viewing.
- **Let people tap once — or not at all — to start playback** (e.g., a Watch Now button over featured or recently viewed live content that disappears and starts full-screen, immersive playback).
- **Make sure live content looks live** — mark it with a badge, symbol or sash, or group it in a row titled "Live".
- **Consider indicating the progress of currently playing live content** (progress bar showing how much remains).
- **Give people additional actions and viewing alternatives.** Playback is always primary; also offer record, restart, download, etc., in the same order everywhere (e.g., Watch, Start Over, Record, Favorite). Show repeat air times so people can schedule viewing.
- **Consider using a content footer for browsing channels during playback** so people browse without leaving the live experience. If you do:
  - Give it a subtle treatment, such as darkening, to keep text legible and items visually distinct from the content behind it.
  - Make the thumbnail of the currently playing content easy to identify — badge it or tint its progress bar.
  - Match its categories to those in your EPG.
  - Design a simple, predictable way to invoke and dismiss it — if swiping up invokes the footer, swiping down dismisses it.
- **Provide instant visual feedback when people change channels** — confirms arrival and buys time for the stream to load.
- **Match audio to the current context.** Audio continues when people browse while live content plays in the background; it stops when they leave the live tab.
- **EPG: prominently display current information and make it easy to return to playback** — current program, channel and time easy to spot on open.
- **EPG: make browsing effortless** — easy paging, scrolling, jumping; consider a My Channels or Favorites group.
- **EPG: group content into familiar categories** (Movies, TV Shows, Kids, Sports, Popular); reuse them in the content footer.
- **EPG: let people browse without leaving their current content** — Picture in Picture or background playback.
- **Cloud DVR: let people start and stop recording from the info panel** while live-streaming.
- **Cloud DVR: let people record a future program in a view with content details**, choosing that program only or all future episodes.
- **Cloud DVR: help people adapt recording to their needs** — current episode only, new episodes only, only games with specific teams.
- **Cloud DVR: allow playback and other content-specific actions within the DVR area** — play, delete, adjust recording settings from the detail view.
- **Cloud DVR: consider a control for managing DVR settings** — delete watched recordings or content older than N days; ideally automatic storage management that overwrites the oldest or already-viewed content.

## Loading
Full page: hig/patterns/loading.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
The best loading finishes before people notice. Design asset, level and content loading so it never disrupts the experience.

**Rules**
- **Show something as soon as possible.** A blank wait reads as a problem; show placeholder text, graphics or animations and replace them as content arrives.
- **Let people do other things in your app or game while content loads** in the background (e.g., read about the next level or use an in-game menu).
- **If loading takes an unavoidably long time, give people something interesting to view** — gameplay hints, tips, new-feature intros. Estimate remaining time accurately so placeholder content is neither cut short nor repeated.
- **Improve installation and launch time by downloading large assets in the background.** Use the Background Assets framework to schedule downloads (level packs, 3D models, textures) immediately after installation, during updates, or at other nondisruptive times.
- **Clearly communicate that content is loading and how long it might take.** When loading takes more than a moment or two, use progress indicators — determinate when the duration is known, indeterminate when it isn't.
- **For games, consider creating a custom loading view** with animations and elements matching the game's style, since standard indicators can feel out of place.

**Platform notes**
- watchOS: **As much as possible, avoid showing a loading indicator.** Display content immediately; if content needs a second or two, a loading indicator is better than a blank screen · other platforms: no additional.

**Dev refs**
- Background Assets, Improving the player experience for games with large downloads (GameKit)

## Managing accounts
Full page: hig/patterns/managing-accounts.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Require an account only when core functionality needs it; otherwise let people use the app without one. If an account is required, consider Sign in with Apple for a consistent, trusted sign-in.

**Rules**
- **Explain the benefits of creating an account and how to sign up** — a brief, friendly description displayed in the sign-in view.
- **Delay sign-in for as long as possible.** Let people get a sense of the app first (e.g., browse freely; sign in only at purchase).
- **If you don't use Sign in with Apple in iOS, iPadOS, macOS or visionOS, prefer using a passkey.** People supply only a user name to create or sign in. If you must keep passwords, require two-factor authentication (iCloud Keychain verification codes).
- **Always identify the authentication method you offer** — "Sign In with Face ID", not a generic "Sign In".
- **Refer only to authentication methods available in the current context.** Check device capabilities (`LABiometryType`); don't mention Face ID on a device without it.
- **In general, avoid offering an app-specific setting for opting in to biometric authentication** — it's a system-level setting; an in-app one is redundant and confusing.
- **Avoid using the term "passcode" to refer to account authentication** — it means the device/Apple-services passcode.
- If you let people create an account in-app you must let them delete it (not just deactivate), and comply with regional law (right to be forgotten). If law compels you to retain data (e.g., digital health records) or follow a specific process, clearly describe it.
- **Provide a clear way to initiate account deletion within your app.** If impossible in-app, link directly to the deletion webpage; don't bury it in Privacy Policy or Terms of Service.
- If people created the account with Sign in with Apple, revoke the associated tokens when they delete it.
- **Provide a consistent account-deletion experience in-app and on the website** — neither version longer or more complicated.
- **Consider letting people schedule account deletion for the future** (use remaining services, wait for renewal) — and always also offer immediate deletion.
- **Tell people when account deletion will complete, and notify them when it's finished.**
- **If you support in-app purchases, help people understand how billing and cancellation work when they delete their account:**
  - Billing for an auto-renewable subscription continues through Apple until people cancel the subscription, regardless of whether they delete their account.
  - After deleting their account, people need to cancel their subscription or request a refund.
  - Also provide information on how to cancel subscriptions and manage purchases (see Apple In-App Purchase > Helping people manage their subscriptions / Providing help). Account deletion is required even if the subscription wasn't bought through your app.
- TV provider apps that require sign-in: use TV Provider Authentication for the most efficient onboarding.
- **Avoid displaying a sign-out option when people are signed in at the system level.** If you must, prompt them to go to Settings > TV Provider.
- **Never instruct people to sign out by adjusting privacy controls.** Settings > Privacy TV-provider controls manage app access, not sign-out.

**Platform notes**
- tvOS: people use a remote, not a keyboard — ask for the minimum amount of information.
  - **Prefer letting people use another device to sign up or authenticate.** With associated domains configured, Apple TV works with other devices to safely suggest credentials, including Sign in with Apple.
  - **When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user.** tvOS 16 and later can share credentials across users while storing each person's profile and data separately (`kSecUseUserIndependentKeychain`, User Management entitlement).
  - **Minimize data entry.** For more than a small amount of information, send people to a website on another device; for an email address, show the email keyboard, which lists recently entered addresses.
- watchOS: use iCloud synchronization for Keychain access so user names and passwords autofill and app settings persist.
- iOS/iPadOS/macOS/visionOS: no additional.

**Dev refs**
- Supporting passkeys (Authentication Services), LABiometryType, Securing Logins with iCloud Keychain Verification Codes, Token revocation (Sign in with Apple REST API), Configuring an associated domain, kSecUseUserIndependentKeychain, User Management Entitlement

## Managing notifications
Full page: hig/patterns/managing-notifications.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
You need permission before sending any notification; people can change it in settings and silence all notifications (except government alerts in some locales). A Focus filters alerts during an activity; delivery scheduling batches alerts into a summary; people choose which contacts and apps break through. A delayed alert doesn't delay the notification itself — it's available as soon as it arrives. Direct communications (calls, messages) use *communication* notifications via SiriKit intents, so people can customize them with Siri and the system times delivery by sender; everything else uses *noncommunication* notifications, each tagged with one of four system-defined interruption levels:
- *Passive* — information people can view at their leisure (a restaurant recommendation).
- *Active* (default) — information people might appreciate when it arrives (a score update for their team).
- *Time Sensitive* — information that directly impacts the person and requires immediate attention (an account security issue, a package delivery).
- *Critical* — urgent health and safety information demanding immediate attention; extremely rare, typically from governmental and public agencies or health/home apps.

**Rules**
- **Build trust by accurately representing the urgency of each notification.** People can turn everything off; never use a high level for low-priority information.
- **Use the Time Sensitive interruption level only for notifications that are relevant in the moment** — an event happening now or within an hour. On the first Time Sensitive notification the system explains the behavior and offers to turn it off; it periodically re-asks.
- A Critical notification requires an entitlement because it overrides the Ring/Silent switch, scheduled delivery and Focus.
- Don't use notifications for marketing or promotional content unless people explicitly agree (e.g., a subscriber offer, a live-event offer in a game).
- **Never use the Time Sensitive interruption level to send a marketing notification** — it must never break through a Focus or scheduled delivery.
- **Get people's permission if you want to send promotional or marketing notifications** — an alert, modal view or other UI describing the types of information, with a clear opt-in/opt-out.
- **Make sure people can manage their notification settings within your app** — an in-app settings screen to change their informational and marketing choices (see Settings).

**Platform notes**
- watchOS: iPhone notification settings apply to the same apps on Apple Watch by default; people manage them in the Apple Watch app on iPhone, or swipe left on an arriving notification for per-notification options such as Mute 1 Hour or Turn off Time Sensitive · other platforms: no additional.

**Specs**

| Interruption level | Overrides scheduled delivery | Breaks through Focus | Overrides Ring/Silent switch on iPhone and iPad |
|---|---|---|---|
| Passive | No | No | No |
| Active | No | No | No |
| Time Sensitive | Yes | Yes | No |
| Critical | Yes | Yes | Yes |

**Dev refs**
- User Notifications, UNNotificationInterruptionLevel, INSendMessageIntent, UNNotificationContentProviding

## Modality
Full page: hig/patterns/modality.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
A modal presentation blocks interaction with the parent view and requires an explicit dismissal. Use it to ensure people receive and act on critical information, to confirm or modify their last action, to complete a distinct narrowly scoped task without losing context, or for an immersive/complex task. Every platform has alerts; platforms add activity views, sheets, confirmation dialogs/action sheets. Distinct tasks use sheets or popovers (iOS/iPadOS/macOS) or a separate window (iPadOS/macOS/visionOS). Full-screen modals suit media viewing or multistep editing; nonmodal full screen is on the Going full screen page; visionOS immersion on Immersive experiences.

**Rules**
- **Present content modally only when there's a clear benefit** — helping people focus or make choices that affect their content or device.
- **Aim to keep modal tasks simple, short, and streamlined.** A complicated modal task makes people lose the task they suspended, especially when the modal obscures it.
- **Avoid creating a modal experience that feels like an app within your app.** If subviews are unavoidable, provide a single path through the hierarchy and avoid buttons that could be mistaken for the dismiss button.
- **Consider a full-screen modal style for in-depth content or a complex task** — videos, photos, camera, marking up a document, editing a photo. In the visionOS Shared Space it fills a window; in a Full Space it can become more immersive.
- **Always give people an obvious way to dismiss a modal view**, following platform conventions: iOS/iPadOS/watchOS — a button in the top toolbar or swipe down; macOS/tvOS — a button in the main content view.
- **When necessary, get confirmation before closing a modal view to avoid data loss.** Whether dismissed by gesture or button, explain the situation and offer ways to resolve it (e.g., an iOS action sheet with a Save option).
- **Make it easy to identify a modal view's task** — a title naming the task, or text describing it or giving guidance.
- **Let people dismiss a modal view before presenting another one.** Stacked modals add clutter and cognitive load. An alert may appear over everything, including other modals, but never show more than one alert at a time.

**Dev refs**
- Presentation modifiers (SwiftUI), UIModalPresentationStyle (UIKit), Modal Windows and Panels (AppKit)

## Multitasking
Full page: hig/patterns/multitasking.md · Platforms: ios,ipados,macos,tvos,visionos
With rare exceptions (some games; visionOS apps in a Full Space) every app must work well with multitasking, and must always be ready to save and restore its context because people can switch away at any time.

**Rules**
- **Pause activities that require people's attention or active participation when they switch away** (games, media viewing); on return, let them continue as if they never left.
- **Respond smoothly to audio interruptions** (an incoming call, a Siri-initiated playlist). People expect:
  - Pause audio indefinitely for primary audio interruptions, such as music, podcasts or audiobooks.
  - Temporarily lower the volume or pause for shorter interruptions, such as GPS directional notifications, then resume the original volume or playback when the interruption ends.
- **Finish user-initiated tasks in the background** (downloads, video processing) — complete any task that needs no further input before suspending.
- **Use notifications sparingly.** Notify when an important or time-sensitive task finishes so people can switch back; don't notify for routine or secondary tasks — let people check on return.

**Platform notes**
- iOS: FaceTime calls and Picture in Picture video continue while people use another app.
- iPadOS: people view and interact with several apps' windows at once, and one app can have multiple open windows.
  - Full-screen apps occupy the whole screen; people switch between windows with the app switcher.
  - Windowed apps are resizable and arranged much like macOS; the system provides window controls for common tiling configurations, entering full screen, minimizing and closing. The frontmost window has colored window controls and casts a drop shadow on windows behind it (see Windows > iPadOS).
  - Videos and FaceTime calls can play in a Picture in Picture overlay in either mode.
  - Apps don't control multitasking configurations and receive no indication of the one people chose — adapt gracefully to every screen size (see Layout, Windows).
- macOS: multitasking is the default; drop shadows layer windows and other effects distinguish window states (see macOS window states).
- tvOS: people can play or browse while a movie/TV show plays in Picture in Picture (where supported).
- visionOS: multiple apps run at once in the Shared Space; only one window is active — the one being looked at — while the previous one becomes more translucent and recedes along the z-axis. Closing a window backgrounds the app without quitting; closing the Now Playing app's window pauses audio (resumable from Control Center without reopening the window).
  - **Avoid interfering with the system-provided multitasking behavior.** The system applies a feathered mask to a window people look away from; don't change the appearance of a window's edges.
  - **Don't pause a window's video playback when people look away from it.** As on macOS, playback started in one window continues while people work in another.
  - **Be prepared for situations where your audio can duck** — unless your app is the Now Playing app, its audio can duck when people look away to another app.
- watchOS: not supported.

**Dev refs**
- Multitasking on iPad, Mac, and Apple Vision Pro (UIKit), Responding to the launch of your app (UIKit)

## Offering help
Full page: hig/patterns/offering-help.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Provide contextual help only when the experience can't be self-evident: inline guidance for small tasks, tutorials for complex ones, tips (TipKit) to teach features, and tooltips (help tags) on macOS/visionOS.

**Rules**
- **Let your app's tasks inform the types of help people might need.** Inline view for one- or two-step tasks; a tutorial for complex multistep tasks. Relate help to the exact action in progress and make it easy to dismiss or skip.
- **Use relevant and consistent language and images.** Match the current input device (no game-controller imagery for Siri Remote users) and platform vocabulary (no "click" on iPhone, no "tap" on Mac).
- **Make sure all help content is inclusive** (see Inclusion).
- **Avoid bloating help by explaining how standard components or patterns work.** Describe the specific action a standard element performs in your app. For a unique control or nonstandard input use (e.g., Siri Remote rotated 90 degrees), orient people quickly, preferring animation or graphics over long text.
- **Use the most appropriate tip type.** Popover tip to preserve content flow; inline tip to keep surrounding information visible — annotation-style when pointing at a specific element, hint-style when not tied to UI.
- **Use tips for simple features.** If a feature needs more than three actions, it's too complicated for a tip.
- **Make tips short, actionable, and engaging** — one or two sentences, direct action-oriented language; nothing promotional (advertises, sells, or off-context) and nothing about a different feature or flow.
- **Define rules so tips reach the intended audience.** Use parameter- or event-based eligibility rules; don't show tips for features someone already used; with several tips set a display frequency, e.g., once every 24 hours.
- **If an image or symbol is associated with the feature, consider including it in the tip, preferring the filled variant.** Don't repeat the same image in both the tip and the UI it points to.
- **Use buttons to direct people to information or options** — straight to the relevant settings, or to additional resources such as a setup flow.

**Platform notes**
- macOS, visionOS: a *tooltip* (called a *help tag* in user documentation) is a small transient view describing how to use a component. It appears when the pointer rests on an element (Mac, including iPhone/iPad apps running there) or when a person looks at or hovers over it (visionOS); SwiftUI `help(_:)`.
  - **Describe only the control that people indicate interest in** — not nearby controls or a larger task.
  - **Explain the action or task the control initiates**, often beginning with a verb ("Restore default settings", "Add or remove a language from the list").
  - **In general, avoid repeating a control's name in its tooltip** — it wastes space and rarely adds value.
  - **Be brief.** Limit tooltip content to a maximum of 60 to 75 characters (localization changes length); use sentence fragments and omit articles. If a control needs a lot of text, simplify the interface instead.
  - **Use sentence case.** For complete sentences, omit ending punctuation unless your app's style requires it.
  - **Consider offering context-sensitive tooltips** — different text for a control's different states.
- iOS/iPadOS/tvOS/watchOS: no additional.

**Dev refs**
- TipKit, help(_:) (SwiftUI), NSHelpManager (AppKit)

## Onboarding
Full page: hig/patterns/onboarding.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Onboarding occurs after launching completes and is not part of launch. Ideally the app explains itself; if onboarding is needed, make it fast, fun and optional.

**Rules**
- **Teach through interactivity.** Let people safely try an action, discover a feature or test a game mechanic instead of reading instructions.
- **Consider providing a collection of context-specific tips instead of a single onboarding flow.** Display instructions near the area they refer to (TipKit).
- **If you need a prerequisite onboarding flow, design a brief, enjoyable experience that doesn't require memorizing a lot.** Teaching too much overwhelms and reduces retention.
- **If you offer a separate tutorial, consider making it optional.** If skipped at first launch, don't show it again, but keep it easy to find (help, account or settings area).
- **Keep onboarding content focused on the experience you provide** — not on how to use the system or device.
- **Briefly display a splash screen if necessary** — a succinct graphic shown just long enough to absorb at a glance without feeling like a delay.
- **Don't let large downloads hinder onboarding.** Ship enough media and content in the package so people can start immediately.
- **Avoid displaying licensing details within your onboarding flow.** Let the App Store show agreements and disclaimers; if you must include them, integrate them without disrupting the flow.
- **Postpone nonessential setup flows or customization steps.** Provide reasonable defaults so most people start right away.
- **If your app needs access to private data or resources before it can function, consider integrating the permission request into onboarding** to explain why and the benefit; otherwise request permission when the specific function is first used (see Privacy > Requesting permission).
- **Prefer letting people experience your app before prompting for ratings or purchases.**

**Dev refs**
- TipKit

## Playing audio
Full page: hig/patterns/playing-audio.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Audio must behave as people expect across outputs (speakers, headphones, Bluetooth, AirPlay) and controls (volume buttons, iPhone Ring/Silent switch, headphone controls, Control Center slider, accessories). Silent mode suppresses nonessential sound (keyboard clicks, effects, game soundtracks, feedback) and plays only explicitly initiated audio (media, alarms, audio/video messaging). Volume settings govern all sound however adjusted (iPhone ringer volume is separate). Connecting headphones reroutes without interruption; disconnecting pauses immediately.

**Rules**
- **Adjust levels automatically when necessary — don't adjust the overall volume.** Mix relative, independent levels; the system volume always governs final output.
- **Permit rerouting of audio when possible** (stereo, car radio, Apple TV) unless there's a compelling reason not to.
- **Use the system-provided volume view** (`MPVolumeView`) — volume slider (appearance customizable) plus an output-rerouting control.
- **Choose an audio category that fits the way your app or game uses sound** (`AVAudioSession.Category`; see Specs). It decides mixing, background play and Ring/Silent response — don't stop another app's music if you don't need to.
- **Respond to audio controls only when it makes sense.** Fine when actively playing, in a clear audio-related context, or connected via Bluetooth/AirPlay; otherwise don't halt audio playing from another app.
- **Avoid repurposing audio controls.** Never redefine a control's meaning; if you don't support a control, don't respond to it.
- **Create custom audio player controls only to offer commands the system doesn't support** (custom skip increments, related content such as a sports score).
- **Let other apps know when your app finishes playing temporary audio** — flag the session so others can resume (`notifyOthersOnDeactivation`).
- **Determine how to respond to audio-session interruptions.** E.g., don't interrupt recording for an incoming call unless the person accepts it. A VoIP app must end the call when an iPad Smart Folio closes (closing mutes the mic and interrupts the session); restarting the session on reopen would unmute without the person's knowledge. Inspect the interruption to decide (Handling audio interruptions).
- **When an interruption ends, determine whether to resume playback automatically.** Interruptions are *resumable* (incoming call) or *nonresumable* (new music playlist). A media app checks the type is resumable before resuming; a game can resume without checking because its audio wasn't an explicit choice (`shouldResume`).

**Platform notes**
- iOS/iPadOS: **Use the system's sound services to play short sounds and vibrations** (Audio Services).
- macOS: notification sounds mix with other audio by default.
- tvOS: the system plays audio only when people initiate it (in-app interaction, device calibration) — no sounds for alerts or notifications.
- visionOS: subtle, expressive sounds provide essential feedback when people look at and gesture with virtual objects; the system combines audio algorithms with the physical surroundings to produce *Spatial Audio* — sound perceived as coming from specific locations in space. Never communicate important information with sound alone. The Now Playing app's audio pauses when its window closes; a non–Now Playing app's audio can duck when people look away from it.
  - **Prefer playing sound.** People keep sounds audible while wearing the device; a silent app — especially in an immersive moment — feels lifeless or broken. Look for sounds that aid navigation and convey the spatial qualities of your app.
  - **Design custom sounds for custom UI elements.** System elements already play sound to help people locate them and get feedback; custom elements need the same.
  - **Use Spatial Audio to create an intuitive, engaging experience.** *Ambient audio* provides pervasive sound that anchors people in a virtual world; an *audio source* sounds like it comes from a specific object. Consider using both.
  - **Consider defining a range of places from which your app's sounds can originate.** Spatial Audio helps people locate a sounding object whether it's stationary or moving; a moved window keeps emitting sound from wherever it goes.
  - **Consider varying sounds that people could perceive as repetitive over time.** Randomize a sound file's pitch and volume during playback rather than authoring many files.
  - **Decide whether sound is fixed to the wearer or tracked by the wearer.** *Fixed* sound seems pointed at the person regardless of gaze direction or object movement; *tracked* sound comes from an object and changes as it moves closer or farther. Generally use tracked for realism; fixed suits enveloping experiences (Mindfulness).
- watchOS: the system manages audio playback — short clips while the app is active in the foreground, or longer audio that continues after wrist-down or an app switch (Playing Background Audio).
  - **Use the recommended encoding values for media assets:** 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding).
  - **Consider presenting a Now Playing view** so people control current or recently played audio without leaving your app. The system-provided view shows the current source (another Watch or iPhone app) and auto-selects the current or most recently used one.

**Specs**

| Category | Meaning | Behavior |
|---|---|---|
| Solo ambient | Sound isn't essential, but it silences other audio. For example, a game with a soundtrack. | Responds to the silence switch. Doesn't mix with other sounds. Doesn't play in the background. |
| Ambient | Sound isn't essential, and it doesn't silence other audio. For example, a game that lets people play music from another app during gameplay in place of the game's soundtrack. | Responds to the silence switch. Mixes with other sounds. Doesn't play in the background. |
| Playback | Sound is essential and might mix with other audio. For example, an audiobook or educational app that teaches a foreign language, which people might want to listen to after leaving the app. | Doesn't respond to the silence switch. May or may not mix with other sounds. Can play in the background. |
| Record | Sound is recorded. For example, a note-taking app that offers an audio recording mode. An app of this nature might switch its category to playback if it lets people play the recorded notes. | Doesn't respond to the silence switch. Doesn't mix with other sounds. Can record in the background. |
| Play and record | Sound is recorded and played, potentially simultaneously. For example, an audio messaging or video calling app. | Doesn't respond to the silence switch. May or may not mix with other sounds. Can record and play in the background. |

**Dev refs**
- AVAudioSession, AVAudioSession.Category, MPVolumeView, notifyOthersOnDeactivation, shouldResume, Handling audio interruptions, Audio Services (AudioToolbox), Configuring your app for media playback (AVFoundation), MusicKit, Playing Background Audio (WatchKit), Adding a Now Playing View (WatchKit)

## Playing haptics
Full page: hig/patterns/playing-haptics.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Haptics add touch to visual and audio feedback. Supported iPhones play haptics automatically for switches, sliders and pickers; Apple Watch's Taptic Engine pairs built-in patterns with an audible tone; a Mac with a Force Touch trackpad can play haptics during drags or force clicks. External devices: game controllers (iPadOS, macOS, tvOS, visionOS), Apple Pencil Pro and some trackpads on certain iPad models.

**Rules**
- **Use system-provided haptic patterns according to their documented meanings.** If the documented use doesn't fit, use a generic pattern or create a custom one — never repurpose a pattern.
- **Use haptics consistently throughout your app or game.** Build a clear causal relationship between each haptic and its trigger; the same pattern must not mean both failure and success.
- **Prefer using haptics to complement other feedback.** Match a haptic's intensity and sharpness to the animation it accompanies; synchronize with sound where useful.
- **Avoid overusing haptics.** Occasional haptics feel right, frequent ones tire; user-test for balance. The best haptic is one people don't notice but miss when it's off.
- **In most apps, prefer playing short haptics that complement discrete events.** Long-running haptics suit gameplay but dilute meaning and distract in apps; on Apple Pencil Pro, continuous haptics don't clarify writing/drawing and can make holding the pencil unpleasant.
- **Make haptics optional.** Let people turn them off or mute them; the app must remain fully usable without them.
- **Be aware that playing haptics might impact other user experiences** — vibration can disrupt the camera, gyroscope or microphone.
- Custom haptics (Core Haptics): combine *transient* events (brief taps/impulses — e.g., the Home Screen Flashlight button) and *continuous* events (sustained vibration — e.g., the lasers message effect); control *sharpness* (soft/rounded/organic through crisp/precise/mechanical) and *intensity* (strength); add optional audio; vary dynamically by input or context (a jump from a tree hits harder than a jump in place).

**Platform notes**
- iOS (supported iPhone models):
  - Use standard UI components — toggles, sliders, pickers — that play Apple-designed system haptics by default.
  - When it makes sense, use a feedback generator (`UIFeedbackGenerator`) to play a predefined pattern: *notification* haptics give the outcome of a task or action (depositing a check, unlocking a vehicle); *impact* haptics provide a physical metaphor complementing a visual (a tap when a view snaps into place, a thud when heavy objects collide); *selection* haptics give feedback while a UI element's value is changing.
- macOS: when a Magic Trackpad is available, respond to a drag operation or force click with one of three patterns — Alignment, Level change, Generic (see Specs; `NSHapticFeedbackPerformer`).
- watchOS: Apple Watch Series 4 and later provides Digital Crown haptics — linear detents by default as the crown rotates; some system controls (e.g., table views) emit a detent as each new item scrolls onto the screen. Use the watchOS haptic set only for its defined meanings (see Specs; `WKHapticType`).
- iPadOS/macOS/tvOS/visionOS: game controllers can provide haptics (Playing Haptics on Game Controllers); Apple Pencil Pro and some trackpads provide haptics on certain iPad models.

**Specs**

macOS Magic Trackpad patterns:

| Haptic feedback pattern | Description |
|---|---|
| Alignment | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| Level change | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| Generic | Intended for providing general feedback when the other patterns don't apply. |

watchOS haptics:

| Haptic | Meaning |
|---|---|
| Notification | Something significant or out of the ordinary has happened and requires attention. Same haptic the system plays when a local or remote notification arrives. |
| Up | An important value increased above a significant threshold. |
| Down | An important value decreased below a significant threshold. |
| Success | An action completed successfully. |
| Failure | An action failed. |
| Retry | An action failed but the person can retry it. |
| Start | An activity started. Use when starting a timer or any activity a person can explicitly start and stop; the Stop haptic usually follows. |
| Stop | An activity stopped. Use when stopping a timer or other activity the person previously started. |
| Click | The sensation of a dial clicking — communicates progress at predefined increments or intervals. Overuse diminishes its utility and overlapping clicks can confuse. |

**Dev refs**
- Core Haptics, UIFeedbackGenerator, NSHapticFeedbackPerformer, WKHapticType, Playing Haptics on Game Controllers, Delivering Rich App Experiences with Haptics

## Playing video
Full page: hig/patterns/playing-video.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
System video players exist for iOS, iPadOS, macOS, tvOS and visionOS; content can also surface through the TV app. The player picks a default mode by aspect ratio: *aspect-fill* / full-screen (scales to fill, may crop edges; default for wide video 2:1 through 2.40:1; `resizeAspectFill`) or *aspect* / fit-to-screen (entire frame visible, letterbox/pillarbox as needed; default for standard 4:3, 16:9 and anything up to 2:1, and for ultrawide above 2.40:1; `resizeAspect`). Most platforms support Picture in Picture. In visionOS and tvOS the player also has *transport controls* (subtitles, audio language, add to library, favorite) and *content tabs* (Info, Episodes, Chapters); in visionOS the transport controls are an ornament.

**Rules**
- **Use the system video player to give people a familiar and convenient experience.** If a custom player is truly required, mirror the system player's behavior and interface — even slight divergence frustrates people who don't know which habits still work.
- **Always display video content at its original aspect ratio.** Embedded letterbox/pillarbox padding defeats scaling, shrinks video in both modes, and breaks edge-to-edge contexts like PiP on iPad.
- **Provide additional information when it adds value** — image, title, description and other metadata in iOS, iPadOS, tvOS and visionOS (`externalMetadata`); restrict it so it doesn't obscure playback.
- **Support the interactions people expect, regardless of input device.** Space on a connected keyboard plays/pauses on Apple Vision Pro, Mac, iPhone, iPad and Apple TV; Siri Remote gestures move through media on Apple TV.
- **If people need playback options or content-specific info in your tvOS app, consider a transport control or a custom content tab.** Offer only the most useful items; actions take no more than a step or two; content is succinct. Transport control = playback-related action (favoriting); content tab = supplementary info or recommendations.
- **Avoid allowing audio from different sources to mix as viewers switch between modes** (full screen ↔ PiP). Mixing happens when an audio source mishandles secondary audio — handle `silenceSecondaryAudioHintNotification`.
- **TV app: ensure a smooth transition to your app.** The TV app fades to black and skips your launch screen; immediately present your own black screen before playing or resuming.
- **TV app: show the expected content immediately.** Go straight from black to content — no splash screens, detail screens, intro animations or other barriers. If an interstitial is unavoidable, Select steps through it and Play skips it.
- **TV app: avoid asking people if they want to resume playback** — resume automatically when possible.
- **TV app: play or pause when people press Space on a connected Bluetooth keyboard.**
- **TV app: make sure content plays for the correct viewer.** Switch automatically to the profile named in the playback request; if none is specified, ask the viewer to choose before playback so it's known next time.
- **TV app: use the previous end time when resuming a long video clip.**
- **Avoid displaying loading screens when possible.** If loading takes more than two seconds, show a black loading screen with a centered activity spinner and no surrounding content.
- **Start playback immediately** — show the loading screen only until enough content has loaded to begin; keep loading the rest in the background.
- **Minimize loading screen content** — minimal branding/images, always on the black background that transitions seamlessly to playback.
- **Exiting playback: show a contextually relevant screen** — people stay in your app, so show a detail view for what they watched with a resume option; failing that, a menu listing it or your main menu.
- **Exiting playback: be prepared for an immediate exit** — prepare the exit view as soon as the playback notification arrives.

**Platform notes**
- tvOS:
  - **Defer to content when displaying logos or noninteractive overlays above video.** A small unobtrusive logo or countdown timer may be appropriate; avoid large distracting overlays. Some devices are prone to image retention — keep overlays short and prefer translucent Standard Dynamic Range (SDR) graphics to bright, opaque content.
  - **Show interactive overlays gracefully** (quizzes, surveys, progress check-ins). Implement a minimum delay of 0.5 seconds before pausing media and displaying the overlay; give people a clear way to dismiss it and resume playback.
- visionOS:
  - **Help people stay comfortable when playing video in your app.** You often don't control the content, but you can:
    - Let people choose when to start playing a video.
    - Use a small window for playback, letting people resize it if they want.
    - Make sure people can see their surroundings during playback.
  - **In a fully immersive experience, avoid letting virtual content obscure playback or transport controls.** The system places the player at a predictable, optimal location; keep the default controls in the ornament near the bottom of the player unoccluded.
  - **Avoid automatically starting a fully immersive video playback experience.** People need control and won't appreciate being launched into immersion without warning.
  - **Create a thumbnail track if you want to support scrubbing.** Supply thumbnails that each measure 160 px in width (HLS Authoring Specification > Trick Play).
  - **Avoid expanding an inline video player to fill a window.** In a window, playback controls sit in the same plane as the player, not in a floating ornament; inline video must be 2D and surrounding window content must stay visible so people don't expect a more immersive experience (`AVPlayerViewController`).
  - **Use a RealityKit video player for video in a splash screen or transitional view.** Such video leads into the next experience, so it needs no controls or system integration (dimming, view anchoring). RealityKit uses the correct aspect ratio for 2D and 3D video, supports closed captions, and can play video as a special effect on the surface of a custom view or object.
- watchOS: the system manages video playback; apps play short clips while active in the foreground — inline via a movie element, or in a separate interface (`VideoPlayer`).
  - **Keep video clips short** — no longer than 30 seconds. Long clips consume disk space and require a raised wrist for longer, causing fatigue.
  - **Use the recommended sizes and encoding values for media assets** (see Specs); avoid scaling video clips, which hurts performance and appearance.
  - **Avoid creating a poster image that looks like a system control.** People must understand they can tap a movie element for playback.
  - **Consider creating a poster image that represents a video clip's contents.** Tapping it replaces the image with inline playback; avoid images unrelated to the content or that look like a control.
- iOS/iPadOS/macOS: no additional.

**Specs**

watchOS video assets (audio values also apply to audio-only assets):

| Attribute | Value |
|---|---|
| Video codec | H.264 High Profile |
| Video bit rate | 160 kbps at up to 30 fps |
| Resolution (full screen) | 208x260 px (portrait orientation) |
| Resolution (16:9) | 320x180 px (landscape orientation) |
| Audio | 64 kbps HE-AAC |

**Dev refs**
- AVKit, AVPlayerViewController, VideoPlayer, resizeAspectFill, resizeAspect, externalMetadata, silenceSecondaryAudioHintNotification, RealityKit, HTTP Live Streaming (HLS Authoring Specification > Trick Play), Configuring your app for media playback (AVFoundation)

## Printing
Full page: hig/patterns/printing.md · Platforms: ios,ipados,macos,visionos
Integrate the system print functionality where it makes sense and add custom printer- or document-specific options only when necessary.

**Rules**
- **Make printing discoverable** in standard locations — a Print item in the macOS File menu; in iOS/iPadOS a toolbar button that opens an action sheet. A macOS toolbar Print button is fine as an optional item people add when customizing the toolbar.
- **Present a printing option only when it's possible.** Nothing to print or no printers: dim File > Print in macOS, remove Print from the action sheet in iOS/iPadOS; dim or hide a custom print button.
- **Present relevant printing options** (page range, multiple copies, double-sided) with the system-provided view, only when the printer supports them.

**Platform notes**
- macOS:
  - **If your app offers app-specific print options the system doesn't, consider creating a custom category for the print panel.** Default categories include Layout, Paper Handling, and Media & Quality; give yours a unique name such as your app name (Keynote adds presenter notes, slide backgrounds, skipped slides).
  - **If your app supports document-specific page settings, consider presenting a page setup dialog** for rarely changed page size, orientation and scaling. Don't reimplement features the system provides (changing orientation, printing in reverse order).
  - **Make sure interdependencies between options are clear** — e.g., when double-sided printing is available, printing on transparencies becomes unavailable.
  - **Separate advanced features from frequently used features** — hide advanced options behind a disclosure control labeled "Advanced Options".
  - **Consider letting people preview the effect of a setting** (e.g., update a thumbnail when a tone control changes).
  - **Consider storing modified settings with the document** — at minimum, keep print settings until the document closes.
- iOS/iPadOS/visionOS: no additional · tvOS/watchOS: not supported.

**Dev refs**
- UIPrintInteractionController (UIKit), NSDocument (AppKit)

## Ratings and reviews
Full page: hig/patterns/ratings-and-reviews.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
A great experience earns ratings; timing the request matters. Signals to consider: launch count or frequency, features explored, tasks completed. People can always rate in the App Store.

**Rules**
- **Ask for a rating only after people have demonstrated engagement** — e.g., after completing a level or a significant task. Never on first launch or during onboarding; premature asks invite negative feedback.
- **Avoid interrupting people while they're performing a task or playing a game** — ask at natural breaks or stopping points.
- **Avoid pestering people.** Allow at least a week or two between requests, and only after further engagement.
- **Prefer the system-provided prompt** (iOS, iPadOS, macOS; `RequestReviewAction`). The system checks for prior feedback, shows a prompt for a rating plus optional written review, lets people respond or dismiss with one tap/click, lets people opt out for all apps, and limits display to three occurrences per app within a 365-day period.
- **Weigh resetting your summary rating on a new version against showing fewer ratings** — a reset reflects the current version but lowers the rating count, which can deter downloads.

**Dev refs**
- RequestReviewAction (StoreKit), Reset app summary rating (App Store Connect)

## Searching
Full page: hig/patterns/searching.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
In-app search uses a search field, personalized with recent searches, suggestions, completions or corrections; scope bars and tokens narrow results. iOS, iPadOS and macOS apps can also implement find-in-document, and Spotlight searches across apps and the web when you index your content. (Page updated 2026-06-08.)

**Rules**
- **If search is important, give it a primary position in your app or view** — e.g., a search field in the bottom toolbar alongside other key actions (Notes), or a dedicated tab in tab-bar apps (Photos, Apple TV).
- **Aim to make your app's content searchable through a single location.** Apps with clearly distinct sections may add a local search that filters the current view (Music's songs/albums).
- **Clearly display the current scope of a search** — descriptive placeholder text, a scope bar, or a title (Mail always names the mailbox being searched).
- **Provide suggestions to make searching easier** — recent searches before typing, predictive suggestions while typing (`searchSuggestions(_:)`).
- **Take privacy into consideration before displaying search history**; if you show it, provide a way to clear it.
- **Make your app's content searchable in Spotlight** — make it indexable and supply descriptive metadata.
- **Define metadata for custom file types you handle** via a Spotlight File Importer plug-in (`CSImportExtension`).
- **Use Spotlight to offer advanced file-search capabilities within your app** — e.g., a button that starts a Spotlight search from the current selection, with a custom results view or filtered subset.
- **Prefer using the system-provided open and save views** — they include a search field over the entire system.
- **Implement a Quick Look generator if your app produces custom file types** so Spotlight and other apps can preview them.

**Dev refs**
- searchSuggestions(_:) (SwiftUI), CSImportExtension, Core Spotlight (Adding your app's content to Spotlight indexes), Quick Look

## Settings
Full page: hig/patterns/settings.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
The system Settings app handles global options (appearance, networking, accounts, accessibility, language/region) and, on some platforms, per-app permissions (location, microphone/camera, notifications, Siri, Search). A custom in-app settings area holds general options (interface style, game-saving behavior); task-specific options belong inside the task.

**Rules**
- **Aim to provide default settings that give the best experience to the largest number of people** — e.g., auto-maximize game performance for the device rather than asking at launch.
- **Minimize the number of settings you offer.** Too many settings feel unapproachable and hide the one people want.
- **Make settings available in ways people expect** — Command-Comma (,) with a hardware keyboard; the Esc key in games.
- **Avoid using settings to ask for setup information you can get in other ways** — detect a connected controller/accessory; detect Dark Mode.
- **Respect people's systemwide settings and avoid redundant versions in your custom settings** (accessibility accommodations, scrolling behavior, authentication methods). Duplicates imply system settings may not apply or that your copy affects other apps.
- **Put general, infrequently changed settings in your custom settings area** — window configuration, game-saving behavior, keyboard mappings, account options. Opening settings suspends the task, so keep frequently changed options out.
- **When possible, let people modify task-specific options without going to your settings area** — showing/hiding parts of a view, reordering items, filtering a list live on the screens they affect. In games, players adjust their approach as gameplay, not via settings.
- **Add only the most rarely changed options to the system-provided Settings app;** if you do, consider a button in your interface that opens it directly.

**Platform notes**
- macOS: choosing Settings in the App menu opens your custom settings window, typically with a toolbar of buttons that switch between *panes* of related settings.
  - **Include a settings item in the App menu.** Don't add settings buttons to a window's toolbar — they take space from frequently used commands. Document-level options go in the File menu.
  - **Dim a settings window's minimize and maximize buttons.** Command-Comma (,) reopens it quickly, so it needn't live in the Dock, and the window sizes itself to the current pane.
  - **Use a noncustomizable toolbar that remains visible and always indicates the active toolbar button** — people rely on a stable settings interface.
  - **Update the window's title to reflect the currently visible pane.** With a single pane, title it "*App Name* Settings".
  - **Restore the most recently viewed pane** when the window opens — people often adjust related settings more than once.
- watchOS: apps and games don't add custom settings to the system Settings app; instead offer a small number of essential options at the bottom of the main view, or let people reconfigure objects through a More menu.
- iOS/iPadOS/tvOS/visionOS: no additional.

**Dev refs**
- Settings (SwiftUI), UserDefaults (Foundation), Preference Panes

## Undo and redo
Full page: hig/patterns/undo-and-redo.md · Platforms: ios,ipados,macos,visionos
People try undo — often repeatedly — until something changes, and may not know which action it targets. Help them predict the outcome and highlight the result.

**Rules**
- **Help people predict the results of undo and redo as much as possible.** On iPhone, describe the result in the alert shown when people shake the device, with options to perform or cancel. In menus, name the result in the item label (Undo Typing, Redo Bold).
- **Show the results of an undo or redo.** If the affected content is offscreen, reveal it (e.g., scroll to the restored paragraph) so people don't think nothing happened and repeat the action.
- **Let people undo multiple times.** No unnecessary limits; people expect to undo every action since a logical step like opening a document or saving.
- **Consider giving people the option to revert multiple changes at once** — batch related incremental adjustments to one property, or undo everything since open/save.
- **Provide undo and redo buttons only when necessary.** People expect the Edit menu (macOS), keyboard shortcuts (Mac, iPad) or shaking (iPhone). If buttons are important, use the standard system symbols and put them in a toolbar.

**Platform notes**
- iOS/iPadOS:
  - **Avoid redefining standard gestures for undo and redo** — three-finger swipe, or shaking iPhone. Redefining them makes the experience unpredictable.
  - **Briefly and precisely describe the operation to be undone or redone.** The alert title automatically prefixes "Undo " or "Redo " (including the trailing space); supply an additional word or two to follow it, e.g., "Undo Name", "Redo Address Change".
- macOS: **Place undo and redo commands at the top of the Edit menu and support the standard keyboard shortcuts** — Command-Z (undo) and Shift-Command-Z (redo).
- visionOS: no additional · tvOS/watchOS: not supported.

**Dev refs**
- UndoManager (Foundation)

## Workouts
Full page: hig/patterns/workouts.md · Platforms: ios,ipados,watchos
People wear Apple Watch during many workouts and carry iPhone or iPad for walking, wheelchair pushing and running; larger or stationary devices (iPad Pro, Mac, Apple TV) are used for live or recorded sessions. Build on device activity data and the familiar fitness components.

**Rules**
- **In a watchOS fitness app, use workout sessions to provide useful data and relevant controls.** During an active session watchOS keeps displaying your app between wrist raises; show the data people care about (elapsed/remaining time, calories burned, distance) and controls like lap or interval markers.
- **Avoid distracting people from a workout with information that's not relevant** — no workout list or other app areas mid-session. The arrangement many watchOS workout apps (including Workout) use:
  - Leftmost screen: large buttons that control the in-progress session, such as End, Resume and New.
  - Dedicated screen: metrics and other data people can read at a glance.
  - Rightmost screen: media playback controls, if supported.
- **Use a distinct visual appearance to indicate an active workout** — real-time updating metrics and a unique layout make the active state recognizable at a glance.
- **Provide workout controls that are easy to find and tap** — pause, resume, stop — with clear feedback when a session starts or stops.
- **Help people understand the health information your app records if sensor data is unavailable** (water may block heart rate; distance and calories still recorded). For the *Swimming* or *Other* workout types, use language similar to the Workout app (see Specs).
- **Provide a summary at the end of a session** — confirms the workout is finished and shows recorded data; consider including Activity rings.
- **Discard extremely brief workout sessions** — if a session ends a few seconds after starting, discard the data automatically or ask whether to record it.
- **Make sure text is legible when people are in motion** — large font sizes, high-contrast colors, the most important information easiest to read.
- **Use Activity rings correctly** — the Apple-designed rings whose colors and meanings match the Activity app; use them only for their documented purpose.

**Platform notes**
- iOS/iPadOS/watchOS: no additional · macOS/tvOS/visionOS: not supported.

**Specs**

| Example text from the Workout app |
|---|
| GPS is not used during a Pool Swim, and water may prevent a heart-rate measurement, but Apple Watch will still track your calories, laps, and distance using the built-in accelerometer. |
| In this type of workout, you earn the calorie equivalent of a brisk walk anytime sensor readings are unavailable. |
| GPS will only provide distance when you do a freestyle stroke. Water might prevent a heart-rate measurement, but calories will still be tracked using the built-in accelerometer. |

**Dev refs**
- WorkoutKit, Workouts and activity rings (HealthKit)
