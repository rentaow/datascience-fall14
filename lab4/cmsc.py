import re

file = open('cmsc.txt','r')

cname = re.compile('^CMSC[0-9]+')
section = re.compile('^0[0-9]+')
seats = re.compile('Seats \(Total: ([0-9]+), Open: ([0-9]+), Waitlist: ([0-9]+)\)')
day = re.compile('(M|Tu|W|Th|F)* (.*)$')
bldg = re.compile('(CSI|ITV|HBK|AVW|MTH|JMP) ([0-9]*)$')
a = re.compile('.*')

class1 = ''
line1 = ''

for line in file:
	if cname.match(line):
		class1 = cname.match(line).group()
	elif section.match(line):
		print line1
		line1 = class1 + ', ' + section.match(line).group()
	elif seats.match(line):
		matchgroup = seats.match(line)
		line1 += ', ' + matchgroup.group(1) + ', ' + matchgroup.group(2) + ', ' + matchgroup.group(3)
	elif day.match(line):
		matchgroup = day.match(line)
		line1 += ', ' + matchgroup.group(1) + ', ' + matchgroup.group(2)
	elif bldg.match(line):
		matchgroup = b;dg.match(line)
		line1 += ", " + matchgroup.group(1) + ", " + matchgroup.group(2)
	else:
		 line1 += ', ' + a.match(line).group()

print line1
