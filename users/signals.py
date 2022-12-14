from django.db.models.signals import post_save #this signal is fired after an object is saved
from django.contrib.auth.models import User #we import the user to make the user the signal
from django.dispatch import receiver
from django.shortcuts import redirect
from .models import Profile

#the receiver decorater takes the signal and sender arguments
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#the receiver decorater takes the signal and sender arguments
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    return redirect('profile')
