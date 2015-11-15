from .get_score import get_score


#PJ Tried to make some comments to understand the code
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

		print('list of locals and refugees: ', frst, scnd)

		# Rusty as hell
		biparts = {}

		for friend in scnd: 				#Loop through people of the opposite status
			s1 = get_score(node,friend)  	#Aquire score against people of the opposite status (this person is labeled 'friend')
			
			if s1 == -1:
				continue # gender pref. discards

			for friend_of_friend in frst: 	#Loop through people of the same staus to match with friend
				if friend_of_friend is node:
					continue # skip itself
				
				s2 = get_score(friend, friend_of_friend) #get score matching 'friend' to the 'friend of friend'
				if s2 == -1:
					continue #discard due to gender pref

				cost = s1 + s2 #Add scores together

				
				if friend_of_friend in biparts:
					biparts[friend_of_friend].append((friend, cost)) # slow 
				else:
					biparts[friend_of_friend] = [(friend, cost)] #Adding score of the friend to a dictionary element contain the friend of friend

		highest = -float("inf")
		square = []

		# find the square
		for fof in biparts:
			two_relatives = sorted(biparts[fof], key=lambda tup: tup[1])[:2] #Aquire top two combined scores 'costs'
			print(two_relatives)
			# if the quad score is highest in the network
			new_cost = two_relatives[0][1] + two_relatives[1][1]
			if new_cost > highest:
				square = [node,two_relatives[0][0],fof,two_relatives[1][0]]
				highest = new_cost

		return square, (highest/4.0);