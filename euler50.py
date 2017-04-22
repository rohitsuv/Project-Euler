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
	
	

	
def maxi(a,n):
	count = 0
	sum = 0
	j = 0
	prime_sum = 0 
	l = Prime_list(a,n)
	for i in l:
		print i 
		sum += i
		j += 1
		if is_prime(sum) and j > count:
			prime_sum = sum
			print sum,j
			count = j	
	return prime_sum,count
	
def Maxi(n):
	count1 = 0
	ans = 0
	for i in Prime_list(2,n):
		if maxi(i,n)[1] > count1:
			count1 = maxi(i,n)[1]
			ans = maxi(i,n)
			
	return ans
	
print Maxi(1000000)
		
		
		