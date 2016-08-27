import pycouchdb
import sys
import os
server = sys.argv[1]
attachment_name = sys.argv[2]
attachment_part = sys.argv[3]

server = pycouchdb.Server(server)
resources = server.database('resources')

bible = resources.get(attachment_name)
part = resources.get_attachment(resources.get(attachment_name), attachment_part)

if not os.path.isdir('./attachments/%s' % attachment_name):
    os.mkdir('./attachments/%s' % attachment_name)

open('./attachments/%s/%s' % (attachment_name,attachment_part),'w').write(part)

#open('page_1211.jpg','wb').write(page_1211)
