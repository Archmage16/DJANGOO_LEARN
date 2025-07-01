from django.db.models.signals import pre_init, post_init, post_save, pre_save
from django.core.signals import request_started, request_finished
from .models import Spare

def before_dispatcher(sender, **kwargs):
    instance = kwargs.get('instance')

    print(f'{sender.__name__} with kwargs: {kwargs}')
    print(f'{instance}')
    
def after_dispatcher(sender, **kwargs):
    instance = kwargs.get('instance')

    print(f'{sender.__name__} with kwargs: {kwargs}')
    print(f'{instance}')
# pre_init.connect(receiver=base_dispatcher, sender=Spare,dispatch_uid='base_dispatcher_signal')
# post_init.connect(receiver=base_dispatcher, sender=Spare, dispatch_uid='base_dispatcher_signal_post')
pre_save.connect(receiver=before_dispatcher, sender=Spare)
post_save.connect(receiver=after_dispatcher, sender=Spare)





def request_start(sender, **kwargs):
    instance = kwargs.get('instance')

    print(f'Work started {sender.__name__}')
    print(f'{instance}')

def request_finish(sender, **kwargs):
    instance = kwargs.get('instance')

    print(f'Work finished {sender.__name__}')
    print(f'{instance}')

request_started.connect(receiver=request_start)
request_finished.connect(receiver=request_finish)