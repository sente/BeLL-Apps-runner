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

    records = list(db.all())
    docs = [r.get('doc') for r in records]
    docs_with_bad_levels = [d for d in docs if isinstance(d.get('Level'),unicode)]

    for doc in docs_with_bad_levels:
        doc['Level'] = [doc.get('Level')]
        print "saving {}".format(doc.get('_id'))
        db.save(doc)

"""
ipython -i 00_fix_non_array_levels.py -- --host=http://corebell.ole.org:5995/ --database=resources_2016-09-06

saving 04a159e6e1f1bde124447fd51ffbe490
saving 0ba64ecf8ff5fd2e524c5825ef00cb2d
saving 2987a7b883997fc20f777f5e26a485e2
saving 54d87c9421261516aaa2cf4ed87a5359
saving 54d87c9421261516aaa2cf4ed87e8082
saving 54d87c9421261516aaa2cf4ed88755fc
saving 54d87c9421261516aaa2cf4ed88e2950
saving 54d87c9421261516aaa2cf4ed897f430
saving 54d87c9421261516aaa2cf4ed8c00eb0
saving 59f510604bb1fd7983968d8c0111ea5f
saving 8a9f8d7d9e4bb337c78a088b5c630d0d
saving 9d171c1c212d3e539cb1bdaa6001b196
saving 9d171c1c212d3e539cb1bdaa6016b0b7
saving a0cf9b7b6981022e27a9ef6bb212baf1
saving b5dda003c94f8095f9efadc9cfc73c13
saving b985804772c7acbde0c031f34f031444
saving cbd4a1877bb79eda6fc5f6659b119f36
saving cbd4a1877bb79eda6fc5f6659b17e266
saving cbd4a1877bb79eda6fc5f6659b2b7518
saving cbd4a1877bb79eda6fc5f6659b593536
saving cbd4a1877bb79eda6fc5f6659b85c6f1
saving dc363e83b6dec454877464028524d508
"""
