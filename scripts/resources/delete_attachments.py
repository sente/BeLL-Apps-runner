import pycouchdb
import time
import sys
server = pycouchdb.Server('http://new.qa:oleoleole@new.qa.ole.org:5985/')
db = server.database('stunopdfjs3')
resources = list(db.all())
docs = [r.get('doc') for r in resources if r['doc'].get("title")]


doc = [d for d in docs if d['_id'] == 'bb7a908e3ca2cdad2681234e28019717'][0]


attachments = [att for att in doc['_attachments'] if att.endswith('.jpg')]


if not attachments:
    print "there are no attachments to delete"
    sys.exit(0)

print "all attachments"

for att in doc['_attachments'].keys():
    if att.endswith(".jpg"):
        print "db.delete_attachment({},{})".format(doc.get("_id"),att)


print "\n\n\n"
print "attempting to delete the one of them"
print "\n\n\n"

if attachments:
    print "deleting %s" % attachments[0]
    db.delete_attachment(doc, attachments[0])
    sys.exit(0)



#att = d['_attachments'].keys()[0]
#
#print 'deleting att
#
#db.delete_attachment(d,d['_attachments'][0])
