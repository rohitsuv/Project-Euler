def sum_divisors(n):
	sum = 0
	for i in xrange(1,n):
		if n%i == 0:
			sum = sum + i
	return sum
	
def is_abundant(n):
	return sum_divisors(n) > n 

list_abundant = []
for i in xrange(1,28124):
	if is_abundant(i):
		list_abundant.append(i)
		
def is_sum_of_elements(n,l):
	for i in l:
		if i < n and n - i in l: 
			return True
	return False
		
ans = []

for i in xrange(1,28123):
	if not is_sum_of_elements(i,list_abundant):
		print i 
		ans.append(i)
		
print sum(ans)
		
	
	
	
	
	
sum = 0		
for i in xrange(1,28124):
	if i not in list_sums:
		sum = sum + i
		


	