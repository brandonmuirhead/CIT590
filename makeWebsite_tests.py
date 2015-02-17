#makeWebsite_tests.py
#author Brandon Muirhead

import unittest
from makeWebsite import *

class Test_makeWebsite(unittest.TestCase):
    fileName = ''
    
    def setUp(self):
        self.fileName = 'testresume.txt'
    
    def test_detect_name(self):
    	name = detectName(self.fileName)
    	self.assertEqual("Brandon K. Muirhead",name)
    	self.assertNotEqual('The first line has to be the name with proper capitalization.',name)
        
        

unittest.main()