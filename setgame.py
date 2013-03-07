import random

class Card(object):
	"""this class represents a set Card"""
	def __init__( self, color, number, shape, fill ):
		self.color = color
		self.number = number
		self.shape = shape
		self.fill = fill

	def __repr__(self):
		return "<" + self.color + str(self.number) + self.shape + str(self.fill) + ">"
		pass

class Board(object):
	"""this class represents the game board"""
	def __init__( self ):
		self.positions =  []
		self.deck = []
		pass

	def deal( self, num_cards ):
		"appends num_cards to list to parent's deck"
		#get int cards from the deck, append to game board
		for n in xrange(0, num_cards, 1):
			random.shuffle(self.deck)
			pick = random.randint(0, len(self.deck)-1)
			self.positions.append(self.deck.pop(pick))
		pass

	def draw():	
		"""placeholder for drawing a card"""
		pass

def generate_cards():
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

def check_hand( card1, card2, card3 ):
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

def hash_hand( *cards ):
	attribute_list = ['color', 'number', 'shape', 'fill']
	conditions_met = set()
	for c in cards:
		for a in attribute_list:
			condition = getattr(c, a)
			conditions_met.add(condition)
	print repr(conditions_met)
	if len(conditions_met)==len(cards):
		print "unique set found: " + repr(cards)
	elif len(conditions_met)==len(cards):
		print "set found: " + repr(cards)
	else:
		pass

def newdemo():
	deck = generate_cards()
	hand = []
	for n in 1, 2, 3:
		random.shuffle(deck)
		pick = random.randint(0, len(deck)-1)
		hand.append(deck.pop(pick))
	print 'checking this hand:', repr(hand)
	matches = chk_hnd(*hand)
	#print matches
	#	print 'set found:', repr(hand)
	#pass

def demoplay():
	deck = generate_cards()
	hand = []
	for n in 1, 2, 3:
		random.shuffle(deck)
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

def play():
	game = Board()
	game.deck = generate_cards()
	game.deal(12)
	return game

