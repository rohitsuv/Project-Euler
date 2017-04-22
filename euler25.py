def no_digits(n):
	st = str(n)
	num = len(st)
	return num
	
def thousand_digit(n):
	list = [1,1]
	while no_digits(list[-1]) < n:
		list.append(list[-1]+list[-2])
		
	return len(list)
	
s = thousand_digit(1000)
print s 