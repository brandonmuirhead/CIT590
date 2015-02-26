import random  # needed for shuffling a Deck

class Card(object):
	
	def __init__(self, r, s):
		self.r = r
		self.s = s
		
	def __str__(self):
		'''Print the rank and suit of a card.'''
		return str(self.r) + self.s
		
	def get_rank(self):
		'''Returns rank of card.'''
		return self.r
	
	def get_suit(self):
		'''Returns suit of card.'''
		return self.s
		
class Deck():
	
	def __init__(self):
		'''Initializes deck as a list of all 52 cards: 13 cards in each of 4 suits'''
		rank = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
		suit = ['S', 'C', 'H', 'D']
		self.__deck = []
		
		for i in rank:
			for j in suit:
				card = Card(i, j)	#create card with each suit for every rank
				self.__deck.append(card)
	
	def shuffle(self):
		'''Shuffle the deck'''
		random.shuffle(self.__deck)
		return self.__deck
		
	def get_deck(self):
		return self.__deck
		
	def deal(self):
		return self.__deck.pop()
		
	def __str__(self):
		'''Represents the whole deck as a string for printing'''
		deck = self.get_deck()
		stringList = ''
		count = 0
		for card in deck:
			deck[count] = str(card)		#converts card objects in list to strings
			count += 1
		for j in deck:
			stringList += j + '\n'		#prints strings on new rows
		return stringList 

def main():
	deck1 = Deck()
	deck1.shuffle()
	print deck1

	 


if __name__ == '__main__':
	main()
