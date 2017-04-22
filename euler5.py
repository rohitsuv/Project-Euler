def evendiv(x):
	for i in xrange(1,21):
		if x%i != 0 :
			return False
	return True
	
def small():
	for i in xrange(1,1000000000):
		if evendiv(i):
			return i
		
		
c = small()
print c 

