string1 = ''

i = 0
while len(string1) < 1000000:
	string1 += str(i)
	i += 1

	
product = int(string1[0])*int(string1[9])*int(string1[99])*int(string1[999])*int(string1[9999])*int(string1[99999])*int(string1[999999])

print product