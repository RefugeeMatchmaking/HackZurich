import os
import webapp2
import jinja2
import hmac #Used for hashing 
import re #regular expression
#Get networkx library from lib folder
from google.appengine.api import mail
import sys 
sys.path.insert(0, 'libs')

SECRET='pjiscool'
DATABASE_FETCH_LIMIT = 500 # max number of users to fetch from the db

from google.appengine.ext import db #Database

#Self made functions
from ReadmyDatabase import *
from lat_long import *
from get_score import *

#Set up template directory
tempplate_dir = os.path.join(os.path.dirname(__file__),'templates')
#Set Up JinJa Environment
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(tempplate_dir), autoescape=True)

#Create a global dictionary to store newuser data
userinfo={"Status":"","firstname":"","surname":"","Languages":[],"Gender":"","Gender_Pref":"","DOB":"",
	"About":"","Location":"", "Email":""}

#User Database Model
class UserInfo(db.Model): #used to crete the database. Art is the name of the databse
	Status=db.StringProperty(required=True) #required = true adds the constraint
	firstname=db.StringProperty(required=True)
	surname=db.StringProperty(required=True)
	Language=db.StringListProperty(required=True)
	Gender=db.StringProperty(required=True)
	Gender_Pref=db.StringProperty(required=True)
	DOB=db.StringProperty(required=True)
	About=db.StringProperty(required=False)
	Email=db.StringProperty(required=True)
	Location=db.StringProperty(required=True)
	Latitude = db.FloatProperty(required=True)
	Longitude = db.FloatProperty(required=True)
	#password=db.StringProperty(required=True)
	created=db.DateTimeProperty(auto_now_add=True) #Automatically adds the time, check the docs


#Handler for write commands
class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw): #the * takes unamed arguments, and the ** takes the named arguments
		self.response.out.write(*a,**kw)

	def render_str(self, template, **params):
		t= jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

#Home Page. Also has the possiblilty to generate a fixed database for trialing
class MainPage(Handler):
	def get(self):
		self.render("home.html")
		#mydata=getdata()
		#mydata.createdatabase(UserInfo)

#Clears userinfo and gets status(refugee or local)
class Index(Handler):
	def get(self):
		userinfo={"Status":"","firstname":"","surname":"","Languages":[],"Gender":"","Gender_Pref":"","DOB":"",
	"About":"","Location":"", "Email":""}
		self.render("index.html")

	def post(self):
		userinfo["Status"]=self.request.get("Status")
		print (str(userinfo))		
		self.redirect('/refugee')

#Gets first name and last name
class Names(Handler):
	def get(self):
		self.render("refugee.html")


	def post(self):
		first = self.request.get("firstname")
		last = self.request.get("surname")
		
		userinfo["firstname"] = first
		userinfo["surname"] = last
#Check if field is full
		if first != '' and last != '': 
			print userinfo	
			self.redirect('/location')
		else: 
			self.redirect('/refugee')
			print("Choose a valid name - print this" )
			pass;

#Quire location. Note that computation is done via coordinates so this will be processed 
#later
class Location(Handler):
	def get(self):
		self.render("location.html")
	def post(self):
		Location = self.request.get("Location")
		if Location != '':
			userinfo["Location"] = Location
			self.redirect('/languages')
		else: 
			self.redirect('/location')

#language, no matching function yet for this
class Languages(Handler):
	def get(self):
		self.render("languages.html")

	def post(self):
		q=[]
		q.append(self.request.get("native"))
		q.append(self.request.get("foreign1"))
		q.append(self.request.get("foreign2"))
		
		if q[0] != '' or q[1] != '' or q[2] != '':
			userinfo["Languages"]=q
			print userinfo	
			self.redirect('/gender', )
		else:
			self.redirect('/languages')

#Gender and preference of gender
class Gender(Handler):
	def get(self):
		self.render("gender.html")
	def post(self):
		userinfo["Gender"]=self.request.get("Gender")
		print userinfo
		self.redirect('/gender_preference')


class Gender_Pref(Handler):
	def get(self):
		self.render("gender_preference.html")
	def post(self):
		userinfo["Gender_Pref"]=self.request.get("Gender_Pref")
		print userinfo
		self.redirect('/dob')

#Page of date of birth
class DOB(Handler):
	def get(self):
		self.render("dob.html")
	def post(self):
		dob = self.request.get("DOB")
		if dob !=  '' :
			userinfo["DOB"] = dob
			print userinfo
			self.redirect('/about-yourself')
		else:
			self.redirect('/dob')

