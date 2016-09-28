import pycouchdb
import requests
import time
import sys
import cPickle as pickle
import pprint
from optparse import OptionParser
import pycouchdb

reload(sys)
sys.setdefaultencoding('utf-8')


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from connect_mongo import *

if __name__ == '__main__':


    dicts = pickle.load(open('lookups/dicts.pkl'))

    server = pycouchdb.Server(options.host)
    db = server.database(options.database)


    records = db.all()
    if options.ignore_design_docs:
        records = [record for record in records if not record.get('id','').startswith('_design/')]


    docs = [r.get('doc') for r in records]


    subjects = dict(dicts['SubjectList'])

    for d in docs:
        if d.get('language') ==  'Arabic':


            old_subjects = d.get('subject',[])
            new_subjects = [subjects.get(s,'null') for s in old_subjects]

#            print '{}\t{}'.format(len(old_subjects),'\t'.join(old_subjects))
#            print '{}\t{}'.format(len(new_subjects),'\t'.join(new_subjects))
#            print '\n\n'
            if new_subjects != old_subjects:
                d['subject'] = new_subjects
                db.save(d)
                print "saving {}, replacing {} with {}".format(d.get('_id'),old_subjects,new_subjects)
            else:
                print "NOT saving {}, {} == {}".format(d.get('_id'),old_subjects,new_subjects)

