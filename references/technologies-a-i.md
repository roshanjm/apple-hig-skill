# Technologies A–I — HIG digest

This digest covers the first half (AirPlay through iMessage apps and stickers) of the HIG **Technologies** section: Apple frameworks, services and hardware features an app can integrate, each with its own design, branding and trademark rules. Full pages live in `hig/technologies/<slug>.md` (collection page: `hig/technologies.md`, crawled 2026-10-14; the collection page lists 29 technologies — Live Photos through Wallet are in `technologies-j-z.md`). This digest keeps every rule and every number from the source pages but drops examples, illustrations and explanatory prose; where a page's crawl stripped do/don't icons or merged table cells, that is noted inline.

## AirPlay
Full page: hig/technologies/airplay.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS (body text: not supported in watchOS) · Latest change 2023-05-02
Wireless streaming of media from iOS, iPadOS, macOS and tvOS devices to Apple TV, HomePod and AirPlay-compatible TVs and speakers. Integrate when your app plays audio or video that people may want to send to a bigger screen or speaker.

**Rules**
- **Prefer the system-provided media player.** Standard controls, chapter navigation, subtitles, closed captioning and AirPlay streaming for free; build a custom player only if it doesn't meet your needs (AVPlayerViewController).
- **Provide content in the highest possible resolution.** The HLS playlist must include the full range of resolutions; AVFoundation picks per device. Content that is fine at 720p on iPhone looks low quality on a 4K TV.
- **Stream only the content people expect.** Not background loops or short in-app-only video (`usesExternalPlaybackWhileExternalScreenIsActive`).
- **Support both AirPlay streaming and mirroring.**
- **Support remote control events.** Play/pause/fast-forward from the lock screen, Siri and HomePod (Remote command center events).
- **Don't stop playback when the app enters the background or the device locks.** Also avoid automatic mirroring — people must explicitly choose to stream other content.
- **Don't interrupt another app's playback unless your app is starting immersive content.** Launch videos and auto-playing inline video play on the local device only while current playback continues (`ambient` audio session category).
- **Let people use other parts of your app during playback.** Other in-app videos must not start and interrupt the stream when people navigate away from the playback screen.
- **If necessary, provide a custom interface for controlling playback.** Custom buttons must match system appearance and behavior with distinct states for starting, playing and unavailable; use only Apple-provided symbols in controls that initiate AirPlay; place the AirPlay icon in the lower-right corner of a custom player (iOS 16 / iPadOS 16 and later).
- **Choose the icon variant to match neighboring technology icons.** Black icon on white/light backgrounds when other technology icons are black; white icon on black/dark backgrounds when others are white; custom color only when other technology icons share that color. Download from Apple Design Resources.
- **Position the AirPlay icon consistently with other technology icons.** If others sit inside shapes, treat the AirPlay icon the same way.
- **Don't use the AirPlay icon or name in custom buttons or interactive elements.** Noninteractive use only.
- **Pair the icon with the name *AirPlay* correctly.** Name below or beside the icon only if other technologies are referenced the same way; same font as the rest of the layout; never use the icon within text or as a replacement for the name.
- **Emphasize your app over AirPlay.** AirPlay references less prominent than your app name or main identity.
- **Use correct capitalization.** *AirPlay* is one word, uppercase A and P, the rest lowercase; all-uppercase only if the layout uses only uppercase designations.
- **Always use *AirPlay* as a noun.** "Use AirPlay to listen on your speaker" — not "AirPlay to your speaker" or "You can AirPlay with [App Name]".
- **Use terms like *works with*, *use*, *supports*, *compatible*.** "[App Name] is compatible with AirPlay", "AirPlay-enabled speaker", "You can use AirPlay with [App Name]" — not "[App Name] has AirPlay". (Do/don't icons stripped in crawl; labels follow the rule text.)
- **Use the name *Apple* with *AirPlay* if desired.** "Compatible with Apple AirPlay".
- **Refer to AirPlay if appropriate and to add clarity.** When content is AirPlay-specific, or in technical specifications.

**Platform notes**
- iOS/iPadOS/macOS/tvOS/visionOS: no additional considerations · watchOS: not supported.

**Dev refs**
AVFoundation, AVKit, AVPlayerViewController, HTTP Live Streaming, MediaPlayer remote command center events, AVAudioSession.Category.ambient, Apple Design Resources, Apple Trademark List

## Always On
Full page: hig/technologies/always-on.md · Platforms: iOS, watchOS · Latest change 2023-09-12
On iPhone 14 Pro / Pro Max the system keeps showing Lock Screen widgets and Live Activities when the device is set face up and idle; on Apple Watch, wrist-down dims the face but keeps showing the frontmost app or a background session. Notifications still appear; a tap exits Always On. Integrate if your app, widget or Live Activity can give glanceable, low-power information.

**Rules**
- **Hide sensitive information.** Redact bank balances, health data and anything personal that could appear in a notification.
- **Keep other personal information glanceable when it makes sense.** Workout pace and heart rate on Apple Watch, flight arrivals or ride-share arrival on iPhone; people who want nothing shown can turn Always On off.
- **Keep important content legible and dim nonessential content.** Increase dimming on secondary text, images and color fills; drop row backgrounds; replace rich images and large color areas with dimmed colors.
- **Maintain a consistent layout.** No distracting changes when Always On begins or ends; transition interactive components to an unavailable appearance rather than removing them; make infrequent, subtle updates (e.g. update only the score, not play-by-play). Motion is especially noticeable on a face-up iPhone.
- **Gracefully transition motion to a resting state; don't stop it instantly.** Finish the current motion so people don't think something broke.

**Platform notes**
- iOS/watchOS: no additional considerations · iPadOS/macOS/tvOS/visionOS: not supported.

**Dev refs**
Designing your app for the Always On state (watchOS), Widgets, Live Activities, Notifications

## App Clips
Full page: hig/technologies/app-clips.md · Platforms: iOS, iPadOS · Latest change 2025-06-09 (demo App Clips)
A lightweight slice of your app or game for an in-the-moment task or a demo, launched without an App Store download from App Clip Codes, NFC tags, QR codes, Siri Suggestions, Maps, Smart App Banners, Safari App Clip cards, Messages links and (iOS 17+) links or App Clip previews inside other apps. It stays on the device only for a limited time.

**Rules**
- **Allow people to complete a task or a demo in your App Clip.** Never require the full app to finish the demo, task or level.
- **Focus on essential features.** Reserve advanced or complex features for the app; a demo shows the essentials of the full experience.
- **Don't use App Clips solely for marketing.** Provide real value; don't advertise services or products; don't display ads.
- **Avoid using web views.** Use native components; if only web components exist, link to the website instead.
- **Design a linear, easy-to-use, focused interface.** No tab bars, complex navigation or settings; minimum screens and entry forms.
- **On launch, show the most relevant part.** Skip unnecessary steps; land people where their context fits.
- **Ensure people can use the App Clip immediately.** Include all required assets, omit splash screens, never make people wait on launch.
- **Ensure the App Clip is small.** Remove unnecessary code and unused assets; avoid downloading additional data.
- **Make the App Clip shareable.** Links to specific points inside it; recipients launch from Messages.
- **Make it easy to pay.** Support Apple Pay for express checkout and typing-free shipping info.
- **Avoid requiring an account before people benefit.** Skip accounts or ask after the task; if required, minimize fields and offer Sign in with Apple.
- **Provide a familiar, focused experience in the full app.** Installing the app replaces the App Clip and takes over its invocations; don't add steps such as logging in again.
- **Limit the data you store and handle yourself.** Store securely; don't rely on data stored on the device earlier — the system may have removed the App Clip and its data; keep login info securely off-device. App Clips can't run background operations.
- **Consider offering Sign in with Apple** and **offer a secure, privacy-respecting way to pay** (Apple Pay).
- **Don't compromise the experience by asking people to install the full app.** The App Clip card and the system app banner (shown on first launch) may be incentive enough; for a demo, let people finish it before asking.
- **Pick the right time to recommend your app.** On task completion or a natural pause, show an `SKOverlay` to start the download in context.
- **Recommend your app in a nonintrusive, polite way.** Don't ask repeatedly, don't interrupt tasks, don't use push notifications for it; clearly state the app's additional features.
- **Notifications are available for up to 8 hours after launch.** Only ask for permission for an extended period if functionality spans more than a day (e.g. car-return reminder).
- **Keep notifications focused.** No purely promotional notifications; send only in response to an explicit user action; often none are needed.
- **Use notifications to help people complete the task** (e.g. delivery updates).
- **Platform providers: use consistent branding.** The individual business's brand is front and center; tone down your own.
- **Platform providers: consider multiple businesses or locations.** Update the UI per business/location, offer switching between recent ones, verify the person's location on launch.
- **App Clip card — be informative.** The image must communicate features, supported tasks or content.
- **App Clip card — prefer photography and graphics.** Not UI screenshots; show the value or the business/location.
- **App Clip card — avoid text in the header image.** Not localizable, hard to read.
- **App Clip card — adhere to image requirements.** 1800x1200 px PNG or JPEG, no transparency.
- **App Clip card — use concise copy.** Title ≤ 30 characters, subtitle ≤ 56 characters; both required.
- **App Clip card — pick the action verb.** *View* for media and informational/educational content, *Play* for games, *Open* for everything else.
- **App Clip Codes always use Apple's designs.** Badge with the App Clip logo, or the logo-less design when space is at a premium; default color pair or custom foreground/background.
- **Two variants:** *scan-only* (camera icon at center; Camera app or Control Center Code Scanner) and *NFC-integrated* (iPhone icon at center; hold the device near it or use the Control Center NFC Tag Reader; also scannable).
- **Use NFC-integrated where people can physically reach the code** (tabletop, register, storefront window, signage, gift card/coupon); **scan-only where it's inaccessible or digital** (posters, behind a counter, digital displays, email, social images).
- **Include the App Clip logo when space allows.** Use the logo-less design when clear-space requirements can't be met, on disposable paper or plastic items, and on items associated with gambling or drinking (playing cards, poker chips, bar coasters). The logo appears only below the code in the badge design — never on its own.
- **Place codes on flat or cylindrical surfaces only.** On a cylinder, code width ≤ one-sixth of the circumference.
- **Keep the code flat.** Avoid deformable materials (paper, plastic, fabric); mount on a rigid card; stickers must adhere to flat surfaces.
- **Place codes for reliable scanning.** Adequate light for scan-only codes; no wide scanning angles.
- **Keep the code unobstructed.** No overlaid text, logos or images; never animate or dim it.
- **Display the code upright.** Don't rotate the code or angle the center glyph.
- **Don't create codes that are too small.** See Specs; keep distance-to-code-size ratio ≤ 20:1, ideally 10:1 (scanned from 40 in / 101 cm → diameter ≥ 4 in / 10.16 cm); next to a QR code or other scannable item, make the App Clip Code at least that item's size.
- **Provide enough clear space.** Minimum clear space = the gap between the center glyph and the circular code; more between adjacent machine-readable codes.
- **Add clear call-to-action messaging, especially with the logo-less design.** Scan-only: "Scan to [action]" / "Scan using the camera on your iPhone or iPad to [action]". NFC: "Scan to [action]" / "Hold your iPhone near the [object] to launch an App Clip that [action]".
- **Adhere to Apple trademark guidelines.** No Apple trademarks in app name or images; title case for *App Clips* and *App Clip Code*.
- **Always use the generated App Clip Code** (App Store Connect or the App Clip Code Generator CLI). Don't redesign or modify it, apply filters, augment colors, or add glows, shadows, gradients or reflections; scale uniformly including stroke widths; keep the aspect ratio.
- **Choose colors with enough contrast.** Each code uses a foreground, a background and a generated third color; the tools refuse suboptimal custom combinations and can suggest a foreground for your background.
- **Printing — use high-quality, non-textured matte materials.** No shine, gloss, reflective or holographic overlays, thin laminates; matte laminate if lamination is needed; UV-resistant materials/coatings outdoors; flexographic printing for professional runs; inkjet for desktop printing.
- **Printing — use high-resolution images and settings.** Rasterize the SVG at ≥ 600 ppi; print at ≥ 300 dpi; level and calibrate the printer; avoid channel misalignment, bad gamma, artifacts, elliptical distortion; on receipt printers print as close to the paper's maximum bounds as possible.
- **Printing — convert sRGB SVGs to CMYK correctly.** Relative colorimetric (media-relative) intent; "Generic CMYK ICC profile" on CMYK printers or "Gracol 2013 ICC profile" on CMYKOV printers; color tolerance CIELab Delta E of 2.5.
- **Grayscale-only printers: generate grayscale codes.** Color codes printed in grayscale scan less reliably.
- **NFC-integrated codes use Type 5 NFC tags**, ≥ 35 mm in diameter or equivalent.
- **Large batches: test the workflow and verify prints.** Small test runs; templates with padded regions showing the invocation URL and SVG filename beside each code; keep a file mapping SVG → URL; manage versions carefully.
- **Verify printer calibration with Apple's test sheets.** Color-pair text-box sheet printed at the right scale; grayscale sheet with two bars — light or missing grays mean recalibrate or the printer is unsuitable.
- **Legal:** only codes generated in App Store Connect or the generator CLI that follow these guidelines are approved; use them only to indicate App Clip availability; Apple may update the design; stop displaying a code when its App Clip is inactive; never use the code, Apple logo, App Clip mark or designs in a company or product name; never seek copyright or trademark registration for them; never use them in ways that damage Apple's goodwill, infringe third-party rights or confuse source; Apple retains all IP; don't add a symbol to generated codes; don't translate Apple trademarks (English even in non-English text; legal notice/credit-line translations only with Apple's approval).

