import tablib
import json
import re
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def normalize(row):
    if not row:
        return []
    elif isinstance(row, list):
        return row
    elif isinstance(row, unicode):
        parts = re.split('\W+', row, flags=re.UNICODE)
        parts = [p.strip() for p in parts if p.strip()]
        return parts
    else:
        return [row]


def test_rows():
    for row in rows:
        if not row:
            print 'null: {}'.format(row)
        if isinstance(row, list):
            print 'list: {}'.format(row)
            time.sleep(.3)
        elif isinstance(row, float):
            print 'deci: {}'.format(row)
            time.sleep(3)
        else:
            print 'norm: {}'.format(row)

    #    return normalize(ow)


def load_lookup_table(filepath):
    d={}
    filetext= open(filepath).read()
    lines = [line.strip() for line in filetext.split('\n')]
    for line in lines:
        try:
            a,b = line.split('\t')
            d[a]=b
        except:
            pass

#    for k in d:
#        if d[k] == 'none':
#            del d[k]

    return d


thedocs = json.load(open('resources.json'))

ids = [t.get('_id') for t in thedocs]
rows = [t.get('language') for t in thedocs]


norms = [normalize(r) for r in rows]



ds = tablib.Dataset(headers=['id','original_language','normalized_language','final_language'])

mapping = load_lookup_table('lookup.txt')
    

for a,b,c in zip(ids,norms,rows):
    print a
    #print a,c,','.join(b),','.join([str(mapping[str(x)]) for x in b])
    _id = str(a),
    original_language = c
    normalized_language = ','.join(b)
    mapped = [mapping[str(x)] for x in b]
    mapped = [m for m in mapped if m != 'none']

    final_language = ','.join(mapped)
#    final_language = ','.join([(mapping[str(x)]) for x in b])

    ds.append([_id, original_language,normalized_language,final_language])


open('ds.xlsx','w').write(ds.xlsx)


