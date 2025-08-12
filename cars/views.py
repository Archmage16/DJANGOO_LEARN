from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import SpareForm
from cars.models import Spare, Machine, Kit
from django.http import HttpResponse

# Create your views here.
class IndexCars(TemplateView):
    template_name = 'cars/cars.html'

# class SparesView(TemplateView):
#     template_name = 'cars/spares.html'

def SparesView(request):
    spares = Spare.objects.all()
    cont = {
        'spares': spares
    }
    return render(request, 'cars/spares.html', cont)

def create_spares(request):
    if request.method == 'POST':
        form = SpareForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Spare created successfully!')
        else:
            print('hi')
    else:
        form = SpareForm()
    return render(request, 'cars/spareForm.html', {'form': form})