import sys
import json
import pycouchdb
import tablib
import collections
import pprint

class HashableList(list):
	'A hashable wrapper around the standard list.'

	def __init__(self, l):
		self.list = tuple(l)
	def __str__(self):
		return str(self.list)
	def __hash__(self):
		return hash(self.list)
	def __len__(self):
		return len(self.list)
	def __getitem__(self, i):
		return self.list[i]
	def __iter__(self):
		return iter(self.list)



def uniqify(field,field_type):
    fields = [t.get(field,[]) for t in thedocs]
    if field_type == 'list':
        fields = [listify(x) for x in fields]
        return dict(collections.Counter([','.join(t.get('Level',[])) for t in thedocs]).most_common())




reload(sys)
sys.setdefaultencoding('utf-8')




if sys.argv[1] == "dump":
    print "dumping"
    url = 'http://corebell.ole.org:5995'
    server = pycouchdb.Server(url)
    resources = server.database('resources')
    docs = list(resources.all())
    thedocs = [d.get('doc') for d in docs]

    open('resources.json','w').write(json.dumps(thedocs))
    sys.exit(0)


if sys.argv[1] == "load":
    resource_file = sys.argv[2]
    thedocs = json.load(open(resource_file, 'r'))




fields = ['_id','Level','subject','language','title']
types = ['str','list','str','str','str']


ds = tablib.Dataset(headers=fields)

def listify(x):
    if isinstance(x, list):
        return x
    else:
        return [x]


def collect_fields(thedocs, fields, types):
    res = []
    for td in thedocs:
        d = {}
        for f in fields:
            d[f] = "|".join(listify(td.get(f,'')))
        res.append(d)
    return res


def unique_fields(thedocs, attr):
    myset = {}
    for td in thedocs:
        vals = listify(td.get(attr))
        for v in vals:
            myset[v] = 1
    return myset


foo = collect_fields(thedocs,fields,types)


ds.dict=foo
open('emily.xls','w').write(ds.xls)
#http://corebell.ole.org:5995/_utils/document.html?resources/002df5029d490ff332ae5f939adf1ef5

