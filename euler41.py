def is_prime(x):
	if x == 0 or x == 1:
		return False
	c = int(x**0.5)  + 1
	for i in xrange(2,c):
		if x%i == 0:
			return False
			
	return True
	
def is_Pandig(num):
	if not '0' in str(num):
		if len(set(str(num))) == len(str(num)) and int(max(str(num))) == len(str(num)):
			return True
			
	return False
l = []	
i = 7654321
while i >0 :
	if is_Pandig(i) and is_prime(i):
		print i
		l.append(i)
		break
	i = i - 1
	
print i 
	