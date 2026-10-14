# Components (content · layout & organization · menus & actions · navigation & search) — HIG digest

These four groups of Apple's Human Interface Guidelines "Components" collection cover the views that hold content (charts, image/text/web views), the containers that organize it (boxes, collections, column/outline/split/tab views, disclosure controls, labels, lists and tables, tvOS lockups), the controls that expose commands (activity views, buttons, context/edit/Dock menus, Home Screen quick actions, menus, visionOS ornaments, pop-up and pull-down buttons, the menu bar, toolbars), and the controls that move people around (path controls, search fields, sidebars, tab bars, token fields). Full pages live in `hig/components/<slug>.md` (crawled 2026-10-14; the group index pages `hig/components/content.md`, `layout-and-organization.md`, `menus-and-actions.md`, `navigation-and-search.md` are link lists only). This digest keeps every rule and every number from those pages but drops examples, screenshots, videos, and prose. The sibling groups — Presentation, Selection and input, Status, System experiences — are digested in a separate file.

## Content

### Charts
Full page: hig/components/charts.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
A chart highlights a few key pieces of a dataset so people can gain insight and decide. Anatomy: marks (bar, line, point) plotted in a plot area; scales map values to position/color/height; axes with ticks and grid lines; labels, accessibility labels, titles, subtitles, annotations, legend. Design guidance for charts as part of an experience is in the Charting data pattern page.

**Rules**
- **Choose a mark type based on what you want to communicate.** Bar: compare categories, part-to-whole, or sums over time (steps per day). Line: change over time; slope shows magnitude of change and trend. Point: individual values, relationships between two properties, outliers, clusters.
- **Combine mark types when it adds clarity** — e.g. point marks on a line to call out individual values.
- **Use a fixed or dynamic axis range depending on meaning.** Fixed when min/max are meaningful for all data (battery 0%–100%); dynamic when values vary widely and marks should fill the plot area (Health Steps).
- **Define the lower bound by mark type and usage.** Zero works for bar charts (relative heights); zero can obscure meaningful differences far from zero (heart rate).
- **Prefer familiar value sequences for tick and grid-line labels** (0, 5, 10 — not 1, 6, 11).
- **Tailor grid-line and label density/weight to the chart's use.** Too many overwhelm; too few hinder estimation. Interactive charts can use fewer grid lines and lighter label colors.
- **Write descriptions that explain what a chart does before people view it** — essential for VoiceOver users and people with cognitive disabilities.
- **Summarize the chart's main message** in a title/subtitle so people grasp it without reading details.
- **Establish a consistent visual hierarchy**: data most prominent; descriptions and axes provide context without competing.
- **In a compact environment, maximize plot-area width**: keep vertical-axis labels short, put units in the title, place long axis labels inside the plot area when they don't obscure data.
- **Make every chart accessible**: supply accessibility labels and support VoiceOver; use Audio Graphs (tones representing values and trend plus text summaries).
- **Let people interact when it makes sense, but never require interaction to reveal critical information.**
- **Make interaction easy**: when marks are too small to target, expand the hit target to the whole plot area and let people scrub.
- **Make interactive charts navigable by keyboard (incl. Full Keyboard Access) and Switch Control.** Either define a logical path with accessibility APIs (`accessibilityRespondsToUserInteraction(_:)`), e.g. along the X axis, or let focus move among subsets of values for large datasets. Both also improve VoiceOver.
- **Help people notice important changes** to marks or axes: animate, but also highlight the change another way for VoiceOver users and people who turn off animations (`UIAccessibility.Notification` / `NSAccessibility.Notification`).
- **Align the chart with surrounding elements**: align leading edges; put each vertical grid-line label on its trailing side; consider moving the Y axis to the trailing side; anchor an orphan label to a grid line with a tick.
- **Never rely solely on color** to differentiate data; add shapes or patterns (Health blood pressure uses two point shapes).
- **Add visual separation between contiguous areas of color** (separators between stacked bar marks).
- **Consider Audio Graphs for VoiceOver users**; customize the Swift Charts default with a chart title and descriptive summary. If you don't use Audio Graphs, provide an overview: chart type, what each axis represents, upper/lower bounds.
- **A chart usually needs an accessibility label for each important or interactive element** (unlike an image). Decide per-mark vs per-group; a single high-level label is fine for a small chart inside a button.
- **Write accessibility labels that serve the chart's purpose** (Maps elevation summarizes route segments; Health Steps labels each bar).
- **Accessibility-label writing — prioritize clarity and comprehensiveness**: a bare value is rarely enough; add context like the date or location without repeating what Audio Graphs or the overview already gives (e.g. an axis name); lead with context, then a succinct description of the element.
- **Avoid subjective terms** (rapidly, gradually, almost) — use actual values so people form their own interpretation.
- **Avoid ambiguous formats and abbreviations**: "June 6" not "6/6"; "60 minutes" or "60 meters" not "60m".
- **Describe what chart details represent, not what they look like** — identify what each series means rather than narrating its color.
- **Refer to a specific axis consistently throughout the app** (e.g. always mention the X axis first).
- **Hide visible axis and tick labels from assistive technologies** — VoiceOver users get values via accessibility labels and Audio Graphs.

**Platform notes**
- watchOS: avoid requiring complex chart interactions; prefer glanceable info and simple interactions; put detail and richer interaction in a companion app on another platform. No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS.

**Dev refs**
Swift Charts, Audio Graphs (Accessibility), accessibilityRespondsToUserInteraction(_:) (SwiftUI), UIAccessibility.Notification (UIKit), NSAccessibility.Notification (AppKit)

### Image views
Full page: hig/components/image-views.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
An image view displays a single image (or an animated sequence) on a transparent or opaque background; it can stretch, scale, size-to-fit, or pin the image, and is typically not interactive. Formats include PNG, JPEG, PDF.

**Rules**
- **Use an image view only when the primary purpose is to display an image.** For a rare interactive image, configure a system button to display the image rather than adding button behavior to an image view.
- **For an icon, consider an SF Symbol or interface icon instead** — both are vector/template images that can take the accent colors people choose.
- **Take care overlaying text on images**: ensure contrast; add a text shadow or background layer to make the text stand out.
- **Use a consistent size for all images in an animated sequence**; prescale to fit the view so the system doesn't scale; same size and shape improves performance when it must.

**Platform notes**
- iOS/iPadOS: no additional considerations.
- macOS: for an editable image view use an image well (supports copy, paste, drag, and the Delete key to clear); for a clickable image use an image button.
- tvOS: many images combine multiple transparent layers for depth — see Layered images.
- visionOS: windows can show 2D and stereoscopic images and spatial photos; with RealityKit you can show images of any type beside 3D content or generate a spatial scene from a 2D image (ImagePresentationComponent); for other 3D content in a window or volume see Windows > visionOS.
- watchOS: use SwiftUI to create animations when possible; WatchKit can animate an image sequence in an image element if necessary (WKImageAnimatable).

**Dev refs**
Image (SwiftUI), UIImageView (UIKit), NSImageView (AppKit), ImagePresentationComponent (RealityKit), WKImageAnimatable (WatchKit)

### Text views
Full page: hig/components/text-views.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
A text view displays multiline, styled, optionally editable text; it can be any height and scrolls when content overflows. Default: leading-aligned, system label color; in iOS/iPadOS/visionOS an editable text view summons the keyboard when selected. Use a label (small, static) or text field (small, editable) instead for short text.

**Rules**
- **Use a text view for text that's long, editable, or specially formatted**; a label or text field is simpler for small amounts.
- **Keep text legible**: multiple fonts/colors/alignments are allowed but readability comes first; adopt Dynamic Type; test with accessibility options like bold text.
- **Make useful text selectable** (error messages, serial numbers, IP addresses) so people can copy it.

**Platform notes**
- iOS/iPadOS: show the keyboard type appropriate to the content (see Virtual keyboards) · tvOS: text views display text only; editable text uses text fields because input is minimal by design · macOS/visionOS/watchOS: no additional considerations.

**Dev refs**
Text (SwiftUI), UITextView (UIKit), NSTextView (AppKit)

### Web views
Full page: hig/components/web-views.md · Platforms: ios,ipados,macos,visionos
A web view loads and displays rich web content (embedded HTML, websites) inside your app (Mail uses one for HTML messages). Not supported in tvOS or watchOS. Don't use it to build a browser.

**Rules**
- **Support forward and back navigation when appropriate** — not on by default; enable it and provide controls if people will visit multiple pages.
- **Avoid using a web view to build a web browser.** Brief in-app access to a site is fine; replicating Safari is unnecessary and discouraged.

**Dev refs**
WKWebView (WebKit)

## Layout and organization

### Boxes
Full page: hig/components/boxes.md · Platforms: ios,ipados,macos,visionos
A box visually groups logically related information and components using a border or background color, optionally with a title. Not supported in tvOS or watchOS.

**Rules**
- **Keep a box relatively small compared with its containing view**; a box near window/screen size stops communicating separation and crowds content.
- **Use padding and alignment, not nested boxes, to communicate subgroups** — nested borders make the interface busy and constrained.
- **Provide a succinct introductory title if it clarifies the contents**; a title also helps VoiceOver users predict the content.
- **Title style**: a brief phrase describing the contents, sentence-style capitalization, no ending punctuation — except in a settings pane, where the title ends with a colon.

**Platform notes**
- iOS/iPadOS: boxes use the secondary and tertiary background colors by default · macOS: the title appears above the box by default · visionOS: no additional considerations.

**Dev refs**
GroupBox (SwiftUI), NSBox (AppKit)

### Collections
Full page: hig/components/collections.md · Platforms: ios,ipados,macos,tvos,visionos
A collection manages an ordered set of content in a customizable, highly visual layout — ideal for image-based content. Not supported in watchOS. Use a table for text.

**Rules**
- **Use the standard horizontal-row or grid layout whenever possible**; avoid custom layouts that confuse or draw attention to themselves.
- **Consider a table instead of a collection for text** — scrollable lists are simpler and more efficient to read.
- **Make it easy to choose an item**: adequate padding around images keeps focus/hover effects visible and prevents overlap.
- **Add custom interactions only when necessary.** Defaults: tap to select, touch and hold to edit, swipe to scroll.
- **Consider animations as feedback for insert, delete, and reorder**; standard animations are supported, custom ones allowed.

**Platform notes**
- iOS/iPadOS: use caution with dynamic layout changes — make them sensible and easy to track, and avoid changing layout while people view/interact unless in response to an explicit action · macOS/tvOS/visionOS: no additional considerations.

**Dev refs**
UICollectionView (UIKit), NSCollectionView (AppKit)

### Column views
Full page: hig/components/column-views.md · Platforms: macos
A column view (browser) navigates a data hierarchy through vertical columns: each column is one level; parents show a triangle; selecting a parent fills the next column. macOS only — for iPadOS/visionOS hierarchies use a split view. Use it for deep hierarchies with frequent back-and-forth where you don't need list/table sorting (Finder column view).

