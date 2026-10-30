# Myanmar: law history in git

The Constitution of the Republic of the Union of Myanmar (2008) and core statutes as a git repository: one file per section and schedule, and the printing it comes from as the commit's author. `git log` and `git blame` name the source of every line; the tools in `tools/` show the text in force on a date.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `mm/`.

**Language:** English. The Constitution is the official English version printed by the Printing and Publishing Enterprise, Ministry of Information, in September 2008. Section 452 of the Constitution says the Myanmar-language text is the one used for interpretation.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the Republic of the Union of Myanmar (2008): preamble, sections 1 to 457 and Schedules 1 to 5 | 1 | The oldest version available: the September 2008 printing, dated from 31 January 2011, the day section 441 brought it into operation (the first session of the Pyidaungsu Hluttaw) |
| `penal-code/` | The Penal Code (India Act XLV, 1860), as applied in Myanmar: sections 1 to 511 with their A-lettered sections, and chapter headings | 1 | The oldest version available: the Myanmar Law Information System text incorporating amendments to 25 March 2019 (Law No. 10/2019), dated from that last amendment |
| `contract-act/` | The Contract Act (India Act IX, 1872), as applied in Myanmar: preamble, sections 1 to 238 and chapter headings (sections 76 to 123 and 239 to 266 are repealed) | 1 | The oldest version available: the Myanmar Law Library copy of the Burma Code text, dated from 4 June 2018, the day that PDF was made |
| `companies-law/` | The Myanmar Companies Law (Pyidaungsu Hluttaw Law No. 29, 2017): preamble, sections 1 to 476, with Parts and Divisions | 1 | The Law as signed on 6 December 2017, dated from 1 August 2018, when it commenced under President Notification 48/2018 |

## What it does not show

- **No later history.** No official consolidated text with amendments was found online, so there is one version. Amendments, the suspension of parts of the Constitution in February 2021 and later proclamations are not in this record.
- **Not the adoption date.** The Constitution was adopted by referendum on 29 May 2008; the first commit is dated from the day it came into operation.
- **Flag and seal.** Sections 437 and 438 show the State Flag and State Seal as drawings; the drawings are not text and are not included.
- **Chapter headings and page numbers** of the Constitution are not separate files. In the statutes, chapters are files named `chapter-NN.md`.

## Dates

Each commit is dated at noon, Asia/Yangon, on the day the change took effect, shown in the `In-force:` trailer. The one date used here comes from section 441.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The text is read from the text layer of the printed PDF (no OCR). A deterministic parser turns it into `corpus.json`, and the shared builder writes the repository with `git fast-import`. `REPRODUCE.md` records the data hash, the decisions and the checks. No AI model wrote or changed legal text.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Constitution of the Republic of the Union of Myanmar (2008), English](https://www.burmalibrary.org/en/constitution-of-the-republic-of-the-union-of-myanmar-2008-english) | Official text, copy held by the Online Burma/Myanmar Library | no | Used. The library's page says: "The official English version." |
| [Penal Code, text incorporating amendments to 25 March 2019](https://sherloc.unodc.org/cld/uploads/res/document/mmr/1861/myanmar_penal_code_html/The_Penal_Code_incorporating_amendments_to_25_March_2019.pdf) | Myanmar Law Information System text (MLIS, watermarked on each page), copy held by UNODC SHERLOC | no | Used. Marginal notes are shown after the section number |
| [The Contract Act, 1872](https://www.myanmar-law-library.org/IMG/pdf/the_contract_act.pdf) | State legal text (Burma Code), copy held by the Myanmar Law Library | no | Used. |
| [Myanmar Companies Law, English](https://www.myco.dica.gov.mm/documentation/mm/MCL.en-US.pdf) | Official text published by the Directorate of Investment and Company Administration (DICA) | no | Used. Amendments after 2017 are not recorded |
| [Myanmar Law Information System](https://www.mlis.gov.mm) | Official legislation | partly | – |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The law text is the Constitution of Myanmar, a state legal text, printed by the Printing and Publishing Enterprise, Ministry of Information (September 2008), the Penal Code as held by the Myanmar Law Information System, the Contract Act as held by the Myanmar Law Library, and the Companies Law as published by DICA. No licence is stated for any of them. The arrangement, commit messages and tools are by Lexifina, under `LICENSE`.

This repository is not legal advice and not an official publication.
