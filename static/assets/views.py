from __future__ import absolute_import

from rest_framework import generics
from rest_framework import permissions

from redd import settings
from . import serializers
from . import models


class AssetsList(generics.ListCreateAPIView):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializers
    permission_classes = (permissions.IsAuthenticated,)


class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Asset.objects.all()
    serializer_class = serializers.AssetSerializers
    permission_classes = (permissions.IsAuthenticated,)


class SubAssetsList(generics.ListCreateAPIView):
    queryset = models.SubAsset.objects.all()
    serializer_class = serializers.SubAssetSerializers
    permission_classes = (permissions.IsAuthenticated,)


class SubAssetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SubAsset.objects.all()
    serializer_class = serializers.SubAssetSerializers
    permission_classes = (permissions.IsAuthenticated,)
