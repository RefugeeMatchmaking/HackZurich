from django import forms
from .models import User

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['refugee_or_local', 'first_name', 'last_name', 'location', 'occupation', 'about', 'picture', 'email', 'gender', 'gender_preference', 'birthdate', 'social_media']