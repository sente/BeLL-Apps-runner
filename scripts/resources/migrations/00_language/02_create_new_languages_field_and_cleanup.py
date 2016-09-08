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




    # first pass
    server = pycouchdb.Server(options.host)
    db = server.database(options.database)
    records = list(db.all())
    docs = [r.get('doc') for r in records]
    docs = [d for d in docs if not d.get('_id').startswith('_design/')]

    print "addding 'languages' field"
    for i,d in enumerate(docs):
        if 'languages' not in d:
            d['languages'] = d.get('language','').split(',')
            print '{}/{} saving {}\t{} --> {}'.format(i+1,len(docs),d.get('_id'), d.get('language'), d.get('languages'))
            db.save(d)

    print "cleaning 'language' field"

    # second pass
    server = pycouchdb.Server(options.host)
    db = server.database(options.database)
    records = list(db.all())
    docs = [r.get('doc') for r in records]
    docs = [d for d in docs if not d.get('_id').startswith('_design/')]

    for i,d in enumerate(docs):
        langs = d.get('languages')
        if len(langs) > 1:
            if 'English' in langs:
                print '{}/{} updating {}\t{} --> {}'.format(i+1,len(docs),d.get('_id'), d.get('language'), 'English')
                d['language'] = 'English'
            db.save(d)

