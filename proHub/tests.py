from django.test import TestCase
from .models import Profile, User

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User()
        self.user.save()
        self.profile = Profile(user = self.user, profile_pic = 'img', name = 'img', bio = 'I am Levlest')
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    # Testing Save Method
    def test_save_method(self):  
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
    def tearDown(self):
        Profile.objects.all().delete()
     
    # Testing Delete Method  
    def delete_profile(self):
        self.delete() 
        
    # Testing Update Method    
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.id,'img', 'name', 'I am Levlest')
        update=Profile.objects.get(profile_pic='img',name='name',bio='I am Levlest')
        self.assertEqual(update.bio,'I am Levlest')                          