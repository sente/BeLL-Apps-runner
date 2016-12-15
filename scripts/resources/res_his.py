import sys
import json
import pycouchdb
import tablib

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://corebell.ole.org:5995'
server = pycouchdb.Server(url)
resources = server.database('resources')
docs = list(resources.all())
thedocs = [d.get('doc') for d in docs]
res = []
unique_levels = {}

unique_subjects = {}
def listify(x):
    if not isinstance(x,list):
        return [x]
    else:
        return x

for i, td in enumerate(thedocs):
    print i
    id = td.get('_id')
    s = td.get('subject',[])
    s = listify(s)
    l = td.get('Level',[])
    l = listify(l)

    for _ in l:
        unique_levels[_] = 1

    for _ in s:
        unique_subjects[_] = 1

    title = td.get('title')

    d = dict()
    d['subject'] = ' | '.join(s)
    d['Level']= ' | '.join(l)
    #d['title'] = title
    d['id'] = id
    res.append(d)

ds = tablib.Dataset(headers=['id','Level','subject'])

ds.dict=res

open('ds.xlsx','w').write(ds.xlsx)
open('ds.xls','w').write(ds.xls)
open('ds.html','w').write(ds.html)
open('ds.csv','w').write(ds.csv)

