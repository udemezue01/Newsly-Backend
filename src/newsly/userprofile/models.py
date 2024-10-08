from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user             =  models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    bio 			= models.CharField(blank = True, max_length = 3000)
    twitter 		= models.CharField(blank = True, max_length = 3000)

    def __str__(self):
        return str(self.user)