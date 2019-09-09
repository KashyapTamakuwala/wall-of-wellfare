from django.urls import path
from django.conf.urls import url,include
from admins.views import ahome,donationtable,pendingtable,solvedtable,donortable,ngotable
urlpatterns = [ 
    path('',ahome, name='index'),
    path('donations/',donationtable, name='dtable'),
    path('pending/',pendingtable, name='pending'),
    path('solved/',solvedtable, name='solved'),
    path('donar/',donortable, name='donar'),
    path('ngo/',ngotable, name='ngo'),
]