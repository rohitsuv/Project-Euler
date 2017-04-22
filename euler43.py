from itertools import permutations

def is_Pandig(num):
	
	if len(set(str(num))) == 10 and len(str(num)) == 10:
		return True
			
	return False
	
def has_prop(num):
	if int(num[1:4])%2 == 0 and int(num[2:5])%3 ==0 and int(num[3:6])%5 == 0 and int(num[4:7])% 7 == 0 and int(num[5:8])%11 == 0 and int(num[6:9])%13 == 0 and int(num[7:10])%17 == 0:
		return True
		
	return False

l = [''.join(p) for p in permutations('0123456789')]	
sum = 0 

for i in l:
	if has_prop(i):
		sum += int(i)
		
print sum 