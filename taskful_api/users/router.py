from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, ProfileViewSet

app_name = "users"

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)