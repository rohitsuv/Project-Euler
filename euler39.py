def is_square(x):
	for i in xrange(0,x+1):
		if i*i == x:
			return True
	return False 


def num_triplets():
	l = []
	for i in xrange(2,1000):
		print i 
		for j in xrange(1,i):
			if is_square(i**2 - j**2):
				l.append((j,(i**2-j**2)**(1/2),i))
	return l 
			 
def return_triplet(x):
	list = []
	for k in xrange(1,x+1):
		for i in xrange(1,x):
			for j in xrange(1,x):
				if i*i + j*j == k*k:
					print i,j,k
					list.append((i,j,k))
	return list
	
a = return_triplet(1000)
b = []
for i in a:
	b.append(i[0]+i[1]+i[2])

	
#find most common in b below 1000 