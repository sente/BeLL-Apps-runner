import tablib
import json
import re
import time

from optparse import OptionParser
import pycouchdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


usage = "usage: %prog [options] arg"
parser = OptionParser(usage)

parser.add_option("--id", "--_id",
                dest="id",
                default="",
                action="store",
                help="the resource to change"
                )

parser.add_option("-H", "--host",
                dest="host",
                default="",
                action="store",
                help="The couchdb server/host"
                )

parser.add_option("--database",
                dest="database",
                default="",
                action="store",
                help="the database on the host"
                )



(options, args) = parser.parse_args()



if __name__ == '__main__':
    server = pycouchdb.Server(options.host)
    db = server.database(options.database)

    doc = db.get(options.id)
    doc['language'] = 'English'
    print doc['language']
    db.save(doc)

#docs = [d.get('doc') for d in db.all()]
#docs = [resources.get('doc') for d in db.all()]
#docs = [resources.get('doc') for d in resources.all()]
#docs
#resources
#docs = [d.get('doc') for d in resources.all()]
#len(docs)
#docs[3]
#dhash = {d.get('_id'),d for d in docs}
#for d in docs:
#    id = d.get('_id')
#    if id:
#        dhash[id] = d
#dhash = {}
#for d in docs:
#    id = d.get('_id')
#    if id:
#        dhash[id] = d
#dhash['00d8a12ca2cb9d39e58d80218a26672c']
#records = [r for r in resources.all()]
#[r for r in records if r.get('doc',{}).get('_id') == '00d8a12ca2cb9d39e58d80218a26672c']
#%history
