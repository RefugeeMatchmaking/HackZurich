import os
import webapp2
import jinja2
import hmac #Used for hashing 
import re #regular expressions

SECRET='pjiscool'


from google.appengine.ext import db

tempplate_dir= os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(tempplate_dir), autoescape=True)



def hash_str(s): #funciton to has a string with a secret string
	return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s): #runs the hash_str function to make a secure value
	return "%s|%s" %(s,hash_str(s))

def check_secure_val(h): #checks the input from the browser against our hash
	val=h.split('|')[0]
	if h==make_secure_val(val):
		return val

class UserInfo(db.Model): #used to crete the database. Art is the name of the databse
	user=db.StringProperty(required=True) #required = true adds the constraint
	email=db.StringProperty(required=False)
	#password=db.StringProperty(required=True)
	created=db.DateTimeProperty(auto_now_add=True) #Automatically adds the time, check the docs


class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw): #the * takes unamed arguments, and the ** takes the named arguments
		self.response.out.write(*a,**kw)

	def render_str(self, template, **params):
		t= jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


class Index(Handler):
	def get(self):
		self.render("index.html")


class Names(Handler):
	def get(self):
		self.render("refugee.html")

class Languages(Handler):
	def get(self):
		self.render("languages.html")

class Gender(Handler):
	def get(self):
		self.render("gender.html")

class Gender_Pref(Handler):
	def get(self):
		self.render("gender_preference.html")

class DOB(Handler):
	def get(self):
		self.render("dob.html")

class AboutYou(Handler):
	def get(self):
		self.render("about-yourself.html")

class Email(Handler):
	def get(self):
		self.render("email.html")

class Match(Handler):
	def get(self):
		self.render("refugee.html")



app = webapp2.WSGIApplication([
	('/index', Index),
	('/refugee', Names),
	('/languages', Languages),
	('/gender', Gender),
	('/gender_preference', Gender_Pref),
	('/dob', DOB),
	('/about-yourself', AboutYou),
	('/email', Email),
	('/match', Match),

], debug=True)


