#Racko.py
#Author - Brandon Muirhead (no partner)


import random

deck = range(1, 61)
discard = list()

def main():
	'''Main game function'''
	global deck
	global discard
	shuffle(deck)
	comp_hand, user_hand = deal_initial_hands()
	discard.append(deck.pop())
	print "\nWelcome to Racko! We'll start by seeing who goes first."

	userStarts = does_user_begin()
	
	while check_racko(comp_hand) == False and check_racko(user_hand) == False:
		print '\nYour turn. Here is your rack:'
		print ''
		print_top_to_bottom(user_hand)
		print '\nTop card on discard pile is', str(discard[-1]).strip('[]')
		print '\nWould you like to take from the discard pile or draw from the deck?'
		question = False
		while question == False:
			answer = raw_input('Input "discard" or "deck": ')
			if answer == 'discard':
				dis_card = discard.pop()
				take_turn(dis_card, user_hand)
				print ''
				print_top_to_bottom(user_hand)
				question = True
			elif answer == 'deck':
				card = deal_card(deck)
				print 'You drew:', str(card)
				secondChoice = raw_input('Do you want to keep it? (Type "y" or "n"): ')
				if secondChoice == 'y':
					take_turn(card, user_hand)
					print_top_to_bottom(user_hand)
					question = True
				else:
					add_card_to_discard(card)
					print ''
					print_top_to_bottom(user_hand)
					question = True	
			else: 
				print 'You typed something other than "discard" or "deck". Please try again.'
		
		print "\nComputer's turn."
		comp_hand = computer_play(comp_hand)
		
		if sum(deck) == 0:
			print '\nNo more cards in the deck. Shuffling the discard pile.'
			shuffle(discard)
			extend.deck(discard)
			discard = [ ]
		
	if check_racko(comp_hand):
		print '\nYou win! Congratulations!'
	else:
		print '\nComputer wins. Better luck next time.'
			
def take_turn(newCard, hand):
	'''follows player's choice of which card to use. User replaces a card in rack with chosen card.'''
	cardToBeReplaced = input('Which card would you like to replace from your rack? (Enter number): ')
	while cardToBeReplaced not in hand:
		print 'You entered a number not in your current rack.'
		cardToBeReplaced = input('Which card would you like to replace from your rack? (Enter number): ')
	find_and_replace(newCard, cardToBeReplaced, hand)				

def shuffle(deck):
	'''Shuffles the deck or the discard pile.'''
	random.shuffle(deck)
	
def check_racko(rack):
	'''Checks both the user and computer racks to see if one has achieved Racko.'''
	win = True
	for i in range (1,11):
		if(rack[i-1] > rack[i]):
			win = False
			break
	return win

def deal_card(deck):
	'''Gets the top card from the deck and places it on the top of the discard pile'''
	return deck.pop()

def deal_initial_hands():
	'''starts game by dealing two hands of 10 each'''
	comp_hand = [ ]
	user_hand = [ ]
	while len(comp_hand) < 10 and len(user_hand) < 10:
		comp_hand.append(deck.pop())		#takes card from deck and places into computer rack first
		user_hand.append(deck.pop())		#takes card from deck and places into user rack
	return comp_hand, user_hand
	
def does_user_begin():
	'''simulates coin toss to determine who goes first. Heads (True) = user first.'''
	return True if random.random() < 0.5 else False

def print_top_to_bottom(hand):
	'''prints a given rack from slot 10 to slot 1'''
	print "\n".join(str(x) for x in hand)

def find_and_replace(newCard, cardToBeReplaced, hand):
	'''finds the card to be replaced in the hand and replaces it with a new card.'''
	position = hand.index(cardToBeReplaced)
	hand[position] = newCard
	discard.append(cardToBeReplaced)
	
def add_card_to_discard(card):
	'''adds a card to the top of discard pile.'''
	discard.append(card)

def computer_play(hand):
	'''Computer takes a turn.'''
	len1 = len(discard)		#checks length of discard
	card1 = discard[-1]	
	comp_algo(card1, hand)
	len2 = len(discard)		#checks len of discard to see if card has been added bc of fit in comp_algo
	if len2 > len1:
		discard.remove(card1)
	
	return hand
	
def comp_algo(card, hand):
	'''Computer evaluates a given number against its rack'''
	a = range(1,7)		#split range of 1-60 into 10
	b = range(7,13)
	c = range(13,19)
	d = range(19,25)
	e = range(25,31)
	f = range(31,37)
	g = range(37,43)
	h = range(43,49)
	i = range(49,55)
	j = range(55,61)
	
	if card in a:	#for each range, checks to see if newCard is in range
		if hand[9] not in a:		#computer keeps card if it already has card in that range
			find_and_replace(card, hand[9], hand)	#otherwise it accepts the new card
		else: return None
	elif card in b:
		if hand[8] not in b:
			find_and_replace(card, hand[8], hand)
		else: return None
	elif card in c:
		if hand[7] not in c:
			find_and_replace(card, hand[7], hand)
		else: return None
	elif card in d:
		if hand[6] not in d:
			find_and_replace(card, hand[6], hand)
		else: return None
	elif card in e:
		if hand[5] not in e:
			find_and_replace(card, hand[5], hand)
		else: return None
	elif card in f:
		if hand[4] not in f:
			find_and_replace(card, hand[4], hand)
		else: return None
	elif card in g:
		if hand[3] not in g:
			find_and_replace(card, hand[3], hand)
		else: return None
	elif card in h:
		if hand[2] not in h:
			find_and_replace(card, hand[2], hand)
		else: return None
	elif card in i:
		if hand[1] not in i:
			find_and_replace(card, hand[1], hand)
		else: return None
	else:
		if hand[0] not in j:
			find_and_replace(card, hand[0], hand)
		else: return None
			
				

if __name__ == "__main__":
	main()