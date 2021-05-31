from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import CreateProfileForm
from django.http import HttpResponseRedirect,Http404
from .email import send_welcome_email
from .models import Comment, Profile, Projects
from .forms import NewSiteForm, RatingForm, UpdateProfile
import datetime as dt
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectsSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
def homepage(request):
  date=dt.date.today()
  projects = Projects.objects.all()
  
  return render(request, 'main/home.html', {"date":date, "projects":projects})

def about(request):
  
  return render(request, 'main/about.html')

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
    profile = Profile.get_user(username)
    projects = Projects.user_projects(username)
    
    return render(request, 'profile/user_profile.html', {"profile": profile, "projects":projects })
  
@login_required
def new_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewSiteForm(request.POST, request.FILES)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = current_user
            site.save()
        return redirect('home')

    else:
        form = NewSiteForm()
    return render(request, 'project/submit_site.html', {"form": form})

@login_required  
def search(request):

    if 'search' in request.GET and request.GET["search"]:
        name = request.GET.get("search")
        searched_projects = Projects.search_project(name)
        print(searched_projects)
        message = f"{name}"

        return render(request, 'project/search_project.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'project/search_project.html',{"message":message})

def single_site(request,project_id):
    comments = Comment.objects.all()
    try:
        project = Projects.objects.get(id = project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"project/single_site.html", {"project":project, "comments":comments})

@login_required
def comment(request,project_id):
    '''
    Method to add post comments
    '''
    project = Projects.objects.get(pk=project_id)
    comments = request.GET.get("comments")
    current_user = request.user
    comment= Comment(project = project, comment = comments, user = current_user)
    comment.save_comment()

    return redirect('single_site', project.pk)

@login_required
def update_profile(request,username):
  user=User.objects.get(username=username)
  current_user = request.user
  
  if request.method =='POST':
    form = UpdateProfile(request.POST,request.FILES, instance=current_user.profile)
    
    if form.is_valid():
      form.save()
      return redirect('profile', user.username)
  
  else:
    form = UpdateProfile(instance=current_user.profile)
  
  return render(request,"profile/update_profile.html", {"form":form})




class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data)
      
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    
class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)    
      
      
class ProjectsList(APIView):
    permission_classes = (IsAdminOrReadOnly,)  
    def get(self, request, format=None):
        projects = Projects.objects.all()
        serializers = ProjectsSerializer(projects, many=True)
        return Response(serializers.data)      
      
    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
    