**Platform notes**
- iOS/iPadOS: no additional considerations · macOS/tvOS/visionOS/watchOS: not supported.

**Specs**

App Clip card: 1800x1200 px PNG/JPEG, no transparency · title ≤ 30 characters · subtitle ≤ 56 characters · action button verb: View / Play / Open.

| Type | Minimum size |
|---|---|
| Printed communications | Minimum diameter of 3/4 inch (1.9 cm). |
| Digital communications | Minimum size of 256×256 px. Use a PNG or SVG file. |
| NFC-integrated App Clip Code | The embedded NFC tag needs to be at least 35 mm in diameter or of equivalent size. For example, if your embedded NFC tag is 35 mm in diameter, your printed App Clip Code needs to be at least 1.37 inches (3.48 cm) in diameter. |

Scanning distance : code size ≤ 20:1 (prefer 10:1) · cylinder: width ≤ 1/6 circumference · raster ≥ 600 ppi, print ≥ 300 dpi · CMYK ΔE 2.5 · NFC Type 5, ≥ 35 mm · notifications ≤ 8 hours after launch.

**Dev refs**
App Clips (AppClip), SKOverlay (StoreKit), App Store Connect, App Clip Code Generator, printer calibration test sheets, Apple Pay, Sign in with Apple, NFC, Guidelines for Using Apple Trademarks

## Apple In-App Purchase
Full page: hig/technologies/apple-in-app-purchase.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS · Latest change 2026-09-17 (rebranded as Apple In-App Purchase)
Sells digital goods and services inside your app: consumable, non-consumable, auto-renewable subscriptions and non-renewing subscriptions; items can also be promoted on the App Store. Use Apple Pay instead for physical goods, services and donations. Very large or multi-creator catalogs can use the Advanced Commerce API.

**Rules**
- **Let people experience your app before making a purchase.** Consider limited free access for subscriptions.
- **Design an integrated shopping experience.** Present products and transactions in your app's own style.
- **Use simple, succinct product names and descriptions.** No truncation or wrapping; plain language.
- **Display the total billing price for each in-app purchase, regardless of type.**
- **Display your store only when people can make payments.** Otherwise hide it or explain why it's unavailable (e.g. parental restrictions; `canMakePayments`).
- **Use the default confirmation sheet.** Don't modify or replicate it.
- **Family Sharing — mention it prominently where people learn about content.** "Family" or "Shareable" in names; reference it on the sign-up screen. Sharing extends to up to five additional family members.
- **Family Sharing — help people understand the benefits and how to participate.** Apple can notify existing subscribers (sharing is off by default) and family members.
- **Family Sharing — customize in-app messaging for purchasers and family members.** e.g. "Your family subscription includes…".
- **Provide help people can view before requesting a refund.** Custom purchase-help screen: missing purchases, FAQs, feedback/contact, plus a link into the system refund flow (`beginRefundRequest`).
- **Use a simple refund action title** like "Refund" or "Request a Refund"; the system flow already explains it's from Apple.
- **Help people find the problematic purchase.** Product image, name, description, original purchase date.
- **Consider offering alternative solutions** (immediate fulfillment, conciliatory item) while making clear a refund is still available.
- **Make it easy to request a refund.** Don't hide the button behind scrolling or another screen.
- **Avoid characterizing Apple's refund policies.** Don't speculate on outcomes; link to Apple's "Request a refund" support article.
- **Call attention to subscription benefits during onboarding.** Strong call to action and clear summary of terms.
- **Offer a range of content choices, service levels and durations.**
- **Consider letting people try content for free first.** Freemium, metered paywall or free trial.
- **Prompt people to subscribe at relevant times**, e.g. near their monthly free limit, with prompts throughout the app.
- **Encourage a new subscription only when someone isn't already a subscriber.** Provide sign-in when the same subscription is sold in multiple apps or on the web.
- **Provide clear, distinguishable subscription options.** Short self-explanatory names; price and duration for each; for an introductory price list the intro price, offer duration and the standard price afterward.
- **Simplify initial signup by asking only for necessary information.** Defer the rest until after signup.
- **tvOS: help people sign up or authenticate using another device** by sending a code.
- **The in-app sign-up screen must include:** subscription name, duration and the content/services per period; the billing amount localized for each territory and currency; a way for existing subscribers to sign in or restore purchases — plus Terms of Service and Privacy Policy links in the app and App Store metadata.
- **Clearly describe how a free trial works.** State the trial length and that payment starts automatically for the next period, with the amount.
- **Include a sign-up opportunity in your app's settings.**
- **Offer codes (iOS/iPadOS):** *one-time use codes* are generated in App Store Connect and redeemable via redemption URL, in-app or in the App Store — for small or restricted distribution; *custom codes* (e.g. NEWYEAR) are redeemable via URL or in-app only — for mass campaigns.
- **Clearly explain offer details** in marketing materials.
- **Custom codes contain only alphanumeric ASCII characters.** No special characters, including Chinese and Arabic characters.
- **Tell people how to redeem a custom code** — it can't be entered in App Store account settings.
- **Consider supporting offer redemption in-app.** The system supplies the redemption screens; you only build the entry point (e.g. "Redeem Code" on the paywall, onboarding or settings; `presentOfferCodeRedeemSheet`, `offerCodeRedemption`).
- **Supply a promotional image** for the redemption screens; otherwise the app icon is used.
- **Let people benefit from unlocked content immediately after redemption.** Welcome new subscribers, tour new features, and handle people who subscribed before first opening the app (smooth account creation/sign-in).
- **Provide summaries of the customer's subscriptions**, especially the upcoming renewal date, in settings/account near the management option (`Product.SubscriptionInfo`).
- **Consider the system-provided subscription-management UI** (`showManageSubscriptions`).
- **Encourage subscribers to keep their subscription or resubscribe later.** On cancel attempts remind them what they lose, suggest another plan or a discount; afterward consider personalized win-back offers (Retention Messaging API).
- **Always make it easy to cancel an auto-renewable subscription.** Deep or unrecognizable management actions feel like obstruction.

