#makeWebsite.py
#author Brandon Muirhead



import string

def main():
	'''Function that creates an html file from a text resume.'''
	f = open('resume.html', 'r+')
	lines = f.readlines()
	f.seek(0)
	f.truncate()
	del lines[-1]
	del lines[-1]
	f.writelines(lines)
	f.write('<div id="page-wrap">')		#resume ready to insert text from .txt file

	text = 'resume.txt'
	intro = intro_section(text)
	edu = edu_section(text)
	proj = proj_section(text)
	courses = course_section(text)
	
	f.write(intro)
	f.write('\r\n')
	f.write(edu)
	f.write('\r\n')
	f.write(proj)
	f.write('\r\n')
	f.write(courses)
	f.write('\r\n')	
	f.write('</div>\r\n</body>\r\n</html>')
	
	f.close()
	
	print 'Resume complete.'

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
	courses = courses.lstrip('Courses ')
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
	projList = cleanList(projList)
	return projList

def detectEducation(filename):
	'''Extracts lines from a file with information about schools and degrees earned.'''
	ed1 = checkEd(filename, 'Doctor')
	ed2 = checkEd(filename, 'Master')
	ed3 = checkEd(filename, 'Bachelor')	
	education = [ed1, ed2, ed3]			#combines all degrees into a list
	education = cleanList(education)	#removes any empty strings 
	return education	#returns list

def intro_section(fileName):
	'''Creates html code for intro section of resume.'''
	nameText = detectName(fileName)
	htmlName = surround_block('h1', nameText)	#name section of html
	
	emailText = detectEmail(fileName)
	htmlEmail = surround_block('p', emailText)	#email section of html
	
	combine = combine_html(htmlName, htmlEmail)
	
	intro = surround_block('div', combine)
	return intro

def edu_section(fileName):
	'''Creates html code for education section of resume.'''
	header = surround_block('h2', 'Education')
		
	education = detectEducation(fileName)
	edu1 = education[0]
	edu2 = ''
	edu3 = ''
	if len(education) > 1:
		edu2 = education[1]		#fills in edu2 if there are two degrees in file
	if len(education) > 2:
		edu3 = education[2]		#fills in edu3 if there are three degrees in file

	edulist = [edu1, edu2, edu3]
	edulist = cleanList(edulist)	
	edulist = list_dict_html(edulist, 'li', '')

	fullEdu = tie_body_header(header, edulist, 'ul')
	return fullEdu		#html text

def proj_section(fileName):
	'''Creates html code for projects section of resume.'''
	header = surround_block('h2', 'Projects')
	projlist = detectProject(fileName)
	projlist = list_dict_html(projlist, 'p', 'li')	
	fullproj = tie_body_header(header, projlist, 'ul')
	return fullproj		#html text

def course_section(fileName):
	'''Creates html code for course section of resume.'''
	header = surround_block('h3', 'Courses')
	courselist = detectCourse(fileName)
	fullcourse = tie_body_header(header, courselist, 'span')
	return fullcourse	#html text
	
def surround_block(tag, text):
	'''surrounds some text in html block'''
	html = '<' + tag + '>\r\n' + text + '\r\n</' + tag + '>'
	return html	
	
def list_dict_html(list, innertag, outertag):
	'''creates desired html with 1-2 tags from given list.'''
	d = {}
	clean = ''
	count = 1
	for x in list:
		d[count] = surround_block(innertag, x)		#using dict lets me assign values to list in for loop
		count += 1
	
	if len(d) == 1:
		if outertag == '':							#just in case I want to put two tags before the text
			clean = d[1]
		else: 
			clean = surround_block(outertag, d[1])
	else: 
		for i in range(1, len(d)+1):			#this is for a list with more than one item
			if outertag != '':	
				d[i] = surround_block(outertag, d[i])	#puts the second tag on both list items
		for i in range(1, len(d)):	
			clean = combine_html(d[i], d[i+1])	#combines everything into one html block
			d[i+1] = clean
	return clean

def cleanList(list):
	'''Removes '\r\n' and extra whitespace from a list.'''
	clean = string.maketrans("", "")
	list = [s.translate(clean, "\r\n") for s in list]	#removes '\r\n' from list
	list = filter(None, list)	#removes empty strings from list
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

def combine_html(html1, html2):
	'''Combines two strings	of html into one.'''
	combine = html1 + '\r\n' + html2
	return combine

def tie_body_header(header, body, bodytag):
	'''Ties together header and body for each section of resume.'''
	section1 = surround_block(bodytag, body)
	full = combine_html(header, section1)
	fullhtml = surround_block('div', full)
	return fullhtml

if __name__ == "__main__":
	main()