from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from ToDoApp_api import serializers
from ToDoApp_api import models
from ToDoApp_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'surname')

class TaskViewSet(viewsets.ModelViewSet):
    """Handles creating and updating tasks"""
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnTask,
        IsAuthenticated
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_email', 'title', 'description')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
