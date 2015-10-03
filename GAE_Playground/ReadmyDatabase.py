

class getdata():

	def createdatabase(self,UserInfo):
		newuser=UserInfo(Status="refugee",firstname="Arnold",
			surname="Schwarzeneger",Languages=["English"],
			Gender="male", Gender_Pref="anyone",
			DOB="2000-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Laax")

		newuser.put()



	def readdatabase(self, database, node):
		self.q=database
		self.node=node
		self.refugees=self.q.filter("Status=","refugee")
		self.local=self.q.filter("Status=","local")
		square=self.get_square(self.node, self.local, self.refugees)

		return square

	def get_square(self,node,local,refugees):
		""" Returns a quadruplet of nodes refugee-refugee-local-local.
			Incredibly rusty, but will work"""
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

		return None