**Rules**
- **Show the root level of the hierarchy in the first column** so people can scroll back to it and start over.
- **Consider showing information about the selected item when it has no children** (Finder shows a preview plus creation/modification dates, type, size).
- **Let people resize columns**, especially when item names exceed the default column width.

**Dev refs**
NSBrowser (AppKit)

### Disclosure controls
Full page: hig/components/disclosure-controls.md · Platforms: ios,ipados,macos,visionos
Disclosure controls reveal and hide information and functionality. A disclosure triangle (for a view or list of items) points inward from the leading edge when collapsed and down when expanded. A disclosure button (for a specific control, e.g. the macOS Save sheet) points down when collapsed and up when expanded. Not supported in tvOS or watchOS.

**Rules**
- **Use a disclosure control to hide details until relevant**: most-used controls at the top of the hierarchy, always visible; advanced functionality hidden by default.
- **Disclosure triangle**: shows/hides information and functionality for a view or list of items (Keynote export options, Finder list-view hierarchy); points inward from the leading edge when content is hidden and down when visible; clicking or tapping toggles the state and the view expands or collapses to fit.
- **Disclosure button**: shows/hides functionality for a specific control (the macOS Save sheet's button beside the Save As field expands the dialog's navigation options); points down when content is hidden and up when visible; clicking or tapping toggles the state.
- **Give a disclosure triangle a descriptive label** that says what is disclosed/hidden ("Advanced Options").
- **Place a disclosure button near the content it shows and hides** so the relationship is clear.
- **Use no more than one disclosure button in a single view.**

**Platform notes**
- iOS/iPadOS/visionOS: available via SwiftUI DisclosureGroup · macOS: no additional considerations.

**Dev refs**
DisclosureGroup (SwiftUI), NSButton.BezelStyle.disclosure (AppKit), NSButton.BezelStyle.pushDisclosure (AppKit)

### Labels
Full page: hig/components/labels.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
A label is static text people can read and often copy but not edit — in buttons (Edit, Cancel, Send), list items (often with a symbol/image), and views (introducing a control or describing a task). SwiftUI offers Label and Text. For editable short text use a text field; for long text use a text view.

**Rules**
- **Use a label for a small amount of uneditable text.**
- **Prefer system fonts**; labels support Dynamic Type by default; keep custom-styled text legible.
- **Use the system label colors to communicate relative importance** (four levels, table below).
- **Make useful label text selectable** (error message, location, IP address).

**Platform notes**
- macOS: display uneditable text with NSTextField's isEditable property · watchOS: date/time text components (configurable formats, calendars, time zones) and countdown/count-up timer components auto-fit available space and update without app input; consider them in complications · iOS/iPadOS/tvOS/visionOS: no additional considerations.

**Specs**

| System color | Example usage | iOS, iPadOS, tvOS, visionOS | macOS |
|---|---|---|---|
| Label | Primary information | label | labelColor |
| Secondary label | A subheading or supplemental text | secondaryLabel | secondaryLabelColor |
| Tertiary label | Text that describes an unavailable item or behavior | tertiaryLabel | tertiaryLabelColor |
| Quaternary label | Watermark text | quaternaryLabel | quaternaryLabelColor |

**Dev refs**
Label (SwiftUI), Text (SwiftUI), UILabel (UIKit), NSTextField (AppKit), UIColor.label/secondaryLabel/tertiaryLabel/quaternaryLabel, NSColor.labelColor/secondaryLabelColor/tertiaryLabelColor/quaternaryLabelColor

### Lists and tables
Full page: hig/components/lists-and-tables.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
Lists and tables present data in one or more columns of rows, optionally grouped or hierarchical, with selecting, adding, deleting, and reordering. Lists often express an app's information hierarchy (iOS Settings); tables often sit inside split views (Mail) or hold multicolumn sortable productivity data.

**Rules**
- **Prefer a list or table for text**; the row format makes text easy to scan. Use a collection for items that vary widely in size or for many images.
- **Let people edit a table when it makes sense** — reordering is appreciated even without add/remove. In iOS/iPadOS people must enter edit mode before selecting items.
- **Give appropriate selection feedback**: a navigation table persistently highlights the selected row; an options table highlights briefly then shows a checkmark.
- **Keep item text succinct** to minimize truncation and wrapping; for long items list titles only and open a detail view.
- **Preserve readability of clipped text** when the table is narrow — a middle ellipsis keeps both the start and end recognizable.
- **Use descriptive column headings in multicolumn tables**: nouns or short noun phrases, title-style capitalization, no ending punctuation. In a single-column table without a heading, add a label or header for context.
- **Choose a table/list style that fits the data and platform**: iOS/iPadOS grouped style (headers, footers, spacing); watchOS elliptical style (items roll off a rounded surface); macOS bordered style (alternating row backgrounds for large tables). See ListStyle.
- **Choose a row style that fits the information** (e.g. leading image + brief label); iOS/iPadOS/tvOS provide UIListContentConfiguration for rows, headers, footers.

**Platform notes**
- iOS/iPadOS/visionOS: an info button (called a detail disclosure button in a list row) only reveals more information about the row's content — it doesn't navigate a hierarchy; to let people drill into a row's subviews use a disclosure indicator accessory control.
- iOS/iPadOS/visionOS: avoid adding an index (letters of the alphabet listed vertically at the trailing side for jumping to sections) to a table whose rows display trailing-edge controls like disclosure indicators — both sit on the trailing side and people activate one while trying to use the other.
- macOS: when it provides value, let people click a column heading to sort by that column; clicking an already-sorted heading re-sorts in the opposite direction.
- macOS: let people resize columns — data widths vary and people want to concentrate on areas or reveal clipped data.
- macOS: consider alternating row colors in a multicolumn table to help track row values across columns, especially in wide tables.
- macOS: use an outline view, not a table view, for hierarchical data — it looks like a table but adds disclosure triangles for nested levels.
- tvOS: a focused row highlights and slightly increases in size, and its corners can become rounded — prepare images on either side of rows for this effect and don't add your own corner masks.
- watchOS: limit the number of rows when possible, but don't hide an expected long list (podcast subscriptions) — list the most relevant items and provide a way to view more.
- watchOS: constrain detail-view length if you support vertical page-based navigation (swiping vertically among the detail items of different rows without returning to the list); it works only with short, non-scrolling detail views.

**Dev refs**
List (SwiftUI), Tables (SwiftUI), ListStyle (SwiftUI), UITableView (UIKit), UIListContentConfiguration (UIKit), UITableViewCell.AccessoryType.disclosureIndicator (UIKit), NSTableView (AppKit)

### Lockups
Full page: hig/components/lockups.md · Platforms: tvos
A lockup combines a content view, header (above), and footer (below) into one interactive unit; all three expand and contract together on focus. Four types: cards (ratings/reviews for media), caption buttons (image or text with title/subtitle beneath), monograms (circular picture plus name; initials if no image), posters (image plus title/subtitle hidden until focus). tvOS only.

**Rules**
- **Cards** combine a header, footer, and content view to present ratings and reviews for media items (TVCardView).
- **Caption buttons** can include a title and subtitle beneath the button and contain either an image or text (TVCaptionButtonView).
- **Monograms** identify people (usually cast and crew): a circular picture plus the person's name, with initials in place of a missing image (TVMonogramContentView).
- **Posters** consist of an image and an optional title and subtitle that stay hidden until the poster gains focus (TVPosterView; see Image views).
- **Allow adequate space between lockups** — a focused lockup expands and must not overlap or displace neighbors.
- **Use consistent lockup sizes within a row or group**; matching widths and heights look better.
- **Caption buttons must tilt with the swipe direction**: vertically aligned → tilt up/down; horizontally aligned → tilt left/right; in a grid → both.
- **Monograms: prefer images over initials**; an image creates a more intimate connection.
- **Posters can be any size, but size them for their content.**

**Dev refs**
TVLockupView, TVLockupHeaderFooterView, TVCardView, TVCaptionButtonView, TVMonogramContentView, TVPosterView (TVUIKit)

### Outline views
Full page: hig/components/outline-views.md · Platforms: macos
An outline view shows hierarchical data in a scrolling list of cells in columns and rows; the first column holds parents with disclosure triangles and their children, extra columns show attributes (size, date). Works well for text content, often on the leading side of a split view. macOS only; use a table for non-hierarchical data.

**Rules**
- **Use a table instead for data that isn't hierarchical.**
- **Expose the hierarchy in the first column only**; other columns display attributes of the primary column's items.
- **Use descriptive column headings**: nouns/short noun phrases, title-style capitalization, no punctuation (no trailing colon). Always provide headings in a multicolumn outline view; a single-column view without a heading needs a label or other context.
- **Consider click-to-sort column headings**: ascending/descending per column; sorting the primary column sorts at each hierarchy level (top-level folders, then items within each); clicking an already-sorted heading reverses the sort; secondary-column sorting can happen behind the scenes.
- **Let people resize columns** to reveal wide data.
- **Make expand/collapse easy**: clicking a triangle expands that container; Option-click expands all its nested containers.
- **Retain people's expansion choices** across sessions so they don't re-navigate.
- **Consider alternating row colors in multicolumn outline views** to track rows across columns.
- **Let people edit data if it makes sense**: single-click a cell to edit; double-click may do something different (open the file); reorder/add/remove rows when useful.
- **Consider a centered ellipsis instead of clipping cell text** to keep start and end recognizable.
- **Consider a search field (usually in the toolbar) for lengthy outline views.**

**Dev refs**
OutlineGroup (SwiftUI), NSOutlineView (AppKit)

### Split views
Full page: hig/components/split-views.md · Platforms: ios,ipados,macos,tvos,visionos,watchos
A split view presents multiple adjacent panes (tables, collections, images, custom views), usually to show several hierarchy levels at once: the primary pane's selection fills the secondary, and an optional tertiary pane shows deeper content. Commonly hosts a sidebar in the leading pane; rarely used for supplementary functional groups (Keynote navigator, presenter notes, inspector).

**Rules**
- **Persistently highlight the current selection in every pane that leads to the detail view** to clarify pane relationships and keep people oriented.
- **Consider letting people drag and drop content between panes** (see Drag and drop).

