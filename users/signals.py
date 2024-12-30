from django.db.models.signals import post_save       #sender --------> this is signal
from django.contrib.auth.models import User          #By using this we perform functions...
from django.dispatch import receiver                 #reciever
from .models import Profile

@receiver(post_save,sender=User)     #it works ------> when the user is registered after the data is saved in database by forms.save() so that we use post_save
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)             #creating the profile

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    try:
        instance.profile.save()                               #saving the profile for the registered user..
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)

#after that setup in apps.py file
