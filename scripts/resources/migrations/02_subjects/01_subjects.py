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




(options, args) = parser.parse_args()

if __name__ == '__main__':
    server = pycouchdb.Server(options.host)
    db = server.database(options.database)

    records = list(db.all())
    docs = [r.get('doc') for r in records]
    docs_with_array_subjects = [d for d in docs if d.get('subject') and isinstance(d.get('subject'),list)]
    docs_with_scalar_subjects = [d for d in docs if d.get('subject') and isinstance(d.get('subject'),unicode)]

    mapping = load_lookup_table('lookup.txt')


    for i,doc in enumerate(docs_with_scalar_subjects):
        doc.get("_id") 
        doc['subject']
        new_subjects = [mapping[doc['subject']]]
        print "{}\t{}\t{}".format(doc.get('_id'),doc['subject'],new_subjects)
        db.save(doc)


    print '\n' * 5
    for i,doc in enumerate(docs_with_array_subjects):
        if len(doc['subject']) > 0:
            new_subjects = []
            for subject in doc['subject']:
                new_subjects.append(mapping[subject])


            print "{}\t{}\t{}".format(doc.get('_id'),doc['subject'],new_subjects)
            doc['subject'] = new_subjects
            db.save(doc)

    sys.exit(0)
