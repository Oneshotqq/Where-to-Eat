from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here.
def home_Page (request: HttpRequest) :
    return render (request , "Wteapp/base.html")