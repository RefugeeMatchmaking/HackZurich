
from .matchmaking import gender_preference_rank
from .earth_distance import haversine
from datetime import date
import math
from .textmatch import textmatch

import time #For speeed checking

def get_score(User1, User2):
	#initialize score
	matchrank = 0.0
	print('.......matching users........')
	#strict rule on gender preference
	#Gender_preference_rank has no children

	if gender_preference_rank(User1.gender, User2.gender, User1.gender_preference, User2.gender_preference) == -1 :
		print('nogo condition for gener preference fulfilled')
		return -1;


	# distance scoring
	t1=time.time()

	"""This is the bottleneck of the code!!!!!!!!!!------------------------------"""
	lon1 =User1.lon
	lat1 =User1.lat
	lon2 =User2.lon
	lat2 =User2.lat
	"""------------------------------------------------------------------------------"""

	t2=time.time()
	print('databasecalling takes',t2-t1,'seconds to run')

	distance = haversine(lon1, lat1, lon2, lat2)

	print('Long1 %f Long2 %f Lat1 %f Lat2 %f'%(lon1,lon2,lat1,lat2))
	print('distance from haversine: %f'%distance)
	distancerank = 400.0/(200.0 + distance) - 1.0 
	
	if(distancerank < 0)
		return -1

	#matchrank += 20.0/(20.0 + distance) # Falls down to 0.5 at 20 km
	matchrank += distancerank
	print('Distance rank: %f'%distancerank)


	# age scoring
	usr1_dob = str(User1.birthdate).split('-')
	usr2_dob = str(User2.birthdate).split('-')

	today = date.today()
	usr1_age = today.year - int(usr1_dob[0])
	usr2_age = today.year - int(usr2_dob[0]) #pulls out of range error


	agerank = math.exp(-((usr1_age - usr2_age)**2)/(10.0)) # add a Gaussian factor 
	#matchrank += math.exp(-((usr1_age - usr2_age)**2)/(10.0)) # add a Gaussian factor
	matchrank += agerank
	print('Age rank: %f'%agerank)

	# text based scoring
	usr1_text = str(User1.about)
	usr2_text = str(User2.about)

	matchscore_text, matchcount_text, matchwords_text = \
		textmatch(usr1_text,usr2_text)

	if not matchscore_text == None:
		print('textmatch rank %f'%matchscore_text)
		matchrank += matchscore_text


	""" Ignore for now """
	#matchrank = location_rank(User1.languages, User2.languages, matchrank)
	#if matchrank == 0:
	#	print('Nogo criteria found. No match!')

	#	return -1
	#by age
	
	print('Overall match rank: %f'%matchrank)
	return matchrank