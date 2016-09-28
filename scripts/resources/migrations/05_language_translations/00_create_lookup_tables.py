import tablib

from collections import OrderedDict
import cPickle as pickle
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


files = ['/Users/stu/code/OLE/BeLL-Apps/init_docs/languages/English.txt',
         '/Users/stu/code/OLE/BeLL-Apps/init_docs/languages/Arabic.txt']

keys = 'SubjectList','LevelArray','mediaList'

jsons = []
for f in files:
    jsons.append(json.load(open(f)))

dicts = {}
for k in keys:
    dicts[k] = OrderedDict()
    pairs = [j[k] for j in jsons]
    for a,b in zip(pairs[0],pairs[1]):
        dicts[k][a]=b

odir = 'lookups'

for key in keys:
    ds = tablib.Dataset(headers=['english','arabic'])
    with open('{}/{}.tsv'.format(odir,key),'w') as ofile:
        print 'creating {}/{}'.format(odir,key)
        for row,val in dicts[key].items():
            ofile.write('{}\t{}\n'.format(row,val))
            ds.append([row,val])
        print "wrote csv/xls"
        open('{}/{}.csv'.format(odir,key),'w').write(ds.csv)
        open('{}/{}.xls'.format(odir,key),'w').write(ds.xls)


pickle.dump(dicts,open('lookups/dicts.pkl','w'))
