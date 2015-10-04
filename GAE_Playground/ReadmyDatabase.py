# The idea is to get an algorithm to find a suitable triples refugee-refugee-local-local
# Advantages: 2 on 2 should a balanced and neutral group. 
# Disadvantages: it might be hard to choose 2 refugees

import networkx as nx 
from get_score import *


class getdata():

	def createdatabase(self,UserInfo):
		location = "Laax" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Hossein",
			surname="Schwarzeneger",Languages=["English", "Arabic"],
			Gender="male", Gender_Pref="anyone",
			DOB="1986-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Laax", Latitude=latitude, Longitude=longitude)
		newuser.put()
		location = "Lausanne" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Muhammed",
			surname="Housein",Languages=["Arabic","English"],
			Gender="male", Gender_Pref="anyone",
			DOB="2000-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location=location,Latitude=latitude, Longitude=longitude)
		newuser.put()
		
		location = "Zurich" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="",
			surname="Ceasar",Languages=["Italian", "English"],
			Gender="male", Gender_Pref="own",
			DOB="1994-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location=location,Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Berlin" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Andan",
			surname="Polan",Languages=["English", "Arabic"],
			Gender="female", Gender_Pref="own",
			DOB="1976-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location=location,Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Paris" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Milini",
			surname="Kouta",Languages=["Arabic"],
			Gender="female", Gender_Pref="own",
			DOB="1987-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location=location,Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Munich" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Maya",
			surname="Fischer",Languages=["English","Arabic","German"],
			Gender="female", Gender_Pref="anyone",
			DOB="1956-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location=location,Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Zurich" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Manna",
			surname="Houseein",Languages=["English","Arabic"],
			Gender="female", Gender_Pref="anyone",
			DOB="1990-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Zurich",Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Zurich" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Bennill",
			surname="Mustafa",Languages=["English","Arabic"],
			Gender="male", Gender_Pref="anyone",
			DOB="1978-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Zurich",Latitude=latitude, Longitude=longitude)
		newuser.put()


		location = "Laax" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Arnold",
			surname="Jr",Languages=["English","German"],
			Gender="male", Gender_Pref="anyone",
			DOB="1988-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Laax",Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Zurich" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="PJ",
			surname="Jayathissa",Languages=["English","Spanish"],
			Gender="male", Gender_Pref="anyone",
			DOB="1988-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Zurich",Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Zurich" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Karoline",
			surname="Davierser",Languages=["English", "German"],
			Gender="female", Gender_Pref="own",
			DOB="1995-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Zurich",Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Biel" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Jonathon",
			surname="paulanner",Languages=["English", "Spanish","Chinese"],
			Gender="male", Gender_Pref="anyone",
			DOB="1993-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Biel",Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Zurich" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Sarah",
			surname="hausser",Languages=["English","German"],
			Gender="female", Gender_Pref="own",
			DOB="2000-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Zurich",Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Zurich" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Benjamin",
			surname="Kuhler",Languages=["English", "German"],
			Gender="male", Gender_Pref="anyone",
			DOB="1968-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Zurich",Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Laax" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Martina",
			surname="Bechler",Languages=["English","German"],
			Gender="female", Gender_Pref="own",
			DOB="1970-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Laax",Latitude=latitude, Longitude=longitude)
		newuser.put()

		location = "Laax" #userinfo["Location"],
		latitude, longitude = lat_long(location)
		newuser=UserInfo(Status="refugee",firstname="Mika",
			surname="Kirtal",Languages=["English", "German"],
			Gender="female", Gender_Pref="anyone",
			DOB="1980-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Laax",Latitude=latitude, Longitude=longitude)
		newuser.put()




		newuser.put()



	def readdatabase(self, querry, node):
		q.filter("Status=","refugee").fetch(limit=5)
		self.local=self.q.filter("Status=","local")
		
		print("list: " + str(database.fetch(limit = 5)))

		print("node: " + str(self.node) + "\n local" + str(self.local) + "\n refugees" + str(self.refugees))
		square=self.get_square(self.node, self.local, self.refugees)

		return square

	def get_square(self,node,local,refugees):
		""" Returns a quadruplet of nodes refugee-refugee-local-local.
			Incredibly rusty, but will work"""

		
		
		print "printing user info: " + str(q)

		frst = local
		scnd = refugees
		node = node
		# flip the lists if you start with a refugee
		if node.Status == "refugee":
			print "Is a refugee"
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



