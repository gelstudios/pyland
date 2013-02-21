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
	conditions_met = []
	for a in attribute_list:
		x = getattr(card1, a)
		y = getattr(card2, a)
		z = getattr(card3, a)
		if x == y == z:
			conditions_met.append(a)
		elif x != y and y != z and x != z:
			conditions_met.append(a)
	return conditions_met


def demoplay():
	deck = generate_cards()
	hand = []
	for n in 1, 2, 3:
		pick = random.randint(0, len(deck)-1)
		#hand.append(deck[pick])
		hand.append(deck.pop(pick))
		print 'picking card #', str(n), ', hand:', repr(hand)
		print str(len(deck)),'cards left in the deck'
	print 'checking this hand:', repr(hand)
	matches = check_hand(*hand)
	if len(matches)==4:
		print 'set found:', repr(hand)
	pass



