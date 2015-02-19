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
		#self.assertRaises(RuntimeError, detect_name("inasdf"))
			
	def test_detect_email(self):
		email = detectEmail(self.fileName)
		self.assertEqual('bmuir@wharton.upenn.edu', email)
		self.assertNotEqual('Bmuir@wharton.upenn.edu', email)	#doesn't seem like the right test here. trying to test the first character not being capitalized
		self.assertNotEqual('bmuir@wharton.upenn.EDU', email)
    	
	def test_detect_courses(self):
		course = detectCourse(self.fileName)
		self.assertEqual('Courses Programming Languages and Techniques, Statistics, Negotiations', course)
		
	def test_detect_projects(self):
		projects = detectProject(self.fileName)
		self.assertEqual(['Bill.com, Philadelphia, PA - Lead bill collector.', 'Army General - deployed platoon to Arizona where we saved the world.'], projects)

	def test_detect_education(self):
		education = detectEducation(self.fileName)
		self.assertEqual('University of Penn, Town, PA, USA - Doctor of Coding', education)

	def test_remove_rn(self):
		remove = remove_rn(['foo\r', 'bar\r\n', 'foobar'])
		self.assertEqual(['foo', 'bar', 'foobar'], remove)
		self.assertEqual([], remove_rn([]))
		
	def test_check_ed(self):
		edu = checkEd(self.fileName, 'Doctor')
		self.assertEqual('University of Penn, Town, PA, USA - Doctor of Coding\r\n', edu)
		
		
unittest.main()