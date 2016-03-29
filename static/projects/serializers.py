from __future__ import absolute_import

from rest_framework import serializers

from . import models


class ProjectSerializers(serializers.ModelSerializer):

    class Meta:

        model = models.Project
        # name = serializers.CharField()
        fields = (
            'id',
            'name',
            'date_created',
            'is_active',
            'created_by',
            'icon',
            'current_client',
        )
