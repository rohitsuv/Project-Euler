f = open('p079_keylog.txt')
g = f.read()
h = g.split('\n')
l = []
h.pop()
for i in h:
	l.append(int(i))
	
num = [0,1,2,3,6,7,8,9]
num1 = '01236789'

def change(keycode, login):
	i = 0
	while i < 2:
		if keycode.index(int(login[i])) < keycode.index(int(login[i+1])):
			i += 1
			continue
		else:
			keycode.remove(int(login[i+1]))
			if keycode[-1] != int(login[i]):
				keycode[keycode.index(int(login[i]))+2:] = keycode[keycode.index(int(login[i]))+1:]
				keycode[keycode.index(int(login[i]))+ 1] = int(login[i+1])
				i += 1
			else:
				keycode.append(int(login[i+1]))
	return keycode
	
for i in l:
	temp = change(num,str(i))
	num = temp
	
print num 
	