def triangle_no():
	l = []
	for i in xrange(1,100000):
		l.append(i*(i-1)/2)
	return l

def pentagonal_no():
	l = []
	for i in xrange(1,100000):
		l.append(i*(3*i-1)/2)
		
	return l
	
def hexagonal_no():
	l= []
	for i in xrange(1,100000):
		l.append(i*(2*i-1))
		
	return l
	
t = triangle_no()
p= pentagonal_no()
h = hexagonal_no()

answer = []
for i in t:
	print i 
	if i in p and i in h:
		print i
		answer.append(i)
		if len(answer) == 3:
	 		break
	 		
print answer
	 		
