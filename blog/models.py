from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# Create your models here.

class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-created_time')
    def order_by_author(self):
        return super().get_queryset().order_by('author__user__username')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')
    
    def __str__(self) -> str:
        return f"{self.user.username} likes"
    
class Prof(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    like = GenericRelation(Like)

    def __str__(self) -> str:
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Prof, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)

    like = GenericRelation(Like)
    objects = PostManager()

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    like = GenericRelation(Like)
    posts = models.ManyToManyField(Post, related_name='tags')
    def __str__(self) -> str:
        return f"{self.name}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    like = GenericRelation(Like)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Comment by {self.author.username} on {self.post.title}"
    
#1
class Message(models.Model):
    content = models.TextField()

class Privete(Message):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'private_message')
#2
class Message2(models.Model):
    content = models.TextField()
    class Meta:
        abstract = True

class Privete2(Message2):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'private_message2')


#3
class PostOrdering(Post):
    class Meta:
        proxy = True
        verbose_name = 'Ordered Post'
        ordering = ['-created_time']