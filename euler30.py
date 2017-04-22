def fifthpower_sum(n):
	b = str(n)
	sum = 0 
	for i in b:
		sum = sum + int(i)**5
		
	return sum 
	
#it can be a maximum of 6 digits as 9999999 has 6 digits.
l = []
sum = 0
for i in xrange(2,1000000):
	if fifthpower_sum(i) == i :
		l.append(i)
		sum = sum + i 
		
print l 
print sum 

 

