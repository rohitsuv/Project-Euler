text_file = open('names.txt')

names = text_file.readlines()
for i in names:
	names_ = i
	
names = names_.replace('"','')
list_names = names.split(',')
list_names.sort()
print list_names

scores = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':
13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def score_name(name):
	sum = 0
	for i in name:
		sum = sum + scores[i]
		
	return sum 

def tot_score(listnames):
	sum = 0 
	for i in xrange(0,len(listnames)):
		sum = sum + score_name(listnames[i])*(i+1)
		
	return sum

answer = tot_score(list_names)

print answer