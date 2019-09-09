from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from login.models import User,details
from donarsite.models import accepteddonations
from ngo.models import needs
from django import template
# Create your views here.
@login_required(login_url='/wallofwellfare/')
def ahome(request):
    t=request.session['type']
    if t == "admin":  
        c={}
        c.update(csrf(request))
        return render(request,'admins/index.html',c)
    else:
        del request.session['username']
        del request.session['type']
        return HttpResponseRedirect("/wallofwellfare/")

@login_required(login_url='/wallofwellfare/')
def donationtable(request):
    x=accepteddonations.objects.filter(status="A")
    args={'x':x}
    return render(request,'admins/donation.html',args)

@login_required(login_url='/wallofwellfare/')
def pendingtable(request):
    x=needs.objects.filter(status='p')
    args={'x':x}
    return render(request,'admins/pending.html',args)

@login_required(login_url='/wallofwellfare/')
def solvedtable(request):
    x=needs.objects.filter(status='f')
    args={'x':x}
    return render(request,'admins/solved.html',args)


@login_required(login_url='/wallofwellfare/')
def donortable(request):
    x=User.objects.filter(type="Donar")
    args={'x':x,}
    return render(request,'admins/donar.html',args)

@login_required(login_url='/wallofwellfare/')
def ngotable(request):
    x=User.objects.filter(type="ngo")
    args={'x':x,}
    return render(request,'admins/ngo.html',args)

