import random
import itertools

class Game(object):
	"""the global game class, the game state is represented here"""
	def __init__( self, player ):
		self.attributeList = ['color', 'number', 'shape', 'fill']
		self.positions = []
		self.deck = generateCards()
		self.players = {}
		self.deal(12)
		self.addPlayers(player)

	def deal( self, num_cards ):
		"removes num_cards from the parent's deck, and inserts them in the positions list"
		#get int cards from the deck, append to game board
		for n in xrange(0, num_cards, 1):
			random.shuffle(self.deck)
			pick = random.randint(0, len(self.deck)-1)
			try:
				self.positions.append(self.deck.pop(pick))
			except:
				return

	def checkHand( self, *cards ):
		matches=0
		for a in self.attributeList:
			check = set()
			for c in cards:
				cardAttribute = getattr(c, a)
				check.add(cardAttribute)
			if len(check)==len(cards) or len(check) == 1:
				matches += 1
		if matches == len(self.attributeList):
			return True
		else:
			return False

	def checkBoard( self ):
		"""checks board for any sets, deals 3 more if none"""
		matches = 0
		hands = itertools.combinations(self.positions, 3)
		for h in hands:
			match = self.checkHand(*h)
			if match == True:
				print "sets on the board: " + repr(h)
				matches += 1
		if matches == 0:
			self.deal(3)

	def addPlayers( self, *players ):
		"""adds Player objects to game Class"""
		for p in players:
			self.players[p.uid]=p
			p.parent = self

class Player(object):
	"""this class represents a player. requires a uid and string name """
	def __init__(self, uid, name):
		self.uid = uid
		self.name = name
		self.score = 0
		self.hand = []

	def pickCard(self, card_id):
		card=self.parent.positions[card_id]
		if card in self.hand:
			return None
		if card in self.parent.positions:	
			self.hand.append(card)
			if len(self.hand) == 3:
				h=self.parent.checkHand(*self.hand)
				if h:
					self.score += 1
					for card in self.hand:
						self.parent.positions.remove(card)
					self.parent.deal(3)
				self.hand = []

class Card(object):
	"""this class represents a set-game Card"""
	def __init__( self, color, number, shape, fill ):
		self.color = color
		self.number = number
		self.shape = shape
		self.fill = fill

	def __repr__(self):
		return "-" + self.color + str(self.number) + self.shape + str(self.fill) + "-"

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
	"""demo method"""
	player = Player( 1203812039821, "eric" )
	game = Game( player )
	while len(player.hand) < 3:
		print "hello " + player.name
		print "game board:"
		print repr(game.positions[0:3])
		print repr(game.positions[4:7])
		print repr(game.positions[8:11])
		if len(game.positions) > 12:
			print repr(game.positions[12:14])
		print
		print "your hand: " + repr(player.hand)
		print "score: " + str(player.score) + " pts"
		userInput = raw_input("Pick a card>")
		player.hand.append(int(userInput))
	print "checking this hand: ", repr(player.hand)
	matches = game.checkHand(*player.hand)
	if matches == True:
		print 'set found:', repr(player.hand)
		player.score += 1
#	myhand=[ Card('red', 1,'~',0), Card('red', 1, 'o', 50), Card('red', 1, 'v', 100) ]
