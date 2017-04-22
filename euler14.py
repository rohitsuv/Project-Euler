
def no_terms(n):
	no = 1
	while n != 1:
		if n %2 == 0:
			n = n/2
			no += 1
		else:
			n = 3*n + 1
			no += 1
	return no
	
def max_collatz(n):
	list = []
	for i in xrange(1,n):
		no = no_terms(i)
		list.append(no)
			
	return list 
		
s = max_collatz(1000000)
v = s.index(max(s)) + 1
print v