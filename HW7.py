#HW7.py
#author Brandon Muirhead


#Question 1
def sameAB(abstring):
	'''tests whether string has same number of a's and b's'''
	if len(abstring) == 0:											#base case
		return True
	if abstring[0] == abstring[-1]:
		return False
	return sameAB(abstring[1:-1])

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
	else: 
		return binary_search([x for x in lst if x > mid], val)		#get items in list greater than mid point

#Question 3
def flatten(lst_of_lst):
	'''takes a list of lists and flattens to a 1D list'''
	if lst_of_lst == []:											#base case returns empty list
		return lst_of_lst
	if isinstance(lst_of_lst[0], list):								#tests to see if element is a list
		return flatten(lst_of_lst[0]) + flatten(lst_of_lst[1:])		#if first element is a list, still need to check rest of list
	else:
		return lst_of_lst[:1] + flatten(lst_of_lst[1:])				#uses [:1] to return first element as a list. Second part returns empty list if list only has 1 element.

#Question 4
def initials(lst):
	'''creates list of initials of strings passed in as names'''
	return [name.split()[0][0] + '.' + name.split()[-1][0] + '.' for name in lst]

#Question 5
def meamers(filename):
	'''counts number of MEAM students in a file.'''
	with open(filename, 'r') as f: return len([x for x in [line for line in f] if 'MEAM' in x])

#Question 6
def most_frequent_alphabet(frequency_dictionary):
	'''returns the letter that has the highest frequency from a dictionary'''
	return [a[0] for a in frequency_dictionary.items() if a[1] == reduce(lambda a,b: a if a[1] > b[1] else b, frequency_dictionary.items())[1]]


if __name__ == '__main__':


##	print sameAB('aaabb')
##	print binary_search([1,2,3,4,5], 2)
##	print flatten([1,1,[1,1,[1]],1,[1,1,[1,[1,[],1]]]])
##	print initials(['Brandon Muirhead', 'Jenni Sue Muirhead', 'Dave Duck'])
##	print meamers('Names.csv')
##	print most_frequent_alphabet({'a':3, 'b':5, 'c':12, 'd':12})