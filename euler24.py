import itertools

def perms():
	l = []
	a = [0,1,2,3,4,5,6,7,8,9]
	b = itertools.permutations(a)

	for	i in b:
		l.append(i)
	return l
	
x = perms()
answer = x[999999]
print answer