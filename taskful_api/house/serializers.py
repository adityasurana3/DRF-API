from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    members_count = serializers.IntegerField(read_only=True)
    members = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='profile-detail')
    manager = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
    
    class Meta:
        model = House
        fields = ['url','id','name','image','description','manager','members_count','members','point','completed_tasks_count','not_completed_tasks_count','created_at','updated_at']
        read_only_fields = ['point','completed_tasks_count','not_completed_tasks_count']
        