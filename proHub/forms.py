from django import forms
from .models import Profile, Projects

class CreateProfileForm(forms.ModelForm):  
    class Meta:
        model = Profile
        exclude = ['user']
        
        
class NewSiteForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['urls', 'profile', 'user', 'pub_date', 'voters']
                