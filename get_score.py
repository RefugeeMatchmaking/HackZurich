from matchmaking import *

def get_score(User1, User2):
	#initialize score
	matchrank = 0

	#check if one if host and one is refugee
	if User1.staus == User2.status:
		return -1 # both hosts or refugees

	#by location
	matchrank = location_rank(User1.location, User2.location, matchrank)

	#check if zero
	if matchrank == 0:
		print('Nogo criteria found. No match!')

		return -1


	#by gender preference
	matchrank = gender_preference_rank(User1.Gender, User2.Gender, User1.Gender_Pref, User2.Gender_Pref, matchrank)

	# by age
	matchrank = age_rank(User1.DOB, User2.DOB, matchrank)
	if matchrank == 0:
		print('Nogo criteria found. No match!')

		return -1

	#check if zero
	if matchrank == 0:
		print('Nogo criteria found. No match!')

		return -1

	matchrank = location_rank(User1.Languages, User2.Languages, matchrank)
	if matchrank == 0:
		print('Nogo criteria found. No match!')

		return -1
	#by age
	



	return matchrank



	