**Platform notes**
- iOS: prefer a split view in a regular — not compact — environment; in a compact environment such as iPhone in portrait, multiple panes wrap or truncate, becoming less legible and harder to use.
- iPadOS: a split view can include two vertical panes (Mail) or three (Keynote).
- iPadOS: account for narrow, compact, and intermediate window widths — iPad windows resize fluidly — and ensure people can navigate between panes logically at every width (see Layout; NavigationSplitView, UISplitViewController).
- macOS: panes can be arranged vertically, horizontally, or both, with dividers between panes that support dragging to resize (VSplitView, HSplitView).
- macOS: set reasonable default minimum and maximum pane sizes that keep the divider visible; a pane that gets too small makes the divider seem to disappear and hard to use.
- macOS: consider letting people hide a pane when it makes sense — e.g. hide other panes around an editing area to reduce distraction (Keynote hides the navigator and presenter notes while editing slides).
- macOS: provide multiple ways to reveal hidden panes — a toolbar button or a menu command, including a keyboard shortcut.
- macOS: prefer the thin divider style — 1 point wide — for maximum content space; use a thicker divider only for a specific need, e.g. table rows with strong linear elements on both sides that make a thin divider hard to distinguish (NSSplitView.DividerStyle).
- tvOS: a split view works well for filtering — choosing a category in the primary pane shows results in the secondary pane.
- tvOS: choose a layout that keeps panes balanced — by default the primary pane gets one-third of the screen width and the secondary two-thirds; you can also specify a half-and-half layout.
- tvOS: display a single title above the split view describing the content as a whole; people don't need titles for each pane.
- tvOS: center the title in the window when the secondary pane contains a content collection; place it above the primary pane when the secondary pane contains a single main view of important content, giving that content more room.
- visionOS: prefer a split view over a new window for supplementary information — new windows can confuse people navigating or repositioning content and require you to manage view relationships; use a sheet to request a small amount of information or present a simple task that must finish before returning to the main task.
- watchOS: the split view displays either the list view or a detail view as a full-screen view.
- watchOS: automatically display the most relevant detail view at launch (based on location, time, or recent actions).
- watchOS: with multiple detail pages, place the detail views in a vertical tab view so people scroll between them with the Digital Crown; watchOS shows a page indicator beside the Crown with the number of tabs and the current one.

**Dev refs**
NavigationSplitView (SwiftUI), VSplitView (SwiftUI), HSplitView (SwiftUI), UISplitViewController (UIKit), NSSplitViewController (AppKit), NSSplitView.DividerStyle (AppKit)

### Tab views
Full page: hig/components/tab-views.md · Platforms: macos,watchos
A tab view presents mutually exclusive panes in one area, switched by a tabbed control on the top edge of the content area. macOS and watchOS only; in iOS/iPadOS use a segmented control; in watchOS tab views display as page controls.

**Rules**
- **Use a tab view for closely related areas of content** — the enclosure signals that each tab's content is similar or related.
- **Ensure controls in a pane affect only that pane**; panes are self-contained.
- **Label each tab with what its pane contains**: nouns or short noun phrases (a verb phrase occasionally), title-style capitalization.
- **Avoid a pop-up button to switch tabs** — it needs two clicks instead of one and hides the choices; acceptable only when there are too many panes to show as tabs.
- **Avoid more than six tabs**; with six or more, use another approach, e.g. a pop-up button menu of view options.
- **You can hide the tabbed control** when switching panes programmatically; the content area can then be borderless (solid or transparent), bezeled, or bordered with a line.
- **Inset the tab view with a margin of window-body area on all sides**; extending it to the window edges is unusual.

**Platform notes**
- iOS/iPadOS: not supported — use a segmented control · tvOS/visionOS: not supported · watchOS: tab views display using page controls (TabView).

**Dev refs**
TabView (SwiftUI), NSTabView (AppKit)

## Menus and actions

### Activity views
Full page: hig/components/activity-views.md · Platforms: ios,ipados,visionos
An activity view (share sheet) presents sharing activities (messaging), actions (Copy, Print), and frequently used apps, usually from an Action/Share button, as a sheet or popover depending on device and orientation. The system lists app-specific actions before cross-app/system ones; people can edit the list. Share and action app extensions let your activities appear in other apps — including on macOS, which has no activity view of its own. Not supported in tvOS or watchOS.

**Rules**
- **Don't duplicate common actions already in the activity view** (a second Print is confusing); if similar app-specific functionality is needed, give it a distinct custom title ("Print Transaction").
- **Consider an SF Symbol for a custom activity**; a custom interface icon should be centered in an area of about 70x70 pixels.
- **Write a succinct, descriptive title for each custom action**: a single verb or brief verb phrase; long titles wrap and may truncate; no company or product name (a share activity, by contrast, shows its company name below its icon).
- **Make activities appropriate to the context**: you can't reorder system tasks, but you can exclude inapplicable ones (e.g. Print) and decide which custom tasks appear when.
- **Use the Share button to display an activity view**; don't invent an alternative route.
- **Share/action extensions — keep a custom interface familiar**: share extensions should use the system composition view; action extensions should include your app name and elements of your app's interface.
- **Streamline and limit interaction** in extensions (e.g. post an image with a single tap).
- **Avoid placing a modal view above your extension** (the extension is already modal; an alert may be necessary, more modals are not).
- **Provide an image that communicates purpose if necessary**: share extensions automatically use your app icon; for action extensions prefer a symbol or an interface icon that identifies the task.
- **Use your main app to show progress of a lengthy operation**: the activity view dismisses immediately after the task; continue work in the background, let people check status in the app; a notification may report a problem but never mere completion.

**Platform notes**
- iOS/iPadOS: share and action extensions appear in the share sheet from the Action button · macOS: share extensions via the toolbar Share button or Share in a context menu; action extensions by hovering over embedded content (e.g. an image in a Mail compose window), a toolbar button, or a Finder quick action · visionOS: no additional considerations.

**Dev refs**
UIActivityViewController (UIKit), UIActivity (UIKit), App Extension Support (Foundation)

### Buttons
Full page: hig/components/buttons.md · Platforms: ios,ipados,macos,tvos,visionos,watchos · Latest change 2025-12-16: updated for Liquid Glass
A button initiates an instantaneous action and combines style (size, color, shape), content (symbol/icon, text, or both), and role (system semantic meaning). Toggles, pop-up buttons, and segmented controls are distinct button-like components with their own guidance.

**Rules**
- **Give every button a hit region of at least 44x44 pt — 60x60 pt in visionOS** — and enough surrounding space to distinguish and activate it with finger, pointer, eyes, or remote.
- **Always include a press state for a custom button**; otherwise it feels unresponsive.
- **Use a prominent style for the most likely action in a view** so the system applies the accent color to its background; keep prominent buttons to one or two per view to limit cognitive load.
- **Use style, not size, to distinguish the preferred choice.** Same-size buttons read as a coherent set; different sizes side by side look inconsistent. Give the preferred option a more prominent style and the rest a less prominent one.
- **Avoid a similar color on button labels and the content-layer background.** With bright, colorful content, prefer the default monochromatic label appearance (see Liquid Glass color).
- **Ensure each button clearly communicates its purpose** via symbol, text, or both. In macOS and visionOS a tooltip appears after hovering; keep it a brief phrase.
- **Associate familiar actions with familiar icons** (square.and.arrow.up for share); use existing or customized SF Symbols; see Standard icons.
- **Use text when a short label is clearer than an icon**: a few words, title-style capitalization, ideally starting with a verb ("Add to Cart").
- **Roles** — a system button has one of four, and the role can affect appearance:
  - Normal: no specific meaning.
  - Primary: the default button, the one people are most likely to choose; uses the app's accent color.
  - Cancel: cancels the current action.
  - Destructive: performs an action that can destroy data; uses the system red color.
- **Assign the primary role to the button people are most likely to choose**; it responds to Return, and in a sheet, editable view, or alert the view can close automatically on Return.
- **Never assign the primary role to a destructive button**, even if it's the likely choice — people press primary buttons without reading.

**Platform notes**
- iOS/iPadOS: configure a button to show an activity indicator for an action that doesn't complete instantly, optionally with an alternate label ("Checkout" → "Checking out…"); the indicator appears beside the label and the button image is hidden · tvOS: no additional considerations.
- macOS — push buttons: the standard macOS button; displays text, a symbol, an icon, an image, or text plus image; can act as the default button in a view; can be tinted.
- macOS — use a flexible-height push button only for tall or variable-height content (two lines of text, a tall icon); it supports the same configurations and uses the same corner radius and content padding as a regular push button, so it stays consistent (NSButton.BezelStyle.flexiblePush).
- macOS — append a trailing ellipsis to a push button title when it opens another window, view, or app; system-wide, an ellipsis signals that people can provide additional input (Safari AutoFill Edit buttons).
- macOS — consider supporting spring loading: with a Magic Trackpad, people activate a button by dragging selected items over it and force clicking, without dropping the items, then continue dragging.
- macOS — square (gradient) buttons: initiate an action related to a view (adding or removing table rows); contain symbols or icons, never text; can behave as push buttons, toggles, or pop-up buttons; appear within or beneath the view they affect.
- macOS — use square buttons in a view, not in the window frame — not in toolbars or status bars (use a toolbar item there).
- macOS — prefer an SF Symbol in a square button; symbols receive appropriate coloring by default and in response to interaction.
- macOS — don't introduce square buttons with labels; their close connection to the view makes their purpose clear (NSButton.BezelStyle.smallSquare).
- macOS — help buttons: circular, consistently sized, contain a question mark, and open app-specific help documentation (see Offering help).
- macOS — use the system-provided help button; people recognize it and know it opens help content.
- macOS — open the help topic related to the current context when possible (the Mail Rules settings help button opens the matching User Guide topic); if no topic applies, open the top level of your help.
- macOS — include no more than one help button per window; several in one context make the result unpredictable.
- macOS — position help buttons where people expect them (Specs table); keep them in the view, not the window frame (no toolbar or status bar); don't add text introducing a help button.
- macOS — image buttons: appear in a view and display an image, symbol, or icon; can behave as push, toggle, or pop-up buttons.
- macOS — use an image button in a view, not in the window frame (no toolbar or status bar); for an image as a button in a toolbar, use a toolbar item.
- macOS — include about 10 pixels of padding between the image edges and the button edges — the button edges define the clickable area even when invisible, so padding ensures clicks register; generally avoid a system-provided border (isBordered).
- macOS — if an image button needs a label, position it below the button.
- visionOS: a button typically includes a visible background and plays sound as feedback on interaction; use standard controls to get the audible feedback people know — the system plays no haptics.
- visionOS: three standard shapes — icon-only buttons use the circle shape; text-only buttons use roundedRectangle or capsule; buttons with icon and text use capsule.
- visionOS: four interaction states — idle, hover, selected, unavailable; buttons don't support custom hover effects; a button can also reveal a tooltip when people look at it briefly, though text buttons generally don't need one.
- visionOS: prefer buttons with a discernible background shape and contrasting fill; the exception is a button in a toolbar, context menu, alert, or ornament, whose shape and material already make the button comfortably visible.
- visionOS: on top of a glass window use the thin material as the button background; floating in space use the glass material.
- visionOS: never create a custom button with a white background fill and black text or icons — the system reserves that style to convey the toggled state.
- visionOS: prefer circular or capsule shapes — eyes are drawn to corners, so rounder shapes are easier to look at steadily; a button displayed by itself should be a capsule.
- visionOS: place buttons so their centers are at least 60 pt apart; for buttons measuring 60 pt or larger add 4 pt of padding around them so hover effects don't overlap; avoid displaying small or mini buttons in a vertical stack or horizontal row.
- visionOS: for text-labeled buttons in a stack or row, prefer the rounded-rectangle shape in a vertical stack and the capsule shape in a horizontal row.
- watchOS: all inline buttons use the capsule shape; an inline button gains a material effect that contrasts with the background to ensure legibility.
- watchOS: use a toolbar to place buttons in the corners — the system moves the time and title to accommodate them and applies Liquid Glass to toolbar buttons for clear visual distinction from content beneath.
- watchOS: prefer buttons that span the screen width for primary actions — they look better and are easier to tap; if two buttons must share the same horizontal space, give both the same height and use images or short text titles.
- watchOS: use toolbar buttons for navigation to related areas or for contextual actions on the view's content (additional information or secondary actions).
- watchOS: use the same height throughout a vertical stack of one- and two-line text buttons.

