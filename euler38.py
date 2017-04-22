def is_Pandig(num):
	if not '0' in str(num):
		if len(set(str(num))) == 9 and len(str(num)) == 9:
			return True
			
	return False
	
def product(num):
	num_str = ''
	i = 1
	while len(num_str) < 9:
		num_str += str(num*i)
		i += 1
		
	return int(num_str)

l = []	

for i in xrange(1,9999):
	if is_Pandig(product(i)):
		l.append(product(i))

print max(l)