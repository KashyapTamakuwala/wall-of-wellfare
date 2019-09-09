from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from login.models import User,details
from django.db import IntegrityError
import traceback
# Create your views here.
def mylogin(request):
   c={}
   c.update(csrf(request))
   return render(request,'login/index.html',c)

def autho(request):
   try:
      username=request.POST.get('username','')
      password=request.POST.get('pass','')
      x=auth.authenticate(username=username,password=password)
      y=x.type
      if x is not None:
         auth.login(request,x)
         request.session['username']=username
         request.session['type']=y
         if y == "Donar":
            return HttpResponseRedirect("/donar/")
         elif y == "ngo" :
            return HttpResponseRedirect("/ngo/")
         elif y == "admin":
            return HttpResponseRedirect("/admins/")
      else:
         return HttpResponse("invalid")
   except:
      r="invalid username"
      r1="invalid password"
      return render(request,'login/index.html',{"error":r,"error2":r1})
      

def Register(request):
   c={}
   c.update(csrf(request))
   return render(request,'login/Registration.html')

def Rdata(request):
   msg=None
   try:
      uname=request.POST.get('username','')
      fname=request.POST.get('fname','')
      lname=request.POST.get('lname','')
      pa=request.POST.get('pass','')
      number=request.POST.get('contact','')
      eid=request.POST.get('email','')
      add=request.POST.get('add','')
      state=request.POST.get('state','')
      city=request.POST.get('city','')
      ty=request.POST.get('type','')
      a=User.objects.create_user(uname,eid,pa)
      a.first_name=fname
      a.last_name=lname
      a.type=ty
      a.save()
      b=details(username=a,Contact=number,Address=add,City=city,State=state)
      b.save()
      if a is not None and b is not None:
         return HttpResponseRedirect('/wallofwellfare/')
      else:
         return HttpResponse("UNSUCCESFULL")
   except IntegrityError as e:
      msg="USERNAME ALREADY TAKEN"
      return render(request,'login/Registration.html',{'msg':msg})