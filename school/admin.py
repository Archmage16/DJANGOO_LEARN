from django.contrib import admin
from school import models


# Register your models here.

admin.site.register(models.Employee)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.OrderedStudent)