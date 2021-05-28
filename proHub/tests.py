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