def is_prime(x):
	if x == 1 or x == 0:
		return False
	c = int(x**0.5)  + 1
	for i in xrange(2,c):
		if x%i == 0:
			return False
			
	return True
	
def is_truncatable(n):
	s = str(n)
	l = len(s)
	for i in xrange(0,l):
		if not is_prime(int(s[i:l+1])):
			return False
			
	for i in xrange(1,l):
		if not is_prime(int(s[0:i])):
			return False
			
	return True
	
	
count = 0 
i = 10
l = []
while count != 11:
	if is_truncatable(i):
		print i 
		count += 1
		l.append(i) 
		i += 1 
	else:
		print i 
		i += 1 
		
print sum(l)