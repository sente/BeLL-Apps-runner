python ../dump_couchdb_database.py --host http://corebell.ole.org:5995 -D resourcefrequency > resourcefrequency.json ; echo $?
python ../dump_couchdb_database.py --host http://corebell.ole.org:5995 -D resources > resources.json ; echo $?
python ../dump_couchdb_database.py --host http://corebell.ole.org:5995 -D resources_2016-08-23 > resources_2016-08-23.json ; echo $?
python ../dump_couchdb_database.py --host http://corebell.ole.org:5995 -D resources_2016-09-06 > resources_2016-09-06.json ; echo $?
python ../dump_couchdb_database.py --host http://corebell.ole.org:5995 -D resources_moved > resources_moved.json ; echo $?
python ../dump_couchdb_database.py --host http://corebell.ole.org:5995 -D resources_original > resources_original.json ; echo $?
python ../dump_couchdb_database.py --host http://corebell.ole.org:5995 -D resources_original_safe > resources_original_safe.json ; echo $?
python ../dump_couchdb_database.py --host http://corebell.ole.org:5995 -D sturesources > sturesources.json ; echo $?
