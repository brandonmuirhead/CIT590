#SolBlackjackTests.py
#author Brandon Muirhead

import unittest
from SolBlackjack import *
from cards import *

class Test_SolBlackjack(unittest.TestCase):

	def setUp(self):
		self.row1 = [Card('K', 'D'), Card(7, 'h'), Card(2, 'd'), Card(6, 's'), Card('J', 'h')]
		self.row2 = [Card('J', 'c'), Card(9, 's'), Card('Q','h'), Card(4, 'c'), Card(10,'d')]
		self.row3 = [Card(9,'s'), Card(8, 's'), Card('A', 'c')]
		self.row4 = [Card(4, 's'), Card('A', 's'), Card(5, 'c')]
		self.discard = [14, 15, 16, 17]
		self.table = {'row1': self.row1, 'row2': self.row2, 'row3': self.row3, 'row4': self.row4, 'discard':self.discard}
		self.game = Blackjack()
	
	def test_gameOver(self):
		over = self.game.gameOver(self.table)
		self.assertTrue(over)
	
	def test_checkErrorMove(self):
		move = self.game.checkErrorMove(2)
		self.assertTrue(move)
	
	def test_getValue(self):
		cardVal1 = self.game.getValue(self.row1[0])
		cardVal2 = self.game.getValue(self.row2[3])
		self.assertEqual(cardVal1, 10)	#Card: KD, value = 10
		self.assertEqual(cardVal2, 4)	#Card: 4C, value = 4		
		self.assertEqual('', '')	#Card = blank	

	#def test_scoreTable(self):
	#	table1 = self.game.scoreTable()
	#	self.assertEqual(table1, 15) 
	
	#def test_card2val(self):
	
	#def test_gameState(self): DO I NEED TO DO THIS TEST?
	
	#def test_processUserMove(self): DO THIS ONE TOO?
	
	#def test_highScore(self):
	
	#def test_flatten2DList(self):
	
	#def test_list_to_string(self):
				
	def test_sumHand(self):
		hand1 = self.game.sumHand(self.row1)
		hand2 = self.game.sumHand(self.row4)
		hand3 = [Card('K', 'd'), Card('a', 'h')]
		hand4 = self.game.sumHand(self.row3)
		self.assertEqual(hand1, 35)
		self.assertEqual(hand2, 20)
		self.assertEqual(self.game.sumHand(hand3), 21)
		self.assertEqual(hand4, 18) 
		
	def test_assignPoints(self):
		hand1 = self.row3
		hand2 = [Card('K', 'd'), Card('A', 'h')]
		total1 = 14
		total2 = 21
		self.assertEqual(self.game.assignPoints(hand1, total1), 1)
		self.assertEqual(self.game.assignPoints(hand2, total2), 10)
		
unittest.main()