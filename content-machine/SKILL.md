---
name: "content-machine"
description: "Write, fix or adapt Cove / Auto Europe Group FAQs and copy to house style for every audience - consumer (incl. motorhomes and leasing), travel agent, My Account, chatbot and Zendesk responses. Checks new FAQs against the live set for duplicates. Use instead of the older cove-content-style skill. Trigger on any request to reword, rewrite, tidy, fix, draft, add or make on-brand an FAQ, help page, email, SMS, UI text or partner content, to copy an FAQ to another audience, or when the user mentions the style guide, house style or the FAQ Machine."
---

# Content Style Fixer

One skill for every piece of FAQ and help copy The Cove and Auto Europe Group (AEG) publish. It has three jobs:

1. **Fix** - bring existing copy into house style with the minimum change.
2. **Write** - turn a rough question and answer (an FAQ Machine submission, an email, a note from Support) into a finished FAQ for the audience(s) it was logged against.
3. **Adapt** - rewrite an approved FAQ for a different audience when a product manager (PM) copies it across.

Work out which job you're doing, and which audience(s) it's for, before you change a word. If the audience isn't stated, infer it from where the copy will live (help centre, Partner Portal, My Account booking page, chatbot, a support reply). If it really can't be inferred, ask once.

---

## Core philosophy

**Self-support comes first.** The knowledge base's #1 job is letting the reader resolve their question without contacting support. Every rule below serves that goal. When a rule applied literally would work against it - burying the answer under repeated jargon, or making the reader click elsewhere for the one fact that resolves their question - self-support wins.

Three tests before shipping any edit:

- **Does this answer, read on its own, resolve the question?** If the key fact lives only on another page, pull it into this answer and link out only for supporting detail.
- **Can the reader scan it and get the point quickly?** If a terminology rule forces the same phrase to repeat 3 or 4 times in a short answer, favor scannability.
- **Is this fact the same for every reader, or does it vary by supplier, country or booking?** If it's the same for everyone and we can state it accurately, state it. Save the My Account pointer for facts that genuinely differ, or for when the reader needs to do something (change a booking, look up their own number, start a claim). My Account is a self-service route for action or booking-specific lookup - not a default sign-off.

**Support is a last resort.** Only point to the contact form when the reader really has to make contact. Never give a phone number as a contact route. Never end an answer that already resolves the question with "contact us".

**Never invent.** Don't fabricate facts, fees, timeframes, link targets, UI labels or features. If a fact or link the style needs is missing, leave the gap (use `TBD` placeholders for unknown link numbers, e.g. `?faq_category=TBD`). Never describe a feature, button or search that doesn't exist on the page. If you're unsure whether something is true on the live frontend, say so to the user rather than writing it as fact.

### Fix mode is minimum-touch

- Respect the input's structure and length. Change only what breaks the rules.
- Preserve facts, numbers and links exactly. Don't update prices, percentages or URLs. Don't convert currencies.
- Rows or answers that already comply stay as they are.

### Write and Adapt modes may restructure

When writing from a rough submission or adapting to a new audience, you can reorder, split, merge and trim to fit the audience pattern below - but every fact must come from the source. Don't add facts the source doesn't contain.

### Before writing a new FAQ: check for similar ones

Every new FAQ (Write mode, or Adapt mode into an audience) starts with a duplicate check, because the knowledge base should stay small and one topic should live in one place.

1. **Read the live set for that audience** (see "Where it lives" under each audience): the consumer production sheet `en-US - Source` tab, the `app-faqs` tab for My Account, the TA FAQ sheet, or the chatbot CSV. If you can't reach it, ask the user to share it or paste the list of questions - don't skip the check silently.
2. **Compare by meaning, not wording.** "Is there a fee if I'm under 25?" and "Do young drivers pay extra fees?" are the same FAQ. Check questions and answers, since the topic may sit inside a broader answer.
3. **Decide and tell the user before writing** (one short line per match, with the existing faqId / Id and question):
   - **Already covered** - don't add a new FAQ. Suggest updating the existing one if the submission adds a fact it's missing.
   - **Overlaps** - suggest merging into the existing FAQ (keep the more specific term; a merged FAQ can carry a 2-part title) or narrowing the new one so it doesn't repeat the other, with a cross-link between them.
   - **Same topic, different process** (e.g. claims for CDW vs Full Protection) - keep it separate and cross-link both ways.
   - **No match** - write it, and name the category and next free number it should take (or `TBD`).