**Platform notes**
- iOS/iPadOS/macOS/tvOS/visionOS: no additional considerations · watchOS: the sign-up screen must show the same required information as other versions; clearly describe how the watchOS version differs (subset of content/features) without implying parity; consider a modal sheet for the required info (default Close button returns people to free content — a custom view needs its own Close/Cancel); make options easy to compare on a small screen: one button per option locked up with its description, or a list of options followed by a button whose title updates to the chosen option.

**Dev refs**
StoreKit In-App Purchase, AppStore.canMakePayments, Transaction.beginRefundRequest(for:in:), AppStore.presentOfferCodeRedeemSheet(from:options:), View.offerCodeRedemption(options:isPresented:onCompletion:), Product.SubscriptionInfo, AppStore.showManageSubscriptions(in:), Retention Messaging API, Advanced Commerce API, App Review Guidelines

## Apple Pay
Full page: hig/technologies/apple-pay.md · Platforms: iOS, iPadOS, macOS, visionOS, watchOS · Latest change 2026-06-08
Payment for physical goods, services, donations and subscriptions in apps and any browser via a system payment sheet (card, amount with tax and fees, shipping, contact details) authorized with Face ID, Touch ID, Optic ID, double-click on Apple Watch, or on the web via a nearby iPhone/Apple Watch or a scanned code. Use Apple In-App Purchase for digital goods.

**Rules**
- **Offer Apple Pay on all devices and browsers that support it.** Don't present it where unsupported (`PKPaymentAuthorizationController`; `applePayCapabilities` on web).
- **Make Apple Pay the primary payment option when credentials are available.** If you use the APIs to detect an active card in Wallet you must make Apple Pay the primary (not necessarily sole) option everywhere you use them; don't move it to a separate step or flow; e.g. pre-select it.
- **Use Apple Pay buttons only to initiate payment or, when appropriate, Apple Pay setup.** Nothing else.
- **A custom payment button must not display "Apple Pay" or the Apple Pay logo.** You must then show the Apple Pay mark or reference Apple Pay in text on the same page.
- **Use the Apple Pay mark only to communicate that you accept Apple Pay.** It doesn't pay; never use or position it as a button. With the mark as the selected method, a separate custom button in your style may start payment.
- **Don't hide an Apple Pay button or make it appear unavailable.** If it can't be used yet (size/color not chosen), explain after the tap or click.
- **Inform search engines that Apple Pay is accepted** in semantic product markup.
- **All websites offering Apple Pay must include a privacy statement** and follow the Acceptable use guidelines for Apple Pay on the web.
- **Provide a cohesive checkout experience.** Your branding throughout; avoid opening different pages or windows (especially on the web).
- **If Apple Pay is available, assume people want to use it.** First option, larger, or separated by a line.
- **Accelerate single-item purchases with Apple Pay buttons on product detail pages.** Such purchases cover that one item only, excluding the cart; remove the item from the cart after purchase.
- **Accelerate multi-item purchases with express checkout.** Immediate payment sheet with a single shipping method and destination.
- **Support coupons and promotional codes in the payment sheet**, especially in express checkout.
- **Collect necessary information (color, size) before people reach the button.** If missing, highlight/warn and auto-navigate to the field.
- **Collect optional information (gift messages, delivery instructions) before checkout or after purchase** — the sheet has no field for it.
- **Gather multiple shipping methods and destinations before showing the sheet.** The sheet allows one method and one destination per order.
- **For in-store pickup, choose the location before the sheet** and show its address on the sheet (read-only pickup address).
- **Prefer checkout information from Apple Pay.** Fetch the latest during checkout even if you have stored data.
- **Avoid requiring account creation before purchase.** Ask on the confirmation page; prepopulate from checkout data.
- **Report transaction results in the payment sheet**, with error messages for failures such as a bad address.
- **Display an order confirmation or thank-you page** with ship timing and status. Listing Apple Pay is optional; if shown, put it after the last four digits or as a note: "1234 (Apple Pay)" or "Paid with Apple Pay."
- **Only present and request essential information on the sheet.** E.g. no shipping address for an electronically delivered gift card.
- **Display the active coupon/promo code, or let people enter one.**
- **Let people choose the shipping method in the sheet.** Description, cost and optionally an estimated delivery/pickup date or range, using calendar and time-zone support (`PKDateComponentsRange`).
- **For pickup, consider letting people choose a pickup window** via the shipping method's date/time ranges.
- **Use line items for additional charges, discounts, pending costs, add-on donations, recurring and future payments.** A line item is a label and cost (recurring items may include frequency); never an itemized product list (`paymentSummaryItems`).
- **Keep line items short** — specific, glanceable, one line.
- **Provide a business name after the word *Pay* on the total line**, matching the bank/credit-card statement: "Pay [Business_Name]".
- **If you're not the end merchant, identify both businesses:** "Pay [End_Merchant_Business_Name (via Your_Business_Name)]".
- **Clearly disclose possible costs after authorization.** Where regulations allow, explain on the sheet and show a subtotal marked Amount Pending; a preauthorized amount must be reflected accurately.
- **Handle data entry and payment errors gracefully.**
- **Defer to the payment sheet for progress information.** No extra spinners or progress indicators.
- **Provide a website icon** for payment authorization (Handoff) and Wallet subscription flows — see Specs.
- **Data validation: validate at sheet appearance, on field changes and after authentication.** System messages highlight fields; supply custom messages for the field detail view. Before authorization only the card type and a redacted shipping address are accessible — validate what's available early, and always surface errors on failed authorization.
- **Avoid forcing compliance with your business logic.** Ignore irrelevant data, infer missing data: accept Zip+4 by ignoring extra digits; accept phone numbers with/without dashes or country code.
- **Accurately report problems to the system.** Custom message plus the correct status code (`PKPaymentError`; Apple Pay Status Codes on web).
- **Explain invalid data clearly and succinctly.** Name the field and what's expected ("Zip code doesn't match city", "Shipping not available for this state"); noun phrases, sentence-style capitalization, no ending punctuation; ≤ 128 characters to avoid truncation.
- **Handle interruptions correctly.** On cancellation or timeout the sheet dismisses — you must cancel any in-progress payment; people restart via the button (`oncancel` on web).
- **Subscriptions — clarify details before showing the sheet.** Billing frequency and terms understood up front; frequency can also appear on the sheet. Recurring amounts may be fixed or (where regulations allow) variable; initial authorization can include discounts and fees.
- **Subscriptions — include line items reiterating billing frequency, discounts and upfront fees.** If nothing is due at authorization, disclose when billing starts.
- **Subscriptions — communicate trial terms.** Line items for the trial amount (including $0), the regular amount after the trial, and the date regular billing begins.
- **Subscriptions — clarify the current payment amount in the total line.**
- **Subscriptions — show the sheet only when a change adds fees.** No authorization when cost decreases or stays the same.
- **Billing agreement field = plain-language summary, not formal terms.** Concise, non-duplicative; leave blank when in doubt.
- **Donations (approved nonprofits only) — use a line item to identify the donation**, e.g. "Donation $50.00".
- **Donations — offer predefined amounts** (e.g. $25, $50, $100) plus an Other Amount option.
- **Always use the Apple-provided API to display Apple Pay buttons.** API buttons have approved captions, fonts, colors and styles, scale proportionally, localize automatically, allow corner-radius customization and include VoiceOver alt text. Never design custom Apple Pay buttons or replicate Apple's (`PKPaymentButtonType`/`PKPaymentButtonStyle`, `WKInterfacePaymentButton`, Apple Pay on the Web).
- **Choose the button type that fits your purchase flow** (see Specs). In some contexts the system shows the default card image on the button.
- **Set Up Apple Pay button:** for devices that support Apple Pay but haven't set it up — place in Settings, a profile, or an interstitial page.
- **Button styles:** *automatic* follows system appearance (`PKPaymentButtonStyle.automatic`, `ApplePayButtonStyle`); *Black* on white/light backgrounds with sufficient contrast, never on black/dark; *White with outline* on white/light backgrounds that lack contrast, never on dark or saturated; *White* on dark backgrounds with sufficient contrast.
- **Prominently display the Apple Pay button.** No smaller than other payment buttons; no scrolling to reach it.
- **Position relative to Add to Cart:** side-by-side → Apple Pay to the right; stacked → Apple Pay above.
- **Adjust the corner radius to match other buttons** — square through capsule (`cornerRadius`).
- **Maintain the minimum button size and margins** (see Specs); titles vary by locale. If the size can't fit the translated title, the system substitutes the plain Apple Pay button; there is no substitute for Set Up Apple Pay.
- **Apple Pay mark — use only Apple's artwork, altering nothing but height.** Height ≥ other payment brand marks in the flow; don't change width, corner radius or aspect ratio; no trademark symbol or added content; don't remove the border; no shadows, glows, reflections; don't flip, rotate or animate.
- **Apple Pay mark — clear space ≥ 1/10 of its height**; don't share its border with another graphic or button. Download from the Apple Pay Marketing Guidelines page.
- **Use *Apple Pay* exactly as in the Apple Trademark List** — never plural or possessive; follow the Guidelines for Using Apple Trademarks.
- **Capitalize *Apple Pay* as two words**, uppercase A and P, all other letters lowercase; all-uppercase only to conform to an established all-caps typographic style.
- **Never use the Apple logo for the word *Apple* in text.** In the US use ® on the first body-text mention; no ® when Apple Pay is a checkout selection option. Do: "Purchase with Apple Pay", "Purchase with Apple Pay®". Don't: "Purchase with ApplePay", "Purchase with [Apple logo] Pay", "Purchase with APPLE PAY" (outside an all-caps style).
- **Coordinate font face and size with your app or site.** Don't mimic Apple typography.
- **Don't translate *Apple Pay* or any Apple trademark.** English even inside non-English text.
- **In a payment selection list, text-only "Apple Pay" is allowed only when every option is text-only.** If any option shows an icon or logo, use the Apple Pay mark.
- **When promoting Apple Pay in an app, follow the App Store marketing guidelines.**

