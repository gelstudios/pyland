import random

class Card(object):
	"""this represents a set Card"""
	def __init__(self, color, number, shape, fill):
		self.color=color
		self.number=number
		self.shape=shape
		self.fill=fill

	def __repr__(self):
		return "<" + self.color + str(self.number) + self.shape + str(self.fill) + ">"
		pass

def generate_cards():
	"""returns a list of cards"""
	color = ['red','green','purple']
	number = [1,2,3]
	shape = ['~','o','v']
	fill = [100,50,0]
	cards = []
	for c in color:
		for n in number:
			for s in shape:
				for f in fill:
					new_card=Card(c, n, s, f)
					cards.append(new_card)
	return cards

def check_hand(card1, card2, card3):
	attribute_list = ['color', 'number', 'shape', 'fill']
	matches = []
	for a in attribute_list:
		if getattr(card1, a) == getattr(card2, a) == getattr(card3, a):
			matches.append(a)
	if len(matches) == 0:
		matches.append('none')
	return matches

def demoplay():
	deck = generate_cards()
	hand = []
	for n in 1, 2, 3:
		pick = random.randint(0, len(deck))
		#pick = random.random() % len(deck)
		hand.append(deck[pick])
		deck.remove(deck[pick])
		print 'picking card #', str(n), 'hand:', repr(hand)
		print 'this card was removed from the deck', repr(deck[pick])
	print 'checking this hand:', repr(hand)
	matches = check_hand(*hand)
	print repr(matches)
	pass

