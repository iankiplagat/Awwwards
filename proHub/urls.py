from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage, name = 'home'),
    path('create_profile/', views.create_profile, name='create_profile'),
]
