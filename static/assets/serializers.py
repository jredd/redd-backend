from __future__ import absolute_import

from rest_framework import serializers

from . import models


class AssetSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id',
            'name',
            'date_created',
            'created_by',
            'project',
            'current_department',

        )


class SubAssetSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SubAsset
        fields = (
            'id',
            'name',
            'date_created',
            'last_modified',
            'created_by',
            'check_out',
            'current_checked_out_user'
            'project',
            'location',
            'current_department',
        )
