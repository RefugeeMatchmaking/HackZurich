from django import forms
from .models import User

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		#fields = ['refugee_or_local', 'first_name', 'last_name', 'location', 'occupation', 'about', 'picture', 'email', 'gender', 'gender_preference', 'birthdate', 'social_media']
		fields = ['refugee_or_local', 'first_name', 'last_name', 'location', 'occupation', 'about', 'email', 'gender', 'gender_preference', 'language1','language2','language3','birthdate', 'social_media']