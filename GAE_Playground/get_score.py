from matchmaking import *

def get_score(User1, User2):
	#initialize score
	matchrank = 0

	#check if one if host and one is refugee
	if User1.status == User2.status:
		return -1 # both hosts or refugees

	#by location
	#matchrank = location_rank(User1.location, User2.location, matchrank)

	#check if zero
	if matchrank == 0:
		print('Nogo criteria found. No match!')

		return -1


	#by gender preference
	matchrank = gender_preference_rank(User1.gender, User2.gender, User1.gender_pref, User2.gender_pref, matchrank)

	# by age
	""" Disabled for now """
	matchrank = age_rank(User1.dob, User2.dob, matchrank)
	if matchrank == 0:
		print('Nogo criteria found. No match!')

		return -1

	#check if zero
	#if matchrank == 0:
	#	print('Nogo criteria found. No match!')

	#	return -1

	""" Ignore for now """
	#matchrank = location_rank(User1.languages, User2.languages, matchrank)
	#if matchrank == 0:
	#	print('Nogo criteria found. No match!')

	#	return -1
	#by age
	
	return matchrank
