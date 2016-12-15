import tablib
import collections
import json
j = json.load(open('results.json'))
docs = [j[1] for j in j]

keycounts = collections.defaultdict(int)

for d in docs:
    keys = sorted(d['doc'].keys())
    for key in keys:
        keycounts[key]+=1

headers = [a[0] for a in collections.Counter(keycounts).most_common()]
keycounts = collections.defaultdict(int)


ds = tablib.Dataset(headers=headers)
rows = []

for d in docs:
    data = dict.fromkeys(headers)
    for key,val in d['doc'].items():
        data[key] = str(type(val)).split("'")[1]
    rows.append(data)



ds.dict=rows


print 'writing..'
open('out/ds.csv','w').write(ds.csv)
open('out/ds.xls','w').write(ds.xls)
open('out/ds.xlsx','w').write(ds.xlsx)
open('out/ds.html','w').write(ds.html)
