from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    
    def __str__(self):
        return str(self.first_name)+" "+str(self.last_name)

