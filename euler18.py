p = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

pd = p.split('\n')

l = []
for i in pd:
	l.append(i.split())
	
print l
m = []
for i in xrange(0,15):
	m.append([])
	
	

for i in xrange(0,15):
	m[i] = [int(j) for j in l[i]]
	
print m


def upper_branch(list_lower,list_upper):
	length = len(list_upper)
	new_branch = []
	for i in xrange(0,length):
		new_branch.append(max([list_upper[i]+list_lower[i],list_upper[i]+list_lower[i+1]]))
		
	return new_branch
		
def new_pyramid(p):
	newP = []
	for i in xrange(0,len(p)):
		newP.append([])
		
	newP[len(p)-1] = p[len(p)-1]
	index = len(p) - 2
	while index >= 0:
		newP[index] = upper_branch(p[index+1],p[index])
		p[index] = newP[index]
		index -= 1
		
	return newP
	
s = new_pyramid(m)

#answer is the first element
		
	