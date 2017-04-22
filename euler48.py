
def power(n):
	 sum = 0 
	 for i in xrange(1,n+1):
	 	sum = sum + (i**i)%10**10
	 	
	 return sum 
	 
c = power(1000)

#answer is last ten digits