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

def load_lookup_table(filepath):
    d={}
    filetext= open(filepath).read()
    lines = [line.strip() for line in filetext.split('\n')]
    for line in lines:
        try:
            a,b = line.split('\t')
            d[a]=b
        except:
            pass
    return d



if __name__ == '__main__':

    server = pycouchdb.Server(options.host)
    db = server.database(options.database)

    records = list(db.all())
    docs = [r.get('doc') for r in records]
    bad_mediums = [d for d in docs if d.get('Medium') and d.get('Medium') == 'Graphic/Pictures']

    for d in bad_mediums:
        new_medium = 'Graphics/Pictures'
        print "{}\t{}\t{}".format(d.get('_id'), d['Medium'], new_medium)
        d['Medium'] = new_medium
        db.save(d)
