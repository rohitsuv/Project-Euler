def factorial(n):
	a = 1
	while n > 0:
		a = a * n
		n = n-1
		
	return a
	
def Combin(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))
	
	
count = 0

for i in xrange(23,101):
	for j in xrange(0,i+1):
		if len(str(Combin(i,j))) >= 7:
			count += 1
			
print count