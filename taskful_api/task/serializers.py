from rest_framework import serializers
from .models import Task, TaskList, Attachment
from house.models import House

class TaskListSerializer(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many=False, view_name='house-detail')
    status = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='profile-detail')
    class Meta:
        model = TaskList
        fields = ['url','id', 'name', 'description', 'status', 'created_at', 'created_by', 'house']
        read_only_fields = ['created_at', 'status']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'id', 'name', 'description']
        read_only_fields = []
        
class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = []
        read_only_fields = []