from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.fields import TextField
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic', blank=True)
    name =  models.CharField(max_length =30, blank=True)
    bio = models.CharField(max_length =200, blank=True)
    location=models.CharField(max_length=50)
    email=models.EmailField()
  
    def __str__(self):
        return self.user.username
      
    def save_profile(self):
        self.save()
          
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def update_profile(cls,id,profile_pic,name,bio):
        cls.objects.filter(id=id).update(profile_pic=profile_pic,name=name,bio=bio)   
        
    @classmethod
    def get_user(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile
    
    
class Projects(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()
  project_image = CloudinaryField('project_images')
  urls = models.URLField()
  pub_date = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE, null=True)
  voters = models.IntegerField(default=0)


  def __str__(self):
    return self.name

  def save_project(self):
    self.save()
  
  def delete_project(self):
    self.delete()

  def voters_num(self):
    return self.voters.count()

  @classmethod
  def get_all_projects(cls):
    return cls.objects.all()

  @classmethod
  def get_project(cls,id):
    return Projects.objects.get(id=id)

  @classmethod
  def search_project(cls,name):
    return cls.objects.filter(name__icontains=name)

  @classmethod
  def user_projects(cls,profile):
    return cls.objects.filter(profile=profile)  

class Meta:
  ordering=['-pub_date']