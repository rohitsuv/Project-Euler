def ispal(x):
	numstr = str(x)
	if len(numstr)%2 == 0:
		for i in xrange(0,len(numstr)/2 +1):
			if numstr[i] != numstr[len(numstr)-i-1]:
				return False
				
	else:
		for i in xrange(0,(len(numstr)-1)/2 +1):
			if numstr[i] != numstr[len(numstr)-i-1]:
				return False
	return True 
	
def reverse(s):
	rev = ''
	i = len(s) - 1
	while i >= 0:
		rev = rev + s[i]
		i = i - 1
		
	return rev
	

	
def base2(x):
	num1 = ''
	if x == 0 or x == 1:
		return x
	while x > 1 :
		num1 = num1 + str(x%2)
		x = x/2
		
	num1 += str(1)
	num2 = reverse(num1)
	
	return int(num2)
	
l = []	
sum = 0
for i in xrange(0,1000000):	
	
	if ispal(i) and ispal(base2(i)):
		print i 
		l.append(i)
		sum += i
		
print sum 
		
	
	
		
	