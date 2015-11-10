import os
import json
from datetime import date
from math import exp,radians, cos, sin, asin, sqrt




#Self made functions
#from ReadmyDatabase import *
from get_score import *


def getGroupScore(self):
	
		#Begin computing the location coordinates
		try:

			user.latitude, user.longitude = lat_long(user.location)
			
		except:
			latitude=1.0
			longitude=1.0

		#Save input into the database uncomment this for application
		newuser=UserInfo(Status=userinfo["Status"],firstname=userinfo["firstname"],
			surname=userinfo["surname"],Languages=userinfo["Languages"],
			Gender=userinfo["Gender"], Gender_Pref=userinfo["Gender_Pref"],
			DOB=userinfo["DOB"], About=userinfo["About"], Email=userinfo["Email"],
			Location=str(location), Latitude=latitude, Longitude=longitude)


		newuser.put()

		#likely stupid and inefficient , but works :) 

		all_locals=User.objects.filter(refugee_or_local='L')
		all_refugees=User.objects.filter(refugee_or_local='R')

		# q = UserInfo.all() 
		# local = q.filter("Status =", "local").fetch(limit=DATABASE_FETCH_LIMIT)
		
		# q = UserInfo.all() 
		# refugees = q.filter("Status =", "refugee").fetch(limit=DATABASE_FETCH_LIMIT)
		
		try:
			print("newuser: " + str(newuser) + "\n refugees:" + str(refugees)+ "\n locals:"+str(local))
			square, score = get_square(newuser,all_locals,all_refugees)
		except:
			square=[]
			score=0

		#x = mygetdata.readdatabase(q, newuser) #run readydatabase.py method, readdatabase
		#print x
		#if square exists (not empty)
		if square and score>0.05:

			template_values= ([(person.firstname +' '+ person.surname) for person in square])
			# string = ''.join([person.firstname for person in square])
			# template_values = {'text':string,}
			groupscore = int(score*100.0)#convert to percentages




#Function from Vojta, move away from here
def get_square(node,all_locals,all_refugees):
		""" Returns a quadruplet of nodes refugee-refugee-local-local.
			Incredibly rusty, but will work"""


		frst = all_locals
		scnd = all_refugees

		# flip the lists if you start with a refugee
		if node.refugee_or_local == "R":
			print("flipped")
			frst = all_refugees
			scnd = all_locals

		print(frst, scnd)

		# Rusty as hell
		biparts = {}

		for friend in scnd:
			s1 = get_score(node,friend) 
			
			if s1 == -1:
				continue # gender pref. discards

			for friend_of_friend in frst:
				if friend_of_friend is node:
					continue # skip itself
				
				s2 = get_score(friend, friend_of_friend)
				if s2 == -1:
					continue 

				cost = s1 + s2

				
				if friend_of_friend in biparts:
					biparts[friend_of_friend].append((friend, cost)) # slow 
				else:
					biparts[friend_of_friend] = [(friend, cost)]

		highest = -float("inf")
		square = []

		# find the square
		for fof in biparts:
			two_relatives = sorted(biparts[fof], key=lambda tup: tup[1])[:2]
			# if the quad score is highest in the network
			new_cost = two_relatives[0][1] + two_relatives[1][1]
			if new_cost > highest:
				square = [node,two_relatives[0][0],fof,two_relatives[1][0]]
				highest = new_cost

		return square, (highest/4.0);

import requests

def lat_long(city):
	''' function to return latitude and longitude information based on city name '''
	try:
		response = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+str(city))
		resp_json_payload = response.json()

		latlong = resp_json_payload['results'][0]['geometry']['location']
		
		lat = latlong['lat']
		lng = latlong['lng']

	except:
		lat=4.5
		lng=2.5


	#lat = 

	return lat, lng


if __name__ == '__main__':
	lat,lng = lat_long('bonn')

	print('lat %.5f' %lat)
	print('lng %.5f' %lng)

def get_score(User1, User2):
	#initialize score
	matchrank = 0.0

	#strict rule on gender preference
	#Gender_preference_rank has no children
	if gender_preference_rank(User1.gender, User2.gender, User1.gender_preference, User2.gender_preference) == -1 :
		return -1;
	
	# distance scoring
	#haversine has no children
	distance = haversine(User1.longitude, User1.latitude, User2.longitude, User2.latitude)
	matchrank += 20.0/(20.0 + distance) # Falls down to 0.5 at 20 km

	# age scoring
	usr1_dob = str(user1.birthdate).split('-')
	usr2_dob = str(user2.birthdate).split('-')

	today = date.today()
	usr1_age = today.year - int(usr1_dob[0])
	usr2_age = today.year - int(usr2_dob[0]) #pulls out of range error
	matchrank += exp(-((usr1_age - usr2_age)**2)/(10.0)) # add a Gaussian factor


	""" Ignore for now """
	#matchrank = location_rank(User1.languages, User2.languages, matchrank)
	#if matchrank == 0:
	#	print('Nogo criteria found. No match!')

	#	return -1
	#by age
	
	return matchrank


