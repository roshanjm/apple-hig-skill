# Technologies J–Z — HIG digest

This file digests the Apple Human Interface Guidelines **Technologies** pages whose titles start with J through Z (Live Photos, Mac Catalyst, Machine learning, Maps, NFC, Photo editing, ResearchKit, SharePlay, ShazamKit, Sign in with Apple, Siri, Tap to Pay on iPhone, VoiceOver, Wallet), as crawled from developer.apple.com on 2026-10-14 (Liquid Glass era, iOS/iPadOS/macOS 27 generation). The full-text renders live in `hig/technologies/<slug>.md`; this digest keeps every rule and every number from those pages but drops examples, artwork captions, video descriptions, and connective prose. Each page lists its platforms as given in the source header, its rules as terse imperatives (Apple's bolded guideline plus the essential condition), platform-specific notes, every numeric table reproduced verbatim, and the frameworks/APIs the page links to.

## Live Photos
Full page: hig/technologies/live-photos.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS
A Live Photo bundles audio and extra frames captured before and after a still; people press it to see it spring to life. Integrate when your app displays, edits, or shares library photos.

**Rules**
- Apply adjustments to all frames — effects or adjustments must cover the entire Live Photo; if unsupported, offer conversion to a still photo.
- Keep Live Photo content intact — never disassemble a Live Photo and present frames or audio separately; use the same visual treatment and interaction model as other apps.
- Implement a great photo sharing experience — let people preview the entire contents before sharing; always offer sharing as a traditional photo.
- Clearly indicate when a Live Photo is downloading and when it is playable — progress indicator during download, an indication when complete.
- Display Live Photos as traditional photos in environments that don't support them — show a still; don't replicate the Live Photos experience.
- Make Live Photos easily distinguishable from still photos — best signal is a hint of movement; there are no built-in motion effects, so design and implement custom ones.
- When movement isn't possible, show the system-provided badge above the photo (with or without text); never a playback button that could read as video playback.
- Keep badge placement consistent — same location on every photo, typically a corner.

**Platform notes**
- iOS/iPadOS/macOS/tvOS: no additional considerations · visionOS: people can view a Live Photo but can't capture one · watchOS: not supported.

**Dev refs**
PHLivePhoto (PhotoKit), LivePhotosKit JS

## Mac Catalyst
Full page: hig/technologies/mac-catalyst.md · Platforms: iPadOS, macOS
Mac Catalyst builds a Mac version of an iPad app. Use it when the iPad app already works well with drag and drop, keyboard navigation, multitasking, and multiple windows.

**Rules**
- Start from an iPad app that already works well on iPad and supports key iPad features:
  - Drag and drop — carries over to the Mac version automatically.
  - Keyboard navigation and shortcuts — Mac users expect both.
  - Multitasking — scaling for Split View, Slide Over, and Picture in Picture lays the groundwork for the window resizability Mac users expect.
  - Multiple windows — supporting multiple scenes on iPad gives multiple windows in macOS.
- Reconsider if essential features need gyroscope, accelerometer, rear camera, HealthKit, or ARKit, or if the primary function is marking, handwriting, or navigation — the app may not suit the Mac.
- Rely on automatic macOS support for pointer interactions and keyboard focus/navigation, window management, toolbars, rich text interaction (copy and paste, editing contextual menus), file management, menu bar menus, and app settings in the system Settings app.
- Expect system elements to take a more Mac-like appearance automatically — split view, file browser, activity view, form sheet, contextual actions, color picker.
- Choose an idiom — the iPad idiom (Xcode default, "Scale Interface to Match iPad") scales iPadOS views and text to 77% in macOS (17pt baseline text becomes 13pt); the Mac idiom renders text and artwork at 100%, gives some elements a more Mac-like look, and can improve performance and power use for graphics-intensive apps.
- Switch to the Mac idiom when the app shows lots of text, detailed artwork, or animations — expect extra work on layout, text, and images.
- When you adopt the Mac idiom, thoroughly audit layout and plan changes — consider a separate asset catalog for the Mac app's assets.
- Adjust font sizes as needed under the Mac idiom — text renders at 100% and can look too large; prefer text styles over fixed font sizes.
- Make sure views and images look good under the Mac idiom — views render at 100% and show more detail.
- Avoid fixed font, view, or layout sizes — unscaled Mac-idiom elements report different metrics, which otherwise means significant extra work.
- Limit appearance customizations to standard macOS customizations that are the same or similar to iPadOS — not all iPadOS control customizations exist on macOS.
- Go beyond displaying the iPadOS layout in a macOS window — learn the platform conventions before updating views and controls.
- Know the iPad navigation components you're translating — split views (two or three columns: primary, optional supplementary, secondary content pane; sidebar changes drive the other columns), tab bars (flat top-level categories in a persistent bottom bar), page controls (dots for a flat list of pages).
- Replace a tab bar with a split view and sidebar (preferred: each tab's contents live in the sidebar; top-level items disclose children; consistent layout across iPad and Mac) or a segmented control (similar mutually exclusive selection; works on Mac for a flat hierarchy).
- Make sure people retain access to important tab-bar items — list top-level items in the macOS View menu.
- Offer multiple ways to move between pages — Next and Previous buttons in addition to swipe gestures, for pointer and keyboard users.
- Create a macOS version of your app icon — lifelike macOS rendering style, harmonious with other platforms.
- Update layout for the wider Mac screen:
  - Divide a single column of content and actions into multiple columns.
  - Use the regular-width and regular-height size classes, and reflow content-area elements side by side as people resize the window.
  - Present an inspector next to the main content instead of in a popover.
- Consider moving controls from the main iPad UI to the Mac window toolbar — and list their commands in the menu bar.
- Adopt a top-down flow — most important actions and content near the top of the window; iPad toolbar controls go in the window toolbar.
- Relocate buttons from the side and bottom screen edges — the iPad reachability rationale doesn't apply on Mac; move them elsewhere or into the toolbar.
- Put every command in the menu bar — Mac users expect it; use UIKeyCommand for shortcuts, UIMenuBuilder and UICommand for custom menus.
- Pop-up and pull-down button menus and context menus convert automatically — look for additional places to add context menus, since Mac users expect every object to offer one.
- Note that the system sends the two touches of pinch and rotate gestures to the view under the pointer, not the view under each touch.

**Specs**

| iPadOS gesture… | Translates to mouse interaction |
|---|---|
| Tap | Left or right click |
| Touch and hold | Click and hold |
| Pan | Left click and drag |

| iPadOS gesture… | Translates to trackpad gesture |
|---|---|
| Tap | Click |
| Touch and hold | Click and hold |
| Pan | Click and drag |
| Pinch | Pinch |
| Rotate | Rotate |

| Idiom scaling | Value |
|---|---|
| iPad idiom view/text scale in macOS | 77% (17pt → 13pt) |
| Mac idiom view/text scale | 100% |

**Platform notes**
- iPadOS/macOS: no additional considerations · iOS/tvOS/visionOS/watchOS: not supported.

**Dev refs**
Mac Catalyst (UIKit), UIKit Catalog, Choosing a user interface idiom for your Mac app, UIKeyCommand, UIMenuBuilder, UICommand, Adding menus and shortcuts to the menu bar and user interface

## Machine learning
Full page: hig/technologies/machine-learning.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Design guidance for features whose behavior comes from models — curated feeds, recommendations, personalization, recognition. Pairs with the Generative AI page for model-driven intelligent experiences.

**Rules**
- Design models with the intended app experience in mind — adjusting model behavior takes a long time, so be ready to change data use and metrics if the experience changes.
- Design the experience by teaching the app how to interpret data and react — you can't script reactions to a static set of scenarios.
- Define the role of ML in each feature along five axes, then use the input/output patterns below:
  - Critical or complementary — if the app still works without the feature, ML is complementary; the more central the feature, the more people expect accurate, reliable results.
  - Private or public — the more sensitive the data, the more serious the consequences of inaccurate results; sensitive-data features must prioritize accuracy and reliability; all apps must protect privacy at all times.
  - Proactive or reactive — proactive results arrive unrequested, so people tolerate low quality less; you may need additional data to avoid intrusive or irrelevant results.
  - Visible or invisible — people judge a visible feature's reliability as they choose from its results; an invisible feature struggles to communicate reliability or receive feedback.
  - Dynamic or static — dynamic features improve as people interact and often use calibration and feedback; static features improve offline and only with app updates.
- Explicit feedback (note: favoriting and social feedback are implicit, not explicit, because they serve people's own goals):
  - Request explicit feedback only when necessary — prefer implicit feedback that costs people no extra work.
  - Always make providing explicit feedback voluntary.
  - Use simple, direct language for each option and its consequences — avoid imprecise terms like *dislike*; prefer "Suggest less pop music", "Suggest more thrillers", "Mute politics for a week".
  - Add icons to an option description if it helps — never an icon by itself.
  - Consider offering multiple, progressively more specific options.
  - Act immediately on explicit feedback and persist the change — hide rejected content everywhere in the app.
  - Consider using explicit feedback to tune when and where you show results.
- Implicit feedback:
  - Always secure people's information — maintain strict privacy controls.
  - Help people control their information — tell them how the app gets and shares it and let them restrict the flow; cross-app effects surprise people.
  - Don't let implicit feedback decrease opportunities to explore — pure reinforcement worsens the long-term experience.
  - Use multiple feedback signals to improve suggestions and mitigate mistakes — a single action (view, share, add to album) doesn't reveal intent.
  - Consider withholding private or sensitive suggestions — devices and accounts are shared.
  - Prioritize recent feedback — fall back to historical feedback when recent isn't available.
  - Update predictions on a cadence that matches the person's mental model — typing suggestions update instantly; continuously changing song recommendations feel rushed.
  - Be prepared for implicit feedback to change when you change the UI — even moving a button changes usage.
  - Beware of confirmation bias — implicit feedback can't reveal new things people might like; don't rely on it alone.
- Calibration (use only when the feature can't function without initial information):
  - Always secure the information people provide.
  - Be clear about why you need the information — emphasize what the feature does, not how it works.
  - Collect only the most essential information.
  - Avoid asking people to calibrate more than once, and calibrate early — evolve via feedback afterward; exception: calibrating with an object (e.g., each new baseball field).
  - Make calibration quick and easy — easy to respond to without compromising information quality:
    - Prioritize a few pieces of important information and infer the rest from other sources or feedback.
    - Avoid asking for information most people would have to look up.
    - Avoid asking people to perform actions that might be difficult.
  - Make sure people know how to succeed — give an explicit goal and show progress (as Face ID's tick marks do).
  - Immediately provide assistance if progress stalls — actionable recommendations; never imply fault; never leave people without a next step.
  - Confirm success — give a clear path into the feature.
  - Let people cancel at any time — no judgment and no messaging about the cancellation.
  - Give people a way to update or remove calibration information — ideally outside the calibration experience as well.
- Mistakes:
  - Anticipate mistakes — design ways to avoid them and mitigate them when they happen.
  - Help people handle mistakes — the tools you provide must address the full range of consequences.
  - Learn from mistakes when doing so improves the app — but not when learning would make the experience unpredictable.
  - Use the patterns that address mistakes — limitations set accuracy expectations; corrections let people succeed despite wrong results; attribution explains where suggestions come from; confidence gauges result quality; explicit and implicit feedback reveal mistakes you don't know about.
  - Understand the significance of a mistake's consequences — match corrective tools to the seriousness (keyboard suggestion vs. missed flight).
  - Make it easy to correct frequent or predictable mistakes.
  - Continuously update the feature for evolving interests and domain trends — people shouldn't have to work to benefit.
  - Address mistakes without complicating the UI — corrections and limitations integrate easily; a wrong attribution magnifies the original mistake.
  - Be especially careful to avoid mistakes in proactive features — less patience, less perceived control.
  - When reducing mistakes in one area, consider the effect on other areas and overall accuracy (better dog recognition may worsen cat recognition).
- Corrections:
  - Give people familiar, easy ways to make corrections — show the steps the automation took (Photos highlights the controls it used to auto-crop).
  - Provide immediate value when people correct — show corrected content instantly and persist it.
  - Let people correct their corrections — respond immediately and persist.
  - Balance the feature's benefit against correction effort — people abandon a feature if doing the task themselves is easier.
  - Never rely on corrections to make up for low-quality results.
  - Learn from corrections when it makes sense — verify the correction will raise quality before using it to update models.
  - Prefer guided corrections (specific alternatives, e.g., speech-to-text completions) over freeform (Photos crop adjustment); combine both if appropriate.
- Multiple options (suggested, requested, or correction options):
  - Prefer diverse options — balance accuracy with diversity (Maps: no tolls, scenic, highways).
  - Avoid too many options — more options raise cognitive load; list them on one screen without scrolling.
  - List the most likely option first — rank by confidence once you know it correlates with quality, plus context (time, location); select it by default when sensible.
  - Make options easy to distinguish and choose — brief descriptions that highlight differences; group many options into scannable categories.
  - Learn from selections when it makes sense — continuing to offer incorrect results erodes trust.
- Confidence:
  - Verify that confidence values correspond to result quality (across thresholds and app versions) before conveying them — if unsure, don't convey confidence.
  - Know what your confidence values mean before deciding how to present them — prominent low-quality results erode trust.
  - Translate confidence into concepts people understand — "Because you listen to pop music" is actionable; "97% match" isn't.
  - Where attributions don't help, rank or order results to imply confidence, or use semantic categories ("high chance", "low chance").
  - Display numeric confidence where people expect statistics — weather, sports, polling.
  - Convey confidence as actionable suggestions whenever possible — "This is a good time to buy", "Consider waiting for a better price".
  - Consider changing presentation at different confidence thresholds — Photos shows faces directly at high confidence and asks for confirmation at lower confidence.
  - Avoid showing results when confidence is low — set a threshold for suggestions and proactive features.
- Attribution (the basis for a result, without explaining the model):
  - Decide whether attributions should change behavior, minimize mistakes, build a mental model, or promote trust.
  - Use attributions to help people distinguish among multiple options ("New books by authors you've read").
  - Avoid being too specific (feels like surveillance) or too general (feels impersonal).
  - Keep attributions factual and objective — "Because you've read nonfiction", not "Because you love nonfiction"; never imply judgment of emotions or beliefs.
  - Avoid technical or statistical jargon — except when the result itself is statistical (weather, sports, polling, science).
- Limitations (things a feature can't do well and things it can't do at all):
  - Help people establish realistic expectations — disclose rare-but-serious limitations before use (marketing or in context); use attributions for minor ones.
  - Demonstrate how to get the best results — otherwise people assume the feature does everything they want:
    - Use placeholder text to suggest input (Photos search shows "Photos, People, Places…" and describes how it scans the library).
    - Give feedback on people's actions as they interact, without overwhelming them (Memoji suggests adjusting lighting or moving closer to the camera).
    - Suggest alternative ways to accomplish the goal instead of showing no results — this requires understanding the goal.
  - Explain how limitations cause unsatisfactory results — recognize and describe the reason (Memoji says it doesn't work well in the dark).
  - Consider telling people when limitations are resolved — so they return to interactions they'd avoided.

**Platform notes**
- No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

**Dev refs**
Create ML, Core ML, Apple Intelligence and machine learning (Technology Overviews); related HIG: Generative AI, Privacy, Icons

## Maps
Full page: hig/technologies/maps.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
A map shows outdoor or indoor geographic data in an app or website with standard, satellite, or hybrid views, annotations, overlays, routing, and place cards. Integrate for store locators, venue maps, trip planning, and anything location-based.

**Rules**
- In general, make your map interactive — people expect zoom, pan, and rotation; noninteractive elements that obscure the map break expectations.
- Pick an emphasis style — *default* (fully saturated, aligns with the Maps app when people switch between them) or *muted* (desaturated, lets information-rich custom content stand out).
- Help people find places — search combined with category filters.
- Clearly identify selected elements — distinct styling such as an outline and color variation.
- Cluster overlapping points of interest — one pin represents nearby POIs and expands progressively on zoom.
- Help people see the Apple logo and legal link — parts of your interface may cover them temporarily, never permanently:
  - Use adequate padding to separate them from map boundaries and custom controls — 7 points on the sides and 10 points above and below works well.
  - Don't let the logo and link move with your interface — they should appear fixed to the map.
  - If a custom element can move relative to the map (e.g., a pull-up card), place the logo and link 10 points above its lowest resting position.
- Note the Apple logo and legal link aren't shown on maps smaller than 200x100 pixels.
- Use annotations that match your app's visual style — default marker is a red tint with a white pin; change the tint and swap the icon for an image or a string; keep icon strings to two or three characters.
- Consider making standard map features (Apple POIs, territories, physical features) independently selectable — give them custom appearance and information.
- Use overlays to define areas related to your content — *above roads* (default; below buildings and trees) or *above labels* (hides everything beneath; for abstracted or irrelevant areas).
- Make sure there's enough contrast between custom controls and the map — thin stroke, light drop shadow, or blend modes on the map.
- Present a place card in the map when someone selects a place you specify (e.g., a map of an author's tour stops) — and optionally for Apple points of interest, territories, and physical features to give context about nearby places.
- Choose a place card style — it sets size, appearance, and included information:
  - *automatic* — the system picks based on the map view's size.
  - *callout* — a popover next to the place; *full* (large, detailed) or *compact* (space-saving, concise); an unspecified callout style defaults to *automatic*, chosen by view size.
  - *caption* — an "Open in Apple Maps" link.
  - *sheet* — a place card in a sheet.
- Expect the full callout to render as a popover on iPadOS and macOS and as a sheet on iOS.
- On websites you can embed a custom map that shows a place card by default for a single place (Maps Embed API).
- Consider your map presentation when choosing a style — full callout is richest; use compact callout for a small map with many annotations.
- Make place cards look good on different devices and window sizes — set a minimum width on full callouts so text doesn't overflow.
- Avoid duplicating information your app already shows — compact callout or caption may complement better.
- Keep the selected location visible when a place card displays — set an offset and point the card at the location.
- Place cards outside a map (search results, store locators): if the card isn't inside a map view, you must include a map in the place card.
- Use location cues in surrounding content (place name, address, details button, or a map pin icon) to signal that a place card can open.
- Indoor maps: adjust detail by zoom level — rooms and buildings at all levels; stores and restrooms as people zoom in.
- Indoor maps: use distinctive styling — color plus icons to distinguish areas, stores, services.
- Indoor maps: offer a floor picker for multiple levels — concise floor numbers rather than names.
- Indoor maps: include surrounding areas for context — dim noninteractive areas with a distinct color.
- Indoor maps: consider routing to nearby transit (bus stops, stations, parking) and a quick switch to Apple Maps.
- Indoor maps: limit scrolling outside the venue — keep part of the map visible at all times; adjust the limit by zoom level.
- Indoor maps: make the map a natural extension of your app — don't replicate Apple Maps; match overlays, icons, and text to your style; use IMDF.

**Platform notes**
- watchOS: maps are static snapshots placed at design time with the region set at runtime; not interactive — tapping opens the Maps app; up to five annotations. Fit the map element to the screen without scrolling; show the smallest region that encompasses the points of interest (content doesn't scroll).

**Specs**

| Measurement (from text) | Value |
|---|---|
| Padding around Apple logo and legal link | 7 points on the sides, 10 points above and below |
| Logo and legal link above a movable custom element | 10 points above its lowest resting position |
| Logo and legal link hidden when map is smaller than | 200x100 pixels |
| Annotation icon string length | 2–3 characters |
| watchOS annotations per map | up to 5 |

**Dev refs**
MapKit, MapKit JS, Indoor Mapping Data Format (IMDF), MKStandardMapConfiguration.EmphasisStyle, MKAnnotationView, MKMapFeatureOptions, MKOverlayLevel, Displaying overlays on a map, mapItemDetailSelectionAccessory(_:), mapFeatureSelectionAccessory(_:), mapView(_:selectionAccessoryFor:), selectionAccessory, selectableMapFeatureSelectionAccessory, MapItemDetailSelectionAccessoryStyle, MKSelectionAccessory.MapItemDetailPresentationStyle, PlaceSelectionAccessoryStyle, offset(_:), accessoryOffset, selectionAccessoryOffset, mapItemDetail(_:), PlaceDetail, mapItemDetailSheet(item:displaysMap:), MKMapItemDetailViewController, Maps Embed API, WKInterfaceMap

## NFC
Full page: hig/technologies/nfc.md · Platforms: iOS, iPadOS
Near-field communication lets a device read electronic tags on real-world objects from a few centimeters away — toys, in-store signs, inventory. Apps scan in-app via a scanning sheet or, on supported devices, in the background.

**Rules**
- Don't encourage people to make contact with physical objects — proximity is enough; use *scan* and *hold near*, not *tap* and *touch*.
- Use approachable terminology — avoid *NFC*, *Core NFC*, *Near-field communication*, and *tag*; name the object instead.
- Provide succinct instructional text for the scanning sheet — one complete sentence in sentence case with ending punctuation; identify the object; revise for subsequent scans; keep short to avoid truncation.
- Support both background and in-app tag reading — in-app scanning is mandatory for devices without background reading.
- Understand background tag reading — on supported devices the system looks for compatible tags whenever the screen is illuminated and shows a notification people tap to send the tag data to your app; it is unavailable when:
  - an NFC scanning sheet is visible
  - Wallet or Apple Pay is in use
  - cameras are in use
  - the device is in Airplane Mode
  - the device is locked after a restart

**Platform notes**
- iOS/iPadOS: no additional considerations · macOS/tvOS/visionOS/watchOS: not supported.

**Specs**

| Use | Don't use |
|---|---|
| Scan the [*object name*]. | Scan the NFC tag. |
| Hold your iPhone near the [*object name*] to learn more about it. | To use NFC scanning, tap your phone to the [*object*]. |

| First scan | Subsequent scans |
|---|---|
| Hold your iPhone near the [*object name*] to learn more about it. | Now hold your iPhone near another [*object name*]. |

**Dev refs**
Core NFC

## Photo editing
Full page: hig/technologies/photo-editing.md · Platforms: iOS, iPadOS, macOS
A photo-editing extension lets people apply your filters or edits inside the Photos app while in edit mode; it loads in a modal view with a system toolbar, and edits save as new files that preserve the original.

**Rules**
- Confirm cancellation of edits — on Cancel, ask for confirmation and say edits will be lost; skip the confirmation if nothing has been edited.
- Don't provide a custom top toolbar — the host modal already includes one; a second toolbar confuses and steals space.
- Let people preview edits — show the result before they close the extension and return to Photos.
- Use your app icon for the extension icon — confirms the extension comes from your app.
- Remember the host flow: the extension appears in edit mode's action menu; dismissing the modal confirms and saves or cancels back to Photos.

**Platform notes**
- iOS/iPadOS/macOS: no additional considerations · tvOS/visionOS/watchOS: not supported.

**Dev refs**
App extensions, PhotoKit

## ResearchKit
Full page: hig/technologies/researchkit.md · Platforms: iOS, iPadOS
ResearchKit provides predesigned screens and transitions for medical research apps: onboarding, consent, surveys, active tasks, profile, and dashboards. (The page states it is informational only and not legal advice.)

**Rules**
- Always display the onboarding screens in the correct order — 1 Introduction, 2 Eligibility, 3 Informed consent, 4 Data-access permission; they're rarely revisited, so clarity is essential.
- Provide an introduction that informs and gives a call to action — describe the study's subject and purpose; let existing participants log in and continue quickly.
- Determine eligibility as soon as possible — only necessary requirements, in simple language, with easy data entry; ineligible people never reach consent.
- Make sure participants understand your study before consent — comply with App Store Guidelines consent requirements and any IRB/ethics board requirements; explain how the study works and the participant's responsibilities.
- Break a long consent form into digestible sections — one aspect each (data gathering, data use, benefits, risks, time commitment, how to withdraw); high-level overview per section with a Learn More button for detail; the entire form must be viewable before agreeing.
- If it makes sense, provide a quiz that tests understanding — for questions normally asked when consenting in person.
- Get consent and, if appropriate, contact information — confirmation dialog, then signature and contact screens; most apps email a PDF of the consent.
- Get permission to access device data and to send notifications — explain why you need location, Health, or other data; don't request anything not critical to the study.
- Create surveys that keep participants engaged — ResearchKit supplies screens for true/false, multiple choice, dates and times, sliding scales, and open-ended text:
  - Tell participants how many questions there are and about how long the survey will take.
  - Use one screen per question.
  - Show participants their progress in the survey.
  - Keep the survey as short as possible — several short surveys work better than one long one.
  - For questions needing explanation, use the standard font for the question and a slightly smaller font for the explanatory text.
  - Tell participants when the survey is complete.
- Make active tasks (speaking into the microphone, tapping fingers, walking, memory tests) easy to understand:
  - Describe how to perform the task in clear, simple language.
  - Explain any requirements, such as a particular time or specific circumstances.
  - Make sure participants can tell when the task is complete.
- Use a profile to help participants manage personal data — edit changing data (weight, sleep), see upcoming activities, leave the study, view the consent document and privacy policy.
- Use a dashboard to show progress and motivate — daily progress, weekly assessments, activity results, comparison with aggregated study results.
- Keep the profile and dashboard accessible at all times in the app.

**Platform notes**
- iOS/iPadOS: no additional considerations · macOS/tvOS/visionOS/watchOS: not supported.

**Dev refs**
ResearchKit (Research & Care), ResearchKit GitHub project, Protecting user privacy (HealthKit)

## SharePlay
Full page: hig/technologies/shareplay.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS
SharePlay keeps an app activity in sync across participants' devices alongside FaceTime or Messages — watching, gaming, sketching together. Activities start from an in-app control, a FaceTime call, or a shared link.

**Rules**
- Use SharePlay for real-time experiences — for asynchronous collaboration, let people share or save the activity after the session (e.g., a Freeform link).
- Design the experience to fit what people do together — one shared view for watching or browsing; per-role views for a game.
- Design activities that work across Apple platforms — different devices, settings, and communication methods.
- Make it easy to start — a clear control such as a button with the SharePlay symbol; also the share sheet; in visionOS the Share button next to the window bar.
- Let people join without friction — reach shared content quickly; present sign-in, download, or subscription in a view that dismisses on completion; offer provisional access or Family Sharing for nonsubscribers; defer nonessential steps (profiles after joining a match).
- Remember each participant needs their own copy or subscription of paid content — the system prompts download or subscription.
- Describe activities clearly and concisely — title, short summary, poster image; brief enough to avoid truncation.
- Keep people oriented as the activity changes — the system coordinates media playback (one pause pauses everyone); for other changes show who's doing what (Freeform shows initials).
- Use the term *SharePlay* correctly — as a noun ("Join SharePlay") or a verb ("SharePlay Movie" button); never with an adjective (*virtual*, *spatial*); never altered (*SharePlayed*, *SharePlays*, *SharePlaying*).
- iOS/iPadOS/macOS: support Picture in Picture for shared video — PiP window on iPhone and iPad; a window people bring forward on Mac.
- visionOS: standard windows share via screen mirroring with the Share button by default; adopt SharePlay to share volumetric windows and immersive content.
- visionOS: align windows and volumes across devices in the shared context — position 3D objects, play sounds, and support interactions so people feel together.
- visionOS: prefer starting from a window — an immersive-space start needs custom UI.
- visionOS: resolve conflicts naturally — no "take control" UI for single-user tools; let people speak or gesture; use a simple rule like last change wins.
- visionOS: reserve unique views for moments that call for them — when someone enters a personal immersive view, replace their spatial Persona with a contact photo and keep FaceTime Audio going.
- visionOS: let people opt in to immersion changes mid-task — if a change would interrupt someone, show a prompt with a join option; everyone else transitions immediately.
- visionOS: keep comfort and accessibility settings (volume, subtitles) unique to each participant.
- visionOS: make it easy to leave and rejoin — clear rejoin control; a windowed version lets people multitask while staying connected.
- visionOS Personas: remote Vision Pro users appear as spatial Personas (contact photo if none); iPhone, iPad, Mac, and Apple TV users appear in a 2D video window; co-located Vision Pro users see each other through passthrough with content in the same physical place.
- visionOS: support people who aren't represented by a spatial Persona — offer UI alternatives when the experience relies on facial expressions or gestures.
- visionOS spatial templates: adopt the system template that fits the activity, or create a custom one — each person gets a seat that sets where they appear and which way they face:
  - *side-by-side* — ideal for viewing or watching; participants along a curve all facing the content; less nonverbal interaction, focus stays on the content.
  - *surround* — ideal for tabletop games and centralized experiences; participants in a circle around the content; works especially well for 3D or per-participant content; encourages verbal and nonverbal interaction.
  - *conversational* — participants around a center point with the content along the circle's edge; not everyone sees the content equally, so use it when the app works in the background (e.g., playing music).
- visionOS: divide a complex activity into stages — one template per stage; prefer mixing system and custom templates over one complex custom template.
- visionOS: let people initiate template transitions — tie seat and role changes to an explicit action (choosing a team).
- visionOS: keep template transitions smooth — avoid frequent or large moves; fade out and in; give reorientation cues.
- visionOS custom templates: seats apply only to spatial Personas; other participants take part without a seat.
- visionOS: account for people who are physically together — a template can't move them; guide with position markers.
- visionOS: provide the best seat orientation — seats face the content center by default; direction is fully controllable.
- visionOS: support the maximum number of seats — five spatial Personas per activity; define every seat up front; keep a seat after someone leaves; add spectator seats when the activity has a participant limit.
- visionOS: place seats at least a meter apart — a Persona that gets too close to another is replaced with a contact photo.
- visionOS: define seat fill order — seats fill in join order; order them so a partly filled arrangement stays balanced (not simply left to right).
- visionOS: keep roles independent of seats — roles must work for unseated participants; let people fill any open seat; reserve a spot only for a role that needs it (a host at the head of the table).

**Platform notes**
- tvOS: no additional considerations · watchOS: not supported.

**Specs**

| Limit (from text) | Value |
|---|---|
| Spatial Personas per activity on Apple Vision Pro | up to 5 |
| Minimum spacing between seats | 1 meter |

**Dev refs**
Group Activities, Adding shared content collaboration to your app (Shared with You), Presenting SharePlay activities from your app's UI, Synchronizing data during a SharePlay activity, Implementing SharePlay for immersive spaces in visionOS, Adding spatial Persona support to an activity, Configure your visionOS app for sharing with people nearby, SystemCoordinator.Configuration.SpatialTemplatePreference, SpatialTemplateSeatElement, ParticipantState.isSpatial, Participant.isNearbyWithLocalParticipant, Building a guessing game for visionOS

## ShazamKit
Full page: hig/technologies/shazamkit.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
ShazamKit matches audio samples against the Shazam catalog or a custom catalog — for genre-matched visuals, synced captions or sign language, or syncing in-app content with external audio.

**Rules**
- Request microphone access only when you need samples, and explain why (see Privacy).
- Stop recording as soon as possible — record only as long as it takes to get the sample.
- Let people opt in to storing recognized songs in their iCloud library — ask first even though the Music Recognition control and Shazam app attribute the song to your app.

**Platform notes**
- No additional considerations on any platform.

**Dev refs**
ShazamKit

## Sign in with Apple
Full page: hig/technologies/sign-in-with-apple.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS (and web/non-Apple platforms)
Sign in with Apple lets people sign in or sign up with their Apple Account, Face ID/Touch ID/Optic ID, built-in two-factor authentication, and an optional private relay email. Offer it anywhere you offer account sign-in.

**Rules**
- Ask people to sign in only in exchange for value — briefly describe the benefits (personalization, extra features, sync).
- Delay sign-in as long as possible — let people explore before committing.
- If you require an account, explain why and have people set it up before offering sign-in options — then offer Sign in with Apple and any other methods.
- Consider letting people link an existing account to Sign in with Apple — keeps existing data while adding convenience; offer linking before or after people sign in to the existing account:
  - if the email shared through Sign in with Apple matches an existing account, suggest linking to it
  - if people signed in with an existing user name and password, show a linking suggestion in account settings or another logical place
- In a commerce app, ask for an account after the purchase — e.g., on the order confirmation page after Apple Pay; don't re-ask for name and email already provided.
- Welcome people to their new account as soon as sign-in completes — don't delay with requests for non-required information.
- Indicate when people are signed in — e.g., "Using Sign in with Apple" in settings or account views.
- Clarify whether additional data is required or recommended — legally/contractually required data (terms agreement, country or region, birth date, real-identity-law data) must be stated as required; optional data must be labeled optional with its benefit.
- Don't ask people to supply a password — unless they've stopped using Sign in with Apple with your app.
- Avoid asking for a personal email address when people supply a private relay address — respect the choice; for customer service or retail flows that identify by email you can:
  - make sure people can view their private relay address in your app or website
  - direct people to Settings > Apple Account > Password & Security > Apps using Apple Account to retrieve it
  - use other identifying values, like an order number or a phone number collected during purchase
- Give people a chance to engage before asking for optional data — and never block the account or features if they decline.
- Be transparent about collected data — welcome people with the shared name or email (shows where the relay address lives); don't collect data you never display.
- Prominently display a Sign in with Apple button — no smaller than other sign-in buttons; never require scrolling to see it.
- Prefer the system-provided buttons — Apple-approved appearance, correct proportions across styles, automatic title translation, configurable corner radius (iOS, macOS, web), and a VoiceOver label.
- Use the button titles Sign in with Apple, Sign up with Apple, or Continue with Apple (iOS, macOS, tvOS, web) consistently; watchOS provides one title, "Sign in".
- Choose the button appearance by background — up to three options depending on platform:
  - *White* — all platforms and the web; use on dark backgrounds that provide sufficient contrast.
  - *White with outline* — iOS, macOS, and the web; use on white or light backgrounds that don't contrast with a white fill; avoid on dark or saturated backgrounds (the black outline adds clutter — use white instead).
  - *Black* — all platforms and the web; use on white or light backgrounds with sufficient contrast; don't use on black or dark backgrounds.
- Note the watchOS black button uses the system dark gray fill, not pure black, to contrast with the watch's black background.
- Adjust the corner radius to match other buttons — from square corners to capsule (iOS, macOS, web).
- Maintain the minimum button size and margin (iOS, macOS, web) — titles vary in length by locale; see Specs.
- Custom buttons (iOS, macOS, web): make them instantly identifiable as Sign in with Apple — App Review evaluates every custom button.
- Use only the Apple logo artwork from Apple Design Resources (PNG, SVG, PDF; black and white; logo-only and logo-plus-text variants with built-in padding); never create a custom Apple logo.
- Follow the logo-file rules when building a custom button:
  - Use the logo file to position the Apple logo in a button; never use the Apple logo as a button.
  - Match the height of the logo file to the height of the button.
  - Don't crop the logo file.
  - Don't add vertical padding.
- Don't change these attributes (they keep custom buttons consistent with the system button):
  - Titles — use only *Sign in with Apple*, *Sign up with Apple*, or *Continue with Apple*.
  - General shape — logo-plus-text buttons are always rectangular; logo-only buttons can be circular or rectangular.
  - Logo and title colors — both black or both white within a button; no custom colors.
- You may change these to coordinate with your design:
  - Title font, including weight and size.
  - Title case — you can capitalize every letter.
  - Background appearance — the overall color stays black or white; a subtle texture or gradient is allowed.
  - Button corner radius — match the other buttons in your UI.
  - Button bezel and shadow — e.g., a stroke to emphasize the bezel or a drop shadow.
- Logo-plus-text buttons: choose the logo format by button height — SVG/PDF for any height; PNG only for 44pt-tall buttons (iOS default and recommended height); logos come in small, medium, and large to match other sign-in buttons.
- Prefer the system font for the title; keep the system proportions — title font size is 43% of button height (button height is 233% of font size, rounded to the nearest integer).
- Preserve the title's capitalization (*Sign*/*Continue* and *Apple* capitalized, rest lowercase) unless your interface uses only uppercase.
- Keep the title and logo vertically aligned — center the title vertically, then add the logo at the button's height (its padding keeps alignment).
- Inset the logo if necessary to align with other authentication logos — adjust the space from the leading edge.
- Keep at least 8% of the button's width as margin between the title and the right edge.
- Logo-only buttons: SVG/PDF for any size; PNG only at 44x44 pt; always a 1:1 aspect ratio; don't add horizontal padding (artwork already includes it).
- Use a mask (circle or rounded rectangle) to change a logo-only button's square shape — never crop the artwork to reduce padding, use the logo by itself, or add padding.
- Keep a margin of at least 1/10 of the button's height around logo-only buttons.

**Platform notes**
- No additional considerations on any platform.

**Specs**

System-provided and custom logo-plus-text buttons (iOS, macOS, web):

| Minimum width | Minimum height | Minimum margin |
|---|---|---|
| 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button's height |

| Custom-button proportion (from text) | Value |
|---|---|
| Title font size relative to button height | 43% |
| Button height relative to title font size | 233%, rounded to nearest integer |
| Minimum margin between title and right edge | 8% of button width |
| PNG logo artwork intended button height | 44 pt (logo+text); 44x44 pt (logo-only) |
| Logo-only button aspect ratio | 1:1 |
| Minimum margin around logo-only button | 1/10 of button height |

**Dev refs**
Authentication Services, ASAuthorizationAppleIDButton (iOS, macOS, tvOS), WKInterfaceAuthorizationAppleIDButton (watchOS), Displaying Sign in with Apple buttons on the web, ASAuthorizationAppleIDButton.cornerRadius, Sign in with Apple button (appleid.apple.com live previews), Apple Design Resources

## Siri
Full page: hig/technologies/siri.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
Siri, powered by Apple Intelligence on supported devices, runs app actions from anywhere in the system, works with onscreen content, and reaches deep features. Apps expose actions (intents) and content (entities) via App Intents, optionally mapped to app schemas.

**Rules**
- Make features and content available through App Intents — intents and entities surface in Siri, Spotlight, and Shortcuts.
- Adopt app schemas when your app fits a known domain (email, music, photos) — built-in logic, wider request handling, natural conversation, deeper context.
- Annotate onscreen views and content with app entities — lets Siri resolve references to what the person is looking at.
- Donate entities to the on-device Spotlight index — makes content searchable in Spotlight and Siri.
- Donate actions people take as intents — helps Siri anticipate and surface future actions (recent activity, items of interest).
- Identify your app's most popular actions and when and where they occur — prioritize which intents and entities to expose (hands-free contexts, specific devices).
- Use familiar terms for content and actions — pick the terminology people recognize (track vs. song vs. podcast).
- Offer relevant content — recent searches, favorites, bookmarks, wishlists rather than everything; whole-catalog access is reasonable for categories like email or messaging.
- Don't advertise — no advertisements, marketing, or in-app purchase pitches in Siri-delivered content.
- Only provide a custom response if built-in responses don't meet your needs.
- Use App Shortcuts to expose custom actions when functionality falls outside the schema domains.
- Add optional intent/entity properties (e.g., a playback snippet) to enhance responses — but expect them to be omitted in non-visual contexts.
- Write response dialogue that's clear and descriptive — customize follow-up questions ("Which soup?" beats "Which one?").
- Keep responses as succinct as possible — drop details the conversation already covers; avoid filler and humor that grate on repetition.
- Provide responses Siri can deliver audibly and visually — the voice response must stand alone without visual elements.
- Design inclusive interactions — avoid unnecessary pronouns ("Who should I send it to?" rather than "What's his or her name?").
- Ask an open-ended question when the full option list is too long to read in a timely way.
- Keep responses device-independent — a request can start on one device and act on another; reference a device only when accurate in context.
- Omit your app name from responses — the system already attributes verbally and visually.
- Use appropriate language and respect parental controls — no offensive language; responses may be spoken aloud near others.
- Help people understand errors and failures — situation-specific messages ("Sorry, we're out of chicken noodle soup").
- Refer to Siri by name — never *she*, *him*, *her*; just *Siri*.
- Be aware the system reserves important actions and phrases for Siri — never impersonate Siri, reproduce Siri's functionality, or produce a response that appears to come from Apple.
- Don't use reserved phrases like "Call 911" or "Hey Siri".
- In a localized context, translate only *Hey* in "Hey Siri" — *Siri* is a trademark and is never translated; use the table below.

**Platform notes**
- No platform-specific section on this page.

**Specs**

| Locale code | "Hey Siri" translation | Locale code | "Hey Siri" translation |
|---|---|---|---|
| ar_AE | يا Siri | fr_CA | Dis Siri |
| ar_SA | يا Siri | fr_CH | Dis Siri |
| da_DK | Hej Siri | fr_FR | Dis Siri |
| de_AT | Hey Siri | it_CH | Ehi Siri |
| de_CH | Hey Siri | it_IT | Ehi Siri |
| de_DE | Hey Siri | ja_JP | Hey Siri |
| en_AU | Hey Siri | ko_KR | Siri야 |
| en_CA | Hey Siri | ms_MY | Hai Siri |
| en_GB | Hey Siri | nb_NO | Hei Siri |
| en_IE | Hey Siri | nl_BE | Hé, Siri |
| en_IN | Hey Siri | nl_NL | Hé Siri |
| en_NZ | Hey Siri | no_NO | Hei Siri |
| en_SG | Hey Siri | pt_BR | E aí Siri |
| en_US | Hey Siri | ru_RU | привет Siri |
| en_ZA | Hey Siri | sv_SE | Hej Siri |
| es_CL | Oye Siri | th_TH | หวัดดี Siri |
| es_ES | Oye Siri | tr_TR | Hey Siri |
| es_MX | Oye Siri | zh_CN | 嘿Siri |
| es_US | Oye Siri | zh_HK | 喂 Siri |
| fi_FI | Hei Siri | zh_TW | 嘿 Siri |
| fr_BE | Dis Siri |  |  |

**Dev refs**
App Intents, App schema domains, Apple Intelligence and Siri AI, Getting started with the App Intents framework, Making actions and content discoverable by Apple Intelligence, Providing contextual cues to Apple Intelligence and Siri, Defining app entities for your custom data types, Making app entities available in Spotlight, Donating your app's data and actions to the system, App Shortcuts, Displaying static and interactive snippets; related HIG: App Shortcuts, Snippets, Writing, Inclusion

## Tap to Pay on iPhone
Full page: hig/technologies/tap-to-pay-on-iphone.md · Platforms: iOS
Tap to Pay on iPhone lets merchants accept contactless payments in your iOS app without external hardware. Requires a supported payment service provider (PSP), the Tap to Pay on iPhone entitlement, and ProximityReader APIs (directly or via the PSP SDK); it works alongside existing hardware.

**Rules**
- Help merchants accept Tap to Pay on iPhone terms and conditions before customer-facing flows — acceptance must precede initial device configuration; offer accept buttons in in-app messaging or onboarding.
- Present the terms and conditions only to an administrative user — tell nonadministrators that admin access is required; let an admin accept via a web interface or a different app (even on non-iPhone devices).
- If your PSP requires specific iOS versions, present the terms only after the merchant updates the device.
- Provide a tutorial that describes the supported payment types and shows how to accept each — offer it:
  - as a Learn More option in your in-app messaging
  - automatically after merchants accept the terms and conditions
  - automatically to new users of your app
  - in a consistent, easy-to-find place like help content or settings
- Build the tutorial from Apple-approved assets in the Tap to Pay on iPhone marketing guidelines, or use ProximityReaderDiscovery for a prebuilt merchant education experience that Apple keeps up to date and localized for the merchant's region.
- If you design your own tutorial, make sure it shows how to:
  - launch a checkout flow for each type of payment
  - help a customer position their contactless card or digital wallet on the merchant's device
  - handle PIN entry for a card, including accessibility mode
- End the tutorial with an opportunity to accept the terms and conditions for merchants who haven't yet.
- Design the checkout flow (time-sensitive for merchants) to be ready to:
  - offer payment options in addition to Tap to Pay on iPhone, as necessary
  - respond quickly if a merchant starts checkout before enabling Tap to Pay on iPhone
  - help merchants check out even while device configuration is still in progress
  - present pre-payment actions that affect the final total before checkout completes
- Provide Tap to Pay on iPhone as a checkout option whether enabled or not — on tap, present the terms if needed and open the Tap to Pay screen automatically when configuration completes.
- Avoid making merchants wait — configure at app launch and immediately after every transition to the foreground (prepare(using:)).
- Keep the checkout option selectable while configuration continues in the background — show an indeterminate progress indicator, or a determinate one when the API reports configuration progress.
- Make the Tap to Pay button easy to find when you support multiple methods — no scrolling; if it's your only method, open Tap to Pay automatically when checkout begins.
- Make switching between Tap to Pay and hardware accessories easy — set both up together; let merchants pick the method at checkout without visiting settings.
- Label the activating button "Tap to Pay on iPhone" or, if space is constrained, "Tap to Pay" — reuse existing Charge/Checkout buttons only if Tap to Pay is your sole method; with icons, use SF Symbols `wave.3.right.circle` or `wave.3.right.circle.fill`; never include the Apple logo.
- Use the "Tap to Pay on iPhone" label only for payment actions.
- Match the button's color and shape to your other buttons — only the label is fixed.
- Determine the final amount (tips and other adjustments) before opening the Tap to Pay screen — aim to show the final amount there.
- Display pre-payment options (e.g., payment type selection) before the Tap to Pay screen.
- Start processing a transaction as soon as possible — request the read result before the checkmark animation finishes (returnReadResultImmediately).
- Show an authorization progress indicator after the Tap to Pay animation finishes and before your result screen — authorization can take several seconds.
- Clearly display declined or successful results — and offer digital receipts (QR code, text message).
- Help merchants complete checkout when a tap fails (card unreadable, unsupported payment network, amount not allowed, online PIN not allowed):
  - present a new screen or reuse the checkout screen to accept an alternate form of payment, like cash
  - support checkout with a different method, like external hardware or a payment link
  - relaunch Tap to Pay on iPhone if the customer has another card to try
- Be ready for post-tap scenarios — Strong Customer Authentication may require a PIN entry screen instead of a result; Offline PIN markets may need PSP PIN-fallback with partial data; consult your PSP.
- Display clear descriptions and resolutions for merchant-addressable errors — e.g., an alert recommending an iOS update.
- Make it easy to get help — in-app or web help content plus an action to contact support.
- Use a generic label (Look Up, Store Card, Verify, Refund) for buttons that read a card with no transaction amount — never "Tap to Pay on iPhone" or "Tap to Pay".
- Give an independent loyalty-card transaction its own clearly labeled button — no payment-related terms in its label.

**Platform notes**
- iOS: no additional considerations · iPadOS/macOS/tvOS/visionOS/watchOS: not supported.

**Dev refs**
ProximityReader, Setting up Tap to Pay on iPhone, Adding support for Tap to Pay on iPhone to your app, ProximityReaderDiscovery, PaymentCardReader.prepare(using:), PaymentCardReader.Event.updateProgress(_:), PaymentCardReader.Event.readyForTap, PaymentCardReader.Options.returnReadResultImmediately, PaymentCardReaderSession.ReadError, Tap to Pay on iPhone marketing guidelines, SF Symbols

## VoiceOver
Full page: hig/technologies/voiceover.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
VoiceOver is the system screen reader; supporting it lets people who are blind or have low vision navigate and understand your interface. Supported in native apps and games, and in Unity games via Apple's Unity plug-ins.

**Rules**
- Provide alternative labels for all key interface elements — replace generic system labels with descriptive ones; label every custom element; keep labels current as the UI changes.
- Describe meaningful images — describe only what the image itself conveys, since VoiceOver reads surrounding captions separately.
- Make charts and other infographics fully accessible — concise description of what each conveys; expose any interactive drill-down through the accessibility APIs.
- Exclude purely decorative images from VoiceOver — saves time and reduces cognitive load.
- Use titles and headings to convey the information hierarchy — unique, succinct page titles (the first thing read on arrival) and accurate section headings.
- Specify how elements are grouped, ordered, or linked — relationships that are visual-only (proximity, alignment) must be described to VoiceOver.
- Group related elements so reading order matches meaning — VoiceOver reads in the active language's order (US English: top to bottom, left to right); ungrouped, it reads every image before any caption; grouped, each image with its caption.
- Inform VoiceOver when visible content or layout changes — so people can update their mental map.
- Support the VoiceOver rotor when possible — identify headings, links, and other content types; the rotor can also bring up the braille keyboard.

**Platform notes**
- iOS/iPadOS/macOS/tvOS/watchOS: no additional considerations · visionOS: with VoiceOver on, apps and games with custom gestures don't receive hand input by default; people can enable Direct Gesture mode to let apps process hand input directly.

**Dev refs**
Accessibility, VoiceOver, Supporting VoiceOver in your app, Accessibility modifiers (SwiftUI), accessibilityHidden(_:), accessibilityElement, isAccessibilityElement, shouldGroupAccessibilityChildren, AccessibilityNotification, AccessibilityRotorEntry (SwiftUI), UIAccessibilityCustomRotor (UIKit), NSAccessibilityCustomRotor (AppKit), Improving accessibility support in your visionOS app, Apple Unity plug-ins; related HIG: Accessibility, Inclusion, Charts

## Wallet
Full page: hig/technologies/wallet.md · Platforms: iOS, iPadOS, macOS, visionOS, watchOS
Wallet stores cards, IDs, transit cards, tickets, keys, and passes. Apps integrate to create and surface passes, track orders, and verify identity with an ID in Wallet; Pass Designer previews and builds passes.

**Rules**
- Offer to add new passes to Wallet — when an action yields a pass (ticket purchase, reward sign-up), present the system UI that adds it with one tap.
- Add passes in the background for frequent, predictable actions like flight check-in — after a one-time authorization, so people don't tap Add to Apple Wallet every time; Wallet notifies on each add.
- Show a custom view with an Add to Apple Wallet button when someone wants to review the pass first.
- Help people add a pass created outside your app — suggest it next time they open the app; if they decline, don't ask again.
- Add related passes as a group — all boarding passes of a multi-connection flight at once; bundle web-distributed sets (event tickets) for one download.
- Display an Add to Apple Wallet button for an existing pass not in Wallet — wherever the pass information appears; an Add to Apple Wallet badge exists for email and web (see Add to Apple Wallet guidelines).
- Let people jump from your app to the pass in Wallet — a link labeled like "View in Wallet".
- Tell the system when passes expire — set expiration date, relevant date, and voided properties correctly; Wallet hides expired passes and offers a button to revisit them.
- Always get permission before deleting passes — e.g., an in-app setting for manual vs. automatic removal; show an alert if necessary.
- Help the system suggest a pass when relevant — supply when/where relevance so a Lock Screen link appears (gym card on arrival); event tickets can also start a Live Activity.
- Keep passes up to date — reflect delays and gate changes as they happen.
- Use change messages only for time-critical updates — a change message interrupts; never for marketing or noncritical changes (gate change yes, support number no); messages are per field.
- Define passes with pass fields (what appears and how it's arranged) plus semantic tags (describe content to the system; enable surfacing a pass when needed and featured actions — quick links such as venue directions or event guides).
- Use semantic tags on poster event and semantic boarding passes — they're required and enable automatic layout; include pass fields alongside them so the passes display correctly on older iOS versions.
- Put supplemental information in sheets linked from the pass front; keep rarely needed settings and legal text on the back.
- Use the pass field areas as intended (layout varies by pass style):
  - Logo and logo text — brand icon and name; remain visible when the pass is collapsed in Wallet.
  - Header — critical information that stays visible when collapsed.
  - Primary — the most important information people need.
  - Secondary and auxiliary — useful but less critical information.
  - Footer — supplemental information such as pass category ("Family", "Annual").
  - Back — supplemental details shown in pass details in Wallet.
- Design a clean, simple pass that feels at home in Wallet — don't merely replicate the physical counterpart; start from Pass Designer templates or a blank pass (boarding passes, coupons, event tickets, store cards, generic, poster generic).
- Design a pass that works on all devices — Apple Watch shows less information and fewer images; keep essential info out of device-dependent elements; don't pad images (watchOS crops white space).
- Keep the pass front uncluttered — essentials (event date, balance) in the header so they show when collapsed; quick-access info on the front; infrequent details on the information sheet.
- Make your pass instantly identifiable — brand colors, images, icons, full-art backgrounds.
- Ensure sufficient contrast between background and text — label colors must stay legible on solid backgrounds and on background images.
- Use language that works on any device — "Slide to view" means nothing on Apple Watch.
- Pick the pass style by purpose — each defines appearance and layout:
  - Boarding pass — airline boarding passes, train, bus, boat, and generic transit tickets; typically one trip with a start and end point; use semantic tags for airline passes and pass fields for all other transit types.
  - Coupon — coupons, special offers, and other discounts.
  - Event ticket — sporting events, concerts, movies, plays; usually one event, or one pass for multiple events (season ticket); supports a full-art background; non-poster event tickets use standard pass fields with a background image and thumbnail.
  - Store card — loyalty, discount, points, and gift cards; usually displays the account balance.
  - Poster generic — full background image and a field layout distinct from other styles; not tied to a category, use when no other style fits.
  - Generic — passes that fit no other category, such as a gym membership card or coat-check claim ticket.
- Create pass images as PNG at @2x and @3x.
- Reserve pass images for visual content — embedded text isn't accessible and may not display everywhere; use text fields and semantic tags; add barcodes with Pass Designer or APIs, not inside images.
- Keep image file sizes small — passes arrive by email and web.
- Provide a pass icon — used on the Lock Screen, in Mail, and on passes; your app icon or a separate design; the system rounds corners.
- Avoid inner drop shadows on logo artwork — they reduce legibility.
- Strip images (coupons, store cards): ensure contrast with overlaid text; keep areas behind text uncluttered; place important elements toward the bottom or trailing edge; no embedded text.
- Thumbnails (event tickets, generic passes): square; put rounded corners in the artwork; export as transparent PNG.
- Backgrounds are the visual centerpiece — they appear blurred behind content on older event tickets and unblurred on poster event tickets and poster generic passes.
- Position background content within the safe area — on poster generic passes and poster event tickets a material strip covers the bottom edge of the image; account for a barcode if the pass has one; preview the layout in Pass Designer; see `footerBackgroundColor`.
- Order tracking: make it easy to add an order — PKPaymentOrderDetails (app) or ApplePayPaymentOrderDetails (web) after an Apple Pay transaction; in iOS 17 and later show the system Track with Apple Wallet button (AddOrderToWalletButton) on confirmation, status, and tracking pages and in emails; re-adding an existing order opens it in Wallet.
- Make order information available immediately after purchase — supply what you have and a status description like "Check back later for full order details."
- Provide fulfillment information as soon as available and keep status current — the system maps your fulfillment status to Order Placed, Processing, Ready for Pickup, Picked Up, Out for Delivery, Delivered, Issue, or Canceled and can notify customers.
- Supply a high-resolution merchant logo with a nontransparent background — 300x300 pixels, PNG or JPEG.
- Supply distinct product images with nontransparent backgrounds — 300x300 pixels, PNG or JPEG; straightforward depiction on a solid background, not a lifestyle shot.
- Keep order text brief — the system truncates; use clear, approachable, localized language; the shown price must match the final confirmed price.
- Provide a universal link to your order-management area — works even without the app installed.
- Clearly describe each line item (price, name, image) — an order lists every item; a fulfillment lists only its items; attach a PDF receipt to a transaction when appropriate.
- Supply a prioritized list of your apps — the system links to the highest-ranked installed app, or the first listed if none is installed.
- Avoid duplicate notifications — suppress Wallet order notifications when one of your associated apps is installed.
- Make contacting the merchant easy — at minimum a website or landing-page link; optionally Messages for Business, phone, email, and support page; shown in the Contact menu.
- Help people track their order — a multi-item order can have multiple fulfillments, each shipping or pickup; supply enough to know where items are and when to expect them, plus:
  - a link that opens the carrier's page for a shipping fulfillment — a direct link in addition to the tracking number; show it on any intermediate tracking page too
  - a scannable barcode when one is required to pick up the order
  - clear, detailed instructions for receiving or picking up the order
- Keep the fulfillment screen centered on order tracking — prioritize tracking over app or service promotion.
- Choose shipping-fulfillment values that match what you know — set `carrier` when known or keep the default "Track Shipment"; use `onTheWay`, `outForDelivery`, `delivered` when you have carrier steps, otherwise `shipped`; always include a tracking link when available.
- Keep customers informed with relevant status descriptions — approachable, accurate, on-brand; be direct and thorough for Issue or Canceled (why, and what to do).
- Identity verification (iOS 16 and later): present a Verify with Wallet option only when the device supports it — offer a fallback verification method otherwise.
- Ask for identity information only at the precise moment you need it — during the process or transaction that requires it, never at account creation or before people start.
- Clearly and succinctly describe why you need the information — a purpose string shown in the verification sheet: brief, complete, direct, specific sentence; sentence case; active voice; ending period.
- Ask only for the data you actually need — use an age threshold request (age(atLeast:)) rather than age or birth date.
- Indicate whether you keep the data and for how long — specify a period, indefinitely, or only for the current verification (PKIdentityIntentToStore); the sheet explains it automatically.
- Choose the system-provided verification button whose label matches your use case and visual design — see the button-type table in Specs.
- Expect every label to have a multiline variant the system uses automatically when horizontal space is constrained.
- Keep the verification button's fixed look — always white letters on a black background; choose the light-outline style when the button must contrast with a dark background; use cornerRadius to match related buttons.
- Remember Apple never creates or sees ID documents; your app receives only encrypted data.

**Platform notes**
- iOS/iPadOS/macOS/visionOS: no additional considerations · tvOS: not supported · watchOS: Wallet shows passes in a scrolling carousel; people can add your pass even without a watch app; tapping reveals a scrolling details screen (sometimes per-transaction detail); each style has fixed layout areas and overflow goes to the details screen; watchOS crops the strip image to the card aspect ratio in every style and may crop white space from other images.

**Specs**

Logo:

|  |  |
|---|---|
| **Supported pass styles** | Non-semantic airline boarding passes, non-airline boarding pass styles, coupons, non-poster event tickets, generic passes, store cards |
| **Filename** | logo.png |
| **Minimum width** | 50 pt |
| **Maximum width** | 160 pt |
| **Height** | 50 pt |

Primary logo:

|  |  |
|---|---|
| **Supported pass styles** | Airline boarding passes, poster event tickets, and poster generic passes |
| **Filename** | primaryLogo.png |
| **Minimum width** | 30 pt |
| **Maximum width** | 126 pt |
| **Height** | 30 pt |

Secondary logo:

|  |  |
|---|---|
| **Supported pass styles** | Poster event ticket |
| **Filename** | secondaryLogo.png |
| **Minimum width** | 12 pt |
| **Maximum width** | 135 pt |
| **Height** | 12 pt |

Icon:

|  |  |
|---|---|
| **Supported pass styles** | All |
| **Filename** | icon.png |
| **Width** | 38 pt |
| **Height** | 38 pt |

Strip image:

|  |  |
|---|---|
| **Supported pass styles** | Coupon, store card |
| **Filename** | strip.png |
| **Width** | 375 pt |
| **Height** | 144 pt |

Thumbnail:

|  |  |
|---|---|
| **Supported pass styles** | Event ticket, generic pass |
| **Filename** | thumbnail.png |
| **Minimum width** | 60 pt |
| **Maximum width** | 90 pt |
| **Height** | 90 pt |

Non-poster pass backgrounds:

|  |  |
|---|---|
| **Supported pass styles** | Event tickets |
| **Filename** | background.png |
| **Width** | 343 pt |
| **Height** | 503 pt |

Poster pass backgrounds:

|  |  |
|---|---|
| **Supported pass styles** | Poster event tickets, poster generic passes |
| **Filename** | artwork.png |
| **Width** | 358 pt |
| **Height** | 448 pt |

Footer:

|  |  |
|---|---|
| **Supported pass styles** | Airline boarding passes |
| **Filename** | footer.png |
| **Width** | 268 pt |
| **Height** | 15 pt |

Order tracking images (from text):

| Image | Size | Format | Background |
|---|---|---|---|
| Merchant logo | 300x300 pixels | PNG or JPEG | nontransparent |
| Product image | 300x300 pixels | PNG or JPEG | solid, nontransparent |

Identity verification purpose strings:

| To verify… | To support… | Example purpose string |
|---|---|---|
| Identity | Opening an account for which proof of identity is legally required to prevent fraud | Federal law requires this information to verify your identity and also to help [App Name] prevent fraud. |
| Driving privilege | Renting a vehicle that requires legal driving privileges | Applicable state law requires [App Name] to verify your driving privileges. |

Verification button types (the first column held button images that the crawl did not capture; the labels the page's text names are "Verify Age", "Verify Identity", and "Continue"):

| Button type | Consider using when… |
|---|---|
|  | Your app can complete the current transaction after you verify a person's age. An example transaction is making a car available to lease. |
|  | Your app can complete the current transaction after you verify a person's identity. An example transaction is a car rental. |
|  | Verify with Wallet forms one part of a verification process that also requires people to supply additional information not provided by Verify with Wallet, such as a Social Security number or phone number. Examples include opening a financial account or performing a background check. |
|  | Your app can complete the current verification flow without additional steps, but the "Verify Age," "Verify Identity," and "Continue" button labels aren't appropriate for your use case. An example is an app that helps people sign up for a government service. |

**Dev refs**
PassKit (Apple Pay and Wallet), Wallet Passes, Wallet Orders, FinanceKit, FinanceKitUI, Pass Designer (Creating a pass with Pass Designer), PKPassLibrary.addPasses(_:withCompletionHandler:), PKPassLibrary.Capability.backgroundAddPasses, PKAddPassesViewController, PKAddPassButton, Add to Apple Wallet guidelines, Pass (expirationDate/relevantDate/voided, footerBackgroundColor), Showing a Pass on the Lock Screen, Adding a Web Service to Update Passes, Distributing and updating a pass, Defining the metadata of your Wallet Pass, Creating an airline boarding pass using semantic tags, Creating a coupon pass, Creating a poster event pass using semantic tags, Creating a store card pass, Creating a Poster Generic Pass, PKPaymentOrderDetails, ApplePayPaymentOrderDetails, AddOrderToWalletButton, Order, LineItem, Merchant (logo), ShippingFulfillment, Allowing apps and websites to link to your content, Requesting identity data from a Wallet pass, VerifyIdentityWithWalletButton, PKIdentityElement.age(atLeast:), PKIdentityIntentToStore, PKIdentityButton.Label, PKIdentityButton.cornerRadius, PKIdentityButton.Style.blackOutline; related HIG: Apple Pay, ID Verifier
