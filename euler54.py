file = open('poker.txt')
g = file.readlines()

h = []
for i in g:
	j = i.replace('\n','')
	h.append(j)
	
j = []

for i in h:
	j.append(i.split(' '))
	
#j is now a list of hands
cards = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
dict_hand = {'royal_flush':9,'straight_flush':8,'four_kind':7,'full_house':6,'flush':5,'straight':4,'three_kind':3,'two_pairs':2,
		'one_pair':1,'high_card':0}

class Hand(object):
	def __init__(self,hands):
		dict_hand = {'royal_flush':9,'straight_flush':8,'four_kind':7,'full_house':6,'flush':5,'straight':4,'three_kind':3,'two_pairs':2,
		'one_pair':1,'high_card':0}
		cards = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
		self.hands = hands
		self.firsthand = hands[0:5]
		self.secondhand = hands[5:10]
		
	def get_firsthand(self):
		return self.firsthand
		
	def get_secondhand(self):
		return self.secondhand
		
	def values(self,hand_1):
		j = []
		for i in hand_1:
			j.append(i[0])
		return j 		
	
	def suits(self,hand_1):
		j = []
		for i in hand_1:
			j.append(i[1])
		return j 
		
	def flush(self,hand_1):
 		s = self.suits(hand_1)
 		term = s[0]
 		for i in s:
 			if i != term:
 				return False
 		return True
 		
 	def straight(self,hand_1):
 		v = self.values(hand_1)
 		s = []
 		for i in v:
 			s.append(cards[i])
 		for i in s:
 			if s.count(i) != 1:
 				return False
 		if max(s) - min(s) != 4:
 			return False
 		return True
 		
 	def straight_flush(self,hand_1):
 		if self.straight(hand_1) and self.flush(hand_1):
 			return True
 		return False
 	
 	def royal_flush(self,hand_1):
 		if self.straight_flush(hand_1):
 			if 'T' in self.values(hand_1) and 'A' in self.values(hand_1):
 				return True
 		return False
 	
 	def count1(self,hand_1):
 		v = self.values(hand_1)
 		c = []
 		for i in v:
 			c.append(v.count(i))
 		return c
 		
 	def four_kind(self,hand_1):
 		c = self.count1(hand_1)
 		if 4 in c:
 			return True
 		return False
 		
 	def full_house(self,hand_1):
 		c = self.count1(hand_1)
 		if 3 in c and 2 in c:
 			return True
 		return False
 		
 	def three_kind(self,hand_1):
 		c = self.count1(hand_1)
 		if 3 in c and not 2 in c:
 			return True
 		return False
 		
 	def two_pairs(self,hand_1):
 		c = self.count1(hand_1)
 		if c.count(2) == 4:
 			return True
 		return False
 		
 	def one_pair(self,hand_1):
 		c = self.count1(hand_1)
 		if c.count(2) == 2 and not 3 in c:
 			return True
 		return False
 		
 	def high_card(self,hand_1):
 		v = self.values(hand_1)
 		c =[]
 		for i in v:
 			c.append(cards[i])
 		return max(c)
 		
 	def check(self,term1,term2):
 		if term1 > term2:
 			return 'first'
 		else:
 			return 'second'
 		
 	def hand_type(self,hand_1):
 		if self.royal_flush(hand_1):
 			return 'royal_flush' 
 		elif self.straight_flush(hand_1):
 			return 'straight_flush'
 		elif self.four_kind(hand_1):
 			return 'four_kind'
 		elif self.full_house(hand_1):
 			return 'full_house'
 		elif self.flush(hand_1):
 			return 'flush'
 		elif self.straight(hand_1):
 			return 'straight'
 		elif self.three_kind(hand_1):
 			return 'three_kind'
 		elif self.two_pairs(hand_1):
 			return 'two_pairs'
 		elif self.one_pair(hand_1):
 			return 'one_pair'
 		else:
 			return 'high_card'
 	
 	def game(self,hand_1,hand_2):
 		c = self.hand_type(hand_1)
 		d = self.hand_type(hand_2)
 		if c != d:
 			return self.check(dict_hand[c],dict_hand[d])
 		else:
 			return self.tie(hand_1,hand_2)
 			
 			
 	def tie(self,hand_1,hand_2):
 		if self.hand_type(hand_1) in ['straight_flush','straight']:
 			a = self.high_card(hand_1)
 			b = self.high_card(hand_2)
 			return self.check(a,b)
 		elif self.hand_type(hand_1) == 'four_kind':
 			for i in self.values(hand_1):
 				if self.values(hand_1).count(i) == 4:
 					a = cards[i]
 			for i in self.values(hand_2):
 				if self.values(hand_2).count(i) == 4:
 					b = cards[i]
 			if a != b:
 				return self.check(a,b)
 			else:
 				for i in self.values(hand_1):
 					if self.values(hand_1).count(i) == 1:
 						a = cards[i]
 				for i in self.values(hand_2):
 					if self.values(hand_2).count(i) == 1:
 						b = cards[i]
 				return self.check(a,b)
		elif self.hand_type(hand_1) == 'full_house':
			for i in self.values(hand_1):
 				if self.values(hand_1).count(i) == 3:
 					a = cards[i]
 			for i in self.values(hand_2):
 				if self.values(hand_2).count(i) == 3:
 					b = cards[i]
 			if a != b:
 				return self.check(a,b)
 			else:
 				for i in self.values(hand_1):
 					if self.values(hand_1).count(i) == 2:
 						a = cards[i]
 				for i in self.values(hand_2):
 					if self.values(hand_2).count(i) == 2:
 						b = cards[i]
 				return self.check(a,b)
		elif self.hand_type(hand_1) == 'flush' or self.hand_type(hand_1) == 'high_card':
			v = self.values(hand_1)
			s = []
			for i in v:
 				s.append(cards[i])
			s.sort()
			s.reverse()
			w = self.values(hand_2)
			t = []
			for i in w:
 				t.append(cards[i])
			t.sort()
			t.reverse()
			for i in xrange(0,5):
				if s[i] != t[i]:
					return self.check(s[i],t[i])
				else:
					continue
		elif self.hand_type(hand_1) == 'three_kind':
			for i in self.values(hand_1):
 				if self.values(hand_1).count(i) == 3:
 					a = cards[i]
 			for i in self.values(hand_2):
 				if self.values(hand_2).count(i) == 3:
 					b = cards[i]
 			if a != b:
 				return self.check(a,b)
 			else:
 				v = self.values(hand_1)
 				w = self.values(hand_2)
 				c = []
 				d = []
 				for i in v:
 					if v.count(i) == 1:
 						c.append(cards[i])
 				for i in w:
 					if w.count(i) == 1:
 						d.append(cards[i])
 				d.sort()
 				d.reverse()
 				c.sort()
 				c.reverse()
 				for i in xrange(0,2):
					if c[i] != d[i]:
						return self.check(c[i],d[i])
					else:
						continue
		elif self.hand_type(hand_1) == 'two_pairs': 
			v = self.values(hand_1)
 			w = self.values(hand_2)
 			c = []
 			d = []
 			for i in v:
 				if v.count(i) == 2:
 					c.append(cards[i])
 					
 			c.sort()
 			c.reverse()
 			for i in w:
 				if w.count(i) == 2:
 					d.append(cards[i])
 			d.sort()
 			d.reverse()
 			for i in xrange(0,4):
				if c[i] != d[i]:
					return self.check(c[i],d[i])
				else:
					continue
			for i in v:
				if v.count(i) == 1:
					a = cards[i]
			for i in w:
				if w.count(i) == 1:
					b = cards[i]
			return self.check(a,b)
		elif self.hand_type(hand_1) == 'one_pair':
			v = self.values(hand_1)
 			w = self.values(hand_2)
			for i in v:
				if v.count(i) == 2:
					a = cards[i]
			for i in w:
				if w.count(i) == 2:
					b = cards[i]
			if a != b :
				return self.check(a,b)
			c = []
			d = []
			for i in v:
 				if v.count(i) == 1:
 					c.append(i)
 			c.sort()
 			c.reverse()
 			for i in w:
				if w.count(i) == 1:
					d.append(i)
			d.sort()
			d.reverse()
			for i in xrange(0,3):
				if c[i] != d[i]:
					return self.check(c[i],d[i])
				else:
					continue
	
def game1(j):
	a = Hand(j)
	b = a.get_firsthand()
	c = a.get_secondhand()
	return a.game(b,c)

q = 0
w = 0 

for i in j:
	ans = game1(i)
	if ans == 'first':
		q += 1
	elif ans == 'second':
		w += 1
print q
print w	
			
			
			
			
 			
			
				
			
 		
 			
 			
 		
 		
 		
		
#types of hands,high card,pair, two pair, three of a kind,four of a kind, full house,
		
	