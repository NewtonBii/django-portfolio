# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20180118_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='article_image',
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(null=True, upload_to='projects/'),
        ),
    ]
