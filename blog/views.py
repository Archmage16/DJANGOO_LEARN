from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from blog.models import Prof, Post, Tag
# Create your views here.
def index(req):
    users = User.objects.all()
    p = Post.objects.all()
    cont = {
        "posts": p,
        "users": users,
    }
    return render(req,'blog/index.html', cont)

def user(req, username):
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

def post(req, username, title):
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
    