**Specs**

Help button location (macOS):

| View style | Help button location |
|---|---|
| Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
| Dialog without dismissal buttons | Lower-left or lower-right corner |
| Settings window or pane | Lower-left or lower-right corner |

visionOS button sizes (the source table shows an image of each shape at each size; ✓ marks a shape/size combination the page illustrates):

| Shape | Mini (28 pt) | Small (32 pt) | Regular (44 pt) | Large (52 pt) | Extra large (64 pt) |
|---|---|---|---|---|---|
| Circular | ✓ | ✓ | ✓ | ✓ | ✓ |
| Capsule (text only) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Capsule (text and icon) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Rounded rectangle | ✓ | ✓ | ✓ | ✓ | ✓ |

Other numbers: minimum hit region 44x44 pt (visionOS 60x60 pt); visionOS button centers ≥ 60 pt apart, +4 pt padding around buttons ≥ 60 pt; macOS image button padding ≈ 10 px.

**Dev refs**
Button (SwiftUI), ButtonBorderShape.circle / .roundedRectangle / .capsule (SwiftUI), Material.thin (SwiftUI), UIButton (UIKit), NSButton (AppKit), NSButton.BezelStyle.flexiblePush, NSButton.BezelStyle.smallSquare, NSButton.isBordered (AppKit)

### Context menus
Full page: hig/components/context-menus.md · Platforms: ios,ipados,macos,tvos,visionos
A context menu gives access to functionality directly related to an item without cluttering the interface; it's hidden by default. Revealed by touch-and-hold / pinch-and-hold (iOS, iPadOS, visionOS), Control-click (macOS, iPadOS), or secondary click on a Magic Trackpad (macOS, iPadOS). Not supported in watchOS. Not for advanced or rarely used items.

**Rules**
- **Prioritize relevancy**: include the commands people most likely need in the current context (Mail Inbox message: reply, move — not edit content or manage mailboxes).
- **Aim for a small number of items**; long menus are hard to scan and scroll.
- **Support context menus consistently throughout the app**; inconsistent availability looks broken.
- **Always make context-menu items available in the main interface too** (toolbar; in macOS, the menu bar lists all commands).
- **Keep submenus to one level** and give each an intuitive title that predicts its contents.
- **Hide unavailable items; don't dim them** — a context menu shows only actions relevant to the current selection. macOS exception: Cut, Copy, and Paste may appear unavailable.
- **Put the most frequently used items where people read first** — nearest the finger/pointer. Because the menu may open above or below the content, you may need to reverse item order to match.
- **Show keyboard shortcuts in the app's main menus, not in context menus.**
- **Use separators to group items; aim for no more than about three groups.**
- **In iOS, iPadOS, and visionOS, list destructive items (Delete, Remove) last and mark them destructive** so the system can show red text.
- **Include a title only if it clarifies the menu's effect** (e.g. the number of selected Mail messages when tapping Mark). Each item needs a short, clear label (see Menus > Labels).
- **Represent actions with familiar icons** — the same icons the system uses for Copy, Share, Delete (Standard icons).

**Platform notes**
- iOS/iPadOS: provide either a context menu or an edit menu for an item, never both — it confuses people and makes it hard for the system to detect intent.
- iPadOS: consider a context menu to let people create a new object — revealed by a long press on the touchscreen or a secondary click with a trackpad/keyboard (Files creates a folder from a context menu in the space between items).
- iOS/iPadOS: a context menu can display a preview of the content near the list of commands; people can choose a command or, in some cases, tap the preview to open it or drag it to another area.
- iOS/iPadOS: prefer a graphical preview that clarifies the target of the commands (Notes and Mail show a condensed version of the content so people confirm the item).
- iOS/iPadOS: ensure the preview looks good as it animates — the system animates it emerging from the content while dimming the screen behind the preview and menu; adjust the preview's clipping path to match the preview image's shape so contours like rounded corners don't appear to change (UIContextMenuInteractionDelegate).
- macOS: a context menu is sometimes called a contextual menu.
- tvOS: no additional considerations.
- visionOS: consider a context menu instead of a panel or inspector window for frequently used functionality — fewer separate views keep the space uncluttered.
- visionOS: avoid letting a context menu's height exceed the window's height — system components sit above and below the window edges (window-management controls, the Share menu) and a tall menu could obscure them; size the item count to how people use the app: specialist apps can justify many sophisticated commands, simple apps want short, scannable menus.

**Dev refs**
contextMenu(menuItems:) (SwiftUI), UIContextMenuInteraction (UIKit), UIContextMenuInteractionDelegate (UIKit), UIMenuElement.Attributes.destructive (UIKit), popUpContextMenu(_:with:for:) (AppKit)

### Dock menus
Full page: hig/components/dock-menus.md · Platforms: macos
Secondary-clicking an app or game icon in the macOS Dock reveals a Dock menu of system-provided items (which vary with whether the app is open) and custom items. iOS/iPadOS have no Dock menu; the equivalent is Home Screen quick actions.

**Rules**
- **Label Dock menu items succinctly and organize them logically** (same rules as all menus).
- **Make custom Dock menu items available elsewhere too** (menu bar menus, in-app) — not everyone uses the Dock menu.
- **Prefer high-value custom items**: list open or recently open windows for quick jumping, plus a few actions useful when the app isn't frontmost or has no windows (Mail: get new mail, compose).

**Dev refs**
applicationDockMenu(_:) (AppKit)

### Edit menus
Full page: hig/components/edit-menus.md · Platforms: ios,ipados,macos,visionos
An edit menu lets people change selected content — text, images, files, contact cards, charts, map locations — and offers related commands like Copy, Select, Translate, and Look Up. In iOS, iPadOS, and visionOS the system detects the data type of a selection and may add a related action (an address adds Get directions). tvOS and watchOS provide no edit menu because editing is rare there.

**Rules**
- **Prefer the system-provided edit menu**; a custom menu with the same commands is redundant and confusing (standard commands: UIResponderStandardEditActions).
- **Let people reveal it with the system interactions they know** (touch and hold, pinch and hold, secondary click); never require a custom interaction for a standard task.
- **Offer only commands relevant in context; remove or dim the rest** — no Copy/Cut with nothing selected, no Paste with nothing to paste.
- **List custom commands near the related system commands** (custom formatting after the system format section); don't overwhelm with custom commands.
- **Let people select and copy noneditable text when it makes sense** (captions, statuses) — content text, not control labels.
- **Support undo and redo**; edit menus act without confirmation, so recovery matters.
- **Avoid other controls that duplicate edit-menu items**; people expect the menu or standard shortcuts, and redundant controls crowd the interface.
- **Differentiate deletion commands when necessary**: Delete behaves like the Delete key; Cut copies to the pasteboard before deleting.
- **Write short labels for custom commands**: verbs or short verb phrases.

**Platform notes**
- iOS: the edit menu is a compact horizontal list that appears on touch-and-hold or double-tap selection; a chevron on the trailing edge expands it into a context menu.
- iPadOS: touch reveals the compact horizontal appearance; a keyboard or pointing device opens the edit menu directly as a context menu.
- iOS/iPadOS: ensure the edit menu works in both styles — compact horizontal for Multi-Touch gestures and vertical for keyboard or pointing device (see Menus > iOS, iPadOS).
- iOS/iPadOS: adjust placement if necessary — by default the menu appears above or below the insertion point or selection with a visual indicator pointing at the target; you can't change the menu's shape or its pointer, but you can move it to avoid covering important content or interface.
- macOS: editing commands appear in a context menu during an editing task and in the app's Edit menu in the menu bar; follow the Edit menu item order in The menu bar.
- visionOS: the standard pinch-and-hold gesture opens the edit menu as a horizontal bar, or people open it in a context menu; no additional considerations.

**Dev refs**
UIEditMenuInteraction (UIKit), UIResponderStandardEditActions (UIKit), NSMenu (AppKit)

