from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jam(requst):
    return HttpResponse('<h1><marquee>Hello How r u</h1></marquee>')
