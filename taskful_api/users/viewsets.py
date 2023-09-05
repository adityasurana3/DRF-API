from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .permissions import IsUserOwnerOrGetAndPostOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrGetAndPostOnly,]

