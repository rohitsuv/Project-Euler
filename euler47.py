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
	sum = 0
	i = a
	while sum < n:
		if is_prime(i):
			sum += i
			l.append(i)
			i += 1
		else:
			i += 1 
			
	return l 

def cons_prime(init,n):
	for i in xrange(init,init+n):
		if num_prime(i) != n:
			return False
			
	return True

	
		
def n_cons(n):
	i = 120000
	cond = True
	while cond:
		if cons_prime(i,n):
			cond = False
			return i
		else:
			print i 
			i+= 1
	
def num_prime(num):
	count = 0
	for i in Prime_list(2,num):
		if is_prime(i):
			if num%i == 0:
				count += 1
				
	return count


print n_cons(4)
	
				