from django.urls import path
from django.views.generic.base import RedirectView

from . import views
from .apps import CarsConfig
app_name = CarsConfig.name
urlpatterns = [
    path('', views.IndexCars.as_view(), name='index'),
    
    path('create_spares/', views.create_spares, name='create_spares'),
    path('spares/', views.SparesView, name='spares'),
         
]