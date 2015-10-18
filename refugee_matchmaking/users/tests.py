from django.test import TestCase
from django.test import Client

# Create your tests here.
client=Client()


#Test to check if the matchmaking algorithm is functioning correctly
class Matchmaking_Test(TestCase):
	def test_user_submission(self):
		resp=self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'PJtest', 'last_name': 'JayathissaTest', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'birthdate':'1988-09-27', 'social_media':'http://www.example.com' })
		print(resp.context)

