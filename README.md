# Myanmar: law history in git


The law of Myanmar as a git history: one file per section (and per schedule, chapter, Part or Division heading), one commit per version on the day it took effect, and the act that made each change as the commit's author. `git blame` names the source behind every line; `git log` lists every change to a section; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Myanmar's national law, which global-law reads at `myanmar/national/acts/`.

**What is in it now:** four acts, each in one version: the Constitution of 2008 (preamble, sections 1 to 457 and five schedules), the Penal Code (1860) as amended to 25 March 2019, the Contract Act (1872) and the Myanmar Companies Law (2017), 1,765 provisions in all. [`REPRODUCE.md`](REPRODUCE.md) lists every act with its versions; [`data/laws.csv`](data/laws.csv) lists the law or publisher each version is credited to.

Each act is a folder with one file per provision (`constitution/section-001.md` is section 1 of the Constitution; `penal-code/section-302.md` is section 302 of the Penal Code, punishment for murder). Each folder's `README.md` lists its provisions and their changes.

The text is in English, as the sources print it; the Constitution is the official English version printed by the Ministry of Information in September 2008. Section 452 bases its interpretation on the Myanmar text, which is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to section 1 of the Constitution | `git log -p --word-diff -- constitution/section-001.md` |
| Which source wrote each line of section 1? | `git blame constitution/section-001.md` |
| Every version of the Constitution, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution ':!*/README.md'` |
| Section 1 as in force on 1 January 2026 | `python tools/on.py 2026-01-01 constitution section-001` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Myanmar law](https://global-law.lexifina.com/v1/try_claude?country=myanmar)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=myanmar)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=citizen&jurisdictions=myanmar)**: a search of Myanmar law for "citizen", returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add myanmar/national/acts
python3 tools/law.py show 2026-01-01 myanmar/national/acts/constitution/section-001.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Asia/Yangon, on the day the version took effect, and carries it in its `In-force:` trailer:

- the Constitution, 31 January 2011, the day the first session of the Pyidaungsu Hluttaw convened, which section 441 makes its day of operation (it was adopted by referendum on 29 May 2008);
- the Companies Law, 1 August 2018, its commencement under President Notification 48/2018 (it was signed on 6 December 2017);
- the Penal Code and the Contract Act, whose texts give no such day: the Penal Code from its last amendment shown, 25 March 2019 (Law No. 10/2019), and the Contract Act from the day its PDF was made, 4 June 2018 (the Act came into force on 1 September 1872).

The Companies Law is credited to the law that enacted it (`Pyidaungsu Hluttaw Law No. 29/2017`). The other three acts are each the "oldest version available", credited to the publisher of the text, not to a law.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect, and on the day before, and compares it file by file with the corpus it was built from; it also checks that every commit's trailers parse, that `main` has no merge commits and that no commit date goes backwards or lies in the future.
- The text is read from each PDF's text layer (no OCR) by a deterministic parser; `tools/build.py` writes the history from the corpus, and the same corpus always gives the same commit hashes.
- [`REPRODUCE.md`](REPRODUCE.md) gives the corpus and builder hashes and every decision made by hand; its Checks section reads "Not yet run for this build".

## What it does not show

- **Later history.** No official consolidated text with amendments was found, so each act has one version. Later amendments, the suspension of parts of the Constitution in February 2021 and later proclamations are not here.
- **Most of the law.** Only these four acts: no other laws, no regulations or notifications, and no case law.
- **The Myanmar text**, which section 452 makes the basis of the Constitution's interpretation.
- **Texts from their publisher.** Only the Companies Law is read from its publisher; the other three are copies held by libraries (see Sources).
- **Drawings.** The State Flag and State Seal in sections 437 and 438 are not included.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Online Burma/Myanmar Library](https://www.burmalibrary.org/en/constitution-of-the-republic-of-the-union-of-myanmar-2008-english) | Constitution (2008), official English version, Ministry of Information printing | no | A copy held by the library |
| [UNODC SHERLOC](https://sherloc.unodc.org/cld/uploads/res/document/mmr/1861/myanmar_penal_code_html/The_Penal_Code_incorporating_amendments_to_25_March_2019.pdf) | Penal Code, Myanmar Law Information System text amended to 25 March 2019 | no | A copy of the official text; marginal notes follow the section number |
| [Myanmar Law Library](https://www.myanmar-law-library.org/IMG/pdf/the_contract_act.pdf) | Contract Act, Burma Code text | no | Sections 76 to 123 and 239 to 266 shown as repealed |
| [Directorate of Investment and Company Administration](https://www.myco.dica.gov.mm/documentation/mm/MCL.en-US.pdf) | Myanmar Companies Law, official English text | no | The Law as signed; later amendments are not recorded |

## Licence

See [`LICENSE`](LICENSE). The four texts are state legal texts, and no licence is stated for any of them; Lexifina's arrangement, tables, commit messages and tools are under the Creative Commons Attribution 4.0 International licence.

No AI model wrote, translated or corrected legal text; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
