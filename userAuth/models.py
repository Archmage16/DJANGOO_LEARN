from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# Create your models here.




class UserProfile(AbstractUser):
    bio = models.TextField(blank=True)
    location = models.CharField(max_length = 100,blank=True)
    date = models.DateField(null = True,blank=True)

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