from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm
from django.http import HttpResponseRedirect,Http404

# Create your views here.
@login_required
def homepage(request):
  
  return render(request, 'home.html')

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
