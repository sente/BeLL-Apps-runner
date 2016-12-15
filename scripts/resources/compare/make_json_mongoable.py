import json
import sys
fname =sys.argv[1]

text = json.load(open(fname))
    
[r for r in text if r.get('doc',{}).get('_attachments')]
good = [r for r in text if r.get('doc',{}).get('_attachments')]
for g in good:
    del g['doc']['_attachments']
    
oname = fname.replace(".json",'.clean.json')

open(oname, 'w').write(json.dumps(good))
