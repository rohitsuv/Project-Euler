

		
	
def is_even(a):
	if a%2 == 0:
		return True
	else:
		return False

def sum(a,b):
	return a + b
	

def fib(first,second):
	list = [first,second]
	while list[-1] +list[-2]< 4000000:
		list.append(list[-1] + list[-2])
	
	return list
	
		
c =fib(1,2)

sum = 0

for i in c:
	if i%2 == 0:
		sum = sum + i
		
	
print sum