from rest_framework import viewsets, mixins
from .models import Task, TaskList, Attachment
from .serializers import TaskListSerializer
from .permissions import IsAllowedToEditTaskListElseNone

class TaskListViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAllowedToEditTaskListElseNone]