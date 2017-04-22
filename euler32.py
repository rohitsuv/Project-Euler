def is_Pandig(num):
	if not '0' in str(num):
		if len(set(str(num))) == 9 and len(str(num)) == 9:
			return True
			
	return False
	
def list_prod():
	l = []
	for i in xrange(1,99): 
		for j in xrange(100,9999):
			if is_Pandig(int(str(i)+str(j)+str(i*j))):
				l.append(i*j)
				
	return l 

a = list_prod()
b = set(a)
c = sum(b)
print b 


print c 