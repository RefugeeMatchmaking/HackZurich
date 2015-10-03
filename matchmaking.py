from earth_distance import get_earth_distance

matchrank = 0

def decode_json_response():
	pass

def location_rank(loc_ref, loc_host, matchrank):
	distance = get_earth_distance(loc_ref,loc_host)

	if distance<10:
		matchrank+=5
	elif distance<25:
		matchrank+=3
	elif distance<50:
		matchrank+=1
	else:
		matchrank = 0 # nogo condition
		

	return matchrank

def gender_preference_rank(gender_ref, gender_host, genderpref_ref, genderpref_host, matchrank):
	if gender_ref == gender_host:
		matchrank+=1 # no problems here

	elif gender_ref != gender_host and genderpref_ref == "anyone" and gernderpref_ref == "anyone":
		matchrank+=1 # no problems here

	else: 
		matchrank = 0 # nogo condition
		

	return matchrank


def age_rank(age_ref, age_host, matchrank):
	if age_host > age_ref * 0.95 and age_host < age_ref * 1.05: #+-5%
		matchrank+=5

	elif age_host > age_ref * 0.9 and age_host < age_ref * 1.1: #+-10%
		matchrank+=3

	elif age_host > age_ref * 0.8 and age_host < age_ref * 1.2: #+-20%
		matchrank+=1
	else:
		matchrank = 0 # nogo condition
		

	return matchrank

def language_rank(languages_ref, languages_host, matchrank):
	''' takes python list of languages for ref and host'''
	lanrank = 0
	for language in languages_ref:
		if language in languages_host:
			lanrank+=1


	if lanrank < 1:
		matchrank = 0 # nogo condition

	else: matchrank += lanrank

	return matchrank
