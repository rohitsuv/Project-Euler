def is_prime(x):
	for i in xrange(2,x):
		if x%i == 0:
			return False
			
	return True

				
				
def divide_byprime(x):
	i = 2
	for i in xrange(2,x):
		if is_prime(i) and x%i == 0:
			return x/i
	return x

#c = prime_factors(600851475143)

#print c 
#d = divide_byprime(600851475143)
#print d
def final_prime(x):
	while divide_byprime(x) != x :
		x = divide_byprime(x)
		
	return x 
e = final_prime(600851475143)	
print e
