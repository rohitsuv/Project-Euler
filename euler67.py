text_file = open("p067_triangle.txt","r")
lines = text_file.readlines()

t = []

	
for i in xrange(0,len(lines)):
	t.append(lines[i].replace('\n',''))
	
print t

n = []

for i in t:
	n.append(i.split())

print i

m = []
for i in xrange(0,len(n)):
	m.append([])
	
for i in xrange(0,len(n)):
	m[i] = [int(j) for j in n[i]]
	

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
#answer is top element 	

