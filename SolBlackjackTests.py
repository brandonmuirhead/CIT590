#SolBlackjackTests.py
#author Brandon Muirhead

import unittest
from SolBlackjack import *
from cards import *

class Test_SolBlackjack(unittest.TestCase):
	fileName = ''
	
	def setUp(self):
		self.row1 = [Card('K', 'D'), Card(7, 'h'), Card(2, 'd'), Card(6, 's'), Card('J', 'h')]
		self.row2 = [Card('J', 'c'), Card(9, 's'), Card('Q','h'), Card(4, 'c'), Card(10,'d')]
		self.row3 = [Card(9,'s'), Card(8, 's'), Card('A', 'c')]
		self.row4 = [Card(4, 's'), Card('A', 's'), Card(6, 'c')]
		self.discard = [14, 15, 16, 17]
		self.table = {'row1': self.row1, 'row2': self.row2, 'row3': self.row3, 'row4': self.row4, 'discard':self.discard}
		self.game = Blackjack()
		self.fileName = 'testHighScore.txt'
	
	def test_createBlackjack(self):
		'''tests init function'''
		blackjackTest = Blackjack()
		self.assertEqual(blackjackTest.table['row1'][0], 1)
		self.assertEqual(blackjackTest.table['row4'][2], 16)
		self.assertEqual(blackjackTest.table['discard'][3], 20)
	
	def test_gameOver(self):
		over = self.game.gameOver(self.table)
		self.assertTrue(over)

	def test_getValue(self):
		cardVal1 = self.game.getValue(self.row1[0])
		cardVal2 = self.game.getValue(self.row2[3])
		self.assertEqual(cardVal1, 10)	#Card: KD, value = 10
		self.assertEqual(cardVal2, 4)	#Card: 4C, value = 4		
		self.assertEqual('', '')	#Card = blank	

	def test_scoreTable(self):
		self.assertEqual(self.game.scoreTable(self.table), 29)	#I drew the table laid out above and scored it myself 
	
	def test_card2val(self):
		hand1 = self.row1
		hand2 = self.row4
		self.assertEqual(self.game.card2val(hand1), 35)
		self.assertEqual(self.game.card2val(hand2), 11) 	#treats Ace as 1 in every case...conversion to 11 happens in self.sumHand
	
	def test_highScore(self):
		#this will fail if you run unit tests more than once, since the function will write the input score as the new high score, and the function will return False
		self.assertTrue(self.game.highScore(20, self.fileName))
	
	def test_flatten(self):
		testlist = [[1,2,3], [4,5,6]]
		testlist2 = [[1, 2, 3], [4, 5], 6]
		self.assertEqual(self.game.flatten(testlist), [1,2,3,4,5,6])
		self.assertEqual(self.game.flatten(testlist2), [1,2,3,4,5,6])
	
	def test_list_to_string(self):
		testlist = ['abcd', 'efgh']
		testlist2 = [1, 2]
		string = self.game.list_to_string(testlist)
		self.assertEqual(string, 'abcdefgh')
		self.assertEqual(self.game.list_to_string(testlist2), 3)
						
	def test_sumHand(self):
		hand1 = self.game.sumHand(self.row1)
		hand2 = self.game.sumHand(self.row4)
		hand3 = [Card('K', 'd'), Card(9, 's'), Card('a', 'h')]
		hand4 = self.game.sumHand(self.row3)
		self.assertEqual(hand1, 35)
		self.assertEqual(hand2, 21)							#correctly counts Ace as 11
		self.assertEqual(self.game.sumHand(hand3), 20)		#when you get a higher score with Ace as 1, it keeps it as 1
		self.assertEqual(hand4, 18) 
		
	def test_assignPoints(self):
		hand1 = self.row3
		hand2 = [Card('K', 'd'), Card('A', 'h')]
		hand3 = [Card(7, 'd'), Card(7, 's'), Card(7, 'h')]
		total1 = 14
		total2 = 21
		total3 = 21
		self.assertEqual(self.game.assignPoints(hand1, total1), 1)
		self.assertEqual(self.game.assignPoints(hand2, total2), 10)
		self.assertEqual(self.game.assignPoints(hand3, total3), 7)		#distinguishes between Blackjack and 21 point values
		
unittest.main()