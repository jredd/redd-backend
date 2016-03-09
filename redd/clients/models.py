from __future__ import unicode_literals

from django.db import models

from projects.models import Project


class Client(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    # created_by = models.ForeignKey(CustomUser, related_name='asset_creator', verbose_name='Owner')
    projects = models.ManyToOneRel(Project)
    # account_manager =
    description = models.CharField()
    address = models.CharField()
    state = models.CharField()
    zip = models.CharField()
    is_active = models.BooleanField()

