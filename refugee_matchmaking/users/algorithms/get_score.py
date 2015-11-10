#from users.algorithms.matchmaking import *
#from users.algorithms.earth_distance import *
from .matchmaking import *
from .earth_distance import *
from datetime import date
import math

def get_score(User1, User2):
	#initialize score
	matchrank = 0.0

	#strict rule on gender preference
	#Gender_preference_rank has no children
	if gender_preference_rank(User1.gender, User2.gender, User1.gender_preference, User2.gender_preference) == -1 :
		return -1;
	
	# distance scoring
	#haversine has no children
	distance = haversine(User1.latitude_longitude[1], User1.latitude_longitude[0], User2.latitude_longitude[1], User2.latitude_longitude[0])
	matchrank += 20.0/(20.0 + distance) # Falls down to 0.5 at 20 km

	# age scoring
	usr1_dob = str(user1.birthdate).split('-')
	usr2_dob = str(user2.birthdate).split('-')

	today = date.today()
	usr1_age = today.year - int(usr1_dob[0])
	usr2_age = today.year - int(usr2_dob[0]) #pulls out of range error
	matchrank += math.exp(-((usr1_age - usr2_age)**2)/(10.0)) # add a Gaussian factor


	""" Ignore for now """
	#matchrank = location_rank(User1.languages, User2.languages, matchrank)
	#if matchrank == 0:
	#	print('Nogo criteria found. No match!')

	#	return -1
	#by age
	
	return matchrank