4. Also check the other audiences' sets when the FAQ is being copied across, so the same topic isn't answered differently in two places.

---

## Output rules

Return **only the content**. No preamble, no postamble, no edit summary, no inline editorial notes, no "Note for sheet entry" lines.

- **Fix mode:** preserve the input's shape. Q&A in, Q&A out. Email in, email out.
- **Write / Adapt mode for several audiences:** return one block per audience, each headed with the audience name only (`Consumer`, `Travel agent`, `My Account`, `Chatbot`, `Zendesk response`), containing the question and answer.
- **When the user asks for comments or a change log** (e.g. a review doc with an "Updated Answers" and "Comments" column), give the rewrite in one place and the reason in the other. Otherwise, no commentary.
- If something can't be resolved without inventing (an unknown link number, a fact you can't confirm), use a `TBD` placeholder in the copy and tell the user in one line after the content.
- Duplicate-check findings for a new FAQ (see above) come before the content, one line per match.

---

## Shared house rules (all audiences)

### Voice

One neutral voice everywhere. Simple and direct - a knowledgeable colleague explaining something quickly, not a mascot and not a lawyer.

- Short sentences (8-18 words is typical).
- Direct openers: "You can...", "Yes.", "No.", "Most rental suppliers...".
- Always use contractions: don't, you'll, it's, can't, won't.
- No slang, idioms, humor or mascot phrasing ("pop in", "rock up", "we've got you covered", "sort out", "cover your bases").
- No legalese or jargon.
- No "you must", "you are required to" or "we will". Use "you'll need to" or restructure.
- Lead benefits with the reader's gain: "For peace of mind...", "To save time at the rental desk...".
- **No emphasis flags.** No `Important:`, `Note:`, `Tip:`, `FYI:` prefixes, bold or not. The live sheet's older Master Style Guide allows "Important:" - that's superseded. Write the point as plain prose.
- **No em dashes.** Use a hyphen with spaces ( - ) or restructure the sentence.

### Always US English

The English source is always US English. en-GB and other languages are translation targets generated downstream.

| Use | Don't use |
|---|---|
| license, driver's license | licence |
| canceled, canceling | cancelled, cancelling |
| traveler | traveller |
| tires | tyres |
| kilometer | kilometre |
| gray | grey |
| windshield | windscreen |
| organize, recognize, incentivized | organise, recognise, incentivised |
| center | centre |
| pre-authorization | pre-authorisation |
| behavior | behaviour |
| learner's permit | learner permit / provisional licence |
| car rental, rental car | car hire |

### Numbers, currency, units

- **All numbers in digits** - body, bullets, titles, tooltips. *1 driver, 3 days, 2 weeks, 48 hours, 21 years old.*
- **Currency in USD** in the source. Preserve the amount as written; translation substitutes local figures. Don't quote one market's fee (e.g. an AUD no-show fee) as if it were global.
- **Distances in miles.** Exception: keep local units when quoting a local legal limit or a supplier's own rule (e.g. a New Zealand speed limit in km/h).
- **Percent, no space:** 50%.
- **Ranges: en dash, no spaces:** 1–2 hours.
- **Timeframes are conservative.** If unsure between 2 figures, use the longer one ("say more rather than less").
- **Prefer evergreen phrasing to dated statistics** ("thousands of sites", not "7,297 sites").

### Brand names

The rule depends on the audience:

