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



if __name__ == '__main__':

    thedocs = json.load(open('resources-2016-09-06.json'))

    ids = [t.get('_id') for t in thedocs]
    rows = [t.get('Level') for t in thedocs]

    norms = [normalize(r) for r in rows]

    for _id, before, after in zip(ids, rows, norms):
        if before != after:
            print _id
            print before
            print after
            print "\n"


