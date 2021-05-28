from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm
from django.http import HttpResponseRedirect,Http404
from .email import send_welcome_email
from .models import Profile

# Create your views here.
def homepage(request):
  
  return render(request, 'home.html')

@login_required
def welcome_mail(request):
  user=request.user
  email=user.email
  name=user.username
  send_welcome_email(name,email)
  return redirect(create_profile)

@login_required
def create_profile(request):
  current_user=request.user
  if request.method == 'POST':
    form = CreateProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      profile.save()
    return HttpResponseRedirect('/')
  else:
    form = CreateProfileForm()
  return render(request,'profile/create_profile.html',{"form":form})

# Profile page
@login_required
def user_profile(request, username):
    '''
    Method to display a specific user profile
    '''
    # images = Image.get_image_by_user(username)
    profile = Profile.get_user(username)
    
    return render(request, 'profile/user_profile.html', {"profile": profile })
