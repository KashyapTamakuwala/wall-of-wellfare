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
from django.core.mail import EmailMessage,send_mail
# Create your views here.
@login_required(login_url='/wallofwellfare/')
def nhome(request):
    t=request.session['type']
    if t == "ngo":
        c={}
        c.update(csrf(request))
        return render(request,'ngo/index.html',c)
    else:
        del request.session['username']
        del request.session['type']
        return HttpResponseRedirect("/wallofwellfare/")

@login_required(login_url='/wallofwellfare/')
def registerneed(request):
    ntype=request.POST.get('type','')
    des=request.POST.get('description','')
    username=request.session['username']
    v=User.objects.get(username=username)
    status='p'
    n=needs(ntype=ntype,description=des,status=status,nname=v)
    n.save()
    if n is not None:
        return HttpResponseRedirect('/ngo/')
    else:
        return HttpResponse('error')

@login_required(login_url='/wallofwellfare/')
def seedonations(request):
    username=request.session['username']
    d=accepteddonations.objects.filter(nmame=username,status="A")
    return render(request,'ngo/table.html',{'d':d})


@login_required(login_url='/wallofwellfare/')
def drequest(request):
    username=request.session['username']
    d=accepteddonations.objects.filter(nmame=username,status="R")
    return render(request,'ngo/table2.html',{'d':d})

def acrequest(request):
    id=request.POST.get('id','')
    d=accepteddonations.objects.get(id=id)
    d.status="A"
    d.save()
    u=User.objects.get(username=d.nmame)
    n=needs.objects.get(ntype=d.dtype,nname_id=u.id)
    n.status="f"
    n.save()
    # ngo email
    to=u.email 
    # donar details
    v=User.objects.get(username=d.dname)
    k=details.objects.get(username=v.id)
    # setting body
    body="%s has donated to your ngo address for pick up %s"%(v.first_name,k.Address)
    # sending mail
    email=EmailMessage('dontations',body,to=[to])
    email.send()
    return HttpResponseRedirect('/ngo/request/')

def derequest(request):
    id=request.POST.get('id','')
    d=accepteddonations.objects.get(id=id)
    d.delete()
    return HttpResponseRedirect('/ngo/request/')



@login_required(login_url='/wallofwellfare/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/wallofwellfare/')