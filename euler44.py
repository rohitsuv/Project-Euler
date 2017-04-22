def pentagonal_no():
	l = []
	for i in xrange(1,4000):
		l.append(i*(3*i-1)/2)
		
	return l
	
a = pentagonal_no()

m = []


				
			
for i in a[a.index(5993002):]:
	print i 
	for j in a[:a.index(i)]:
		if i - j in a and 2*j - i in a:
			m.append((j,i))
			


print m 