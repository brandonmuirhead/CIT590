#numberTheory.py
#program that classifies random numbers
#written by Brandon Muirhead, January 2015


from math import sqrt
import random


def main():
	'''Function that evaluates a given number for various number tests.'''
	number = input("Please input a number between 1 and 10000. ")
	if number == -1:
		quit()
	while isInt(number) is False:
		print 'The number you chose is not an integer.'
		number = input('Please input an integer between 1 and 10000. ')
		if number == -1:
			quit()
	while number < 1 or number > 10000:
		print 'The number you chose is outside of the acceptable range.'
		number = input("Please input a number between 1 and 10000. ")
		if number == -1:
			quit()
	
	if isPrime(number): 
		print number, 'is prime, '
	else: 
		print number, 'is not prime, '

	if isComposite(number):
		print 'is composite, '
	else:
		print 'is not composite, '

def isPrime(x):
	'''Checks whether or not an inputted number is prime. Returns boolean.'''
	if x < 2: return False
	for n in range(2,int(round(sqrt(x)))):		#only need to go up to sqrt(x) since if there exists a number
		if x % n == 0:							#p > sqrt(x) that divides x, then there must also be a number 
			return False						#q = x / p which also divides x, and q < sqrt(x)
	return True

def isComposite(x):
	'''Checks whether or not a number is a composite. Returns boolean.'''
	if x < 2 or isPrime(x) is True:
		return False
	return True
	
def isInt(x):
	'''Checks if x is an integer or not. Returns boolean.'''
	return x == int(x)

	
if __name__ == "__main__":
	main()


