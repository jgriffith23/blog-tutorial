# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-18 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_graf',
            field=models.TextField(blank=True),
        ),
    ]
