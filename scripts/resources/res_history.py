!kls
!ll
!ls
!ls -lrt
thedocs2 = json.load(open('corebell.resources.json'))
thedocs[0]
thedocs2[0]
unique_fields(thedoc2,'language')
unique_fields(thedoc2s,'language')
unique_fields(thedocs2,'language')
unique_fields(thedocs,'language')
stra = json.dumps(thedocs)
strb = json.dumps(thedocs2)
len(stra)
len(strb)
stra == strb
len(stra.split("\n"))
len(stra)
type(strb)
type(stra)
stra[0:20]
strb[0:20]
strb[0:-20]
strb[-20:0]
strb[-20:-1]
stra[-20:-1]
stra[-2000:-1] == strb[-2000:-1]
"adsf" == "adsf"
strb[-20:-1]
stra[-20:-1]
stra[-20:-1] == strb[:-20:-1]
str(stra[-20:-1] )== str(strb[:-20:-1])
print str(strb[:-20:-1])
print str(stra[:-20:-1])
print str(strb[:-20:-1])
x = str(strb[:-20:-1])
y = str(stra[:-20:-1])
x
y
x == y
stra == strb
stra[0:100] == strb[0:100]
stra[0:1000] == strb[0:1000]
stra[0:10000] == strb[0:10000]
stra[1000:1200] == strb[1000:1200]
for x,y in zip(stra,strb):
    if x != y:
        print x, y
for i,(x,y) in enumerate(zip(stra,strb)):
    if x != y:
        print x, y
for i,(x,y) in enumerate(zip(stra,strb)):
    if x != y:
        print i, x, y
stra[21829]
strb[21829]
for i,(x,y) in enumerate(zip(stra,strb)):
    if x != y:
        print i, x, y
        break
stra[1400:1415]
strb[1400:1415]
json.dump?
foobar = json.dumps(thedocs,sort_keys=True)
thedocs2 = json.load(open('corebell.resources.json'))
foobar2 = json.dumps(thedocs2,sort_keys=True)
len(foobar)
len(foobar2)
foobar == foobar2
thedocs[4].keys()
thedocs[4]['Tag']
headers = ['Level','_id','subject','language']
headers = ['_id','_id','subject','language']
import tablib
%history -f res_history.py
