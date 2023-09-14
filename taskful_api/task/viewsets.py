from rest_framework import viewsets, mixins
from .models import Task, TaskList, Attachment
from .serializers import TaskList
from .permissions import IsAllowedToEditTaskListElseNone

class TaskViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = TaskList.objects.all()
    serializer_class = TaskList
    permission_classes = [IsAllowedToEditTaskListElseNone]