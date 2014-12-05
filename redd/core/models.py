from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

from redd import settings
from user_auth.models import CustomUser


class Project(models.Model):
    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_creator', verbose_name='Owner')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Department(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='department_creator', verbose_name='Owner')
    project = models.ManyToManyField(Project, verbose_name="list of projects")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name