from __future__ import absolute_import

from rest_framework import serializers

from . import models


class ProjectSerializers(serializers.ModelSerializer):

    class Meta:

        model = models.Project
        current_client = serializers.CharField(required=False)
        fields = (
            'id',
            'name',
            'date_created',
            'is_active',
            'created_by',
            'icon',
            # 'current_client',
        )
