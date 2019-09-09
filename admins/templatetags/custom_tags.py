from django import template
from login.models import User,details
from donarsite.models import accepteddonations
from ngo.models import needs

register=template.Library()

@register.simple_tag
def get_co(pk):
    obj = details.objects.get(username=pk)
    ci=obj.City
    ad=obj.Address
    return obj.Contact

@register.simple_tag
def get_st(pk):
    obj = details.objects.get(username=pk)
    return obj.State

@register.simple_tag
def get_ci(pk):
    obj = details.objects.get(username=pk)
    return obj.City

@register.simple_tag
def get_add(pk):
    obj = details.objects.get(username=pk)
    return obj.Address