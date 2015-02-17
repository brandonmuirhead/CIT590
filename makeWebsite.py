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
		name=f.readline()
		name=name.rstrip('\r\n')
		return name
	




if __name__=='__main__':
    print detectName('testresume.txt')