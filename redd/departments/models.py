from __future__ import unicode_literals

from django.db import models

from redd import settings
from projects.models import Project


 # name  = CharField
 #    date_created = DateTimeField
 #    is_active = BooleanField
 #    created_by = ForeignKey(CustomeUser)
 #    projec(s)t =ManyToManyField(Can belong to many projects)
 #    description = CharField
 #    icon=ImageField

class Department(models.Model):

    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='department_creator', verbose_name='Owner')
    project = models.ManyToManyField(Project, verbose_name="list of projects")
    description = models.CharField()
    icon = models.ImageField()


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name