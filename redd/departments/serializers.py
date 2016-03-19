from __future__ import absolute_import

from rest_framework import serializers

from . import models


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = (
            'id',
            'name',
            'date_created',
            'is_active',
            'created_by',
            'project',
            'description',
            'icon'
        )
