#Racko.py
#Author - Brandon Muirhead (no partner)


import random

deck = range(1, 61)
discard = list()



def shuffle(deck):
	'''Shuffles the deck or the discard pile.'''
	random.shuffle(deck)
	
def check_racko(rack):
	'''Checks both the user and computer racks to see if one has achieved Racko.'''

def deal_card(deck):
	'''Gets the top card from the deck'''
	card = deck[1:]
	return [deck[0], card]

def deal_initial_hands():
	'''starts game by dealing two hands of 10 each'''
	comp_hand = [ ]
	user_hand = [ ]
	while len(comp_hand) < 10 and len(user_hand) < 10:
		comp_hand.append(deck.pop())
		user_hand.append(deck.pop())
	return comp_hand, user_hand
	
def does_user_begin():
	'''simulates coin toss to determine who goes first. Heads = user first.'''
	return 'H' if random.random() < 0.5 else 'T'

def print_top_to_bottom(rack):
	'''prints a given rack from slot 10 to slot 1'''
	print rack [::-1]
	

def main():
	'''Main game function'''
	global deck
	global discard
	shuffle(deck)
	comp_hand, user_hand = deal_initial_hands()
	print comp_hand
	print user_hand
	print deck

if __name__ == "__main__":
	main()