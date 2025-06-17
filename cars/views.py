from django.shortcuts import render
from django.views.generic.base import TemplateView
from cars.models import Spare, Machine, Kit

# Create your views here.
class IndexCars(TemplateView):
    template_name = ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Machine.objects.all()
        return context