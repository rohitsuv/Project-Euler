def series(lower,upper):
	l = []
	for i in xrange(lower,upper+1):
		for j in xrange(lower,upper+1):
			if i**j not in l:
				l.append(i**j)
				
	return l 
	
a = series(2,100)
answer = len(a)
print answer