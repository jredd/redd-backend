from __future__ import unicode_literals

from django.db import models

from redd.settings import AUTH_USER_MODEL as User
from projects.models import Project
from departments.models import Department


class Asset(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='asset_creator', verbose_name='Owner')
    project = models.ForeignKey(Project)
    current_department = models.ManyToManyField(Department, verbose_name="list of departments")

    def __unicode__(self):
        return self.name


class SubAsset(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    last_modified = models.DateTimeField('date modified', auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='sub_asset_creator', verbose_name='Owner')
    parent_asset = models.ForeignKey(Asset)
    checked_out = models.BooleanField(default=False)
    current_checked_out_user = models.ForeignKey(User, related_name='temp_owner', verbose_name='temp-owner')
    location = models.FilePathField(allow_folders=False)
    # type = models.CharField()
    current_department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.name