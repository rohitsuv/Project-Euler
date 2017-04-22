
class Fraction(object):
	def __init__(self,num,den):
		self.numerator = num
		self.denominator = den
		self.value = num/float(den)
		
	def __lt__(self,other):
		return self.value < other.value
		
	def __str__(self):
		return " (%d / %d )" % (self.numerator,self.denominator)
		
	def __repr__(self):
		return self.__str__() 


		
def GCD(den,num):
	if num == 0:
		return den
	else:
		return GCD(num,den%num)
		


list_fracs = []

for d in range(2,1000001):
	print d
	for n in range(max(1,3*d/7 - 1),3*d/7 + 1):
		if GCD(n,d) ==1 :
			list_fracs.append(Fraction(n,d))
			
print list_fracs[len(list_fracs) - 2]
			
