from .get_score import get_score

import time #For speed checking


#PJ Tried to make some comments to understand the code
def get_square(node,all_locals,all_refugees):
	""" Returns a quadruplet of nodes refugee-refugee-local-local.
			Incredibly rusty, but will work"""


	threshold=0.1 #Set threshold for a linear match (ie match between two people)
	highest = -float("inf") #variable for finding the highest score
	triangle={} #A dictionary of triangluar matches. A triangular match consists of three people. Node, friend, friend_of friend

	# This determines what database we search first, and what we search second
	if node.refugee_or_local == "L":
		#Our node (user) is a local so we first want to search the refugee database
		frst = all_refugees
		scnd = all_locals

	elif node.refugee_or_local=="R":
		#Our node (user) is a refugee so we first want to search the local database
		frst = all_locals
		scnd = all_refugees

	#Loop through the database and get scores
	for friend in frst:


		s1 = get_score(node,friend)

		if s1 > threshold: #If the score is higher than the threshold then save it

			#Now we want to loop through the second database and compare that to our newly found friend
			for friend_of_friend in scnd:

				if friend_of_friend is node:
					continue # skip itself

				s2 = get_score(friend,friend_of_friend)

				if s2 > threshold: #If the score is higher than the threshold then we have found a triangluar match (3 people)
					
					s3 = get_score(node, friend_of_friend)
					if friend_of_friend in triangle:
						triangle[friend_of_friend].append((friend,2*s1+2*s2 + s3 ))
					else:
						triangle[friend_of_friend]=[(friend,2*s1+2*s2+s3)]
				

	#Loop through the dictionary of triangles
	for fof in triangle:

		#If our friend_of_friend connects back to node via another refugee, we get a square
		if len(triangle[fof])>1:
			#If our friend_of_friend has more than two friends then we need to obtain the top two
			toptwo=sorted(triangle[fof], key=lambda tup: tup[1])[:2]
			#Lets sum the scores of the top two friends and add the scores between the friends
			left_friend = toptwo[0][0]
			right_friend = toptwo[1][0]
			s4 = 2*get_score(left_friend, right_friend)

			new_score = toptwo[0][1] + toptwo[1][1] + s4 # this gets the score as a sum of all edges in fully connected 4 point graph
			#if this score is the highest, then save the square, if not, leave it
			if new_score>highest:
				square=[node,toptwo[0][0],toptwo[1][0], fof]
				highest=new_score

	#Return the square with the highest score
	return square, (highest/4.0)




