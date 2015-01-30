#numberTheory.py
#program that classifies numbers
#written by Brandon Muirhead, January 2015


from math import sqrt


def main():
	'''Function that evaluates a given number for various number properties.'''
	number = 0
	while number != -1:
		number = input("\nPlease input a number between 1 and 10000. ")
		if number == -1:	#entering -1 is the only way to end the loop
			break
		while isInt(number) is False:
			print 'The number you chose is not an integer.'
			number = input('\nPlease input an integer between 1 and 10000. ')
			if number == -1:
				break
		while number < 1 or number > 10000:
			print 'The number you chose is outside of the acceptable range.'
			number = input("\nPlease input a number between 1 and 10000. ")
			if number == -1:
				break
		
		number = int(number)	#convert to int in case a floating number was input, e.g. 24.0
		
		if isPrime(number): 
			print number, 'is prime,',
		else: 
			print number, 'is not prime,',

		if isComposite(number):
			print 'is composite,',
		else:
			print 'is not composite,',

		if isPerfect(number):
			print 'is perfect,',
		else:
			print 'is not perfect,',

		if isAbundant(number):
			print 'is abundant,',
		else:
			print 'is not abundant,',

		if isTriangular(number):
			print 'is triangular,',
		else:
			print 'is not triangular,',

		if isPentagonal(number):
			print 'is pentagonal,',
		else:
			print 'is not pentagonal,',

		if isHexagonal(number):
			print 'and is hexagonal.'
		else:
			print 'and is not hexagonal.'
	
	print 'End of calculations.'


def isPrime(x):
	'''Determines whether a number is prime. Returns boolean.'''
	if x < 2: return False
	for n in range(2, x):
		if x % n == 0:		
			return False
	return True

def isComposite(x):
	'''Determines whether a number is a composite. Returns boolean.'''
	if x < 2 or isPrime(x) is True:
		return False
	return True

def isPerfect(x):
	'''Determines whether a number is the sum of its factors. Returns boolean.'''
	sum_factor = sumFactor(x)		#calculates the sum of factors of x
	return sum_factor == x
	
def isAbundant(x):
	'''Determines whether a number is abundant. Returns boolean.'''
	sum_factor = sumFactor(x)		#calculates the sum of factors of x
	return sum_factor > x
	
def isTriangular(x):
	'''Determines whether a number is triangular. Returns boolean.'''
	#formula for triangular calc: 0 = n**2 + n - 2x
	if quad_int(1, 1, -2*x):
		return True
	else:
		return False

def isPentagonal(x):
	'''Determines whether a number is pentagonal. Returns boolean.'''
	#formula for pentagonal calc: 0 = 3n**2 - n - 2*x
	if quad_int(3, -1, -2*x):
		return True
	else:
		return False

def isHexagonal(x):
	'''Determines whether a number is hexagonal. Returns boolean.'''
	#formula for hexagonal calc: 0 = 2n**2 - n - x
	if quad_int(2, -1, -1*x):
		return True
	else:
		return False

def quad_int(a, b, c):
	'''Determines if a quadratic equation returns at least one positive integer value.'''
	    #Negative integer values are useful for solving quadratic equations, but do not
	    #make sense for counting the nth triangular / pentagonal / hexagonal term,
	    #as the -4th hexagonal number has no meaning.
	    #a*x**2 + b*x + c = 0	
	
	d = b**2-4*a*c 

	if d < 0:	#no integer solution
		return False
	else:
		plus = (-b + sqrt(d)) / (2*a)
		minus = (-b - sqrt(d)) / (2*a)
	
	if	(isInt(plus) and plus > 0) or (isInt(minus) and minus > 0):		#needs to be both integer and positive
		return True
	else: 
		return False

def isInt(x):
	'''Checks if x is an integer or not. Returns boolean.'''
	return x == int(x)
	
def sumFactor(x):
	'''Sums the factors for a given number.'''
	sum_factor = 0
	for n in range (1, x):
		if x % n == 0:
			sum_factor += n
	return sum_factor

	
if __name__ == "__main__":
	main()


