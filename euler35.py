def is_prime(x):
	if x <=0:
		return False
	if x == 1:
		return False
	c = int(x**0.5)  + 1
	for i in xrange(2,c):
		if x%i == 0:
			return False
			
	return True
	
def rotations(n):
	l = [n]
	a = str(n)
	b = ''
	while len(l) != len(a):
		for i in xrange(0,len(a)):
			b += a[i - 1]
		
		l.append(int(b))
		a = b
		b = ''
	return l 
	
def is_circprime(n):
	for i in rotations(n):
		if not is_prime(i):
			return False
			
	return True

sum = 0	
for i in xrange(2,1000000):
	if is_circprime(i):
		print i
		sum += 1
		
