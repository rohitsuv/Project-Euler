def sum_dig(a,b):
	sum = 0
	str1 = str(a**b)
	for i in str1:
		sum += int(i)
		
	return sum
	

def max_sum():
	sum = 0
	for i in xrange(0,100):
		for j in xrange(0,100):
			if sum_dig(i,j) > sum:
				sum = sum_dig(i,j)
				a,b = i,j
				
	return sum,a,b

print sum,a,b