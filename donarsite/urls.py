from django.urls import path
from django.conf.urls import url,include
from donarsite.views import dhome,about,activity,contact,dupdate,logout
from django.contrib.auth.views import LoginView
urlpatterns = [ 
    path('',dhome, name='index'),
    path('aboutme',about, name='aboutme'),
    path('activity/',activity, name='activity'),
    path('contact/',contact, name='contact'),
    path('dupdate/',dupdate, name='update'),
    path('logout/',logout, name='logout'),
    ]