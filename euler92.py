def sum_square(num):
	sum = 0 
	while num:
		sum += (num%10)*(num%10)
		num = num/10
	return sum	
	
def typenum(num):
	ans = 0
	while ans !=1 and ans!= 89:
		ans = sum_square(num)
		num = ans
		
	return ans
	
count = 0 

for i in xrange(1,10000000):
	if typenum(i) == 89:
		print i 
		count += 1
	else:
		continue