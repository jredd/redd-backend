# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=b''),
        ),
    ]