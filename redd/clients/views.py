from __future__ import absolute_import

from rest_framework import generics
from rest_framework import permissions

from redd import settings
from . import serializers
from . import models


class ClientList(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializers
    permission_classes = (permissions.IsAuthenticated,)