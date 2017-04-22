def triangle_no(n):
	return n*(n+1)/2
	
def no_divisors(n):
	j = 0
	c = int(n**0.5) + 1
	for i in xrange(1,c+1):
		if n%i == 0:
			j +=2
	return j
	
def fn(n):
	i = 1
	while i > 0:
		t = triangle_no(i)
		d = no_divisors(t)
		if d > n:
			return t
		i +=1
		
s = fn(500)

print s