import requests

servers = [a.strip() for a in open('servers.txt').readlines()]
hosts = ['%s' % s for s in servers if 'ole.org' in s ]

dfile = open('design_docs.txt','w')

for h in hosts:
    for db in requests.get('%s/_all_dbs' %h).json():
        dfile.write( '%s/%s/_design/bell\n' % (h, db))
