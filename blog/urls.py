from django.urls import path, reverse_lazy

from .apps import BlogConfig
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView,PasswordChangeView

app_name = BlogConfig.name
urlpatterns = [
    path('', views.index, name='index'),
    
    path('login/', LoginView.as_view(template_name='blog/reg/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/reg/logout.html'), name='logout'),
    
    path('password_change/', PasswordChangeView.as_view(template_name = 'blog/reg/psc.html', success_url = reverse_lazy('blog:password_change_done')), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name = 'blog/reg/pscd.html'), name='password_change_done'),
    
    
    path('tagForm/', views.tagForm, name='tagForm'),
    path('postForm/', views.postForm, name='postForm'),  
    path('profForm/', views.profForm, name='profForm'),
    path('commentForm/', views.commentForm, name='commentForm'),    
    
    path('postComment/<str:username>/<str:title>/', views.postComment, name='postComment'),
    path('<str:username>/', views.user, name='user'),
    path('<str:username>/<str:title>', views.post, name='post'),
]