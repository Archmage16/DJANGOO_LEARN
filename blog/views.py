from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.views import redirect_to_login
from blog.models import Prof, Post, Tag
from blog.forms import TagModelForm, PostModelForm, ProfModelForm, CommentModelForm



# Create your views here.
# @login_required()
# def index(req):
#     users = User.objects.all()
#     user = req.user
#     p = list(Post.objects.all())
#     revers_only5 = p[::-1][:5]  
#     cont = {
#         "posts": p,
#         "users": users,
#         "user": user,
#         "rever_posts": revers_only5,
#     }
#     return render(req,'blog/index.html', cont)

class IndexView(TemplateView):
    template_name = 'blog/index.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all()
        context['user'] = self.request.user
        context['rever_posts'] = list(Post.objects.all())[::-1][:5]
        return context


def myauth(req):
    if req.user.is_authenticated:
        mess = 'User is login'
    else:
        mess = "User isn't login"
    return HttpResponse(mess)




# def user(req, username):
#     if req.user.is_authenticated:
#         print(1)
#         try:
#             user = User.objects.get(username=username)
#             prof = Prof.objects.get(user=user)
#             posts = Post.objects.filter(author=prof)
#             tags = Tag.objects.all()
#             cont = {
#                 "user": user,
#                 "prof": prof,
#                 "posts": posts,
#                 "tags": tags,
#             }
#             return render(req, 'blog/user.html', cont)
#         except Prof.DoesNotExist:
#             return HttpResponse("I can't find this user")
#     else:
#         return redirect('blog:login')
 
# def post(req, username, title):
#     if req.user.is_authenticated:
#         try:
#             user = User.objects.get(username=username)
#             prof = Prof.objects.get(user=user)
#             post = Post.objects.get(title=title, author=prof)
#             tags = Tag.objects.all()
#             cont = {
#                 "user": user,
#                 "prof": prof,
#                 "post": post,
#                 "tags": tags,
#             }
#             return render(req, 'blog/post.html', cont)
#         except Post.DoesNotExist:
#             return HttpResponse("I can't find this post")
#     else:
#         return redirect('blog:login')

# def postComment(req, username, title):
#     if req.user.is_authenticated:
#         try:
#             user = User.objects.get(username=username)
#             prof = Prof.objects.get(user=user)
#             post = Post.objects.get(title=title, author=prof)
#             tags = Tag.objects.all()
#             cont = {
#                 "user": user,
#                 "prof": prof,
#                 "post": post,
#                 "tags": tags,
#                 'comments': post.comments.all(),
#             }
#             return render(req, 'blog/comments.html', cont)
#         except Post.DoesNotExist:
#             return HttpResponse("I can't find this post")
#     else:
#         return redirect('blog:login')

class UserProfileView(LoginRequiredMixin, DetailView):
    model = Prof
    template_name = 'blog/user.html'
    # pk_url_kwarg = 'user__username'
    slug_url_kwarg = 'username'
    slug_field = 'user__username'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']

        try:
            user = User.objects.get(username=username)
            prof = Prof.objects.get(user=user)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")        
        
        posts = Post.objects.filter(author=prof)

        context['user'] = user
        context['prof'] = prof
        context['posts'] = posts
        context['tags'] = Tag.objects.all()
        return context


    

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post.html'
    
    context_object_name = 'post'
    def get_object(self):
        username = self.kwargs['username']
        title = self.kwargs['title']
        try:
            user = User.objects.get(username=username)
            prof = Prof.objects.get(user=user)
            post = Post.objects.get(title=title, author=prof)
            return post
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']
        
        try:
            user = User.objects.get(username=username)
            prof = Prof.objects.get(user=user)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
        
        context['user'] = user
        context['prof'] = prof
        context['tags'] = Tag.objects.all()
        return context 
    

class PostCommentsView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']
        title = self.kwargs['title']

        try:
            user = User.objects.get(username=username)
            prof = Prof.objects.get(user=user)
            post = Post.objects.get(title=title, author=prof)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

        context['user'] = user
        context['prof'] = prof
        context['post'] = post
        context['tags'] = Tag.objects.all()
        context['comments'] = post.comments.all()
        return context





# def postForm(req):
#     if req.method == 'POST':
#         form = PostModelForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Post created successfully")
#     else:
#         form = PostModelForm()
#         return render(req, 'blog/forms/postForm.html', {'form': form})

class PostFormView(LoginRequiredMixin, FormView):
    template_name = 'blog/forms/postForm.html'
    form_class = PostModelForm
    success_url = '/blog'  
    http_method_names = ['get', 'post']
    

    def form_valid(self, form):
        form.save()
        return HttpResponse("Post created successfully")
    

# def profForm(req):
#     if req.user.is_authenticated:
#         if req.method == 'POST':
#             form = ProfModelForm(req.POST, instance=req.user.prof)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponse("Profile updated successfully")
#         else:
#             form = ProfModelForm(instance=req.user.prof)
#             return render(req, 'blog/forms/profForm.html', {'form': form})
#     else:
#         return redirect('blog:login')

class ProfFormView(LoginRequiredMixin, FormView):
    template_name = 'blog/forms/prof_form.html'
    form_class = ProfModelForm
    success_url = '/blog'  
    http_method_names = ['get', 'post']
    
    def form_valid(self, form):
        form.save()
        return HttpResponse("Profile updated successfully")

# def tagForm(req):
#     if req.method == 'POST':
#         form = TagModelForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Tag created successfully")
#     else:
#         form = TagModelForm()
#         return render(req, 'blog/forms/tag_form.html', {'form': form})   


class TagFormView(LoginRequiredMixin, FormView):
    template_name = 'blog/forms/tag_form.html'
    form_class = TagModelForm
    success_url = '/blog'  
    http_method_names = ['get', 'post']
    
    def form_valid(self, form):
        form.save()
        return HttpResponse("Tag created successfully")


# def commentForm(req):
#     if req.method == 'POST':
#         form = CommentModelForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Comment created successfully <a href='/blog'>Go back</a>")
        
#     else:
#         form = CommentModelForm()
#         return render(req, 'blog/forms/commentForm.html', {'form': form})


class CommentFormView(LoginRequiredMixin, FormView):
    template_name = 'blog/forms/commentForm.html'
    form_class = CommentModelForm
    success_url = '/blog'  
    http_method_names = ['get', 'post']
    
    def form_valid(self, form):
        form.save()
        return HttpResponse("Comment created successfully <a href='/blog'>Go back</a>")