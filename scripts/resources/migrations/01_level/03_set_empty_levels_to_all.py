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
    docs_with_bad_levels = [d for d in docs if not d.get('Level')]
    docs_with_bad_levels = [ d for d in docs_with_bad_levels if '_design' not in d.get("_id")]
    
#    unique_levels = []
#    for d in docs:
#        for level in d.get('Level',[]):
#            unique_levels.append(level)

    unique_levels = [ "Early Education",
            "Lower Primary",
            "Upper Primary",
            "Lower Secondary",
            "Upper Secondary",
            "Undergraduate",
            "Graduate",
            "Professional" ]


    for i,doc in enumerate(docs_with_bad_levels):
        doc['Level'] = unique_levels
        print '{} - updating level for {}'.format(i, doc.get('_id'))
        db.save(doc)





"""
stu@redmac ~/code/OLE/BeLL-Apps-runner/scripts/resources/migrations/01_level (master) $ ipython -i 03_set_empty_levels_to_all.py -- --host=http://corebell.ole.org:5995/ --database=resources_2016-09-060 - updating level for CapineraEncyclopediaOfEntomology2espringer2008
1 - updating level for Encyclopaediabri23chisrich_201303
2 - updating level for Encyclopaediabri25chisrich_201303
3 - updating level for Encyclopaediabri26chisrich_201303
4 - updating level for Encyclopaediabri28chisrich_201303
5 - updating level for MikeDixonKennedy.......encyclopediaOfGrecoRomanMythologybyHouseOfBooks

"""
