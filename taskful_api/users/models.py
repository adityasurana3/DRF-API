from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import os
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from house.models import House

@deconstructible
class GenerateProfileImagePath(object):
    def __init__(self):
        pass
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f"media/accounts/{instance.user.id}/images"
        name = f"profile_image.{ext}"
        return os.path.join(path, name) 

user_profile_imag_path = GenerateProfileImagePath()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_imag_path, blank=True, null=True)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, blank=True, null=True, related_name='members')

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        username = f"{instance.first_name}_{instance.last_name}".lower()
        counter = 1
        while User.objects.filter(username=username):
            username = f"{instance.first_name}_{instance.last_name}_{counter}".lower()
            counter += 1

        instance.username = username
