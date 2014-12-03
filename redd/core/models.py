from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date joined', default=timezone.now)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='artist', verbose_name='Owner')


class Department(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', default=timezone.now)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='artist', verbose_name='Owner')
    project = models.ManyToManyField(Project)