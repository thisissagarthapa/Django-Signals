
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import  pre_init,pre_save,pre_delete,post_init,post_save,post_delete
from django.core.signals import request_finished,request_started,got_request_exception
from django.db.models.signals import pre_migrate, post_migrate

from django.db.backends.signals import connection_created
from django.db import connections

@receiver(user_logged_in,sender=User)
def login_success(sender, request, user, **kwargs):
    print('---------------------')
    print('Logged-in signals ....Run-Intro....')
    print('Sender:', sender)
    print('request:', request)
    print('User:', user)
    print(f'kwargs: {kwargs}')

print('Connecting login_success signal handler')
# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out,sender=User)
def logout_success(sender, request, user, **kwargs):
    print('---------------------')
    print('Logged-out signals ....Run-Intro....')
    print('Sender:', sender)
    print('request:', request)
    print('User:', user)
    print(f'kwargs: {kwargs}')

print('Connecting logout_success signal handler')
# user_logged_out.connect(logout_success, sender=User)


@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print('---------------------')
    print('Login failed signals ....Run-Intro....')
    print('Sender:', sender)
    print('credentials:', credentials)
    print('request:', request)
    print(f'kwargs: {kwargs}')
    
print('Connecting login_failed signal handler')
# user_login_failed.connect(login_failed)

@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print('---------------------')
    print('Pre Save signals ')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
    
# pre_save.connect(at_beginning_save,sender=User)



@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print('---------------------')
        print('post Save signals ')
        print('new record')
        print('Sender:', sender)
        print('Instance:', instance)
        print('Created:', created)
        print(f'kwargs: {kwargs}')
    else:
        print('---------------------')
        print('post Save signals ')
        print('updated')
        print('Sender:', sender)
        print('Instance:', instance)
        print('Created:', created)
        print(f'kwargs: {kwargs}')
        
# post_save.connect(at_ending_save,sender=User)


@receiver(pre_delete,sender=User)
def at_beginning_delete(sender,instance,**kwargs):
    print('---------------------')
    print('Pre delete signals ')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
    
# pre_delete.connect(at_beginning_delete,sender=User)


@receiver(post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print('---------------------')
    print('post delete signals ')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
    
# post_delete.connect(at_ending_delete,sender=User)


@receiver(pre_init,sender=User)
def at_beginning_init(sender,*args,**kwargs):
    print('---------------------')
    print('pre init signals ')
    print('Sender:', sender)
    print(f'Args:{args}')
    print(f'kwargs: {kwargs}')
    
# pre_init.connect(at_beginning_init,sender=User)


@receiver(post_init,sender=User)
def at_ending_init(sender,*args,**kwargs):
    print('---------------------')
    print('post init signals ')
    print('Sender:', sender)
    print(f'Args:{args}')
    print(f'kwargs: {kwargs}')
    
# post_init.connect(at_ending_init,sender=User)



@receiver(request_started)
def at_beginning_request(sender,environ,**kwargs):
    print('---------------------')
    print('At Beginning signals ')
    print('Sender:', sender)
    print('Environ:',environ)
    print(f'kwargs: {kwargs}')
    
# request_started.connect(at_beginning_request)



@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print('---------------------')
    print('At ending signals ')
    print('Sender:', sender)
    print(f'kwargs: {kwargs}')
    
# request_finished.connect(at_ending_request)


@receiver(got_request_exception)
def at_req_exception(sender,request,**kwargs):
    print('---------------------')
    print('At req Exception signals ')
    print('Sender:', sender)
    print('Request:', request)
    print(f'kwargs: {kwargs}')
    
# got_request_exception.connect(at_req_exception)




def pre_migrate_handler(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('---------------------')
    print('Pre-migrate signals ....Run-Intro....')
    print('sender:', sender)
    print('app_config:', app_config)
    print('verbosity:', verbosity)
    print('interactive:', interactive)
    print('using:', using)
    print('plan:', plan)
    print('apps:', apps)
    print(f'kwargs: {kwargs}')
    
print('Connecting pre_migrate signal handler')
pre_migrate.connect(pre_migrate_handler)

def post_migrate_handler(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('---------------------')
    print('Post-migrate signals ....Run-Intro....')
    print('sender:', sender)
    print('app_config:', app_config)
    print('verbosity:', verbosity)
    print('interactive:', interactive)
    print('using:', using)
    print('plan:', plan)
    print('apps:', apps)
    print(f'kwargs: {kwargs}')
print('Connecting post_migrate signal handler')
post_migrate.connect(post_migrate_handler)





def connection_created_handler(sender, connection, **kwargs):
    print('---------------------')
    print('Database connection created ....Run-Intro....')
    print('sender:', sender)
    print('connection:', connection)
    print(f'kwargs: {kwargs}')

print('Connecting connection_created signal handler')
connection_created.connect(connection_created_handler)