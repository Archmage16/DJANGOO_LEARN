from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from .models import Prof

def prof_create(sender, instance, created, **kwargs):
    if created:
        Prof.objects.create(user=instance)
        print(f'Профиль создан для пользователя: {instance.username}')
    else:
        instance.prof.save()
        print(f'Профиль обновлён для пользователя: {instance.username}')

def prof_delete(sender, instance, **kwargs):
     print(f"⚠️ Удаление профиля: {instance.user.username}")


post_save.connect(prof_create, sender=User)
pre_delete.connect(prof_delete, sender=Prof)
