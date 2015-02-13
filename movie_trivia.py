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
	for i in movie_Db.iterkeys():
		if movie in movie_Db[i]:
			movie_Db[i].remove(movie)
			
def select_where_actor_is(actorName, movie_Db):
	'''Given an actor, return list of all movies.'''
	return list(movie_Db[actorName])	#converts set of movies to list and returns list
	
def select_where_movie_is(movieName, movie_Db):
	'''Given a movie, returns list of all actors.'''
	actor_list = [ ]
	for i in movie_Db.iterkeys():
		if movieName in movie_Db[i]:
			actor_list.append(i)
	return actor_list
	
def select_where_rating_is(targeted_rating, comparison, is_critic, ratings_Db):
	'''Returns list of movies that satisfy a set of conditions.'''
	good_movies = [ ]
	if comparison == '>':
		for i in ratings_Db.iterkeys():
			if int(ratings_Db[i][not is_critic]) > targeted_rating:
				good_movies.append(i)
		return good_movies
	elif comparison == '=':
		for i in ratings_Db.iterkeys():
			if int(ratings_Db[i][not is_critic]) == targeted_rating:
				good_movies.append(i)
		return good_movies
	elif comparison == '<':
		for i in ratings_Db.iterkeys():
			if int(ratings_Db[i][not is_critic]) < targeted_rating:
				good_movies.append(i)
		return good_movies
	else: print 'Bad comparison input'	
	
def get_co_actors(actorName, moviedb):
	'''Returns a list of all actors that actor has worked with in any movie.'''
	movie_list = select_where_actor_is(actorName, moviedb)
	actor_list = [ ]
	for i in movie_list:
		new = select_where_movie_is(i, moviedb)
		actor_list.append(new)
	actor_list = flatten2DList(actor_list) #some movies have multiple actors, so I need to flatten the list
	new_set = set(actor_list) #converting to set removes duplicates	
	new_list = list(new_set) #back to list to remove the original actor
	new_list.remove(actorName)
	return new_list

def get_common_movie(actor1, actor2, moviedb):
	'''Returns a list of movies in which both actors were cast.'''
	actor1List = select_where_actor_is(actor1, moviedb)
	actor2List = select_where_actor_is(actor2, moviedb)
	common = set(actor1List).intersection(actor2List)
	return list(common)

def critics_darling(movie_Db, ratings_Db):
	'''Returns list of actors whose movies have the highest average rotten tomatoes critics rating'''
	top_actor = [ ]
	top_score = 0
	for i in movie_Db.iterkeys():
		count = 0
		movie_list = select_where_actor_is(i, movie_Db)
		movie_sum = 0
		for j in movie_list:
			if ratings_Db.has_key(j) == 1:
				count += 1
				movie_sum += eval(ratings_Db[j][0])	#[0] returns first score, which is critics' score	
		avg_rating = movie_sum / count
		if avg_rating > top_score:
			top_score = avg_rating
			top_actor = [i]
		elif avg_rating == top_score:
			top_actor.append(i)
	return top_actor
		
def audience_darling(movie_Db, ratings_Db):
	'''Returns list of actors whose movies have the highest average rotten tomatoes audience rating'''
	top_actor = [ ]
	top_score = 0
	for i in movie_Db.iterkeys():
		count = 0
		movie_list = select_where_actor_is(i, movie_Db)
		movie_sum = 0
		for j in movie_list:
			if ratings_Db.has_key(j) == 1:
				count += 1
				movie_sum += eval(ratings_Db[j][1])
		avg_rating = movie_sum / count
		if avg_rating > top_score:
			top_score = avg_rating
			top_actor = [i]
		elif avg_rating == top_score:
			top_actor.append(i)
	return top_actor	
	
def good_movies(ratings_Db):
	'''Returns set of movies rated above 85 by both critics and audiences.'''
	audienceList = select_where_rating_is(85, '>', False, ratings_Db) #audience list of movies over 85
	criticList = select_where_rating_is(85, '>', True, ratings_Db) #critic list of movies over 85
	common = set(audienceList).intersection(criticList)
	return common

def flatten2DList(x):
	'''Convert a list of lists into a 1D list.'''
	res = []
	for i in x:
		res.extend(i)
	return res


	
def main():
	actor_DB = create_actors_DB('movies.txt')
	ratings_DB = create_ratings_DB('moviescores.csv')
	
	print 'Welcome to the actor and movie database.'
	print 'This database contains actor info and movie ratings.'
	print '\n'
   
    
    
    
    
    
    
if __name__ == '__main__':
    main()
