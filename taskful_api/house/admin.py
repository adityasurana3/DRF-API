from django.contrib import admin
from .models import House

# Register your models here.

class HouseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in House._meta.get_fields()]

admin.site.register(House, HouseAdmin)
