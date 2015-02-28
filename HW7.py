#HW7.py
#author Brandon Muirhead


#Question 1
def sameAB(abstring):
	'''tests whether string has same number of a's and b's'''
	newstring = abstring[:]
	
	if newstring[0] == newstring[-1]:
		return len(newstring) == len(abstring)/2 
	return sameAB(newstring[1:])
	

#Question 2
def binary_search(lst, val):
	'''given a sorted list of integers, determines if a value is in the list'''
	if lst == []:													#recursion eventually gives an empty list if val not in list
		return False
	mid = lst[len(lst)/2]											#find middle element in list
	if val == mid:
		return True
	elif val < mid:
		return binary_search([x for x in lst if x < mid], val)		#get items in list less than mid point
	elif val > mid:
		return binary_search([x for x in lst if x > mid], val)		#get items in list greater than mid point


#Question 3
def flatten(lst):
	'''takes a list of lists and flattens to a 1D list'''
	if lst == []:													#base case returns empty list
		return lst
	if isinstance(lst[0], list):									#tests to see if element is a list
		return flatten(lst[0]) + flatten(lst[1:])					#if first element is a list, still need to check rest of list
	else:
		return lst[:1] + flatten(lst[1:])							#uses [:1] to return first element as a list. Second part returns empty list if list only has 1 element.
	

#Question 4
def initials(lst):
	'''creates list of initials of strings passed in as names.'''
	return [name.split()[0][0] + '.' + name.split()[1][0] + '.' for name in lst]


#Question 5
def meamers(filename):
	'''Counts number of MEAM students in a file.'''
	with open(filename, 'r') as f:
		lines = [line for line in f]								#puts rows into a list
		return len([x for x in lines if 'MEAM' in x])				#makes a list of mentions of 'MEAM' and gives # of occurrences



#Question 6
def most_frequent_alphabet(frequency_dictionary):
	'''Returns the letter that appears the most times in a dictionary'''
	dlist = frequency_dictionary.items()							#dictionary to list of k,v pairs
	high = reduce((lambda a,b: a if (a[1] > b[1]) else b), dlist)	#returns k,v pair with highest frequency
	return [a[0] for a in dlist if a[1] == high[1]]					#returns all letters with the high frequency



if __name__ == '__main__':
	s = {'a':2, 'b':6, 'c':40, 'd':40, 'e':5}
	print most_frequent_alphabet(s)