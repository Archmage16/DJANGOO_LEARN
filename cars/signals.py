# from django.db.models.signals import pre_init, post_init, post_save, pre_save
# from django.core.signals import request_started, request_finished
from .models import Spare
from django.db.models.signals import post_save, post_delete
import django.dispatch

have_10_spares = django.dispatch.Signal()

def spare_created_handler(sender, instance, created, **kwargs):
    if created:
        print(f'New spare created:{instance}')
    else:
        print(f'Spare updated:{instance}')
    
def spare_deleted_handler(sender, instance, created, **kwargs):
    print(f'Spare deleted:{instance}')

def spare_lim_handler(sender,**kwargs):
    if Spare.objects.count() >=10:
        print("There are 10 or more")
    else:
        print('There are less than 10')

post_save.connect(spare_created_handler,sender=Spare)
post_delete.connect(spare_deleted_handler,sender=Spare)
have_10_spares.connect(spare_lim_handler, sender = Spare)



# def before_dispatcher(sender, **kwargs):
#     instance = kwargs.get('instance')

#     print(f'{sender.__name__} with kwargs: {kwargs}')
#     print(f'{instance}')
    
# def after_dispatcher(sender, **kwargs):
#     instance = kwargs.get('instance')

#     print(f'{sender.__name__} with kwargs: {kwargs}')
#     print(f'{instance}')
# # pre_init.connect(receiver=base_dispatcher, sender=Spare,dispatch_uid='base_dispatcher_signal')
# # post_init.connect(receiver=base_dispatcher, sender=Spare, dispatch_uid='base_dispatcher_signal_post')
# pre_save.connect(receiver=before_dispatcher, sender=Spare)
# post_save.connect(receiver=after_dispatcher, sender=Spare)





# def request_start(sender, **kwargs):
#     instance = kwargs.get('instance')

#     print(f'Work started {sender.__name__}')
#     print(f'{instance}')

# def request_finish(sender, **kwargs):
#     instance = kwargs.get('instance')

#     print(f'Work finished {sender.__name__}')
#     print(f'{instance}')

# request_started.connect(receiver=request_start)
# request_finished.connect(receiver=request_finish)