# How this repository was made (Myanmar)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Constitution of the Republic of the Union of Myanmar (2008), official English version, Ministry of Information printing (copy held by Online Burma/Myanmar Library) | <https://www.burmalibrary.org/sites/burmalibrary.org/files/obl/docs5/Myanmar_Constitution-2008-en.pdf> | 2026-10-29 | no licence stated; official state text |
| The Penal Code (India Act XLV, 1860), Myanmar Law Information System text amended to 25 March 2019, copy held by UNODC SHERLOC | <https://sherloc.unodc.org/cld/uploads/res/document/mmr/1861/myanmar_penal_code_html/The_Penal_Code_incorporating_amendments_to_25_March_2019.pdf> | 2026-10-30 | no licence stated; official state text (Myanmar Law Information System) |
| The Contract Act (India Act IX, 1872), copy held by the Myanmar Law Library (myanmar-law-library.org) | <https://www.myanmar-law-library.org/IMG/pdf/the_contract_act.pdf> | 2026-10-30 | no licence stated; state legal text, copy held by the Myanmar Law Library |
| Myanmar Companies Law (Pyidaungsu Hluttaw Law No. 29, 2017), English text, Directorate of Investment and Company Administration (DICA, MyCo) | <https://www.myco.dica.gov.mm/documentation/mm/MCL.en-US.pdf> | 2026-10-30 | no licence stated; official state text published by DICA |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of the Union of Myanmar (2008) | 1 | 2011-01-31 to 2011-01-31 |
| `penal-code` | The Penal Code (India Act XLV, 1860), as applied in Myanmar | 1 | 2019-03-25 to 2019-03-25 |
| `contract-act` | The Contract Act (India Act IX, 1872), as applied in Myanmar | 1 | 2018-06-04 to 2018-06-04 |
| `companies-law` | The Myanmar Companies Law (Pyidaungsu Hluttaw Law No. 29, 2017) | 1 | 2018-08-01 to 2018-08-01 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 4 laws in the record.
- 5 tags.

## Dates

Each commit is dated at noon (Asia/Yangon) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution of the Republic of the Union of Myanmar (2008), section 441: it comes into operation from the day the first session of the Pyidaungsu Hluttaw is convened (31 January 2011). https://www.burmalibrary.org/sites/burmalibrary.org/files/obl/docs5/Myanmar_Constitution-2008-en.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `62e3a32b02405c532bf28230935211b06b92b95f37720bd1e6232025e60323cc` (1534653 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English is built: this is the official English version printed by the Ministry of Information. The Myanmar text prevails (section 452).
- The only version available is the September 2008 printing. Its from date is 2011-01-31, the day the first session of the Pyidaungsu Hluttaw convened, which is when section 441 brought the Constitution into operation; that date is a historical fact and is not in the printed text.
- Amendments, the 2021 suspension and later proclamations are not recorded: no official consolidated text was found. The text is the 2008 printing only.
- Page numbers and chapter headings are dropped; wrapped lines are joined; sub-clauses (a), (b) and list items each start a line; curly quotes and dashes are made plain.
- The state flag and seal drawings in sections 437 and 438 are not text and are not included.
- Penal Code: the only version available is the Myanmar Law Information System text amended to 25 March 2019; its from date is that last amendment date, and it is credited to the publisher as the oldest version available, not to Law No. 10/2019.
- Penal Code: marginal notes (printed in the left margin) are written after the section number as its heading; "<Amendment ...>" tags and the closing footnote are dropped; wrapped lines are joined and paragraphs are split by line length and (a), Explanation and Illustration markers.
- Contract Act: the Myanmar Law Library copy is the only text that could be read; its from date is the date its PDF file was made, 2018-06-04, credited to the publisher as the oldest version available. Group sub-headings between sections are dropped. Repealed ranges (sections 76 to 123 and 239 to 266) are single files holding "* * * *".
- Companies Law: the DICA English text is the Law as signed on 6 December 2017 (Law No. 29/2017). Its from date, 1 August 2018, is the commencement date fixed under section 1(b) by President Notification 48/2018; that date is a historical fact and is not in the text. Later amendments are not recorded.
- Companies Law: Part and Division headings are files; the italic sub-headings inside Divisions and the contents pages are dropped; each (a), (i), (A) item starts a line.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none. Claude Code wrote the parsers; no model produced or altered any legal text.
