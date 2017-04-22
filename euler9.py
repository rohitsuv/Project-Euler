def is_square(x):
	for i in xrange(0,x+1):
		if i*i == x:
			return True
	return False 
	
def return_triplet(x):
	list = []
	for k in xrange(1,x+1):
		for i in xrange(1,x):
			for j in xrange(1,x):
				if i*i + j*j == k*k:
					print i,j,k
					list.append((i,j,k))
	return list
	
y = return_triplet(1000)

for i in y:
	if i[0]+i[1]+i[2] == 1000:
		print i 
		
product = i[0]*i[1]*i[2]