import os
import pycouchdb

server = sys.argv[1]
database = sys.argv[2]
attachment_name = sys.argv[3]

server = pycouchdb.Server(server)
nopdfjs = server.database(database)

keys = list(nopdfjs.all())

for k in keys:
    doc = k.get('doc')
    print doc
    att = doc.get('_attachments',None)
    if att:
        for ka,va in att.items():
            print doc.get('_id'),ka
    print '\n'

docs = [k.get('doc') for k in keys]
docs = [d for d in docs if d.get('title')]

for d in docs:
    dirname = './resources/%s' % d.get("title")
    print dirname
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    for att in d.get('_attachments'):
        fname = dirname + '/%s' % att
        print 'saving %s' % fname
        open(dirname + '/%s' % att,'w').write(nopdfjs.get_attachment(d,att))



