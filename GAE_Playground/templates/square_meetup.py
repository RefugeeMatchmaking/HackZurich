# The idea is to get an algorithm to find a suitable triples refugee-refugee-local-local
# Advantages: 2 on 2 should a balanced and neutral group. 
# Disadvantages: it might be hard to choose 2 refugees

import networkx as nx 
import 
# A mock list of refugees/locals s
refugees = list({'firstname':"Arnold", 
				 'surname':"Schwarzeneger", 
				 'dob':"1947-30-6", # how to insert the date correctly
				 'gender':"male", 
				 'status':"refugee",
				 'gender_pref':"anyone",
				 'about':"lorem ipsum",
				 'email':"lorem@lorem.uk"},

				 {'firstname':"Bertolt", 
				 'surname':"Brecht", 
				 'dob':"1898-10-2", # how to insert the date correctly
				 'gender':"male", 
				 'status':"refugee",
				 'gender_pref':"anyone",
				 'about':"lorem ipsum",
				 'email':"bertolt@lorem.uk"},


				 {'firstname':"Albert", 
				 'surname':"Camus", 
				 'dob':"1913-11-7", # how to insert the date correctly
				 'gender':"male", 
				 'status':"refugee",
				 'gender_pref':"anyone",
				 'about':"lorem ipsum",
				 'email':"albert@lorem.uk"},

				 {'firstname':"Søren", 
				 'surname':"Kirkegaard", 
				 'dob':"1813-5-5", # how to insert the date correctly
				 'gender':"male", 
				 'status':"refugee",
				 'gender_pref':"anyone",
				 'about':"lorem ipsum",
				 'email':"albert@lorem.uk"},) # Hook these to the database please
local = list(
				{'firstname':"JP", 
				 'surname':"Sartre", 
				 'dob':"1905-21-6", # how to insert the date correctly
				 'gender':"male", 
				 'status':"local",
				 'gender_pref':"own",
				 'about':"lorem ipsum",
				 'email':"lorem@lorem.uk"},

				 {'firstname':"Friedrich", 
				 'surname':"Nietszsche", 
				 'dob':"1844-10-15", # how to insert the date correctly
				 'gender':"male", 
				 'status':"local",
				 'gender_pref':"own",
				 'about':"lorem ipsum",
				 'email':"bertolt@lorem.uk"},


				 {'firstname':"FM", 
				 'surname':"Dostoyevsky", 
				 'dob':"1821-11-11", # how to insert the date correctly
				 'gender':"male", 
				 'status':"local",
				 'gender_pref':"anyone",
				 'about':"lorem ipsum",
				 'email':"fyodor@lorem.uk"},

				 {'firstname':"Simone", 
				 'surname':"Beauvoit", 
				 'dob':"1908-1-8", # how to insert the date correctly
				 'gender':"female", 
				 'status':"local",
				 'gender_pref':"anyone",
				 'about':"lorem ipsum",
				 'email':"simone@lorem.uk"},) # Hook) 

