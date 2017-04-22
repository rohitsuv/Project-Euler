
def sum_divisors(n):
	sum = 0
	for i in xrange(1,n):
		if n%i == 0:
			sum = sum + i
	return sum
	
def is_amicable(a,b):
	if a == b :
		return False
	elif a != b :
		return sum_divisors(a) == b and sum_divisors(b) == a
	
def sum_amicable(n):
	sum = 0
	for i in xrange(1,n):
		if is_amicable(i,sum_divisors(i)):
			sum = sum + i
				
	return sum

answer = sum_amicable(10000)

print answer