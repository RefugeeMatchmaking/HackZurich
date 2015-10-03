from django.db import models
from django.utils import timezone

class Language(models.Model):
	language = models.CharField(max_length=100)

class User(models.Model):
    GENDER = (
        ('0', 'Female'),
        ('1', 'Male'),
        ('2', 'Other'),
    )
    STATUS = (
        ('0', 'Refugee'),
        ('1', 'Local'),
    )
    refugee_or_local = models.IntegerField(choices=STATUS)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    about = models.TextField()
    picture = models.ImageField(blank=True)
    email = models.EmailField(max_length=254)
    langauge = models.ManyToManyField(Language)
    gender = models.IntegerField(choices=GENDER)
    gender_preference = models.PositiveIntegerField(blank=True, choices=GENDER)
    birthdate = models.DateField()
    social_media = models.URLField(max_length=200, blank=True)
    submitted  = models.DateTimeField(default=timezone.now, editable=False)
    submission_ip = models.GenericIPAddressField(protocol='both')
