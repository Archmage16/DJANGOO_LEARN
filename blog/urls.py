from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.user, name='user'),
    path('<str:username>/<str:title>', views.post, name='post'),
]