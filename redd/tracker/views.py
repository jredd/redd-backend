from __future__ import absolute_import

from rest_framework import generics
from rest_framework import permissions

from . import models
from . import serializers


class AssetList(generics.ListCreateAPIView):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializer
    permission_classes = (permissions.IsAuthenticated,)
