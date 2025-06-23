from django.contrib import admin
from cars import models
# Register your models here.

admin.site.register(models.Spare)
admin.site.register(models.Machine)
admin.site.register(models.Kit)
