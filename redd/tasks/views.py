from __future__ import absolute_import

from rest_framework import generics
from rest_framework import permissions

from redd import settings
from . import serializers
from . import models


class TaskList(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializers
    permission_classes = (permissions.IsAuthenticated,)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializers
    permission_classes = (permissions.IsAuthenticated,)