### Home Screen quick actions
Full page: hig/components/home-screen-quick-actions.md · Platforms: ios,ipados
Touching and holding an app icon (or pressing with increased pressure on 3D Touch devices) shows a menu of app-specific quick actions plus system items for removing the app and editing the Home Screen. Each action has a title, an interface icon on the left or right (depending on the icon's position), and an optional subtitle; title and subtitle are left-aligned in left-to-right languages. Actions can update dynamically (Messages lists recent conversations).

**Rules**
- **Create quick actions for compelling, high-value tasks** (Maps: search nearby, directions home); people expect at least one, and you can provide a total of four.
- **Avoid unpredictable changes to dynamic quick actions**; updating for location, recent activity, time of day, or settings is fine if the changes are predictable.
- **Give each action a succinct title that states the result** ("Directions Home", "Create New Contact", "New Message"); add a subtitle for context (Mail shows unread counts); no app name or extraneous text; keep short to avoid truncation; account for localization.
- **Provide a familiar interface icon**; prefer SF Symbols (see Standard icons); for custom icons use the Quick Action Icon Template in Apple Design Resources for iOS and iPadOS.
- **Don't use an emoji in place of a symbol or icon** — quick-action icons are monochromatic and adapt to Dark Mode; emoji are full color.

**Dev refs**
Add Home Screen quick actions (UIKit)

### Menus
Full page: hig/components/menus.md · Platforms: ios,ipados,macos,tvos,visionos,watchos · Latest change 2026-06-08: menu item icon guidance
A menu reveals menu items — commands, options, or states affecting the current selection or context — when people interact with it. Labeling and organization guidance applies to every menu type (pop-up, pull-down, context, menu bar, in-game). An app menu item can show its keyboard command; a game's rarely does because it maps many input devices.

**Rules**
- **Write a clear, succinct label for each item**; for actions use a verb or verb phrase (View, Close, Select); let the app's communication style set tone.
- **Use title-style capitalization** (every word except articles, coordinating conjunctions, short prepositions; always capitalize the last word).
- **Remove articles (a, an, the)** from labels — they lengthen without clarifying.
- **Show when an item is unavailable** (dimmed, non-interactive). If all items are unavailable, the menu itself must still open so people can learn its commands.
- **Append an ellipsis (…) when the action needs more input** before it can complete.
- **Represent common actions with the standard system icons** (Share, Print, Search; see Standard icons).
- **Use item icons sparingly and purposefully**: for the most common actions, key features, file-system locations, connected devices, visual concepts (rotate, flip), and user-generated content (folders, documents). Omit an icon if none clearly represents the item.
- **Apply a uniform treatment within a group**: icons for every item in the group, or none.
- **List important or frequently used items first**; people scan from the top.
- **Group logically related items** (Copy/Cut/Paste; Look Up/Down/Left) with separators (a horizontal line or a gap in the background, by platform and menu type).
- **Keep all related commands in one group even when their importance differs** (Paste and Match Style lives with Paste, Copy, Cut).
- **Be mindful of length**: divide a long menu into separate menus or use a submenu (difficulty levels under New Game). Exception: user-defined or dynamically generated content (Safari History, Bookmarks) may be long and scroll.
- **Use submenus sparingly**; consider one when a term repeats in more than two items of a group (Sort by Date/Score/Time → Sort by ▸ Date, Score, Time) and reuse the repeated term as the parent label.
- **Limit submenus to a single level**; if a submenu has more than about five items, consider a new menu.
- **Keep a submenu available even when its nested items are unavailable.**
- **Prefer a submenu to indenting items**; indentation is inconsistent with the system.
- **Toggled items — consider a changeable label that describes the current state** (one item whose label switches between Show Map and Hide Map) instead of two items.
- **Include a verb if a changeable label isn't clear enough** (HDR On / HDR Off could be states; Turn HDR On / Turn HDR Off are clearly actions).
- **Display both items instead of one toggled item when seeing both states helps** (Take Account Online and Take Account Offline, with only the applicable one available).
- **Consider a checkmark to show an attribute currently in effect** (Format > Font styles applied to selected text) — easy to scan.
- **Consider an item that removes multiple toggled attributes at once** (Plain clears all applied formatting).
- **In-game menus: let players navigate with the platform's default interaction** (touch in iOS/iPadOS; direct and indirect gestures in visionOS) — the same interactions they use for other menus on the device.
- **Keep in-game menus easy to open and read on every platform**: scaling game content to a different screen, especially a mobile one, can make menus too small — enlarge tap targets and consider other ways to communicate the menu's content (see Typography, Touch controls).

**Platform notes**
- iOS/iPadOS: three menu layouts — Small: a row of four items at the top (symbol or icon only, no label) above a list of the remaining items; Medium: a row of three items at the top (symbol/icon above a short label) above the list; Large (default): all items in a list (UIMenu.preferredElementSize).
- iOS/iPadOS: choose a small or medium layout when it streamlines choices — medium for three important actions people often perform (Notes: Scan, Lock, Pin); small only for closely related actions that typically appear as a group (Bold, Italic, Underline, Strikethrough), each with a recognizable symbol that works without a label.
- visionOS: menus use the small or large layouts; you can present a menu from 3D content using a SwiftUI view; as in macOS, an open menu in a window can extend outside the window's boundaries.
- visionOS: prefer displaying a menu near the content it controls — people look at an item before tapping and may miss its effect if the content is far away.
- visionOS: prefer the subtle breakthrough effect in most cases to keep a menu visible when other content occludes it — it blends the presentation with surroundings while preserving depth; automatic resolves to subtle when the menu overlaps 3D content; prominent displays the menu over the entire scene but can disrupt the experience and cause discomfort; none fully occludes the menu behind 3D content (e.g. a puzzle game with barriers) at the cost of visibility and access.
- macOS/tvOS/watchOS: no additional considerations.

**Dev refs**
Menu (SwiftUI), presentationBreakthroughEffect(_:) (SwiftUI), BreakthroughEffect.automatic / .subtle / .prominent / .none (SwiftUI), Menus and shortcuts (UIKit), UIMenu.preferredElementSize (UIKit), Menus (AppKit)

### Ornaments
Full page: hig/components/ornaments.md · Platforms: visionos
An ornament floats in a plane parallel to and slightly in front of its window (along z), moves with the window, and keeps its content fixed while the window scrolls. It can sit on any window edge and hold buttons, segmented controls, and other views. The system builds toolbars, tab bars, and video playback controls as ornaments; use a custom ornament only for custom components. visionOS only.

**Rules**
- **Consider an ornament for frequently needed controls or information in a consistent, uncluttered location** (Music's Now Playing controls).
- **Keep an ornament visible in general**; hide it only when people dive into content (watching a video, viewing a photo).
- **With multiple ornaments, prioritize the window's visual balance**: constrain the total number to avoid visual weight and complexity; relocate a removed ornament's elements into the main window.
- **Keep an ornament's width the same as or narrower than its window**; a wider one interferes with a tab bar or other vertical content on the window's side.
- **Consider borderless buttons** — the ornament background is glass, so buttons placed directly on it may not need a border, and the system applies the hover effect when people look at them.
- **Use the system toolbars and tab bars** (they already appear as ornaments) unless you need a custom component.

**Dev refs**
ornament(visibility:attachmentAnchor:contentAlignment:ornament:) (SwiftUI), Toolbars (SwiftUI), TabView (SwiftUI)

### Pop-up buttons
Full page: hig/components/pop-up-buttons.md · Platforms: ios,ipados,macos,visionos
A pop-up button shows a menu of mutually exclusive options; after a choice the menu closes and the button can update to show the selection. Not supported in tvOS or watchOS. Use a pull-down button instead for a list of actions, multiple selection, or a submenu.

**Rules**
- **Use a pop-up button for a flat list of mutually exclusive options or states** that affect content or the surrounding view.
- **Provide a useful default selection** — the item most people want — shown until a choice is made.
- **Let people predict the options without opening the menu** via an introductory label or a button label describing its effect.
- **Consider a pop-up button when space is limited** and all options needn't be visible at once.
- **Include a Custom option when occasional extra items are needed** to avoid cluttering the interface; explanatory text may appear below the list.

**Platform notes**
- iPadOS: within a popover or modal view, consider a pop-up button instead of a disclosure indicator for a list item with a small, well-defined set of options so people choose without navigating to a detail view · iOS/macOS/visionOS: no additional considerations.

**Dev refs**
MenuPickerStyle (SwiftUI), UIButton.changesSelectionAsPrimaryAction (UIKit), NSPopUpButton (AppKit)

### Pull-down buttons
Full page: hig/components/pull-down-buttons.md · Platforms: ios,ipados,macos,visionos
A pull-down button shows a menu of items or actions that directly relate to the button's purpose; choosing one closes the menu and performs the action. Not supported in tvOS or watchOS. For mutually exclusive choices that aren't commands, use a pop-up button.

**Rules**
- **Use a pull-down button for commands directly related to the button's action** — Add ▸ what to add; Sort ▸ attribute; Back ▸ a specific location to revisit — to avoid extra buttons.
- **Don't put all of a view's actions in one pull-down button**; primary actions must stay discoverable.
- **Balance menu length**: list a minimum of three items to make opening worthwhile; for one or two items use buttons, toggles, or switches instead; too many items slow people down.
- **Show a succinct menu title only if it adds meaning**; the button plus descriptive items usually suffice.
- **Flag destructive items and ask for confirmation**: menus show destructive actions in red; on choosing one the system presents an action sheet (iOS) or popover (iPadOS) to confirm or cancel.
- **Include an icon or image after an item's label when it clarifies meaning**; SF Symbols stay aligned with text at every scale.

**Platform notes**
- iOS/iPadOS: a gesture on a button can reveal its pull-down menu (iOS 14+: touch and hold Safari's Tabs button shows New Tab, Close All Tabs); consider a More (ellipsis) pull-down button for items that don't need prominent positions, but weigh its compactness against reduced discoverability — the ellipsis doesn't predict contents · macOS/visionOS: no additional considerations.

**Dev refs**
MenuPickerStyle (SwiftUI), UIControl.showsMenuAsPrimaryAction (UIKit), NSPopUpButton.pullsDown (AppKit)

### The menu bar
Full page: hig/components/the-menu-bar.md · Platforms: ipados,macos · Latest change 2025-06-09: iPadOS menu bar guidance
On Mac and iPad the menu bar at the top of the screen shows an app's top-level menus; iPad menus use the same order, item sets, and keyboard-shortcut patterns as Mac. Menu order: *YourAppName*, File, Edit, Format, View, app-specific menus, Window, Help — plus, in macOS, the Apple menu on the leading side and menu bar extras on the trailing side. Not supported in iOS, tvOS, visionOS, watchOS. General labeling/organization rules are in Menus.

**Rules**
- **Support the default system-defined menus and their ordering**; the system often implements standard items for you (Edit > Copy for text fields).
- **Always show the same set of menu items**; disable unavailable items rather than hiding them so people learn what the app supports.
- **Represent actions with familiar icons** — the same system icons for Copy, Share, Delete (Standard icons).
- **Support the standard keyboard shortcuts** for standard items (Copy, Cut, Paste, Save, Print); define custom shortcuts only when necessary.
- **Prefer short, one-word menu titles**; multi-word titles use title-style capitalization. Spacing varies with display size and menu bar extras.
- **App menu**: lists app-wide items; the app name appears in bold. Display About first, followed by a separator so it sits alone in its group. Items and order in Specs.
- **File menu**: commands for managing files/documents; rename or remove it if the app handles no files. Items in Specs.
- **Edit menu**: content editing and Clipboard commands — useful even in non-document apps. Decide whether Find belongs here or in File (if it searches files/objects). Items in Specs.
- **Format menu**: text formatting; omit if the app doesn't edit formatted text. Items in Specs.
- **View menu**: customizes the appearance of all windows; it does not navigate or manage windows (that's Window). Provide a View menu even for a subset of functions (e.g. only Enter/Exit Full Screen). Each show/hide title must reflect current state (Show Toolbar when hidden, Hide Toolbar when visible). Items in Specs.
- **App-specific menus** go between View and Window. Provide them for custom commands even when available elsewhere — the menu bar is where people look, enables keyboard shortcuts, and serves Full Keyboard Access; excluding commands makes them hard to find. Reflect app hierarchy in order (Mail: Mailbox, Message, Format). List from most to least general/commonly used.
- **Window menu**: navigate, organize, manage windows; it doesn't customize appearance or close windows. Provide it even for a single-window app, with Minimize and Zoom for Full Keyboard Access. Consider items to show/hide panels (not the font or text color panels — Format covers those). Items in Specs.
- **Help menu** at the trailing end; Help Book format adds an automatic search field. Separate primary help from additional items (registration, release notes) with a separator; keep the item count small or link from within help. Items in Specs.
- **Dynamic menu items** (behavior changes while holding Control, Option, Shift, or Command — Minimize → Minimize All): never make one the only way to do a task; use them primarily in menu bar menus, not context or Dock menus; require only a single modifier key (isAlternate). macOS sizes a menu to its widest item including dynamic ones.

**Platform notes**
- iPadOS: people reveal the menu bar by moving the pointer to the top edge of the screen or swiping down from it; when visible it occupies the same vertical space as the status bar. Differences from macOS in Specs.
- iPadOS: because the menu bar is often hidden when an app runs full screen, ensure people can access all of the app's functions through its UI — in particular always offer other ways to do tasks assigned to dynamic menu items, which are available only with a hardware keyboard; don't use the menu bar as a catch-all for functionality that fits nowhere else.
- iPadOS: reserve *YourAppName* > Settings for opening the app's page in iPadOS Settings; if the app has an internal preferences area, link to it with a separate item beneath Settings in the same group, and place other custom app-wide configuration options in that section too.
- iPadOS: for apps with tab-style navigation, consider adding each tab as an item in the View menu — a natural extra way to navigate — and consider assigning a key binding to each tab.
- iPadOS: consider grouping items into submenus more often than on Mac to conserve vertical space — iPad menu rows use more space to make tapping easier, and some iPad screens are small.
- macOS: the Apple menu is always the first item on the leading side, with system-defined items that are always available; you can't modify or remove it.
- macOS: when menu bar space is constrained the system prioritizes menus and essential menu bar extras, may decrease the space between titles, and truncates them if necessary.
- macOS: in full-screen mode the menu bar typically hides until people move the pointer to the top of the screen (see Going full screen).
- macOS — menu bar extras: an icon on the trailing side of the menu bar that exposes app-specific functionality while the app runs, even when it isn't frontmost; the system hides extras when it needs room for app menus, and may hide some when there are too many.
- macOS — consider a symbol for a menu bar extra: create an icon or use an SF Symbol as-is or customized; both use black and clear to define their shape so the system can recolor the black areas for dark and light menu bars and for the selected state. The menu bar's height is 24 pt.
- macOS — display a menu, not a popover, when people click a menu bar extra, unless the functionality is too complex for a menu.
- macOS — let people, not the app, decide whether the extra appears in the menu bar — typically via the app's settings window; consider offering the option during setup for discoverability.
- macOS — avoid relying on the presence of menu bar extras: the system hides and shows them regularly, and you can't predict which other extras people show or where yours appears.
- macOS — consider exposing the same functionality in other ways too, e.g. a Dock menu, which is always available while the app runs even if people hide or ignore the menu bar extra.

**Specs**

App menu (in order):

| Menu item | Action | Guidance |
|---|---|---|
| About *YourAppName* | Displays the About window (copyright, version). | Prefer a short name of 16 characters or fewer. Don't include a version number. |
| Settings… | Opens the settings window, or the app's page in iPadOS Settings. | Only app-level settings; document-specific settings go in File. |
| Optional app-specific items | Custom app-level setting/configuration actions. | List after Settings, in the same group. |
| Services (macOS only) | Submenu of services from the system and other apps for the current context. | |
| Hide *YourAppName* (macOS only) | Hides the app and its windows; activates the most recently used app. | Use the same short app name as About. |
| Hide Others (macOS only) | Hides all other open apps and windows. | |
| Show All (macOS only) | Shows all other apps' windows behind yours. | |
| Quit *YourAppName* | Quits. Option changes it to Quit and Keep Windows. | Use the same short app name as About. |

File menu (in order):

| Menu item | Action | Guidance |
|---|---|---|
| New *Item* | Creates a new document, file, or window. | Name the item type the app creates (Calendar: Event, Calendar). |
| Open | Opens the selected item or presents a chooser. | Ellipsis follows the command when a separate chooser is needed. |
| Open Recent | Submenu of recently opened documents, typically with Clear Menu. | Show recognizable names, not paths; most recently opened first. |
| Close | Closes the current window/document. Option → Close All. In a tab-based window, Close Tab replaces Close. | In a tab-based window, consider adding Close Window. |
| Close Tab | Closes the current tab. Option → Close Other Tabs. | |
| Close File | Closes the file and all its windows. | Support if the app opens multiple views of one file. |
| Save | Saves the document. | Autosave periodically; prompt for name and location for a new document; for multiple formats, prefer a pop-up menu in the Save sheet. |
| Save All | Saves all open documents. | |
| Duplicate | Duplicates the document, leaving both open. Option → Save As. | Prefer Duplicate to Save As, Export, Copy To, Save To — those don't clarify the original/new relationship. |
| Rename… | Renames the current document. | |
| Move To… | Prompts for a new location. | |
| Export As… | Prompts for name, location, and format; current document stays open, export doesn't open. | Reserve for formats the app doesn't typically handle. |
| Revert To | With autosave on, submenu of recent versions plus the version browser; the chosen version replaces the document. | |
| Page Setup… | Panel for document-specific printing parameters (paper size, orientation), savable with the document. | Include only for per-document parameters; global (printer name) or frequently changed (copies) parameters belong in the Print panel. |
| Print… | Opens the standard Print panel (print, fax, save as PDF). | |

Edit menu (in order):

| Menu item | Action | Guidance |
|---|---|---|
| Undo | Reverses the previous user operation. | Clarify the target: Undo Paste and Match Style; Undo Typing for text entry. |
| Redo | Reverses the previous Undo. | Clarify the target: Redo Paste and Match Style; Redo Typing. |
| Cut | Removes selection to the Clipboard, replacing its contents. | |
| Copy | Duplicates selection to the Clipboard. | |
| Paste | Inserts Clipboard contents at the insertion point; Clipboard unchanged so Paste repeats. | |
| Paste and Match Style | Pastes, matching surrounding text style. | |
| Delete | Removes selection without placing it on the Clipboard. | Use Delete, not Erase or Clear — it equals pressing the Delete key. |
| Select All | Highlights all selectable content. | |
| Find | Submenu: Find, Find and Replace, Find Next, Find Previous, Use Selection for Find, Jump to Selection. | |
| Spelling and Grammar | Submenu: Show Spelling and Grammar, Check Document Now, Check Spelling While Typing, Check Grammar With Spelling, Correct Spelling Automatically. | |
| Substitutions | Submenu: Show Substitutions, Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, Text Replacement. | |
| Transformations | Submenu: Make Uppercase, Make Lowercase, Capitalize. | |
| Speech | Submenu: Start Speaking, Stop Speaking. | |
| Start Dictation | Opens dictation; system adds it automatically at the bottom of Edit. | |
| Emoji & Symbols | Opens the Character Viewer; system adds it automatically at the bottom of Edit. | |

Format menu (in order):

| Menu item | Action |
|---|---|
| Font | Submenu: Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy Style, Paste Style. |
| Text | Submenu: Align Left, Align Center, Justify, Align Right, Writing Direction, Show Ruler, Copy Ruler, Paste Ruler. |

View menu (in order):

| Menu item | Action |
|---|---|
| Show/Hide Tab Bar | Toggles the tab bar above the body area in a tab-based window. |
| Show All Tabs/Exit Tab Overview | Enters/exits a Mission Control-like overview of all open tabs. |
| Show/Hide Toolbar | Toggles toolbar visibility. |
| Customize Toolbar | Opens the toolbar customization view. |
| Show/Hide Sidebar | Toggles sidebar visibility. |
| Enter/Exit Full Screen | Opens the window full-screen in a new space (apps supporting full screen). |

Window menu (in order):

| Menu item | Action | Guidance |
|---|---|---|
| Minimize | Minimizes the active window to the Dock. Option → Minimize All. | |
| Zoom | Toggles between a content-appropriate size and the user-set size. Option → Zoom All. | Don't use Zoom for full screen; the View menu does that. |
| Show Previous Tab | Shows the previous tab in a tab-based window. | |
| Show Next Tab | Shows the next tab. | |
| Move Tab to New Window | Opens the current tab in a new window. | |
| Merge All Windows | Combines all open windows into one tabbed window. | |
| Enter/Exit Full Screen | Opens the window full-screen in a new space. | Include here only if the app has no View menu; still keep separate Minimize and Zoom. |
| Bring All to Front | Brings all the app's windows forward, preserving position, size, layering (same as clicking the Dock icon). Option → Arrange in Front (tiled). | |
| *Name of an open app-specific window* | Brings that window to the front. | List open windows alphabetically; omit panels and modal views. |

Help menu:

| Menu item | Action | Guidance |
|---|---|---|
| Send *YourAppName* Feedback to Apple | Opens Feedback Assistant. | |
| *YourAppName* Help | Opens Help Book content in the Help Viewer. | |
| *Additional Item* | | Separator between primary help and additional items (registration, release notes); keep the total small or link from within help. |

iPadOS vs macOS menu bar:

| | iPadOS | macOS |
|---|---|---|
| Menu bar visibility | Hidden until revealed | Visible by default |
| Horizontal alignment | Centered | Leading side |
| Menu bar extras | Not available | System default and custom |
| Window controls | In the menu bar when the app is full screen | Never in the menu bar |
| Apple menu | Not available | Always available |
| App menu | About, Services, and app visibility-related items not available | Always available |

Other numbers: About name ≤ 16 characters; macOS menu bar height 24 pt; one modifier key per dynamic item.

**Dev refs**
CommandMenu (SwiftUI), MenuBarExtra (SwiftUI), Adding menus and shortcuts to the menu bar and user interface (UIKit), NSStatusBar (AppKit), NSMenuItem.isAlternate (AppKit), NSHelpManager (AppKit)

### Toolbars
Full page: hig/components/toolbars.md · Platforms: ios,ipados,macos,tvos,visionos,watchos · Latest change 2025-12-16: updated for Liquid Glass
A toolbar is one or more sets of controls along the top or bottom edge of a view, grouped into logical sections, holding three kinds of content: the view title, navigation controls (back/forward, search fields), and actions/bar items (buttons, menus). In iOS a navigation-specific toolbar is sometimes called a navigation bar. A tab bar, by contrast, is only for navigating between app areas.

**Rules**
- **Choose items deliberately to avoid overcrowding**; define which items move to the overflow menu as the toolbar narrows.
- **Never add an overflow menu manually** — macOS and iPadOS add one automatically when items no longer fit — and avoid layouts that overflow by default.
- **Add a More menu for additional, less important actions** only if really needed; try to fit all actions in the toolbar first.
- **In iPadOS and macOS, consider letting people customize the toolbar** — valuable for apps with many items, advanced functionality, or long sessions (e.g. a range of editing actions).
- **Reduce toolbar backgrounds and tinted controls.** Custom backgrounds can interfere with system background effects; let the content layer inform the toolbar's color and use a ScrollEdgeEffectStyle when the toolbar area needs distinguishing from content.
- **Avoid a similar color on toolbar item labels and the content-layer background**; with bright colorful content prefer the default monochromatic toolbar appearance (see Liquid Glass color).
- **Prefer standard components in a toolbar** — standard buttons, text fields, headers, and footers have corner radii concentric with the bar's corners; a custom component must match that concentricity.
- **Consider temporarily hiding toolbars for a distraction-free experience**, contextually, with a reliable way to restore them (see Going full screen; visionOS: Immersive experiences).
- **Titles — provide a useful title for each window** to confirm location and distinguish windows; leave the title area empty when a title would be redundant (Notes with a single window; separate note windows are titled by first line).
- **Don't title windows with your app name.**
- **Write concise titles**: a word or short phrase, under 15 characters, leaving room for controls.
- **Navigation — use the standard Back and Close buttons** with their standard symbols, not text labels reading Back or Close; a custom version must look, behave, and be implemented consistently throughout the app.
- **Actions — provide actions that support people's main tasks**; prioritize the most likely commands (most frequent, or those mapping to the highest-level objects).
- **Make each control's meaning clear**: prefer simple, recognizable symbols over text, except for actions like edit that symbols represent poorly (see Standard icons).
- **Prefer system symbols without borders** (no outlined-circle variants) — the section provides the container and the system defines hover/selection states and vibrancy.
- **Use the `.prominent` style for key actions like Done or Submit**; specify only one primary action and put it on the trailing side.
- **Leading edge**: elements that return to the previous document and show/hide the sidebar sit at the far leading edge, followed by the view title; next to the title the toolbar can include a document menu of standard and app-specific whole-document commands (Duplicate, Rename, Move, Export). Leading-edge items aren't customizable, so they're always available.
- **Center area**: common, useful controls, and the view title if it isn't on the leading edge. In macOS and iPadOS people can add, remove, and rearrange items here when you allow toolbar customization; items in this section automatically collapse into the system-managed overflow menu as the window shrinks.
- **Trailing edge**: important items that must remain available, buttons that open nearby inspectors, an optional search field, the More menu (additional items; also supports toolbar customization), and the primary action such as Done when one exists. Trailing-edge items remain visible at all window sizes.
- **Pin items to the leading edge, center, or trailing edge** to get the groupings you want, inserting space between buttons or other items where appropriate.
- **Group items logically by function and frequency of use** (Keynote: presentation-level, playback, object insertion).
- **Group navigation controls and critical actions (Done, Close, Save) in dedicated, familiar, visually distinct sections.**
- **Keep groupings and placement consistent across platforms.**
- **Minimize the number of groups — aim for a maximum of three.**
- **Keep text-labeled actions separate**: a text button beside a symbol button reads as one combined action, and adjacent text buttons run together — insert fixed space between them (UIBarButtonItem.SystemItem.fixedSpace).

**Platform notes**
- iOS: prioritize only the most important items for the main toolbar area — space is very limited, so include the essential actions first and create a More menu for additional items.
- iOS: use a large title to help people stay oriented — by default it transitions to a standard title as people begin scrolling and back to large when they scroll to the top (UINavigationBar.prefersLargeTitles).
- iPadOS: a toolbar and a tab bar can coexist in the same horizontal space at the top of the view — useful when navigating a few main areas while keeping the full window width for content (see Layout, Windows).
- macOS: the toolbar resides in the window frame at the top, either below or integrated with the title bar; window titles can display inline with controls; toolbar items don't include a bezel.
- macOS: make every toolbar item available as a command in the menu bar — people can customize or hide the toolbar, so it can't be the only place a command lives; conversely, not every menu item deserves a toolbar item.
- tvOS: no additional considerations.
- visionOS: the system-provided toolbar appears along the window's bottom edge, above the window-management controls, in a parallel plane slightly in front of the window along the z-axis; a variable blur in the bar background keeps items legible as content scrolls behind them while the window's glass material stays uniform and undivided.
- visionOS: supply either a symbol or a text label for each toolbar item; when people look at a symbol item, visionOS reveals its text label.
- visionOS: prefer the system-provided toolbar — consistent and familiar, optimized for eye and hand input, and automatically placed in the correct position relative to its window.
- visionOS: avoid creating a vertical toolbar — tab bars are vertical in visionOS, so a vertical toolbar could confuse people.
- visionOS: try to prevent windows from resizing below the toolbar's width — visionOS has no menu bar listing all actions, so the toolbar must give reliable access to essential controls at any window size.
- visionOS: if the app can enter a modal state (e.g. a multistep photo-editing task), consider contextually relevant toolbar controls for that state and reinstate the window's standard toolbar controls when it exits.
- visionOS: avoid a pull-down menu in a toolbar — hard to discover, may clutter the interface, and because the toolbar sits at the bottom edge the menu might obscure the standard window controls below it.
- watchOS: toolbar buttons can sit in the top corners or along the bottom; placed above scrolling content they always remain visible as content scrolls under them (ToolbarItemPlacement.topBarLeading, .topBarTrailing, .bottomBar).
- watchOS: a button placed in the scrolling view (a scrolling toolbar button) stays hidden until people reveal it by scrolling up; discovery is automatic because people frequently scroll to the top (ToolbarItemPlacement.primaryAction).
- watchOS: use a scrolling toolbar button for an important action that isn't a primary app function but is closely related to the view's purpose (Mail's New Message button at the top of the Inbox list).

**Specs**
Title length under 15 characters; maximum of about three item groups; one `.prominent` primary action, trailing side.

**Dev refs**
Toolbars (SwiftUI), ScrollEdgeEffectStyle (SwiftUI), ToolbarItemPlacement.topBarLeading / .topBarTrailing / .bottomBar / .primaryAction (SwiftUI), UIToolbar (UIKit), UIBarButtonItem.SystemItem.fixedSpace (UIKit), UINavigationBar.prefersLargeTitles (UIKit), NSToolbar (AppKit)

## Navigation and search

### Path controls
Full page: hig/components/path-controls.md · Platforms: macos
A path control shows the file-system path of a selected file or folder (Finder's View > Show Path Bar shows the selected item's path, or the window's folder when nothing is selected). Two styles, standard and pop up. macOS only.

**Rules**
- **Standard style**: a linear list of the root disk, parent folders, and selected item, each with an icon and a name; when the list is too long to fit, names between the first and last items are hidden; if the control is editable, people can drag an item onto it to select it and show its path.
- **Pop-up style**: resembles a pop-up button showing the selected item's icon and name; clicking opens a menu containing the root disk, parent folders, and selected item; if editable, the menu adds a Choose command for selecting an item, and people can also drag an item onto the control.
- **Use a path control in the window body, not the window frame** — not in toolbars or status bars (Finder's path bar sits at the bottom of the window body, not in the status bar).

**Dev refs**
NSPathControl (AppKit)

### Search fields
Full page: hig/components/search-fields.md · Platforms: ios,ipados,macos,tvos,visionos,watchos · Latest change 2026-06-08: terminology and search-as-a-tab guidance
A search field is an editable text field with a Search icon, a Clear button, and placeholder text, optionally with a scope bar (filters/adjusts search scope) and tokens (selectable, editable representations of search terms that filter further terms). Entry-point patterns differ per platform. Systemwide search guidance is in the Searching pattern page.

**Rules**
- **Use placeholder text to tell people what they can search for** and to reinforce scope.
- **Start searching immediately as a person types, if possible**; continuously refined results feel responsive.
- **Consider showing suggested search terms** — recent searches before search begins, predictive suggestions while typing.
- **Simplify results**: most relevant first to minimize scrolling; consider categorizing them.
- **Consider letting people filter results**, e.g. a scope bar in the results area.
- **Use a scope bar to filter among clearly defined categories**, moving from broader to narrower (Mail: entire mailbox → current mailbox).
- **Default to a broader scope** and let people refine; the full set gives context for narrowing.
- **Use tokens to filter by common terms or items**: a token clarifies a term (a specific contact in Mail) or focuses attributes (photos in Messages). The macOS counterpart is the token field.
- **Pair tokens with search suggestions** so people learn which tokens exist.

**Platform notes**
- iOS — three main places for the search entry point: a tab in the tab bar, a toolbar at the bottom or top of the screen, or directly inline with content; choose by the app's layout, content, and navigation.
- iOS — search as a tab keeps search visible and always available as people switch sections. Two styles: Standard tab (displayed uniformly with the rest of the tab bar; tapping opens a search landing page with the field at the top) and Button appearance (displayed as a separate button; tapping focuses the field and shows the keyboard immediately).
- iOS — choose the standard tab style to provide suggestions, promote discovery, and encourage exploration — the dedicated landing page can surface content or suggestions before people tap the field; great for an app with varied, rich content (Apple TV presents genres and categories).
- iOS — choose the button appearance to help people quickly find what they need — the keyboard and field appear at once; a transient experience that returns people to their previous tab when they exit search; ideal when search should resolve quickly and seamlessly.
- iOS — search in a bottom toolbar: either an expanded field or a toolbar button, depending on available space; tapping animates it into a search field above the keyboard.
- iOS — search in a top toolbar (navigation bar): a toolbar button; tapping animates it into a search field above the keyboard, or at the top if there isn't space at the bottom.
- iOS — place search at the bottom if there's room — add a field to an existing toolbar or create a new toolbar where search is the only item; keeps search easy to reach whenever it's a priority (Settings: the only item; Mail and Notes: alongside other important controls).
- iOS — place search at the top when it's important to defer to content at the bottom of the screen (Wallet keeps event passes stacked at the bottom for glanceable access) or when there's no bottom toolbar.
- iOS — place search as an inline field when its position alongside the content it searches strengthens that relationship — filtering or searching within a single view rather than globally; useful when the app has more than one search field or location is critical to scope (Music: main search is a tab, the library offers an inline field to filter songs and albums).
- iOS — when at the top, position an inline search field above the list it searches, and consider pinning it to the top toolbar while scrolling to keep it distinct from search in other locations.
- iPadOS/macOS: search-field placement and behavior are similar on both — if the app is on both platforms, keep the search experience as consistent as possible.
- iPadOS/macOS: put the search field at the trailing side of the toolbar for most common uses, particularly split-view apps that search across multiple columns (Mail, Notes, Voice Memos) — people navigate results while their selection stays visible in the detail view; also consider the toolbar when results appear in the detail view (Freeform filters the boards shown below).
- iPadOS/macOS: include search at the top of the sidebar when it filters sidebar content or navigation (Settings filters the sidebar to expose sections several levels deep for search, preview, and navigation) — useful with a rich detail view when you need a distinct separation between the sidebar being filtered and the adjacent view.
- iPadOS/macOS: include search as an item in the sidebar or tab bar when you want a dedicated discovery area — when search pairs with rich suggestions, categories, or content needing more space (Music, TV: a unified place for suggested content, categories, and recent searches); a dedicated area also keeps search available while people switch sections.
- iPadOS/macOS: in a search field in a dedicated area, consider immediately focusing the field when people navigate there so they search faster and find the field easily — except on iPad when only a virtual keyboard is available, where leaving the field unfocused prevents the keyboard from unexpectedly covering the view.
- iPadOS/macOS: account for window resizing — on iPad the search field resizes fluidly with the window as on Mac; for compact views on iPad make sure search sits where it's most contextually useful (Notes and Mail place it above the content-list column when resized to compact).
- tvOS: a search screen is a specialized keyboard screen with results beneath in a fully customizable view (UISearchController); provide popular, context-specific, and recent suggestions because people don't want to type much (Using suggested searches with a search controller).
- watchOS: tapping the search field opens a full-screen text-input control; the app returns to the field only after Cancel or Search.
- visionOS: no additional considerations.

**Dev refs**
searchable(text:placement:prompt:) (SwiftUI), Adding a search interface to your app (SwiftUI), Scoping a search operation (SwiftUI), UISearchBar (UIKit), UISearchTextField (UIKit), UISearchController (UIKit), NSSearchField (AppKit)

### Sidebars
Full page: hig/components/sidebars.md · Platforms: ios,ipados,macos,tvos,visionos · Latest change 2026-06-08: sidebar icon colors; adaptable sidebar style
A sidebar on the leading side navigates between app areas or top-level collections (folders, playlists). It needs a lot of vertical and horizontal space; when space is limited or content should dominate, a tab bar (or the tab bar style that converts to a sidebar) is better. Not supported in watchOS.

**Rules**
- **Extend visually rich content beneath the sidebar.** In iOS, iPadOS, and macOS sidebars — like toolbars and tab bars — float above content in the Liquid Glass layer; reinforce the separation by letting content scroll horizontally beneath it or applying a background extension effect that mirrors adjacent content to appear stretched under the sidebar (backgroundExtensionEffect()).
- **Let people customize the sidebar's contents when possible** — which areas appear and in what order.
- **Group hierarchy with disclosure controls when there's a lot of content** to keep vertical space manageable.
- **Use familiar SF Symbols for items**; for a custom icon prefer a custom symbol over a bitmap.
- **Consider letting people hide the sidebar** using platform interactions they know: iPadOS edge swipe; macOS show/hide button or Show Sidebar/Hide Sidebar in the View menu; in visionOS the window usually expands to fit the sidebar so hiding is rare. Never hide it by default — it must stay discoverable.
- **Show no more than two levels of hierarchy in a sidebar**; for deeper data use a split view with a content list between sidebar and detail.
- **With two levels, title each group with a succinct, descriptive label**; omit unnecessary words.
- **Make sidebar icon colors serve a clear purpose.** Icons default to the app accent color; in macOS people can change the system accent color and expect all sidebar icons to follow it, so honor it. Sparingly used fixed colors can clarify meaning or draw attention (Mail's VIP icon is yellow).

**Platform notes**
- iOS/iPadOS: the sidebarAdaptable tab view style lets you choose whether the app opens showing a sidebar or a tab bar; both variations include a button to switch between them; the style adapts its appearance per platform and responds automatically to rotation and window resizing with a version appropriate to the view's width.
- iOS/iPadOS: to display a sidebar only, use NavigationSplitView with the sidebar in the primary pane of a split view, or UISplitViewController.
- iOS/iPadOS: consider using a tab bar first — it provides more space to feature content and enough flexibility for most apps' main areas; if you need to expose more areas than fit, the tab bar's convertible sidebar-style appearance can give access to content people use less often (see Tab bars).
- iOS/iPadOS: if you're not using SwiftUI, apply UICollectionLayoutListConfiguration.Appearance.sidebar to a collection view list layout to get the correct sidebar appearance.
- macOS: a sidebar's row height, text, and glyph size depend on its overall size — small, medium, or large — which you can set programmatically and people can change via the sidebar icon size in General settings.
- macOS: consider automatically hiding and revealing the sidebar when its window resizes (reducing a Mail viewer window collapses the sidebar to make room for message content).
- macOS: avoid putting critical information or actions at the bottom of a sidebar — people often position windows so the bottom edge is hidden.
- tvOS: no additional considerations.
- visionOS: if the app's hierarchy is deep, consider a sidebar within a tab in a tab bar to support secondary navigation inside the tab; prevent selections in the sidebar from changing which tab is open.

**Dev refs**
sidebarAdaptable (SwiftUI TabViewStyle), NavigationSplitView (SwiftUI), ListStyle.sidebar (SwiftUI), backgroundExtensionEffect() (SwiftUI), UICollectionLayoutListConfiguration / .Appearance.sidebar (UIKit), UISplitViewController (UIKit), NSSplitViewController (AppKit)

### Tab bars
Full page: hig/components/tab-bars.md · Platforms: ios,ipados,macos,tvos,visionos · Latest change 2026-06-08: terminology and art (Liquid Glass guidance 2025-07-28 / 2025-12-16)
A tab bar lets people switch between an app's top-level sections while preserving each section's navigation state. For actions on the current view use a toolbar instead. Not supported in watchOS.

**Rules**
- **Use a tab bar for navigation, not actions** (Clock: Alarm, Stopwatch, Timer); controls acting on the current view belong in a toolbar.
- **Keep the tab bar visible as people navigate within sections**; hiding it makes people lose their place. Only a modal view may cover it (temporary and self-contained).
- **Use the appropriate number of tabs**: weigh each extra tab against how often people need the section; fewer tabs are easier; for complex structures consider a sidebar or a tab bar that adapts to a sidebar.
- **Avoid overflow tabs.** When horizontal space runs out, the trailing tab becomes a More tab (iOS/iPadOS) listing the rest, making hidden sections hard to reach and notice — limit the scenarios where this happens.
- **Never disable or hide tab bar buttons, even when content is unavailable**; explain why a section is empty instead.
- **Include tab labels** beneath (compact) or beside (regular) the icon; use single words when possible.
- **Consider SF Symbols for tab icons** — they adapt to compact/regular layouts automatically; prefer filled symbols/icons for platform consistency; custom icon dimensions are in Apple Design Resources.
- **Use a badge only for critical information**: a red oval with white text — a number or an exclamation point — signaling new/updated content; don't dilute it.
- **Avoid a similar color on tab labels and the content-layer background**; with bright colorful content prefer a monochromatic tab bar or an accent color with sufficient differentiation (see Liquid Glass color).

**Platform notes**
- iOS: the tab bar floats above content at the bottom of the screen; its items rest on a Liquid Glass background that lets content beneath peek through.
- iOS: for a tab bar with an attached accessory (Music's MiniPlayer), you can choose to minimize the tab bar and move the accessory inline with it when a person scrolls down; tapping a tab or scrolling to the top of the view exits the minimized state (TabBarMinimizeBehavior, UITabBarController.MinimizeBehavior).
- iOS: a tab bar can include a dedicated search tab at the trailing end (see Search fields).
- iPadOS: the system displays the tab bar near the top of the screen, either as a fixed element (tabBarOnly) or with a button that converts it to a sidebar (sidebarAdaptable); to present a sidebar without the option to convert it to a tab bar, use a navigation split view instead of a tab view (see Sidebars).
- iPadOS: prefer a tab bar for navigation — it gives access to the sections people use most; for a more complex app, provide the option to convert the tab bar to a sidebar so people can reach a wider set of navigation options.
- iPadOS: let people customize the tab bar in apps with many sections — select frequently used items to add and remove less used ones (Music lets a person show a favorite playlist in the tab bar); if you allow this, aim for a default list of five or fewer tabs to preserve continuity between compact and regular view sizes (TabViewCustomization, UITab.Placement).
- macOS: no additional considerations.
- tvOS: the tab bar is highly customizable — specify a tint, color, or image for the background; choose a font for tab items, including a different font for the selected item; specify tints for selected and unselected items; add button icons like settings and search.
- tvOS: by default the tab bar is translucent and only the selected tab is opaque; when people use the remote to focus on the tab bar, the selected tab shows a drop shadow emphasizing its selected state. The height of a tab bar is 68 points and its top edge is 46 points from the top of the screen; you can't change either value.
- tvOS: overflow — when items don't fit, the system truncates the rightmost item with a fade effect beginning at the right side; with enough items to cause scrolling, a truncating fade also starts from the left side.
- tvOS: be aware of scrolling behaviors — by default people can scroll the tab bar offscreen when the current tab contains a single main view (TV app: Watch Now, Movies, TV Show, Sports, Kids); when a screen contains a split view (TV app Library, an app's Settings) the tab bar stays pinned at the top while content scrolls within the panes; regardless of content, pressing Menu on the remote always returns focus to the tab bar at the top.
- tvOS: in a live-viewing app, organize tabs consistently in this order — Live content; Cloud DVR or other recorded content; Other content (see Live-viewing apps).
- visionOS: the tab bar is always vertical, floating in a position fixed relative to the window's leading side; it expands automatically when people look at it and can temporarily obscure content behind it while expanded; people look at a tab and tap to open it.
- visionOS: supply a symbol and a text label for each tab — the symbol is always visible, and the system reveals labels when people look at the tab bar; keep labels short enough to read at a glance.
- visionOS: if the app's hierarchy is deep, consider a sidebar within a tab to support secondary navigation; prevent sidebar selections from changing which tab is open.

**Specs**
tvOS tab bar: height 68 pt; top edge 46 pt from the top of the screen (both fixed). iPadOS customizable tab bar: default list of five or fewer tabs.

**Dev refs**
TabView (SwiftUI), TabViewStyle.tabBarOnly / .sidebarAdaptable (SwiftUI), TabBarMinimizeBehavior (SwiftUI), TabViewBottomAccessoryPlacement (SwiftUI), TabViewCustomization (SwiftUI), Enhancing your app's content with tab navigation (SwiftUI), UITabBar (UIKit), UITabBarController.MinimizeBehavior (UIKit), UITab.Placement (UIKit), Elevating your iPad app with a tab bar and sidebar (UIKit), NavigationSplitView (SwiftUI)

### Token fields
Full page: hig/components/token-fields.md · Platforms: macos
A token field is a text field that converts entered text into tokens people can select, reorder by dragging, or move to another field (Mail's address fields). It can show suggestions as people type (selecting one inserts a token), and each token can carry a contextual menu (Mail: edit name, mark VIP, view contact card). Tokens can also represent search terms — see Search fields. macOS only.

**Rules**
- **Add value with a context menu on tokens** — extra options or information about the token.
- **Consider additional ways to convert text into tokens**: by default a comma creates a token; add shortcuts such as Return.
- **Consider customizing the delay before suggested tokens appear**: the default is immediate, which can distract people while typing — tune it to a comfortable level.

**Dev refs**
NSTokenField (AppKit)
