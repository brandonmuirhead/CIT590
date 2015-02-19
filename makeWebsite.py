#makeWebsite.py
#author Brandon Muirhead

import string

def detectName(filename):
	'''Extracts first line from a resume.txt file, checks to ensure first character is A-Z'''
	f = open(filename)
	character = f.read(1)
	try: 
		if character not in string.ascii_uppercase:
			raise RuntimeError 
	except RuntimeError:
		return 'The first line has to be the name with proper capitalization.'
	else:
		f.seek(0)
		name = f.readline()
		name = name.rstrip('\r\n')
		f.close()
		return name
	
def detectEmail(filename):
	'''Extracts email address from a text file. Only allows .com and .edu endings.'''
	f = open(filename)
	emailLine = ''
	for line in f:
		# check for '@' and '.edu' or '.com' in the line
		if all(char in line for char in '@.edu') or all(char in line for char in '@.com'):
			emailLine = line.rstrip('\r\n')
	f.close()
	if emailLine[:1] in string.ascii_lowercase:		#checks first character to make sure it is lowercase
		return emailLine

def detectCourse(filename):
	'''Extracts course list from resume text file.'''
	f = open(filename)
	course = ''
	for line in f:
		if 'Course' in line:
			course = line.rstrip('\r\n')
	f.close()
	courses = course.translate(None, '!?./;-:')	#removes any punctuation except commas
	courses = " ".join(courses.split())	#gets rid of extra whitespace
	return courses	#string

def detectProject(filename):
	'''Extracts projects from resume text file.'''
	fileList = []
	projList = []
	f = open(filename, 'r')
	for line in f:
		fileList.append(line)	#convert file to list
	f.close()
	index = fileList.index('Projects\n')
	while fileList[index+1][:10] != str("----------"):
		projList.append(fileList[index+1])
		index += 1
	print projList
	projList = remove_rn(projList)	#remove \r\n endings
	projList = filter(None, projList)	#remove empty strings from list
	return projList

def detectEducation(filename):
	'''Extracts lines from a file with information about schools and degrees earned.'''
	ed1 = checkEd(filename, 'Bachelor')
	ed2 = checkEd(filename, 'Master')
	ed3 = checkEd(filename, 'Doctor')	
	education = ed1 + ed2 + ed3
	education = education.rstrip(' \r\n')
	return education

def remove_rn(list):
	'''Removes '\r\n' and similar endings from a list'''
	clean = string.maketrans("", "")
	list = [s.translate(clean, "\r\n") for s in list]
	return list	

def checkEd(file, degree):
	'''Loops through file and checks for specific degree.'''
	f = open(file)
	education = ''
	for line in f:
		if 'University' in line and degree in line:
			education += line
	f.close()
	return education

		
if __name__ == "__main__":
	print detectEducation('testresume.txt')