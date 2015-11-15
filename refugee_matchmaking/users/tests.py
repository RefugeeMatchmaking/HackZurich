from django.test import TestCase
from django.test import Client

from .models import *

# Create your tests here.
client=Client()


#Test to check if the input form is working correctly
class Matchmaking_Test(TestCase):
	def test_user_submission(self):
		resp=self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'PJtest', 'last_name': 'JayathissaTest', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'birthdate':'1988-09-27', 'social_media':'http://www.example.com' })
		print(resp.context)
		self.assertEqual(resp.context, None)

	def test_scoring(self):
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Mike', 'last_name': 'Ong', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'birthdate':'1989-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Karim', 'last_name': 'karim', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'birthdate':'1984-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Ali', 'last_name': 'aladin', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'birthdate':'1985-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Ognyan', 'last_name': 'theognyan', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'birthdate':'1982-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Karl', 'last_name': 'Wruck', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'birthdate':'1985-09-27', 'social_media':'http://www.example.com' })
		resp=self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Sara', 'last_name': 'Akhbar', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'birthdate':'1982-09-27', 'social_media':'http://www.example.com' })
		print(resp.content)