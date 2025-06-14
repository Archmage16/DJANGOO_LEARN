from django.urls import path
from django.views.generic.base import RedirectView

from . import views
from .apps import PollsConfig
app_name = PollsConfig.name
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.QuesDetailView.as_view(), name='detail'),
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:choice_id>/votes/', views.votes, name='votes'),
    path('paginator/', views.paginator, name='paginator'),

    # path('question/', views.question, name='question'),
    path('question/', views.AddQues.as_view(), name='question'),
    path('question/question-suc/', views.Suc.as_view(), name='question-suc'),

    path('choice/', views.choices, name='choices'),

    # Greeting
    path('Teacher/', views.TeacherGreet.as_view(), name='teacher'),
    path('Student/', views.StudentGreet.as_view(), name='student'),
    path('redirect/', RedirectView.as_view(pattern_name='polls:index'), name='redirect'),
]