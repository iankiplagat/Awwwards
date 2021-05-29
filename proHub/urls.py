from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.homepage, name = 'home'),
    path('email/',views.welcome_mail,name='email'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile/<username>',views.user_profile,name='profile'),
    path('new/site', views.new_site, name='new_site'),
    path('search/', views.search, name='search'),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectsList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
