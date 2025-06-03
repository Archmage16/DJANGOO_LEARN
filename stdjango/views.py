from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(req):
    return render(req, 'main.html')
