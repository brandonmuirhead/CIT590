#makeWebsite.py
#author Brandon Muirhead

def detectName(filename):
	'''Extracts first line from a resume.txt file, checks to ensure first character is A-Z'''
	f = open(filename)
	character = f.read(1)
	print character
	try: 
		character.istitle() == True
	except Exception as value:
		print (value)
		return 'The first line has to be the name with proper capitalization.'
	else:
		f.seek(0)
		name=f.readline()
		name=name.rstrip('\r\n')
		return name
	




if __name__=='__main__':
    print detectName('testresume.txt')