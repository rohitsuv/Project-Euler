def is_prime(x):
	if x <=0:
		return False
	if x == 1:
		return False
	c = int(x**0.5)  + 1
	for i in xrange(2,c):
		if x%i == 0:
			return False
			
	return True

#checking for 5 digit numbers
def next_num(num):
	if num% 10 ==3:
		return num + 4
	elif num%10 == 1 or num %10 == 7 or num%10 ==9 :
		return num + 2
	
	

	
def answer(num_prime):
	num = 1
	num_digits = 2
	num_star = num_digits - len(str(num))
	
def star_forms(num_digits):
	last_dig = [1,3,7,9]
	first_dig = range(1,10)
	other_dig = range(10)
	for star in xrange(1,num_digits):
		
	
		
	
	
	
	 
	
	
	
		
	
	
	
		
		

