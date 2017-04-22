def four_squares(n):
	if n == 1:
		return 1
	else:
		a = n*n
		b = a - (n-1)
		c = b - (n-1)
		d = c - (n-1)
		sum = a+b+c+d
	return sum
	
s = 0	
for i in xrange(1,1003,2):
	s = s + four_squares(i)
	
print s 
	