- **Consumer FAQs (help centre):** "Auto Europe" may be used where it makes the answer clearer and matches approved copy - e.g. "Auto Europe voucher number", "your Auto Europe invoice", "How do I contact Auto Europe?". Don't add it where "we" / "us" reads just as well. The value-claim footnote may cite "RentalCover.com research" as approved. Never name the supplier brands (Hertz, Avis, THL, Jucy).
- **All other audiences (travel agent, My Account, chatbot, Zendesk responses) and partner-reused content:** strictly brand-neutral. "We" / "us" / "our" for the platform, "our partners" for protection providers, "our research" in footnotes, and no tool or vendor names (Zendesk, Relevance, etc.). These surfaces serve several brands (Auto Europe, DriveAway, Car Rental 8).
- When adapting a consumer FAQ to any other audience, remove "Auto Europe" and RentalCover.com.

| Refers to | Use | Don't use |
|---|---|---|
| Car rental company | **the rental supplier** or **the supplier** | "the rental company" (confusing, as AEG is itself a rental company), "the agency", "vendor" |
| Protection providers | "our partners" | partner names (outside the approved consumer footnote) |
| Tools and vendors | omit | "Zendesk", any tool name |

### Terminology

| Concept | Use | Don't use |
|---|---|---|
| Excess / deductible | **deductible (also known as an excess)** on the first mention in an answer; later mentions shorten to "the deductible", "deductible/excess" or "a deductible reduction" | "the excess" alone as the first mention, "the excess fee" |
| Protection as a generic noun | **protection** (singular) | "cover", "coverage", "protections" |
| Insurance | only for the customer's own policy or their credit card benefit | "insurance" for anything we or the supplier sell |
| What protection does | **reimburses you for supplier charges** | "covers you for", "insures against", "you're covered" |
| Who's eligible | "only drivers named on the rental agreement are eligible for reimbursement" | "you're only covered if..." |
| Liability | "...for which you're responsible under the terms of the rental agreement" | vague "you'll pay" |
| Roadside | "roadside assistance covers **mechanical faults only**" | "roadside cover" |
| Email | "email" | "e-mail" |
| Phone | "mobile number" | "cell phone", "phone number" alone |
| Pick-up / drop-off | "pick-up", "drop-off" (hyphenated) | "pickup", "collection" |
| Acronyms | full term once, then the acronym: "Collision Damage Waiver (CDW)" | CDW with no introduction |

**Pair once, don't repeat.** Pair "deductible (also known as an excess)" in full on the first mention per answer. Later mentions in the same answer shorten as long as the meaning is clear. A question title can carry the pairing too ("What is a deductible (also known as an excess) and how does it work?"); the answer still pairs it once.

