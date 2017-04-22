def is_prime(x):
	if x <= 1:
		return False
	elif x<= 3:
		return True
	elif  x%2== 0 or x%3 == 0:
		return False
	i = 5
	while i*i <= x:
		if x%i == 0 or x%(i+2) == 0:
			return False
		i += 6
	return True
	

def no_repfact(num):
	for i in range(2,int(num**0.5 + 1)):
		if is_prime(i):
			if num%i == 0 and (num/i)%i ==0:
				return False
	return True
	
def Condition_true(num):
	
	if not is_prime(num+1):
		return False
	for i in xrange(1,int(num**0.5)+1):
		if num%i == 0:
			if not is_prime(i + num/i):
				return False
	return True
	
def sum(limit):
	sum = 0
	for i in xrange(2,limit+1,4): 
		if i > 6 and (i % 10 == 6 or i%10 == 4 or i%3 ==2):
			continue
		# if not no_repfact(i):
# 			continue
		if Condition_true(i):
			print i 
			sum += i
	print sum
	return sum
		