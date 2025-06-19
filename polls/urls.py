from django.urls import path
from django.views.generic.base import RedirectView

from . import views
from .apps import PollsConfig
app_name = PollsConfig.name
urlpatterns = [
    path('', views.QuestionListView.as_view(), name='index'),
    path('all/', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.QuesDetailView.as_view(), name='detail'),
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:choice_id>/votes/', views.votes, name='votes'),
    path('paginator/', views.QuestionListView.as_view(), name='paginator'),

    # path('question/', views.question, name='question'),
    path('question/', views.AddQues.as_view(), name='question'),
    path('question/question-suc/', views.QuesSuc.as_view(), name='question-suc'),
    path('question/create/', views.QuesCreateeView.as_view(), name='question-create'),
    path('question/update/<int:question_id>', views.QuesUpdateView.as_view(), name='question-update'),
    path('question/delete/<int:question_id>', views.QuesDeleteView.as_view(), name='question-delete'),

    path('choice/', views.choices, name='choices'),

    path('choice/choice-suc/', views.ChoiceSuc.as_view(), name='choice-suc'),
    path('<int:question_id>/choices/choiceList/', views.ChoiceListView.as_view(), name='choice-list'),
    path('choice/create/', views.ChoiceCreateeView.as_view(), name='choice-create'),
    path('choice/update/<int:question_text_id>', views.ChoiceUpdateView.as_view(), name='choice-update'),
    path('choice/delete/<int:question_text_id>', views.ChoiceDeleteView.as_view(), name='choice-delete'),
    
    
    # Greeting
    path('Teacher/', views.TeacherGreet.as_view(), name='teacher'),
    path('Student/', views.StudentGreet.as_view(), name='student'),
    path('redirect/', RedirectView.as_view(pattern_name='polls:index'), name='redirect'),
]