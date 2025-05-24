from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prof(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Prof, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name='tags')
    def __str__(self) -> str:
        return f"{self.name}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Comment by {self.author.username} on {self.post.title}"
    