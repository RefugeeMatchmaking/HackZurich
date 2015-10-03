# The idea is to get an algorithm to find a suitable triples refugee-refugee-local-local
# Advantages: 2 on 2 should a balanced and neutral group. 
# Disadvantages: it might be hard to choose 2 refugees

import networkx as nx 
from get_score import *

class MockUser:
	def __init__(self, _id,  status, firstname, surname, dob, gender, gender_pref, languages, about, email, location = "Zurich"):
		self.status = status
		self.id = _id
		self.firstname = firstname
		self.surname = surname
		self.dob = dob
		self.gender = gender
		self.gender_pref = gender_pref
		self.languages = languages
		self.about = about
		self.email = email
		self.location = location


# A mock list of refugees/locals s
refugees = list([MockUser(1, "refugee", 
						  "Arnold", 
						  "Schwarzeneger", 
				 		  "2000-30-6", # how to insert the date correctly
				 		  "male", 
				 		  "anyone",
				 		  ["English"],
						  "lorem ipsum",
						  "lorem@lorem.uk",
						  "Laax"),

				 MockUser(2, "refugee", 
						  "Bertolt", 
						  "Brecht", 
				 		  "2000-10-2", # how to insert the date correctly
				 		  "male", 
				 		  "anyone",
				 		   ["English"],
						  "lorem ipsum",
						  "bertolt@lorem.uk",
						  "Chur"),

				 MockUser(3, "refugee", 
						  "Albert", 
						  "Camus", 
				 		  "2000-11-7", # how to insert the date correctly
				 		  "male", 
				 		  "anyone",
				 		   ["English"],
						  "lorem ipsum",
						  "albi@lorem.uk",
						  "Oerlikon"),

				 MockUser(4, "refugee",
				 	      "Soren", 
				          "Kirkegaard", 
				          "2000-5-5", # how to insert the date correctly
				 		  "male", 
				 		   ["English"],
						  "anyone",
						  "lorem ipsum",
				 		  "soren@lorem.uk")]) # Hook these to the database please
local = list([ 
				MockUser(5, "local", 
						  "JP", 
				 		  "Sartre", 
				 		  "2000-21-6", # how to insert the date correctly
				 		  "male", 
				 		   ["English"],
				 		  "own",
				 		  "lorem ipsum",
				 		  "lorem@lorem.uk",
				 		  "Winterthur"),

				 
				 MockUser(6, "local",
				 		  "Friedrich", 
				 		  "Nietszsche", 
				 		  "2000-10-15", # how to insert the date correctly
				 		  "male", 
				 		   ["English"],
				 		  "own",
				 		  "lorem ipsum",
				 		  "bertolt@lorem.uk",
				 		  "Saas Fe"),


				 MockUser(7,"local",
				 	  	  "Fyodor",
				 		  "Dostoyevsky", 
				 		  "2000-11-11", # how to insert the date correctly
						  "male", 
						   ["English"],
				 		  "anyone",
						  "lorem ipsum",
				 		  "fyodor@lorem.uk"),

				 MockUser(8, "local",
				 		  "Simone", 
				 		  "Beauvoit", 
				 		  "2000-1-8", # how to insert the date correctly
				 		  "female", 
				 		   ["English"],
				 		  "anyone",
				 		  "lorem ipsum",
				 		  "simone@lorem.uk")]) # Hook) 

def get_square(node,local,refugees):
	""" Returns a quadruplet of nodes refugee-refugee-local-local.
		Incredibly rusty, but will work"""
	frst = local
	scnd = refugees
	# flip the lists if you start with a refugee
	if node.status == "refugee":
		frst = refugees
		scnd = local

	# Rusty as hell
	biparts = {}

	for friend in scnd:
		for friend_of_friend in frst:
			if friend_of_friend is node:
				continue # skip itself
			cost = get_score(node,friend) + get_score(friend, friend_of_friend)
			
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

	return square;




