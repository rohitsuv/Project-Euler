def factorial(n):
	a = 1
	while n > 0:
		a = a * n
		n = n-1
		
	return a
	
def sum_digits(x):
	s = str(x)
	l = len(s)
	sum = 0
	for i in s:
		sum = sum + int(i)
		
	return sum
	
v = factorial(100)

answer = sum_digits(v)
print answer