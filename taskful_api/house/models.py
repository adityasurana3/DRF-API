from typing import Any
from django.db import models
from django.utils.deconstruct import deconstructible
import os
import uuid

@deconstructible
class GenerateProfileImagePath(object):
    def __init__(self) -> None:
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f"media/houses/{instance.id}/images"
        name = f"main.{ext}"
        return os.path.join(path, name) 

house_image_path = GenerateProfileImagePath()

# Create your models here.
class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=house_image_path, blank=True, null=True)
    description = models.TextField()
    manager = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='managed_house')
    point = models.IntegerField(default=0)
    completed_tasks_count = models.IntegerField(default=0)
    not_completed_tasks_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.id} | {self.name}'
