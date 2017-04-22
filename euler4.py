
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
l = []	
for i in xrange(100,1000):
	for j in xrange(100,1000):
		if ispal(i*j):
			l.append(i*j)
			
print l
print max(l) 
