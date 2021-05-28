from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage, name = 'home'),
    path('email/',views.welcome_mail,name='email'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile/<username>',views.user_profile,name='profile'),
]
