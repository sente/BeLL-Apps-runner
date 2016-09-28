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


    levels = dict(dicts['LevelArray'])

    for d in docs:
        if d.get('language') ==  'Arabic':

            old_levels = d.get('Level',[])
            new_levels = [levels.get(s,'null') for s in old_levels]

#            print '{}\t{}'.format(len(old_levels),'\t'.join(old_levels))
#            print '{}\t{}'.format(len(new_levels),'\t'.join(new_levels))
#            print '\n\n'
            if new_levels != old_levels:
                d['Level'] = new_levels
                db.save(d)
                print "saving {}, replacing {} with {}".format(d.get('_id'),old_levels,new_levels)
            else:
                print "NOT saving {}, {} == {}".format(d.get('_id'),old_levels,new_levels)

