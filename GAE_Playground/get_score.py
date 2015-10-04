from matchmaking import *
from earth_distance import *
from datetime import date
from math import exp

def get_score(User1, User2):
	#initialize score
	matchrank = 0.0

	#strict rule on gender preference
	if gender_preference_rank(User1.Gender, User2.Gender, User1.Gender_Pref, User2.Gender_Pref) == -1 :
		return -1;
	
	# distance scoring
	distance = haversine(User1.Longitude, User1.Latitude, User2.Longitude, User2.Latitude)
	matchrank += 20.0/(20.0 + distance) # Falls down to 0.5 at 20 km

	# age scoring
	usr1_dob = str(User1.DOB).split('-')
	usr2_dob = str(User2.DOB).split('-')

	today = date.today()
	usr1_age = today.year - int(usr1_dob[2])
	usr2_age = today.year - int(usr2_dob[2])
	matchrank += exp(-((usr1_age - usr2_age)**2)/(10.0)) # add a Gaussian factor


	""" Ignore for now """
	#matchrank = location_rank(User1.languages, User2.languages, matchrank)
	#if matchrank == 0:
	#	print('Nogo criteria found. No match!')

	#	return -1
	#by age
	
	return matchrank
