from django.contrib import admin
from .models import Task, TaskList, Attachment

# Register your models here.

class TaskListAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created_at']
    
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created_at']

class AttachmentAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created_at']

admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Attachment, AttachmentAdmin)