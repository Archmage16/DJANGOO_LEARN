from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# Create your models here.
from datetime import datetime

def get_timestamp_path(instance, filename):
    return f'cvs/{datetime.now().timestamp()}_{filename}'


class UserProfile(AbstractUser):
    bio = models.TextField(blank=True)
    location = models.CharField(max_length = 100,blank=True)
    date = models.DateField(null = True,blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    cv = models.FileField(upload_to=get_timestamp_path, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )