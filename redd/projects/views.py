from __future__ import absolute_import

from rest_framework import generics
from rest_framework import permissions

from redd import settings
from . import models
from . import serializers


class ProjectList(generics.ListCreateAPIView):

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializers
    permission_classes = (permissions.IsAuthenticated,)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializers
    permission_classes = (permissions.IsAuthenticated,)
