from itertools import permutations

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
	i = a
	while i < n:
		if is_prime(i):
			l.append(i)
			i += 1
		else:
			i += 1 
			
	return l 
	
list_prime = Prime_list(1000,10000)

def Perm_prime(num):
	l = [''.join(p) for p in permutations(str(num))]
	j = []
	for i in l:
		if int(i) != num and is_prime(int(i)):
			j.append(int(i))
	return j

def has_prop(num):
	list_perm = Perm_prime(num)
	for i in list_perm:
		if 2*i - num in list_perm:
			return num,i,2*i - num
		else:
			continue
	return 0
m = []	
for i in list_prime:
	if has_prop(i) != 0:
		m.append(has_prop(i))
		
print m 
		

		
	