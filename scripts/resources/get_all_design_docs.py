import os
import json
import pycouchdb
import requests


dbs = json.loads(requests.get('http://corebell.ole.org:5995/_all_dbs').content)

server = pycouchdb.Server('http://corebell:oleoleole@corebell.ole.org:5995')

dic = {}

for d in dbs:
    db = server.database(d)
    try:
        desdoc = db.get("_design/bell")
        dic[d] = desdoc
    except:
        pass

dic['resources'].items()
dic['resources'].keys()
dic['resources']['views']
dic['resources']['views'].keys()
[v.get('map') for v in dic['resources']['views'].values()]
[v.get('map') for v in dic['resources']['views'].values()][0]


for db,val in dic.items():
#    print val
    viewdata = val.get('views')
    print viewdata.keys()
    for k,v in viewdata.items():
        filepath = "data/views/{}/{}.js".format(db,k)
        print filepath
        if not os.path.isdir(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        with open(filepath ,'w') as o:
            o.write(v.get('map'))
            print 'saved {}'.format(filepath)

##        code = view_val.get('map')
#        code =json.loads(view_val)
#        if code:
#

#    for view_name,view_data in val.get('views').items():
#        print db,view_name,view_data.keys()

#for view_name, view_val in dic['resources']['views'].items():
#    print view_name
#    print view_val.get('map')
