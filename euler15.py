import itertools

def selections(x, total):
	b = factorial(x)
	answer = 1
	while x > 0:
		answer = answer*total
		total = total - 1
		x = x - 1
		
	return answer/b
			
def factorial(n):
	a = 1
	while n > 0:
		a = a * n
		n = n-1
		
	return a 
	
c = selections(20,40)
print c