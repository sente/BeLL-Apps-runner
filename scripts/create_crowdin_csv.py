from __future__ import print_function
import os
import six
import glob
import sys
import tablib
import json

try:
    bell_dir = os.environ.get('BELL_APPS_DIRECTORY', '/Users/stu/code/ole/BeLL-Apps/')
    lang_dir = os.path.join(os.path.join(bell_dir, 'init_docs/languages'))
except:
    sys.stderr.write("BELL_APPS_DIRECTORY not set")




english_file = lang_dir + "/English.txt"
j = json.load(open(english_file))
headers = [k for k in j.keys() if isinstance(j[k],unicode)]
headers = ['file'] + headers


ds = tablib.Dataset(headers=headers)

input_files = glob.glob(lang_dir + '/*.txt')

for ff in input_files:
    with open(ff) as ifile:
         j = json.loads(ifile.read())
         j['file'] = os.path.basename(ff)
         ds.append([j[h] for h in headers])

transposed = ds.transpose()

open('crowdin_table.tsv','wb').write(ds.tsv)
open('crowdin_transposed.tsv','wb').write(transposed.tsv)
