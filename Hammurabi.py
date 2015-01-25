#Hammurabi.py
#A game of strategy, skill, and a little luck.
#written by Brandon Muirhead, January 2015


import random

# Intro message

def print_intro():
	'''This prints the introduction to the game.'''
	print '''\nCongrats, you are the newest ruler of ancient Samaria, elected for a ten 
year term of office. Your duties are to distribute food, direct farming, and 
buy and sell land as needed to support your people. Watch out for rat 
infestations and the resultant plague! Grain is the general currency, 
measured in bushels. The following will help you in your decisions:
	
	* Each person needs at least 20 bushels of grain per year to survive.
	* Each person can farm at most 10 acres of land.
	* It takes 2 bushels of grain to farm an acre of land.
	* The market price for land fluctuates yearly.
		
Rule wisely and you will be showered with appreciation at the end of your term.
Rule poorly and you will be kicked out of office!'''

def Hammurabi():
	'''This is the main game loop.'''
	starved = 0
	immigrants = 5
	population = 100
	harvest = 3000 # total bushels harvested
	bushels_per_acre = 3 # amount harvested for each acre planted
	rats_ate = 200 # bushels destroyed by rats
	bushels_in_storage = 2800
	acres_owned = 1000
	cost_per_acre = 19 # each acre costs this many bushels
	plague_deaths = 0
	
	print_intro()
	
	for year in range(0,11):
                
		print '\nO Great Hammurabi'
		print 'You are in year', year, 'of your ten year rule.'
		print 'In the previous year', starved, 'people starved to death.'
		print 'In the previous year', immigrants, 'people entered the kingdom.'
		print 'The population is now %d.' %population
		print 'We harvested', harvest, 'bushels at', bushels_per_acre, 'bushels per acre.'
		print 'Rats destroyed', rats_ate, 'bushels, leaving', bushels_in_storage, 'bushels in storage.'
		print 'The city owns', acres_owned, 'acres of land.'
		print 'Land is currently worth', cost_per_acre, 'bushels per acre.'
		print 'There were', plague_deaths, 'deaths from the plague.'
			
			
		land_bought = ask_to_buy_land(bushels_in_storage, cost_per_acre)
		if land_bought == 0:
			land_sold = ask_to_sell_land(acres_owned)
		else:
			land_sold = 0

		acres_owned = acres_owned + land_bought - land_sold
		bushels_in_storage = bushels_in_storage - (land_bought - land_sold) * cost_per_acre
		
		bushels_feed = ask_to_feed(bushels_in_storage)
		bushels_in_storage = bushels_in_storage - bushels_feed
		
		acres_planted = ask_to_cultivate(acres_owned, population, bushels_in_storage)
		bushels_in_storage = bushels_in_storage - acres_planted * 2

		plague = isPlague()
		if plague: plague_deaths = population / 2
		else:
			plague_deaths = 0
		population = population - plague_deaths
		
		if numStarving(population, bushels_feed) is None:
			quit()
		else:
			starved = numStarving(population, bushels_feed)
			population = population - starved
			
		immigrants = numImmigrants(acres_owned, bushels_in_storage, population, starved)
		population = population + immigrants
		
		bushels_per_acre = getHarvest()
		harvest = acres_planted * bushels_per_acre
		bushels_in_storage = bushels_in_storage + harvest
		
		rat_prob = random.uniform(0,1)
		if rat_prob > 0.4:
			rats_ate = 0
		else:
			rats_ate = int(round(effectOfRats() * bushels_in_storage))
		
		bushels_in_storage = bushels_in_storage - rats_ate
		
		cost_per_acre = priceOfLand()
	
	finalSummary(starved,acres_owned)
		
		
def ask_to_buy_land(bushels, cost):
	'''Ask user how many bushels to spend buying land. '''
	acres = input("How many acres will you buy? ")
	while acres * cost > bushels:
		print "O great Hammurabi, we have but", bushels, "bushels of grain!"
		acres = input("How many acres will you buy? ")
	return acres
	
def ask_to_sell_land(acres):
	'''Ask user how much land they want to sell. '''
	acres_sell = input("How many acres will you sell? ")
	while acres_sell > acres:
		print "O great Hammurabi, we have but", acres, "acres of land."
		acres_sell = input("How many acres will you sell? ")
	return acres_sell
			
def ask_to_feed(bushels):
	'''Ask user how many bushels they want to use for feeding. '''
	bushels_feed = input("How many bushels of grain will you feed the people? ")
	while bushels_feed > bushels:
		print "O great Hammurabi, we have but", bushels, "bushels of grain."
		bushels_feed = input("How amany bushels of grain will you feed the people? ")
	return bushels_feed

def ask_to_cultivate(acres, population, bushels):
	'''Ask user how much land they want to plant seed in '''
	acres_planted = input("How many acres of land will you plant? ")
	while acres_planted > acres:
		print "O great Hammurabi, we have but", acres, "acres of land."
		acres_planted = input("How many acres of land will you plant? ")
	while acres_planted > population * 10:
		print "O great Hammurabi, we have but", population, "people to plant."
		acres_planted = input("How many acres of land will you plant? ")
	while acres_planted * 2 > bushels:
		print "O great Hammurabi, we have but", bushels, "bushels in storage."
		acres_planted = input("How many acres of land will you plant? ")
	return acres_planted

def isPlague():
	'''Determines if there is a plague this year.'''
	number = random.randint(1,100)
	if number <= 15:
		print '\nThere was a plague this year and half the people died.'
		return isPlague

def numStarving(population, bushels):
	'''Determines the number of people that starve each year.'''
	numStarving = population - (bushels / 20)
	if numStarving <= 0: numStarving = 0
	if numStarving > population * 0.45:
		print '\nYou killed', numStarving, 'people with your mismanagement.'
		if population - numStarving == 0: print 'There is not even a soul left to curse your name.'
		else:
			print 'The people revolt and you are thrown out of office. Game over!'
		return None
	return numStarving
	
def numImmigrants(land, grainInStorage, population, numStarving):
	'''Determines the number of new people who come to the city each year.'''
	if numStarving > 0:
		return 0
	else:
		return (20 * land + grainInStorage)/((100 * population) + 1)

def getHarvest():
	'''Provides the bushels of grain per acre harvested.'''
	rand_number = random.randint(1,8)
	return rand_number
	
def effectOfRats():
	'''This provides the percent of grain destroyed in the event of rat infestation.'''
	rand_number = random.uniform(0.1,0.3)
	return rand_number
	
def priceOfLand():
	'''Determines the price of land in each year.'''
	rand_number = random.randint(16,22)
	return rand_number
	
def finalSummary(starved, acres_owned):
	'''Final messages after completed 10th round based on performance.'''
	print '\nYou have completed your term in office!'
	if starved < 50 and acres_owned > 1500:
		print '\nYou were an historic leader. Monuments have been erected in your likeness!'
	elif starved < 100 and acres_owned > 1000:
		print '\nYou did an average job. Enjoy your retirement.'
	else:
		print '\nYou were not a good leader. May your teeth become wood.'

if __name__ == "__main__":
	Hammurabi()
