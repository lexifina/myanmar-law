import pymupdf, re
def rows(pdf):
    d = pymupdf.open(str(pdf)); out = []
    for pno, p in enumerate(d):
        ls = []
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines', []):
                sp = [s for s in l['spans'] if s['text'].strip()]
                if not sp: continue
                ls.append((l['bbox'][1], l['bbox'][0], l['bbox'][2], ''.join(s['text'] for s in l['spans']).strip(), sp[0]['font'], sp[0]['size']))
        ls.sort()
        grp = []
        for y, x0, x1, t, f, sz in ls:
            if grp and abs(grp[-1]['y'] - y) < 3:
                grp[-1]['parts'].append((x0, x1, t, f)); continue
            grp.append({'y': y, 'parts': [(x0, x1, t, f)], 'page': pno})
        for g in grp:
            g['parts'].sort()
            g['x0'] = g['parts'][0][0]; g['x1'] = max(p[1] for p in g['parts'])
            g['font'] = g['parts'][0][3]
            g['t'] = ' '.join(p[2] for p in g['parts'])
            out.append(g)
    return out
