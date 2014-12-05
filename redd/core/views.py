from __future__ import absolute_import

from rest_framework import generics
from rest_framework import permissions

from redd import settings
from . import models
from . import serializers


class ProjectList(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DepartmentList(generics.ListCreateAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # serializer_class = serializers.DepartmentSerializer(queryset, many=True)

    # def get_queryset(self):
    #     print self.kwargs
    #     name = self.kwargs['name']
    #     owner = self.kwargs['owner']
    #     project = self.kwargs['project']
    #
    #     print name, owner, project
    #
    #     return models.Department.objects.all()