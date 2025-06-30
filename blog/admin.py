from django.contrib import admin
from blog import models
# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Prof)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(models.Like)
admin.site.register(models.Message)
admin.site.register(models.Privete)
admin.site.register(models.Privete2)

