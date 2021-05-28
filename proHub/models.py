from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.fields import TextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('photo', blank=True)
    name =  models.CharField(max_length =30, blank=True)
    bio = models.CharField(max_length =200, blank=True)
  
    def __str__(self):
        return self.user.username