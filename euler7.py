def is_prime(x):
	for i in xrange(2,x):
		if x%i == 0:
			return False
			
	return True
	
def n_primes(n):
	list = []
	i = 2
	while i > 0:
		if is_prime(i):
			list.append(i)
			print i 
			if len(list) == n:
				i = 0
			else:
				i+=1
		else:
			i += 1
			
	return list
	
list = n_primes(10001)
print list
