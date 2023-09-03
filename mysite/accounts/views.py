from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth import get_user_model
from .serializers import UserSerializer


User = get_user_model()


class UserViewSet(ModelViewSet):
    # only admin has access to this viewset
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer