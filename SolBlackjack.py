#SolBlackjack.py
#author Brandon Muirhead

from cards import *

class SolBlackjack():
	
	table = {'row1':[1, 2, 3, 4, 5], 'row2':[6, 7, 8, 9, 10], 'row3':[11, 12, 13], 'row4':[14, 15, 16]}
	discardList = [17, 18, 19, 20]
	
	def __init__(self):
		self.deck = Deck()
		
	#def scoreHand(self):
	
	#def displayHand(self):
	
	def gameState(self):
		'''Visually represents the current state of the game with four rows and the discard pile'''
		listHand = []
		for key in self.table:
			new = [str(x) + '\t' for x in self.table[key]]
			listHand.append(new)
		gameState = self.flatten2DList(listHand)
		discard = [str(x) + '\t' for x in self.discardList]
		
		row1 = gameState[0:4]					#creates string of characters in shape of game
		row1 = self.list_to_string(row1)
		row2 = gameState[5:9]
		row2 = self.list_to_string(row2)
		row3 = gameState[10:12]
		row3 = self.list_to_string(row3)
		row4 = gameState[13:15]
		row4 = self.list_to_string(row4)
		
		print 'Table: '
		print row1 + '\n' + row2 + '\n\t' + row3 + '\n\t' + row4
		print '\nDiscard Pile: '
		print self.list_to_string(discard) + '\n'
	
	def play(self):
		deck = Deck()
		deck.shuffle()
		print deck
		print 'Welcome to Solitaire Blackjack. You can choose where to place the top card in the deck.\n'
		
		#while not self.gameOver():
		#	self.gameState()
		#	card = deck.deal()				#card is a Card object
		#	print 'The top card on the deck is: ', card
		#	self.acceptUserMove()
		#	self.processUserMove()
			
	def acceptUserMove(self):
		'''Asks user to specify a move location, then checks to ensure input is acceptable'''
		move = raw_input('Please indicate the position in which you would like to place this card: ')
		if self.checkErrorMove(move):
			return move
		
	def checkErrorMove(self, input):
		'''Checks a user's move for errors in input'''
		question = False
		while question == False:
			if input not in range(1,17):
				print 'Please enter a number corresponding with slots 1-16'
				input = raw_input('Please indicate the position in which you would like to place this card: ')
			####elif input: 
				####question = True
		return question

	def processUserMove(self, location, card):
		'''Takes move which has been error checked and executes the move'''
		if location in range(1,6):
			self.table['row1'][location] = card		#card is Card object
		elif location in range(6, 11):
			self.table['row2'][location - 6] = card 
		elif location in range(11, 14):
			self.table['row3'][location - 11] = card
		elif location in range(14, 17):
			self.table['row4'][location - 14] = card
		else:
			discardList[location - 17] = card

	def gameOver(self):
		'''Checks to see if all 16 spots on the table are filled with card objects'''
		for key in self.table:
			return all(isinstance(x, Card) for x in self.table[key])
	
	def flatten2DList(self, list):
		'''Flattens list of lists into one list.'''
		return [item for sublist in list for item in sublist]	#needs two levels of list comprehension
		
	def list_to_string(self, list):
		'''convert word list to string'''
		return reduce(lambda x, y: x + y, list)
	
if __name__ == '__main__':
	bj = SolBlackjack()
	#bj_solitaire.gameState()	
	bj.play()