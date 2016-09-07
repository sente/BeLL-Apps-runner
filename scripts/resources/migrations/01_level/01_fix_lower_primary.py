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
    print doc['Level']
    doc['Level'] = ['Lower Primary']
    print doc['Level']
    db.save(doc)

