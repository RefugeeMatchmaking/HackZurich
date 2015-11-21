from django.db import models
from django.utils import timezone
from django.conf import settings
from ipware.ip import get_ip
import uuid
import sys


#Self created functions
from users.algorithms.lat_long import lat_long

class User(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    GENDERPREF = (
        ('S', 'Same'),
        ('A','Any'),
        )
    STATUS = (
        ('R', 'Refugee'),
        ('L', 'Local'),
    )
    user_key = models.CharField(max_length=10, editable=False, primary_key=True, unique=True)
    refugee_or_local = models.CharField(choices=STATUS, max_length=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    about = models.TextField()
    #picture = models.ImageField(blank=True)
    email = models.EmailField(max_length=254)
    gender = models.CharField(choices=GENDER, max_length=1)
    gender_preference = models.CharField(blank=True, choices=GENDERPREF, max_length=1)
    birthdate = models.DateField()
    social_media = models.URLField(max_length=200, blank=True)
    submitted  = models.DateTimeField(default=timezone.now, editable=False)
    submission_ip = models.GenericIPAddressField(protocol='both', blank=True, null=True, editable=False)

    #Add Password Field
    #Add Flag Field ('Normal', 'Reported', 'Malicious')
    #Add Matched Field ('Waiting', 'Matched')

    def latitude_longitude(self):
        """ Method to get the latitude and logitude and create a property """
        mylat_long=lat_long(self.location)
        return mylat_long
    #This is really slow!! We want to be calling the database for the lat long values. Not calling the function to compute it    
    
    #latitude_longitude=property(t_latitude_longitude)


    def save(self):
        if not self.user_key:
            self.user_key = uuid.uuid1().hex[:10]
        super(User, self).save()

    #For better printing of the user in the database
    def __str__(self):
        return self.last_name

class Language(models.Model):
	language = models.CharField(max_length=7, choices=settings.LANGUAGES)
	user = models.ForeignKey(User)
	def __str__(self):
		return self.language