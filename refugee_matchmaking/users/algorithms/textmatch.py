import nltk

def textmatch(targetstring,string_from_database):
	''' text based matching
	requires nltk module
	test targetstring against string from user database
	string_from_database to be looped through whole database
	'''
	
	matchscore = 0
	matchcount = 0
	matchwords = []
	filterwords = ['are','like','i']

	# make sure strings are not empty
	if not targetstring or not string_from_database:
		print("ERROR: Please provide valid strings")
		return None, None, None

	text1 = nltk.word_tokenize(targetstring.lower())
	tags1 = nltk.pos_tag(text1)

	nouns1 = [word for word,pos in tags1 if (pos == 'NN' or pos == 'NNS') \
				and not word in filterwords]
	verbs1 = [word for word,pos in tags1 if (pos == 'VBP' or pos == 'VBG' or pos == 'VB')\
				 and not word in filterwords]
	

	text2 = nltk.word_tokenize(string_from_database.lower())
	tags2 = nltk.pos_tag(text2)
	

	nouns2 = [word for word,pos in tags2 if (pos == 'NN' or pos == 'NNS') \
				and not word in filterwords]
	verbs2 = [word for word,pos in tags2 if (pos == 'VBP' or pos == 'VBG' or pos == 'VB')\
	 			and not word in filterwords]
	
	words1 = nouns1 + verbs1
	words2 = nouns2 + verbs2
	


	# if len(words1) < len(words2):
	# 	for word in words1:
	# 		if word in words2:
	# 			matchscore+=1
	# 			matchwords.append(word)
	# else:
	# 	for word in words2:
	# 		if word in words1:
	# 			matchscore+=1
	# 			matchwords.append(word)


	# matchscore = float(matchscore)/min(len(words1),len(words2))	


	for word in words1:
		if word in words2 and not word in matchwords:
			matchcount+=1
			matchwords.append(word)

	matchscore = float(matchcount)/len(words1)

	return matchscore, matchcount, matchwords



if __name__ == '__main__':

	string1 = "My hobbies are programming, inventing cool stuff and \
	rocking the word with my GuiTar. I also like to hang with friends in the park.\
	Animals are awesome. I always like to meet new people. Friends friends. \
	Multiple occurances should only be counted once."

	string2 = 'I like cooking, Programming and chilling with friends. My dog is the best.\
	I have a band in which I play the guitar. In my spare time I do a lot of rock climbing.\
	People should help each other and meet.'

	string1=""
	string2=""


	matchscore, matchcount, matchwords = textmatch(string1,string2)
	try:
		print('Matchscore %.2f'%matchscore)
		print('Matchcount %i'%matchcount)
		print('Matchwords %s'%matchwords)
	except:
		print('Could not print')
		print(matchscore)
		print(matchcount)
		print(matchwords)