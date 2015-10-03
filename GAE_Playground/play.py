import os
import webapp2
import jinja2
import hmac #Used for hashing 
import re #regular expressions

SECRET='pjiscool'


from google.appengine.ext import db

tempplate_dir= os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(tempplate_dir), autoescape=True)

userinfo={"Status":"","firstname":"","surname":"","Languages":[],"Gender":"","Gender_Pref":"","DOB":"",
	"About":"","email":""}

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
		userinfo={"Status":"","firstname":"","surname":"","Languages":[],"Gender":"","Gender_Pref":"","DOB":"",
	"About":"","Email":""}
		self.render("index.html")

	def post(self):
		userinfo["Status"]=self.request.get("Status")
		print userinfo		
		self.redirect('/refugee')

class Names(Handler):
	def get(self):
		self.render("refugee.html")


	def post(self):
		userinfo["firstname"]=self.request.get("firstname")
		userinfo["surname"]=self.request.get("surname")
		print userinfo	
		self.redirect('/languages')



class Languages(Handler):
	def get(self):
		self.render("languages.html")
	def post(self):
		q=[]
		q.append(self.request.get("native"))
		q.append(self.request.get("foreign1"))
		q.append(self.request.get("foreign2"))
		userinfo["Languages"]=q
		print userinfo	
		self.redirect('/gender')

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

class DOB(Handler):
	def get(self):
		self.render("dob.html")
	def post(self):
		userinfo["DOB"]=self.request.get("DOB")
		print userinfo
		self.redirect('/about-yourself')

class AboutYou(Handler):
	def get(self):
		self.render("about-yourself.html")
	def post(self):
		userinfo["About"]=self.request.get("About")
		print userinfo
		self.redirect('/email')

class Email(Handler):
	def get(self):
		self.render("email.html")
		print 'email received'
	def post(self):
		userinfo["Email"]=self.request.get("Email")
		print 'i was here'
		print userinfo
		self.redirect('/match')

class Match(Handler):
	def get(self):
		self.render("match.html")
		print'-------------------------------'
		print userinfo



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


