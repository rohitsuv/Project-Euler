from fractions import Fraction
from __future__ import division


	
	
def num_more(n):
	s = funct(n)
	if len(str(s.numerator)) > len(str(s.denominator)):
		return True
		
	return False
	

		
def funct():
	i = 0
	t = 1/2
	count = 0
	while i < 1001:
		sum = Fraction(1 + Fraction(t))
		t = Fraction(1/Fraction(2+t))
		i += 1
		if len(str(sum.numerator)) > len(str(sum.denominator)):
			count += 1
			
	return count
	
a = funct()
print a