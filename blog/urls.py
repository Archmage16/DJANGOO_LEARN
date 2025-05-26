from django.urls import path

from .apps import BlogConfig
from . import views

app_name = BlogConfig.name
urlpatterns = [
    path('', views.index, name='index'),
    path('tagForm/', views.tagForm, name='tagForm'),
    path('postForm/', views.postForm, name='postForm'),  
    path('profForm/', views.profForm, name='profForm'),
    path('commentForm/', views.commentForm, name='commentForm'),
    
    path('postComment/<str:username>/<str:title>/', views.postComment, name='postComment'),
    path('<str:username>/', views.user, name='user'),
    path('<str:username>/<str:title>', views.post, name='post'),
]