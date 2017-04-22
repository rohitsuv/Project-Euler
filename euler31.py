def isValid(a,b,c,d,e,f,g,h):
	if a + 2*b + 5*c + 10*d + 20*e + 50*f + 100*g + 200*h == 200:
		return True
		
	return False
		
sum = 0 
		
for i in xrange(0,2):
	for j in xrange(0,3):
		for k in xrange(0,5):
			for l in xrange(0,11):
				for m in xrange(0,21):
					for n in xrange(0,41):
						for o in xrange(0,101):
							for p in xrange(0,201):
								if isValid(p,o,n,m,l,k,j,i):
									print p,o,n,m,l,k,j,i
									sum += 1
									