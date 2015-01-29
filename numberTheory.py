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
	for i in range(2, x):
		if x % i == 0:		
			return False
	return True

def isComposite(x):
	'''Checks whether or not a number is a composite. Returns boolean.'''
	if x < 2 or isPrime(x) is True:
		return False
	return True

def isPerfect(x):
	'''Determines whether a number is the sum of its factors. Returns boolean.'''
	sum_factor = 0
	if x < 2: return False
	for i in range(1, x):
		if x % i == 0:
			sum_factor += i
	return sum_factor == x
	
def isAbundant(x):
	'''Determines whether a number is abundant. Returns boolean.'''
	sum_factor = 0
	for i in range (1, x):
		if x % i == 0:
			sum_factor += i
	return sum_factor > x
	
def isTriangular(x):
	'''Determines whether a number is triangular. Returns boolean.'''
	

def quad_int(a, b, c):
	'''Determines if a quadratic equation returns at least one integer value.'''
	#a*x**2 + b*x + c = 0	
	
	d = b**2-4*a*c # discriminant

	if d < 0:
		return False
	else: # if d >= 0
		plus = (-b + math.sqrt(d)) / (2*a)
		minus = (-b - math.sqrt(d)) / (2*a)
	
	if	isInt(plus) or isInt(minus):
		return True
	else: 
		return False	

def isInt(x):
	'''Checks if x is an integer or not. Returns boolean.'''
	return x == int(x)

	
if __name__ == "__main__":
	main()


