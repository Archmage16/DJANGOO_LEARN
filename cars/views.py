from django.shortcuts import render
from django.views.generic.base import TemplateView
from cars.models import Spare, Machine, Kit

# Create your views here.
class IndexCars(TemplateView):
    template_name = 'cars/cars.html'