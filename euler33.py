from decimal import *

def fraction(a,b):
	if b != 0:
		return Decimal(a)/Decimal(b)
	else:
		return "Not defined"		
			
def has_common(a,b):
	str1 = str(a)
	str2 = str(b)
	for i in str1:
		if i in str2 and i!= 0:
			return True
			
	return False
	
	
def remove_common(a,b):
	str1 = str(a)
	str2 = str(b)
	for i in str1:
		if i in str2 and i!= 0:
			str1 = str1.replace(i,'',1)
			str2 = str2.replace(i,'',1)
			return (int(str1),int(str2))
	
def curious_fractions():
	l = []
	val = 0
	temp = 0
	for i in xrange(11,100):
		for j in xrange(10,i):
			if has_common(j,i):
				val = fraction(j,i)
				temp = remove_common(j,i)
				if fraction(temp[0],temp[1]) == val:
					l.append((j,i))
					
	return l 
	
	
b = []
for i in a:
	if not '0' in str(i[0]):
		b.append(i)
		
print b				
				
				
				