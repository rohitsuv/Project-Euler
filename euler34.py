def factorial(n):
	a = 1
	while n > 0:
		a = a * n
		n = n-1
		
	return a
	
#can be a 7 digit no maximum

def sum_of_factorial(n):
	a = str(n)
	sum = 0
	for i in a:
		sum += factorial(int(i))
		
	return sum
l = []	
for i in xrange(0,10000000):
	if sum_of_factorial(i) == i:
		print i 
		l.append(i)
		
	
		
	

	
