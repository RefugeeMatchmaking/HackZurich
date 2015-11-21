from django.test import TestCase
from django.test import Client

from .models import *

# Create your tests here.
client=Client()


#Test to check if the input form is working correctly
class Matchmaking_Test(TestCase):
	def test_user_submission(self):
		resp=self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'PJtest', 'last_name': 'JayathissaTest', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'en', 'language_2':'es', 'language_3':'pl','birthdate':'1988-09-27', 'social_media':'http://www.example.com' })
		print(resp.context)
		self.assertEqual(resp.context, None)

	def test_scoring(self):
		resp=self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'PJtest', 'last_name': 'JayathissaTest', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'es', 'language_2':'en', 'language_3':'ger','birthdate':'1988-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Mike', 'last_name': 'Ong', 'location':'Berlin', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'S', 'language_1':'es', 'language_2':'en', 'language_3':'pl', 'birthdate':'1989-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Karim', 'last_name': 'karim', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, baseball', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1984-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Ali', 'last_name': 'aladin', 'location':'Rome', 'occupation':'Architect', 'about':'violin, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'F', 'gender_preference':'S', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1985-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Ognyan', 'last_name': 'theognyan', 'location':'Zurich', 'occupation':'Architect', 'about':'running, guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1982-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Karl', 'last_name': 'Wruck', 'location':'Bern', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'F', 'gender_preference':'A', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1985-09-27', 'social_media':'http://www.example.com' })
		resp=self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Sara', 'last_name': 'Akhbar', 'location':'Rapperswil', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'es', 'language_2':'en', 'language_3':'es', 'birthdate':'1982-09-27', 'social_media':'http://www.example.com' })
		#I would love to be able to access the score here so I could run a assertEqual on it

	def test_language(self):
		resp=self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'PJtest', 'last_name': 'JayathissaTest', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'es', 'language_2':'en', 'language_3':'ger','birthdate':'1988-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Mike', 'last_name': 'Ong', 'location':'Berlin', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'S', 'language_1':'es', 'language_2':'en', 'language_3':'pl', 'birthdate':'1989-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Karim', 'last_name': 'karim', 'location':'Zurich', 'occupation':'Architect', 'about':'guitar, baseball', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1984-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Ali', 'last_name': 'aladin', 'location':'Rome', 'occupation':'Architect', 'about':'violin, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'F', 'gender_preference':'S', 'language_1':'jpn', 'language_2':'jpn', 'language_3':'jpn', 'birthdate':'1985-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Ognyan', 'last_name': 'theognyan', 'location':'Zurich', 'occupation':'Architect', 'about':'running, guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1982-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Karl', 'last_name': 'Wruck', 'location':'Bern', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'F', 'gender_preference':'A', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1985-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Ali', 'last_name': 'aladin', 'location':'Rome', 'occupation':'Architect', 'about':'violin, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'F', 'gender_preference':'S', 'language_1':'it', 'language_2':'it', 'language_3':'it', 'birthdate':'1985-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Ognyan', 'last_name': 'theognyan', 'location':'Zurich', 'occupation':'Architect', 'about':'running, guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1982-09-27', 'social_media':'http://www.example.com' })
		self.client.post('/',{'refugee_or_local': 'L', 'first_name': 'Karl', 'last_name': 'Wruck', 'location':'Bern', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'F', 'gender_preference':'A', 'language_1':'en', 'language_2':'en', 'language_3':'en', 'birthdate':'1985-09-27', 'social_media':'http://www.example.com' })
		resp=self.client.post('/',{'refugee_or_local': 'R', 'first_name': 'Sara', 'last_name': 'Akhbar', 'location':'Rapperswil', 'occupation':'Architect', 'about':'guitar, tennis', 'email':'p.jayatthissa@gmail.com', 'gender':'M', 'gender_preference':'A', 'language_1':'es', 'language_2':'en', 'language_3':'es', 'birthdate':'1982-09-27', 'social_media':'http://www.example.com' })
		