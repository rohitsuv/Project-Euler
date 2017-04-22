def single_numbers(n):
	dict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:
	'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
	16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
	return dict[n]
	
dict1 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
			
def words(n):
	m = str(n)
	l = len(m)
	if l == 4:
		return 'onethousand'
	elif l == 3 and m[1] == '0' and m[2] == '0':
		return single_numbers(int(m[0]))+'hundred'
	elif l == 3 and m[1] != '0' and m[1] != '1' and m[2] == '0':
		return single_numbers(int(m[0]))+'hundredand'+dict1[int(m[1])]
	elif l == 3 and m[1] == '0' and m[2] != '0':
		return single_numbers(int(m[0]))+'hundredand'+single_numbers(int(m[2]))
	elif l == 3 and m[1] == '1':
		return single_numbers(int(m[0]))+'hundredand'+single_numbers(int(m[1:]))
	elif l == 3:
		return single_numbers(int(m[0]))+'hundredand'+dict1[int(m[1])]+single_numbers(int(m[2]))
	elif l ==2 and m[0] =='1':
		return single_numbers(n)
	elif l == 2 and m[1] == '0':
		return dict1[int(m[0])]
	elif l == 2:
		return dict1[int(m[0])]+single_numbers(int(m[1]))
	elif l == 1:
		return single_numbers(n)
		
def list_words():
	sum = 0
	for i in xrange(1,1001):
		sum += len(words(i))
		
	return sum
	
s = list_words()
print s 

		