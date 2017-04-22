global memo = {}

def Num_partitions(n,k):
	#number of partitions of a number n into k groups
	if (n,k) in memo:
		return memo[n,k]
	if k == 1 or n == k:
		ans = 1
		memo[(n,k)] = ans
	elif k < 1 or k > n:
		ans = 0
		memo[(n,k)] = ans
	else:	
		ans = Num_partitions(n-1,k-1) + Num_partitions(n-k,k)
		memo[(n,k)] = ans
	return ans

sum = 0		
		
for j in range(2,101):
	print j 
	sum += Num_partitions(100,j)