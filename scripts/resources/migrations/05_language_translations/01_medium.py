import pycouchdb
import requests
import time
import sys
import cPickle as pickle
import pprint

reload(sys)
sys.setdefaultencoding('utf-8')


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




from optparse import OptionParser
import pycouchdb

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


    mediums = dict(dicts['mediaList'])

    for d in docs:
        if d.get('language') ==  'Arabic':
            key = d.get('Medium')
            if key in mediums:
                print "updating database for {}\t{} changing to {} ".format(d.get("_id"),key,mediums[key])
                d['Medium'] = mediums[key]
                db.save(d)
            else:
                print "skipping id {} key not found {}".format(d.get("_id"), d.get("Medium"))
