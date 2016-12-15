import sys
import json
import pycouchdb
import tablib
import collections
import pprint
from itertools import chain
import tablib

reload(sys)
sys.setdefaultencoding('utf-8')
fname = sys.argv[1]

data = json.load(open(fname,'r'))

#keys = collections.defaultdict(int)
#for row in data
#    for key in row:
#        keys[key]+=1

columns = ["_id", "kind", "_rev", "articleDate", "author", "Tag", "uploadDate", "openWith", "title", "subject", "language", "Level", "averageRating"]

ds = tablib.Dataset(headers=columns)
for row in data:
    row = row.get("doc",{})
    the_row = []
    for c in columns:
        the_row.append(row.get(c))
    ds.append(the_row)

def json_to_dicts(json_str):
    objects = json.loads(json_str)

    def to_single_dict(lst):
        result = {}
        for d in lst:
            for k in d.keys():
                result[k] = d[k]
        return result;

    return [dict(to_keyvalue_pairs(obj)) for obj in objects]

def to_keyvalue_pairs(source, ancestors=[], key_delimeter='_'):
    def is_sequence(arg):
        return (not hasattr(arg, "strip") and hasattr(arg, "__getitem__") or hasattr(arg, "__iter__"))

    def is_dict(arg):
        return hasattr(arg, "keys")

    if is_dict(source):
        result = [to_keyvalue_pairs(source[key], ancestors + [key]) for key in source.keys()]
        return list(chain.from_iterable(result))
    elif is_sequence(source):
        result = [to_keyvalue_pairs(item, ancestors + [str(index)]) for (index, item) in enumerate(source)]
        return list(chain.from_iterable(result))
    else:
        return [(key_delimeter.join(ancestors), source)]




open(fname + '.csv','w').write(ds.csv)
