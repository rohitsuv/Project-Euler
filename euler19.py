	
def is_leap_year(year):
	if year%100 == 0:
		if year%400 == 0:
			return True
		else:
			return False
	elif year%4 == 0:
		return True
	return False		

reg_days = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_days = [31,29,31,30,31,30,31,31,30,31,30,31]

def num_suns():
	n= 0
	days = 1
	for i in xrange(1901,2001):
		if is_leap_year(i):
			for j in leap_days:
				days = days + j
				print days
				if days%7 == 6:
					n = n+1
					print n
		else:
			for j in reg_days:
				days = days + j
				print days
				if days%7 == 6:
					n = n + 1
					print n 
	return n
				
			
			
a = num_suns()


print a 