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
    docs_with_bad_levels = [d for d in docs if d.get('Level')==['All']]

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
ipython -i 02_replace_all_level_with_array.py -- --host=http://corebell.ole.org:5995/ --database=resources_2016-09-06

0 - updating level for 04a159e6e1f1bde124447fd51ffbe490
1 - updating level for 1c60a9f0525786ef0c93e5d7a169561f
2 - updating level for 2987a7b883997fc20f777f5e26a485e2
3 - updating level for 2d6d824f80ba316a0a24c7dad4d3509c
4 - updating level for 324f53a8b1ee2b174ff6e72d3703684e
5 - updating level for 3d14022200d84378ee183431499648d0
6 - updating level for 41d459f2e2815471670b369086192782
7 - updating level for 455450ec4a20477585a44fff7e753887
8 - updating level for 481a3337cfef0ce9eedcccf0b760bfd9
9 - updating level for 54d87c9421261516aaa2cf4ed87a5359
10 - updating level for 54d87c9421261516aaa2cf4ed87e8082
11 - updating level for 54d87c9421261516aaa2cf4ed88755fc
12 - updating level for 54d87c9421261516aaa2cf4ed88e2950
13 - updating level for 54d87c9421261516aaa2cf4ed897f430
14 - updating level for 54d87c9421261516aaa2cf4ed8c00eb0
15 - updating level for 59f510604bb1fd7983968d8c0111ea5f
16 - updating level for 59f510604bb1fd7983968d8c01febf33
17 - updating level for 8273f84adb73d4025f56895f599b96e5
18 - updating level for 8a92474cf7f3e4bf02131393ce3ae7e8
19 - updating level for 8a92474cf7f3e4bf02131393ce4b6117
20 - updating level for 8a9f8d7d9e4bb337c78a088b5c630d0d
21 - updating level for 978d1f23989f09441300ff89cc4a75bd
22 - updating level for 978d1f23989f09441300ff89cc51854d
23 - updating level for 978d1f23989f09441300ff89cc55a71d
24 - updating level for 99bde820238987db56cab45495b3a9c7
25 - updating level for 9d171c1c212d3e539cb1bdaa6001b196
26 - updating level for 9d171c1c212d3e539cb1bdaa6016b0b7
27 - updating level for 9d9ebcf05949ad25e8aa0b5c602bf055
28 - updating level for ActionsFeelingsAndThingsVocabulary
29 - updating level for Alphabetofobject00nymciala_201303
30 - updating level for Aristotlespoliti00arisuoft_201306
31 - updating level for AutobiographyOfMarkTwain
32 - updating level for BeTheSentence
33 - updating level for BlackWomenLeadersMaeJemison
34 - updating level for ComparingProverbs
35 - updating level for DiggingInTheDictionaryWorksheet
36 - updating level for Earlyeuropeanhis01webs_201303
37 - updating level for Encyclopaediabrit06chisrich_201303
38 - updating level for GirlRisingInNepalAGirlAWriterAPowerfulStory.
39 - updating level for HealthPromot.Int.2009Tang6877
40 - updating level for MarketingStrategiesForFarmersAndRanchers
41 - updating level for MenstrualCycleCoachingQuestions
42 - updating level for MontessoriElementaryMaterials
43 - updating level for MotivationThroughMusic
44 - updating level for MrSmithGoesToWashington1939480x360
45 - updating level for OnTheSoul
46 - updating level for PEPFARADecadeOfSavingLives
47 - updating level for PracticalGrammarAndComposition
48 - updating level for RulesForUltimateFrisbee
49 - updating level for SchSkills4health03
50 - updating level for Standards12Worksheets
51 - updating level for SymptomsAndInjuries
52 - updating level for TeachingTechniques
53 - updating level for TheCallOfTheWild
54 - updating level for TheGoldenCompass_201307
55 - updating level for TheHareRevenge
56 - updating level for TheLostEgg
57 - updating level for TheMouseThatWas
58 - updating level for Voltaireetext03candi10
59 - updating level for WomenAndEducation
60 - updating level for WorldAtlas_201303
61 - updating level for a0cf9b7b6981022e27a9ef6bb212baf1
62 - updating level for ab14eff48b4dcd59b653bf05fa70eee3
63 - updating level for b5dda003c94f8095f9efadc9cfc73c13
64 - updating level for b985804772c7acbde0c031f34f031444
65 - updating level for bb2b8f5c1dcee93158f72de6424c826e
66 - updating level for c2e3a55430dfa1172698f843010ce38f
67 - updating level for c958e477766294882405527b1f22d2ad
68 - updating level for c958e477766294882405527b1f406229
69 - updating level for cbd4a1877bb79eda6fc5f6659b119f36
70 - updating level for cbd4a1877bb79eda6fc5f6659b17e266
71 - updating level for cbd4a1877bb79eda6fc5f6659b2b7518
72 - updating level for cbd4a1877bb79eda6fc5f6659b593536
73 - updating level for cbd4a1877bb79eda6fc5f6659b85c6f1
74 - updating level for dc363e83b6dec454877464028524d508
75 - updating level for e1302d45b7a36ee766528b7aa2666be5
76 - updating level for e5821cbcaa0cbd84827ea97b955e99ff
77 - updating level for ed2775019f701e098f338dc126a11096
78 - updating level for ed2775019f701e098f338dc126effb39

"""



