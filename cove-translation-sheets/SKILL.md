---
name: "cove-translation-sheets"
description: "Translate, audit and fix Cove / Auto Europe car rental content and production translation sheets across the 14 locales (en-GB, de-DE, es-ES, es-MX, fr-FR, pt-PT, pt-BR, it-IT, da-DK, nl-NL, nb-NO, pl-PL, fi-FI, sv-SE). Use for any request to translate, review, check or fix FAQs, UI strings, policies, labels or HTML, to fill empty language columns, or to update translations after the English changed. Holds the full glossary, native-speaker corrections, an automated check script and Google Sheets connector steps. Replaces car-rental-translator."
---

# Cove Translation Sheets

Translate and maintain content for the car rental booking platform. This skill encodes
domain rules built through iteration with native-speaker feedback - terminology, product
names, protection-vs-insurance, currency, register - plus the defects found in real
production files and the mechanics of working in Google Sheets.

It replaces `car-rental-translator` and is self-contained: the full glossary and the check
script are in this file. Where an older skill or note disagrees, this one is current.

## When to use

- Translating FAQs, UI strings, policies, labels or any car rental website content
- Filling empty language columns in a translation sheet
- Updating translations after the English source changed
- Reviewing or auditing an existing production file
- Applying a batch of reviewer-suggested changes
- Translating HTML snippets while preserving tags

## The locales

15 columns: one source (en-US) plus 14 targets - en-GB, de-DE, es-ES, es-MX, fr-FR, pt-PT,
pt-BR, it-IT, da-DK, nl-NL, nb-NO, pl-PL, fi-FI, sv-SE.

Norwegian is `nb-NO`, language first. `no-NB` is a transposition and has appeared as a real
header typo in a production file - check it every time.

---

## Step 0: Audit before translating anything

Never start filling cells until the file has been audited. Production sheets have
repeatedly contained pre-existing defects that translating over would bury. Run this audit,
report what it finds, and let the user set scope before writing.

