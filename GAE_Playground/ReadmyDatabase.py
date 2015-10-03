

class getdata():

	def createdatabase(self,UserInfo):
		newuser=UserInfo(Status="refugee",firstname="Arnold",
			surname="Schwarzeneger",Languages=["English"],
			Gender="male", Gender_Pref="anyone",
			DOB="2000-30-6", About="lorem ipsum", Email="lorem@lorem.uk",
			Location="Laax")

		newuser.put()



	def readdatabase(self, database):
		self.q=database


		return "Hello PJ"

		#q.filter("Status"="Refugee")


db = getdata()

db.createdatabase