def get_earth_distance(loc1, loc2):
	'''Function that returns the haversine distance between two locations'''
	
	#url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(loc1),str(loc2))
	
	#result= simplejson.load(urlopen(url))
	
	#print(result)
	#driving_distance = result['rows'][0]['elements'][0]['distance']['value']/1000 # [km]
	
	lat1, lon1 = lat_long(loc1)
	lat2, lon2 = lat_long(loc2)

	return haversine(lon1, lat1, lon2, lat2)


def haversine(lon1, lat1, lon2, lat2):
	lon1, lat1, lon2, lat3 = map(radians,[lon1, lat1, lon2, lat2])

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
	c = 2*asin(sqrt(a))
	r = 6371
	return c*r #[m]


if __name__ == "__main__":
	earth_distance = get_earth_distance("koeln","bonn")
	print(earth_distance)


def decode_json_response():
	pass

def location_rank(loc_ref, loc_host, matchrank):
	distance = get_earth_distance(str(loc_ref),str(loc_host)) # great one

	if distance<10:
		matchrank+=5
	elif distance<25:
		matchrank+=3
	elif distance<50:
		matchrank+=1
	else:
		matchrank = 0 # nogo condition
		

	return matchrank

def gender_preference_rank(gender_ref, gender_host, genderpref_ref, genderpref_host):
	
	matchrank = 0

	#make sure everything is string
	gender_ref = str(gender_ref)
	gender_host = str(gender_host)
	genderpref_ref = str(genderpref_ref)
	genderpref_host = str(genderpref_host)

	if gender_ref == gender_host:
		matchrank+=1 # no problems here
	elif gender_ref != gender_host and genderpref_ref == "anyone" and genderpref_host == "anyone":
		matchrank+=1 # no problems here

	else: 
		matchrank = -1 # nogo condition
		

	return matchrank


def age_rank(usr1_dob, usr2_dob, matchrank):

	# TODO
	# convert date of birth to month, year, day
	# format is "dd.mm.yyyy"
	usr1_dob = str(usr1_dob).split('.')
	usr2_dob = str(usr2_dob).split('.')


	today = date.today()
	usr1_age = today.year - int(usr1_dob[2])
	usr2_age = today.year - int(usr2_dob[2])

	age_host = usr1_age
	age_ref = usr2_age

	print(age_host)
	print(age_ref)

	if age_host > age_ref * 0.9 and age_host < age_ref * 1.1: #+-10%
		matchrank+=5

	elif age_host > age_ref * 0.8 and age_host < age_ref * 1.2: #+-20%
		matchrank+=3

	elif age_host > age_ref * 0.6 and age_host < age_ref * 1.4: #+-40%
		matchrank+=1
	else:
		matchrank = 0 # nogo condition
		

	return matchrank

def language_rank(languages_ref, languages_host, matchrank):
	''' takes python list of languages for ref and host'''
	import re
	lanrank = 0

	# language will be comma or colon separated string
	#languages_ref = re.split('; |, ',languages_ref)
	#languages_host = re.split('; |, ',languages_host)
	

	languages_ref =[str(lan).lower() for lan in languages_ref]
	languages_host =[str(lan).lower() for lan in languages_host]


	for language in languages_ref:
		language = str(language).lower()
		if language in languages_host:
			lanrank+=1

	if lanrank < 1:
		matchrank = 0 # nogo condition

	else: matchrank += lanrank

	return matchrank


if __name__ == '__main__':

	print('---- testing age rank ----')
	usr1_dob = "12.04.1950"
	usr2_dob = "10.07.1960"
	matchrank = 0
	matchrank=age_rank(usr1_dob,usr2_dob,matchrank)
	print(usr1_dob)
	print(usr2_dob)
	print("matchrank: %i" %matchrank)

	usr1_dob = "12.04.1990"
	usr2_dob = "10.07.1970"
	matchrank = 0
	matchrank=age_rank(usr1_dob,usr2_dob,matchrank)
	print(usr1_dob)
	print(usr2_dob)
	print("matchrank: %i" %matchrank)

	print('---- testing language rank ----')
	matchrank = 0
	languages_ref = ['English', 'Spanish', 'German']
	languages_host = ['English', 'German', 'Italian']
	print(languages_ref)
	print(languages_host)
	matchrank = language_rank(languages_ref,languages_host,matchrank)
	print("matchrank: %i" %matchrank)
	
