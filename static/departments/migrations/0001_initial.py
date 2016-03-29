# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-19 17:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, unique=True, verbose_name='name')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=500)),
                ('icon', models.ImageField(upload_to=b'')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_creator', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('project', models.ManyToManyField(to='projects.Project', verbose_name='list of projects')),
            ],
        ),
    ]
