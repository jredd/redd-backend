from __future__ import absolute_import

from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'date_joined',
            'is_superuser',
            'salary',
            'wage',
            'current_assignments',
            'departments',
            'projects',
            'avatar'
                  # 'groups',
        )


class UserDealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('mserver_path',
                  'name',
        )
