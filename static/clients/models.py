from __future__ import unicode_literals

from django.db import models

from projects.models import Project


class Client(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    # created_by = models.ForeignKey(CustomUser, related_name='asset_creator', verbose_name='Owner')
    current_project = models.ManyToManyField(Project, )
    # account_manager =
    description = models.CharField('description', max_length=150)
    address = models.CharField('address', max_length=40)
    state = models.CharField('state', max_length=2)
    zip = models.CharField('zip', max_length=5)
    city = models.CharField('city', max_length=20)
    is_active = models.BooleanField(default=True)

