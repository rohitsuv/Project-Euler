import string

f = open('p059_cipher.txt')
g = f.read()
g = g.replace('\n','')

h = g.split(',')
list1 = []

for i in h:
	list1.append(int(i))

letters = string.ascii_lowercase
letters2 = string.ascii_uppercase


def is_word(str1):
	for i in str1:
		if i not in letters and i not in letters2:
			return False
		
	return True

for i in letters:
	s = ''
	for j in letters:
		for k in letters:
			asc1 = [ord(i),ord(j),ord(k)]
			for d in l:
				s += chr(d^asc1[l.index(d)%3])
					
				e = s.split(' ')
				
				for m in e:
					if not is_word(m):
						break
				
					
					
def find_key():	
	s = ''
	c = 0 
	for i in letters[5:]:
		for j in letters:
			for k in letters:
				print i,j,k
				asc1 = [ord(i),ord(j),ord(k)]
				for d in list1:
					s += chr(d^asc1[c%3])
					c += 1
					
				s = s.replace('.','')
				s = s.replace('(','')
				s = s.replace(')','')
				s = s.replace(',','')
				s = s.replace('!','')
				s = s.replace('`','')
				s = s.replace('-','')
				s = s.replace('/','')
				s = s.replace(';','')
				s = s.replace(':','')
				s = s.replace("'",'')
				
				print s 
				
				if is_words(s):
					return s
				else:
					s = ''
					c = 0
					continue
					
				

def decrypted(i,j,k,l):
	s = ''
	c = 0
	asc1 = [ord(i),ord(j),ord(k)]
	for m in l:
		s += chr(m^asc1[c%3])
		c += 1
		
	return s
	
def ascii_conv(text):
	l = []
	for i in text:
		l.append(ord(i))
		
	return l
		
def is_words(str1):
	for i in str1:
		if not i.isalpha() and not i.isspace() and not i.isdigit():
			return False
			
	return True
	


				