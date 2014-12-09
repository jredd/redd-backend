from __future__ import absolute_import

from rest_framework import serializers

from . import models


class AssetSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField()
    # project = serializers.PrimaryKeyRelatedField(many=True)
    # current_department = serializers.StringRelatedField(many=True)

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
