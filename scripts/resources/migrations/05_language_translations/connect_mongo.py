import pycouchdb
import requests
import time
import sys
import pprint

reload(sys)
sys.setdefaultencoding('utf-8')

# example output https://gist.github.com/sente/e5dd3d20fd0919722d83a9520a6f9984


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

parser.add_option("--list-databases",
                dest="list_databases",
                default=False,
                action="store_true",
                help="List the databases and exit"
                )

parser.add_option("--ignore-design-docs",
                dest="ignore_design_docs",
                default=False,
                action="store_true",
                help="ignore the design docs"
                )


(options, args) = parser.parse_args()

def list_databases():
    print '{}/_all_dbs'.format(options.host)
    resp = requests.get('{}/_all_dbs'.format(options.host))
    dbs = resp.json()
    for db in dbs:
        print db

if __name__ == '__main__':

    if options.list_databases:
        list_databases()
        sys.exit(0)


    server = pycouchdb.Server(options.host)
    db = server.database(options.database)


    records = db.all()
    if options.ignore_design_docs:
        records = [record for record in records if not record.get('id','').startswith('_design/')]


#    if option.list_databases:
#        server.databsae


    #docs = list(db.all())

