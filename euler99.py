import math

def MaxVal_line(filename):
	file1 = open(filename)
	base_exp = []
	for line in file1.readlines():
		elem = line.strip().split(",")
		a,b = int(elem[0]),int(elem[1])
		base_exp.append((a,b))
	file1.close()
	return base_exp

dataList = MaxVal_line("p099_base_exp.txt")

max = None
index = None

for item in xrange(0,len(dataList)):
	if max == None:
		max = dataList[item][1]*math.log(dataList[item][0])
		index = item + 1
	else:
		val = dataList[item][1]*math.log(dataList[item][0])
		if val > max:
			max = val
			index = item + 1
	
print 'answe is %d' %index