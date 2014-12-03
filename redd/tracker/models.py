from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from core import models as core


class Asset(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', default=timezone.now)
    created_by = models.ForeignKey(User, related_name='artist', verbose_name='Owner')
    project = models.ForeignKey(core.Project)
    current_department = models.ForeignKey(core.Department)


class SubAsset(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', default=timezone.now)
    last_modified = models.DateTimeField('date modified', default=timezone.now)
    created_by = models.ForeignKey(User, related_name='artist', verbose_name='Owner')
    parent_asset = models.ForeignKey(Asset)
    checked_out = models.BooleanField(default=False)
    current_checked_out_user = models.ForeignKey(User, related_name='artist', verbose_name='temp-owner')
    location = models.FilePathField(allow_folders=False)
    type = models.CharField()
    current_department = models.ForeignKey(core.Department)
