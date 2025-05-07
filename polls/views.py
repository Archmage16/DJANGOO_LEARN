from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("<h1>Welcome to the POLLS</h1>")
def hiWorld(req):
    return HttpResponse("Hello Django!")