from django.urls import path
from django.views.generic.base import RedirectView

from . import views
from .apps import CarsConfig
app_name = CarsConfig.name
urlpatterns = [
    path('', views.IndexCars.as_view(), name='index'),
]