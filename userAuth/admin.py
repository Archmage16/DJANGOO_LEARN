from django.contrib import admin
from userAuth import models
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(models.UserProfile)
class UserAdminProf(UserAdmin):
    # admin.site.register(models.UserProfile)
    fieldsets = UserAdmin.fieldsets + (
        ("AddInfo", 
            {'fields': ('bio', 'location', 'date', 'cv', 'avatar'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("AddInfo", 
            {'fields': ('bio', 'location', 'date', 'cv', 'avatar'),
        }),
    )
    pass
