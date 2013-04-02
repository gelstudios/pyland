import random

class Game(object):
	"""the global game class, the game state is represented here"""
	def __init__( self ):
		self.positions = []
		self.deck = generateCards()
		self.players = []

	def deal( self, num_cards ):
		"removes num_cards from the parent's deck, and inserts them in the positions list"
		#get int cards from the deck, append to game board
		for n in xrange(0, num_cards, 1):
			random.shuffle(self.deck)
			pick = random.randint(0, len(self.deck)-1)
			self.positions.append(self.deck.pop(pick))
		pass

	def checkHand( *cards ):
		attributeList = ['color', 'number', 'shape', 'fill']
		matches=0
		cards=cards[1:]
		#print "repr of cards is: " + repr(cards)
		for a in attributeList:
			check = set()
			for c in cards:
				cardAttribute = getattr(c, a)
				check.add(cardAttribute)
			#print repr(check)
			if len(check)==len(cards) or len(check) == 1:
				#print a + " set found: " + repr(cards)
				matches += 1
		if matches == len(attributeList):
			return True
		else:
			return False

class Player(object):
	def __init__( self, uid, name ):
		self.uid = uid
		self.name = name
		self.score = 0
		self.hand = []

class Card(object):
	"""this class represents a set-game Card"""
	def __init__( self, color, number, shape, fill ):
		self.color = color
		self.number = number
		self.shape = shape
		self.fill = fill

	def __repr__(self):
		return "<" + self.color + str(self.number) + self.shape + str(self.fill) + ">"
		pass

def generateCards():
	color = ['red','green','purple']
	number = [1,2,3]
	shape = ['~','o','v']
	fill = [100,50,0]
	cards = []
	for c in color:
		for n in number:
			for s in shape:
				for f in fill:
					newCard=Card(c, n, s, f)
					cards.append(newCard)
	return cards

def do():
	import os
	game = Game()
	game.deal(12)
	player = Player( 1203812039821, "eric" )
	player.tmpPositions = game.positions 
	while len(player.hand) < 3:
		os.system('clear')
		print "hello " + player.name
		print "game board:"
		print repr(player.tmpPositions[0:3])
		print repr(player.tmpPositions[4:7])
		print repr(player.tmpPositions[8:11])
		print 
		print "your hand: " + repr(player.hand)
		print "score: " + str(player.score) + " pts"
		userInput = raw_input("Pick a card>")
		try:
			player.hand.append(player.tmpPositions.pop(int(userInput)))
		except:
			print "not a valid choice"
		pass
	print 'checking this hand:', repr(player.hand)
	matches = game.checkHand(*player.hand)
	if matches == True:
		print 'set found:', repr(player.hand)
		player.score += 1


#	myhand=[ Card('red', 1,'~',0), Card('red', 1, 'o', 50), Card('red', 1, 'v', 100) ]
#	game.checkhand(*hand)
	pass