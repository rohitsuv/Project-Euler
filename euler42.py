l = []
for i in xrange(1,40):
	l.append(i*(i+1)/2)
	
f = open('p042_words.txt')

g= f.read()

h = g.replace('"','')
i = h.split(',')

scores = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':
13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def score(word):
	sum = 0
	for i in word:
		sum += scores[i]
		
	return sum
	
sum = 0 
	
for j in i:
	if score(j) in l:
		sum += 1
		
print sum