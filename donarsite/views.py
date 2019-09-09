from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from login.models import User,details
from ngo.models import needs
from donarsite.models import accepteddonations
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import datetime
# Create your views here.
@login_required(login_url='/wallofwellfare/')
def dhome(request):
    t=request.session['type']
    if t == "Donar":
        c = {}
        c.update(csrf(request))
        ty = request.POST.get('type','')
        if ty is "":
            ty="money"
        x = needs.objects.filter(ntype=ty,status="p")
        con = { 'c': c,'x': x,'ty':ty}
        return render(request, 'donar/index.html',con)
    else:
        del request.session['username']
        del request.session['type']
        return HttpResponseRedirect("/wallofwellfare/")
@login_required(login_url='/wallofwellfare/')   
def about(request):
    return render(request,"donar/about.html")
@login_required(login_url='/wallofwellfare/')
def activity(request):
    name=request.session['username']
    y=User.objects.get(username=name)
    x=accepteddonations.objects.filter(status="A",dname=y.id)
    args={'x':x}
    return render(request,"donar/activity.html",args)
@login_required(login_url='/wallofwellfare/')
def contact(request):
    return render(request,"donar/contact.html")
@login_required(login_url='/wallofwellfare/')
def dupdate(request):
    t=request.POST.get('t','')
    ngo=request.POST.get('ngos','')
    n=request.session['username']
    v=User.objects.get(username=n)

    date=datetime.date.today()
    d='x'
    d=accepteddonations(dname=v,dtype=t,nmame=ngo,date=date,status="R")
    d.save()
    
    if d is not None:
        return HttpResponseRedirect('/donar/')
    else:
        return HttpResponse("error")
@login_required(login_url='/wallofwellfare/')
def logout(request):
    auth.logout(request)
    # del request.session['username']
    return HttpResponseRedirect('/wallofwellfare/')
