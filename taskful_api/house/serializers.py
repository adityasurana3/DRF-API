from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = House
        fields = ['url','id','name','image','description','manager','point','completed_tasks_count','not_completed_tasks_count','created_at','updated_at']
        read_only_fields = ['point','completed_tasks_count','not_completed_tasks_count']
        