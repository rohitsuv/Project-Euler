def ispal(x):
	numstr = str(x)
	if len(numstr)%2 == 0:
		for i in xrange(0,len(numstr)/2 +1):
			if numstr[i] != numstr[len(numstr)-i-1]:
				return False
				
	else:
		for i in xrange(0,(len(numstr)-1)/2 +1):
			if numstr[i] != numstr[len(numstr)-i-1]:
				return False
	return True 

def reverse(x):
	numstr = str(x)
	l =''
	for i in xrange(0,len(numstr)):
		l += numstr[-1*(i + 1)]
	return int(l)
	
def is_lychrel(num):
	sum = 0
	for i in xrange(0,50):
		sum = num + reverse(num)
		if ispal(sum):
			return False
		else:
			num = sum
			sum = 0
			
	return True
	
count = 0 

for i in xrange(1,10000):
	if is_lychrel(i):
		count += 1
		
print count 