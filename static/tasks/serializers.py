from __future__ import absolute_import

from rest_framework import serializers

from . import models


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        fields = (
            'id',
            'name',
            'date_created',
            'date_assigned',
            'is_active',
            'created_by',
            'project',
            'department',
            'description',
            'assigned_users',
            'date_completed',
            'notes',
            'assigned_assets',
            'assigned_sub_assets',
        )