**Read the file as data, not as a rendered preview.** Markdown and preview exports truncate
long sheets silently - a gap analysis built on one under-reports missing cells (this has
already caused a wrong answer: 4 reported vs 12 actual). Read every row: either with the
Google Sheets connector (`get_values` on the full tab range, see "Working in Google
Sheets") or by exporting to .xlsx and parsing with openpyxl.

1. **Header sanity** - locale codes correct and correctly ordered; no missing column.
2. **Column shift** - a row whose translations sit one column off from their header.
   Signature: a run of cells each holding the *next* column's language, with a trailing
   empty cell at the end of the row. Affects whole rows, not single cells. Fix by
   rewriting the row's cells to the correct columns (connector), or natively in the sheet
   (select the range, cut, paste one column across) - never by pushing the text through
   the clipboard as data.
3. **Language ID** - verify statistically that each cell is in the language its column
   claims:

   ```python
   import py3langid as langid
   langid.set_languages(['en','pt','it','es','fr','de','da','nl','no','pl','fi','sv'])
   ```

   Classify per paragraph, not per cell, so mixed-language cells are caught. Expect false
   positives on the Danish/Norwegian pair and on placeholder-heavy strings - verify every
   flag by eye before changing anything. (`langdetect` fails to build here; `py3langid`
   works. A hand-rolled marker-based detector is too noisy - don't.)
4. **Truncation** - cells that stop mid-sentence, end on a dangling preposition or
   conjunction, or are far shorter than the source. Flag anything under roughly half the
   source length.
5. **Placeholder parity** - every `{variable}` in the source appears in every translation,
   same count, same spelling.
6. **Empty cells** - count per tab and per language, before and after.
7. **Letters and diacritics** - two separate checks, because language ID catches neither:
   - **Wrong letters:** no letter that belongs to another language (no ä/ö in da-DK or
     nb-NO, no æ/ø in sv-SE or fi-FI, no æ/ø/å outside the Nordic columns, no ñ outside
     Spanish). See the table under "Letter swaps and dropped diacritics".
   - **Stripped diacritics:** a long cell in a language that uses accents but contains none
     at all (Polish "Jesli samochod" for "Jeśli samochód") has usually had them stripped.

Steps 4–7 are automated by the check script (see "The check script"). Run it, then read
every flagged cell by eye.

---

## Workflow

### Step 1: Understand the input

Source language (usually en-US), target languages, content type (FAQ, UI label, policy,
HTML, country name), and audience - customer-facing or partner/affiliate-facing (Rule 9).

### Step 2: Translate one row at a time

For each row and each target language: translate with correct domain terminology, apply all
10 rules, and preserve every markdown link, HTML tag, bullet, bold marker and `{variable}`.

Work in batches of 10-20 rows, keeping a running count. After the final batch, confirm the
output row count matches the source exactly.

### Step 2b: Updating an existing string - change only what changed

When the source changes for a string that is already translated, **edit the existing
translation; do not retranslate it from scratch.** Keep every sentence whose source
sentence did not change, character for character, and rewrite only the changed part.

Regenerating a whole string retypes text that was already correct, and every retyped
word can come back with a typo. This has happened on a live PR (FE-700, da-DK FAQ). Only
the last paragraph or sentence of each string changed, but the whole strings were
regenerated, and the untouched sentences came back with Nordic letter errors:
"stjålet" → "stålet", "lejekøretøj" → "lejekøretoj". The same PR also added "ändrer"
(Swedish/German "ä") where Danish needs "ændrer".

How to do it:

1. **Snapshot before you touch anything.** Save the tab as it is now - every source and
   translation cell - to `before.xlsx` (connector `get_values` written out with openpyxl,
   or a Drive export). The old English must be in the snapshot too, so you can see which
   source sentences changed.
2. **Work sentence by sentence.** Compare old and new English per sentence. For each
   language, copy across every sentence whose English didn't change, untouched, and
   translate only the new or changed sentences.
3. **Prove it.** Save the result to `after.xlsx` and run the check script with
   `--before before.xlsx`. It flags any translation that changed when its source didn't,
   and any string where more sentences changed than the source did. Every changed word must
   come from a changed source sentence. Anything else is a regression - put the original
   back.

### Step 3: Verify

Run the check script, then the 16-point checklist below across the full output. The script
only covers mechanical checks - grammar, register and naturalness still need a read.

### Step 4: Output

- Live Google Sheet: write with the Google Sheets connector (see "Working in Google
  Sheets"), then read back.
- Excel/CSV: .xlsx with language columns filled. Read the xlsx skill first. Preserve
  column order, header row and untranslated columns exactly - only fill empty target cells.
- Single strings: a table (Language | Translation).
- HTML: preserve all tags exactly.

### Fallback - terms not in the glossary

1. Use what native car rental sites in that market actually use.
2. Flag it in a "Terms not in the glossary - please verify" section, with the choice per
   language.
3. Never invent a localized product name. No entry means keep the English name and flag it.
4. Terms marked ⚠ VERIFY in the glossary are best-judgment and not yet confirmed by a
   native speaker. Use them, but list them in the same flagged section.

---

## The 10 Rules

### Rule 1: Industry-specific terminology

One concept, one term per language, used consistently throughout. Core concepts:
deductible/excess, pickup/collection, return/drop-off, deposit/security hold, rental
counter, rental company/provider, main and additional driver, rental agreement, fuel
policy, voucher/booking confirmation, CDW, theft protection. The terms are in the Glossary.

**Never substitute from another domain** - medical (co-pays), real estate (lease/tenancy),
banking (surplus, surcharge, franchise fee for deductible), retail (gift voucher for
booking confirmation), aviation (pilot for driver), or legal jargon a customer wouldn't
understand. Watch for literal translations that land in the wrong domain in the target
language.

**One term only - no synonyms.** Remove parenthetical alternatives ("X (also known as
Y)"), slash pairs ("X/Y") and "also called" clauses. Then check for redundant "X (or X)",
dangling punctuation and broken grammar.

Note the asymmetry with source style: the US English source deliberately pairs
"deductible (also known as an excess)" on first mention for an American reader. That is a
source-language device only - in every target language it collapses to the single local
term.

### Rule 2: Product and brand names

Use localized product names exactly as listed in the Glossary. Never paraphrase into a
generic description, prefix with the local word for "insurance" or any other descriptor,
leave in English where a localized name exists, or use outdated orthography.

The current English product names (they match the content-machine skill):

| English product name | Localized name |
|---|---|
| Full Protection | In the Glossary |
| Flexible Cancellation Protection | In the Glossary (⚠ VERIFY) |
| My Account | In the Glossary |
| Theft Protection | In the Glossary (theft protection) |
| Collision Damage Waiver (CDW) | Keep "CDW"; first-mention gloss in the Glossary |
| Annual Full Protection | None yet - keep English, flag |
| Breakdown Protection (older copy: Breakdown Cover) | None yet - keep English, flag |
| Supplemental Liability Insurance (SLI) | None yet - keep English, flag |
| Premium Excess Guarantee | None yet - keep English, flag |

The Glossary's "roadside assistance" column is the generic service (what the supplier's
roadside help does), not the Breakdown Protection product. Don't use it as a name for
Breakdown Protection until a localized product name is confirmed.

### Rule 3: Protection vs insurance

The most commonly violated rule.

**"Protection"** for anything sold by the rental company or platform - branded products,
CDW and theft protection, counter add-ons, and collective references ("these insurances"
→ "these protections"). Check every form: headers, verb phrases, compounds, singular and
plural.

**"Insurance"** only for the customer's own policy, credit card benefits, or unconnected
third-party insurers. The one exception inside our products is a fixed product name that
contains "Insurance" (Supplemental Liability Insurance) - keep it as named.

### Rule 4: Grammar cascading

After replacing a term, re-check articles, adjective agreement, later pronoun references
and verb conjugation. Review data says this rule is the most under-applied: a large share
of reviewer changes were agreement errors left behind by an earlier term swap.

### Rule 5: Currency and number localization

One correct currency and number format per market (see the currency table in the Glossary).
Do not assume "EU = euro" - Denmark, Sweden and Poland are EU markets that do not use it.

- Never mix currency symbols within one language's output.
- Match separators and symbol placement: de-DE "2.000 €", fr-FR "2 000 €", en-GB "£2,000".
- **"Convert" means substitute, not calculate.** Source amounts are almost always
  illustrative - replace with a natural round figure of similar magnitude in the target
  currency. Exception: a contractual or exact amount (a real fee, a real deposit) keeps its
  original currency and value, and gets flagged for the user to confirm.

### Rule 6: Regional variant

pt-PT European (not Brazilian), pt-BR Brazilian (not European), es-ES European, es-MX
Mexican, fr-FR European. Current official spelling standard, no mixing of conventions. The
Glossary lists the key es-ES / es-MX and pt-PT / pt-BR differences.

Norwegian and Danish are the pair most often confused, by machine language ID and by
translators:

| Signal | nb-NO | da-DK |
|---|---|---|
| "what" | hva | hvad |
| infinitive marker | å | at |
| deductible | egenandel | selvrisiko |
| pickup | henting | afhentning |
| consonants | hard: bok, kake | soft: bog, kage |

Norwegian must also not drift into Swedish. A cell mixing Norwegian and Swedish forms reads
as broken to a native speaker even though language ID scores it "Norwegian" - rewrite the
whole cell rather than patching words.

### Rule 7: No cross-language leaking

Nothing from the source or a sibling language should remain, except universally accepted
loan words (voucher, online, e-mail). Watch for untranslated product names and terms
leaking from a neighbouring column.

### Rule 8: Consistency

Same concept, same term, every time - across key terms, product names, account/portal
references, driver terminology, rental company references, and pickup/return terminology.

### Rule 9: Tone and register

"Formal everywhere" is wrong - several markets read formal address as stiff or archaic.

| Language | Address form | Notes |
|---|---|---|
| de-DE | Formal - Sie | Always capitalized |
| fr-FR | Formal - vous | |
| es-ES | Formal - usted | |
| es-MX | Formal - usted | |
| it-IT | Formal - Lei / impersonal | Impersonal preferred for policy text |
| pt-PT | Impersonal / 3rd person | Avoid "tu"; avoid "você" - use impersonal or "o cliente" |
| pt-BR | você | Standard neutral register in Brazil |
| en-GB | you | Neutral |
| da-DK | Informal - du | "De" reads archaic |
| nl-NL | u | Default for booking/payment contexts |
| nb-NO | Informal - du | Standard in Norwegian web copy |
| pl-PL | Formal - Państwo / impersonal | |
| fi-FI | Informal - sinä | Standard in Finnish web copy |
| sv-SE | Informal - du | "ni" reads stiff |

Partner-facing content can be casual if the source is, but keeps the same address form.

Register is a per-file property - sample across tabs rather than checking string by string.

### Rule 10: UI strings and short labels

- **Natural word order** - rearrange for the target language, never word-for-word
- **Concise** - drop unnecessary articles and pronouns
- **Common UI terms** - what native speakers expect on websites
- **Keep loan words** where standard (FAQs, CDW, online)
- **"Popular" = widely liked**, not "frequent"
- **Expand abbreviations** the local market doesn't use
- **"&" in headings and sentence-like labels → the local conjunction** (y, e, et, und, och,
  og, ja, i, en). This reverses the older rule that said keep "&" everywhere: a native
  reviewer flagged it as English-looking in headings such as "Search & Results". Keep a
  bare "&" only in genuinely tight tabular or chip labels, and stay consistent within a tab.

---

## Corrections from native-speaker review

The patterns a reviewer actually flagged on this platform. Highest-yield re-read before
shipping.

### Truncation and dropped clauses - check first

The most damaging defects were missing words, not wrong ones. All of these reached live
sites:

- An error message reduced to its opening politeness word, actual error text gone
- A deposit tooltip stating the amount but dropping "and is held on your card"
- A fuel policy hint dropping "to avoid charges" - the reason the instruction exists
- Luggage tooltips reduced to a single stub word

A translation that loses the consequence clause, the condition, or the second half of a
sentence is worse than an untranslated string, because nothing looks broken in the UI.
Compare every translation's length against source and read any short cell in full.

### Anglicisms

Reviewers flagged English structures carried through even when every word was translated:
English word order in headings, noun stacking, English punctuation patterns, loan words
where a normal local word exists. Read each string as if seeing it on a local competitor's
site.

### Cap, limit and amount phrasing

Strings expressing a maximum ("up to", "covers up to", "maximum of") are a recurring source
of corrections. Each language has a settled commercial phrasing for a cap and the literal
rendering usually isn't it. Check every string containing a limit or an "up to".

### Letter swaps and dropped diacritics

Errors slip through as single wrong or missing letters that a skim misses, especially
after a string is regenerated. Two kinds:

**Wrong letter from a sibling language** - mostly the Nordic group, which shares most
letters but not all:

| Locale | Uses | Never uses |
|---|---|---|
| da-DK, nb-NO | æ ø å | ä ö |
| sv-SE | å ä ö | æ ø |
| fi-FI | ä ö (å rarely) | æ ø |
| de-DE | ä ö ü ß | æ ø å |
| es-ES, es-MX | á é í ó ú ñ ü | ã õ ç |
| pt-PT, pt-BR | ã õ ç á é í ó ú â ê ô à | ñ |
| fr-FR | é è ê à ç ù â î ô û ë ï | ñ ã õ |
| it-IT | à è é ì ò ù | ñ ç |
| pl-PL | ą ć ę ł ń ó ś ź ż | Nordic and German letters |

**Dropped or flattened diacritic** - any language: ø → o, å → a, ó → o, ł → l, ã → a,
é → e, ß → ss. Seen on this platform: "stålet" for "stjålet", "lejekøretoj" for
"lejekøretøj", "ändrer" for "ændrer", and Polish "przestoj" for "przestój". When the same
word appears twice in a string, check that both are spelled the same way.

### Wrong-domain vocabulary

Beyond Rule 1's list, reviewers specifically corrected banking and insurance terms used in
rental contexts. When a term has both a financial-services sense and a rental sense, the
rental sense is what customers expect.

---

## Formatting

- **No added bolding** - no `**` unless the source has it
- **Bullets** - `*`, matching source structure
- **Links** - `[Text](URL)` only; don't duplicate, nest or break
- **HTML** - preserve tags exactly, translate only the text between them
- **Variables** - `{variableName}` preserved exactly
- **Clean copy** - ready for direct CMS entry, no leading whitespace
- **No em dashes** - hyphen, or restructure, in every language

---

## Working in Google Sheets

**Use the Google Sheets connector when it's available.** It reads and writes cell values
directly, so nothing goes through the browser or the clipboard. Load its tools with
ToolSearch (`get_spreadsheet`, `get_values`, `update_values`; `insert_dimension` and
`update_formulas` when rows need adding).

1. **Find the tabs:** `get_spreadsheet` with `fields: ["sheets.properties.sheetId",
   "sheets.properties.title"]`.
2. **Read everything:** `get_values` on the whole tab, e.g. `'app-faqs'!A1:Q2000`. Check
   the returned row count against the sheet, then save what you read as the `before.xlsx`
   snapshot (openpyxl) before changing anything.
3. **Write narrowly:** `update_values` with the exact A1 range of the cells you're filling,
   e.g. `'app-faqs'!E12:R12` for one row's 14 targets. Multi-line answers go in as normal
   strings with `\n` line breaks. Never write a wider range than you mean to change, and
   never send a blank string into a cell you didn't intend to clear.
4. **Read back and check:** `get_values` on the same range, compare with what you sent,
   save it as `after.xlsx` and run the check script. Values can be reinterpreted on entry -
   watch for text starting with `=`, `+` or `-` and number-like strings.
5. **Formula columns** (e.g. a faqId column): copy the formula pattern from the row above
   with `update_formulas`. Don't write the displayed value as text.
6. **Tab names are exact** - `en-GB(fallback)`, not `en-GB`. Quote names with spaces or
   brackets in ranges.

**Fallback - no connector.** Google Sheets renders to canvas, so the grid can't be read
from the DOM. Read by exporting (Drive download as xlsx) and parsing; write by pasting:

- **Single-line cells**: `navigator.clipboard.writeText` with tab-separated values.
- **Multi-line cells**: TSV will not survive. Use a `ClipboardItem` with a `text/html` table
  where newlines are `<br>`, plus a `text/plain` fallback:

  ```javascript
  const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;')
                    .replace(/>/g,'&gt;').replace(/\n/g,'<br>');
  const html = '<table><tr>' + cells.map(c=>`<td>${esc(c)}</td>`).join('') + '</tr></table>';
  await navigator.clipboard.write([new ClipboardItem({
    'text/html': new Blob([html],{type:'text/html'}),
    'text/plain': new Blob([cells.join('\t')],{type:'text/plain'})})]);
  ```

- **Select the range first, paste second, in separate calls.** Batching selection and paste
  together has caused a 29-row block to land in one cell.
- **The name box needs grid focus.** `cmd+j` only works with a cell selected, not one in
  edit mode - two pastes failed silently this way. Safer: click the name box, `cmd+a`, type
  the range, confirm visually that it's in the box, Return as its own step, paste as its own
  step.
- If a cell accidentally enters edit mode, press **Escape**, not Enter (Enter commits the
  blank).
- To shift a run of cells one column, use the sheet's own cut and paste.
- **Confirm which file is open before pasting.** A clipboard prepared for one sheet will
  paste happily into another.

---

## The check script

Write this to a scratch file (e.g. `check_translations.py`, outside the folder holding the
sheet export) and run it with `python3 -I`. It reads an .xlsx whose header row contains the
locale codes and checks every target cell for:

- empty cells
- letters from another language
- long cells with no accented letters at all (stripped diacritics)
- placeholders, link targets and HTML tags that differ from the source
- possible truncation (under half the source length)
- em dashes
- insurance and wrong-domain terms from the Reject list

With `--before` it also checks for regressions against a snapshot: a translation that
changed when its source didn't, or more changed sentences than the source has.

```
python3 -I check_translations.py after.xlsx [--before before.xlsx] [--sheet TAB] [--key Key]
```

`--key` is the column that identifies a row (Key, Id, Number). Without it, rows are matched
by position, which breaks if rows were inserted. Every flag still needs a human look - a
reject term is fine when it really is the customer's own insurance, and a short UI label can
legitimately have no accents.

```python
#!/usr/bin/env python3
"""Mechanical checks for a translation sheet. Usage:
  python3 check_translations.py after.xlsx [--before before.xlsx] [--sheet TAB] [--key COL]
The sheet needs a header row with locale codes (en-US plus targets). --key names the
column that identifies a row (e.g. Key or Id); without it rows are matched by position."""
import argparse, re, sys
import openpyxl

LOCALES = ["en-US","en-GB","de-DE","es-ES","es-MX","fr-FR","pt-PT","pt-BR","it-IT",
           "da-DK","nl-NL","nb-NO","pl-PL","fi-FI","sv-SE"]
# letters that must never appear in a locale (lower case is enough, text is lowered)
FORBIDDEN = {
    "da-DK": "äöüõ", "nb-NO": "äöüõ", "sv-SE": "æøü", "fi-FI": "æøü",
    "de-DE": "æøå", "nl-NL": "æøå", "pl-PL": "æøåäöü", "fr-FR": "æøåäöñãõ",
    "es-ES": "æøåäöãõç", "es-MX": "æøåäöãõç", "it-IT": "æøåäöñãõç",
    "pt-PT": "æøåäöñ", "pt-BR": "æøåäöñ", "en-GB": "æøåäöñãõ",
}
# letters a long cell in this locale almost always contains at least one of
EXPECTED = {
    "de-DE": "äöüß", "fr-FR": "éèêàçùâîôû", "es-ES": "áéíóúñ¿¡", "es-MX": "áéíóúñ¿¡",
    "pt-PT": "ãõçáéíóúâêô", "pt-BR": "ãõçáéíóúâêô", "it-IT": "àèéìòù",
    "da-DK": "æøå", "nb-NO": "æøå", "sv-SE": "åäö", "fi-FI": "äö",
    "pl-PL": "ąćęłńóśźż",
}
REJECT = {  # insurance and wrong-domain stems, see Reject list
    "de-DE": ["versicherung","versichert","überschuss","zuzahlung","eigenanteil","gutschein"],
    "fr-FR": ["assurance","assuré","excédent","bon cadeau"],
    "es-ES": ["seguro","asegurado","deducible","excedente","cupón"],
    "es-MX": ["seguro","asegurado","franquicia","excedente"],
    "it-IT": ["assicurazion","assicurato","eccesso","buono regalo"],
    "pt-PT": ["seguro","segurado","excesso","dedutível","motorista","você"],
    "pt-BR": ["seguro","segurado","excesso","dedutível","aluguer","levantamento"],
    "en-GB": ["insurance","deductible","gift voucher"],
    "da-DK": ["forsikring","fradrag","gavekort"], "nb-NO": ["forsikring","fradrag","gavekort"],
    "nl-NL": ["verzekering","aftrekbaar","cadeaubon"], "pl-PL": ["ubezpieczeni","franczyza"],
    "fi-FI": ["vakuutu","lahjakortti"], "sv-SE": ["försäkring","avdrag","presentkort"],
}
PLACEHOLDER = re.compile(r"\{[^{}]+\}")
LINK = re.compile(r"\]\(([^)]+)\)")
TAG = re.compile(r"</?([a-zA-Z][a-zA-Z0-9]*)[^>]*?>")
SENT = re.compile(r"(?<=[.!?:])\s+|\n+")

def load(path, sheet):
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[sheet] if sheet else wb.worksheets[0]
    rows = [[("" if c is None else str(c)) for c in r] for r in ws.iter_rows(values_only=True)]
    head = rows[0]
    return head, rows[1:]

def cols(head):
    m = {}
    for i, h in enumerate(head):
        h2 = h.strip().replace("_", "-")
        for loc in LOCALES:
            if h2.lower() == loc.lower() or h2.lower().startswith(loc.lower()):
                m.setdefault(loc, i)
    return m

def sentences(t):
    return [s.strip() for s in SENT.split(t) if s.strip()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("after"); ap.add_argument("--before"); ap.add_argument("--sheet")
    ap.add_argument("--key")
    a = ap.parse_args()
    head, rows = load(a.after, a.sheet)
    cm = cols(head)
    if "en-US" not in cm:
        sys.exit("No en-US column found in header: %s" % head)
    keyi = head.index(a.key) if a.key else None
    issues = []
    def flag(r, loc, msg): issues.append(f"row {r} [{loc}] {msg}")
    for n, row in enumerate(rows, start=2):
        src = row[cm["en-US"]] if cm["en-US"] < len(row) else ""
        if not src.strip():
            continue
        for loc, i in cm.items():
            if loc == "en-US":
                continue
            t = row[i] if i < len(row) else ""
            if not t.strip():
                flag(n, loc, "empty"); continue
            low = t.lower()
            bad = sorted({ch for ch in low if ch in FORBIDDEN.get(loc, "")})
            if bad: flag(n, loc, "foreign letters: " + "".join(bad))
            if loc in EXPECTED and len(t) > 60 and not any(ch in low for ch in EXPECTED[loc]):
                flag(n, loc, "no accented letters at all - check for stripped diacritics")
            if sorted(PLACEHOLDER.findall(src)) != sorted(PLACEHOLDER.findall(t)):
                flag(n, loc, "placeholders differ from source")
            if sorted(LINK.findall(src)) != sorted(LINK.findall(t)):
                flag(n, loc, "link targets differ from source")
            if sorted(TAG.findall(src)) != sorted(TAG.findall(t)):
                flag(n, loc, "HTML tags differ from source")
            if len(src) > 20 and len(t) < 0.5 * len(src):
                flag(n, loc, f"possible truncation ({len(t)} vs {len(src)} chars)")
            if "—" in t: flag(n, loc, "em dash")
            for stem in REJECT.get(loc, []):
                if stem in low: flag(n, loc, f"reject term '{stem}' - check it isn't a rental product")
    if a.before:
        bhead, brows = load(a.before, a.sheet)
        bcm = cols(bhead)
        def index(rs, h):
            if keyi is None: return {i: r for i, r in enumerate(rs)}
            k = h.index(a.key); return {r[k]: r for r in rs if k < len(r)}
        old, new = index(brows, bhead), index(rows, head)
        for k, nr in new.items():
            orow = old.get(k)
            if orow is None: continue
            label = k if keyi is not None else f"row {k + 2}"
            osrc, nsrc = orow[bcm["en-US"]], nr[cm["en-US"]]
            src_changed = len(set(sentences(nsrc)) - set(sentences(osrc)))
            for loc, i in cm.items():
                if loc == "en-US" or loc not in bcm: continue
                ot, nt = orow[bcm[loc]], (nr[i] if i < len(nr) else "")
                if not ot.strip() or ot == nt: continue
                changed = [s for s in sentences(nt) if s not in sentences(ot)]
                if src_changed == 0:
                    issues.append(f"{label} [{loc}] REGRESSION: source unchanged but translation changed")
                elif len(changed) > src_changed:
                    issues.append(f"{label} [{loc}] {len(changed)} sentences changed for {src_changed} changed source sentence(s) - check these: " + " | ".join(changed))
    print("\n".join(issues) if issues else "No mechanical issues found.")
    print(f"\n{len(issues)} issue(s). Every flag still needs a human look before changing anything.")
    sys.exit(1 if issues else 0)

if __name__ == "__main__":
    main()
```

---

## Worked examples

**1 - FAQ answer (en → de-DE):** `Our Full Protection insurance covers your deductible (also known as an excess) if the car is damaged.`

- Wrong: `Unsere Vollschutz-Versicherung deckt Ihren Überschuss (auch bekannt als Selbstbeteiligung), wenn das Auto beschädigt wird.`
- Right: `Der Vollschutz deckt Ihre Selbstbeteiligung, wenn das Auto beschädigt wird.`

No "Versicherung" for a platform product (3); product name exact, no descriptor (2);
"Überschuss" is wrong-domain (1); the source's deductible/excess pairing collapses to the
one local term and grammar is re-checked (1, 4).

**2 - UI label (en → sv-SE):** `Manage your booking in My Account`

- Wrong: `Hantera Er bokning i Mitt Konto` - formal "Er" reads stiff
- Right: `Hantera din bokning i Mitt Konto` (9, 2)

**3 - HTML (en → fr-FR):** `<p>Pick-up from <strong>{stationName}</strong> requires a credit card deposit.</p>`

- Right: `<p>La prise en charge à <strong>{stationName}</strong> nécessite une caution par carte de crédit.</p>`

**4 - tooltip (en → es-ES), completeness:** `A deposit of 200 EUR applies and is held on your card until the vehicle is returned.`

- Wrong: `Se aplica un depósito de 200 EUR.` - the hold and its release condition are gone
- Right: the full sentence, including that the amount is held and when it is released

**5 - heading (en → es-ES / it-IT):** `Search & Results` → `Búsqueda y resultados` /
`Ricerca e risultati`, never `Búsqueda & Resultados` (10).

**6 - update (en → da-DK), change only what changed:** the English answer's last sentence
changed from "Contact us." to "Use the form."

- Old Danish: `Hvis bilen bliver stjålet, betaler du selvrisikoen. Kontakt os.`
- Wrong: `Hvis bilen bliver stålet, betaler du selvrisikoen. Brug formularen.` - the first
  sentence was retyped and lost a letter
- Right: `Hvis bilen bliver stjålet, betaler du selvrisikoen. Brug formularen.` - first
  sentence copied untouched, only the changed sentence translated (Step 2b)

---

## Verification checklist - 16 checks

1. **Terminology** - every rejected term, in all forms
2. **Product names** - only correct localized names; unlisted products kept in English and flagged
3. **Currency** - right currency and number format, no mixed symbols
4. **Links** - count matches source, URLs unchanged, none nested or bare
5. **Redundancy** - no "X (or X)", dangling parentheses, orphaned slashes
6. **Cross-language** - nothing leaked in
7. **Consistency** - one term per concept throughout
8. **Grammar** - articles, adjectives, pronouns, verbs agree after all changes
9. **HTML tags** - all preserved with matching open/close
10. **Formatting** - bold and bullet counts match source, no leading whitespace
11. **Completeness** - row count matches, no empty cells, no English in a non-English column
12. **Truncation** - nothing stops mid-sentence or on a dangling conjunction; read any cell
    under half the source length
13. **Column alignment** - no row one column off; last locale column not unexpectedly empty
14. **Conjunction and punctuation** - no stray "&" in headings, no em dashes
15. **Spelling and letters** - no letters from another language, no dropped diacritics, the
    same word spelled the same way everywhere
16. **No regressions** - when updating existing strings, text whose source did not change
    is identical to before (check script with `--before`)

---

## Glossary

Authoritative term mappings for all 14 locales. Use exactly these terms - no synonyms.
Terms marked ⚠ VERIFY are best-judgment and not yet confirmed by a native speaker or the
live localized site: use them, but flag them in output.

### Core rental terms (1)

| Locale | Deductible | Pickup | Return | Deposit | Rental counter |
|---|---|---|---|---|---|
| de-DE | Selbstbeteiligung | Abholung | Rückgabe | Kaution | Mietschalter |
| fr-FR | franchise | prise en charge | restitution | caution | comptoir de location |
| es-ES | franquicia | recogida | devolución | depósito | mostrador de alquiler |
| es-MX | deducible | recogida | devolución | depósito | mostrador de renta |
| it-IT | franchigia | ritiro | restituzione | deposito cauzionale | banco di noleggio |
| pt-PT | franquia | levantamento | devolução | caução | balcão de aluguer |
| pt-BR | franquia | retirada | devolução | depósito | balcão de locação |
| en-GB | excess | pick-up | return / drop-off | deposit | rental counter |
| da-DK | selvrisiko | afhentning | aflevering | depositum | udlejningsskranke |
| nl-NL | eigen risico | ophalen | inleveren | borg | verhuurbalie |
| nb-NO | egenandel | henting | innlevering | depositum | utleieskranke |
| pl-PL | udział własny | odbiór | zwrot | kaucja | stanowisko wynajmu |
| fi-FI | omavastuu | nouto | palautus | vakuusmaksu | vuokrauspiste |
| sv-SE | självrisk | upphämtning | återlämning | deposition | uthyrningsdisk |

### Core rental terms (2)

| Locale | Driver | Main driver | Additional driver | Driver's license | Rental agreement |
|---|---|---|---|---|---|
| de-DE | Fahrer | Hauptfahrer | Zusatzfahrer | Führerschein | Mietvertrag |
| fr-FR | conducteur | conducteur principal | conducteur additionnel | permis de conduire | contrat de location |
| es-ES | conductor | conductor principal | conductor adicional | permiso de conducir | contrato de alquiler |
| es-MX | conductor | conductor principal | conductor adicional | licencia de conducir | contrato de renta |
| it-IT | conducente | conducente principale | conducente aggiuntivo | patente di guida | contratto di noleggio |
| pt-PT | condutor | condutor principal | condutor adicional | carta de condução | contrato de aluguer |
| pt-BR | motorista | motorista principal | motorista adicional | carteira de habilitação | contrato de locação |
| en-GB | driver | main driver | additional driver | driving licence | rental agreement |
| da-DK | fører | hovedfører | ekstra fører | kørekort | lejeaftale |
| nl-NL | bestuurder | hoofdbestuurder | extra bestuurder | rijbewijs | huurovereenkomst |
| nb-NO | fører | hovedfører | ekstra fører | førerkort | leieavtale |
| pl-PL | kierowca | główny kierowca | dodatkowy kierowca | prawo jazdy | umowa wynajmu |
| fi-FI | kuljettaja | pääkuljettaja | lisäkuljettaja | ajokortti | vuokrasopimus |
| sv-SE | förare | huvudförare | extra förare | körkort | hyresavtal |

### Core rental terms (3)

Where two terms are shown, the first is the default; the second is acceptable where the
first would be repetitive. Pick one per document and stay consistent (Rule 8).

| Locale | Rental company | Fuel policy | Booking confirmation | "Rental" (the word) | Commission (partner content) |
|---|---|---|---|---|---|
| de-DE | Vermieter / Autovermietung | Tankregelung | Buchungsbestätigung | Miete / Mietwagen | Provision |
| fr-FR | loueur / société de location | politique de carburant | confirmation de réservation | location | commission |
| es-ES | empresa de alquiler / proveedor | política de combustible | confirmación de reserva | alquiler | comisión |
| es-MX | empresa de renta / arrendadora | política de combustible | confirmación de reservación | renta | comisión |
| it-IT | società di noleggio / fornitore | politica del carburante | conferma di prenotazione | noleggio | commissione |
| pt-PT | empresa de aluguer | política de combustível | confirmação de reserva | aluguer | comissão |
| pt-BR | locadora | política de combustível | confirmação de reserva | locação | comissão |
| en-GB | rental company / provider | fuel policy | booking confirmation | rental / hire | commission |
| da-DK | biludlejningsfirma / udlejer | brændstofpolitik | bookingbekræftelse | leje / biludlejning | provision |
| nl-NL | verhuurbedrijf / verhuurder | brandstofbeleid | boekingsbevestiging | huur / autoverhuur | commissie |
| nb-NO | utleiefirma / utleier | drivstoffregler | bookingbekreftelse | leie / bilutleie | provisjon |
| pl-PL | wypożyczalnia | polityka paliwowa | potwierdzenie rezerwacji | wynajem | prowizja |
| fi-FI | vuokraamo | polttoainekäytäntö | varausvahvistus | vuokraus | provisio |
| sv-SE | uthyrningsföretag / uthyrare | bränslepolicy | bokningsbekräftelse | hyra / biluthyrning | provision |

"Voucher" is an accepted loan word in every locale - keep it as "voucher". Never use a
gift-voucher or coupon word for it (see the Reject list).

### Products and protection

Product names are fixed: no paraphrasing, no "insurance" prefix. See Rule 2 for products
that have no localized name yet.

| Locale | Full Protection | Flexible Cancellation Protection ⚠ VERIFY | My Account | Theft protection | Protection (generic) |
|---|---|---|---|---|---|
| de-DE | Vollschutz | Flexibler Stornoschutz | Mein Konto | Diebstahlschutz | Schutz |
| fr-FR | Protection complète | Protection annulation flexible | Mon compte | protection contre le vol | protection |
| es-ES | Protección Total | Protección de Cancelación Flexible | Mi Cuenta | protección contra robo | protección |
| es-MX | Protección Total | Protección de Cancelación Flexible | Mi Cuenta | protección contra robo | protección |
| it-IT | Protezione Totale | Protezione Cancellazione Flessibile | Il mio account | protezione furto | protezione |
| pt-PT | Proteção Total | Proteção de Cancelamento Flexível | Minha Conta | proteção contra roubo | proteção |
| pt-BR | Proteção Total | Proteção de Cancelamento Flexível | Minha Conta | proteção contra roubo | proteção |
| en-GB | Full Protection | Flexible Cancellation Protection | My Account | theft protection | protection |
| da-DK | Fuld Beskyttelse | Fleksibel Afbestillingsbeskyttelse | Min Konto | tyveribeskyttelse | beskyttelse |
| nl-NL | Volledige Bescherming | Flexibele Annuleringsbescherming | Mijn Account | diefstalbescherming | bescherming |
| nb-NO | Full Beskyttelse | Fleksibel Avbestillingsbeskyttelse | Min Konto | tyveribeskyttelse | beskyttelse |
| pl-PL | Pełna Ochrona | Elastyczna Ochrona Anulowania | Moje Konto | ochrona przed kradzieżą | ochrona |
| fi-FI | Täysi Suoja | Joustava Peruutussuoja | Oma Tili | varkaussuoja | suoja |
| sv-SE | Fullt Skydd | Flexibelt Avbokningsskydd | Mitt Konto | stöldskydd | skydd |

| Locale | CDW first-mention gloss ⚠ VERIFY | Roadside assistance - generic service, not a product name ⚠ VERIFY |
|---|---|---|
| de-DE | Haftungsreduzierung bei Schäden (CDW) | Pannenhilfe |
| fr-FR | protection contre les dommages par collision (CDW) | assistance routière |
| es-ES | cobertura por daños de colisión (CDW) | asistencia en carretera |
| es-MX | cobertura por daños de colisión (CDW) | asistencia vial |
| it-IT | copertura danni da collisione (CDW) | assistenza stradale |
| pt-PT | cobertura de danos por colisão (CDW) | assistência em viagem |
| pt-BR | proteção contra danos de colisão (CDW) | assistência rodoviária |
| en-GB | Collision Damage Waiver (CDW) | roadside assistance |
| da-DK | dækning af kollisionsskader (CDW) | vejhjælp |
| nl-NL | dekking voor aanrijdingsschade (CDW) | pechhulp |
| nb-NO | dekning for kollisjonsskader (CDW) | veihjelp |
| pl-PL | ochrona od szkód kolizyjnych (CDW) | pomoc drogowa |
| fi-FI | kolarisuoja (CDW) | tiepalvelu |
| sv-SE | vagnskadeskydd (CDW) | vägassistans |

Keep "CDW" in every language. Pair it with the gloss on first mention in a document, then
"CDW" alone.

### Reject list

Never use these for rental products or rental concepts. The insurance words are correct
only for the customer's own policy, credit card benefits or a third-party insurer (Rule 3).

| Locale | Insurance words | Wrong deductible | Wrong voucher (retail) | Wrong driver |
|---|---|---|---|---|
| de-DE | Versicherung, Versicherungen, versichert | Franchise, Überschuss, Zuzahlung, Eigenanteil | Gutschein, Coupon | Pilot, Lenker |
| fr-FR | assurance(s), assuré, assurance collision, assurance location | excédent, surplus | bon cadeau, coupon | pilote, chauffeur |
| es-ES | seguro(s), asegurado | deducible, exceso, excedente | vale, cupón | piloto, chofer |
| es-MX | seguro(s), asegurado | franquicia, exceso, excedente | vale, cupón | piloto, chofer |
| it-IT | assicurazione, assicurazioni, assicurato | eccesso, franchigia assicurativa | buono, coupon | pilota, autista |
| pt-PT | seguro(s), segurado | excesso, dedutível, franchise | vale, cupão | piloto, motorista |
| pt-BR | seguro(s), segurado | excesso, dedutível, franchise | vale-presente, cupom | piloto, condutor |
| en-GB | insurance (for rental products) | deductible | gift voucher, coupon | pilot |
| da-DK | forsikring, forsikringer | fradrag, overskud | gavekort | pilot |
| nl-NL | verzekering, verzekeringen | franchise, aftrekbaar | cadeaubon, tegoedbon | piloot, chauffeur |
| nb-NO | forsikring, forsikringer | fradrag, overskudd | gavekort | pilot |
| pl-PL | ubezpieczenie, ubezpieczenia | franczyza, odliczenie | kupon, bon podarunkowy | pilot |
| fi-FI | vakuutus, vakuutuksen, vakuutuksia | vähennys, ylimääräinen | lahjakortti, kuponki | pilotti |
| sv-SE | försäkring, försäkringar | avdrag, överskott | presentkort, kupong | pilot |

### es-ES vs es-MX

| Concept | es-ES | es-MX |
|---|---|---|
| Rental | alquiler | renta |
| Deductible | franquicia | deducible |
| Driver's license | permiso de conducir | licencia de conducir |
| Car (informal) | coche | auto |
| Booking | reserva | reservación |
| Rental counter | mostrador de alquiler | mostrador de renta |
| Rental agreement | contrato de alquiler | contrato de renta |
| ID document | documento de identidad oficial | identificación oficial |

### pt-PT vs pt-BR

| Concept | pt-PT | pt-BR |
|---|---|---|
| Rental | aluguer | locação |
| Pickup | levantamento | retirada |
| Driver | condutor | motorista |
| Driver's license | carta de condução | carteira de habilitação |
| Rental counter | balcão de aluguer | balcão de locação |
| Settings | definições | configurações |
| Contact (verb) | contacte | entre em contato |
| Deposit | caução | depósito |

### Currency and number formatting

Authoritative for Rule 5.

| Market | Currency | 2000 | Decimal | Notes |
|---|---|---|---|---|
| de-DE | € | 2.000 € | 1.234,56 € | Symbol after, dot thousands, comma decimals |
| fr-FR | € | 2 000 € | 1 234,56 € | Symbol after, space thousands, comma decimals |
| es-ES | € | 2.000 € | 1.234,56 € | Symbol after |
| es-MX | $ (MXN) | $2,000 MXN | $1,234.56 MXN | Add "MXN" where it could be read as USD |
| it-IT | € | 2.000 € | 1.234,56 € | Symbol after |
| pt-PT | € | 2.000 € | 1.234,56 € | Symbol after |
| pt-BR | R$ | R$ 2.000 | R$ 1.234,56 | Symbol before with space |
| en-GB | £ | £2,000 | £1,234.56 | £ by default; €/$ only when the source amount is explicitly in that currency |
| en-US | $ | $2,000 | $1,234.56 | USD only |
| da-DK | kr. (DKK) | 2.000 kr. | 1.234,56 kr. | Not euro |
| nl-NL | € | € 2.000 | € 1.234,56 | Symbol before with space |
| nb-NO | kr (NOK) | 2 000 kr | 1 234,56 kr | Not euro |
| pl-PL | zł (PLN) | 2000 zł | 1234,56 zł | Not euro |
| fi-FI | € | 2 000 € | 1 234,56 € | Space thousands |
| sv-SE | kr (SEK) | 2 000 kr | 1 234,56 kr | Not euro |

Illustrative amounts become a natural round figure of similar magnitude ("$2,000" →
"2.000 €" for de-DE, "20 000 kr" for sv-SE) - no exchange-rate math. Contractual or exact
amounts keep their original currency and value, flagged for the user.