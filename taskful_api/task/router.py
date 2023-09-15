from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register('tasklists', viewsets.TaskListViewSet)