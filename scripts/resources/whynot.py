# given a tab-delimited input file and two column indices, say why
# the second column is not functionally dependent on the first
import sys

infile = open(sys.argv[1])
left = int(sys.argv[2])
right = int(sys.argv[3])

header = infile.readline()[:-1]

dict = {}
lineno = 2
try:
	while 1:
		line = infile.readline()[:-1]
		fields = [x.rstrip() for x in line.split("\t")]
		if dict.has_key(fields[left]) and dict[fields[left]][1] != fields[right]:
			print "line %d vs %d: %s != %s" % (lineno, dict[fields[left]][0], dict[fields[left]][1], fields[right])
		else:
			dict[fields[left]] = (lineno, fields[right])
		lineno = lineno + 1
except:
	pass
