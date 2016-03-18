from __future__ import absolute_import

from rest_framework import serializers

from . import models


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = (
            'id',
            'name',
            'date_created',
            'is_active',
            'current_project',
            'address',
            'state',
            'zip',
            'city',
        )
