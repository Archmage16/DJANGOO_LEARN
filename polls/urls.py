from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:choice_id>/votes/', views.votes, name='votes'),
    path('paginator/', views.paginator, name='paginator'),
    path('question/', views.question, name='question'),
    path('choice/', views.choices, name='choices'),
]