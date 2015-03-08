#SolBlackjack.py
#author Brandon Muirhead


from cards import *

class Blackjack():
	
	def __init__(self):
		self.table = {}
		self.table['row1'] = [1, 2, 3, 4, 5]
		self.table['row2'] = [6, 7, 8, 9, 10]
		self.table['row3'] = [11, 12, 13]
		self.table['row4'] = [14, 15, 16]
		self.table['discard'] = [17, 18, 19, 20]
		
	def play(self):
		deck = Deck()
		deck.shuffle()
		print '\nWelcome to Solitaire Blackjack. You can choose where to place the top card in the deck.\n'
		self.table['row1'] = [1, 2, 3, 4, 5]				#have to repeat this to reset the table for each round of playing
		self.table['row2'] = [6, 7, 8, 9, 10]
		self.table['row3'] = [11, 12, 13]
		self.table['row4'] = [14, 15, 16]
		self.table['discard'] = [17, 18, 19, 20]
		
		while not self.gameOver(self.table):
			self.gameState()
			card = deck.deal()
			print 'The top card on the deck is: ', card
			move = self.acceptUserMove()
			self.processUserMove(move, card)
		
		self.gameState()
		print 'Game complete. Your score is being calculated.'
		print 'Your score is: ',
		score = self.scoreTable(self.table)
		print score
		self.highScore(score, 'highScore.txt')
		print 'Thanks for playing!'
		self.restart()										#gives option to restart or ends game
	
	def scoreTable(self, table):
		hand1 = [table['row1'][0], table['row2'][0]]
		hand2 = [table['row1'][1], table['row2'][1], table['row3'][0], table['row4'][0]]
		hand3 = [table['row1'][2], table['row2'][2], table['row3'][1], table['row4'][1]]
		hand4 = [table['row1'][3], table['row2'][3], table['row3'][2], table['row4'][2]]
		hand5 = [table['row1'][-1], table['row2'][-1]]
		hand6 = table['row1']
		hand7 = table['row2']
		hand8 = table['row3']
		hand9 = table['row4']
		
		scoretable = [hand1, hand2, hand3, hand4, hand5, hand6, hand7, hand8, hand9]
		sums = [self.sumHand(x) for x in scoretable]
		points = [self.assignPoints(x,y) for x,y in zip(scoretable, sums)]	#gets the points for every hand / total pair
		return sum(points)
	
	def sumHand(self, hand):
		'''Scores a single hand. Hands can be 2, 3, 4, or 5 cards.'''	
		check_for_ace = [True for card in hand if card.get_rank() == 'A']
		if check_for_ace:
			altList = []									#creates a new list 
			count = 0
			for i in hand:
				if hand[count].get_rank() != 'A':		
					altList.append(hand[count])				#Adds only cards that are not Aces
				count += 1
			hand_val = self.assignPoints(hand, self.card2val(hand))
			altList_val = self.assignPoints(altList, self.card2val(altList)+11)	#adds 11 to the list where the Ace is missing
			if hand_val > altList_val:						#compares the scores for the lists with A=1 and A=11
				return self.card2val(hand)					#returns the hand which has a higher point score
			else: return self.card2val(altList) + 11		#adds 11 to the count
		else:
			return self.card2val(hand)						#if no Aces, totals the score for the hand
	
	def card2val(self, hand):
		'''Converts cards objects in a hand into a sum of the values of those cards'''
		return reduce(lambda x, y: x + y, [self.getValue(x) for x in hand])		
		
	def assignPoints(self, hand, total):
		'''Given a hand total, assigns points to the hand'''
		points = {'Blackjack':10, 21:7, 20:5, 19:4, 18:3, 17:2, '16_or_less':1, 'Bust':0}
		if len(hand) == 2 and total == 21:
			return points['Blackjack']
		if total > 21:
			return points['Bust']
		elif total <= 16:
			return points['16_or_less']
		else:
			return points[total]
		
	def getValue(self, card):	
		'''Returns a value for any given card'''
		values = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':1}
		cardRank = card.get_rank()
		return values[cardRank]
	
	def gameState(self):		#no unit test because it just prints statements but doesn't actually return anything
		'''Visually represents the current state of the game with four rows and the discard pile'''
		listHand = [[str(x) + '\t' for x in self.table[key]] for key in self.table]		#converts values for the table into strings one tab apart, each in a list
		gameState = self.flatten(listHand)					#flattens list of lists

		row1 = gameState[0:5]								#creates string of characters in shape of game
		row1 = self.list_to_string(row1)
		row2 = gameState[5:10]
		row2 = self.list_to_string(row2)
		row3 = gameState[10:13]
		row3 = self.list_to_string(row3)
		row4 = gameState[13:16]
		row4 = self.list_to_string(row4)
		row5 = gameState[16:21]
		row5 = self.list_to_string(row5)
		
		print '\n\n\n\n\n\n\n\n\n\n\n\n\n\nTable: '			#I like to see only the current table/discard pile, so I added a bunch of spaces between each new card draw
		print row1 + '\n' + row2 + '\n\t' + row3 + '\n\t' + row4
		print '\nDiscard Pile: '
		print row5 + '\n'
	

	def acceptUserMove(self):	#no unit test for this because all it does is takes user input and calls a new function
		'''Asks user to specify a move location, then checks to ensure input is acceptable'''
		move = raw_input('Please indicate the position in which you would like to place this card: ')
		return self.checkErrorMove(move)
		
	def checkErrorMove(self, move):
		'''Checks a user's move for errors in input'''
		question = False
		while question == False:
			try:
				val = int(move)													#if a non-integer input is given, raises exception
				if int(move) not in range(1,21):								#only accepts input of integers in range 
					print 'Please enter a number corresponding with slots 1-20'
					move = raw_input('Please indicate the position in which you would like to place this card: ')
				elif int(move) not in self.flatten(self.table.values()): 		#checks if user choice is already a card	
					print 'You chose a position that is already filled.'
					move = raw_input('Please indicate the position in which you would like to place this card: ')
				else:
					question = True
			except ValueError:
				print("You did not enter a number. Please enter a number between 1-20.")
				move = raw_input('Please indicate the position in which you would like to place this card: ')
		return int(move)

	def processUserMove(self, location, card):
		'''Takes move which has been error checked and executes the move'''
		if location in range(1,6):
			self.table['row1'][location - 1] = card			#card is Card object
		elif location in range(6, 11):
			self.table['row2'][location - 6] = card 
		elif location in range(11, 14):
			self.table['row3'][location - 11] = card
		elif location in range(14, 17):
			self.table['row4'][location - 14] = card
		else:
			self.table['discard'][location - 17] = card

	def gameOver(self, table):
		'''Checks to see if all 16 spots on the table are filled with card objects'''
		count = 0
		for key in sorted(table)[1:]:											#doesn't count the discard row, only the table rows
			if all(isinstance(x, Card) for x in table[key] if 'row' in key):	#checks to see if every place has a card object
				count += 1
		if count == 4:
			return True
		else:
			return False

	def highScore(self, score, filename):
		'''checks game score to see if it is high score'''
		with open(filename, 'r+') as f:
			if score > int(f.readlines()[0]):
				f.seek(0)
				f.writelines(str(score))
				print '\n##########################################\nCongratulations! You got a new high score!\n##########################################' 
				return True														#returns boolean for unit testing purposes
			else: return False													#doesn't show up on user interface

	def restart(self):
		restart = raw_input('\nWould you like to play another game? (enter 1 for "Yes" or 0 for "No") ')
		loop = False
		while loop == False:
			try:
				val = int(restart)
				if int(restart) == 0:
					print '\nGame over.'
					loop = True
				elif int(restart) == 1: 
					loop = True
					self.play()
				else: 
					print 'Please enter either 1 or 0.'
					restart = raw_input('\nWould you like to play another game? (enter 1 for "Yes" or 0 for "No") ')
			except ValueError:
				print 'You did not enter either 1 or 0.'
				restart = raw_input('\nWould you like to play another game? (enter 1 for "Yes" or 0 for "No") ')
			
	def flatten(self, lst_of_lst):
		'''Flattens list of lists into one list.'''
		if lst_of_lst == []:													#base case returns empty list
			return lst_of_lst
		if isinstance(lst_of_lst[0], list):										#tests to see if element is a list
			return self.flatten(lst_of_lst[0]) + self.flatten(lst_of_lst[1:])	#if first element is a list, still need to check rest of list
		else:
			return lst_of_lst[:1] + self.flatten(lst_of_lst[1:])				#uses [:1] to return first element as a list. Second part returns empty list if list only has 1 element.
		
	def list_to_string(self, list):
		'''convert word list to string'''
		return reduce(lambda x, y: x + y, list)
		
def main():
	'''Main function for this program'''
	bj_solitaire = Blackjack()
	bj_solitaire.play()

	
if __name__ == '__main__':
	main()