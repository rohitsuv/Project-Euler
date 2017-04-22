f = open('euler81.txt')
g = f.readlines()

h = []
for i in g:
	j = i.replace('\n','')
	h.append(j)
	
k = []

for i in h:
	l = i.split(',')
	k.append(l)
	
p = []

for i in k:
	m = []
	for x in i:
		num = int(x)
		m.append(num)
	p.append(m)
	
s = []
for i in xrange(0,80):
	s.append([])
	
for i in s:
	for j in xrange(0,80):
		i.append(0)
#empty list of list s to fill the sums 
	
	
def prev(list1,sum_list,x,y):
	if x == 0 and y == 0 :
		return list1[x][y]
	elif x == 0:
		return sum_list[x][y-1] + list1[x][y]
	elif y == 0:
		return sum_list[x-1][y] + list1[x][y]
	else:
		return min(sum_list[x][y-1],sum_list[x-1][y]) + list1[x][y]
		
for x in xrange(0,80):
	for y in xrange(0,80):
		s[x][y] = prev(p,s,x,y)
		

print s[79][79]

	