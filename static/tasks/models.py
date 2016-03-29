from __future__ import unicode_literals

from django.db import models

from projects.models import Project
from departments.models import Department
from redd.settings import AUTH_USER_MODEL as User

from assets.models import Asset, SubAsset


class Task(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_assigned = models.DateTimeField('date assigned', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='task_creator', verbose_name='Owner')
    project = models.ForeignKey(Project, verbose_name="list of projects")
    department = models.ForeignKey(Department, related_name='department', verbose_name='Department')
    description = models.CharField(max_length=500)
    assigned_users = models.ManyToManyField(User, verbose_name=('assigned user'), blank=True)
    date_completed = models.DateTimeField('date completed')
    notes = models.CharField(max_length=800)
    assigned_assets = models.ManyToManyField(Asset)
    assigned_sub_assets = models.ManyToManyField(SubAsset)
