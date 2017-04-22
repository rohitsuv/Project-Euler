def is_square(n):
	if n == 1:
		return True
	for i in xrange(1,n):
		if n == i*i:
			return True
			
	return False
	
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

def Prime_list(a,n):
	l = []
	for i in xrange(a,n):
		if is_prime(i):
			l.append(i)
     
	return l


def is_gladbach(n):
	for i in Prime_list(2,n): 
		if is_square((n-i)/2) and (n-i)%2 == 0:
			return True
	
	return False
	
	
cond = True
i = 3
c = 0

while cond:
	if not is_prime(i):
		if not is_gladbach(i):
			c = i
			cond = False
		
		else:
			i += 2
			print i 
	else:
		i += 2
		print i 
		
		
print c 