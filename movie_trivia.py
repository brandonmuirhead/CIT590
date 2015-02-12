#use these first 2 functions to create your 2 dictionaries
import csv
def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()
        actorAndMovies = line.split(',')
        actor = actorAndMovies[0]
        movies = [x.lstrip().rstrip() for x in actorAndMovies[1:]]
        movieInfo[actor] = set(movies)
    f.close()
    return movieInfo

def create_ratings_DB(ratings_file):
    '''make a dictionary from the rotten tomatoes csv file'''
    scores_dict = {}
    with open(ratings_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            scores_dict[row[0]] = [row[1], row[2]]
    return scores_dict

def insert_actor_info(actor, movies, movie_Db):
	'''Inserts or updates info for a given actor.'''
	if actor not in movie_Db:
		movie_Db[actor] = set(movies)	#adds actor if not already in database
	else: movie_Db[actor].update(movies)	#appends new movies to actor's list
	
def insert_rating(movie, ratings, ratings_Db):
	'''Inserts or updates a movie rating.'''
	ratings_Db[movie] = ratings

def delete_movie(movie, movie_Db, ratings_Db):
	'''Deletes all information from the databases related to a given movie.'''
	del ratings_Db[movie]	#deletes from the ratings database
	########Need to find how to get key from value, then delete value using set.remove(item)
			
def select_where_actor_is(actorName, movie_Db):
	'''Given an actor, return list of all movies.'''
	return list(movie_Db[actorName])	#converts set of movies to list and returns list
	
def select_where_movie_is(movieName, movie_Db):
	'''Given a movie, returns list of all actors.'''
	#########How do you return key given value?

def select_where_rating_is(targeted_rating, comparison, is_critic, ratings_Db):
	'''Returns list of movies that satisfy a set of conditions.'''
	
	
	
def get_co_actors(actorName, moviedb):
	'''Returns a list of all actors that actor has worked with in any movie.'''
	movie_list = select_where_actor_is(actorName)
	actor_list = [ ]
	for i in movie_list:
		new = select_where_movie_is(i)
		actor_list.append(new)
	new_set = set(actor_list)
	return list(new_set)
	

def main():
    actor_DB = create_actors_DB('movies.txt')
    ratings_DB = create_ratings_DB('moviescores.csv')
    # PLEASE TAKE THE NEXT FEW PRINTING LINES OUT
    # ONCE YOU HAVE CONFIRMED THIS WORKS
    print actor_DB
    print ratings_DB
    print 'Welcome to the actor and movie database.'
    print 'This database contains actor info and movie ratings.'
    print '\n'
    print actor_DB['Humphrey Bogart']
    print ratings_DB['Rambo']
    delete_movie('From Russia With Love', actor_DB, ratings_DB)
    print actor_DB
    print ratings_DB
    print select_where_actor_is('Sean Connery', actor_DB)
    
    
if __name__ == '__main__':
    main()
