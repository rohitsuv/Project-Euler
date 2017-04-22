#n is num len of square

from decimal import Decimal

def diag_elem(n):
	i = 1
	k = 2
	prime = 0 
	count = 1
	while i < n**2:
		for j in xrange(0,4):
			i = i + k
			count += 1
			if is_prime(i):
				prime += 1 
		k = k + 2
	print prime,count
	return Decimal(prime)/Decimal(count)
			
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


	
def diag_elem2():
	i = 1
	k = 2
	prime = 0 
	count = 1
	while True:
		for j in xrange(0,4):
			i = i + k
			count += 1
			if is_prime(i):
				prime += 1 
		if Decimal(prime)/Decimal(count) < 0.1:
			return i
		k = k + 2
	
a = diag_elem2()

ans = a**0.5

print ans
	
	
	
	
	
	
	
	
	
	
	
	