def power_2(x):
	p = 1
	for i in xrange(0,x):
		p = p*2
	return p 
	
def sum_digits(x):
	s = str(x)
	l = len(s)
	sum = 0
	for i in s:
		sum = sum + int(i)
		
	return sum
	
		
a = power_2(1000)

b = sum_digits(a)

print b 