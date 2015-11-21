from django import forms
from .models import User, Language
from django.contrib.admin import widgets  

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		#fields = ['refugee_or_local', 'first_name', 'last_name', 'location', 'occupation', 'about', 'picture', 'email', 'gender', 'gender_preference', 'birthdate', 'social_media']
		fields = ['refugee_or_local', 'first_name', 'last_name', 'location', 'occupation', 'about', 'email', 'gender', 'gender_preference', 'birthdate', 'social_media']
		help_texts = {
            'birthdate': ('eg: year-month-day'),
            }
		widgets = {
            'birthdate': forms.DateInput(attrs={'class':'datepicker'}),
        }