**Product names stay literal** even when they contain "cover": Full Protection, Annual Full Protection, Flexible Cancellation Protection, Breakdown Protection (older copy: Breakdown Cover - keep whichever the source uses, don't mix in one answer), Collision Damage Waiver (CDW), Theft Protection, Supplemental Liability Insurance (SLI), Premium Excess Guarantee. Never rename or translate a product name in the English source.

### Grammar and punctuation

- Bullet fragments: no trailing period. Bullet sentences: trailing period.
- Oxford comma.
- Double quotes for quoted text.
- Hyphens: out-of-state, cross-border, pick-up, drop-off, pre-authorization.
- Headings in Title Case.
- UI labels and feature names in plain Title Case, exactly as on screen - *Manage My Bookings, Cancel or Modify, Add Driver, Edit Extras, Contact Support*. No bold, quotes or italics.
- Markdown bullets use `* `.

### Bullets

- Any list of 3+ items becomes bullets, even when buried in prose. 2 items can stay inline.
- **All or nothing.** In a given answer, either the key points are bulleted or nothing is. Never put the important points in prose and minor ones in bullets - readers only read the bullets.
- Heterogeneous items use a colon-label: *"Security deposit: The amount shown in your booking terms."*
- Pull "if X then Y, but if Z then W" logic out of prose into bullets.

### Links

- Link the **concept words**, never "here", "click here" or "this article". Link text is a page name or the full title of the linked FAQ.
- No question mark inside link text and no period straight after a question link.
- One link per concept per answer. Link at the end of a sentence where possible.
- **A link supplements the answer, never replaces it.** State the essential fact, then link for more.
- Link to the **specific** FAQ (the CDW claim FAQ, not the general claims FAQ). Double-check the number - a wrong number sends the chatbot to the wrong answer too.
- Relative links only. Never full autoeurope.com URLs or legacy paths like `/my-booking`, `/form`, `/account` in help-centre copy.
- Allowed targets: `/member-accounts` (My Account), `/contact` (contact form), `/privacy`, `/help`, brand SEO pages that exist (e.g. `/international-driving-permit-faq`, `/motorhome-rental`), and FAQ cross-links. Don't link to `/claim` or `/search-result`.
- Don't load an FAQ with resource lists (sites, parks, affiliate websites). Link to a single SEO article instead, or point to the supplier.

### Content rules from review

- **Don't state facts that vary as if they're universal.** Strip supplier-specific fees and percentages ("$350 + 20%") and write "Conditions vary by supplier" plus the self-service pointer.
- **Claims always start in My Account**, never by email. Don't hard-code one claim vendor's process; routing depends on the protection purchased.
- **Don't repeat the question as the opening of the answer.**
- **One topic per FAQ.** Split multi-topic FAQs. Merge near-duplicates (keep the more specific term). A merged FAQ can carry a 2-part title: "What is Full Protection? How is it better than what I can buy at the rental desk?"
- **Limit the number of FAQs, but keep separate FAQs where the process genuinely differs** (e.g. claims for Full Protection, CDW and SLI each get their own FAQ and cross-link).
- **Only write about what's live.** Don't write FAQs for features that aren't on day 1.
- Grammar passes must not lose nuance. Fix punctuation, double spaces and paragraph breaks without flattening meaning.

---

## FAQ anatomy (all audiences)

**Question** - in the reader's own words, the way they'd actually ask or type it. *"Can I take my rental car on a ferry?"*, not *"Cross-border travel: permissions and restrictions."* Ends with a question mark. One topic.

**Opener** - answers the question in the first sentence. No preamble.

| Question type | Opener | Example |
|---|---|---|
| "How do I X?" | "You can [verb] in [location]." | You can add extra drivers through [My Account](/member-accounts). |
| Yes/no | "Yes." or "No." + declarative | Yes. The card you used to book with us can be different from the card you use for the supplier's deposit. |
| "What is X?" | "[X] is [definition]." | A deductible (also known as an excess) is the amount you pay if your rental car is damaged or stolen, even if it wasn't your fault. |
| "Why X?" | Direct factual statement | The security deposit is required by the rental supplier and is shown in your booking terms. |
| "What if X?" | "If X, [outcome]." | If you haven't received your booking confirmation, your contact details may have been entered incorrectly. |

Drop "Yes." when the question isn't a yes/no question.

**Body** - conditional logic and lists in bullets (all-or-nothing). Pull in any fact the answer depends on.

**Closer** - often a link, often skipped.

- First decide if a closer is needed. If the fact is universal and already stated, skip it.
- Point to My Account only when something genuinely varies by supplier, country or booking, or the reader needs to act.
- Don't send readers to their booking confirmation or confirmation email as well as My Account. My Account holds the same details, so one route is enough.
- Standard closers are audience-specific - see each audience below. Use them word for word, because fixed phrasing translates consistently.

---

## Audience: Consumer (help centre)

**Reader:** a customer on the public help centre (`/faqs`), either before booking or after.

**Where it lives:** the "FAQ (Questions & Answers) Production file" Google Sheet (ask the skill maintainer for the link), `en-US - Source` tab. Columns: Group | Number | Question | Answer | Popular. Groups:

1. Manage My Account
2. Pick-up & On The Road
3. Protection, Insurance & Deposits
4. Rental Rules & Conditions
5. Charges & Refunds
6. Claims

Number format is `3_04` (category_sequence). Cross-links: `[Flexible Cancellation Protection](?faq_category=3&faq_question=08)` with the question number zero-padded. Hand finished FAQs to the `add-faq-to-sheet` skill with faqId, group, question and answer.

**Closers (word for word):**

- Booking-specific detail: `For details specific to your booking, see [My Account](/member-accounts).`
- Changes: `For changes to your booking, go to [My Account](/member-accounts).`
- Obvious next step: `If you need to add an additional driver, see [How do I add an additional driver](?faq_category=1&faq_question=02).`

**Value-claim footnote:**

```
... up to 50%<sup>†</sup> cheaper than equivalent products sold at the rental desk.
<small><sup>†</sup> Based on average rental desk prices from RentalCover.com research.</small>
```

Protection FAQs may be confidently persuasive ("you can safely decline the supplier's competing product") as long as every claim is in the approved source.

**Contact FAQ order** (how to reach us): My Account for changes, then the supplier for vehicle and desk issues, then the claims FAQ, then the contact form "Have your voucher number ready". No phone number.

### Worked example (Fix mode)

Source:

> Q: Can I cancel or change my booking, and will there be a fee?
> A: You can cancel or change your booking via your account. If you do this more than 48 hours before pickup it's normally free, but if you cancel inside that window we charge a fee unless you purchased Flexible Cancellation Protection. Note that rental prices change so modifying may show a different price.

Fixed:

> Q: Can I cancel or change my booking, and will there be a fee?
> A: You can cancel or make changes in [My Account](/member-accounts).
>
> * If you cancel or modify more than 48 hours before pick-up, there is usually no fee.
> * If you cancel within 48 hours of pick-up, a cancellation fee may apply. If you added [Flexible Cancellation Protection](?faq_category=3&faq_question=08) when you booked, you'll have a more generous cancellation window.
> * Rental rates can change over time, so if you modify your booking you may see a different price.
>
> For changes to your booking, go to [My Account](/member-accounts).

*When not to add a closer:* "Is my booking deposit non-refundable?" → "Yes. Your deposit is non-refundable if you cancel after booking." It's universal; a My Account pointer would imply an exception that doesn't exist.

### Consumer: Motorhomes

Motorhome FAQs use the consumer rules plus:

- **Terms:** "motorhome" is primary. Questions may say "motorhome or campervan". Use "RV" for the USA and Canada. "Security bond" (or "holding bond"), not "security deposit". "Campgrounds", "depot", "rental supplier".
- **Product names:** use the protection product name exactly as the approved source has it (currently Premium Excess Guarantee for the standalone motorhome product in some copy, Full Protection in others). Don't mix names within one FAQ. If the source is ambiguous, keep it and flag it to the user. Call CDW and Theft Protection "protection", not "insurance".
- **Closer (word for word):** `Check the conditions at the time of booking, or see [My Account](/member-accounts).` Keep "at the time of booking" - pre-booking readers can't log in. Don't add the booking confirmation or email to the closer.
- **Strip supplier-specific fees and rules** (cancellation fee amounts, one-way restrictions) unless they're verified and genuinely universal. "Conditions vary by supplier." plus the closer.
- **Verify against supplier terms.** Claims that may be out of date (e.g. "only available from France") get removed or flagged, not kept.
- **Write product FAQs generically** where the same answer works for cars and motorhomes. Don't add "motorhomes, caravans and RVs" to shared protection FAQs.
- **Don't list parks or sites.** Link to the brand's SEO page where one exists, or point to the rental supplier.
- Categories follow the consumer groups (Make/manage a booking, Protection & deposits, Pick-up & on the road, Charges & refunds, Claims). New category numbers that aren't confirmed stay `TBD`.

### Consumer: Leasing

No leasing FAQ set has been approved yet. Until one is:

- Apply the consumer rules.
- Only write a leasing-specific FAQ where leasing genuinely differs from a standard rental. Otherwise point to (or reuse) the existing consumer FAQ - specialized products leave out redundant FAQs.
- Treat every leasing fact (terms, minimum period, mileage, insurance, delivery) as unverified unless it's in the source. Don't infer from car rental rules. Flag gaps rather than filling them.
- Use the leasing product's own UI and contract terms exactly as supplied.

---

## Audience: Travel agent (Partner Portal)

**Reader:** a travel agent working in the Partner Portal on behalf of a client. TA-only content (commission, reporting, agency settings) must never appear on consumer FAQ pages.

**Voice and terms:**

- Address the agent as "you"; the traveler is **"your client"** in sentences. ("Customer" appears only as a UI field label.) Don't mix "client" and "customer" in one answer.
- **Partner Portal** and **Partner Support** are always capitalized. Other internal team names stay capitalized too (Reservations team, Account Manager).
- Start from the agent's context: "Within the Partner Portal you'll see..." rather than "Booking statuses indicate...".
- No "must". "Bookings need to be made directly through the Partner Portal."
- Product lists aren't exhaustive: "Commission-eligible products include:", not "Commission-eligible products:".
- Hedge where it depends on account setup: "Depending on how your account is set up, ...".
- When saying what support can't do, say what it can: "Partner Support is no longer able to create bookings on your behalf... Once you have a quote or booking, Partner Support is available if changes or requests are required that can't be processed via the Partner Portal."
- Don't shut out high-value bookings. Large bookings start with a quote, then the agent contacts us.
- Don't send agents to Partner Support for login problems. That route belongs on the login page and its error message.
- Check every UI claim ("records the agent name and email") against the live Partner Portal. If unconfirmed, flag it.
- Strictly brand-neutral - the portal serves several brands.

**Closers:**

- New portal: nearly every answer ends with a CTA link. To start a booking or quote: `[Log in](TBD) to get started.` word for word. To review or change bookings: link to the Partner Portal page that does it.
- Current (embedded) portal: the agent is already in the portal, so say "here" instead of naming the portal and skip the login closer.
- When the user's sheet has "FOR NEW PORTAL" and "FOR CURRENT PORTAL" columns, write both versions.

**Pre-booking topics agents need** (gap to fill): fuel policy, zero excess, driver age, flight validation.

**Where it lives:** TA FAQ review sheets, currently "FAQ Review - Batch 2 (Travel Agents) - Revised" (ask the skill maintainer for the link; columns ID, Category, Question, Answer, FOR NEW PORTAL, FOR CURRENT PORTAL). In the app, categories are `agent_cancellations` (Cancellations & Changes), `agent_pick_up` (Pick-Up & Documentation), `agent_protection` (Protection) and `agent_commission` (Commission & Payments). In the chatbot CSV, TA rows start the question with `[TA]`.

**Example:**

> Q: How do I update my agency details?
> A: Agency details can be updated directly in My Account within the Partner Portal. [Log in](TBD) to get started.

---

## Audience: My Account (booking page FAQs)

**Reader:** a logged-in customer looking at one booking (pre-pickup, mid-rental or post-return) or at their protection policy. The FAQs sit in an in-context panel below the booking, ending with "Still need help?".

**Rules:**

- **Never tell them to go to My Account** - they're already there. Point to the exact control on the page, by its on-screen label: Cancel or Modify, Add Driver, Edit Extras, Driver & Flight Details, the Documents section, Trip Details, View/Upgrade Protection, Manage Renewal, the Auto-Renew toggle, Update Payment Method, Cancel Policy, Profile > Communication Preferences, Profile > Account Settings > Close Account, Contact Support.
- Say **"this booking"** and **"your policy"**, not "your booking in My Account".
- **Cut branching the account already knows.** If the page knows which policy or supplier applies, don't explain every variant.
- **Leave out pre-login and pre-booking questions** - they belong on the public help centre.
- **Only cover day-1 features.** If a control isn't live yet, the FAQ waits.
- **No phone contact routes.**
- The fallback FAQ is the last step before "Still need help?": "If none of these answers help, use Contact Support below to reach us."
- Strictly brand-neutral ("Voucher number: issued when you book with us").
- Answers are short - usually 1–3 sentences, or a short colon-label list.

**Where it lives:** the app "Translations" Google Sheet (ask the skill maintainer for the link), `app-faqs` tab. Column A = category key (`booking_change_or_cancellation`, `manage_account`, `account_or_login`, `pickup_or_driver_requirements`, `pick_up_on_the_road`, `protection_deposits`, `refund_or_unexpected_charge`, `charges_refunds`, `damage_or_claim`). Ids alternate `C7_Q1` / `C7_A1`. Cross-links use `[Flexible Cancellation Protection](?faq_id=C7_Q6)`. Placeholders in curly braces stay untouched.

**Example:**

> Q: How do I add an additional driver?
> A: You can add extra drivers using Add Driver on this booking, if the option is available. If it's not shown, you can add a driver at the rental desk for a fee.

---

## Audience: Chatbot

**How the bot uses it:** the FAQ chatbot loads a 2-column CSV (Question, Answer; kept in the chatbot's code repo and currently built from the consumer set) and matches the customer's message to the closest **question by meaning**. On a confident match it sends the **answer verbatim**, with no rewriting. Relative links are turned into full links automatically. So each row has to work as a complete chat reply on its own.

**Rules:**

- **Questions in the customer's words.** Write the question the way people actually type it. "What age do I need to be to rent a car?" matches; "Is there a fee if I'm under 25?" filed under "Young driver surcharge" doesn't.
- **One topic per row.** A row covering 2 topics only ever returns as one answer and half gets lost. Split it.
- **Self-contained.** No "see above", no "as mentioned", no reliance on the page around it. The answer must make sense with no category heading.
- **Short.** Open with the direct answer ("Yes, you can add an additional driver at the rental desk when you pick up your vehicle."), then 1–3 short sentences or a short bullet list.
- **No "contact us" endings** unless contact is genuinely the only route. Never a phone number. Never offer to "connect" or "transfer" the reader to an agent.
- **Explain money in plain prose.** "If your deductible is $2,000 and the damage costs $600, you'll pay $600." No arrows, tables or `$600 → $600` notation.
- **Markdown is fine** (bullets, links). Keep links relative - they're absolutized automatically. Link text is a page name or a full FAQ question, because linked questions open as a new chat turn.
- **No HTML.** Leave out `<sup>`/`<small>` footnotes; state the claim without the dagger or drop the comparison.
- **Strictly brand-neutral** - the bot is deployed for several brands.
- **TA rows:** start the question with `[TA]` (e.g. `[TA] How do I check my commission?`) so they rank first for travel agents.
- Never leave stub rows ("MOVED TO...") or near-duplicate questions - fill a real gap instead. A missing topic makes the bot serve the nearest wrong answer.

**Example (adapting a consumer FAQ):**

Consumer:
> Yes. You can add an additional driver at the rental desk when you pick up your vehicle. An additional fee may apply, and the additional driver needs to bring a valid driver's license.

Chatbot:
> Yes, you can add an additional driver at the rental desk when you pick up your vehicle. A fee may apply. The additional driver needs to bring a valid driver's license.

---

## Audience: Zendesk responses (provisional)

Saved replies support agents send to customers by email. No approved set exists yet, so treat this pattern as provisional and confirm with Support before relying on it.

- **Structure:** greeting, 1 sentence that answers or confirms what's happening, the detail (bullets if 3+ items), the self-service route if one exists, specific next step, sign-off.
- **Greeting:** `Hi [name],` using the name placeholder exactly as Support supplies it. Don't invent placeholder syntax - if none is supplied, use `Hi there,`.
- **Acknowledge once, briefly**, when the customer is reporting a problem ("Sorry your vehicle wasn't available at pick-up."). No over-apologizing.
- **Self-service first:** tell them what they can do in My Account themselves. Replies go by email, so links must be full URLs; if the URL isn't supplied, leave `[My Account link]` as a placeholder.
- **End with a specific next step,** not "let me know if you have any questions" ("If you share your voucher number, we can check this booking for you."). Then `Thanks,` and the team sign-off Support uses.
- Same voice, terms and brand rules as the other non-consumer audiences. No phone numbers. Don't promise timeframes beyond what's approved.

---

## Copying an FAQ to a new audience (Adapt mode)

Start from the approved source FAQ. Keep every fact. Change only what the target audience needs:

| From → To | Change |
|---|---|
| Consumer → My Account | Replace "in [My Account](/member-accounts)" with the on-page control ("using Cancel or Modify below"). Say "this booking". Drop pre-booking content and branching the page already knows. Swap `?faq_category=` links for `?faq_id=` links (or `TBD`). Remove brand names and the RentalCover footnote ("our research"). |
| Consumer → Travel agent | "you/your booking" → "your client / your client's booking" where it's the traveler; "you" stays for the agent's own actions. Remove consumer-only routes (My Account sign-in, contact form) and use the Partner Portal / Partner Support routes. Add the "[Log in](TBD) to get started." closer where the agent starts a booking. Remove brand names. |
| Consumer → Chatbot | Rephrase the question as customers type it. One topic per row (split if needed). Make it self-contained, shorter, no HTML, no footnote dagger, no "contact us" ending. Remove brand names. Prefix `[TA]` if it's for agents. |
| Any → Zendesk response | Wrap in greeting and sign-off. Convert relative links to full URLs or placeholders. Add one specific next step. |
| My Account → Consumer | Replace on-page control references with "in [My Account](/member-accounts)". Add the booking-specific closer only where something varies. |

Then run the whole checklist for the target audience.

---

## Other content types

- **Help pages and guides:** same voice, Title Case headings, short paragraphs (2–4 sentences), bullets for any list of conditions or options. Lead each section with the reader's benefit.
- **Transactional emails:** 1 CTA (default: account creation, `/account` or `/member-accounts`). Minimal copy - don't put booking detail in the body, point to the account. No logos, no off-path links. Pair every transactional email with 1 SMS.
- **SMS:** under 160 characters where possible. 1 sentence, 1 link, 1 CTA. No exclamation marks, no emoji. Sign off "Thanks, The team".
- **UI strings:** shortest clear wording, sentence case unless it's a named feature. Keep `{placeholders}` untouched.

---

## Process context

- Every FAQ is approved before it's translated or published (the content owner approves all knowledge-base content; the FAQ Machine requires PM approval). Never translate a draft.
- Reviews happen in a single Google Doc with comments and suggestions, not in sheets, to avoid version conflicts. Once approved, run this skill over the final text to format it for the sheet.
- Consumer FAQs go into the production sheet with the `add-faq-to-sheet` skill. Translation follows the `cove-translation-sheets` / `car-rental-translator` rules.

---

## Pre-flight checklist

**Every audience**

- New FAQ: checked against the live set for that audience; duplicates and overlaps reported with their faqId before writing
- The answer resolves the question on its own; links only supplement it
- Self-service pointer only where something varies or an action is needed - not added by reflex
- No phone numbers, no "contact us" ending on an answer that already resolves the question
- Nothing invented - unknowns are `TBD` and flagged to the user in one line
- US spelling; digits for all numbers; USD; miles (local units only for local legal limits); percent with no space; en dash ranges
- Contractions; no "must", "required to" or "we will"; no slang or idioms
- "the rental supplier" / "the supplier", never "the rental company"
- deductible (also known as an excess) paired once per answer, shortened after
- "protection" (singular) as the generic noun; "insurance" only for the customer's own policy or card; product names literal
- No emphasis flags (Important:, Note:, Tip:); no em dashes
- 3+ items in bullets; bullets all-or-nothing; fragment bullets without periods
- Descriptive link text (never "here" or "this article"); no ? or . inside link text; link points to the specific, correct FAQ
- One topic per FAQ; the opener doesn't repeat the question; question in the reader's own words
- Output is clean - no commentary unless asked

**By audience**

- Consumer: brand name only where it helps and matches approved copy; consumer closers word for word; `?faq_category=X&faq_question=NN` links
- Motorhomes: motorhome terms (security bond, RV for USA/Canada); "at the time of booking" closer pointing to My Account only (no booking confirmation or email); no supplier-specific fees; no resource lists
- Leasing: nothing assumed from car rental rules; gaps flagged
- Travel agent: "your client"; Partner Portal / Partner Support capitalized; CTA closer ("[Log in](TBD) to get started."); support can/can't both stated; brand-neutral; both portal versions if the sheet has them
- My Account: no "go to My Account"; exact on-page control labels; "this booking"; day-1 features only; `?faq_id=` links; brand-neutral
- Chatbot: customer-phrased question; one topic; self-contained and short; no HTML; plain-prose money examples; brand-neutral; `[TA]` prefix for agent rows
- Zendesk: greeting and sign-off; full URLs or placeholders; specific next step; brand-neutral