**Platform notes**
- iOS/iPadOS/macOS/visionOS/watchOS: no additional considerations · tvOS: not supported.

**Specs**

Website icon (Handoff authorization, Wallet subscription flows):

| @2x | @3x |
|---|---|
| 60x60 pt (120x120 px @2x) | 60x60 pt (180x180 px @3x) |

Payment button types (button images were stripped in the crawl; the label column is inferred from each row's text):

| Button (inferred) | Example usage |
|---|---|
| Buy with Apple Pay | An area in an app or website where people can make a purchase, such as a product detail page or shopping cart page. |
| Pay with Apple Pay | An app or website that lets people pay bills or invoices, such as those for a utility — like cable or electricity — or a service like plumbing or car repair. |
| Check Out with Apple Pay | An app or website offering a shopping cart or purchase experience that includes other payment buttons that start with the text *Check Out*. |
| Continue with Apple Pay | An app or website offering a shopping cart or purchase experience that includes other payment buttons that start with the text *Continue*. |
| Book with Apple Pay | An app or website that helps people book flights, trips, or other experiences. |
| Donate with Apple Pay | An app or website for an approved nonprofit that lets people make donations. |
| Subscribe with Apple Pay | An app or website that lets people purchase a subscription, such as a gym membership or a meal-kit delivery service. |
| Reload with Apple Pay | An app or website that uses the term *Reload* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| Add Money with Apple Pay | An app or website that uses the term *Add Money* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| Top Up with Apple Pay | An app or website that uses the term *Top Up* to help people add money to a card, account, or payment system associated with a service, such as transit or a prepaid phone plan. |
| Order with Apple Pay | An app or website that lets people place orders for items like meals or flowers. |
| Rent with Apple Pay | An app or website that lets people rent items like cars or scooters. |
| Support with Apple Pay | An app or website that uses the term *Support* to help people give money to projects, causes, organizations, and other entities. |
| Contribute with Apple Pay | An app or website that uses the term *Contribute* to help people give money to projects, causes, organizations, and other entities. |
| Tip with Apple Pay | An app or website that lets people tip for goods or services. |
| Apple Pay (plain) | An app or website that has stylistic reasons to use a button that can have a smaller minimum width or that doesn't specify a call to action. If you choose a payment button type that isn't supported on the version of the operating system your app or website is running in, the system may replace it with this button. |

Button size (reproduced verbatim; the empty cells are row-spanned in the source — Buy, Check Out, Donate, Set Up and Subscribe share the Book row's 140pt / 30pt / 1/10 values):

| Button | Minimum width | Minimum height | Minimum margins |
|---|---|---|---|
| Apple Pay | 100pt (100px @1x, 200px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button's height |
| Book with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button's height |
| Buy with Apple Pay |  |  |  |
| Check Out with Apple Pay |  |  |  |
| Donate with Apple Pay |  |  |  |
| Set Up Apple Pay |  |  |  |
| Subscribe with Apple Pay |  |  |  |

Apple Pay mark clear space: 1/10 of its height · error message length: ≤ 128 characters.

**Dev refs**
PassKit Apple Pay, Apple Pay on the Web, PKPaymentAuthorizationController, PKPaymentAuthorizationViewControllerDelegate, PKPaymentRequest.paymentSummaryItems, PKDateComponentsRange, PKPaymentError, Apple Pay Status Codes, ApplePaySession.applePayCapabilities / oncancel, PKPaymentButtonType, PKPaymentButtonStyle, PKPaymentButton.cornerRadius, ApplePayButtonStyle, WKInterfacePaymentButton (WatchKit), Apple Pay Marketing Guidelines, Apple Pay on the web interactive demo

## Augmented reality
Full page: hig/technologies/augmented-reality.md · Platforms: iOS, iPadOS, visionOS
ARKit overlays 3D virtual objects on the live camera view so they appear to inhabit the physical world; people reorient the device, interact with gestures and movement, and can share multiuser sessions. The guidance below is for iOS/iPadOS; visionOS uses ARKit for immersive experiences.

**Rules**
- **Offer AR features only on capable devices.** AR-primary apps: restrict availability to ARKit devices. Optional AR features: don't show an error on unsupported devices — simply don't offer the feature.
- **Let people use the entire display.** Minimize controls and information that break immersion.
- **Strive for convincing illusions when placing realistic objects.** Detailed assets with lifelike textures; scale and position on detected surfaces; reflect environmental lighting; simulate camera grain; cast top-down diffuse shadows; update visuals with camera motion; render scenes 60 times per second so objects don't jump or flicker.
- **Consider how reflective surfaces show the environment.** Reflections are approximations — prefer small or coarse reflective surfaces.
- **Use audio and haptics to enhance immersion.** Confirm contact between objects/surfaces; background music.
- **Minimize text in the environment.**
- **Put additional information or controls in screen space** — fixed in the virtual world or (less commonly) on the device screen.
- **Consider indirect (2D screen-space) controls for persistent controls.** Reachable without changing grip; translucent so they don't block the scene.
- **Anticipate a wide variety of real-world environments.** State requirements up front; consider different feature sets for different environments.
- **Be mindful of comfort.** Place objects at distances that reduce device movement; keep game levels short with downtime.
- **If your app encourages movement, introduce motion gradually.**
- **Be mindful of safety.** Don't encourage rapid, sweeping or expansive motions.
- **Use the built-in coaching view** (`ARCoachingOverlayView`) for initialization and relocalization.
- **Hide unnecessary app UI while people use a coaching view.**
- **If necessary, offer a custom coaching experience**, using the system view as reference.
- **Show people when to locate a surface and place an object.** System coaching for horizontal/vertical planes; then a custom indicator aligned with the detected plane when placement is possible.
- **Integrate placed objects immediately.** Don't wait for refined surface data; subtly refine later, e.g. nudge an object back onto the surface (`ARTrackedRaycast`).
- **Consider guiding people toward offscreen objects** with visual or audible cues (e.g. an edge indicator).
- **Avoid precisely aligning objects with detected surface edges.** Boundaries are approximations that change.
- **Incorporate plane classification into placement.** Furniture only on "floor"; a game board only on "table".
- **Let people use direct manipulation when possible.** Indirect controls work better when people are moving around.
- **Use standard, familiar gestures.** Single-finger drag to move; two-finger rotation to spin.
- **Keep interactions simple.** Limit movement to the 2D surface the object rests on; limit rotation to a single axis.
- **Respond to gestures within reasonable proximity of interactive objects.** Assume the nearby object is the target for small, thin or distant objects.
- **Let people scale objects only when it makes sense.** Fine for imaginary environments; not for real-world visualization (furniture). Never use scaling to adjust distance.
- **Be wary of conflicting gestures** (two-finger pinch vs two-finger rotation); test.
- **Keep object movement consistent with the environment's physics.** Objects stay attached to surfaces and remain visible — no jumping, vanishing or reappearing during resize, rotate or move.
- **Explore other interaction methods** — motion and proximity (a character turns to look at an approaching person).
- **Consider people occlusion** so virtual objects can appear behind people in the camera feed.
- **Let new participants join a multiuser experience** via implicit map merging (`isCollaborationEnabled`) unless everyone must join first.
- **When a detected image disappears, delay removing attached virtual objects** — wait up to one second before fading or removing them.
- **Limit reference images in use at one time to 100 or fewer.** Swap active sets by context (e.g. museum area via location).
- **Limit reference images requiring an accurate position.** Use a tracked image only when the image may move or the attached content is small relative to the image.
- **Use approachable terminology in instructional text.** Avoid ARKit, world detection, tracking, plane, anchor, "Insufficient features", "Excessive motion detected". Do: "Unable to find a surface. Try moving to the side or repositioning your phone." / "Tap a location to place the [object]." / "Try turning on more lights and moving around." / "Try moving your phone more slowly."
- **In a three-dimensional context, prefer 3D hints** (e.g. a 3D rotation indicator); show 2D text overlays only when people don't respond.
- **Make important text readable.** Critical labels, annotations and instructions in screen space; text in 3D space faces people and keeps the same type size regardless of distance.
- **If necessary, provide a visual indicator that people can tap for more information.**
- **Consider the system coaching view to help people relocalize** after an interruption.
- **Consider hiding previously placed objects during relocalization** to avoid flicker.
- **Minimize interruptions if your app has both AR and non-AR experiences** — embed non-AR tasks inside AR (e.g. change upholstery without leaving AR).
- **Allow people to cancel relocalization.** It can continue indefinitely; offer a reset or restart.
- **Indicate when the front-facing camera can't track a face for more than about half a second.** Visual indicator; minimal text.
- **Let people reset the experience** rather than wait or struggle with placement.
- **Suggest fixes when problems occur** in friendly language: insufficient features → turn on more lights and move around; excessive motion → move the phone slower; slow surface detection → move around, add light, point at a textured surface.
- **Use the AR glyph as intended.** Only to initiate ARKit-based experiences; alter only size and color; never for other purposes or non-ARKit AR.
- **Maintain minimum clear space around the AR glyph of 10% of its height.**
- **Use the AR badges as intended and don't alter them.** Collapsed/expanded badge and glyph-only badge identify objects viewable in AR via ARKit only; never change color or use for non-ARKit AR.
- **Prefer the AR badge to the glyph-only badge**; glyph-only for constrained spaces. Both work at default size.
- **Use badging only when the app mixes AR-viewable and non-AR objects.**
- **Keep badge placement consistent and clear.** Same corner of each object photo, large enough to see without occluding detail.
- **Maintain minimum clear space around the AR badge of 10% of its height.**

**Platform notes**
- iOS/iPadOS: no additional considerations · macOS/tvOS/watchOS: not supported · visionOS: with permission, use ARKit to detect surfaces, use hand and finger positions for custom gestures, and bring nearby physical objects into immersive experiences.

**Specs**

| Problem | Possible suggestion |
|---|---|
| Insufficient features detected. | Try turning on more lights and moving around. |
| Excessive motion detected. | Try moving your phone slower. |
| Surface detection takes too long. | Try moving around, turning on more lights, and making sure your phone is pointed at a sufficiently textured surface. |

Frame rate 60/s · reference images ≤ 100 active · image-loss delay up to 1 second · face-tracking loss indicator after ~0.5 s · glyph and badge clear space 10% of height.

**Dev refs**
ARKit, ARCoachingOverlayView, ARTrackedRaycast, ARWorldTrackingConfiguration.isCollaborationEnabled, Verifying Device Support and User Permission, Occluding virtual content with people, Detecting Images in an AR Experience, Managing Session Life Cycle and Tracking Quality, Apple Design Resources (AR glyph and badges)

## CareKit
Full page: hig/technologies/carekit.md · Platforms: iOS, iPadOS · Latest change 2023-05-02
Open-source framework (CareKit UI prebuilt views + CareKit Store on-device database with sync) for apps that manage care plans — chronic illness, recovery from injury or surgery, wellness goals — with HealthKit, Core Motion, Photos and ResearchKit integration.

**Rules**
- **Provide a coherent privacy policy.** A privacy-policy URL is required at submission and shown on the App Store page.
- **Get permission before accessing data through iOS features, and protect all data** whether entered by people or read from the device.
- **Request access to health data only when you need it.** In context (e.g. when logging weight), not at launch; request each time since permissions can change (`requestAuthorization`).
- **Clarify intent with descriptive messages on the standard permission screen.** A few succinct sentences on why and how people benefit; no custom screens that replicate it.
- **Manage health data sharing solely through Settings > Privacy.** No in-app screens that alter the flow of health data.
- **Motion data (with permission):** stationary/walking/running/cycling/driving, step count, pace, flights climbed; custom physical-therapy data via ResearchKit tasks (Core Motion).
- **Photos (with permission):** camera and library access to share treatment-progress photos with the care team (`UIImagePickerController`).
- **ResearchKit integration:** surveys, tasks, charts and the informed-consent module can be incorporated.
- **Use each view category for its intended purpose** (Tasks, Charts, Contact views — see Specs). A view = header (text, symbol, disclosure indicator, optional bottom separator) + optional vertical content stack; CareKit UI manages layout constraints.
- **Use the simple task style for a one-step task.** Header with title, subtitle and button; optional custom completion image (default: filled button with checkmark); no content stack.
- **Use the instructions style to add informative text to a simple task** ("Take on an empty stomach").
- **Use the log style to help people log events**, with automatic timestamps.
- **Use the checklist style for a list of steps in a multistep task.** Each item has text and a done button; instructional text below the list.
- **Use the grid style for a compact grid of buttons in a multistep task.** Succinct button titles; instructional text below; exposes its collection view for custom UI.
- **Consider color to reinforce the meaning of task items** (medications vs activities) — never color as the only signal.
- **Combine accuracy with simplicity when describing tasks.** Marketing name over chemical description; drop words the context makes redundant (e.g. *take*).
- **Supplement multistep or complex tasks with videos or images.**
- **Charts (bar, scatter, line): highlight narratives and trends** that show progress (e.g. medication adherence vs pain).
- **Label chart elements clearly and succinctly.** Put a unit like *BPM* in an axis label, not on every point.
- **Use distinct colors** — not shades of one color; sufficient contrast.
- **Consider a legend** when colors aren't self-explanatory.
- **Clearly denote units of time** (seconds through years) in labels or on an axis.
- **Consolidate large data sets** by grouping for readability.
- **If necessary, offset data to keep charts proportional** so small points stay readable beside large ones.
- **Contact views (simple, detailed): consider color to categorize care team members.**
- **Minimize notifications.** Use sparingly; coalesce multiple items into one.
- **Consider a notification detail view** so people can act (e.g. mark pending tasks complete) without opening the app.
- **Prefer CareKit's built-in symbols** (phone, messaging, envelope, clock); customize mainly in grid-style views using SF Symbols.
- **Design a relevant care symbol.** Closely tied to your app or health/wellness; never purely decorative or a corporate logo.
- **Incorporate refined, unobtrusive branding.** No advertising; brand through color and communication style.

**Platform notes**
- iOS/iPadOS: no additional considerations · macOS/tvOS/visionOS/watchOS: not supported.

**Specs**

| Category | Purpose |
|---|---|
| Tasks | Present tasks, like taking medication or doing physical therapy. Support logging of patient symptoms and other data. |
| Charts | Display graphical data that can help people understand how their treatment is progressing. |
| Contact views | Display contact information. Support communication through phone, message, and email, and link to a map of the contact's location. |

| Information | Required | Description | Example value |
|---|---|---|---|
| Title | Yes | A word or short phrase that introduces the task. | *Ibuprofen* |
| Schedule | Yes | The schedule on which a task must be completed. | *Four times a day* |
| Instructions | No | Detailed instructions, recommendations, and warnings. | *Take 1 tablet every 4–6 hours (not to exceed 4 tablets daily).* |
| Group ID | No | An identifier you can use to group similar tasks in ways that make sense in your app. | A category identifier like *medication* or *exercise*. |

CareKit 2.0: 5 task styles (simple, instructions, log, checklist, grid) · 3 chart styles (bar, scatter, line) · 2 contact styles (simple, detailed).

**Dev refs**
CareKit (CareKit UI, CareKit Store), HealthKit, HKHealthStore.requestAuthorization(toShare:read:completion:), Protecting user privacy, Core Motion, UIImagePickerController, ResearchKit, SF Symbols

## CarPlay
Full page: hig/technologies/carplay.md · Platforms: iOS · Latest change 2023-05-02
iPhone apps (audio, communication, navigation, and more) rendered on the car's built-in display through system-defined templates — your app supplies content, iOS handles layout, resolution and input hardware (touchscreens, knobs, touch pads). Note: CarPlay audio and video apps also work on Apple HomeView without modification.

**Rules**
- **Eliminate app interactions on iPhone when CarPlay is active.** All interaction via the car's controls and display; any setup happens before the vehicle moves.
- **Never lock people out of CarPlay because the connected iPhone requires input.** Work when the phone is in a bag or trunk; defer problem resolution until the vehicle stops.
- **Make sure your app works without unlocking iPhone.**
- **Let people choose when to start playback.** No auto-play unless the app plays a single audio source or is resuming interrupted audio; don't start an audio session until ready — it silences other sources like the radio.
- **Start playback as soon as audio has sufficiently loaded.** The system keeps the selection highlighted with a spinner until you signal readiness.
- **Display the Now Playing screen when audio is ready.** Don't wait for descriptive metadata; load it in the background.
- **Resume after an interruption only when appropriate.** Resume after temporary interruptions (phone call) if audio was playing; permanent interruptions (a Siri-initiated playlist) are nonresumable.
- **Adjust relative audio levels when necessary, never the overall volume.**
- **Provide useful, high-value information in a clean layout** scannable from the driver's seat; no nonessential detail or embellishment.
- **Maintain a consistent appearance** — similar functions look similar.
- **Make primary content stand out and feel actionable.** Larger = more important and easier to tap; put the most important content and controls in the upper half of the screen.
- **Prefer a limited color palette that coordinates with your logo.**
- **Avoid the same color for interactive and noninteractive elements.**
- **Test the color scheme under varied lighting in an actual car.** Night brightness; sunlight washing out low contrast.
- **Look great in both dark and light appearances.** CarPlay may switch automatically with lighting.
- **Choose inclusive colors.**
- **Supply @2x and @3x images for all CarPlay artwork.** Landscape and portrait displays are supported; the system picks and scales.
- **Mirror your iPhone app icon.**
- **Don't use black for the icon background.** Lighten it or add a border.
- **Report errors in CarPlay, not on iPhone**, and only when absolutely necessary; never direct people to pick up the phone.

**Platform notes**
- iOS only · iPadOS/macOS/tvOS/visionOS/watchOS: not supported.

**Specs**

| Dimensions (pixels) | Aspect ratio |
|---|---|
| 800x480 | 5:3 |
| 960x540 | 16:9 |
| 1280x720 | 16:9 |
| 1920x720 | 8:3 |

CarPlay app icon:

| @2x (pixels) | @3x (pixels) |
|---|---|
| 120x120 | 180x180 |

**Dev refs**
CarPlay App Programming Guide, CarPlay developer portal

## Game Center
Full page: hig/technologies/game-center.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS · Latest change 2025-06-09 (challenges, multiplayer activities, Apple Games app, Game Overlay)
Apple's social gaming network (GameKit): achievements, leaderboards, challenges, multiplayer activities and friend discovery surfaced in-game, in the Apple Games app, the App Store and notifications. Use GameKit's built-in UI or present the data in custom UI.

**Rules**
- **Check at launch whether the player is signed in to Game Center; if not, initialize the player then.** Maximizes discovery (Top Played chart, friend recommendations).
- **Access point destinations:** Game Overlay in iOS/iPadOS/macOS; full-screen in-game dashboard in visionOS/tvOS.
- **Display the access point in menu screens** (main menu, settings) — not during gameplay, splash screens, cinematics or tutorials.
- **Avoid placing controls near the access point.** It sits fixed in any of the four corners and has collapsed and expanded sizes; in visionOS its location varies by game type (immersive, volume).
- **Consider pausing the game while the Game Overlay or dashboard is present.**
- **Custom UI can deep-link into the overlay/dashboard** (leaderboards, profile).
- **Use the Game Center artwork from Apple Design Resources in custom links.** Don't change dimensions or visual effects.
- **Use correct Game Center terminology** (see Specs).
- **Align with the four achievement states:** locked, in-progress, hidden, completed; the system groups Completed vs Locked.
- **Determine achievement display order before uploading** — upload order is display order.
- **Be succinct describing achievements.** Title and description are limited to two lines each and truncate; title-style capitalization for titles, sentence-style for descriptions.
- **Give players a sense of progress** with progressive achievements (system shows progress and encouragement).
- **Design rich, high-quality achievement images.** Never reuse one asset for several achievements; missing assets get a placeholder.
- **Create achievement art in the right size and format.** A circular mask is applied — keep content centered (see Specs).
- **Choose a leaderboard type.** *Classic* tracks all-time best with no end; *recurring* resets on an interval you define (daily/weekly) for rotating puzzles, seasonal events, battle modes.
- **Use leaderboard sets for multiple leaderboards**, grouped by difficulty, activity type, or genre/theme.
- **Add leaderboard images** — a unique image per leaderboard showing the gameplay. iOS/iPadOS/macOS: a single image; tvOS: a layered set that animates on focus (tvOS template in Apple Design Resources).
- **Mind cropping.** iOS/iPadOS/macOS crop artwork for leaderboards inside a set; tvOS focus effects may crop layer edges — keep primary content comfortably inside.
- **Create engaging challenges.** Short (1–5 minutes), skill-based, individually completable, with a clear measure (fastest lap, most enemies in a round, fewest mistakes on a daily puzzle). Challenges are built on leaderboards and are time-limited.
- **Avoid challenges that track overall progress or personal bests.** Track the most recent score per attempt to keep the field level.
- **Make it easy to jump into a challenge.** Entry via invitation links, the Game Overlay or the Games app; always deep-link to the exact mode or level; run required onboarding first and tell first-time players the game will jump into the challenge afterward.
- **Create challenge artwork that invites play.** Shown in the Game Overlay, Games app and invitation previews; keep primary content out of the area the title and description may cover; localize any text in the image via App Store Connect or Xcode (see Specs).
- **Use party codes to invite players to multiplayer activities.** Game Center generates alphanumeric codes, typically eight characters (e.g. "2MP4-9CMF"); let players join late, leave early and return; show the current code in-game; allow manual code entry.
- **Support multiplayer activities through in-game UI.** The overlay/dashboard default interface invites nearby or recent players, friends and contacts; custom UI is also possible. Real-time and turn-based are supported.
- **Provide engaging activity artwork** (see Specs) — shown in party codes, the Games app and in-game UI.

**Platform notes**
- iOS/iPadOS/macOS/visionOS: no additional considerations · tvOS: optionally show an image at the top of the dashboard — simple, recognizable at a distance, your logo or word mark, never the app icon (spec below) · watchOS: GameKit API is available but there is no system Game Center UI on watchOS; Game Center content for watch games appears on the connected iPhone.

**Specs**

Terminology:

| Term | Incorrect terms | Localization |
|---|---|---|
| Game Center | GameKit, GameCenter, game center | Use the system-provided translation of *Game Center* |
| Game Center Profile | Profile, Account, Player Info | Use the system-provided translation of *Game Center* and localize *Profile* |
| Achievements | Awards, Trophies, Medals |  |
| Leaderboards | Rankings, Scores, Leaders |  |
| Challenges | Competitions |  |
| Add Friends | Add, Add Profiles, Include Friends |  |

Achievement image — iOS, iPadOS, macOS, visionOS:

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Mask diameter | 512 pt (1024 px @2x) |

Achievement image — tvOS:

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 320x320 pt (640x640 px @2x) |
| Mask diameter | 200 pt (400 px @2x) |

Leaderboard image — iOS, iPadOS, macOS:

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Cropped area | 512x312 pt (1024x624 px @2x) |

Leaderboard image — tvOS:

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 659x371 pt (1318x742 px @2x) |
| Focused size | 618x348 pt (1236x696 px @2x) |
| Unfocused size | 548x309 pt (1096x618 px @2x) |

Challenge artwork:

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |

Multiplayer activity artwork:

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |

tvOS dashboard image:

| Attribute | Value |
|---|---|
| Image size | 600x180 pt (1200x360 px @2x) |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |

Achievement title/description: 2 lines each · challenge length: 1–5 minutes · party codes: typically 8 alphanumeric characters.

**Dev refs**
GameKit, Adding an access point to your game, Rewarding players with achievements, Encourage progress and competition with leaderboards, Creating engaging challenges from leaderboards, Creating activities for your game, Finding multiple players for a game, Game Porting Toolkit, Apple Design Resources (Game Center artwork, tvOS template)

## Generative AI
Full page: hig/technologies/generative-ai.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS · Latest change 2026-06-08 (refining results, feedback during generation, model-type choice)
Machine-learning models that create or transform text, images and other content — on-device (Foundation Models framework, requires Apple Intelligence) or server-based. Integrate for creative expression, communication or task completion where it adds clear value.

**Rules**
- **Design your experience responsibly.** Outputs vary even for identical inputs and requests are unpredictable; design for inclusion, care and privacy.
- **Keep people in control.** Honor in-scope requests; handle sensitive content carefully; let people dismiss, revert or retry; clearly identify when and where AI is used.
- **Ensure an inclusive experience for all.** Ask for needed attributes rather than inferring personal or cultural characteristics; seek clarity before assumptions about gender identities or relationship types; test across diverse people.
- **Design engaging and useful generative features** only where they add specific value (time savings, communication, creativity).
- **Ensure a great experience when generative features are unavailable or declined.** Offer a non-AI fallback where possible (regular emoji beside Genmoji; unsummarized notifications).
- **Communicate where your app uses AI.** Never let people think they're interacting with a human when it's AI; follow regional disclosure regulations.
- **Set clear expectations about capabilities and limits.** Brief tutorial on introduction; curated suggestions for open-ended prompts; state known limitations, how to get good results and why poor results happen.
- **Choose a model type that fits the feature and protects privacy.** On-device: private, fast, offline; server-based when more power or context is needed — process locally as much as possible, minimize what's sent, tell people data goes to a server, what is shared, and what may be stored or used for training.
- **Ask permission before using personal information and usage data.** Use the minimum; offer a clear opt-out; explicit permission for model improvement or storage; vet third parties' privacy; outputs can leak sensitive data; stricter rules for kids' apps.
- **Clearly disclose how the app and model use and store personal information**, including whether it's used for training.
- **Thoughtfully evaluate model capabilities early.** General vs task-specific models; availability can depend on device compatibility, network and battery (Foundation Models needs Apple Intelligence on).
- **Be intentional when choosing or creating a dataset.** Diverse representation; known provenance; proper licenses; time for testing to mitigate bias and misinformation.
- **Guide people on how to use the feature.** Diverse predefined example inputs.
- **Raise awareness about, and minimize, hallucinations.** Say AI content may contain errors; scope requests tightly; avoid factual requests unless the model has verified, current information; never use generated content where a hallucination could harm.
- **Consider consequences and get permission before irreversible or problematic tasks.** Don't automate destructive actions (deleting photos) or hard-to-undo ones (purchases); confirm significant actions; follow model usage policies and regional regulation.
- **Make it easy to refine or revert results, and acknowledge corrections.** Edit, Undo, Retry, Adjust near the output; clear signal that an adjustment took effect.
- **Help people improve requests when results are blocked or undesirable.** Coach toward success; offer example requests.
- **Reduce unexpected and harmful outcomes with thoughtful design and thorough testing.** Test out-of-scope, vague, ambiguous, sensitive and adversarial requests; improve the model, prevention and responses.
- **Strive to avoid replicating copyrighted content.** Build on models that guard against it; curate inputs (pre-approved prompts); instruct the model to avoid specific content or styles.
- **Factor processing time into your design.** Generative models are slower than real-time models (ARKit body tracking, Vision) — design a loading experience or generate in the background.
- **Give specific, reassuring feedback during generation.** "Finding substitutions for ingredients", not "Processing…"; on failure, plain-language explanation and a next step.
- **Consider offering alternate versions of results** so people can choose.
- **Consider ways to improve the model over time.** Frequent small updates (blocked-word lists) and planned major ones; fine-tune, retest and re-engineer prompts when changing base models.
- **Let people share feedback on outputs.** Voluntary, non-interrupting, clearly placed; quick thumbs up/down plus a detailed path; act on it quickly.
- **Design flexible, adaptable features.** Separate the model from the UX so models can be swapped as capabilities evolve.

**Platform notes**
- No additional considerations for any platform.

**Dev refs**
Foundation Models, Core AI, Apple Intelligence and machine learning overview, Acceptable Use Requirements for the Foundation Models Framework, Vision, ARKit body motion capture, Machine learning (HIG), Loading (HIG), Privacy (HIG)

## HealthKit
Full page: hig/technologies/healthkit.md · Platforms: iOS, iPadOS, watchOS
Central repository for health and fitness data; apps with health/fitness functionality can ask permission to read and write it. Apps without health or fitness functionality must not request health data.

**Rules**
- **Provide a coherent privacy policy** via the required URL at submission.
- **Request access to health data only when you need it**, in context (e.g. when logging weight), and on every access since permissions can change (`requestAuthorization`).
- **Clarify intent with descriptive messages on the standard permission screen.** Succinct why/benefit; no custom replicas of the system screen.
- **Manage health data sharing solely through Settings > Privacy.** No in-app screens that alter the flow of health data.
- **Use Activity rings for Move, Exercise and Stand information only.** Never replicate or modify them for other data; never show Move/Exercise/Stand in another ring-like element.
- **Use Activity rings to show progress for a single person**, with an obvious label, photo or avatar.
- **Don't use Activity rings for ornamentation** — never in labels or background graphics.
- **Don't use Activity rings for branding** — never in the app icon or marketing.
- **Maintain Activity ring and background colors.** No filters, color changes or opacity changes; design the surrounding UI to blend (e.g. enclose in a circle); scale appropriately.
- **Maintain Activity ring margins.** Outer margin ≥ the distance between rings; nothing crops, obstructs or encroaches; to show rings in a circle, adjust the enclosing view's corner radius rather than applying a circular mask.
- **Differentiate other ring-like elements from Activity rings** with padding, lines, labels, color or scale.
- **Provide app-specific information only in Activity notifications.** The system already sends Move/Exercise/Stand updates; never show an Activity ring in your notifications.
- **Use only the Apple-provided Apple Health icon** from Apple Design Resources; never mimic it.
- **Display the name *Apple Health* close to the icon.**
- **Display the Apple Health icon no smaller than other health-related app icons** in the same view.
- **Don't use the Apple Health icon as a button** — compatibility indicator only.
- **Don't alter the icon's appearance.** No corner-radius masking or circular shape; no borders, overlays, gradients, shadows or effects.
- **Maintain clear space around the Apple Health icon of 1/10 of its height**; don't composite it onto another graphic.
- **Don't use the icon within text or in place of *Health*, *Apple Health* or *HealthKit*.**
- **Don't display Health app images or screenshots** — copyrighted; use an Activity ring element instead.
- **Refer to the Health app as *Apple Health* or *the Apple Health app*.**
- **Don't use the term *HealthKit* in user-facing text.** Say the app "works with the Apple Health app" or "uses data from the Apple Health app".
- **Capitalize *Apple Health* as two words**, uppercase A and H; all-uppercase only to match an established all-caps interface style.
- **Use the system-provided translation of *Health*.**

**Platform notes**
- iOS/iPadOS/watchOS: no additional considerations · macOS/tvOS/visionOS: not supported.

**Specs**
Apple Health icon clear space: 1/10 of its height · Activity ring outer margin ≥ inter-ring distance.

**Dev refs**
HealthKit, HKHealthStore.requestAuthorization(toShare:read:completion:), HKActivityRingView (HealthKitUI), Protecting user privacy, Works with Apple Health badge, Apple Design Resources

## HomeKit
Full page: hig/technologies/homekit.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS · Latest change 2023-05-02
Secure control of connected home accessories via Siri or the Home app. An iOS, tvOS or watchOS app integrates to help set up, name and organize accessories, offer fine-grained or custom accessory features, teach automations, and provide support. MFi licensees: see the MFi portal for packaging naming/messaging.

**Rules**
- **Use HomeKit's terminology and object model.** *home* (root; people can have several) → *rooms* (names only) → *accessories* (physical devices, each in a *category* such as thermostat, fan, light) → *services* (controllable features, e.g. garage door opener, ceiling fan light — spoken to Siri) → *characteristics* (controllable attributes, e.g. speed, brightness). *Service groups* control several services as one; *actions* change a characteristic; *scenes* group actions (API term *action set* — always say *scene* in UI); *automations* react to location, time, accessory state or sensors; *zones* group rooms (upstairs/downstairs). Never show the words *service* or *characteristic* in UI.
- **Acknowledge the hierarchical model** even if your UI isn't organized by rooms and zones — people need locations for Siri/HomePod commands.
- **Make an accessory's related HomeKit details easy to find.** Room, zone, etc. in the accessory detail view, not buried in settings.
- **Recognize that people can have more than one home**; show the relevant home in the accessory detail view.
- **Don't present duplicate home settings.** Defer to Home app settings; don't make people re-set up their home.
- **Use the system-provided setup flow** (`performAccessorySetup`) — naming, network join, pairing, room and category assignment, favorites in a few steps.
- **Provide a purpose string explaining Home data access**, e.g. "Lets you control this accessory with the Apple Home app and Siri across your Apple devices."
- **Don't require an account or personal information.** Defer to HomeKit; make any cloud account optional and offer it after HomeKit setup.
- **Honor people's setup choices.** Don't force other platforms into the HomeKit setup flow.
- **Carefully consider a custom setup experience.** Always start with the system flow; offer a custom post-setup experience for unique features once basic functionality works.
- **Suggest service names that suit your accessory**; never suggest company names or model numbers.
- **Check that names follow HomeKit naming rules** when your app allows renaming: only alphanumeric, space and apostrophe characters; start and end with a letter or digit; no emojis. Explain violations and suggest alternatives. Valid: "Reading lamp", "2nd garage door"; invalid: "📚 lamp", "#2 garage door".
- **Help people avoid location information in service names** ("kitchen light" breaks voice control); detect it and guide people to assign the room or zone instead.
- **Present example Siri commands using the chosen service name right after setup.**
- **After setup, teach more complex Siri commands** in context (e.g. in a scene detail view: *You can say "Hey Siri, set 'Movie Time.'"*). Siri resolves services, service groups, accessory categories, rooms, zones, scenes, homes, characteristics (brighter/dim/open/occupancy) and the current home/room via HomePod.
- **Recommend zones and service groups when they make sense** for your accessory ("upstairs", "media center").
- **Offer shortcuts only for accessory-specific functionality HomeKit doesn't support** (e.g. "Order AC filters"); never duplicate HomeKit voice control.
- **If you support both HomeKit and shortcuts, explain the difference**; never encourage a shortcut for a scene or action HomeKit already handles.
- **Be clear about what people can do in your app versus the Home app.** Guide scene creation for your accessory's actions, then point to the Home app to add other accessories.
- **Defer to HomeKit if your database differs.** Reflect Home-app and third-party changes automatically; if a conflict needs confirmation, show it visually (e.g. both names side by side).
- **Ask permission before updating the HomeKit database from your app.** Never overwrite settings without explicit direction.
- **Cameras: don't block camera images.** Alerts may supplement; don't cover the picture.
- **Cameras: show a microphone button only if the camera supports bidirectional audio.**
- **Use only Apple-provided HomeKit and Home app icons** from Apple Design Resources. HomeKit icon for setup/instructional content; Home app icon when referencing the app or linking to its App Store page.
- **Icon styles:** black on white/light backgrounds when other technology icons are black; white on black/dark when others are white; custom color when others share it.
- **Position the HomeKit icon consistently with other technology icons** (same shapes/containers).
- **Use the HomeKit icon noninteractively.** Not in custom buttons; the Home app icon may open the App Store product page.
- **Don't use the HomeKit icon within text or as a replacement for the word HomeKit.**
- **Pair the icon with the name *HomeKit* correctly** — below or beside, only if other technologies are shown that way, in the layout's font.
- **Emphasize your app over HomeKit** / Apple Home.
- **Adhere to Apple's trademark guidelines.** No Apple trademarks in app name or images; singular only, never possessive; never translate Apple, Apple Home, HomeKit or other trademarks; no category descriptors (iPad, not tablet); no implied sponsorship, partnership or endorsement; correct credit lines wherever legal text appears; mention Apple devices/OSes only in technical specs or compatibility descriptions ("…from your iPhone or iPad", not "…from your iOS devices").
- **Capitalize correctly.** *HomeKit* one word, uppercase H and K; *Apple Home* two words, uppercase A and H; all-uppercase only in an all-uppercase layout.
- **Don't use *HomeKit* as a descriptor.** Use *works with*, *use*, *supports*, *compatible*: "[Brand] lightbulbs work with HomeKit", "HomeKit-enabled thermostat", "You can use HomeKit with [App Name]" — not "HomeKit lightbulbs".
- **Don't suggest HomeKit performs an action.** "Back door is unlocked with HomeKit" — not "HomeKit unlocked the back door".
- **Use *Apple* with *HomeKit* if desired** ("Compatible with Apple HomeKit") and **use *HomeKit* for setup, configuration and instructions** ("Open HomeKit settings").
- **Use *Apple Home* whenever referring specifically to the app.** Full name on first mention in body copy, "the Home app" afterward; never just "Open Home."

**Platform notes**
- No additional considerations for any platform.

**Specs**
Service name rules: alphanumeric + space + apostrophe only · starts and ends with a letter or digit · no emoji.

**Dev refs**
HomeKit, HMAccessorySetupManager.performAccessorySetup(using:completionHandler:), MFi portal, Apple Design Resources, Apple Trademark List, Guidelines for Using Apple Trademarks

## iCloud
Full page: hig/technologies/icloud.md · Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS · Latest change 2025-06-09 (game data sync)
Transparent access to people's content from any device without explicit synchronization; people shouldn't need to know where content lives. Integrate for documents, app state and game saves.

**Rules**
- **Make it easy to use your app with iCloud.** Work automatically once iCloud is on; if offering a choice, show one simple all-or-nothing option on first launch.
- **Avoid asking which documents to keep in iCloud.** Automate file management.
- **Keep content up to date when possible**, balanced against storage and bandwidth; for very large documents let people control downloads, indicate when a newer version exists, and give subtle feedback when a download takes more than a few seconds.
- **Respect iCloud storage space.** Store what people create, not regenerable resources; iCloud backups include every app's Documents folder, so be selective about what goes there.
- **Behave appropriately when iCloud is unavailable.** No alert when iCloud or Airplane Mode is toggled; optionally note unobtrusively that changes won't sync until access returns.
- **Keep app state information in iCloud** (e.g. last page read) — only for settings people want on all devices.
- **Warn about the consequences of deleting a document.** Deletion removes it from iCloud and every device — warn and confirm.
- **Make conflict resolution prompt and easy.** Resolve automatically where possible; otherwise an unobtrusive notification that makes versions easy to tell apart, as early as possible.
- **Include iCloud content in search results.**
- **For games, consider saving player progress in iCloud** with the GameSave framework (cross-device sync, built-in alerts for offline syncing and conflicts, or custom UI over its data).

**Platform notes**
- No additional considerations for any platform.

**Dev refs**
CloudKit, GameSave

## ID Verifier
Full page: hig/technologies/id-verifier.md · Platforms: iOS · Latest change 2023-09-12 (new page)
Lets an iPhone app read ISO 18013-5 mobile IDs in person with no external hardware (iOS 17+). *Display Only* requests show name/age/portrait in system UI without passing data to your app; *Data Transfer* requests (extra entitlement) return data when you have a legal verification requirement.

**Rules**
- **Ask only for the data you need.** For an age gate use an age-threshold request (`ageAtLeast(_:)`), not current age or birth date.
- **Register for ID Verifier through Apple Business Register if your app qualifies**, so your organization name and logo appear on customers' devices during verification.
- **Provide a button that initiates verification.** Labels like "Verify Age" (simple age check) or "Verify Identity" (detailed data request); no symbol implying a communication type (NFC, QR); never the Apple logo in the label.
- **In a Display Only request, let the operator record the result of their visual check**, e.g. "Matches Person" / "Doesn't Match Person" buttons returning approved/rejected.

**Platform notes**
- iOS only · iPadOS/macOS/tvOS/visionOS/watchOS: not supported.

**Specs**

| Button type | Example usage |
|---|---|
| Verify Age (image stripped; label from rule text) | An app that checks whether people are old enough to attend an event or access a venue, like a concert hall. |
| Verify Identity (image stripped; label from rule text) | An app that verifies whether specific identity information matches expected values, such as name and birth date when picking up a rental car. |

**Dev refs**
ProximityReader — Adopting the Verifier API in your iPhone app, MobileDriversLicenseDisplayRequest, MobileDriversLicenseDataRequest, MobileDriversLicenseRawDataRequest, Apple Business Register, Wallet identity verification

## iMessage apps and stickers
Full page: hig/technologies/imessage-apps-and-stickers.md · Platforms: iOS, iPadOS · Latest change 2023-05-02
iMessage apps let people share content, collaborate and play games inside a Messages conversation; sticker packs decorate conversations and also appear in Messages and FaceTime effects. Ship as a standalone app or as an extension of your iOS/iPadOS app.

**Rules**
- **Prefer one primary experience per iMessage app.** Immediately understandable in conversational flow; split distinct functions into separate iMessage apps.
- **Consider surfacing content from your iOS/iPadOS app** (shopping list, itinerary) or a simple collaborative task (choosing a restaurant or movie).
- **Present essential features in the compact view** (below the transcript); reserve extras for the expanded view.
- **In general, let people edit text only in the expanded view** — the compact view is roughly keyboard-sized.
- **Create stickers that are expressive, inclusive and versatile.** Legible on varied backgrounds, rotated and scaled; use transparency to blend with text, photos and other stickers.
- **Provide a localized alternative description for each sticker** for VoiceOver.
- **Supply a square-cornered icon** in every listed size; the system applies the rounded mask.
- **Pick one sticker size and use it for the whole pack** — don't mix sizes. Supply @3x; the system downscales to @2x/@1x at runtime (`MSStickerSize`).

**Platform notes**
- iOS/iPadOS: no additional considerations · macOS/tvOS/visionOS/watchOS: not supported.

**Specs**

Icon sizes (the empty Usage cells are row-spanned under "Messages, notifications" in the source):

| Usage | @2x (pixels) | @3x (pixels) |
|---|---|---|
| Messages, notifications | 148x110 | - |
|  | 143x100 | - |
|  | 120x90 | 180x135 |
|  | 64x48 | 96x72 |
|  | 54x40 | 81x60 |
| Settings | 58x58 | 87x87 |
| App Store | 1024x1024 | 1024x1024 |

| Sticker size | @3x dimensions (pixels) |
|---|---|
| Small | 300x300 |
| Regular | 408x408 |
| Large | 618x618 |

Sticker file size: 500 KB or smaller.

| Format | Transparency | Animation |
|---|---|---|
| PNG | 8-bit | No |
| APNG | 8-bit | Yes |
| GIF | Single-color | Yes |
| JPEG | No | No |

**Dev refs**
Messages framework, MSStickerSize, Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime
