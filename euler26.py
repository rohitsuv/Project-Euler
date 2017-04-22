from decimal import *


def decimal_part(n):	
	getcontext().prec = 10000
	return str(Decimal(1)/Decimal(n))[2:]
	
def find_nth(string1,a,n):
	sum = 0
	count = 0 
	for i in string1:
		count +=1
		if i == a:
			sum += 1
			if sum == n:
				return count
		
def count(string1,a):
	count = 0
	for i in string1:
		if i == a:
			count +=1
			
	return count
	
def chain_n(string1,a,n):
	index1 = find_nth(string1,a,1) - 1
	index2 = find_nth(string1,a,1+n) - 1
	return string1[index1:index2] == string1[index2:2*index2 - index1]	
		
def chain_len(string1,a,n):
	index1 = find_nth(string1,a,1) - 1
	index2 = find_nth(string1,a,1+n) - 1
	return index2 - index1
	

def len_recur(string1):
	if len(string1) == 10000 or len(string1) == 10001 or len(string1) == 10002:
		i = 2
		while True:
			if count(string1,string1[i]) > 9000:
				return 1
			if count(string1,string1[i]) > 5:
				for j in xrange(1,500):
					if chain_n(string1,string1[i],j):
						return chain_len(string1,string1[i],j)
					elif j == 499: 
						i = i + 1
			
			else: 
				i = i + 1 	
						
	
	else:
		return 0
				

			
		
l = []
for i in xrange(2,1000):
	print i
	q = decimal_part(i)
	r = len_recur(q)
	l.append(r)


for i in xrange(385,1000):
	print i
	q = decimal_part(i)
	r = len_recur(q)
	l.append(r)	
	
def f(string1)