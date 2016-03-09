from __future__ import unicode_literals

from django.db import models

from projects.models import Project
from departments.models import Department
# Task
#     name = CharField
#     assigned_user = ForeignKey(CustomUser)
#     assigned_by = ForeignKey(CustomUser)
#     date_assigned = DateField
#     date_completed = DateField
#     feed_back = CharField
#     Description = CharField
#     assigned_assets = ManyToMany(many tasks can be assigned to many assets)
#     assigned_sub_assets = ManyToMany


class Task(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_assigned = models.DateTimeField('date assigned', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task_creator', verbose_name='Owner')
    project = models.ForeignKey(Project, verbose_name="list of projects")
    department = models.ForeignKey(Department, '')
    description = models.CharField()
    assigned_users = models.ManyToManyRel()
    date_completed = models.DateTimeField('date completed')
    notes = models.CharField()
    assigned_assets = models.ManyToManyRel()
    assigned_sub_assets = models.ManyToManyRel()


