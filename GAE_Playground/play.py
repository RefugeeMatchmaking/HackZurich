import os
import webapp2
import jinja2
import hmac #Used for hashing 
import re #regular expressions

SECRET='pjiscool'


from google.appengine.ext import db

tempplate_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(tempplate_dir), autoescape=True)

userinfo={"Status":"","firstname":"","surname":"","Languages":[],"Gender":"","Gender_Pref":"","DOB":"",
	"About":"","Email":""}

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
		print (str(userinfo))		
		self.redirect('/refugee')

class Names(Handler):
	def get(self):
		self.render("refugee.html")


	def post(self):
		first = self.request.get("firstname")
		last = self.request.get("surname")
		
		userinfo["firstname"] = first
		userinfo["surname"] = last

		if first != '' and last != '': 
			print userinfo	
			self.redirect('/languages')
		else: 
			self.redirect('/refugee')
			print("Choose a valid name - print this" )
			pass;

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
			self.redirect('/gender')
		else:
			self.redirect('/languages')

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
		dob = self.request.get("DOB")
		if dob !=  '' :
			userinfo["DOB"] = dob
			print userinfo
			self.redirect('/about-yourself')
		else:
			self.redirect('/dob')

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
		email = self.request.get("Email")
		if email != '':
			userinfo["Email"] = email
			print userinfo
			self.redirect('/match')
		else: 
			self.redirect('/email')
		

class Match(Handler):
	def get(self):
		self.render("match.html")
		print'-------------------------------'
		print userinfo
		newuser=UserInfo(Status=userinfo["Status"],firstname=userinfo["firstname"],
			surname=userinfo["surname"],Languages=userinfo["Languages"],
			Gender=userinfo["Gender"], Gender_Pref=userinfo["Gender_Pref"],
			DOB=userinfo["DOB"], About=userinfo["About"], Email=userinfo["Email"])

		newuser.put()

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


