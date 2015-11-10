import nltk

def textmatch(string1,string2):
	''' text based matching
	requires nltk module'''
	
	matchscore = 0
	matchwords = []
	filterwords = ['are','like','i']

	text1 = nltk.word_tokenize(string1.lower())
	tags1 = nltk.pos_tag(text1)

	nouns1 = [word for word,pos in tags1 if (pos == 'NN' or pos == 'NNS') \
				and not word in filterwords]
	verbs1 = [word for word,pos in tags1 if (pos == 'VBP' or pos == 'VBG' or pos == 'VB')\
				 and not word in filterwords]
	

	text2 = nltk.word_tokenize(string2.lower())
	tags2 = nltk.pos_tag(text2)
	

	nouns2 = [word for word,pos in tags2 if (pos == 'NN' or pos == 'NNS') \
				and not word in filterwords]
	verbs2 = [word for word,pos in tags2 if (pos == 'VBP' or pos == 'VBG' or pos == 'VB')\
	 			and not word in filterwords]
	
	words1 = nouns1 + verbs1
	words2 = nouns2 + verbs2
	


	if len(words1) < len(words2):
		for word in words1:
			if word in words2:
				matchscore+=1
				matchwords.append(word)
	else:
		for word in words2:
			if word in words1:
				matchscore+=1
				matchwords.append(word)


	matchscore = float(matchscore)/min(len(words1),len(words2))	




	return matchscore, matchwords



if __name__ == '__main__':

	string1 = "My hobbies are programming, inventing cool stuff and \
	rocking the word with my GuiTar. I also like to hang with friends in the park.\
	Animals are awesome. I always like to meet new people."

	string2 = 'I like cooking, Programming and chilling with friends. My dog is the best.\
	I have a band in which I play the guitar. People sould help each other and meet.'




	matchscore, matchwords = textmatch(string1,string2)
	print('Matchscore %.2f'%matchscore)
	print('Matchwords %s'%matchwords)