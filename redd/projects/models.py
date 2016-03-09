from __future__ import unicode_literals

from redd import settings
from django.db import models


# name = CharField
#     date_created = DateTimeField
#     is_active =BooleanField
#     created_by =ForeignKey(CustomeUser)
#     client = CharField
#     icon=ImageField


class Project(models.Model):
    name = models.CharField('name', max_length=80, unique=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_creator', verbose_name='Owner')
    client = models.CharField
    icon = models.ImageField

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name