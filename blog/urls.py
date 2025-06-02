from django.urls import path, reverse_lazy

from .apps import BlogConfig
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, \
    PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView

app_name = BlogConfig.name
urlpatterns = [
    path('', views.index, name='index'),
    
    path('login/', LoginView.as_view(template_name='blog/reg/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/reg/logout.html'), name='logout'),
    
    path('password_change/', PasswordChangeView.as_view(template_name = 'blog/reg/psc.html', success_url = reverse_lazy('blog:password_change_done')), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name = 'blog/reg/pscd.html'), name='password_change_done'),
    
    path('password_reset/', PasswordResetView.as_view(template_name = 'blog/reg/reset_pass.html', success_url = reverse_lazy('blog:password_reset_done'), 
                                                      subject_template_name = 'blog/reg/reset_email.txt', email_template_name = 'blog/reg/password_reset_email.html'), name='password_reset'),
    path('reset_done', PasswordResetDoneView.as_view(template_name = 'blog/reg/reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url = reverse_lazy("blog:reset_complete")), name='password_reset_confirm'),
    path('reset_complete', PasswordResetCompleteView.as_view(), name='reset_complete'),


    path('tagForm/', views.tagForm, name='tagForm'),
    path('postForm/', views.postForm, name='postForm'),  
    path('profForm/', views.profForm, name='profForm'),
    path('commentForm/', views.commentForm, name='commentForm'),    
    
    path('postComment/<str:username>/<str:title>/', views.postComment, name='postComment'),
    path('<str:username>/', views.user, name='user'),
    path('<str:username>/<str:title>', views.post, name='post'),
]