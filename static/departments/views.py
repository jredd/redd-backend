from __future__ import absolute_import

from rest_framework import generics
from rest_framework import permissions

from redd import settings
from . import serializers
from . import models


class DepartmentList(generics.ListCreateAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializers
    permission_classes = (permissions.IsAuthenticated,)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializers
    permission_classes = (permissions.IsAuthenticated,)
