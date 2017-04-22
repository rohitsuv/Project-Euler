def is_prime(x):
	c = int(x**0.5)  + 1
	for i in xrange(2,c):
		if x%i == 0:
			return False
			
	return True
	
def primes_below(x):
	list = []
	for i in xrange(2,x):
		if is_prime(i):
			print i 
			list.append(i)
	return list
	
y = primes_below(2000000)

def sumlist(y):
	sum = 0
	for i in y :
		sum = sum+ i
	return sum


sum = sumlist(y)
print sum 


	
	