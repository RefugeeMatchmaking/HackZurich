# The idea is to get an algorithm to find a suitable triples refugee-refugee-local-local
# Advantages: 2 on 2 should a balanced and neutral group. 
# Disadvantages: it might be hard to choose 2 refugees

import networkx as nx 
from get_score import *


class getdata():

	def createdatabase(self,UserInfo):
		newuser=UserInfo(Status="refugee",firstname="Arnold",
			surname="Schwarzeneger",Languages=["English"],
			Gender="male", Gender_Pref="anyone",
			DOB="2000-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Laax")

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



