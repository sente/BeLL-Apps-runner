import pycouchdb
import sys
host = sys.argv[1]
database = sys.argv[2]
server = pycouchdb.Server(host)
records = server.database(database).all()
for record in records:
    print record.get('doc')
