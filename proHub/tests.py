from django.test import TestCase
from .models import Profile, User, Projects, Rating, Comment

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User()
        self.user.save()
        self.profile = Profile(user = self.user, profile_pic = 'img', name = 'img', bio = 'I am Levlest', country = 'Kenya', email = 'test@gmail.com')
        
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
        
        
class ProjectsImageClass(TestCase):
    def setUp(self):
        self.user = User()
        self.user.save()
        self.profile= Profile(user = self.user, profile_pic = 'img', name = 'img', bio = 'I am Levlest', country = 'Kenya', email = 'test@gmail.com')
        self.profile.save()
        self.project = Projects(name = 'name', description = 'description', project_image = 'img', url = 'url', pub_date = 'date', user = self.user, profile = self.profile)
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Projects)) 
        
    # Testing Save Method
    def test_save_method(self):  
        self.project.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) > 0)
        
    def tearDown(self):
        Projects.objects.all().delete() 
        Profile.objects.all().delete() 
        User.objects.all().delete()   
      
    def test_delete_project(self):
        self.project.save_project()
        projects = Projects.objects.all()
        self.assertEqual(len(projects),1)
        self.project.delete_project()
        del_project=Projects.objects.all()
        self.assertEqual(len(del_project),0)        
        
        
class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User()
        self.user.save()
        self.profile= Profile(user = self.user, profile_pic = 'img', name = 'img', bio = 'I am Levlest', country = 'Kenya', email = 'test@gmail.com')
        self.profile.save()
        self.project = Projects(name = 'name', description = 'description', project_image = 'img', url = 'url', pub_date = 'date', user = self.user, profile = self.profile)
        self.project.save()
        self.comment = Comment(comment = 'This is lovely', user = self.user, project = self.project)
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))        
        
    # Testing Save Method
    def test_save_method(self):  
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)    
        
    def tearDown(self):
        User.objects.all().delete() 
        Profile.objects.all().delete()        
        Projects.objects.all().delete() 
        Comment.objects.all().delete() 
        
    def test_delete_comment(self):
        self.comment.save_comment()
        comments=Comment.objects.all()
        self.assertEqual(len(comments),1)
        self.comment.delete_comment()
        del_comments=Comment.objects.all()
        self.assertEqual(len(del_comments),0)        
        
        
class RatingTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User()
        self.user.save()
        self.profile= Profile(user = self.user, profile_pic = 'img', name = 'img', bio = 'I am Levlest', country = 'Kenya', email = 'test@gmail.com')
        self.profile.save()
        self.project = Projects(name = 'name', description = 'description', project_image = 'img', url = 'url', pub_date = 'date', user = self.user, profile = self.profile)
        self.project.save()
        self.rating = Rating(user = self.user, project = self.project, post_date = 'date', usability = 0, design = 0, creativity = 0, content = 0, mobile = 0)
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rating,Rating))        
        
    # Testing Save Method
    def test_save_method(self):  
        self.rating.save_rating()
        ratings = Rating.objects.all()
        self.assertTrue(len(ratings) > 0)    
        
    def tearDown(self):
        User.objects.all().delete() 
        Profile.objects.all().delete() 
        Projects.objects.all().delete() 
        Rating.objects.all().delete() 
        
    def test_delete_rating(self):
        self.rating.save_rating()
        ratings=Rating.objects.all()
        self.assertEqual(len(ratings),1)
        self.rating.delete_rating()
        del_rating=Rating.objects.all()
        self.assertEqual(len(del_rating),0)                                          