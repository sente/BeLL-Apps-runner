import tablib
import pycouchdb
import sys
import collections


host_name = sys.argv[1]
database_name = sys.argv[2]
server = pycouchdb.Server(host_name)
database = server.database(database_name)


records = []
for i,rec in enumerate(database.all()):
    rows = []
    print i
    records.append(rec.keys())
#    for a,b in rec['doc']['_attachments'].items():
#        rows.append(b)




#ds = tablib.Dataset(headers=b.keys())


#d = server.database(database)
#counts = collections.defaultdict(int)
#for i,rec in enumerate(d.all()):
#    ty = rec.get('doc',{}).get('openWith','')
#    counts[ty]+=1
#counts
#dict(counts)
#rec
#rec.keys()
#rec['doc']
#rec['doc'].keys()
#for k,v in rec['doc'].items():
#    print k,type(v)
#for k,v in rec['doc'].items():
#    print type(v),k
#rec['doc']['Tag']
#rec['doc']['_attachments']
#len(rec['doc']['_attachments'])
#for a in rec['doc']['_attachments']:
#    print a
#for a in rec['doc']['_attachments'].items():
#    print a
#for a in rec['doc']['_attachments'].items():
#    pprint.pprint(a)
#import pprint
#for a in rec['doc']['_attachments'].items():
#    pprint.pprint(a)
#for a in rec['doc']['_attachments'].items():
#    a.values()['content_type']
#for a in rec['doc']['_attachments'].items():
#    dict(a.values())
#for a,b in rec['doc']['_attachments'].items():
#    print b['content_type']
#for a,b in rec['doc']['_attachments'].items():
#    if 'pdf' in b['content_type']:
#        print b
#for a,b in rec['doc']['_attachments'].items():
#    if 'pdf' in b['content_type']:
#        print a,b
#b