#Optional Input for 'About You?'
class AboutYou(Handler):
	def get(self):
		self.render("about-yourself.html")
	def post(self):
		userinfo["About"]=self.request.get("About")
		print userinfo
		self.redirect('/email')

#Aquire email and SUBMIT
class Email(Handler):
	def get(self):
		self.render("email.html")
	def post(self):
		email = self.request.get("Email")
		if email != '':
			userinfo["Email"] = email
			


		else: 
			self.redirect('/email')
		

		if email != '':
			#Start Computing the Registration

			#Bigin computing the location coordinates
			location = userinfo['Location'] #can have unicode bug
			latitude, longitude = lat_long(location)

			#Save input into the database uncomment this for application
			newuser=UserInfo(Status=userinfo["Status"],firstname=userinfo["firstname"],
				surname=userinfo["surname"],Languages=userinfo["Languages"],
				Gender=userinfo["Gender"], Gender_Pref=userinfo["Gender_Pref"],
				DOB=userinfo["DOB"], About=userinfo["About"], Email=userinfo["Email"],
				Location=str(location), Latitude=latitude, Longitude=longitude)
			#This can be uncommented for debugging. comment the top
			'''newuser=UserInfo(Status="refugee",firstname="Bertold",
				surname="Brecht",Languages=["English"],
				Gender="male", Gender_Pref="any",
				DOB="2000-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
				Location="Laax", Latitude=latitude, Longitude=longitude)'''

			newuser.put()

			#Create fake database. Comment this out later
			#mygetdata= getdata() #Initialise instance of class
			#mygetdata.createdatabase(UserInfo) #Import database
			#Querry the db and 

			#likely stupid and inefficient , but works :) 
			q = UserInfo.all() 
			local = q.filter("Status =", "local").fetch(limit=DATABASE_FETCH_LIMIT)
			
			q = UserInfo.all() 
			refugees = q.filter("Status =", "refugee").fetch(limit=DATABASE_FETCH_LIMIT)
			
			print("newuser: " + str(newuser) + "\n refugees:" + str(refugees)+ "\n locals:"+str(local))
			square, score = get_square(newuser,local,refugees)


			#x = mygetdata.readdatabase(q, newuser) #run readydatabase.py method, readdatabase
			#print x
			#if square exists (not empty)
			if square:

				template_values= ([(person.firstname +' '+ person.surname) for person in square])
				# string = ''.join([person.firstname for person in square])
				# template_values = {'text':string,}
				groupscore=int(score*100) #convert to percentages
				print '------------------'
				print email 
				#Write email to user confirming match
				if mail.is_email_valid(email):
					sender_address = "refugeelighthouse@gmail.com Support <refugeelighthouse@gmail.com>"
					subject = "Confirm your registration"
					body =  """Congratulations on finding a match"""
					mail.send_mail(sender_address, email, subject, body)
					

			else:
				template_values=None
				groupscore=0



			self.render("match.html", template_values=template_values,score=groupscore)








		
#In case of accidental redirect
class Match(Handler):
	def get(self):
		self.render("match.html",template_values=None, score=None)


	def post(self):
		self.redirect('/register')

#Register for an account at refugeelighthouse
#-needs a sequre log in and databasing of informaiton
class Register(Handler):
	def get(self):
		self.render("register.html")

	def post(self):
		self.redirect('/review')

#Send a review
class Review(Handler):
	def get(self):
		self.render("review.html")

	def post(self):
		self.redirect('/thankyou')

class ThankYou(Handler):
	def get(self):
		self.render("thankyou.html")


app = webapp2.WSGIApplication([
	('/', MainPage),
	('/index', Index),
	('/refugee', Names),
	('/languages', Languages),
	('/gender', Gender),
	('/gender_preference', Gender_Pref),
	('/dob', DOB),
	('/about-yourself', AboutYou),
	('/email', Email),
	('/location',Location),
	('/match', Match),
	('/register', Register),
	('/review', Review),
	('/thankyou', ThankYou),

], debug=True)


#Function from Vojta, move away from here
def get_square(node,local,refugees):
		""" Returns a quadruplet of nodes refugee-refugee-local-local.
			Incredibly rusty, but will work"""


		frst = local
		scnd = refugees

		# flip the lists if you start with a refugee
		if node.Status == "refugee":
			print("flipped")
			frst = refugees
			scnd = local

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

		return square, (highest/8.0);


