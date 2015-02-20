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
		self.assertEqual('Programming Languages and Techniques, Statistics, Negotiations', course)
		
	def test_detect_projects(self):
		projects = detectProject(self.fileName)
		self.assertEqual(['Bill.com, Philadelphia, PA - Lead bill collector.', 'Army General - deployed platoon to Arizona where we saved the world.'], projects)

	def test_detect_education(self):
		education = detectEducation(self.fileName)
		self.assertEqual(['University of Penn, Town, PA, USA - Doctor of Coding', 'Brigham Young University, Provo, UT, USA - Bachelor of Pinkberry'], education)

	def test_intro_section(self):
		intro = intro_section(self.fileName)
		self.assertEqual('<div>\r\n<h1>\r\nBrandon K. Muirhead\r\n</h1>\r\n<p>\r\nbmuir@wharton.upenn.edu\r\n</p>\r\n</div>', intro)
		
	def test_edu_section(self):
		edu = edu_section(self.fileName)
		self.assertEqual('<div>\r\n<h2>\r\nEducation\r\n</h2>\r\n<ul>\r\n<li>\r\nUniversity of Penn, Town, PA, USA - Doctor of Coding\r\n</li>\r\n<li>\r\nBrigham Young University, Provo, UT, USA - Bachelor of Pinkberry\r\n</li>\r\n</ul>\r\n</div>', edu)

	def test_proj_section(self):
		proj = proj_section(self.fileName)
		self.assertEqual(proj, '<div>\r\n<h2>\r\nProjects\r\n</h2>\r\n<ul>\r\n<li>\r\n<p>\r\nBill.com, Philadelphia, PA - Lead bill collector.\r\n</p>\r\n</li>\r\n<li>\r\n<p>\r\nArmy General - deployed platoon to Arizona where we saved the world.\r\n</p>\r\n</li>\r\n</ul>\r\n</div>')

	def test_course_section(self):
		course = course_section(self.fileName)
		self.assertEqual(course, '<div>\r\n<h3>\r\nCourses\r\n</h3>\r\n<span>\r\nProgramming Languages and Techniques, Statistics, Negotiations\r\n</span>\r\n</div>')
		
	def test_surround_block(self):
		test = surround_block('div', 'test')
		test2 = surround_block('', 'test')
		self.assertEqual(test, '<div>\r\ntest\r\n</div>')
		self.assertEqual(test2, '<>\r\ntest\r\n</>')

	def test_list_dict_html(self):
		html = list_dict_html(['one', 'two'], 'li', 'div')
		html2 = list_dict_html(['one'], 'li', 'div')
		html3 = list_dict_html(['one', 'two'], 'li', '')
		html4 = list_dict_html(['one', 'two', 'three'], 'li', '')
		html_empty = list_dict_html([], '', '')
		self.assertEqual('<div>\r\n<li>\r\none\r\n</li>\r\n</div>\r\n<div>\r\n<li>\r\ntwo\r\n</li>\r\n</div>', html)
		self.assertEqual('<div>\r\n<li>\r\none\r\n</li>\r\n</div>', html2)
		self.assertEqual('<li>\r\none\r\n</li>\r\n<li>\r\ntwo\r\n</li>', html3)
		self.assertEqual('', html_empty)
		self.assertEqual('<li>\r\none\r\n</li>\r\n<li>\r\ntwo\r\n</li>\r\n<li>\r\nthree\r\n</li>', html4)
			
	def test_cleanList(self):
		clean = cleanList(['foo\r', 'bar\r\n', '', 'foobar'])
		self.assertEqual(['foo', 'bar', 'foobar'], clean)
		self.assertEqual([], cleanList([]))
		
	def test_check_ed(self):
		edu = checkEd(self.fileName, 'Doctor')
		self.assertEqual('University of Penn, Town, PA, USA - Doctor of Coding\n', edu)
	
	def test_combine(self):
		combine = combine_html('html1', 'html2')
		self.assertEqual('html1\r\nhtml2', combine)
		
	def test_tie_body_header(self):
		header = tie_body_header('<h2>\r\nEducation\r\n</h2>', 'One, Two', 'div')
		self.assertEqual(header, '<div>\r\n<h2>\r\nEducation\r\n</h2>\r\n<div>\r\nOne, Two\r\n</div>\r\n</div>')
	

unittest.main()