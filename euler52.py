def is_perm(l):
	s = set(str(l[0]))
	for i in l:
		if set(str(i)) != s:
			return False
	return True
	
def mult_list(num):
	return [num,2*num,3*num,4*num,5*num,6*num]
	
cond = True
i = 1
while cond:
	if is_perm(mult_list(i)):
		print i
		cond = False
	i = i+1
	
print i 