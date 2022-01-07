from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.views.generic.edit import CreateView
from . models import *

from adminapp.models import Branch, StuRegistration

def index(request):
    return render(request,"adminapp/index.html")

class SturegCreat(CreateView):
    model=StuRegistration
    fields=['email','password','course','regDate','totalfee','discountfee','paymentRefNo','staffId','branch','remark','regStatus']
    success_url="reg"




