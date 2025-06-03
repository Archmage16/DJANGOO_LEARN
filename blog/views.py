from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.views import redirect_to_login
from blog.models import Prof, Post, Tag
from blog.forms import TagModelForm, PostModelForm, ProfModelForm, CommentModelForm

# Create your views here.
@login_required()
def index(req):
    users = User.objects.all()
    user = req.user
    p = Post.objects.all()
    cont = {
        "posts": p,
        "users": users,
        "user": user,
    }
    return render(req,'blog/index.html', cont)


def myauth(req):
    if req.user.is_authenticated:
        mess = 'User is login'
    else:
        mess = "User isn't login"
    return HttpResponse(mess)




def user(req, username):
    if req.user.is_authenticated:
        print(1)
        try:
            user = User.objects.get(username=username)
            prof = Prof.objects.get(user=user)
            posts = Post.objects.filter(author=prof)
            tags = Tag.objects.all()
            cont = {
                "user": user,
                "prof": prof,
                "posts": posts,
                "tags": tags,
            }
            return render(req, 'blog/user.html', cont)
        except Prof.DoesNotExist:
            return HttpResponse("I can't find this user")
    else:
        return redirect('blog:login')
    
    
def post(req, username, title):
    if req.user.is_authenticated:
        try:
            user = User.objects.get(username=username)
            prof = Prof.objects.get(user=user)
            post = Post.objects.get(title=title, author=prof)
            tags = Tag.objects.all()
            cont = {
                "user": user,
                "prof": prof,
                "post": post,
                "tags": tags,
            }
            return render(req, 'blog/post.html', cont)
        except Post.DoesNotExist:
            return HttpResponse("I can't find this post")
    else:
        return redirect('blog:login')
    
def postComment(req, username, title):
    if req.user.is_authenticated:
        try:
            user = User.objects.get(username=username)
            prof = Prof.objects.get(user=user)
            post = Post.objects.get(title=title, author=prof)
            tags = Tag.objects.all()
            cont = {
                "user": user,
                "prof": prof,
                "post": post,
                "tags": tags,
                'comments': post.comments.all(),
            }
            return render(req, 'blog/comments.html', cont)
        except Post.DoesNotExist:
            return HttpResponse("I can't find this post")
    else:
        return redirect('blog:login')


def postForm(req):
    if req.method == 'POST':
        form = PostModelForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Post created successfully")
    else:
        form = PostModelForm()
        return render(req, 'blog/forms/postForm.html', {'form': form})

def profForm(req):
    if req.method == "POST":
        form = ProfModelForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Profile created successfully")
    else:
        form = ProfModelForm()
        return render(req, 'blog/forms/prof_form.html', {'form': form})

def tagForm(req):
    if req.method == 'POST':
        form = TagModelForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Tag created successfully")
    else:
        form = TagModelForm()
        return render(req, 'blog/forms/tag_form.html', {'form': form})
    
def commentForm(req):
    if req.method == 'POST':
        form = CommentModelForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Comment created successfully <a href='/blog'>Go back</a>")
        
    else:
        form = CommentModelForm()
        return render(req, 'blog/forms/commentForm.html', {'form': form})
    