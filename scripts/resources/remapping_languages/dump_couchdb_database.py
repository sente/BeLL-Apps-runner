from optparse import OptionParser
import sys
import json
import pycouchdb
import tablib
import collections
import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

usage = "usage: %prog [options] arg"
parser = OptionParser(usage)

parser.add_option("-d", "--docs",
                dest="docs",
                default=False,
                action="store_true",
                help="return a list of docs"
                )

parser.add_option("-H", "--host",
                dest="host",
                default="",
                action="store",
                help="The couchdb server/host"
                )

parser.add_option("-D", "--database",
                dest="db",
                default="",
                action="store",
                help="the database on the host"
                )



(options, args) = parser.parse_args()


def dump_database(server_host,database,docs):
        server = pycouchdb.Server(server_host)
        db = server.database(database)
        data = list(db.all())
        if docs:
            data = [d.get('doc') for d in db.all()]
        print json.dumps(data)


if __name__ == '__main__':
    db = options.db
    host = options.host
    docs = options.docs

    dump_database(host,db,docs)




