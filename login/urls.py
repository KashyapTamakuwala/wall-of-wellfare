
from django.urls import path
from django.conf.urls import url,include
from login.views import mylogin,autho,Register,Rdata
from django.contrib.auth.views import LoginView
urlpatterns = [ 
    path('',mylogin, name='index'),
    path('authenticate/',autho, name='auth'),
    path('Register/',Register, name='reg'),
    path('rdata',Rdata, name='regdata'),
    ]
