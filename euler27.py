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
	
def quadratic(n,a,b):
	return n**2 + a*n + b
	
#b has to be a prime
#a has to be odd

def num_of_cons_primes(a,b):
	i = 0
	while is_prime(quadratic(i,a,b)):
		i +=1
	return i
	
l = []

for i in xrange(2,1000):
	if is_prime(i):
		l.append(i)
		
for i in xrange(-999,1000,2):
	for j in l:
		if num_of_cons_primes(i,j) >=40:
			print i,j,num_of_cons_primes(i,j)
			m.append((i,j))
			
#max is a = =61, b = 971
			