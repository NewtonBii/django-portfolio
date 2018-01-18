# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repo_link',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='web_link',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='article_image',
            field=models.ImageField(null=True, upload_to='articles/'),
        ),
    ]