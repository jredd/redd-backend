# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-19 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='current_project',
            field=models.ManyToManyField(to='projects.Project'),
        ),
    ]
