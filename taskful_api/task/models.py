from typing import Any
from django.db import models
from house.models import House
import uuid
import os
from django.utils.deconstruct import deconstructible
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.

NOT_COMPLETE = 'NC'
COMPLETE = 'C'
TASK_STATUS_CHOICES =(
    (NOT_COMPLETE, 'Not Completed'),
    (COMPLETE, 'Complete')
)

@deconstructible
class GenerateAttachmentFilePath(object):
    
    def __init__(self):
        pass
    
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f"media/tasks/{instance.task.id}/attachments"
        name = f"{instance.id}.{ext}"
        return os.path.join(path, name)

attachment_file_path = GenerateAttachmentFilePath()
        
class TaskList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    compleated_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('users.Profile', null=True, blank=True, on_delete=models.SET_NULL, related_name='lists')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default=NOT_COMPLETE)
    
    def __str__(self):
        return f'{self.id} | {self.name}'


class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    compleated_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('users.Profile', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_tasks')
    completed_by = models.ForeignKey('users.Profile', null=True, blank=True, on_delete=models.SET_NULL, related_name='completed_tasks')
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default=NOT_COMPLETE)
    
    def __str__(self):
        return f'{self.id} | {self.name}'

class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.FileField(upload_to=attachment_file_path)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    
    def __str__(self) -> str:
        return f"{self.id} | {self.task}"
    

# Signals

@receiver(post_save, sender=Task)
def update_house_point(sender, instance, created, **kwargs):
    house = instance.task_list.house
    if instance.status == COMPLETE:
        house.point += 10
    elif instance.statud == NOT_COMPLETE:
        if house.status > 10:
            house.point -= 10
    house.save()
    
@receiver(post_save, sender=Task)
def update_tasklist_status(sender, instance, created, **kwargs):
    task_list = instance.task_list
    is_complete = True
    for task in task_list.tasks.all():
        if task.status != COMPLETE:
            is_complete = False
            break
    task_list.status = COMPLETE if is_complete else NOT_COMPLETE
    task_list.save()