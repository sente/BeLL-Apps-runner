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
    lang_info = json.load(open('ds.json'))


    server = pycouchdb.Server(options.host)
    db = server.database(options.database)

    #records = list(db.all())
    #docs = [r.get('doc') for r in records]


    for stuff in lang_info:
        if stuff.get("id").startswith('_design'):
            continue
        if stuff['final_language'] != stuff['original_language']:
            print "fix\t\t{}".format(stuff['id'])
            doc = db.get(stuff['id'])
            if doc.get('language') != stuff['final_language']:
                doc['language'] = stuff['final_language']
                db.save(doc)
                print 'UPDATING\t\t{}\t\t+++++'.format(stuff['id'])

        else:
            print "skip\t\t{}".format(stuff['id'])

    sys.exit(0)
