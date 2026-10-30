"""Parse the cached PDF into corpus.json (deterministic, no network)."""
import hashlib, json, pathlib, re
import pypdf
H = pathlib.Path(__file__).parent
PDF = H / '.cache' / 'constitution-en.pdf'
URL = 'https://www.burmalibrary.org/sites/burmalibrary.org/files/obl/docs5/Myanmar_Constitution-2008-en.pdf'
raw = PDF.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
text = '\n'.join(p.extract_text() for p in pypdf.PdfReader(str(PDF)).pages)
text = text.replace(' ', ' ').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
text = text.replace('–', '-').replace('—', '-')
lines = [re.sub(r'\s+', ' ', l).strip() for l in text.split('\n')]
lines = [l for l in lines if l and not re.fullmatch(r'\d{1,3}', l)]  # blanks and page numbers
start = [i for i, l in enumerate(lines) if l == 'Preamble'][-1]
lines = lines[start + 1:]

SCH = {'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5}
chunks = []  # (key, label, [lines])
cur = ('preamble', 'Preamble', [])
expect = 1
for l in lines:
    ms = re.fullmatch(r'SCHEDULE (ONE|TWO|THREE|FOUR|FIVE)', l)
    if ms:
        chunks.append(cur)
        n = SCH[ms.group(1)]
        cur = (f'schedule-{n}', f'Schedule {n}', [])
        continue
    if cur[0].startswith('schedule'):
        cur[2].append(l)
        continue
    m = re.match(r'(\d+)\. ?(.*)', l)
    if m and int(m.group(1)) == expect and expect <= 457:
        prev = cur[2]
        while prev and not re.search(r'[.;:)"\']$', prev[-1]):
            prev.pop()  # heading lines (no closing punctuation) belong to the layout, not the section
        chunks.append(cur)
        cur = (f'section-{expect:03d}', f'Section {expect}', [l])
        expect += 1
        continue
    cur[2].append(l)
chunks.append(cur)
assert expect == 458, expect


def paras(ls):
    out = []
    for l in ls:
        if re.fullmatch(r'Chapter [IVX]+', l):
            continue
        newp = not out or re.match(r'^(\(\w{1,4}\) |- |\d+\. )', l) or (re.search(r'[.:;]$', out[-1]) and re.match(r'^[A-Z0-9(]', l))
        if newp:
            out.append(l)
        elif out[-1].endswith('-'):
            out[-1] += l
        else:
            out[-1] += ' ' + l
    return out


units = {}
for key, label, ls in chunks:
    ps = paras(ls)
    if key.startswith('section-'):
        ps[0] = re.sub(r'^\d+\. ?', '', ps[0])
        ps = [p for p in ps if p]
    kind = 'schedule' if key.startswith('sch') else ('preamble' if key == 'preamble' else 'section')
    units[key] = {'label': label, 'kind': kind, 'text': f'# {label}\n' + '\n'.join(ps) + '\n'}
credits = {k: ['publisher-print-2008'] for k in units}
corpus = {
  'country': {'code': 'MM', 'name': 'Myanmar', 'slug': 'myanmar', 'lang': 'en', 'tz': 'Asia/Yangon', 'future_branch': 'future',
    'publisher': {'name': 'Printing and Publishing Enterprise, Ministry of Information (Myanmar)', 'email': 'pandp@mininfo.gov.mm.invalid'},
    'default_in_force_rule': {'text': 'Constitution of the Republic of the Union of Myanmar (2008), section 441: it comes into operation from the day the first session of the Pyidaungsu Hluttaw is convened (31 January 2011).', 'source': URL},
    'licence_note': 'State legal text of Myanmar, printed by the Printing and Publishing Enterprise, Ministry of Information, September 2008; read from the copy held by the Online Burma/Myanmar Library. No licence was stated for the text.'},
  'sources': [{'name': 'Constitution of the Republic of the Union of Myanmar (2008), official English version, Ministry of Information printing (copy held by Online Burma/Myanmar Library)',
     'url': URL, 'retrieved': '2026-10-29', 'licence': 'no licence stated; official state text', 'notes': 'Text-layer PDF, 213 pages, 457 sections and five schedules. sha256 ' + sha}],
  'laws': {'publisher-print-2008': {'label': 'Constitution as printed September 2008', 'title': 'Constitution of the Republic of the Union of Myanmar (2008): oldest version available', 'kind': 'publisher', 'enacted': '2008-05-29', 'published': '2008-09-01', 'url': URL, 'temporary_until': None, 'restores': None, 'note': None}},
  'acts': [{'slug': 'constitution', 'short': 'Constitution', 'title': 'Constitution of the Republic of the Union of Myanmar (2008)', 'url': URL, 'first_law': None, 'earlier_laws': [],
     'versions': [{'from': '2011-01-31', 'source_url': URL, 'sha256': sha, 'units': units, 'credits': credits,
       'note': 'Adopted by referendum on 29 May 2008; the printed English version of September 2008, as the oldest version available. Not amended in this record.'}]}],
  'applies': [],
  'decisions': ['English is built: this is the official English version printed by the Ministry of Information. The Myanmar text prevails (section 452).',
    'The only version available is the September 2008 printing. Its from date is 2011-01-31, the day the first session of the Pyidaungsu Hluttaw convened, which is when section 441 brought the Constitution into operation; that date is a historical fact and is not in the printed text.',
    'Amendments, the 2021 suspension and later proclamations are not recorded: no official consolidated text was found. The text is the 2008 printing only.',
    'Page numbers and chapter headings are dropped; wrapped lines are joined; sub-clauses (a), (b) and list items each start a line; curly quotes and dashes are made plain.',
    'The state flag and seal drawings in sections 437 and 438 are not text and are not included.'],
  'ai_use': ['none. Claude Code wrote the parser; no model produced or altered any legal text.']}
(H / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', encoding='utf8', newline='\n')
print(len(units), 'units')
