#cards_tests.py
#author Brandon Muirhead

import unittest
from cards import *

class Test_cards(unittest.TestCase):

	def setUp(self):
		self.card1 = Card(2, 'C')
		self.card2 = Card('A', 'H')
		self.card3 = Card(10, 'D')
		self.deck1 = Deck()
	
	def test_Creation(self):
		'''tests the init method'''
		self.assertEqual(str(self.card1), str(Card(2, 'C')))
		self.assertEqual(str(self.card2), str(Card('A', 'H')))
		
	def test_printCard(self):
		self.assertEqual(str(self.card1), '2C') 
	
	def test_Rank(self):
		self.assertEqual(self.card1.r, 2)
		self.assertEqual(self.card3.r, 10)
		
	def test_Suit(self):
		self.assertEqual(self.card2.s, 'H')
		self.assertEqual(self.card3.s, 'D')

	def test_deck_Creation(self):
		'''tests init method for deck. Also tests the __str__ function'''
		self.assertEqual(str(self.deck1), 'AS\nAC\nAH\nAD\n2S\n2C\n2H\n2D\n3S\n3C\n3H\n3D\n4S\n4C\n4H\n4D\n5S\n5C\n5H\n5D\n6S\n6C\n6H\n6D\n7S\n7C\n7H\n7D\n8S\n8C\n8H\n8D\n9S\n9C\n9H\n9D\n10S\n10C\n10H\n10D\nJS\nJC\nJH\nJD\nQS\nQC\nQH\nQD\nKS\nKC\nKH\nKD\n')
	
	def test_shuffleDeck(self):
		self.assertNotEqual(str(self.deck1), str(self.deck1.shuffle()))
	
	#def test_getDeck(self):
	#	self.new_deck = Deck()
	#	self.assertEquals(str(self.new_deck), str(self.new_deck.get_deck()))

	def test_dealDeck(self):
		self.assertEqual(str(self.deck1.deal()), 'KD')


unittest.main()