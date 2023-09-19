from rest_framework import viewsets, mixins, filters
from .models import Task, TaskList, Attachment, COMPLETE, NOT_COMPLETE
from rest_framework import status as st
from rest_framework.response import Response
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer
from .permissions import IsAllowedToEditTaskListElseNone, IsAllowedToEditTaskElseNone, IsAllowedToEditAttachmentElseNone
from rest_framework.decorators import action
from django.utils import timezone
from django_filters.rest_framework.backends import DjangoFilterBackend


class TaskListViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAllowedToEditTaskListElseNone]
    

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAllowedToEditTaskElseNone]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['points', 'completed_tasks_count', 'notcompleted_tasks_count']
    filterset_fields = ['status', ]
    
    def get_queryset(self):
        queryset =  super(TaskViewSet, self).get_queryset()
        user_profile = self.request.user.profile
        updated_queryset = queryset.filter(created_by=user_profile)
        return updated_queryset
    
    @action(detail=True, methods=['patch'])
    def update_atsk_status(self, request, pk=None):
        try:
            task = self.get_object()
            profile = request.user.profile
            status = request.data['status']
            if (status == NOT_COMPLETE):
                if (task.status == COMPLETE):
                    task.status = NOT_COMPLETE
                    task.created_at = None
                    task.created_by = None
                else:
                    raise Exception("Task is already marked as not complete")
            elif (status == COMPLETE):
                if (task.staus == NOT_COMPLETE):
                    task.status = COMPLETE
                    task.created_at = timezone.now()
                    task.created_by = profile
                else:
                    raise Exception("Task already marked complete")
            else:
                raise Exception("Incorrect status provided")
            task.save()
            serializer = TaskSerializer(instance=task, context={"request":request})
            return Response(serializer.data, status=st.HTTP_200_OK)
        except Exception as e:
            return Response({"detail":str(e)}, status=st.HTTP_400_BAD_REQUEST)
    
class AttachmentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAllowedToEditAttachmentElseNone]