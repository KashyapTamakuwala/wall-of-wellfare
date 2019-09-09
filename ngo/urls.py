from django.urls import path
from django.conf.urls import url,include
from ngo.views import nhome,registerneed,logout,seedonations,drequest,acrequest,derequest
urlpatterns = [ 
    path('',nhome, name='index'),
    path('rneed/',registerneed, name='rneed'),
    path('sdonations/',seedonations, name='donations'),
    path('logout/',logout, name='logout'),
    path('request/',drequest, name='request'),
    path('accept/',acrequest, name='accept'),
    path('decline/',derequest, name='decline'),
]