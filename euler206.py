def is_of_form(num):
	if len(str(num)) == 19:
		num_str = str(num)
		req_str = num_str[0] + num_str[2] + num_str[4] +num_str[6]+num_str[8]+num_str[10]+num_str[12]+num_str[14]+num_str[16]+num_str[18]
		if req_str == '1234567890':
			return True
	return False
	
cond = True
i = 1000000000

while cond:
	if is_of_form(i*i):
		cond = False
		print 'Answer is %d' %i
		break
	else:
		i+=10
		print i 
	